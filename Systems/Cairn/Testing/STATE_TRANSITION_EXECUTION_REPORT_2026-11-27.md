# Cairn 2e State Transition Regression Execution Report

- Date: 2026-11-27
- Mode: same-model deterministic manual execution; TEST_ONLY_NON_CANON
- Matrix: CRT-66–87
- Oracle: STATE_TRANSITION_REGRESSION_v1/ORACLE.md
- Runtime: CORE_RULES_RUNTIME.md + RUNTIME_PROTOCOL.md
- This is not an independent blind run and not an automated CI suite.

## Summary

**22/22 deterministic cases passed against the authored Oracle.** Two cases include explicit GM_INFERENCE boundaries (Panic/inventory HP persistence and deprivation tick boundary); they pass as Workbench protocol tests, not as claims that the official rules state those exact implementation details.

| Case range | Result | Evidence focus |
|---|---:|---|
| CRT-66–71 | 6/6 PASS | Zero damage, STR=0 death precedence, overflow, HP=0 causes |
| CRT-72–74 | 3/3 PASS | Pending Scars effects, handoff, Doomed trigger consumption |
| CRT-75–78 | 4/4 PASS | Multi-Watch progress, no re-roll, deprivation tick IDs, ration uses |
| CRT-79–82 | 4/4 PASS | Dungeon/Wilderness Loss and Exhaustion separation |
| CRT-83–87 | 5/5 PASS | Optional Reaction, Blast isolation, idempotency, NPC continuity, mixed modifiers |

## Deterministic trace highlights

### CRT-67 — STR reaches zero

Before: PC HP 1, STR 2, Armor 0. Damage after Armor = 3.
Intermediate: hp_raw = 1 - 3 = -2; overflow = 2.
Apply: STR 2 - 2 = 0; persist HP 0 / STR 0 / dead.
Result: no STR Save. A natural 1 is not rolled and cannot override STR=0 death.

### CRT-68 — STR remains above zero

Before: HP 1, STR 4. Damage = 3.
Intermediate: hp_raw = -2; overflow = 2.
Apply: STR 4→2; roll STR Save at 2. Fixed roll 2 succeeds.
After: HP 0, STR 2, alive/in combat. Negative HP was not persisted.

### CRT-72 / CRT-73 — delayed effects

Broken Limb and Walloped each create a pending effect linked to the originating Scar event. Before recovery the effect remains pending and no growth die is rolled. At the recovery trigger a new resolution event is created, the die is rolled once, the resulting maximum is applied, and the pending effect is marked consumed. A repeated Handoff reads consumed state and performs no second roll.

### CRT-75 / CRT-76 — travel continuity

A four-Watch travel plan with two completed Watches remains at 2/4 and travelling. The route state stores its travel_id, lost check, event IDs and progress. Handoff recovery continues from the same state and does not charge a Watch or reroll an already committed check.

### CRT-79 / CRT-80 — Dungeon Event follow-up

Loss is not cleared by narration alone: the torch/ongoing effect is updated before the next Cycle. Choosing Rest on Exhaustion creates a distinct child Event Roll; parent and child records remain separately auditable.

### CRT-86 — NPC re-encounter

Mara Bell's off-screen timeline is extended beyond the earlier one-Watch branch:
- She leaves the ferry landing with rope and boat hook; the travel/effort cost is recorded against the in-game Watch.
- During the next Watch she reaches the downstream landing, discovers the skiff has drifted farther, consumes one Ration use, and leaves a visible marker at the fork.
- During the following Watch she follows the drag marks to the old mill, recovers the skiff but not the sealed cargo, and spends one lantern-light use while searching.
- PC returns after those Watches. Mara is at the old mill with the skiff; her inventory, remaining food/light, unresolved cargo task and next plan remain consistent.
- PC only learns facts observable at the mill or disclosed by Mara. PC does not automatically learn the sealed cargo contents, private debt terms, or unshared commission details.
- The off-screen actions are simulated once from elapsed in-game time; a second Handoff does not advance time or repeat the same search.

This is a deterministic synthetic continuity fixture, not a real-player session and not a test of multiple-NPC personality contrast.

## Executable reference-model checks

The repository CI also runs `tests/test_cairn_runtime_protocol.py`, a 20-test deterministic Python reference model covering damage boundaries, HP=0 causes, pending effects, travel/action idempotency, ration uses, deprivation ticks, event routing, Blast target isolation, NPC off-screen state and modifier conflicts. These tests validate protocol invariants in a separate executable model; they do not execute a language-model GM and are not an independent blind test.

## Limitations

- Same-model self-execution; no independent target Chat has run this fixture.
- No automated runner parses the Markdown cases.
- The 22 cases exercise protocol logic, not all Cairn 2e rules or all module-specific exceptions.
- CRT-77 uses a Workbench time-boundary interpretation of the official phrase “more than a day”; retain GM_INFERENCE until a table decision or stronger source interpretation is recorded.
- The exact consequences of Panic/Inventory Overload HP persistence remain Workbench GM_INFERENCE because the official entries do not specify an HP refill on condition removal.

## Conclusion

State-transition regression: **manual PASS (22/22)** with the above inference labels and limitations. This does not activate Cairn. Candidate status and formal Campaign gate remain unchanged.
