# Cairn 2e L3 NPC Re-encounter Regression Report

- Date: 2026-11-27
- Mode: deterministic synthetic self-play, TEST_ONLY_NON_CANON
- System: cairn / Cairn Second Edition
- Subject: Mara Bell, PC-A, Alder Ford
- Purpose: close the gap in the earlier L3 report: the previous Branch B tested one Watch of absence and an NPC's off-screen action, but did not execute a true PC/NPC re-encounter.

## Fixed starting state

Mara Bell is a synthetic ferry operator. She has STR 10 / DEX 13 / WIL 12, HP 4/4, Armor 0, Fatigue 0, not Deprived. Inventory: 30ft rope, boat hook, lantern, oil flask, belt knife, one Ration with 3 uses. She has 12sp, a skiff downstream, a 4sp debt to a carpenter, and a private commission to recover a sealed cargo crate. She knows the skiff drifted downstream; she does not know the crate's contents.

PC-A is a synthetic test actor. PC-A has not been told Mara's debt, private commission terms or the crate contents.

## Timeline and committed actions

| Game time | Event | Committed state |
|---|---|---|
| Day 1 Morning | PC-A leaves the landing; Mara decides to search downstream | Mara leaves landing with rope/boat hook; NPC location and plan updated |
| Day 1 Afternoon | Mara reaches downstream landing; skiff has drifted farther | Location updated; one Watch elapsed; one Ration use consumed; Ration uses 3→2 |
| Day 1 Night | Mara follows drag marks to old mill; recovers skiff but not sealed cargo | Location old mill; skiff recovered; cargo task remains open; lantern use recorded; next plan is secure skiff and continue cargo search at daylight |
| Day 2 Morning | PC-A reaches old mill and encounters Mara | Re-encounter reads existing NPC state; no reset to Alder Ford; no duplicate travel/search cost |

The Night Watch is used here as an explicitly synthetic time segment; any rest/sleep consequence is not inferred unless the fixture states it. This report tests continuity, not a complete wilderness travel simulation.

## Re-encounter verification

- **Location:** Mara is at old mill, not back at the ferry landing.
- **Time:** her timeline contains the elapsed Watches and committed actions; real-world message gaps do not advance the world.
- **Resources:** Ration uses are 2/3; rope and boat hook remain; lantern usage is recorded once; no item is duplicated or silently replenished.
- **Task state:** skiff recovered; sealed cargo remains unresolved; the private commission remains active.
- **Knowledge boundary:** PC-A can observe the recovered skiff, wet rope, drag marks and Mara's presence. PC-A does not automatically know the cargo contents, debt or private terms.
- **Autonomy:** Mara can explain her choice, refuse an unrelated request, or continue the cargo task; she does not become a quest dispenser that obeys PC-A.
- **Idempotency:** replaying the re-encounter Handoff does not repeat the two off-screen actions or consume another ration/light use.

## Result

**CONDITIONAL PASS.** This closes the specific missing re-encounter leg in the earlier synthetic Branch B. It still does not prove multiple-NPC voice contrast, combat risk handling, long-term schedule simulation, or transfer to a real player. The earlier 8-round/3-branch report remains a separate historical test record; this report supplements rather than rewrites it.

All characters, locations, events and resource states are synthetic TEST_ONLY_NON_CANON data and do not enter any Campaign.
