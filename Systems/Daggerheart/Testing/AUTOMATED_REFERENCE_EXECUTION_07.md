# Daggerheart Reference Executor — Automated Run 07

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: **92/92 reference-model tests passed**; repository-wide CI also passed.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `abf8681341217e1f2fb3bcb2707e9a86c6e2f9f9`
- Workflow run: [Run 46148383257](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46148383257)
- Daggerheart reference job: **success**; exact output: `Ran 92 tests — OK`.
- Repository-wide `validate` job: **success**.
  - 41 general repository regression tests: passed.
  - Roll Runtime Adapter conformance harness: passed.
  - Non-Markdown patch whitespace check: passed.
- All 10 new Downtime Move tests DH-REF-083–092 passed.

## New coverage added after Run 06

| Test | Scenario | Verified assertion |
|---|---|---|
| DH-REF-083 | Per-PC Downtime Move limit | Each PC may use at most two moves per rest; a third is rejected without changing state |
| DH-REF-084 | Short Rest: Tend to Wounds | Target clears 1d4 + acting PC Tier HP, capped by marked HP |
| DH-REF-085 | Short Rest: Clear Stress | Target clears 1d4 + Tier Stress; Vulnerable from full Stress ends once no longer full |
| DH-REF-086 | Short Rest: Repair Armor | Target clears 1d4 + Tier marked Armor Slots |
| DH-REF-087 | Solo Prepare | Gain 1 Hope, respecting the Hope cap |
| DH-REF-088 | Group Prepare | Each participant gains 2 Hope and spends one Downtime Move slot |
| DH-REF-089 | Long Rest: Tend to All Wounds | Clears all marked HP on the target |
| DH-REF-090 | Long Rest: Clear All Stress | Clears all Stress and the Vulnerable state caused by full Stress |
| DH-REF-091 | Long Rest: Repair All Armor | Clears all marked Armor Slots on the target |
| DH-REF-092 | Short Rest-only move during Long Rest | The move is rejected rather than silently using the wrong recovery procedure |

## Interpretation and scope boundaries

- Recovery amounts use the acting PC's Tier, as specified by the Core Set Downtime Move procedure.
- The two-move limit is tracked per PC within one rest event. Group Prepare spends one move slot from each participant.
- Work on a Project is deliberately not resolved by this generic helper: it requires GM approval, a project-specific Countdown, and potentially an Action Roll. That procedure remains Campaign-bound.
- The helper models the mechanical effects only; it is not a replacement for the GM's fictional judgment about whether a target can be reached or helped.

This is a deterministic reference executor / test oracle, not the production GM runtime. It validates selected documented rule interpretations and local Core Set data. It does not establish that the live conversational GM will always execute those rules correctly.

Still outside this executable slice: full character creation and advancement, Tag Team complete semantics, card-by-card feature execution, complete Adversary and Environment procedures, feature-specific conditions, all range-band edge cases and movement interactions, dynamic Countdown procedures, project-specific Downtime, Battle Points and encounter balance, full inventory transactions, and complete Core Rulebook / Errata coverage.

Do not promote the system from Candidate based on this run. Actual short-scene play, external blind GM testing, and production Runtime validation remain required.
