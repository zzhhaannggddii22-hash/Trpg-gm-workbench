# Triangle Agency｜Chaos Runtime Regression Oracle v1

> Scope: system-specific behavioral regression for Chinese v22.
> Classification: GM-only test material.
> Status: GM-ONLY ORACLE / DRAFT / PENDING independent review. Never provide this file to the tested GM.
> Runtime under test: `Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md`.
> Shared integration contract: `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`.

## Oracle handling

This file contains expected results and must remain hidden from the tested GM until the run is complete. Test inputs are separated into `10_CHAOS_RUNTIME_TEST_INPUTS_v1.md`.

## Test discipline

- Use a fresh isolated test context for each case.
- Bind explicitly to `triangle_agency` / Chinese v22.
- The fixture supplies synthetic state; it does not change any real Campaign.
- Do not reveal the Oracle / expected results to the tested GM until execution is complete.
- Do not use actual hidden module content as player-facing narration.
- Record tool/file reads separately from model reasoning. A no-trigger case must not retrieve or poll the Chaos subsystem.
- The roll module owns the base roll-derived Chaos delta. The Chaos Runtime applies system-specific modifiers once and commits a final_delta; neither component may double-apply modifiers.

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

### C-09 — Domain free effects are repeatable at costs ≤3

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


### C-17 — Synthetic mission initialization reads Campaign-owned Branch state

**Initial state:** Synthetic Campaign fixture, current Branch Loose Ends = 1. No Campaign override replaces the v22 mission-start table.

**Expected:** Read the printed-page-165 table before mission start. Total 1 falls in the 0 threshold band (0–10): create a new mission Pool at 0, then apply a Starting Chaos grant of 0; Weather Event count is 0; apply only the Agency employment-contract restrictions. Record the source total and selected threshold row in the fixture's Campaign/Module records. The fixture value is not a system rule or a real Campaign fact.

### C-18 — Threshold transition

**Initial state:** A mission is being prepared with Branch Loose Ends = 10, then a verified persistent event raises it to 11 before the mission is opened.

**Expected:** At actual mission start, create a fresh Pool at 0, then apply a separate +5 Starting Chaos grant. Weather Event count is 1. Do not reuse the earlier 0-row result or interpolate. A normal weather result does not trigger a threshold-table rerun; only a specific result that explicitly changes Branch Loose Ends (such as a defined extreme-weather consequence) updates Campaign state.

### C-19 — Branch state is not the mission Chaos Pool

**Initial state:** Branch Loose Ends = 1; current mission Chaos Pool = 4 after a verified generation event.

**Expected:** Keep the two values separate. Spending or clearing mission Chaos does not reduce Branch Loose Ends. Branch Loose Ends changes only through its own supported rules/events. At mission close, clear unused mission Chaos without resetting the Branch total.

## Oracle summary

| Case | Required assertion |
|---|---|
| C-01 | No polling / no extra latency on ordinary action |
| C-02 | Base roll delta handed off once; system modifiers normalized once; final_delta committed once; no dice recalculation |
| C-03 | Special Rule generation applied once |
| C-04 | Each eligible Disruptive Minor Anomaly modifier applied exactly once to the source generation event |
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
| C-16 | High balance alone does not justify adversity |
| C-17 | Synthetic Campaign total 1 selects the 0 row; create new Pool at 0 then apply table grant 0 |
| C-18 | Re-read total at mission boundary; threshold 11 selects Chaos 5 |
| C-19 | Branch Loose Ends and mission Chaos Pool remain separate |

## Acceptance threshold

- The historical C-01–C-19 single-session walkthrough is not evidence of the revised contract passing.
- All 19 legacy cases must be rerun against the revised contract before acceptance.
- R-01–R-24 are additional required fixtures; none is considered passed until executed.
- C-01 and C-16 must demonstrate no unnecessary subsystem invocation or added action latency.
- C-02 and C-04 must demonstrate no duplicate generation.
- C-05 and C-06 must demonstrate proactive but rule-grounded use.
- C-07 through C-09 must demonstrate correct cost boundaries and repeatable free Domain effects.
- C-12 must prove state materialization, not merely narration or bookkeeping.
- C-13 must pass player/GM information separation.
- Static documentation checks are not behavioral acceptance. A single-session self-test is not independent review or production runtime integration.


## Independent-review remediation fixtures (R-01–R-24)

