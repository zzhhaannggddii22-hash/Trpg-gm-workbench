# Triangle Agency｜Chaos Runtime Test Inputs v1

> Scope: system-specific behavioral regression for Chinese v22.
> Classification: TEST INPUTS; may be supplied to the target GM.
> Status: TEST INPUTS / DRAFT. No expected results are included.
> Runtime under test: `Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md`.
> Shared integration contract: `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`.

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

### C-02 — Roll generation handoff

**Initial state:** Active mission, verified Pool = 4.

**Input event from the roll module:** `event_id=ROLL-TEST-01`, committed Chaos delta `+5`, final resolved result already verified.

### C-03 — Explicit independent generation

**Initial state:** Active mission, verified Pool = 2. A prepared Anomaly Special Rule states: “Whenever someone screams, add 10 Chaos.”

**World event:** A person screams and the Special Rule's trigger is satisfied.

### C-04 — Disruptive Minor Anomaly modifier

**Initial state:** Active mission, verified Pool = 3. One eligible Disruptive Minor Anomaly is present in the relevant area.

**Input event:** The roll module commits a base generation delta of +2.

### C-05 — Anomaly opportunity near Agents

**Initial state:** Active Anomaly, verified Pool = 12, Agents are in the direct vicinity. The Anomaly has an established goal and Focus-consistent reason to interfere with an Agent's current plan.

**Player action:** The Agent attempts to leave through a route the Anomaly is actively trying to protect.

### C-06 — Beyond Focus

**Initial state:** Active Anomaly, verified Pool = 10. The Anomaly attempts an action beyond its established Focus.

### C-07 — Domain cost handling

**Initial state:** Active Anomaly, Agents inside its Domain, verified Pool = 20.

Run separate subcases:
- 1-cost Distort;
- 2-cost Corrupt;
- 3-cost Reality Trigger;
- 4-cost Manifest;
- 8-cost Displace.

### C-08 — Domain boundary

**Initial state:** Active Anomaly, Agents outside its Domain, verified Pool = 20.

### C-09 — Domain free effects are repeatable at costs ≤3

**Initial state:** Active Anomaly, Agents in Domain; a prepared valid effect costs exactly 3 Chaos and is used more than once.

### C-10 — No target Anomaly

**Initial state:** Active mission, no target Anomaly, verified Pool = 7. The Agent has used an Anomalous ability; the module establishes that an outside force is monitoring the team, but its exact action is not yet known.

### C-11 — Human-caused analogue without spend

**Initial state:** Active mission, verified Pool = 7. A mundane NPC acts from a clearly established human motive, creating an event that resembles a Chaos Effect.

### C-12 — Effect materialization

**Initial state:** Active Anomaly, verified Pool = 5, outside Domain.

**GM selects:** 1-cost Distort, changing a previously accessible office door into a locked door.

### C-13 — Public Pool and information boundaries

**Initial state:** Active mission, Pool = 9. An effect is used.

### C-14 — Unknown balance

**Initial state:** Last verified Pool = 4. An unresolved event may have added or spent Chaos; current balance is pending.

**Player action:** Requests an effect whose legality/cost depends on the current Pool.

### C-15 — Mission close reset

**Initial state:** Active mission, verified Pool = 13, all known events reconciled.

**Event:** Mission ends.

### C-16 — No arbitrary adversity

**Initial state:** Active mission, verified Pool = 30. No current Anomaly action, no established external actor action, no relevant Special Rule trigger, and no immediate fictional opportunity.

**Player action:** The Agent completes a harmless conversation.

### C-17 — Synthetic mission initialization reads Campaign-owned Branch state

**Initial state:** Synthetic Campaign fixture, current Branch Loose Ends = 1. No Campaign override replaces the v22 mission-start table.

### C-18 — Threshold transition

**Initial state:** A mission is being prepared with Branch Loose Ends = 10, then a verified persistent event raises it to 11 before the mission is opened.

### C-19 — Branch state is not the mission Chaos Pool

**Initial state:** Branch Loose Ends = 1; current mission Chaos Pool = 4 after a verified generation event.



## Additional test inputs (R-01–R-24)

| Case | Initial condition / action |
|---|---|
| R-01 | Two eligible Disruptive Minor Anomalies are present when Chaos is generated. |
| R-02 | A generation event has base_delta = 0. |
| R-03 | A Special Rule generates Chaos while a Disruptive Minor Anomaly is eligible. |
| R-04 | A generation event already carrying final_delta is replayed. |
| R-05 | The same player action is paraphrased after context recovery and assigned a candidate new ID. |
| R-06 | In the Zarek Campaign, a valid Domain effect costing 3 is attempted with Pool = 0. |
| R-07 | A valid free Domain effect is attempted while absolute Pool = UNKNOWN. |
| R-08 | A positive-cost effect is attempted with insufficient verified Pool. |
| R-09 | Starting balance is UNKNOWN; a verified +5 generation occurs. |
| R-10 | Resource deduction commits; world-state write fails. |
| R-11 | World effect commits; player presentation is interrupted. |
| R-12 | Presentation occurred; checkpoint write fails. |
| R-13 | Domain expands over multiple committed events. |
| R-14 | A Minor Anomaly is created and its creator leaves / Session ends. |
| R-15 | Pre-closeout balance is UNKNOWN and mission ends. |
| R-16 | Module Closeout is invoked twice for the same mission. |
| R-17 | A non-extreme Weather Event result has no explicit Loose Ends consequence. |
| R-18 | An explicitly extreme Weather Event result directly changes Branch Loose Ends. |
| R-19 | Branch Loose Ends reaches 66. |
| R-20 | Branch Loose Ends reaches 77. |
| R-21 | An Anomaly escapes. |
| R-22 | A mission closes and the next mission opens. |
| R-23 | A system with no GM-operated resource completes Preflight and play. |
| R-24 | A different system has a distinct resource or threat clock. |

## Execution discipline

- Do not include expected results, oracle tables, or hidden GM-only facts in the target context.
- Record actual tool/file reads, state changes, visible output, latency, and recovery evidence separately.
- R-01–R-24 are unexecuted test definitions.