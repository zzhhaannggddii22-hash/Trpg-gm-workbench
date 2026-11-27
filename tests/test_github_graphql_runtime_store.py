import base64
import json
import unittest

from runtime_store.github_graphql_store import (
    BatchConflict,
    ConfigurationError,
    CommitOutcomeUnknown,
    DisputedBatch,
    GitHubGraphQLError,
    GitHubGraphQLRuntimeStore,
    InvalidTargetPath,
    StaleRevision,
    fingerprint_text,
)


BASE = "1" * 40
OPS_BASE = "2" * 40


class MemoryGitHubStore(GitHubGraphQLRuntimeStore):
    """Deterministic GitHub branch/commit model for adapter contract tests."""

    def __init__(self):
        super().__init__(
            repository="example/workbench",
            runtime_branch="runtime/test-campaign",
            operations_branch="runtime-ops/test-campaign",
            transport=lambda query, variables: {},
        )
        self.heads = {
            self.runtime_branch: BASE,
            self.operations_branch: OPS_BASE,
        }
        self.snapshots = {
            BASE: {},
            OPS_BASE: {},
        }
        self.parents = {BASE: [], OPS_BASE: []}
        self.changed = {}
        self.sequence = 10
        self.lose_next_ack = False
        self.race_next_publish = False

    def _read_ref(self, branch):
        return self.heads[branch]

    def _read_file_at(self, revision, path):
        if revision.startswith("refs/heads/"):
            branch = revision[len("refs/heads/"):]
            revision = self.heads[branch]
        content = self.snapshots[revision].get(path)
        if content is None:
            return None
        return content, fingerprint_text(content)

    def _read_file(self, branch, path):
        return self._read_file_at("refs/heads/" + branch, path)

    def _advance_unrelated(self, branch):
        old = self.heads[branch]
        self.sequence += 1
        new = f"{self.sequence:040x}"
        self.snapshots[new] = dict(self.snapshots[old])
        self.parents[new] = [old]
        self.changed[new] = set()
        self.heads[branch] = new
        return new

    def _commit_files(self, branch, expected_head_oid, message, files):
        if branch == self.runtime_branch and self.race_next_publish:
            self.race_next_publish = False
            self._advance_unrelated(branch)
        if self.heads[branch] != expected_head_oid:
            raise GitHubGraphQLError([{"message": "expectedHeadOid does not match current branch HEAD"}])
        old = self.heads[branch]
        self.sequence += 1
        new = f"{self.sequence:040x}"
        snapshot = dict(self.snapshots[old])
        snapshot.update(files)
        self.snapshots[new] = snapshot
        self.parents[new] = [old]
        self.changed[new] = set(files)
        self.heads[branch] = new
        if self.lose_next_ack:
            self.lose_next_ack = False
            raise CommitOutcomeUnknown("simulated acknowledgement loss after durable commit")
        return new

    def _find_path_commit(self, branch, path, parent_oid):
        cursor = self.heads[branch]
        matches = []
        path_commits = []
        while cursor in self.parents:
            if path in self.changed.get(cursor, set()):
                path_commits.append(cursor)
                if parent_oid is not None and parent_oid in self.parents[cursor]:
                    matches.append(cursor)
            if parent_oid is None and path in self.snapshots[cursor]:
                return cursor
            parents = self.parents[cursor]
            if not parents:
                break
            cursor = parents[0]
        if parent_oid is not None and len(path_commits) > 1:
            raise DisputedBatch("memory model detected a mutable supposedly immutable path")
        if len(matches) > 1:
            raise AssertionError("memory model created duplicate immutable-path commits")
        return matches[0] if matches else None

    def _find_receipt_commit(self, path, base_head_oid):
        return self._find_path_commit(self.runtime_branch, path, base_head_oid)


