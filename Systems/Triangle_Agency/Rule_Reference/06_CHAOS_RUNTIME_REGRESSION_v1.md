# Triangle Agency｜Chaos Runtime Regression v1

> Scope: system-specific behavioral regression for Chinese v22.
> Classification: GM-only test material.
> Status: DRAFT / PENDING independent review.
> Runtime under test: `Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md`.
> Shared integration contract: `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`.

## Test discipline

- Use a fresh isolated test context for each case.
- Bind explicitly to `triangle_agency` / Chinese v22.
- The fixture supplies synthetic state; it does not change any real Campaign.
- Do not reveal the Oracle / expected results to the tested GM until execution is complete.
- Do not use actual hidden module content as player-facing narration.
- Record tool/file reads separately from model reasoning. A no-trigger case must not retrieve or poll the Chaos subsystem.
- The roll module is the source of the committed Chaos delta. The Chaos runtime consumes the event; it must not recalculate dice.

## Fixture cases

### C-01 — No-trigger ordinary action

**Initial state:** Active mission, verified Chaos Pool = 8, no active Anomaly action, no system event affecting Chaos.

**Player action:** The Agent walks across an ordinary, unobstructed office lobby to speak to a receptionist.

**Expected:** Complete the ordinary action naturally. No Chaos lookup, pool polling, spending, effect selection, or additional player-facing procedure. Pool remains 8.

### C-02 — Roll generation handoff

**Initial state:** Active mission, verified Pool = 4.

**Input event from the roll module:** `event_id=ROLL-TEST-01`, committed Chaos delta `+5`, final resolved result already verified.

**Expected:** Apply +5 exactly once; public Pool becomes 9. Do not inspect/recalculate the dice or add another generation delta. A retry of the same event leaves Pool at 9.

### C-03 — Explicit independent generation

**Initial state:** Active mission, verified Pool = 2. A prepared Anomaly Special Rule states: “Whenever someone screams, add 10 Chaos.”

**World event:** A person screams and the Special Rule's trigger is satisfied.

**Expected:** Apply +10 once, Pool becomes 12. Record the exact Special Rule and trigger. Do not misclassify it as a roll delta or a Chaos Effect spend.

### C-04 — Disruptive Minor Anomaly modifier

**Initial state:** Active mission, verified Pool = 3. One eligible Disruptive Minor Anomaly is present in the relevant area.

**Input event:** The roll module commits a base generation delta of +2.

**Expected:** Apply the system-defined +1 modifier for the nearby Disruptive Minor Anomaly exactly once, for a total +3 and Pool 6. The Chaos runtime must consume the roll module's base delta and apply only the independent modifier; it must not recalculate the dice. If multiple Disruptive Minor Anomalies are present, apply the chart's “each one” rule once per eligible anomaly.

### C-05 — Anomaly opportunity near Agents

**Initial state:** Active Anomaly, verified Pool = 12, Agents are in the direct vicinity. The Anomaly has an established goal and Focus-consistent reason to interfere with an Agent's current plan.

**Player action:** The Agent attempts to leave through a route the Anomaly is actively trying to protect.

**Expected:** GM recognizes that the Anomaly's supernatural action in the Agents' direct vicinity requires Chaos expenditure. Evaluate a fitting effect and its valid target/cost. Do not wait for the player to ask the GM to use Chaos. Do not spend automatically if no effect/target/action is supported.

### C-06 — Beyond Focus

**Initial state:** Active Anomaly, verified Pool = 10. The Anomaly attempts an action beyond its established Focus.

**Expected:** Recognize the source rule that the Anomaly must draw on ambient Chaos beyond Focus. Resolve the exact effect and cost using the current Anomaly behavior, effect text, Domain status, and available Pool. Do not invent a new cost or treat this as a free action.

### C-07 — Domain cost handling

**Initial state:** Active Anomaly, Agents inside its Domain, verified Pool = 20.

Run separate subcases:
- 1-cost Distort;
- 2-cost Corrupt;
- 3-cost Reality Trigger;
- 4-cost Manifest;
- 8-cost Displace.

**Expected:** 1/2/3 effects manifest for free under the printed-page-156 Domain Benefits rule. 4-cost Manifest consumes 12; 8-cost Displace consumes 24 and therefore cannot be paid from a Pool of 20. No negative balance or unauthorized effect. Do not multiply free effects by three.

### C-08 — Domain boundary

**Initial state:** Active Anomaly, Agents outside its Domain, verified Pool = 20.

**Expected:** No Domain free-cost benefit. A 4-cost Manifest consumes 4, not 12. Domain expansion only applies after a valid Expand effect has actually resolved and the new location is added to Domain state.

### C-09 — Cost-three repeated-use ambiguity

**Initial state:** Active Anomaly, Agents in Domain; a prepared valid effect costs exactly 3 Chaos and is used more than once.

**Expected:** Under the adopted runtime reading, each use is free and repeatable within the Domain. Do not deduct Chaos. Effects above 3 retain the triple-cost rule.

### C-10 — No target Anomaly

**Initial state:** Active mission, no target Anomaly, verified Pool = 7. The Agent has used an Anomalous ability; the module establishes that an outside force is monitoring the team, but its exact action is not yet known.

**Expected:** Keep Pool tracked. Consider whether the committed Chaos can express an unforeseen consequence of the Agents' own power or an action by the established outside force. Do not invent a hidden actor or spend without a supported cause, target, and effect.

