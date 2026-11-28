# Daggerheart Reference Executor — Automated Run 04

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: **66/66 reference-model tests passed**; repository-wide CI also passed.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `3564d725bd05669dcd129532dea7056f23cef5af`
- Workflow run: [Run 46147447940](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46147447940)
- Daggerheart reference job: **success**, 66 tests.
- Repository-wide `validate` job: **success**.
  - 41 general repository regression tests: passed.
  - Roll Runtime Adapter conformance harness: passed.
  - Non-Markdown patch whitespace check: passed.
- All 7 new movement / range / line-of-sight tests DH-REF-060–066 passed.

## New coverage added after Run 03

| Test | Scenario | Verified assertion |
|---|---|---|
| DH-REF-060 | PC moves during an Action Roll | Movement within Close can be part of the action; Far cannot be added for free |
| DH-REF-061 | PC repositions without an Action Roll | A successful Agility Roll is required |
| DH-REF-062 | Adversary movement | Close movement can accompany an action; Very Far requires a separate action |
| DH-REF-063 | Partial and total obstruction | Partial cover imposes Disadvantage; total obstruction blocks the attack |
| DH-REF-064 | Area effect targets | Every target must be within Very Close of the same origin |
| DH-REF-065 | Ranged attack without line of sight | The attack is blocked |
| DH-REF-066 | Area effect origin outside effect range | The effect is invalid even if targets are close to one another |

## Scope and limitations

This is a deterministic reference executor / test oracle, not the production GM runtime. It validates selected documented rule interpretations and local Core Set data. It does not establish that the live conversational GM will always execute those rules correctly.

Still outside this executable slice: full character creation and advancement, Tag Team complete semantics, card-by-card feature execution, complete Adversary and Environment procedures, feature-specific conditions, all range-band edge cases and movement interactions, dynamic Countdown procedures, all Rest/Downtime details, Battle Points and encounter balance, full inventory transactions, and complete Core Rulebook / Errata coverage.

Do not promote the system from Candidate based on this run. Actual short-scene play, external blind GM testing, and production Runtime validation remain required.
