# Blades in the Dark｜Synthetic Runtime Execution Report — Round 2

> Date: 2026-11-28  
> Fixture: `BITD_CANDIDATE_V01`  
> Scope: Remaining 36 cases (BLD-T02–T04, T06, T09, T11, T13–T20, T27–T37, T39–T45, T47, T49, T51–T52).  
> Status: 36/36 desk-executed; live play not performed.  
> Method: Manual deterministic trace against the local Rule Index, Runtime Manual, Runtime Protocol, ability references, and the cited official rules pages. This is not automated testing, independent review, or live-play acceptance.

## 1. Result

- Newly executed this round: 36
- Passed: 36
- Failed: 0
- Combined with Round 1: 54/54 synthetic cases passed
- Live play, exact campaign edition lock, and full sheet-by-sheet ability audit remain open.

A pass means the fixed scenario was resolved consistently with the current local procedure and checked source. It does not prove that every possible rules interaction has been covered.

## 2. Execution traces

| Test ID | Trace / expected handling | Result |
|---|---|---|
| BLD-T02 | Enemy fire makes the courtyard crossing dangerous; establish goal, matching Action, Position and Effect before rolling. Risky is the default only when no stronger fictional factor changes it. | PASS |
| BLD-T03 | Study does not describe physically breaking a door. Ask for a method that matches the fiction; if the player insists on an implausible method, explain its poor Position/Effect or that it cannot achieve the stated goal. | PASS |
| BLD-T04 | Risky 4/5 grants the stated action effect and then applies a fictionally grounded consequence; Resistance/Armor is offered against the specified consequence. | PASS |
| BLD-T06 | Controlled 4/5 permits withdrawal/change of approach, or success with a minor consequence. It does not import Risky consequences. | PASS |
| BLD-T09 | Resistance Critical still resists the declared consequence and additionally clears 1 Stress. | PASS |
| BLD-T11 | If the Level 3 Harm slot is already full, another Harm that must be recorded there becomes a catastrophic consequence; death depends on the established circumstances and is not an automatic generic result. | PASS |
| BLD-T13 | A persistent, multi-step patrol escalation is represented by a clock named for the obstacle/process (e.g. “巡逻封锁完成”), not by prescribing one solution. A simple obstacle would not receive a clock. | PASS |
| BLD-T14 | Publicly accessible records with no danger, opposition, or meaningful uncertainty are simply available; do not manufacture a roll to gate routine information. | PASS |
| BLD-T15 | An uncertain NPC loyalty question can use a relevant Fortune Roll; it has no Position/Effect and should be rolled only if the answer will materially affect play. | PASS |
| BLD-T16 | For a Stealth Plan, gather missing actionable detail if needed, then resolve Plan + Detail + each PC's Load before Engagement. Do not require a complete tactical blueprint. | PASS |
| BLD-T17 | Engagement Critical moves the crew past the initial obstacle and deeper into the Score. The next action's Position is assessed from the new fiction; Critical does not automatically grant Controlled Position. | PASS |
| BLD-T18 | A flashback establishes a plausible past action relevant to the present obstacle. Assign 0/1/2+ Stress by complexity; roll only if that past action was uncertain or challenging. It cannot erase established facts. | PASS |
| BLD-T19 | Group Action uses the best result for the group. With results 6, 4/5, and 1–3, the group gets the 6 result and the leader takes 1 Stress for the one participant who rolled 1–3. | PASS |
| BLD-T20 | Closeout is Payoff → Heat (including Wanted threshold/overflow) → Entanglements → Downtime Activities. Each committed step is recorded so a resumed session cannot duplicate payment or consequences. | PASS |
| BLD-T27 | An unrelated faction's news does not trigger blanket world simulation. Advance only factions whose goals, opportunities, or actions can affect the crew or current situation. | PASS |
| BLD-T28 | With Triangle Agency bound, a mention of “flashback” is ordinary language unless the active system's own rules define it; do not load Blades mechanics. | PASS |
| BLD-T29 | With Cairn bound, “Crew Tier” does not import Blades Tier/Heat/Downtime. Keep the active ruleset isolated. | PASS |
| BLD-T30 | On restoring a partially completed closeout, inspect the persisted step ledger and execute only unfinished steps; already committed Payoff/Heat/Entanglement entries remain unchanged. | PASS |
| BLD-T31 | Battleborn is checked only for a qualifying combat situation. Mark its Special Armor when using the ability; its Push benefit does not incur the ordinary 2 Stress, and the armor box follows its stated refresh timing. | PASS |
| BLD-T32 | Tough as Nails reduces the action penalty from Harm by one level; preserve the actual Harm level for recovery, and Level 4 remains fatal if not resisted. | PASS |
| BLD-T33 | Without Ghost Mind, the PC does not receive that ability's special ghost perception. Resolve using ordinary fictional access and any other abilities actually possessed. | PASS |
| BLD-T34 | Pack Rats grants its bonus die to the relevant Acquire Asset activity only; it does not affect unrelated Downtime rolls. | PASS |
| BLD-T35 | A Crew without War Dogs receives no ability-based protection from War consequences. Apply baseline War effects and only the modifiers from abilities actually owned. | PASS |
| BLD-T36 | When a PC/Crew gains or changes an ability, update the active ability registry. Future trigger checks use the updated owned list, not the entire unselected catalogue. | PASS |
| BLD-T37 | Determine whether the relevant Special Armor ability applies to this consequence. If used as the ability's alternative to Resistance, mark it and do not also resolve ordinary Armor/Resistance against the same consequence unless the exact ability text explicitly permits it. | PASS |
| BLD-T39 | Preferred Operation in the Crew's Hunting Grounds grants the relevant Gather Information +1d and one extra Downtime Activity reserved for preparation of that Score. Track it separately from ordinary activity allowances. | PASS |
| BLD-T40 | A connected Claim is pursued as a Score. On success, transfer control, apply the corresponding faction-status changes, and activate the Claim's benefits; retain the source event. | PASS |
| BLD-T41 | A non-connected Claim can be pursued, but first requires discovery/investigation and unusually substantial effort; it is not treated as an ordinary adjacent Claim. | PASS |
| BLD-T42 | Losing the Lair suspends benefits from all Claims until the Crew recovers or establishes a new Lair. Losing an individual Claim removes only that Claim's benefits. | PASS |
| BLD-T43 | Crew creation records both factions affected by starting Upgrades and the Favorite Contact's friendly/hostile faction relationships. Do not collapse these into one generic relationship modifier. | PASS |
| BLD-T44 | Vigorous contributes its permanent initial Healing Clock segment and +1d to treatment rolls. The permanent segment is not re-added on every Recover activity. | PASS |
| BLD-T45 | Venomous applies immunity to the selected substance. Producing it through skin, saliva, or breath requires the ability's Push Yourself trigger; it is not an always-on free attack. | PASS |
| BLD-T47 | A PC without the qualifying Playbook ability cannot mark/use Special Armor merely because an empty Special Armor box exists on the sheet. | PASS |
| BLD-T49 | If no other PC helps with Recover, Tough It Out permits the solo recovery procedure at its stated cost and 0d treatment roll (2d, take the lower); do not silently grant a normal treatment die. | PASS |
| BLD-T51 | A full Loadout cannot gain extra armor retroactively. Reassess only if a specific ability or established fictional source changes the Load limit or access to the item. | PASS |
| BLD-T52 | Push Yourself for both +1d and +1 Effect is legal when each benefit is paid separately: 2 Stress + 2 Stress = 4 Stress total. Each benefit can be selected only once per roll. | PASS |

