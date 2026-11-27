"""GitHub GraphQL-backed, append-only Runtime store.

This module persists PREPARE manifests on an operations branch and publishes
all domain targets plus a receipt/checkpoint in one expected-HEAD commit.
It is a backend adapter, not a GM/rules runtime.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable, Mapping


GRAPHQL_URL = "https://api.github.com/graphql"
_RESERVED_PREFIX = ".runtime/"
_CHECKPOINT_PATH = ".runtime/checkpoint.json"
_BATCH_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,119}$")
_OID_RE = re.compile(r"^[0-9a-f]{40}$")


class RuntimeStoreError(RuntimeError):
    """Base error for the GitHub Runtime store."""


class ConfigurationError(RuntimeStoreError):
    pass


class BranchNotFound(RuntimeStoreError):
    pass


class InvalidBatch(RuntimeStoreError):
    pass


class InvalidTargetPath(RuntimeStoreError):
    pass


class BatchConflict(RuntimeStoreError):
    pass


class StaleRevision(RuntimeStoreError):
    pass


class DisputedBatch(RuntimeStoreError):
    pass


class CommitOutcomeUnknown(RuntimeStoreError):
    """The mutation may have committed, but its result could not be proven."""


class GitHubGraphQLError(RuntimeStoreError):
    def __init__(self, errors: Any):
        self.errors = errors
        super().__init__("GitHub GraphQL request failed: " + json.dumps(errors, ensure_ascii=False))


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def fingerprint_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def fingerprint_text(value: str) -> str:
    return fingerprint_bytes(value.encode("utf-8"))


def _validate_branch(branch: str) -> None:
    if not isinstance(branch, str) or not branch or branch.startswith("/") or ":" in branch:
        raise ConfigurationError("branch must be a non-empty unqualified Git branch name")


def _validate_batch_id(batch_id: str) -> None:
    if not isinstance(batch_id, str) or not _BATCH_RE.fullmatch(batch_id):
        raise InvalidBatch("batch_id must be a stable path-safe identifier (1-120 chars)")


def _validate_target_path(path: str) -> None:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        raise InvalidTargetPath("target paths must be non-empty relative POSIX paths")
    parts = path.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise InvalidTargetPath("target path contains an unsafe component")
    if path.startswith(_RESERVED_PREFIX):
        raise InvalidTargetPath("target path uses the adapter-reserved .runtime/ namespace")


def _validate_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(manifest, Mapping):
        raise InvalidBatch("manifest must be an object")
    result = dict(manifest)
    required = {"batch_id", "base_revision", "target_revision", "base_head_oid", "target_fingerprints"}
    missing = required - set(result)
    if missing:
        raise InvalidBatch("manifest missing fields: " + ", ".join(sorted(missing)))
    _validate_batch_id(result["batch_id"])
    if not isinstance(result["base_revision"], (str, int)) or not isinstance(result["target_revision"], (str, int)):
        raise InvalidBatch("base_revision and target_revision must be strings or integers")
    if not _OID_RE.fullmatch(str(result["base_head_oid"])):
        raise InvalidBatch("base_head_oid must be a full 40-character commit SHA")
    fingerprints = result["target_fingerprints"]
    if not isinstance(fingerprints, dict) or not fingerprints:
        raise InvalidBatch("target_fingerprints must be a non-empty object")
    for path, digest in fingerprints.items():
        _validate_target_path(path)
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise InvalidBatch("each target fingerprint must be a SHA-256 hex digest")
    return result


class _UrllibGraphQLTransport:
    def __init__(self, token: str, timeout: float = 20.0):
        if not token:
            raise ConfigurationError("GITHUB_TOKEN is required")
        self.token = token
        self.timeout = timeout

    def __call__(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
        request = urllib.request.Request(
            GRAPHQL_URL,
            data=payload,
            headers={
                "Authorization": "Bearer " + self.token,
                "Content-Type": "application/json",
                "Accept": "application/vnd.github+json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = response.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise CommitOutcomeUnknown("GitHub request transport failed; reconcile before retrying") from exc
        try:
            decoded = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise RuntimeStoreError("GitHub returned a non-JSON GraphQL response") from exc
        if decoded.get("errors"):
            raise GitHubGraphQLError(decoded["errors"])
        if "data" not in decoded:
            raise RuntimeStoreError("GitHub GraphQL response did not contain data")
        return decoded["data"]


_READ_REF = """
query ReadRuntimeBranch($owner: String!, $name: String!, $qualifiedName: String!) {
  repository(owner: $owner, name: $name) {
    ref(qualifiedName: $qualifiedName) {
      target { ... on Commit { oid } }
    }
  }
}
"""

_READ_FILE = """
query ReadRuntimeFile($owner: String!, $name: String!, $expression: String!) {
  repository(owner: $owner, name: $name) {
    object(expression: $expression) {
      ... on Blob { oid text isTruncated }
    }
  }
}
"""

_FIND_RECEIPT_COMMIT = """
query FindRuntimeReceiptCommit($owner: String!, $name: String!, $qualifiedName: String!, $path: String!) {
  repository(owner: $owner, name: $name) {
    ref(qualifiedName: $qualifiedName) {
      target {
        ... on Commit {
          history(first: 100, path: $path) {
            nodes {
              oid
              parents(first: 2) { nodes { oid } }
            }
          }
        }
      }
    }
  }
}
"""

_CREATE_COMMIT = """
mutation CommitRuntimeBatch($input: CreateCommitOnBranchInput!) {
  createCommitOnBranch(input: $input) {
    commit { oid }
    ref { name target { ... on Commit { oid } } }
  }
}
"""


class GitHubGraphQLRuntimeStore:
    """GitHub-backed Runtime persistence for one Campaign/Run branch pair.

    The operations branch stores immutable PREPARE manifests.
    The runtime branch stores each publication as one atomic commit containing
    every target file, the checkpoint pointer, and an immutable receipt.

    Both branches must be provisioned before use. No branch creation, deletion,
    force-push, domain adjudication, or player delivery is performed here.
    """

    def __init__(
        self,
        repository: str,
        runtime_branch: str,
        operations_branch: str,
        token: str | None = None,
        transport: Callable[[str, dict[str, Any]], dict[str, Any]] | None = None,
    ):
        if not isinstance(repository, str) or repository.count("/") != 1:
            raise ConfigurationError("repository must be owner/name")
        self.owner, self.name = repository.split("/", 1)
        if not self.owner or not self.name:
            raise ConfigurationError("repository must be owner/name")
        _validate_branch(runtime_branch)
        _validate_branch(operations_branch)
        if runtime_branch == operations_branch:
            raise ConfigurationError("runtime and operations branches must be separate")
        self.runtime_branch = runtime_branch
        self.operations_branch = operations_branch
        if transport is None:
            transport = _UrllibGraphQLTransport(token or os.environ.get("GITHUB_TOKEN", ""))
        self._transport = transport

    def _graphql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        return self._transport(query, variables)

    def _read_ref(self, branch: str) -> str:
        data = self._graphql(_READ_REF, {
            "owner": self.owner,
            "name": self.name,
            "qualifiedName": "refs/heads/" + branch,
        })
        repository = data.get("repository")
        ref = repository.get("ref") if isinstance(repository, dict) else None
        target = ref.get("target") if isinstance(ref, dict) else None
        oid = target.get("oid") if isinstance(target, dict) else None
        if not oid:
            raise BranchNotFound("Git branch not found or does not point to a commit: " + branch)
        return oid

    def _read_file_at(self, revision: str, path: str) -> tuple[str, str] | None:
        expression = revision + ":" + path
        data = self._graphql(_READ_FILE, {
            "owner": self.owner,
            "name": self.name,
            "expression": expression,
        })
        repository = data.get("repository")
        obj = repository.get("object") if isinstance(repository, dict) else None
        if obj is None:
            return None
        if obj.get("isTruncated"):
            raise RuntimeStoreError("GitHub truncated file content; refusing to verify it")
        text = obj.get("text")
        oid = obj.get("oid")
        if not isinstance(text, str) or not isinstance(oid, str):
            raise RuntimeStoreError("requested Git object is not a complete UTF-8 blob")
        return text, oid

    def _read_file(self, branch: str, path: str) -> tuple[str, str] | None:
        return self._read_file_at("refs/heads/" + branch, path)

    def _find_path_commit(self, branch: str, path: str, parent_oid: str | None) -> str | None:
        data = self._graphql(_FIND_RECEIPT_COMMIT, {
            "owner": self.owner,
            "name": self.name,
            "qualifiedName": "refs/heads/" + branch,
            "path": path,
        })
        repository = data.get("repository")
        ref = repository.get("ref") if isinstance(repository, dict) else None
        target = ref.get("target") if isinstance(ref, dict) else None
        history = target.get("history") if isinstance(target, dict) else None
        nodes = history.get("nodes", []) if isinstance(history, dict) else []
        matches = []
        for node in nodes:
            oid = node.get("oid")
            if not oid:
                continue
            if parent_oid is None:
                # For a deleted path, history includes both its creation and
                # deletion. Return a commit where the blob actually existed.
                if self._read_file_at(oid, path) is not None:
                    return oid
                continue
            parents = node.get("parents", {}).get("nodes", [])
            parent_oids = [item.get("oid") for item in parents]
            if parent_oid in parent_oids:
                matches.append(oid)
        if len(matches) > 1:
            raise DisputedBatch("multiple commits claim the same parent and immutable path")
        return matches[0] if matches else None

    def _find_receipt_commit(self, path: str, base_head_oid: str) -> str | None:
        return self._find_path_commit(self.runtime_branch, path, base_head_oid)

    def _commit_files(self, branch: str, expected_head_oid: str, message: str, files: Mapping[str, str]) -> str:
        if not _OID_RE.fullmatch(expected_head_oid):
            raise InvalidBatch("expected_head_oid must be a full commit SHA")
        if not files:
            raise InvalidBatch("a Runtime commit must contain at least one file")
        additions = []
        for path, content in sorted(files.items()):
            if not isinstance(content, str):
                raise InvalidBatch("GitHub Runtime v1 accepts UTF-8 text files only")
            additions.append({
                "path": path,
                "contents": base64.b64encode(content.encode("utf-8")).decode("ascii"),
            })
        data = self._graphql(_CREATE_COMMIT, {
            "input": {
                "branch": {
                    "repositoryNameWithOwner": self.owner + "/" + self.name,
                    "branchName": branch,
                },
                "expectedHeadOid": expected_head_oid,
                "message": {"headline": message},
                "fileChanges": {"additions": additions},
            }
        })
        result = data.get("createCommitOnBranch")
        commit = result.get("commit") if isinstance(result, dict) else None
        oid = commit.get("oid") if isinstance(commit, dict) else None
        if not isinstance(oid, str) or not _OID_RE.fullmatch(oid):
            raise RuntimeStoreError("GitHub did not return the created commit OID")
        return oid

    @staticmethod
    def _operation_path(batch_id: str) -> str:
        return ".runtime/operations/" + batch_id + ".json"

    @staticmethod
    def _receipt_path(batch_id: str) -> str:
        return ".runtime/receipts/" + batch_id + ".json"

    def prepare(self, manifest: Mapping[str, Any]) -> dict[str, Any]:
        """Persist and independently read back one immutable PREPARE manifest."""
        normalized = _validate_manifest(manifest)
        batch_id = normalized["batch_id"]
        digest = fingerprint_text(canonical_json(normalized))
        path = self._operation_path(batch_id)

        for _ in range(3):
            existing = self._read_file(self.operations_branch, path)
            if existing is None and self._find_path_commit(self.operations_branch, path, None) is not None:
                raise DisputedBatch("PREPARE path disappeared after a historical creation")
            if existing is not None:
                current = json.loads(existing[0])
                if (current.get("batch_id") != batch_id
                        or current.get("manifest") != normalized
                        or current.get("manifest_fingerprint") != digest):
                    raise BatchConflict("batch_id already exists with different PREPARE content")
                prepare_parent = current.get("prepare_base_head_oid")
                commit_oid = self._find_path_commit(self.operations_branch, path, prepare_parent) if prepare_parent else None
                historical = self._read_file_at(commit_oid, path) if commit_oid else None
                if historical is None or historical[0] != existing[0]:
                    raise DisputedBatch("PREPARE manifest is not backed by its immutable creation commit")
                return {"status": "PREPARED", "batch_id": batch_id,
                        "manifest_ref": self.operations_branch + ":" + path,
                        "manifest_fingerprint": digest}

            head = self._read_ref(self.operations_branch)
            envelope = {
                "schema_version": 1,
                "batch_id": batch_id,
                "prepare_base_head_oid": head,
                "manifest": normalized,
                "manifest_fingerprint": digest,
            }
            content = canonical_json(envelope) + "\n"
            try:
                self._commit_files(
                    self.operations_branch, head,
                    "PREPARE Runtime batch " + batch_id, {path: content},
                )
            except (GitHubGraphQLError, CommitOutcomeUnknown, RuntimeStoreError) as exc:
                # Lost acknowledgements are resolved by independent readback.
                readback = self._read_file(self.operations_branch, path)
                if readback is not None:
                    current = json.loads(readback[0])
                    if current == envelope:
                        commit_oid = self._find_path_commit(self.operations_branch, path, head)
                        historical = self._read_file_at(commit_oid, path) if commit_oid else None
                        if historical is None or historical[0] != readback[0]:
                            raise CommitOutcomeUnknown("PREPARE acknowledgement was lost and historical readback failed") from exc
                        return {"status": "PREPARED", "batch_id": batch_id,
                                "manifest_ref": self.operations_branch + ":" + path,
                                "manifest_fingerprint": digest}
                    raise BatchConflict("PREPARE path was created with conflicting content") from exc
                latest = self._read_ref(self.operations_branch)
                if latest != head and isinstance(exc, GitHubGraphQLError):
                    continue
                if isinstance(exc, CommitOutcomeUnknown):
                    raise CommitOutcomeUnknown("PREPARE outcome remains unknown; do not reuse the batch ID") from exc
                raise
            readback = self._read_file(self.operations_branch, path)
            if readback is None or json.loads(readback[0]) != envelope:
                raise CommitOutcomeUnknown("PREPARE commit returned but independent readback failed")
            commit_oid = self._find_path_commit(self.operations_branch, path, head)
            historical = self._read_file_at(commit_oid, path) if commit_oid else None
            if historical is None or historical[0] != readback[0]:
                raise CommitOutcomeUnknown("PREPARE creation commit could not be independently verified")
            return {"status": "PREPARED", "batch_id": batch_id,
                    "manifest_ref": self.operations_branch + ":" + path,
                    "manifest_fingerprint": digest}
        raise StaleRevision("operations branch kept advancing; PREPARE was not committed")

    def publish(
        self,
        batch_id: str,
        expected_head_oid: str,
        target_files: Mapping[str, str],
    ) -> dict[str, Any]:
        """Publish all target files, checkpoint and receipt in one atomic commit."""
        _validate_batch_id(batch_id)
        if not isinstance(target_files, Mapping) or not target_files:
            raise InvalidBatch("target_files must be a non-empty path-to-text mapping")
        for path, content in target_files.items():
            _validate_target_path(path)
            if not isinstance(content, str):
                raise InvalidBatch("target file contents must be UTF-8 text")

        op_file = self._read_file(self.operations_branch, self._operation_path(batch_id))
        if op_file is None:
            raise InvalidBatch("no independently persisted PREPARE manifest exists")
        envelope = json.loads(op_file[0])
        manifest = _validate_manifest(envelope.get("manifest", {}))
        manifest_fingerprint = fingerprint_text(canonical_json(manifest))
        if envelope.get("batch_id") != batch_id or envelope.get("manifest_fingerprint") != manifest_fingerprint:
            raise DisputedBatch("PREPARE manifest identity or fingerprint is inconsistent")
        if expected_head_oid != manifest["base_head_oid"]:
            raise StaleRevision("publish expected head differs from PREPARE base_head_oid")

        actual_fingerprints = {path: fingerprint_text(content) for path, content in sorted(target_files.items())}
        if actual_fingerprints != manifest["target_fingerprints"]:
            raise BatchConflict("target file set or content differs from PREPARE fingerprints")

        receipt_path = self._receipt_path(batch_id)
        existing_receipt = self._read_file(self.runtime_branch, receipt_path)
        if existing_receipt is not None:
            outcome = self.reconcile(batch_id)
            if outcome["status"] == "PUBLISHED":
                return outcome
            raise DisputedBatch("receipt already exists but does not reconcile")

        current_head = self._read_ref(self.runtime_branch)
        if current_head != expected_head_oid:
            raise StaleRevision("runtime branch advanced after PREPARE")

        receipt = {
            "schema_version": 1,
            "batch_id": batch_id,
            "manifest_ref": self.operations_branch + ":" + self._operation_path(batch_id),
            "manifest_fingerprint": manifest_fingerprint,
            "base_head_oid": expected_head_oid,
            "base_revision": manifest["base_revision"],
            "target_revision": manifest["target_revision"],
            "target_fingerprints": actual_fingerprints,
        }
        checkpoint = {
            "schema_version": 1,
            "revision": manifest["target_revision"],
            "previous_revision": manifest["base_revision"],
            "previous_commit_oid": expected_head_oid,
            "last_batch_id": batch_id,
            "last_manifest_ref": receipt["manifest_ref"],
            "last_receipt_ref": self.runtime_branch + ":" + receipt_path,
        }
        files = dict(target_files)
        files[_CHECKPOINT_PATH] = canonical_json(checkpoint) + "\n"
        files[receipt_path] = canonical_json(receipt) + "\n"

        try:
            commit_oid = self._commit_files(
                self.runtime_branch, expected_head_oid,
                "PUBLISH Runtime batch " + batch_id, files,
            )
        except (GitHubGraphQLError, CommitOutcomeUnknown, RuntimeStoreError) as exc:
            # Never replay blindly. A successful commit is discoverable by its
            # immutable receipt, even if later batches have advanced the branch.
            outcome = self.reconcile(batch_id)
            if outcome["status"] == "PUBLISHED":
                return outcome
            latest = self._read_ref(self.runtime_branch)
            if latest != expected_head_oid and isinstance(exc, GitHubGraphQLError):
                raise StaleRevision("expected HEAD lost the atomic commit race") from exc
            if isinstance(exc, CommitOutcomeUnknown):
                raise CommitOutcomeUnknown("publish outcome cannot yet be proven; reconcile before retrying") from exc
            raise

        outcome = self.reconcile(batch_id)
        if outcome["status"] != "PUBLISHED" or outcome.get("commit_oid") != commit_oid:
            raise CommitOutcomeUnknown("publish commit returned but historical readback did not verify it")
        return outcome

    def reconcile(self, batch_id: str) -> dict[str, Any]:
        """Verify PREPARE, immutable receipt, commit ancestry and all target bytes."""
        _validate_batch_id(batch_id)
        operation_path = self._operation_path(batch_id)
        op_file = self._read_file(self.operations_branch, operation_path)
        if op_file is None:
            prior = self._find_path_commit(self.operations_branch, operation_path, None)
            if prior is not None:
                return {"status": "DISPUTED", "batch_id": batch_id, "reason": "PREPARE_MANIFEST_MISSING"}
            return {"status": "NOT_FOUND", "batch_id": batch_id}
        envelope = json.loads(op_file[0])
        manifest = _validate_manifest(envelope.get("manifest", {}))
        digest = fingerprint_text(canonical_json(manifest))
        if (envelope.get("batch_id") != batch_id
                or envelope.get("manifest_fingerprint") != digest
                or not envelope.get("prepare_base_head_oid")):
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "PREPARE_FINGERPRINT_MISMATCH"}
        prepare_commit = self._find_path_commit(
            self.operations_branch, self._operation_path(batch_id), envelope["prepare_base_head_oid"]
        )
        historical_prepare = self._read_file_at(prepare_commit, self._operation_path(batch_id)) if prepare_commit else None
        if historical_prepare is None or historical_prepare[0] != op_file[0]:
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "PREPARE_HISTORY_MISMATCH"}

        receipt_path = self._receipt_path(batch_id)
        receipt_file = self._read_file(self.runtime_branch, receipt_path)
        if receipt_file is None:
            prior_receipt_commit = self._find_receipt_commit(receipt_path, manifest["base_head_oid"])
            if prior_receipt_commit is not None:
                return {"status": "DISPUTED", "batch_id": batch_id, "reason": "PUBLISHED_RECEIPT_MISSING"}
            return {"status": "PREPARED", "batch_id": batch_id, "manifest_fingerprint": digest}
        try:
            receipt = json.loads(receipt_file[0])
        except json.JSONDecodeError:
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "RECEIPT_NOT_JSON"}
        if (receipt.get("batch_id") != batch_id
                or receipt.get("manifest_fingerprint") != digest
                or receipt.get("base_head_oid") != manifest["base_head_oid"]
                or receipt.get("target_revision") != manifest["target_revision"]
                or receipt.get("target_fingerprints") != manifest["target_fingerprints"]):
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "RECEIPT_MANIFEST_MISMATCH"}

        commit_oid = self._find_receipt_commit(receipt_path, receipt["base_head_oid"])
        if commit_oid is None:
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "PUBLICATION_COMMIT_NOT_IN_HISTORY"}
        receipt_at_commit = self._read_file_at(commit_oid, receipt_path)
        if receipt_at_commit is None or json.loads(receipt_at_commit[0]) != receipt:
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "HISTORICAL_RECEIPT_MISMATCH"}

        checkpoint_file = self._read_file_at(commit_oid, _CHECKPOINT_PATH)
        if checkpoint_file is None:
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "CHECKPOINT_MISSING"}
        checkpoint = json.loads(checkpoint_file[0])
        if (checkpoint.get("last_batch_id") != batch_id
                or checkpoint.get("revision") != manifest["target_revision"]
                or checkpoint.get("previous_commit_oid") != manifest["base_head_oid"]
                or checkpoint.get("last_manifest_ref") != receipt["manifest_ref"]):
            return {"status": "DISPUTED", "batch_id": batch_id, "reason": "CHECKPOINT_MISMATCH"}

        for path, expected in manifest["target_fingerprints"].items():
            item = self._read_file_at(commit_oid, path)
            if item is None or fingerprint_text(item[0]) != expected:
                return {"status": "DISPUTED", "batch_id": batch_id,
                        "reason": "TARGET_READBACK_MISMATCH", "target": path}
        return {
            "status": "PUBLISHED",
            "batch_id": batch_id,
            "manifest_fingerprint": digest,
            "commit_oid": commit_oid,
            "target_revision": manifest["target_revision"],
        }
