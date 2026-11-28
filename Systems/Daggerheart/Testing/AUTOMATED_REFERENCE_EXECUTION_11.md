# Daggerheart Reference Executor — Automated Run 11

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: **109/109 reference-model tests passed**; repository-wide CI also passed.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `e547467cf40c5edffa1b90515c309cda083136d4`
- Workflow run: [Run 46150141666](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46150141666)
- Daggerheart reference job: **success**; exact output: `Ran 109 tests in 0.018s — OK`.
- Repository-wide `validate` job: **success**.
  - 41 general repository regression tests: passed.
  - Roll Runtime Adapter conformance harness: passed.
  - Non-Markdown patch whitespace check: passed.

## New coverage added after Run 10

| Test | Scenario | Verified assertion |
|---|---|---|
| DH-REF-103 | Standard Countdown | Each valid Action Roll ticks down by 1; value clamps at 0 |
| DH-REF-104 | Dynamic Progress Countdown | Applies the SRD 2.0 result table: 0 / 0 / 1 / 2 / 3 |
| DH-REF-105 | Dynamic Consequence Countdown | Applies the SRD 2.0 result table: 3 / 2 / 1 / 0 / 0 |
| DH-REF-106 | Dynamic Countdown type boundary | Rejects non-Progress / non-Consequence types |
| DH-REF-107 | Simple Project | GM-approved project uses a Progress Countdown; each valid Long Rest Move advances it and completion occurs at 0 |
| DH-REF-108 | Complex Project | Requires a resolved Action Roll and uses the Dynamic Progress table |
| DH-REF-109 | Work on a Project rest-type restriction | Short Rest is rejected; no Countdown is created and no Downtime Move is consumed |

## Correction made during this run

The first automated attempt exposed a test-fixture omission: two existing project tests did not explicitly pass the Long Rest context after the helper was tightened to enforce the rule. The helper correctly rejected those calls. The fixtures were corrected to provide Long Rest context, and the final full run passed 109/109.

## Scope and limitations

The reference executor now covers the standard and dynamic Countdown advancement tables, event de-duplication, countdown clamping, Simple / Complex project progress, GM approval, Downtime Move limits, and the Long Rest-only restriction.

It still does not replace Campaign-specific project design, GM judgment about project complexity and starting values, or production Runtime validation. Actual short-scene play and the external blind GM test remain pending.
