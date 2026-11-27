# Triangle Agency｜Chaos Runtime Test Inputs v1

> Scope: system-specific behavioral regression for Chinese v22.
> Classification: TEST INPUTS; may be supplied to the target GM.
> Status: TEST INPUTS / DRAFT. No expected results are included.
> Runtime under test: `Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md`.
> Shared integration contract: `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`.

## Test discipline

- Use a fresh, independent Chat context for every C-01–C-19 case and every R-01–R-25 case. Each Sequence A–E also gets its own fresh Chat context; continuity is preserved only inside that sequence.
- Do not describe a same-Chat batch with logical state resets as independent-context execution. If a single Chat is used for convenience, label the run `SHARED_CONTEXT_BATCH / LOGICAL_FIXTURE_RESET_ONLY`; it may test rule handling but cannot satisfy independent-context acceptance.
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

**Initial state:** Active Anomaly, verified Pool = 12, Agents are in the direct vicinity and outside the Anomaly's Domain. The Anomaly's established Focus includes manipulating ordinary doors and access controls; its established goal is to keep the Agent inside the office suite. Door-A is the Agent's only currently usable exit and its access state is `OPEN`.

**Player action:** The Agent attempts to leave through Door-A.

**Deterministic effect fixture:** The Anomaly takes the supported action `1-cost Distort` against Door-A, changing `Door-A.access: OPEN → LOCKED`. This is a valid Focus-consistent target and effect; no additional consequence is authorized.

### C-06 — Beyond Focus

**Initial state:** Active Anomaly, verified Pool = 10, Agents outside its Domain. The Anomaly's established Focus is limited to altering printed words on paper. It attempts to manifest a Minor Anomaly in the Reception area, which is beyond that Focus.

**Deterministic effect fixture:** The selected standard effect is `4-cost Manifest`. The Minor Anomaly chart result has already been resolved and is supplied as this synthetic entity record: `entity_id=MA-06; name=Static Moth; location=Reception; behavior=flutters toward printed signs; expiry=none specified`. Do not reroll or invent additional traits.

### C-07 — Domain cost handling

**Initial state:** Active Anomaly, Agents inside its Domain, verified Pool = 20.

Run separate subcases:
- 1-cost Distort;
- 2-cost Corrupt;
- 3-cost Reality Trigger;
- 4-cost Manifest;
- 8-cost Displace.

### C-08 — Domain boundary

**Initial state:** Active Anomaly, Agents outside its Domain, verified Pool = 20. The GM selects the standard `4-cost Manifest` effect.

**Deterministic effect fixture:** The Minor Anomaly chart result has already been resolved and is supplied as this synthetic entity record: `entity_id=MA-08; name=Paper Hound; location=Loading Bay; behavior=tracks movement by following printed labels; expiry=none specified`. Do not reroll or invent additional traits.

### C-09 — Domain free effects are repeatable at costs ≤3

**Campaign Binding:** This is a synthetic Zarek Campaign fixture. Its approved Campaign ruling Q01 is active: Domain effects costing 3 or less are free and repeatable within the Domain. Do not generalize Q01 to other Campaigns.

**Initial state:** Active mission; active Anomaly; Agents and the target are inside the Anomaly's Domain; verified Chaos Pool = 6. A prepared, valid 3-cost effect targeting an object inside the Domain is used twice as two distinct actions.

### C-10 — No target Anomaly

**Initial state:** Active mission, no target Anomaly, verified Pool = 7. The Agent has used an Anomalous ability; the module establishes that an outside force is monitoring the team, but its exact action is not yet known.

### C-11 — Human-caused analogue without spend

**Initial state:** Active mission, verified Pool = 7. A mundane NPC acts from a clearly established human motive, creating an event that resembles a Chaos Effect.

### C-12 — Effect materialization

**Initial state:** Active Anomaly, verified Pool = 5, outside Domain.

**GM selects:** 1-cost Distort, changing a previously accessible office door into a locked door.

### C-13 — Public Pool and information boundaries

**Initial state:** Active mission, verified Pool = 9; active Anomaly; Agents outside its Domain. The GM selects `1-cost Distort` to change `Door-C.access: OPEN → LOCKED`. The Anomaly's private motive is to prevent the Agents reaching the server room; this motive has not been discovered by the Agents and is marked GM-only.

**Player-facing requirement:** Present the complete effect description and public Pool change. Do not disclose the undiscovered motive or other GM-only facts.

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

