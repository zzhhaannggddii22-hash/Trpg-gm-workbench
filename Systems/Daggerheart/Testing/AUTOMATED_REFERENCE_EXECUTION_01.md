# Daggerheart Reference Executor — Automated Run 01

> Date: 2026-11-28  
> Scope: Core Set reference model; deterministic tests against local Core Set JSON  
> Status: 42/42 reference-model tests passed; full rules/runtime acceptance remains pending.

## Execution evidence

- Test runner: `Systems/Daggerheart/Testing/daggerheart_reference_engine.py`
- GitHub Actions workflow: `.github/workflows/pr-validation.yml`
- Commit under test: `ed3b70abd79052fed9880542f220d8509d6c579e`
- Workflow run: [Run 46136478962](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/actions/runs/46136478962)
- Daggerheart test step: **success**, 42 tests in 0.009s.
- Existing repository-wide regression step: **failure**, unrelated to Daggerheart. It found four pre-existing broken Markdown links in Cairn campaign snapshots and GM_Training/NQB01 files. The Daggerheart step was configured with `if: always()` and ran despite that failure.

## Covered by the 42 automated checks

- Duality Dice outcomes, Critical Success, Hope/Fear gain and caps
- Reaction Roll resource separation
- Advantage/Disadvantage cancellation
- Help an Ally resource payment and highest Advantage die
- Group Action helper modifier aggregation
- Stress overflow, Stress costs, Vulnerable and clearing Stress
- Damage thresholds, Armor severity reduction, Direct Damage and Resistance order
- Adversary d20 attack vs PC Evasion
- Countdown event idempotency
- Short/Long Rest interruption, rest-count boundary and Long Rest Fear gain
- Domain Card Recall Stress cost and five-card Loadout
- Fear spending, shared enemy pool token accounting and one-time Evolution
- Tier equipment gate
- Core Set JSON parsing, manifest count check and Hope & Fear dataset isolation

## Important interpretation

This file is a **deterministic reference executor / test oracle**, not an implementation already used by the live GM runtime. The test suite validates the coded interpretation of selected documented rules and checks the repository's Core Set data files. It does not establish that the live conversational GM will always execute those rules correctly.

The following major areas remain outside this first executable slice and require further source-backed modeling and tests:

- Full character creation, advancement and Death Moves
- Tag Team complete timing/resource semantics
- Spellcast and card-by-card Domain/Ancestry/Class feature execution
- Full Adversary stat-block behavior, Fear Features and Environment procedures
- Conditions and their individual durations/removal rules
- Range, movement, line of sight and area targeting
- Dynamic Countdown procedures
- Rest Downtime Moves and all refresh details
- Battle Points, encounter construction and balance
- Inventory, consumable and currency transactions
- Complete Core Rulebook / Errata cross-check

Do not promote the system from Candidate based on this run. The next phase should expand the executable reference model by rule family, with each rule tied to a local source section and explicit expected state transitions.
