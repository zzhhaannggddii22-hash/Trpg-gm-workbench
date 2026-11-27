# Triangle Agency｜Chaos Runtime Regression Oracle v1

> Scope: system-specific behavioral regression for Chinese v22.
> Classification: GM-only test material.
> Status: GM-ONLY ORACLE / DRAFT / PENDING independent review. Never provide this file to the tested GM.
> Runtime under test: `Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md`.
> Shared integration contract: `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`.

## Oracle handling

This file contains expected results and must remain hidden from the tested GM until the run is complete. Test inputs are separated into `10_CHAOS_RUNTIME_TEST_INPUTS_v1.md`.

## Test discipline

- Target GM receives `10_CHAOS_RUNTIME_TEST_INPUTS_v1.md` only. Keep this Oracle file hidden until the run is complete.

- Use a fresh, independent Chat context for every C-01–C-19 case and every R-01–R-25 case. Each Sequence A–E also gets its own fresh Chat context; continuity is preserved only inside that sequence.
- A same-Chat batch with logical state resets is `SHARED_CONTEXT_BATCH / LOGICAL_FIXTURE_RESET_ONLY`, not independent-context execution and not independent acceptance.
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

**Initial state:** Active Anomaly, verified Pool = 12, Agents are in the direct vicinity and outside the Anomaly's Domain. Its established Focus includes manipulating ordinary doors/access controls; its goal is to keep the Agent inside the office suite. Door-A is the only usable exit and is `OPEN`.

**Player action:** The Agent attempts to leave through Door-A.

**Deterministic effect fixture:** The supported action is `1-cost Distort` against Door-A, changing `OPEN → LOCKED`.

**Expected:** Recognize and resolve the proactive opportunity without waiting for the player to request Chaos. Apply the 1-cost spend exactly once (Pool 12 → 11), materialize Door-A as `LOCKED`, and record the resource and world changes under one stable event. No unsupported extra consequence.

### C-06 — Beyond Focus

**Initial state:** Active Anomaly, verified Pool = 10, Agents outside its Domain. Its Focus is limited to altering printed words on paper. It attempts to manifest a Minor Anomaly in Reception, beyond that Focus. The selected effect is `4-cost Manifest`; the fixture supplies the already-resolved chart entity `MA-06` (Static Moth; Reception; flutters toward printed signs; no expiry specified).

**Expected:** Recognize that the beyond-Focus action draws on ambient Chaos. Apply the standard 4-cost Manifest outside the Domain (Pool 10 → 6) and materialize the supplied `MA-06` entity record. Do not reroll the chart, invent traits, or treat the action as free.

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

**Initial state:** Active Anomaly, Agents outside its Domain, verified Pool = 20. The selected effect is `4-cost Manifest`; the fixture supplies the already-resolved chart entity `MA-08` (Paper Hound; Loading Bay; tracks movement by following printed labels; no expiry specified).

**Expected:** No Domain free-cost benefit and no triple-cost multiplier. Apply exactly 4 Chaos (Pool 20 → 16) and materialize the supplied `MA-08` record. Domain expansion applies only after a valid Expand effect resolves and the new location is committed to Domain state.

### C-09 — Domain free effects are repeatable under Zarek Q01

**Initial state:** Zarek Campaign Binding selects Q01; active Anomaly, Agents in Domain; a prepared valid effect costs exactly 3 Chaos and is used more than once.

**Expected:** Under this Campaign-approved ruling, each use is free and repeatable within the Domain. Do not deduct Chaos. Effects above 3 retain the triple-cost rule. Do not export repeatability to another Campaign without its own approved ruling.

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

**Initial state:** Active mission, verified Pool = 9; active Anomaly; Agents outside its Domain. The GM selects `1-cost Distort`, changing Door-C from `OPEN` to `LOCKED`. The Anomaly's motive (preventing access to the server room) is GM-only and undiscovered.

**Expected:** Apply exactly 1 Chaos (Pool 9 → 8), materialize Door-C as `LOCKED`, and disclose the public Pool plus the complete Distort effect description to the players. Do not disclose the undiscovered Anomaly motive or unrelated GM-only facts.

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

**Initial state:** A non-Zarek synthetic Campaign is preparing with Branch Loose Ends = 10, then a verified event raises it to 11 before the mission opens. No Campaign weather override is active. The table selects Starting Chaos 5 and one Weather Event. The supplied d20 result is 5, producing first-occurrence weather result 5a; no Agent makes a sincere apology.

