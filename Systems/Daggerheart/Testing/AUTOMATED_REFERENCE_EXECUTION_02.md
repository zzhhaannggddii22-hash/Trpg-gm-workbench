# Daggerheart Reference Executor — Automated Run 02

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: **51/51 reference-model tests passed**; full rules/runtime acceptance remains pending.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `8c6e66274a61d6e22609f3363bf4d42c136283de`
- Workflow run: [Run 46146790931](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46146790931)
- Daggerheart job: **success**.
- Exact output: `Ran 51 tests in 0.009s — OK`.
- The 9 added damage-interaction tests DH-REF-043–051 all passed.

## New coverage added after Run 01

| Test | Scenario | Verified assertion |
|---|---|---|
| DH-REF-043 | Direct Damage with Resistance | Resistance still halves damage; Direct Damage bypasses Armor Slots only |
| DH-REF-044 | Resistance and Armor Slot together | Resistance first, round up, then compare threshold and reduce severity with Armor |
| DH-REF-045 | Duplicate Resistance sources | Resistance does not stack |
| DH-REF-046 | Immunity to one damage type | Matching damage is ignored |
| DH-REF-047 | Mixed damage, only one type defended | No partial benefit from defending only one of the two damage types |
| DH-REF-048 | Mixed damage, Resistance to both types | Each type is reduced, then the resulting damage is combined |
| DH-REF-049 | Simultaneous same-type damage sources | Sources are combined before threshold comparison |
| DH-REF-050 | Mixed damage, Immunity to both types | Both damage types are ignored |
| DH-REF-051 | Mixed damage, Resistance to one type and Immunity to the other | Both types are defended; each defense is applied to its own type |

## Repository-wide CI distinction

At the same commit, the separate repository-wide validation job failed its Markdown anchor audit on eight stale anchors in the Blades in the Dark rule index. This did not affect the Daggerheart-specific job or its 51/51 result. The eight anchors were corrected afterward in commit `a19f979c532cabd4c40adc59e8e33435fcfa2506`; a later full-repository run is required to verify that repair.

## Scope and limitations

This is a deterministic reference executor / test oracle, not the production GM runtime. It validates selected documented rule interpretations and local Core Set data. It does not establish that the live conversational GM will always execute those rules correctly.

Still outside this executable slice: full character creation and advancement, Tag Team complete semantics, card-by-card feature execution, complete Adversary and Environment procedures, Conditions, movement/line of sight, dynamic Countdown procedures, all Rest/Downtime details, Battle Points and encounter balance, full inventory transactions, and complete Core Rulebook / Errata coverage.

Do not promote the system from Candidate based on this run. Actual short-scene play, external blind GM testing, and production Runtime validation remain required.
