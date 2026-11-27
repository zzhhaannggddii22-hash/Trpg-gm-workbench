# Cairn 2e State Transition Regression v1 — Cases (Inputs Only)

**Mode:** CANDIDATE_VALIDATION / TEST_ONLY_NON_CANON  
**Visibility:** Target runtime may read this file. It contains no expected outcomes.

| Case | Initial state / action / fixed input |
|---|---|
| CRT-66 | PC HP 3, STR 10, Armor 2. An attack rolls 2 damage. Resolve the resulting damage transaction. |
| CRT-67 | PC HP 1, STR 2, Armor 0. An attack deals 3 damage after Armor. A hypothetical Save die of 1 is supplied only to detect whether the runtime incorrectly rolls after STR reaches 0. |
| CRT-68 | PC HP 1, STR 4, Armor 0. An attack deals 3 damage after Armor. If a STR Save is reached, fixed d20 result is 2. |
| CRT-69 | PC HP 0, STR 5, Armor 0. The PC takes 2 damage after Armor. If a STR Save is reached, fixed d20 result is 3. |
| CRT-70 | PC is Panicked at HP 0. On their turn they spend an action and succeed at the required WIL Save. No healing action is declared. |
| CRT-71 | PC has all 10 inventory slots occupied and HP has been reduced to 0 by inventory overload. The PC drops one ordinary item, freeing one slot; no healing action is declared. |
| CRT-72 | PC has the Broken Limb Scar. The limb is later treated and the official recovery condition is declared satisfied. Fixed 2d6 result for the recovery growth check: 10. Current maximum HP: 8. |
| CRT-73 | PC has the Walloped Scar and its Deprived/rest condition. Handoff occurs before the required hours of rest have elapsed. A later session records the recovery condition as satisfied. Fixed 1d6 result: 4. |
| CRT-74 | PC has the Doomed Scar. First resolve an ordinary WIL Save. Later the PC suffers Critical Damage; the new STR is 10 and the fixed STR Save result is 10. Fixed 3d6 result after a successful Critical Damage Save: 15. Current maximum HP: 12. |
| CRT-75 | Party has a travel_plan with total cost 4 Watches. Two Watches have been committed; current position is an intermediate route point; two Watches remain. |
| CRT-76 | Continue the same travel_plan after Handoff. The same travel_action_id has a committed lost check (Trail path, 2-in-6 risk, fixed d6 result 2) and one Watch already committed. |
| CRT-77 | A character has been continuously Deprived for 25 hours, then later 49 hours. Initial Fatigue is 0. Record each due Fatigue tick with its own ID. |
| CRT-78 | One Ration has uses_remaining 3. One PC makes camp and consumes one Ration use. |
| CRT-79 | Dungeon Event result is Loss. The concrete loss is that the party's currently lit torch is extinguished. |
| CRT-80 | Dungeon Event result is Exhaustion. The party chooses the Rest option. The new child Event Roll has fixed result 6 (Quiet). |
| CRT-81 | Wilderness Event result is Loss. The Warden presents a concrete, fictionally grounded cost: one carried oil flask is lost during a river crossing. |
| CRT-82 | Wilderness Event result is Exhaustion. The route is blocked by a fallen tree; the party chooses to spend one additional Watch clearing a safe passage rather than take Fatigue. |
| CRT-83 | NPC Reaction is uncertain at first glance, but established fiction already determines the villager's attitude: they are grateful because the PC previously rescued their child. |
| CRT-84 | A Blast attack affects three targets. Their Armor values are 1, 0, and 2. Resolve each target's damage and state transaction separately; use fixed damage rolls 4, 2, and 5 respectively. |
| CRT-85 | A damage/event transaction with event_id evt-17 has already been committed and its state delta is present. Restore the same Handoff and replay the same event input. |
| CRT-86 | Use the Mara Bell synthetic setup from the re-encounter report. PC-A leaves Alder Ford. Mara advances across the stated Watches, recovers the skiff at the old mill but not the sealed cargo, and PC-A later arrives at the old mill. Maintain private debt/commission facts as unshared knowledge. |
| CRT-87 | PC attacks an unconscious target from behind cover while the PC is also restrained. The situation presents both a possible Enhanced and Impaired factor. A separate Blast from the same scene affects two targets; resolve each target independently. |

## Execution note

For each case, preserve the raw inputs, intermediate arithmetic, event IDs, state deltas, pending effects and resulting state. Do not use expected outcomes as prompts. If the official rule does not determine a detail, label it UNKNOWN or GM_INFERENCE rather than silently inventing a rule.
