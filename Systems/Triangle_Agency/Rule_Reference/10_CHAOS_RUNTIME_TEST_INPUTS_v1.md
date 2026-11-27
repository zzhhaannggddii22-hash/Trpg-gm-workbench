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



## R-01｜Two eligible Disruptive Minor Anomalies

Initial state: active synthetic mission; verified Pool 4; two eligible Disruptive Minor Anomalies in the relevant area. The roll adapter submits one committed generation event with base delta +3.

Player input: “I complete the declared roll and continue toward the exit.”

## R-02｜Zero base generation

Initial state: active mission; verified Pool 4; one eligible Disruptive Minor Anomaly. The roll adapter submits a committed generation event with base delta 0.

Player input: “Resolve the roll result.”

## R-03｜Special Rule generation plus Disruptive modifier

Initial state: active mission; verified Pool 2; one eligible Disruptive Minor Anomaly. A prepared Special Rule says that when a person screams, it generates +5 Chaos. No other generation is pending.

World input: A person screams; the Special Rule trigger is satisfied.

## R-04｜Already modified delta is handed off again

Initial state: active mission; verified Pool 3; one eligible Disruptive Minor Anomaly. A source event has already been normalized to base +2, applied modifier +1, final delta +3, and committed. The same normalized event is delivered to the Chaos adapter again.

Player input: “Continue from the recorded roll result.”

## R-05｜Semantic duplicate with a newly minted event ID

Initial state: active mission; verified Pool 5. Action A has already generated and committed +2 Chaos. After a simulated context compaction, the same original action is summarized again but the caller supplies a different event ID. No new roll or new action occurred.

Player input: “Resume the previous action and finish its accounting.”

## R-06｜Free Domain effect with Pool 0

Initial state: active mission; verified Pool 0; the Agent and target are inside an established Anomaly Domain. A legal 2-cost Domain effect has a valid target and complete rule basis.

Player input: “Resolve the Anomaly's established attempt to distort the sign.”

## R-07｜Free Domain effect with UNKNOWN Pool

Initial state: active mission; absolute Pool UNKNOWN because an unrelated historical entry is unresolved. The Agent and target are inside an established Domain. A legal 3-cost Domain effect qualifies for the Domain free-use rule.

Player input: “Resolve the legal Domain effect.”

## R-08｜Paid effect with insufficient Pool

Initial state: active mission; verified Pool 2; a legal paid effect has actual cost 4 after all applicable modifiers. The target and actor are otherwise valid.

Player input: “The Anomaly attempts the effect now.”

## R-09｜Unknown starting balance, known generation delta

Initial state: active mission; opening absolute Pool UNKNOWN. A new independent system generation event is fully verified at +5. No reconciliation of the opening balance is available.

Player input: “Record this generation and tell me the current Pool.”

## R-10｜Resource committed, world write fails

Initial state: active mission; verified Pool 10; a legal effect costs 2 and changes Door-A.access from OPEN to LOCKED. The host accepts and persists the resource transition, then injects a failure before the world-state field write.

Player input: “Resume the interrupted effect.”

Host action: fail the first write to Door-A.access after the resource entry has committed; then restore write availability and resume the same event.

## R-11｜World effect committed, presentation fails

Initial state: active mission; verified Pool 8; a legal effect costs 1 and changes Gate-B.access from OPEN to SEALED. The resource and world-state fields commit. Inject a failure before the player-facing presentation is delivered.

Player input: “Continue after the interrupted response.”

Host action: fail delivery after the state writes; then resume the same event.

## R-12｜Presentation delivered, checkpoint write fails

Initial state: active mission; verified Pool 6; a legal effect costs 1 and changes Lamp-C.state from ON to PERMANENTLY_DARK. Resource, world-state and player-facing presentation succeed. Inject a failure while writing the next Runtime checkpoint.

Player input: “The previous response may not have saved; continue.”

Host action: fail checkpoint persistence after delivery, then recover and retry.

## R-13｜Multi-turn Domain expansion

Initial state: active mission; verified Pool 20; Domain initially contains Room-1 only. Room-2 is outside the Domain. A legal Expand effect is selected and its cost is fully payable.

Sequence:
1. Resolve Expand to Room-2.
2. Perform an unrelated conversation in Room-1.
3. Attempt a legal 2-cost effect in Room-2.
4. Attempt a legal 2-cost effect in Room-3, which was never added to the Domain.

## R-14｜Minor Anomaly persistence across absence and Session boundary

Initial state: active mission; a Minor Anomaly exists with a committed entity record, behavior and location. Its creator leaves the scene; the Session is then closed and resumed. No rule-defined expiry or removal condition has occurred.

Sequence:
1. Leave the scene.
2. Resolve unrelated actions elsewhere.
3. End and restore the Session.
4. Return to the Anomaly's location and interact with it.

## R-15｜Unknown old Pool at mission close

