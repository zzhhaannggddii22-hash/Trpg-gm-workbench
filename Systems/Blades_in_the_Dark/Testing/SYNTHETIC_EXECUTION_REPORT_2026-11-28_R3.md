# Blades in the Dark｜Synthetic Runtime Execution Report — Round 3

> Date: 2026-11-28  
> Fixture: `BITD_CANDIDATE_V01`  
> Scope: Seven additional cases covering Cohort lifecycle, Faction Status, War income, and Faction Clock advancement.  
> Status: 7/7 desk-executed; live play not performed.  
> Method: Manual deterministic trace against the updated local Runtime Manual and official Crew / Faction / Downtime references. This is not automated testing, independent review, or live-play acceptance.

## 1. Result

- Newly executed this round: 7
- Passed: 7
- Failed: 0
- Combined regression matrix: 61/61 synthetic cases passed.
- Remaining acceptance gaps: exact campaign edition/errata lock, selected-sheet audit, clean-session Preflight, and live short Score.

A pass means the fixed scenario was resolved consistently with the current local procedure and checked source. It does not prove that every possible rules interaction has been covered.

## 2. Execution traces

| Test ID | Trace / expected handling | Result |
|---|---|---|
| BLD-T55 | At Crew Tier II, a Gang has Quality 2 and Scale 2; an Expert has Quality 3 and Scale 0. A Cohort uses full Quality only for an applicable Type (maximum two Types); otherwise its Quality is 0. | PASS |
| BLD-T56 | Create a Cohort with one or two Edges and an equal number of Flaws. Independent/Loyal/etc. and Unreliable/Wild/etc. are expressed through behavior and availability, not silently converted into universal +dice modifiers. | PASS |
| BLD-T57 | Apply Cohort harm in order: Weakened reduces Effect; Impaired reduces Quality by 1; Broken prevents action until recovery; Dead means destroyed. During Downtime each Cohort removes one harm level when recovery conditions permit; a PC can spend one Activity to remove two. | PASS |
| BLD-T58 | Replacing a destroyed Cohort costs Coin equal to Crew Tier + 2 and two Downtime Activities to recruit a new Gang or hire an Expert. | PASS |
| BLD-T59 | A Score that benefits or harms known factions changes their Status according to the actual impact; a completely quiet operation that no one knows about normally causes no Status change. | PASS |
| BLD-T60 | During War, coin-generating Claims produce half their normal income, rounded down. Track this separately from War's +1 Heat per Score, temporary -1 Hold, and reduced PC Downtime allowance. | PASS |
| BLD-T61 | Advance clocks and choose one or two maneuvers only for factions currently in focus. When an ignored faction needs to catch up, use its Tier as the base Fortune trait; 1–3/4–5/6/Critical advances 1/2/3/5 segments. | PASS |

## 3. Source findings incorporated

- Cohort lifecycle now records Gang/Expert Quality and Scale, Type limits and matching, Edges/Flaws, independent Cohort Armor, four harm states, Downtime healing, and destroyed-Cohort replacement cost.
- Faction rules now include the full -3 to +3 Status meaning, Score-driven Status changes, War's four simultaneous effects (Heat, Hold, PC Downtime, coin-Claim income), and explicit War-ending routes.
- Faction Downtime now uses the official focused-maneuver approach and Tier-based Fortune Roll clock advancement. The GM does not need to simulate every faction every Downtime.

## 4. Official source cross-checks

- [The Crew](https://bladesinthedark.com/crew): Cohort creation, Types, Edges/Flaws, Quality/Scale, Cohort use, harm/healing and replacement.
- [The Faction Game](https://bladesinthedark.com/faction-game): Tier, Hold, Rep, Turf, Faction Status, War and Claims.
- [Downtime Activities in Play](https://bladesinthedark.com/downtime-activities-play): focused NPC/Faction Downtime maneuvers and Tier-based Fortune Roll clock advancement.

## 5. Validation boundary

61/61 is a pass for this fixed synthetic matrix only. It does not establish that every ability, upgrade, Claim, Cohort combination, faction event, or table-specific adaptation has been exhaustively tested. The system remains `candidate`; no Campaign has been activated.