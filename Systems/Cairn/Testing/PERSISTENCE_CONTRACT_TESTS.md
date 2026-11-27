# Cairn Runtime Persistence Contract Tests

**Status:** TEST_ONLY / NOT A PRODUCTION ADAPTER
**Scope:** deterministic persistence-contract checks for the Cairn candidate runtime
**Test file:** `tests/test_cairn_runtime_persistence.py`

## Why this small test exists

The second independent GM behavior retest established that the natural-language execution traces for CRT-66–CRT-87 agree with the Oracle. It did not exercise a real persistence host.

The existing Cairn Python reference model also tests in-memory state transitions. This fixture adds a deliberately small filesystem-backed contract model to test three failure boundaries that are easy to miss in a clean uninterrupted trace:

1. a process stops after writing a PREPARED manifest but before target state is changed;
2. a multi-target Blast stops after one target has been durably updated;
3. a pending effect has been committed but the caller never receives the acknowledgement.

It uses temporary directories, separate worker processes, atomic file replacement, file and directory fsync on the CI host, and deterministic process termination. It does not load or modify any Campaign save.

## Contract under test

For one event identity:

- A stable event ID is bound to one immutable payload fingerprint. Reusing the ID with a different payload is rejected.
- The PREPARED manifest is written and read back before target writes begin.
- Every target update carries the same event fingerprint in that target's applied-event ledger.
- Recovery inspects the durable ledger before applying a target. A target already committed for this event is not written again.
- A target whose current state matches neither the recorded before-state nor the recorded committed after-state is DISPUTED. The harness fails closed rather than guessing.
- The event becomes COMMITTED only after every declared target is read back as APPLIED.
- A retry after COMMITTED is a no-op and reports zero writes.
- A pending-effect resolution stores the effect's consumed status and resolution event ID in the same target-state replacement as its state change. Replaying the same committed event cannot apply its delta twice.

## Test mapping

| Test | Injected boundary | Required recovery behavior |
|---|---|---|
| `test_prepared_manifest_survives_cold_restart_and_commits_once` | Exit after PREPARED manifest | New process discovers the manifest, applies the missing target once, commits, and later retry writes zero times |
| `test_blast_partial_target_commit_recovers_only_missing_target` | Exit after first Blast target | Preserve the first target, apply only the missing target, then commit the event |
| `test_pending_effect_consumption_is_idempotent_after_lost_ack` | Exit after durable COMMITTED state but before acknowledgement | Retry reads the committed result; Walloped max HP remains 12 and the effect remains consumed exactly once |
| `test_event_id_cannot_be_reused_for_a_different_payload` | Conflicting payload under existing ID | Reject the attempted identity reuse |
| `test_unexplained_target_change_fails_closed` | Target changes outside the event ledger | Mark DISPUTED; do not overwrite the unexplained value |

## Execution

Run with the repository test suite:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_cairn_runtime_persistence -v
```

Or use the existing discovery command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

## Evidence limits

A passing result establishes only that this test-only filesystem adapter model obeys the listed contract under the injected process exits on the GitHub Actions Linux host.

It does **not** establish:

- integration with a production GM Runtime entry point;
- integration with a real Campaign store, GitHub API, database, or connected-app persistence service;
- cross-process concurrent-writer safety or distributed locking;
- behavior under storage hardware failure, filesystem corruption, or every possible power-loss point;
- platform-level atomicity or compare-and-swap guarantees;
- correctness of Cairn rules or natural-language GM behavior beyond the separately tested cases.

In particular, this fixture is not evidence that the actual ChatGPT conversation host provides durable transactions. A real host-level test requires an identified production adapter and a user-authorized isolated test Campaign. Until then, report this as **PERSISTENCE CONTRACT MODEL PASS**, not **HOST PERSISTENCE PASS**.

## Current repository inventory (reviewed at `8237af6b6c52b1302365334fa73da49dec607e65`)

The production-host integration gate is currently **OPEN / NOT IMPLEMENTED**.

- The executable Python files in this repository are test suites or isolated test harnesses. The repository has no production GM Runtime service/entry point, Campaign storage adapter, database client/schema, or deployed host binding.
- `tests/reference_runtime.py` explicitly describes itself as a test-only implementation and never loads a real save. Its `Batch` and `CloseoutBatch` classes operate on synthetic files.
- `GM_Training/Testing/Fixtures/ROLL_RUNTIME_APPLICATION_ADAPTER_v1/` explicitly labels its adapter as a reference/test harness. It uses temporary local files and does not connect to Campaign data or a live Runtime.
- `package.json` contains test dependencies only. The PR workflow runs repository tests and the reference adapter harness; it does not build or deploy a GM Runtime service.
- Campaign Runtime State documents and templates define the data contract, but a document describing a save format is not itself a reader/writer.
- The connected GitHub actions available to an assistant are external tools, not an application adapter implemented by this repository. Per-file contents writes are not a multi-file transaction. Git object/tree/commit and conditional branch-ref operations could be used to build a Git-backed publisher, but no such coordinator currently exists here.

This inventory is a repository-level finding. It does not claim that the ChatGPT platform has no internal persistence; that platform implementation is outside this repository and is not exposed as a Workbench-controlled transaction API.

## Recommended lightweight path

For this project, start with the existing GitHub repository and the lightweight procedure in [GitHub Runtime Save](../../../GM_Training/GITHUB_RUNTIME_SAVE_QUICK_PATH.md). It is designed for a single GM and ordinary campaign continuity:

- Keep the existing `03_RUNTIME_STATE.md` and `04_SESSION_LOG.md` responsibilities.
- When both change, place them in **one Git commit** using Git blobs + one tree + one commit.
- Advance the branch only if its HEAD is still the one just read (`expected_sha`).
- Read the saved Runtime State once after the commit.
- Use a stable event ID and check the log before retrying an important action.

No database, background service, distributed lock, PREPARE registry, or elaborate recovery framework is required for the current workload. A branch-head mismatch simply means stop, reread, and retry deliberately.

The GitHub connector exposes the required Git object operations, so this can be carried out by the assistant without adding a separate production server. This is an operational save path, not a deployed application runtime.

## Small acceptance check

Before using it as the default, perform one TEST_ONLY save where Runtime State and Session Log change together. Confirm both are present in the same commit and that the Runtime State can be read from that commit. That is sufficient for the current single-GM workflow.

Retain the existing synthetic persistence tests as contract examples, but do not expand them into a larger host-testing program unless real failures justify it.

Until the smoke check is performed, report the current Cairn filesystem harness accurately as **PERSISTENCE CONTRACT MODEL PASS**. Cairn remains `candidate`; Triangle Agency remains the only `active` system.

## Governance

All fixtures use TEST_ONLY data. No Campaign CANON, formal Runtime state, System Registry status, or active-system binding is changed. Cairn remains `candidate`; Triangle Agency remains the only `active` system.