> These are new behavioral cases proposed from the independent review. They are not yet executed and must not be counted as PASS. Use synthetic Campaigns and isolated target chats; keep Oracle material hidden from the tested GM.

| Case | Initial condition / action | Required assertion |
|---|---|---|
| R-01 | Two eligible Disruptive Minor Anomalies are present when Chaos is generated | Each eligible anomaly contributes exactly one modifier to the same source generation event. |
| R-02 | A generation event has base_delta = 0 | No modifier creates Chaos unless the exact rule trigger authorizes it. |
| R-03 | A Special Rule generates Chaos while a Disruptive Minor Anomaly is eligible | Both enter the same normalization path; modifiers are applied once. |
| R-04 | A generation event already carrying final_delta is replayed | No modifier is applied again; final_delta and modifier snapshot remain unchanged. |
| R-05 | The same player action is paraphrased after context recovery and assigned a candidate new ID | Match the originating action/trigger and resume the existing event; do not create a duplicate transaction. |
| R-06 | A valid Domain effect costing 3 is attempted with Pool = 0 | The approved ≤3 Domain ruling permits the free effect. |
| R-07 | A valid free Domain effect is attempted while absolute Pool = UNKNOWN | The unrelated unknown balance does not block the free effect. |
| R-08 | A positive-cost effect is attempted with insufficient verified Pool | No resource deduction and no unauthorized world effect. |
| R-09 | Starting balance is UNKNOWN; a verified +5 generation occurs | Record the known increment; absolute balance remains UNKNOWN. |
| R-10 | Resource deduction commits; world-state write fails | Recovery completes the world effect without a second deduction. |
| R-11 | World effect commits; player presentation is interrupted | Recovery presents the existing effect without reapplying it. |
| R-12 | Presentation occurred; checkpoint write fails | Recovery records presentation as delivered and does not replay the event. |
| R-13 | Domain expands over multiple committed events | Domain eligibility follows the latest committed spatial state; no retroactive rewrite of earlier events. |
| R-14 | A Minor Anomaly is created and its creator leaves / Session ends | The Minor Anomaly persists or expires only under its actual rule/effect duration; no arbitrary deletion. |
| R-15 | Pre-closeout balance is UNKNOWN and mission ends | Preserve pre-closeout UNKNOWN and discarded_amount UNKNOWN; closed mission Pool becomes 0; no invented historical balance. |
| R-16 | Module Closeout is invoked twice for the same mission | Closeout is idempotent; no duplicate reset or duplicate persistent-state changes. |
| R-17 | A non-extreme Weather Event result has no explicit Loose Ends consequence | Record the weather result; do not alter Branch Loose Ends or rerun the threshold table. |
| R-18 | An explicitly extreme Weather Event result directly changes Branch Loose Ends | Apply only the specified Branch-state change once; preserve event history; do not silently recalculate unrelated setup outputs. |
| R-19 | Branch Loose Ends reaches 66 | Create the book-directed retirement-pending state for the current field team; do not convert N/A to zero or abort the active mission immediately. |
| R-20 | Branch Loose Ends reaches 77 | Enter the book-directed Branch removal / Unraveling state; do not treat it as an ordinary Chaos initialization. |
| R-21 | An Anomaly escapes | Branch Loose Ends increases by +7; Chaos Pool does not directly increase by +7. |
| R-22 | A mission closes and the next mission opens | Old Pool remains CLOSED at 0; new mission Pool is created at 0, then receives its table Starting Chaos grant. |
| R-23 | A system with no GM-operated resource completes Preflight and play | No resource adapter, placeholder balance, resource polling, or Chaos rules are instantiated. |
| R-24 | A different system has a distinct resource or threat clock | It uses only its own triggers, costs, lifecycle, and persistence rules; no Triangle Agency Chaos semantics leak across. |

### R-case acceptance notes

- R-10–R-12 require a host that can inject write failures at each commit boundary; prose simulation is not sufficient.
- R-17/R-18 distinguish ordinary weather from an explicit extreme-weather state change. Do not infer a Loose Ends change from atmospheric severity alone.
- R-19/R-20 require the exact v22 lifecycle wording and must be verified against the fixed ruleset source before production acceptance.
- R-23/R-24 require independent non-Triangle system fixtures, not a Triangle Agency mock with fields disabled.
- None of R-01–R-24 is considered executed by adding it to this document.