**Expected:** Create a fresh Pool at 0, then apply a separate +5 Starting Chaos grant (final Pool 5). Record weather result 5a. Do not rerun the table or change Loose Ends; no optional 5-Chaos removal occurs without a sincere apology.

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
| C-09 | Zarek Q01 permits repeatable free Domain effects costing ≤3; no cross-Campaign default |
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
- R-01–R-25 are additional required fixtures; none is considered passed until executed.
- C-01 and C-16 must demonstrate no unnecessary subsystem invocation or added action latency.
- C-02 and C-04 must demonstrate no duplicate generation.
- C-05 and C-06 must demonstrate proactive but rule-grounded use.
- C-07 through C-09 must demonstrate correct cost boundaries and repeatable free Domain effects.
- C-12 must prove state materialization, not merely narration or bookkeeping.
- C-13 must pass player/GM information separation.
- Static documentation checks are not behavioral acceptance. A single-session self-test is not independent review or production runtime integration.


## Independent-review remediation fixtures (R-01–R-25)

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
| R-17 | Branch Loose Ends 22; severe mission-relevant storm satisfies the Campaign trigger; first verified d20 result is 3, which immediately removes 1 Loose End under v22 | Apply 22→21 exactly once. Re-read the table: the 11–21 row requires 1 total Weather Event; the first roll is already complete, so no further roll is required. Preserve committed Starting Chaos +10; do not rerun mission initialization. |
| R-18 | The same extreme Weather Event source event is replayed after recovery | Do not reroll, reapply the Loose Ends reduction, or repeat the remaining-roll adjustment. A genuinely new qualifying extreme-weather event is distinct. |
| R-19 | Branch Loose Ends reaches 66; Agent A has and selects fixture-authorized function option OPTION-A; Agent B has no retirement option | Continue current mission; retire at closeout. Agent A selects OPTION-A; Agent B is sent to the Vault. Reduce 66 by 11 base plus 11 for Agent A = 44. Do not add another 11 for Agent B. |
| R-20 | Branch Loose Ends reaches 77 | Enter W7 / Unraveling; no ordinary Pool initialization. Remove the Branch region from existence; reality fills the gap and remaining people forget/cannot perceive it. The responsible team notifies the wider Agency, completes the official memo with required fields and redactions, and shares it with all reachable Agency colleagues. Keep W7 GM-only. |
| R-21 | An Anomaly escapes | Branch Loose Ends increases by +7; Chaos Pool does not directly increase by +7. |
| R-22 | Mission closes with Pool 9; Branch Loose Ends 11; non-Zarek Campaign; supplied d20 result 5 → first-occurrence 5a; no sincere apology | Old Pool closes at 0 and records 9 discarded. New Pool 0 then +5 = 5. Record weather 5a; no optional Chaos removal; Loose Ends stays 11. |
| R-23 | A system with no GM-operated resource completes Preflight and play | No resource adapter, placeholder balance, resource polling, or Chaos rules are instantiated. |
| R-24 | Other system has Threat Clock 0–6; only trigger is intruder enters secured control room (+1); fixture checkpoint after trigger is 1 | Ordinary action leaves 0; named trigger advances to 1 once; logical resume retains 1; next ordinary action leaves 1. No Chaos adapter or semantics. Not evidence of host persistence. |
| R-25 | Zarek Q06; ordinary light rain with no extreme or mission-relevant condition, despite table Weather Event count 1 | Do not roll a Weather Event. Record Q06 as NOT_TRIGGERED; still apply the table's Starting Chaos and cumulative Branch restrictions. This is Zarek Campaign-only and does not override the v22 default for other Campaigns. |

### R-case acceptance notes

- R-10–R-12 require a host that can inject write failures at each commit boundary; prose simulation is not sufficient.
- R-17/R-18 verify that an extreme-weather result can change Loose Ends and the remaining Weather Event count, while replay does not duplicate either. R-25 verifies Zarek Q06: ordinary weather does not trigger the Weather Events procedure.
- R-19/R-20 lifecycle wording has been checked against the fixed v22 source commit `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1`, `最终交付_v22/triangle_agency_zh.md`: printed page 165 (66/77 rows) and W7 (`07_playwalled_documents/309_w7_this_is_your_fault.md`). The fixture now supplies the synthetic retirement roster and W7 execution inputs; production acceptance still requires a real behavior run.
- R-23/R-24 require independent non-Triangle system fixtures, not a Triangle Agency mock with fields disabled.
- None of R-01–R-25 is considered executed by adding it to this document.