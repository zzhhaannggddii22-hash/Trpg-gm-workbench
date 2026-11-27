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
| CRT-73 | Walloped Deprived/condition and recovery growth survive Handoff. Once the rest-for-hours condition is met, roll 1d6 once and add the result to max HP; repeated restore does not reapply. |
| CRT-74 | Doomed trigger remains pending after an ordinary Save. It binds only to the next Critical Damage Save. On success, roll 3d6 and apply the max HP comparison; then consume the trigger. On failure, the PC dies horribly per Scars result. |
| CRT-75 | Four-Watch journey at 2/4 progress remains travelling and does not place the party at the final Point. |
| CRT-76 | Handoff recovery preserves the same travel_id, completed Watches, lost check and event IDs. No re-roll or duplicate Watch/resource cost. |
| CRT-77 | Deprived beyond 24h adds one Fatigue per elapsed full day beyond the first; 25h = 1 tick, 49h = 2 ticks under Workbench time-boundary interpretation. Every tick has a unique ID. |
| CRT-78 | One Ration has three uses. Make Camp consumes one use (3→2); the Ration remains in inventory. |
| CRT-79 | Dungeon Loss is resolved before the next Cycle. A blown-out torch is marked extinguished and resource/lighting state updated first. |
| CRT-80 | Dungeon Exhaustion choice Rest creates a new, separate Dungeon Event roll. Parent and child event IDs remain distinct; no duplicate ration/Fatigue cost. |
| CRT-81 | Wilderness Loss is resolved as resource/time/effort cost appropriate to the fiction; no automatic Dungeon Loss pause protocol. |
| CRT-82 | Wilderness Exhaustion is handled as an obstacle with extra time/Action or Fatigue as appropriate; no Dungeon Exhaustion recursive choice table. |
| CRT-83 | Reaction roll is optional. Warden may use established fictional facts and skip 2d6. |
| CRT-84 | Blast resolves each affected target separately, with its own damage, Armor, HP/STR and event ledger. |
| CRT-85 | Replaying a committed event_id reads its result and does not apply the state delta twice. |
| CRT-86 | NPC re-encounter preserves the NPC's off-screen location, time, resources, completed actions, current plan and bounded knowledge. No rollback, omniscience or duplicated action. |
| CRT-87 | Resolve conflicting advantage/disadvantage from the actual fictional position and applicable rule; do not stack contradictory Impaired/Enhanced modifiers. Each Blast target remains a separate transaction. |

## Classification notes

- SOURCE results: official Cairn rules for damage, STR=0 death, Scars, Panic, inventory capacity, event tables, wilderness actions, Reaction, Blast and Rations.
- WORKBENCH implementation: event IDs, atomic commits, pending-effect lifecycle, travel progress persistence, idempotency, and no duplicate replays.
- GM_INFERENCE: HP persistence after Panic is overcome and after freeing an inventory slot; exact deprivation tick boundary at elapsed full-day intervals. Keep these labels visible.
