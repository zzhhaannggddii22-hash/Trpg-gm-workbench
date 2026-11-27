# Roll Runtime Application Adapter — executable contract

> Status: REFERENCE ADAPTER / TEST HARNESS. Not a production Workbench runtime connector.

This executable model tests the boundary that a same-turn dialogue simulation cannot prove: idempotent event application, Resource Ledger append semantics, Session Log references, immutable application manifests, checkpoint revision checks, cold recovery, and player projection filtering.

## Architecture boundary

- The generic routing protocol remains system-neutral; it does not define dice mechanics or resource formulas.
- The Triangle Agency Chinese v22 protocol remains the only source for that system's dice mechanics.
- The adapter consumes an already-resolved event envelope. It does not decide whether to roll, generate dice, adjudicate a result, choose a player option, or calculate system resource deltas.
- Resource transactions are appended to the Resource Ledger. Session Log records reference those entries. Runtime State stores checkpoint/reconciliation references, not duplicate resource balances.
- The player projection is generated from the authorized `player_reply_payload`; internal IDs and GM-only fields are rejected.

## Run

Python 3.10+, standard library only:

```bash
python roll_runtime_adapter.py
```

The harness uses temporary directories and synthetic data only. It never reads or writes a Campaign, Zarek's character sheet, a real Resource Ledger, Session Log, Runtime State, or GitHub-hosted runtime state.

## Safety behavior

- Stable event identity makes duplicate delivery a verify/read operation, not a second resource application.
- Resource before/after values are chained from the Resource Ledger; Runtime State is not a second balance authority.
- Stale base revisions are rejected.
- A complete application requires matching ledger entries, Session Log references, target revision, immutable manifest fingerprint/checkpoint reference, and a valid player projection.
- Partial writes discovered during cold recovery are marked `DISPUTED` / `INCOMPLETE`; the adapter never replays domain effects or guesses which side succeeded.
- If the persistence proof is complete but the player projection was not yet written, recovery rebuilds it from the immutable prepared payload and revalidates its allowlist.
- Manifests are immutable. Correction/supersession workflows are deliberately outside this harness.

## Non-goals and production gates

This is a conformance reference, not a deployable production adapter. It does not prove ChatGPT platform persistence, integrate with a live Runtime/database, model concurrent writers or distributed locks, implement the full §14.14 supersession/dispute-resolution lifecycle, provide real RNG, deploy Dice UI, or integrate Playwall dice overrides. It also does not provide atomic cross-file transactions: partial writes fail closed and require reconciliation.

A production integration must bind these operations to the actual host storage API, add concurrency control and host-level fault injection, and pass independent read-back tests before this reference can be treated as an implementation.
