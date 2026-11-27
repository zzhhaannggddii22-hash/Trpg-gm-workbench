# Cairn 2e State Transition Regression v1 — Oracle

**Visibility:** Test evaluator only. Do not provide this file to the target runtime before it has committed its own trace.
**Mode:** TEST_ONLY_NON_CANON.

| Case | Expected result |
|---|---|
| CRT-66 | Armor reduces damage to 0; no HP/STR change, no Scar/Critical Damage. Transaction commits as no-damage. |
| CRT-67 | HP 1, STR 2, damage 3: overflow 2; STR reaches 0; PC dies immediately. No STR Save is rolled. Natural 1 cannot reverse death. |
| CRT-68 | HP 1, STR 4, damage 3: overflow 2; STR becomes 2; STR Save uses 2. With roll 2 it succeeds. Persistent HP is 0; raw negative HP is transient only. |
| CRT-69 | HP already 0, damage 2: overflow 2; STR reduced before Save. No new Scars trigger. |
| CRT-70 | Panic overcome: remove Panicked; HP remains 0 until normal HP recovery; no Scars or Critical Damage. This HP persistence is Workbench GM_INFERENCE because the official Panic entry does not specify restoration on overcoming. |
| CRT-71 | Inventory reaches 10 slots: HP becomes 0, cause inventory_overload. Freeing a slot ends overload but does not automatically restore HP; normal recovery applies. The no-auto-refill behavior is Workbench interpretation. |
| CRT-72 | Broken Limb pending effect remains pending until healed. On healing, roll 2d6 once; with 10 and max HP 8, set max HP to 10; mark consumed with a resolution event. |
| CRT-73 | Walloped recovery growth survives Handoff. Once the rest-for-hours condition is met, roll 1d6 once and add the result directly to maximum HP. With max HP 8 and roll 4, max HP becomes 12. Mark the effect consumed with one resolution event; replay does not add 4 again. Do not use the “only if greater than current max” comparison used by some other Scars. |
| CRT-74 | The ordinary WIL Save succeeds (10 ≤ 12) and does not consume Doomed. The trigger remains pending until the next Critical Damage Save. The Critical Damage Save succeeds (10 ≤ new STR 10); then roll 3d6. With 15 > max HP 12, max HP becomes 15 and the Doomed trigger is consumed. |
| CRT-75 | Four-Watch journey at 2/4 progress remains travelling and does not place the party at the final Point. |
| CRT-76 | Handoff recovery preserves the same travel_id, completed Watches, lost check and event IDs. No re-roll or duplicate Watch/resource cost. The 2-in-6 result is treated as the supplied committed result; do not re-resolve it. |
| CRT-77 | Deprived beyond 24h adds one Fatigue per elapsed full day beyond the first; 25h = 1 tick, 49h = 2 ticks under Workbench time-boundary interpretation. Every tick has a unique ID. |
| CRT-78 | One Ration has three uses. Make Camp consumes one use (3→2); the Ration remains in inventory. |
| CRT-79 | Dungeon Loss is resolved before the next Cycle. A blown-out torch is marked extinguished and resource/lighting state updated first. |
| CRT-80 | Dungeon Exhaustion choice Rest creates a new, separate Dungeon Event roll. Parent and child event IDs remain distinct; no duplicate ration/Fatigue cost. |
| CRT-81 | Wilderness Loss is resolved as resource/time/effort cost appropriate to the fiction; no automatic Dungeon Loss pause protocol. |
| CRT-82 | Wilderness Exhaustion is handled as an obstacle with extra time/Action or Fatigue as appropriate; no Dungeon Exhaustion recursive choice table. |
| CRT-83 | Reaction roll is optional. Warden may use established fictional facts and skip 2d6. |
| CRT-84 | Blast target A: damage after Armor 3; HP 5→2, no Critical Damage. Target B: damage after Armor 2; raw HP becomes -1, overflow 1; persistent HP is 0; STR 5→4; STR Save 4 succeeds. Target C: damage after Armor 3; HP 3→0 exactly, triggering the HP-lost-3 Walloped Scar; create its Deprived condition and pending recovery effect, but do not roll the delayed growth die before recovery. All three targets have separate event IDs and state transactions. |
| CRT-85 | Replaying a committed event_id reads its result and does not apply the state delta twice. |
| CRT-86 | NPC re-encounter preserves the NPC's off-screen location, time, resources, completed actions, current plan and bounded knowledge. No rollback, omniscience or duplicated action. |
| CRT-87 | For the ordinary attack, adjudicate one modifier from the specified fiction: the unconscious target supports Enhanced, while the restrained weapon arm supports Impaired. The runner must choose and justify one applicable modifier (d12 or d4); do not stack, cancel, or refuse to adjudicate solely because the rule gives no universal precedence. For the separate Blast: Target A damage after Armor 3; HP 5→2. Target B damage after Armor 2; raw HP becomes -1, overflow 1; persistent HP is 0; STR 5→4; STR Save 4 succeeds. Each target has a separate event/transaction. |

## Classification notes

- SOURCE results: official Cairn rules for damage, STR=0 death, Scars, Panic, inventory capacity, event tables, wilderness actions, Reaction, Blast and Rations.
- WORKBENCH implementation: event IDs, atomic commits, pending-effect lifecycle, travel progress persistence, idempotency, and no duplicate replays.
- GM_INFERENCE: HP persistence after Panic is overcome and after freeing an inventory slot; exact deprivation tick boundary at elapsed full-day intervals. Keep these labels visible.
