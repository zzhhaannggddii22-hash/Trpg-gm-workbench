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

## Minimum production integration boundary

Do not add another synthetic adapter and call it production. Before a host-level test, select and implement one actual storage backend behind a small adapter contract:

1. **Read/discovery:** load the current checkpoint and immutable manifests; discover active PREPARED/INCOMPLETE batches by Campaign / Module / Run identity.
2. **Conditional prepare:** create one immutable PREPARE manifest for a stable batch/event identity, rejecting identity reuse with a different payload and rejecting a stale base revision.
3. **Idempotent target application:** apply each declared field/target once using a stable operation ID and an expected-before revision/value; return a durable target reference.
4. **Independent readback/reconciliation:** reread every required target and manifest from the backend, verify exact content/revision/recipient scope, and distinguish APPLIED, PARTIAL, NOT_APPLIED, and DISPUTED.
5. **Conditional publication:** advance the published checkpoint only if the base revision/head still matches. If the backend cannot provide conditional update or equivalent serialization, stop at INCOMPLETE rather than claiming publication.
6. **Cold recovery:** after a fresh process/session starts, rediscover the batch from backend state, reconcile existing writes, and never replay a domain effect merely because an acknowledgement was lost.

Responsibility boundary:

- The **system-specific rules/runtime** resolves the action and produces a validated event/delta. Cairn persistence code must not decide Triangle Agency mechanics, and vice versa.
- The **generic persistence adapter** applies already-resolved event data, revisions, idempotency, manifests, reconciliation, and publication. It does not roll dice or adjudicate rules.
- The **player projection layer** emits only the authorized recipient-scoped payload after the underlying result is verified.
- The **host/backend** supplies durable reads/writes, conditional creation/update or equivalent concurrency control, and independently readable evidence.

For a GitHub-backed implementation, prefer one immutable Git tree/commit containing the manifest, all required target files, and publication pointer, followed by a branch-ref update guarded by the expected old SHA. Do not emulate a transaction by sequentially calling per-file update operations. For a database backend, use transactional writes plus unique idempotency constraints and revision compare-and-swap.

## Host-level acceptance gate

A production claim requires all of the following on an isolated TEST_ONLY Campaign/store:

- real host adapter and real backend are identified in the test report;
- cold-process/session restart after PREPARE, after each target write, after publication, and after lost acknowledgement;
- duplicate delivery, conflicting event identity, stale revision, and concurrent writer tests;
- independent backend readback of manifests, targets, and published checkpoint;
- player projection allowlist/recipient-scope tests against the actual delivery boundary;
- evidence that no formal Campaign/CANON or active-system binding was touched.

Until these gates pass, retain **PERSISTENCE CONTRACT MODEL PASS** only. Cairn remains `candidate`; Triangle Agency remains the only `active` system.

## Governance

All fixtures use TEST_ONLY data. No Campaign CANON, formal Runtime state, System Registry status, or active-system binding is changed. Cairn remains `candidate`; Triangle Agency remains the only `active` system.