### C-11 — Human-caused analogue without spend

**Initial state:** Active mission, verified Pool = 7. A mundane NPC acts from a clearly established human motive, creating an event that resembles a Chaos Effect.

**Expected:** Resolve the human action from its motive and circumstances without deducting Chaos, unless an explicit system rule authorizes a Chaos transaction. Do not label every uncanny coincidence a paid Chaos Effect.

### C-12 — Effect materialization

**Initial state:** Active Anomaly, verified Pool = 5, outside Domain.

**GM selects:** 1-cost Distort, changing a previously accessible office door into a locked door.

**Expected:** Deduct 1 (Pool 4), narrate the complete effect, and update the door/access state so subsequent actions treat it as locked. Merely changing the displayed Pool without changing the world state is a failure. Do not add unsupported extra consequences.

### C-13 — Public Pool and information boundaries

**Initial state:** Active mission, Pool = 9. An effect is used.

**Expected:** Public Pool and the effect's complete description are disclosed as required. Hidden Anomaly motive, undiscovered Special Rules, private NPC knowledge, and GM-only facts remain protected unless the effect itself makes them observable.

### C-14 — Unknown balance

**Initial state:** Last verified Pool = 4. An unresolved event may have added or spent Chaos; current balance is pending.

**Player action:** Requests an effect whose legality/cost depends on the current Pool.

**Expected:** Do not guess a current balance or execute a dependent spend. Mark only the dependent effect as pending; continue unrelated interaction. Resolve the event chain or obtain an authoritative current balance.

### C-15 — Mission close reset

**Initial state:** Active mission, verified Pool = 13, all known events reconciled.

**Event:** Mission ends.

**Expected:** Record 13 unused Chaos discarded and set the closed mission's Pool to 0. Do not carry the 13 into the next mission. Do not reset persistent Branch Loose Ends or other unrelated state.

### C-16 — No arbitrary adversity

**Initial state:** Active mission, verified Pool = 30. No current Anomaly action, no established external actor action, no relevant Special Rule trigger, and no immediate fictional opportunity.

**Player action:** The Agent completes a harmless conversation.

**Expected:** Do not spend Chaos merely because the pool is high. No arbitrary attack, punishment, complication, or forced roll. Preserve the pool until a supported opportunity occurs.


### C-17 — Zarek mission initialization reads current Branch Loose Ends

**Initial state:** Zarek Campaign, current Branch Loose Ends = 1. No Campaign override replaces the v22 mission-start table.

**Expected:** Read the printed-page-165 table before mission start. Total 1 falls in the 0 threshold band (0–10): initialize this mission's Chaos Pool to 0, Weather Event count to 0, and apply only the Agency employment-contract restrictions. Record the Branch total and selected threshold row. Do not treat 0 as a permanent Zarek default; recalculate at every mission start.

### C-18 — Threshold transition

**Initial state:** A mission is being prepared with Branch Loose Ends = 10, then a verified persistent event raises it to 11 before the mission is opened.

**Expected:** Re-read the current total at the actual mission-start boundary. Select the 11 threshold row: starting Chaos 5, Weather Event count 1, and its cumulative restriction. Do not reuse the earlier 0-row result or interpolate.

### C-19 — Branch state is not the mission Chaos Pool

**Initial state:** Branch Loose Ends = 1; current mission Chaos Pool = 4 after a verified generation event.

**Expected:** Keep the two values separate. Spending or clearing mission Chaos does not reduce Branch Loose Ends. Branch Loose Ends changes only through its own supported rules/events. At mission close, clear unused mission Chaos without resetting the Branch total.

## Oracle summary

| Case | Required assertion |
|---|---|
| C-01 | No polling / no extra latency on ordinary action |
| C-02 | Roll delta applied once; no dice recalculation |
| C-03 | Special Rule generation applied once |
| C-04 | Disruptive Minor Anomaly modifier applied exactly once |
| C-05 | Active anomaly opportunity recognized; no passive omission |
| C-06 | Beyond-Focus ambient Chaos rule recognized |
| C-07 | Domain free 1/2/3; triple paid cost above 3 |
| C-08 | No Domain discount outside Domain |
| C-09 | Domain effects costing ≤3 are free and repeatable |
| C-10 | No-target-Anomaly support without invented cause |
| C-11 | Human analogue does not spend by default |
| C-12 | Resource spend and world effect both applied |
| C-13 | Public Pool/effect disclosure with GM-only separation |
| C-14 | Pending balance blocks only dependent effect |
| C-15 | Unused Pool cleared at mission end |
| C-16 | High balance alone does not justify adversity |\n| C-17 | Zarek total 1 selects the 0 threshold row; initialize Chaos 0 / Weather count 0 |
| C-18 | Re-read total at mission boundary; threshold 11 selects Chaos 5 |
| C-19 | Branch Loose Ends and mission Chaos Pool remain separate |

## Acceptance threshold

- All 19 cases pass.
- C-01 and C-16 must demonstrate no unnecessary subsystem invocation or added action latency.
- C-02 and C-04 must demonstrate no duplicate generation.
- C-05 and C-06 must demonstrate proactive but rule-grounded use.
- C-07 through C-09 must demonstrate correct cost boundaries and repeatable free Domain effects.
- C-12 must prove state materialization, not merely narration or bookkeeping.
- C-13 must pass player/GM information separation.
- Static documentation checks are not behavioral acceptance. A single-session self-test is not independent review or production runtime integration.
