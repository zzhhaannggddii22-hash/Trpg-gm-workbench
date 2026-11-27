"""Opt-in live smoke test for the GitHub GraphQL Runtime Store.

Run only from the trusted issue_comment workflow. Uses disposable branches and
removes them in a finally block. Never targets a Campaign or production branch.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from urllib.parse import quote
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from runtime_store.github_graphql_store import (
    GitHubGraphQLRuntimeStore,
    fingerprint_text,
)


def rest(method: str, url: str, token: str, payload=None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
            return json.loads(raw.decode("utf-8")) if raw else None
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub REST {method} {url} failed: {exc.code} {detail}") from exc


def main():
    token = os.environ["GITHUB_TOKEN"]
    repository = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    api = "https://api.github.com/repos/" + repository
    repo_data = rest("GET", api, token)
    default_branch = repo_data["default_branch"]
    base = rest("GET", api + "/git/ref/heads/" + default_branch, token)["object"]["sha"]

    runtime_branch = f"runtime-store-smoke/{run_id}"
    operations_branch = f"runtime-store-smoke-ops/{run_id}"
    created = []

    def create_branch(name):
        rest("POST", api + "/git/refs", token, {
            "ref": "refs/heads/" + name,
            "sha": base,
        })
        created.append(name)

    try:
        create_branch(runtime_branch)
        create_branch(operations_branch)

        store = GitHubGraphQLRuntimeStore(
            repository=repository,
            runtime_branch=runtime_branch,
            operations_branch=operations_branch,
            token=token,
        )
        initial_head = store._read_ref(runtime_branch)
        targets = {
            f"Runtime_Store_Smoke/{run_id}/state.json":
                json.dumps({"smoke_run": run_id, "revision": 1}, sort_keys=True) + "\n"
        }
        manifest = {
            "batch_id": "LIVE-" + run_id,
            "base_revision": 0,
            "target_revision": 1,
            "base_head_oid": initial_head,
            "target_fingerprints": {
                path: fingerprint_text(value) for path, value in targets.items()
            },
        }

        first_prepare = store.prepare(manifest)
        second_prepare = store.prepare(manifest)
        assert first_prepare["status"] == "PREPARED"
        assert second_prepare == first_prepare

        first_publish = store.publish(manifest["batch_id"], initial_head, targets)
        second_publish = store.publish(manifest["batch_id"], initial_head, targets)
        assert first_publish["status"] == "PUBLISHED"
        assert second_publish["status"] == "PUBLISHED"
        assert first_publish["commit_oid"] == second_publish["commit_oid"]

        # Simulate a cold process restart: no in-memory state is reused.
        restarted = GitHubGraphQLRuntimeStore(
            repository=repository,
            runtime_branch=runtime_branch,
            operations_branch=operations_branch,
            token=token,
        )
        recovered = restarted.reconcile(manifest["batch_id"])
        assert recovered["status"] == "PUBLISHED"
        assert recovered["commit_oid"] == first_publish["commit_oid"]
        for path, expected in targets.items():
            actual = restarted._read_file_at(recovered["commit_oid"], path)
            assert actual is not None and actual[0] == expected

        print(json.dumps({
            "result": "PASS",
            "repository": repository,
            "runtime_branch": runtime_branch,
            "operations_branch": operations_branch,
            "batch_id": manifest["batch_id"],
            "publish_commit": first_publish["commit_oid"],
            "checks": [
                "real GraphQL PREPARE commit and readback",
                "idempotent PREPARE retry",
                "real GraphQL atomic PUBLISH commit",
                "idempotent PUBLISH retry",
                "cold-restart reconciliation",
                "historical target byte readback",
            ],
        }, indent=2))

    finally:
        for name in reversed(created):
            try:
                rest("DELETE", api + "/git/refs/heads/" + quote(name, safe=""), token)
            except Exception as exc:  # cleanup must be visible, never silently claimed
                print(f"WARNING: cleanup failed for {name}: {exc}")


if __name__ == "__main__":
    main()