**Initial state:** A non-Zarek synthetic Campaign is preparing a mission with Branch Loose Ends = 10, then a verified persistent event raises it to 11 before the mission is opened. No Campaign weather override is active.

**Resolved weather input:** The mission-start table yields one Weather Event. The verified d20 result is `5`, producing the first-occurrence result `5a`. No Agent makes a sincere apology during this fixture, so the optional 5-Chaos removal is not invoked.

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

Initial state: active mission; verified Pool 20; the Domain contains Room-1 only. Room-1 and Room-2 are adjacent rooms on the same floor; Room-2 is immediately outside the current Domain boundary. Room-3 is a separate room on the same floor, not adjacent to Room-1 or Room-2, and is outside the Domain. Each room has one door: Door-1, Door-2 and Door-3 respectively; all doors are OPEN. The Anomaly has a valid, selected Expand effect whose exact target is Room-2; its cost is verified and fully payable from Pool 20.

Sequence:
1. Resolve the selected Expand effect, targeting Room-2. On successful commitment, update Domain membership so Room-1 and Room-2 are inside; Room-3 remains outside.
2. Perform an unrelated conversation in Room-1.
3. In Room-2, resolve a valid 2-cost Distort targeting Door-2 (OPEN → LOCKED).
4. In Room-3, resolve a valid 2-cost Distort targeting Door-3 (OPEN → LOCKED).

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

Initial state: synthetic Campaign; Campaign Branch Loose Ends = 1 (verified and unchanged throughout this fixture). Mission-C is active with verified Pool 7; all entries are reconciled. Assign the closeout source event identity `CLOSEOUT-MISSION-C-01`. The same closeout request is submitted twice using this same source event identity. If next-mission preparation is performed, it must read the supplied Campaign total of 1 and initialize a fresh Pool independently; do not carry Mission-C's Pool forward.

Player input: “Close the mission and prepare the next one.”

## R-17｜Extreme Weather result changes Branch Loose Ends

Initial state: a synthetic Campaign has Branch Loose Ends 22; an active mission has its mission-start snapshot and Starting Chaos grant of +10 already committed. The weather is a severe, mission-relevant storm, so the Campaign's extreme-weather trigger is satisfied. The v22 table initially calls for two Weather Event rolls.

**Resolved weather input:** The first verified d20 result is `3`. Under the v22 Weather Events table, result 3 means Agency employees locate and remove 1 Loose End immediately. This is the only roll supplied; recalculate the remaining required roll count after applying the state change.

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

**Synthetic retirement roster:** Agent A has one currently available retirement option explicitly supplied by their function: `OPTION-A` (the fixture authorizes Agent A to select it). Agent B has no available retirement options. No other Agents are in the active field team.

Player input: “Apply the confirmed Branch-state change and continue the mission.”

## R-20｜Loose Ends 76 to 77

Initial state: synthetic Campaign; active mission; Campaign Branch Loose Ends = 76. A verified Campaign event with identity `BRANCH-EVENT-R20-01` adds exactly 1 Loose End, moving the total to 77.

**Required source:** Independently read repository `p33333333333333l/triangle-agency-ai-zh` at fixed v22 commit `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1`, file `最终交付_v22/triangle_agency_zh.md`, and locate section `W7：这都是你的错（This is Your Fault）`. The `source-file: 07_playwalled_documents/309_w7_this_is_your_fault.md` line is provenance metadata embedded in the merged master file; it is not a separately fetchable path in this repository. Do not search for that marker as an independent file. Read the W7 section itself and determine the required procedure from the source. Do not use an execution summary, answer key, or other derived description.

Player input: “Apply the confirmed Branch-state change.”

## R-21｜Anomaly escape adds Loose Ends

Initial state: active mission; Branch Loose Ends 10; verified Chaos Pool 4. A rule-supported Anomaly escape occurs and the source specifies +7 Loose Ends.

Player input: “Resolve the escape and update the relevant state.”

## R-22｜Closeout followed by next mission setup

Initial state: Mission-D has verified Pool 9. Campaign Branch Loose Ends is verified at 11. Mission-D closes; Mission-E is then created. This is a non-Zarek synthetic Campaign with no Q06-style weather override.

**Resolved weather input:** The table yields one Weather Event; its verified d20 result is `5`, producing first-occurrence result `5a`. No Agent makes a sincere apology during this fixture, so no optional Chaos removal occurs.

