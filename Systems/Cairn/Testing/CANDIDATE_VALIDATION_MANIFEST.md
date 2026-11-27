# Cairn Candidate Validation Manifest

**Manifest type:** CANDIDATE_VALIDATION  
**Canon status:** TEST_ONLY_NON_CANON  
**System:** cairn  
**Ruleset:** Cairn Second Edition  
**System entry:** Systems/Cairn/README.md  
**Runtime references:**
- Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md
- Systems/Cairn/RUNTIME_PROTOCOL.md
- Systems/Cairn/Testing/CORE_RULE_RUNTIME_REGRESSION_MATRIX.md

## Required fields for each validation run

```yaml
validation:
  mode: CANDIDATE_VALIDATION
  canon_status: TEST_ONLY_NON_CANON
  validation_id: "<unique-run-id>"
  system_id: cairn
  ruleset_version: "Cairn Second Edition"
  source_commit: "<exact-commit-sha>"
  fixture_entry: "<exact-fixture-path>"
  runner_chat: "<fresh-chat-identifier-or-description>"
  started_at: "<in-game-time-or-test-start>"
  completed_at: null
  result: pending # pass | conditional_pass | fail | blocked
  scope:
    - "<explicit cases or scenario>"
  prohibited:
    - importing any other system's rules or state
    - reading Oracle before the target runtime commits its own result
    - writing test characters, NPCs, events or state into a formal Campaign
    - treating a synthetic pass as independent blind validation
```

## Current fixture registration

- Fixture: [STATE_TRANSITION_REGRESSION_v1/START.md](./STATE_TRANSITION_REGRESSION_v1/START.md)
- Inputs: [STATE_TRANSITION_REGRESSION_v1/CASES.md](./STATE_TRANSITION_REGRESSION_v1/CASES.md) — no expected outcomes.
- Oracle: [STATE_TRANSITION_REGRESSION_v1/ORACLE.md](./STATE_TRANSITION_REGRESSION_v1/ORACLE.md) — evaluator-only until target output is committed.
- Scope: CRT-66–87.
- Synthetic re-encounter: [L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md](./L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md).
- Current validation result is recorded in the execution reports; it does not change Cairn's candidate status.

## Exit requirements

1. All test outputs and state traces are saved under the Cairn Testing directory.
2. No state or canon has been copied into a formal Campaign.
3. All GM_INFERENCE and UNKNOWN items remain visibly labeled.
4. A formal Campaign cannot be started from this Manifest; it requires a separately approved active-system binding and its own Preflight.
