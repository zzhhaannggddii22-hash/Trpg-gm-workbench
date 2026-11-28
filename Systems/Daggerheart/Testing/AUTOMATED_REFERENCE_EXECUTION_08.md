# Daggerheart Reference Executor — Automated Run 08

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: **98/98 reference-model tests passed**; repository-wide CI also passed.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `c118cb3157c06b20622d689657574ceb74f80163`
- Workflow run: [Run 46148577036](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46148577036)
- Daggerheart reference job: **success**; exact output: `Ran 98 tests — OK`.
- Repository-wide `validate` job: **success**.
  - 41 general repository regression tests: passed.
  - Roll Runtime Adapter conformance harness: passed.
  - Non-Markdown patch whitespace check: passed.
- All 6 new Encounter Battle Point tests DH-REF-093–098 passed.

## New coverage added after Run 07

| Test | Scenario | Verified assertion |
|---|---|---|
| DH-REF-093 | Base Encounter BP budget | 3 × participating PC count + 2 |
| DH-REF-094 | Encounter BP adjustments | Light/short, multiple Solos, damage boost, lower-Tier enemy, and harder/longer adjustments stack |
| DH-REF-095 | Adversary Type BP cost | Social/Support 1; Horde/Ranged/Skulk/Standard 2; Leader 3; Bruiser 4; Solo 5 |
| DH-REF-096 | Minion group BP | A group with one Minion per PC costs 1 BP; mismatched counts cannot use that special cost |
| DH-REF-097 | Encounter total BP | Adversary costs sum and can be compared against the adjusted budget |
| DH-REF-098 | No major adversary type | If the encounter has no Bruiser, Horde, Leader, or Solo, budget increases by 1 BP |

## Scope and limitations

Battle Points are a starting encounter-design budget, not a guarantee of difficulty or balance. The helper calculates documented budget adjustments and type costs; it does not evaluate enemy synergy, terrain, objectives, Fear pressure, party composition, action economy, or solo encounter balance.

This is a deterministic reference executor / test oracle, not the production GM runtime. Actual short-scene play, external blind GM testing, and production Runtime validation remain required.