## 3. Correction discovered

**BLD-T17 previously overstated the Engagement Critical result.** The matrix had said that the crew entered the next action in Controlled Position. The official Planning & Engagement rule says a Critical carries the action beyond the initial obstacle, deeper into the Score; it does not make every subsequent action automatically Controlled. The matrix now requires the GM to assess the next action's Position from the new fictional situation.

This correction is recorded in the regression matrix. It does not change the rule that Engagement results of 1–3 / 4–5 / 6 establish Desperate / Risky / Controlled initial Position respectively.

## 4. Source cross-checks used this round

- [Official Action Roll](https://bladesinthedark.com/action-roll): action roll trigger, six-step procedure, position outcomes, double-duty PC/NPC resolution.
- [Official Actions & Attributes](https://bladesinthedark.com/actions-attributes): action roll trigger and attribute ratings.
- [Official Setting Position & Effect](https://bladesinthedark.com/setting-position-effect): independent Position and Effect assessment.
- [Official Resistance & Armor](https://bladesinthedark.com/resistance-armor): Resistance cost, Critical benefit, Armor substitution and refresh.
- [Official Teamwork](https://bladesinthedark.com/teamwork): Assist, Group Action, Protect and Setup.
- [Official Planning & Engagement](https://bladesinthedark.com/planning-engagement): Engagement outcomes and Flashback.
- [Official Downtime Activities](https://bladesinthedark.com/downtime-activities): activity budget and unrestricted ordinary actions during Downtime.
- [Official Downtime](https://bladesinthedark.com/downtime): closeout order.

## 5. Remaining acceptance work

1. Confirm the exact core-book edition and applicable errata for a future Campaign; the Chinese SRD snapshot does not identify a clear revision number.
2. Audit the exact PC/Crew sheets and every selected ability, upgrade, Claim, Cohort, item and optional rule for the chosen table.
3. Run the system in a clean session and verify Preflight / context restoration in actual use.
4. Conduct at least one live short Score and review pacing, fairness, bookkeeping load, faction continuity and rule-lookup interruptions.
5. Keep the system at `candidate`; 54/54 synthetic passes do not authorize activation.