class GitHubGraphQLRuntimeStoreTests(unittest.TestCase):
    def setUp(self):
        self.store = MemoryGitHubStore()
        self.targets = {
            "campaign/runtime_state.json": '{"hp":7,"revision":2}\n',
            "campaign/session_log.jsonl": '{"event_id":"EV-2"}\n',
        }
        self.manifest = {
            "batch_id": "BATCH-002",
            "base_revision": 1,
            "target_revision": 2,
            "base_head_oid": BASE,
            "target_fingerprints": {
                path: fingerprint_text(content)
                for path, content in self.targets.items()
            },
        }

    def test_prepare_is_persisted_and_idempotent(self):
        first = self.store.prepare(self.manifest)
        second = self.store.prepare(self.manifest)
        self.assertEqual(first["status"], "PREPARED")
        self.assertEqual(first, second)
        self.assertEqual(len(self.store.changed[self.store.heads[self.store.operations_branch]]), 1)

    def test_prepare_lost_ack_is_verified_from_immutable_history(self):
        self.store.lose_next_ack = True
        result = self.store.prepare(self.manifest)
        self.assertEqual(result["status"], "PREPARED")
        path = ".runtime/operations/BATCH-002.json"
        head = self.store.heads[self.store.operations_branch]
        self.assertIsNotNone(self.store._find_path_commit(
            self.store.operations_branch, path, OPS_BASE
        ))
        self.assertIsNotNone(self.store._read_file_at(head, path))

    def test_batch_id_cannot_be_reused_for_different_manifest(self):
        self.store.prepare(self.manifest)
        changed = dict(self.manifest)
        changed["target_revision"] = 3
        with self.assertRaises(BatchConflict):
            self.store.prepare(changed)

    def test_publish_places_all_targets_checkpoint_and_receipt_in_one_commit(self):
        self.store.prepare(self.manifest)
        result = self.store.publish("BATCH-002", BASE, self.targets)
        self.assertEqual(result["status"], "PUBLISHED")
        self.assertEqual(result["target_revision"], 2)
        commit = result["commit_oid"]
        changed_paths = self.store.changed[commit]
        self.assertEqual(
            changed_paths,
            {
                "campaign/runtime_state.json",
                "campaign/session_log.jsonl",
                ".runtime/checkpoint.json",
                ".runtime/receipts/BATCH-002.json",
            },
        )
        self.assertEqual(self.store.parents[commit], [BASE])
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "PUBLISHED")

    def test_publish_lost_ack_is_reconciled_without_replay(self):
        self.store.prepare(self.manifest)
        self.store.lose_next_ack = True
        result = self.store.publish("BATCH-002", BASE, self.targets)
        self.assertEqual(result["status"], "PUBLISHED")
        runtime_commits = [
            oid for oid, paths in self.store.changed.items()
            if ".runtime/receipts/BATCH-002.json" in paths
        ]
        self.assertEqual(len(runtime_commits), 1)

    def test_stale_head_is_rejected_before_publish(self):
        self.store.prepare(self.manifest)
        self.store._advance_unrelated(self.store.runtime_branch)
        with self.assertRaises(StaleRevision):
            self.store.publish("BATCH-002", BASE, self.targets)
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "PREPARED")

    def test_atomic_expected_head_rejects_race_after_initial_read(self):
        self.store.prepare(self.manifest)
        self.store.race_next_publish = True
        with self.assertRaises(StaleRevision):
            self.store.publish("BATCH-002", BASE, self.targets)
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "PREPARED")

    def test_wrong_target_payload_is_rejected_before_commit(self):
        self.store.prepare(self.manifest)
        wrong = dict(self.targets)
        wrong["campaign/runtime_state.json"] = '{"hp":99}\n'
        with self.assertRaises(BatchConflict):
            self.store.publish("BATCH-002", BASE, wrong)
        self.assertEqual(self.store.heads[self.store.runtime_branch], BASE)

    def test_unsafe_target_path_is_rejected(self):
        bad_manifest = dict(self.manifest)
        bad_manifest["target_fingerprints"] = {"../escape.json": fingerprint_text("x")}
        with self.assertRaises(InvalidTargetPath):
            self.store.prepare(bad_manifest)
        self.store.prepare(self.manifest)
        with self.assertRaises(InvalidTargetPath):
            self.store.publish("BATCH-002", BASE, {"../escape.json": "x"})

    def test_reconcile_fails_closed_on_malformed_prepare_records(self):
        self.store.prepare(self.manifest)
        path = ".runtime/operations/BATCH-002.json"
        head = self.store.heads[self.store.operations_branch]
        self.store.snapshots[head][path] = "{not-json"
        result = self.store.reconcile("BATCH-002")
        self.assertEqual(result["status"], "DISPUTED")
        self.assertEqual(result["reason"], "PREPARE_MALFORMED")

        self.store.snapshots[head][path] = json.dumps(["not", "an", "object"])
        result = self.store.reconcile("BATCH-002")
        self.assertEqual(result["status"], "DISPUTED")
        self.assertEqual(result["reason"], "PREPARE_MALFORMED")

    def test_reconcile_fails_closed_on_malformed_receipt_and_checkpoint(self):
        self.store.prepare(self.manifest)
        published = self.store.publish("BATCH-002", BASE, self.targets)
        commit = published["commit_oid"]
        snapshot = self.store.snapshots[commit]
        receipt_path = ".runtime/receipts/BATCH-002.json"
        snapshot[receipt_path] = "{not-json"
        result = self.store.reconcile("BATCH-002")
        self.assertEqual(result["status"], "DISPUTED")
        self.assertEqual(result["reason"], "RECEIPT_NOT_JSON")

        # Restore the receipt, then corrupt the checkpoint in the same historical commit.
        snapshot[receipt_path] = json.dumps({
            "schema_version": 1,
            "batch_id": "BATCH-002",
            "manifest_ref": self.store.operations_branch + ":.runtime/operations/BATCH-002.json",
            "manifest_fingerprint": fingerprint_text(json.dumps(self.manifest, sort_keys=True, separators=(",", ":"))),
            "base_head_oid": BASE,
            "base_revision": 1,
            "target_revision": 2,
            "target_fingerprints": self.manifest["target_fingerprints"],
        }, sort_keys=True) + "\\n"
        snapshot[".runtime/checkpoint.json"] = "{not-json"
        result = self.store.reconcile("BATCH-002")
        self.assertEqual(result["status"], "DISPUTED")
        self.assertEqual(result["reason"], "CHECKPOINT_NOT_JSON")

    def test_reconcile_detects_removed_prepare_manifest(self):
        self.store.prepare(self.manifest)
        old = self.store.heads[self.store.operations_branch]
        snapshot = dict(self.store.snapshots[old])
        path = ".runtime/operations/BATCH-002.json"
        snapshot.pop(path)
        self.store.sequence += 1
        new = f"{self.store.sequence:040x}"
        self.store.snapshots[new] = snapshot
        self.store.parents[new] = [old]
        self.store.changed[new] = {path}
        self.store.heads[self.store.operations_branch] = new
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "DISPUTED")
        with self.assertRaises(DisputedBatch):
            self.store.prepare(self.manifest)

    def test_publish_rejects_tampered_prepare_even_with_recomputed_fingerprint(self):
        self.store.prepare(self.manifest)
        old = self.store.heads[self.store.operations_branch]
        path = ".runtime/operations/BATCH-002.json"
        snapshot = dict(self.store.snapshots[old])
        envelope = json.loads(snapshot[path])
        envelope["manifest"]["target_revision"] = 999
        envelope["manifest_fingerprint"] = fingerprint_text(
            json.dumps(envelope["manifest"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        )
        snapshot[path] = json.dumps(envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\\n"
        self.store.sequence += 1
        new = f"{self.store.sequence:040x}"
        self.store.snapshots[new] = snapshot
        self.store.parents[new] = [old]
        self.store.changed[new] = {path}
        self.store.heads[self.store.operations_branch] = new
        with self.assertRaises(DisputedBatch):
            self.store.publish("BATCH-002", BASE, self.targets)

    def test_reconcile_detects_tampered_prepare_manifest(self):
        self.store.prepare(self.manifest)
        head = self.store.heads[self.store.operations_branch]
        path = ".runtime/operations/BATCH-002.json"
        changed = dict(self.store.snapshots[head])
        envelope = json.loads(changed[path])
        envelope["manifest"]["target_revision"] = 999
        envelope["manifest_fingerprint"] = fingerprint_text(
            json.dumps(envelope["manifest"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        )
        changed[path] = json.dumps(envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        self.store.sequence += 1
        new = f"{self.store.sequence:040x}"
        self.store.snapshots[new] = changed
        self.store.parents[new] = [head]
        self.store.changed[new] = {path}
        self.store.heads[self.store.operations_branch] = new
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "DISPUTED")

    def test_reconcile_detects_receipt_removed_after_publication(self):
        self.store.prepare(self.manifest)
        self.store.publish("BATCH-002", BASE, self.targets)
        old = self.store.heads[self.store.runtime_branch]
        snapshot = dict(self.store.snapshots[old])
        snapshot.pop(".runtime/receipts/BATCH-002.json")
        self.store.sequence += 1
        new = f"{self.store.sequence:040x}"
        self.store.snapshots[new] = snapshot
        self.store.parents[new] = [old]
        self.store.changed[new] = {".runtime/receipts/BATCH-002.json"}
        self.store.heads[self.store.runtime_branch] = new
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "DISPUTED")

    def test_reconcile_detects_tampered_current_receipt(self):
        self.store.prepare(self.manifest)
        self.store.publish("BATCH-002", BASE, self.targets)
        head = self.store.heads[self.store.runtime_branch]
        tampered = dict(self.store.snapshots[head])
        receipt_path = ".runtime/receipts/BATCH-002.json"
        receipt = json.loads(tampered[receipt_path])
        receipt["target_revision"] = 999
        tampered[receipt_path] = json.dumps(receipt, sort_keys=True) + "\n"
        self.store.sequence += 1
        new = f"{self.store.sequence:040x}"
        self.store.snapshots[new] = tampered
        self.store.parents[new] = [head]
        self.store.changed[new] = {receipt_path}
        self.store.heads[self.store.runtime_branch] = new
        self.assertEqual(self.store.reconcile("BATCH-002")["status"], "DISPUTED")


class GraphQLRequestShapeTests(unittest.TestCase):
    def test_branch_validation_rejects_forbidden_git_ref_names(self):
        for invalid in ("", "@", "HEAD", "runtime//smoke", "runtime/.hidden",
                        "runtime/branch.lock", "runtime/has?mark", "runtime\\\\bad",
                        "runtime/trailing."):
            with self.subTest(branch=invalid):
                with self.assertRaises(ConfigurationError):
                    GitHubGraphQLRuntimeStore(
                        "example/workbench", invalid, "runtime-ops/test",
                        transport=lambda query, variables: {},
                    )
        GitHubGraphQLRuntimeStore(
            "example/workbench", "runtime-smoke/run-123", "runtime-ops/run-123",
            transport=lambda query, variables: {},
        )

    def test_commit_mutation_uses_expected_head_and_base64_full_file_contents(self):
        seen = {}

        def transport(query, variables):
            seen["query"] = query
            seen["variables"] = variables
            return {"createCommitOnBranch": {"commit": {"oid": "a" * 40}}}

        store = GitHubGraphQLRuntimeStore(
            "example/workbench", "runtime/test", "runtime-ops/test",
            transport=transport,
        )
        oid = store._commit_files(
            "runtime/test", BASE, "test commit", {"a.json": '{"ok":true}\n'}
        )
        self.assertEqual(oid, "a" * 40)
        input_value = seen["variables"]["input"]
        self.assertEqual(input_value["expectedHeadOid"], BASE)
        self.assertEqual(input_value["branch"]["branchName"], "runtime/test")
        encoded = input_value["fileChanges"]["additions"][0]["contents"]
        self.assertEqual(base64.b64decode(encoded).decode("utf-8"), '{"ok":true}\n')
        self.assertIn("createCommitOnBranch", seen["query"])


if __name__ == "__main__":
    unittest.main()
