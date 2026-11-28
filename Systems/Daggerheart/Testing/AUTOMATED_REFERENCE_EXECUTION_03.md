# Daggerheart Reference Executor — Automated Run 03

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: **59/59 reference-model tests passed**; repository-wide CI also passed.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `35843371b4e9d26935cea68ba87d5f54371e2597`
- Workflow run: [Run 46147279952](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46147279952)
- Daggerheart reference job: **success**, 59 tests.
- Repository-wide `validate` job: **success**.
  - 41 general repository regression tests: passed.
  - Roll Runtime Adapter conformance harness: passed.
  - Non-Markdown patch whitespace check: passed.
- All 8 new condition lifecycle tests DH-REF-052–059 passed.

## New coverage added after Run 02

| Test | Scenario | Verified assertion |
|---|---|---|
| DH-REF-052 | Same standard condition applied twice to one target | No stacking; a different target can hold the same condition |
| DH-REF-053 | Hidden condition and target attack | Rolls against Hidden have Disadvantage; the target's attack ends Hidden |
| DH-REF-054 | Restrained condition | The target cannot move but can still act from its current position |
| DH-REF-055 | Vulnerable condition | Rolls targeting the creature have Advantage |
| DH-REF-056 | Hidden and Vulnerable together | Advantage and Disadvantage cancel |
| DH-REF-057 | PC clears a Temporary condition | Failure does not clear it; a successful appropriate Action Roll does |
| DH-REF-058 | Adversary clears a Temporary condition | The adversary uses its own Spotlight to clear it; that Spotlight is consumed |
| DH-REF-059 | Special Condition | It clears only when its specific requirement is met |

## Interpretation boundary

The condition tests encode the current local Core Set reference text: Hidden, Restrained, Vulnerable, Temporary tags, and Special Conditions. They do not attempt to encode every feature-specific condition or every bespoke removal requirement; those remain attached to the originating feature text.

This is a deterministic reference executor / test oracle, not the production GM runtime. It validates selected documented rule interpretations and local Core Set data. It does not establish that the live conversational GM will always execute those rules correctly.

Still outside this executable slice: full character creation and advancement, Tag Team complete semantics, card-by-card feature execution, complete Adversary and Environment procedures, feature-specific conditions, movement/line of sight edge cases, dynamic Countdown procedures, all Rest/Downtime details, Battle Points and encounter balance, full inventory transactions, and complete Core Rulebook / Errata coverage.

Do not promote the system from Candidate based on this run. Actual short-scene play, external blind GM testing, and production Runtime validation remain required.
