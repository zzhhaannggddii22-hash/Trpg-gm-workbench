# GitHub GraphQL Runtime Store v1

**Status:** IMPLEMENTED ADAPTER COMPONENT / NOT YET DEPLOYED OR CONNECTED TO THE GM Runtime.

This is a generic persistence backend. It does not adjudicate rules, roll dice, choose actions, simulate NPCs, or construct player-facing narrative. Triangle Agency and Cairn must supply already-resolved event/state payloads through their own system bindings.

## Why GraphQL, not a REST ref update

The REST Git Database flow can create blobs, trees and commits, then move a branch ref. The ordinary REST "Update a reference" endpoint exposes a target SHA and a force flag, but no expected-old-SHA parameter. A client-side read-then-write check is not an atomic compare-and-swap.

GitHub GraphQL createCommitOnBranch accepts expectedHeadOid, creates a commit whose parent is the branch HEAD, and updates the branch. The mutation's file changes are included in that commit. The adapter uses this server-side expected-HEAD check for both PREPARE and PUBLISH.

Relevant GitHub documentation:
- https://docs.github.com/en/graphql/reference/commits#createcommitonbranch
- https://docs.github.com/en/graphql/reference/git#filechanges
- https://docs.github.com/en/graphql/reference/objects#commithistoryconnection

## Storage layout

Provision two dedicated branches for each isolated Campaign/Run identity:

- Runtime branch: authoritative state snapshots and published checkpoints.
- Operations branch: immutable PREPARE manifests and operation discovery.

The adapter deliberately does not create or delete branches. Branch provisioning and permissions are an administrative setup step.

**Append-only trust boundary:** the Runtime and operations branches must be protected against force-push and deletion. PREPARE and receipt paths are one-write records: verification rejects a path whose Git history shows more than one change event, and checks the creation commit and blob against the expected parent and content. This detects ordinary later edits/deletions; repository rules are still required to prevent an administrator or privileged writer from rewriting the branch history itself.

### PREPARE

prepare(manifest) writes one immutable file:

    .runtime/operations/<batch_id>.json

The manifest binds:
- stable batch ID;
- base and target domain revision;
- exact base Git commit OID;
- SHA-256 fingerprint for every target file.

The file is independently read back before the method reports PREPARED. If the response is lost, a retry first reads the existing path and accepts it only when the complete envelope matches. Reusing a batch ID with different content is rejected.

### PUBLISH

publish(batch_id, expected_head_oid, target_files) verifies the PREPARE manifest and payload fingerprints, then appends one GitHub GraphQL commit to the Runtime branch. That single commit contains:

- every declared target file;
- .runtime/checkpoint.json;
- .runtime/receipts/<batch_id>.json.

expectedHeadOid is checked by GitHub as part of the commit mutation. If another writer advanced the branch after the caller's read, the commit is rejected rather than rebased or silently applied to a different base.

The adapter performs historical readback: it locates the commit that introduced the immutable receipt, confirms its parent is the prepared base commit, and reads each target/checkpoint/receipt from that exact commit. A later batch may advance the branch without invalidating proof of the earlier publication.

### Recovery

reconcile(batch_id) returns:
- NOT_FOUND: no PREPARE exists;
- PREPARED: PREPARE exists but no publication receipt is visible;
- PUBLISHED: receipt, parent commit, checkpoint and every target byte match;
- DISPUTED: identity, history, checkpoint or target evidence conflicts.

A transport error after a mutation is not blindly retried. The adapter first attempts independent readback. If the outcome remains unknown, it raises CommitOutcomeUnknown; the caller must reconcile before any retry.

## Minimal usage

    from runtime_store.github_graphql_store import GitHubGraphQLRuntimeStore, fingerprint_text

    store = GitHubGraphQLRuntimeStore(
        repository="owner/repository",
        runtime_branch="runtime/campaign-123/run-01",
        operations_branch="runtime-ops/campaign-123/run-01",
    )

    targets = {
        "Campaigns/example/Runtime_State.json": '{"revision": 2}\n',
        "Campaigns/example/Session_Log.jsonl": '{"event_id":"EV-02"}\n',
    }

    manifest = {
        "batch_id": "BATCH-0002",
        "base_revision": 1,
        "target_revision": 2,
        "base_head_oid": "<40-character current Runtime branch HEAD>",
        "target_fingerprints": {
            path: fingerprint_text(content)
            for path, content in targets.items()
        },
    }

    store.prepare(manifest)
    result = store.publish("BATCH-0002", manifest["base_head_oid"], targets)
    assert result["status"] == "PUBLISHED"

The example omits the caller's system-specific event validation and authorization. The adapter must only receive already-approved target payloads.

## Safety and current limits

- UTF-8 text files only; binary objects are rejected.
- No target deletion in v1.
- User target paths cannot write into .runtime/.
- Runtime and operations branches must be distinct and pre-provisioned.
- Both branches require repository rules that block force-push and deletion; code-level history checks cannot protect against privileged history rewrites.
- PREPARE and receipt paths must remain single-change immutable records; later edits/deletions are treated as disputes.
- No branch bootstrap, permission management, token provisioning, or deployment is performed.
- The adapter does not migrate existing Campaigns or decide which historical state is authoritative.
- The adapter does not deliver player projections; those are separate recipient-scoped targets and must be validated before inclusion.
- This code has unit tests with a deterministic in-memory GitHub model. Those tests are not a live GitHub host acceptance test.
- Production deployment still requires a trusted execution environment with a least-privilege token, branch protections, isolated TEST_ONLY branches, live cold-restart tests, and integration with the actual GM Runtime entry point.

Until those integration gates pass, classify this as GITHUB BACKEND ADAPTER IMPLEMENTED / HOST INTEGRATION NOT VERIFIED, not as a deployed or production-accepted Runtime.