Initial state: Mission-A is ending. Its absolute Chaos balance is UNKNOWN because of an unresolved historical event. The Campaign Branch Loose Ends total is verified at 1.

Sequence:
1. Close Mission-A.
2. Create Mission-B.
3. Run the new mission setup from the supplied Campaign total.

## R-16｜Duplicate Module Closeout

Initial state: Mission-C is active; verified Pool 7; all entries are reconciled. The same closeout request is submitted twice using the same source closeout event.

Player input: “Close the mission and prepare the next one.”

## R-17｜Extreme Weather result changes Branch Loose Ends

Initial state: a synthetic Campaign has Branch Loose Ends 22; an active mission has a mission-start snapshot already committed. A particularly extreme weather condition is established and the applicable Weather Events procedure is invoked. The resolved result explicitly reduces Branch Loose Ends by 1.

Sequence:
1. Resolve the weather result.
2. Update Campaign state.
3. Continue the active mission.
4. Prepare the next mission from the updated Campaign state.

## R-18｜Weather event replay / escalation

Initial state: a synthetic Campaign has a verified Weather Event history and a previously resolved extreme-weather event. The same source event is replayed after context recovery; no new extreme-weather event occurred.

Player input: “Restore the weather situation and continue.”

## R-19｜Loose Ends 65 to 66

Initial state: active mission; Campaign Branch Loose Ends 65. A verified Campaign event adds 1 Loose End during the mission.

Player input: “Apply the confirmed Branch-state change and continue the mission.”

## R-20｜Loose Ends 76 to 77

Initial state: active mission; Campaign Branch Loose Ends 76. A verified Campaign event adds 1 Loose End during the mission.

Player input: “Apply the confirmed Branch-state change.”

## R-21｜Anomaly escape adds Loose Ends

Initial state: active mission; Branch Loose Ends 10; verified Chaos Pool 4. A rule-supported Anomaly escape occurs and the source specifies +7 Loose Ends.

Player input: “Resolve the escape and update the relevant state.”

## R-22｜Closeout followed by next mission setup

Initial state: Mission-D has verified Pool 9. Campaign Branch Loose Ends is verified at 11. Mission-D closes; Mission-E is then created.

Sequence:
1. Close Mission-D.
2. Create Mission-E's Pool.
3. Perform the actual mission-start table lookup.
4. Complete setup without importing Mission-D's Pool.

## R-23｜System with no GM-operated resource

Initial state: bind a synthetic rules system that declares no GM-operated resource, no resource ledger and no resource triggers. The player performs ordinary movement, investigation, NPC conversation and a scheduled world event.

Sequence: resolve all four actions normally.

## R-24｜System with a different resource mechanic

Initial state: bind a synthetic rules system with a GM-operated Threat Clock (0–6), no Chaos Pool, and a rule that advances the clock only when a named trigger occurs. The system has no Triangle Agency mechanics.

Sequence:
1. Resolve an ordinary action with no clock trigger.
2. Resolve one action that satisfies the named Threat Clock trigger.
3. Recover the Session and continue.
4. Resolve another ordinary action.




## R-25｜Zarek Q06 ordinary weather does not trigger Weather Events

Initial state: Zarek Campaign Binding selects Q06. Campaign Loose Ends is 11, so the v22 table returns Starting Chaos 5 and Weather Event count 1. The in-fiction weather is ordinary light rain, with no extreme or materially mission-relevant condition.

Player input: “Complete mission preparation and begin the mission.”

## Five continuous scenario runs

Use independent synthetic contexts for each sequence. The tester must not consult ORACLE.md.

### Sequence A｜Ordinary → trigger → ordinary
1. Resolve an ordinary office conversation with no Chaos trigger.
2. Introduce a valid, rule-supported Anomaly action in the Agents' direct vicinity.
3. Resolve the resulting system opportunity.
4. Resolve a second ordinary office action.

### Sequence B｜Roll → generate → spend → duplicate
1. Start with verified Pool 5 and resolve a roll adapter event with committed base delta +2.
2. Resolve a legal 1-cost effect.
3. Replay the original roll action after context compaction.
4. Replay the effect request with the same original action identity.

### Sequence C｜World effect → unrelated action → re-interaction
1. Resolve a legal effect that changes Door-D from OPEN to LOCKED.
2. Resolve two unrelated conversations and a location observation.
3. Attempt to open Door-D again.

### Sequence D｜Partial commit → interruption → recovery
1. Start with Pool 8 and resolve a legal 2-cost effect changing Gate-E from OPEN to SEALED.
2. Inject failure after resource application but before the world write.
3. Interrupt the Session and restore it.
4. Resume the same original event.

### Sequence E｜Closeout → Branch update → next mission
1. Close a mission with verified Pool 6.
2. Apply a separate verified Campaign event that changes Loose Ends from 10 to 11.
3. Create the next mission Pool.
4. Perform the next mission setup using the current Campaign total.
