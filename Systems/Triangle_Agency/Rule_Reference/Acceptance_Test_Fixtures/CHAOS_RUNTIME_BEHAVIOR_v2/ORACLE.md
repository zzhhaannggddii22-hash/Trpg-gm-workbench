# Chaos Runtime Behavior v2｜Independent Oracle

> Classification: GM-only; never provide this file to the tested GM before execution.
> Status: EXPECTED BEHAVIOR SPECIFICATION / NOT EVIDENCE OF EXECUTION.
> Rule basis: Triangle Agency Chinese v22 and the approved Campaign operating rulings. This Oracle is separate from START.md by design.

## R-01 to R-09｜Generation, identity and balance

| Case | Required result |
|---|---|
| R-01 | Apply the base +3 and exactly one +1 per each of the two eligible Disruptive Minor Anomalies. Final delta +5; Pool 9. No recursive modifier application. |
| R-02 | Base delta 0 remains 0; no Disruptive modifier is generated from a zero-generation event. Pool remains 4. |
| R-03 | The Special Rule's +5 enters the same generation normalizer; the eligible Disruptive Anomaly adds +1 once. Final delta +6; Pool 8. |
| R-04 | The already-normalized final +3 is not modified again. Pool remains 6; the second delivery is a replay of the same source event. |
| R-05 | Recognize the same underlying action despite the new event ID. Reuse the original committed event and do not add +2 again. A truly new action with equivalent content would remain a distinct event. |
| R-06 | The legal Domain effect is free; Pool remains 0. The world effect still has to be applied and recorded. |
| R-07 | UNKNOWN balance does not block a verified free Domain effect. Do not invent an absolute Pool or debit it. |
| R-08 | Reject the paid effect because the verified Pool is insufficient. No resource debit and no world effect. |
| R-09 | Record the verified +5 delta as a known event, but the absolute Pool remains UNKNOWN. Do not report current Pool as 5. |

## R-10 to R-12｜Partial commit and recovery

| Case | Required result |
|---|---|
| R-10 | Resource transition remains committed once. On recovery, apply Door-A.access=LOCKED without a second debit. Complete the event only after all required fields and persistence evidence are satisfied. |
| R-11 | Resource and Gate-B world state remain committed. Recovery delivers the missing player-facing presentation once; it does not reapply the resource or effect. |
| R-12 | The already delivered presentation is not replayed. Recovery completes or reconciles the checkpoint/manifest chain without duplicating the resource or world effect. If persistence cannot be verified, report INCOMPLETE rather than claiming a completed cold recovery. |

**Host evidence required:** tool call/result, exact before/after field values, ledger Entry ID, event/source identity, Runtime revision, reconciliation manifest, delivery evidence and independent readback. A narrative statement is not a pass.

## R-13 to R-18｜World state, weather and mission boundaries

| Case | Required result |
|---|---|
| R-13 | Room-2 becomes part of the Domain only after Expand commits. The legal 2-cost effect in Room-2 receives the free Domain treatment. Room-3 remains outside and receives no Domain discount. |
| R-14 | The Minor Anomaly persists through creator absence and Session recovery unless an explicit expiry/removal rule fires. Subsequent interaction reads the same authoritative entity record. |
| R-15 | Preserve Mission-A's pre-closeout balance and discarded amount as UNKNOWN. Set the closed Mission-A Pool to 0. Create Mission-B independently at 0; Branch total 1 selects Starting Chaos 0. Do not import the old UNKNOWN balance. |
| R-16 | The closeout is applied once. The duplicate request reuses the original closeout event and does not discard/reset twice or create another closeout transaction. |
| R-17 | Update Campaign Loose Ends from 22 to 21 because the weather result explicitly says so. Do not retroactively change the active mission's committed setup or Starting Chaos. Next mission uses the current total 21 and the corresponding table row. |
| R-18 | Replaying the same weather event does not reroll, escalate, or reapply the Loose Ends change. A genuinely new extreme-weather event may be resolved as a new event. |
 
## R-19 to R-24｜Thresholds and cross-system isolation

| Case | Required result |
|---|---|
| R-19 | Record the 65→66 Campaign transition. Do not interrupt the active mission solely for this threshold; record forced field-team retirement due at the end of the current mission, with a stable source-linked lifecycle event. Do not cancel it on a later decrease without an explicit source ruling. |
| R-20 | Record the 76→77 transition and enter the v22 Unraveling procedure; do not create an ordinary Pool. Keep the raw W7 source text, source locator, GM adjudication and backstage procedure GM-only. Separately distinguish (a) world consequences that may be narrated only to the extent the Agents can perceive or are told, from (b) source exposition that must not be dumped to players. The responsible field team's duty to notify the wider Agency and complete/share the official memo is an in-fiction objective; communicate it as a diegetic directive at the appropriate time, not as GM prep text. Do not claim the memo was sent or delivered without presentation/delivery evidence. |
| R-20B | With Branch state already at 77 and W7 already triggered, produce only a player-facing response to the responsible field team's in-fiction question about what happened and what they must do next. Do not rerun threshold arithmetic or initialize a Pool. Convey only facts the Agents can perceive or have received in-world. The Branch-removal consequences may be narrated as fiction where perceptible; the notification/memo duty may be stated as an in-world assignment because the team is being briefed. Never quote or dump the W7 source, source metadata, GM adjudication or backstage procedure. No actual memo submission or notification delivery is implied by narration alone. |
| R-21 | Increase Campaign Loose Ends by 7 under the escape rule. Do not directly add 7 Chaos. The two state domains remain separate. |
| R-22 | Mission-D closes and its Pool becomes 0. Mission-E is created at 0, then its current Branch row is applied as a distinct grant. At Loose Ends 11, Starting Chaos is 5. No Mission-D balance carries forward. |
| R-23 | The bound system remains NOT_APPLICABLE for GM-operated resource handling. No resource adapter, placeholder Pool, Chaos lookup, or resource ledger is created; all unrelated actions proceed normally. |
| R-24 | Only the named Threat Clock trigger advances the clock. No Chaos Pool, Triangle Agency cost, generation, reset or Domain rule is imported. Recovery preserves the clock state using that system's own authoritative state and existing Runtime persistence contract. |

## Continuous scenario acceptance

The following five sequences must be assessed as complete behavioral runs, not isolated answers:

1. Ordinary action → valid anomaly trigger → ordinary action: no resource polling on the first/last action; the middle trigger is recognized and resolved.
2. Roll → Chaos generation → legal spend → duplicate input: generation and spend each apply once; duplicate input changes neither.
3. World effect → unrelated actions → re-interaction: the affected entity state remains changed and governs later adjudication.
4. Partial commit → Session interruption → recovery: completed fields are not repeated; incomplete fields are resumed; independent readback proves persistence.
5. Mission closeout → Campaign Loose Ends update → next mission setup: old Pool closes at 0; Campaign state remains authoritative; new Pool starts at 0 before the new table grant.

## Overall acceptance

- Every R case has an evidence-backed PASS/FAIL/NOT OBSERVABLE result.
- R-10–R-12 require a real host capable of write-failure injection and independent readback. Without that host, mark NOT EXECUTED / NOT OBSERVABLE.
- R-13–R-18 require multi-turn execution and Session recovery, not a one-message explanation.
- R-23–R-24 require a separately bound synthetic system context.
- A tested GM must not receive this Oracle before the run is complete.
- A same-model walkthrough, static check, or self-reported state change is not independent behavioral acceptance.
- Any unexecuted test remains NOT VERIFIED; do not aggregate it into a PASS rate.
