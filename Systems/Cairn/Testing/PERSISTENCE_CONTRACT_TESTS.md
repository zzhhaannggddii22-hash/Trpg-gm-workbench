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

## Governance

All fixtures use TEST_ONLY data. No Campaign CANON, formal Runtime state, System Registry status, or active-system binding is changed. Cairn remains `candidate`; Triangle Agency remains the only `active` system.
