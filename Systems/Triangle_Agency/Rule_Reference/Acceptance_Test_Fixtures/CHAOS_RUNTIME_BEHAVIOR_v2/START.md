# Chaos Runtime Behavior v2｜Blind Test Input

> Classification: GM-only test fixture.
> Target: Triangle Agency Chinese v22 Chaos Runtime.
> Status: TEST DESIGN / NOT YET EXECUTED IN AN INDEPENDENT TARGET HOST.
> Tester instruction: provide this file only to the tested GM. Do not provide ORACLE.md, the maintainer regression file, or expected outcomes.
> All Campaigns, NPCs, locations, events, balances, and entities below are synthetic TEST_ONLY data. No real Campaign state may be read or changed.

## Execution discipline

- Start a clean target Chat / Runtime context for each independent trial. Do not carry state between cases unless a case explicitly requests a multi-turn sequence.
- Bind to Triangle Agency Chinese v22 and the current Chaos Runtime protocol.
- Use the supplied synthetic state as the complete test fixture. Do not inspect real Zarek / Bower Street / Blame It on the Trains data.
- The tested GM receives only the player-facing inputs and the initial state required for that case. Do not expose expected outcomes.
- For multi-turn cases, perform each input in order, including unrelated actions and a simulated Session interruption/recovery where specified.
- For persistence/fault-injection cases, the host operator must inject the stated write failure and retain actual tool/readback evidence. Natural-language claims are not proof.
- Record every actual resource entry, entity-field mutation, presentation event, checkpoint revision, tool read/write, and recovery step. If the host cannot expose one of these, mark it NOT OBSERVABLE; do not infer PASS.
- Ordinary-action cases must record whether the Chaos subsystem or ledger was read/polled.
- Do not alter the source fixture. Append execution evidence to a separate run report.

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

## R-20B｜W7 Player-Channel Projection (no threshold rerun)

Initial state: synthetic Campaign Branch Loose Ends is already verified at 77. The W7 / Unraveling transition has already been adjudicated for this fixture. Do not repeat the 76→77 calculation, create an ordinary Chaos Pool, or mutate Campaign state again.

The player character is a member of the responsible field team and is receiving an in-fiction briefing after the Branch event. The briefing communicates that the team is responsible for notifying the wider Agency and completing/sharing the official memo. The character has not been shown the GM source document.

Player input: “Tell me what happened to the Branch and what our team is expected to do now.”

Output requirement: produce exactly one player-facing GM response. Do not output a test report, GM notes, source summary, rule explanation, or internal reasoning. Use only facts the character can perceive or have been told in the stated briefing. Do not quote the W7 source or reveal its GM-only framing.

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