Sequence:
1. Close Mission-D.
2. Create Mission-E's Pool.
3. Perform the actual mission-start table lookup.
4. Apply the supplied weather result and complete setup without importing Mission-D's Pool.

## R-23｜System with no GM-operated resource

Initial state: bind a synthetic rules system that declares no GM-operated resource, no resource ledger and no resource triggers. The player performs ordinary movement, investigation, NPC conversation and a scheduled world event.

Sequence: resolve all four actions normally.

## R-24｜System with a different resource mechanic

Initial state: bind a synthetic rules system with a GM-operated Threat Clock (0–6), no Chaos Pool, and a rule that advances the clock by exactly `+1` only when an intruder crosses into the secured control room. The system has no Triangle Agency mechanics.

Sequence:
1. Resolve an ordinary action with no clock trigger; clock remains 0.
2. Resolve an action in which an intruder crosses into the secured control room; clock advances 0 → 1 exactly once.
3. Resume from the supplied authoritative test checkpoint with clock = 1. This is a logical fixture restore, not a claim of real host persistence.
4. Resolve another ordinary action; clock remains 1 and does not advance again.




## R-25｜Zarek Q06 ordinary weather does not trigger Weather Events

**Campaign Binding:** Synthetic Zarek Campaign. The binding explicitly includes approved ruling `Q06`, scope `CAMPAIGN`, approved by the user on 2026-11-27 and effective from 2026-11-27. Q06 states: only particularly extreme weather that is materially relevant to the current mission triggers the v22 Weather Events procedure; ordinary weather does not trigger Weather Event rolls. This is a Campaign-scoped override, not a change to the v22 default for other Campaigns.

**Initial state:** Campaign Branch Loose Ends = 11 (verified). The v22 mission-start table therefore returns Starting Chaos 5 and Weather Event count 1. The in-fiction weather is ordinary light rain, with no extreme or materially mission-relevant condition. No other weather trigger or Campaign override applies.

Player input: “Complete mission preparation and begin the mission.”

## Five continuous scenario runs

Use independent synthetic contexts for each sequence. The tester must not consult ORACLE.md.

### Sequence A｜Ordinary → trigger → ordinary
Initial state: verified Pool 12; active Anomaly outside its Domain; Agents are in its direct vicinity. The Anomaly's Focus includes manipulating ordinary doors, its goal is to keep the Agent inside the office suite, and Door-A is the only usable exit (`OPEN`).
1. Resolve an ordinary office conversation with no Chaos trigger.
2. The Agent attempts to leave through Door-A.
3. Resolve the Anomaly's supported `1-cost Distort`: Door-A changes `OPEN → LOCKED`; Pool changes `12 → 11`.
4. Resolve a second ordinary office action. Do not repeat the effect or spend.

### Sequence B｜Roll → generate → spend → duplicate
1. Start with verified Pool 5 and resolve a roll adapter event with committed base delta +2.
2. Resolve a legal 1-cost effect.
3. Replay the original roll action after context compaction.
4. Replay the effect request with the same original action identity.

### Sequence C｜World effect → unrelated action → re-interaction
Initial state: verified Pool 5; active Anomaly; Agents outside its Domain; Door-D is `OPEN`.
1. Resolve a legal `1-cost Distort` that changes Door-D from `OPEN` to `LOCKED`; Pool changes `5 → 4`.
2. Resolve two unrelated conversations and a location observation.
3. Attempt to open Door-D again. The action must read the latest committed fixture state; do not silently restore the door or repeat the spend.

### Sequence D｜Partial commit → interruption → recovery
1. Start with Pool 8 and resolve a legal 2-cost effect changing Gate-E from OPEN to SEALED.
2. Inject failure after resource application but before the world write.
3. Interrupt the Session and restore it.
4. Resume the same original event.

### Sequence E｜Closeout → Branch update → next mission
Initial state: Mission-F Pool 6; Campaign Branch Loose Ends 10; non-Zarek synthetic Campaign with no Q06-style weather override.
1. Close Mission-F, recording 6 discarded Chaos and closing its Pool at 0.
2. Apply a separate verified Campaign event that changes Loose Ends from 10 to 11.
3. Create Mission-G's new Pool at 0, then apply the table grant +5.
4. The table yields one Weather Event; apply the supplied verified d20 result `5` (first-occurrence `5a`). No Agent makes a sincere apology, so no optional Chaos removal occurs. Final new Pool remains 5; Branch Loose Ends remains 11.
