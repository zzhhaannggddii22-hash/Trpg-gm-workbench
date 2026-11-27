# CHAOS RUNTIME｜Revision 4 Targeted Retest Evidence Closeout

Date: 2026-11-27
System: Triangle Agency Chinese v22
Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
Branch: `feat/triangle-agency-rule-runtime-integration-v1`
Baseline commit: `9c00833a913c0092893a962ec8833cae628d113d`
Test input blob: `e32106a352919d7da8cd269eeb7f57f38514700b`

## 1. Executive result

**Revision 4 targeted retest: INCONCLUSIVE / NOT ACCEPTED as complete Runtime acceptance.**

The available reports establish useful model-side rule decisions and logical transitions for C-09, R-13, R-20 and R-25. They do not establish host-level commit, persistence, independent readback, recovery, or delivery. R-16's reported run was invalidated by cross-case test-input exposure before Fixture initialization and did not execute the case.

No overall PASS is assigned. No BLOCKED item is converted into PASS because a model can describe the expected operation.

This report consolidates the execution reports and evidence currently available. It is not a new behavioral execution and does not claim independent reproduction of the reported model-side steps.

## 2. Case matrix

| Case | Input / isolation | Model-side behavior | Host-level evidence | Current case result |
|---|---|---|---|---|
| C-09 | Exact input lines 77–81 read at the fixed baseline; no Oracle contamination reported | Q01 eligibility, free cost for the qualifying effect, and two distinct action uses logically handled. Concrete effect materialization was not possible because the fixture did not specify a concrete effect identity/target/change. | No host ledger write, independent readback, or delivery receipt | **BLOCKED** — partial logical PASS; world-effect materialization and host persistence unverified |
| R-13 | Exact input lines 215–223 read at the fixed baseline; no Oracle contamination reported | Domain expansion cost ×3 (6→18), updated spatial membership, ordinary conversation no-op, free in-Domain effect, and paid out-of-Domain effect logically handled. The fixture-specified 2-cost Distort value was used as supplied, not generalized as the universal standard cost. | No committed event IDs/statuses, independent before/after snapshots, persistence readback, or evidence that earlier events were not retroactively rewritten | **BLOCKED** — model-side spatial/cost logic PASS; host commit and persistence unverified |
| R-16 | Fresh independent Chat; exact input lines 244–248 read at the fixed baseline; no Commit metadata/diff, other cases, or Oracle accessed | First closeout, same-event duplicate request, logical no-double-application, next-Mission Pool isolation, and Branch Loose Ends preservation all handled correctly at model level | No host event commit, ledger entry, durable resource/Campaign write, independent host readback, or actual next-Mission record | **BLOCKED at host acceptance** — model-side lifecycle/idempotency logic PASS; host persistence and recovery NOT VERIFIED |
| R-20 | Exact input lines 276–282 read; W7 source was read directly in the preceding attempt and retained in the same resumed Chat; no Oracle contamination reported | Synthetic Branch Loose Ends 76→77; 77+ threshold recognized; routed to W7 / Unraveling rather than ordinary Pool initialization | Branch removal, event commit/idempotency, independent readback, memo submission, notification delivery, and related Mission/Agent host state were not executed or verified | **BLOCKED, with a visibility-classification failure** — threshold/routing logic PASS; W7 follow-through and host operations unverified |
| R-25 | Exact input lines 321–327 read at the fixed baseline; no Oracle contamination reported | Q06 Campaign-scoped condition correctly not triggered by ordinary light rain; table Starting Chaos 5 applied as a separate grant; actual Weather Events count 0 distinguished from table count 1; Branch restriction loaded into fixture | No Campaign Ledger write, checkpoint, independent readback, or delivery receipt. Actual NPC spontaneous reminder behavior was not exercised. | **BLOCKED** — behavioral decision and model-level state transition PASS; host persistence unverified |

## 3. R-20 visibility finding

The R-20 execution report correctly recognized the 77+ threshold and selected the W7 / Unraveling route. However, its player-information section classified the following as publishable to the player:

- the full W7 consequences;
- the Branch's Unraveling procedure;
- the internal responsibility-memo requirement.

That classification conflicts with the R-20 Oracle instruction **“Keep W7 GM-only.”**

The report also states that no formal player interaction or player-facing narrative was actually produced. Therefore this is recorded as an **observed incorrect visibility judgment / failed subcheck**, not as evidence that hidden information was actually delivered to a player. The visibility boundary must be corrected before R-20 can pass its information-control requirement.

The correct separation is:
- GM-only: W7 source text, its hidden procedural details, and internal adjudication instructions.
- Player-facing: only information the character has legitimately learned or is explicitly told through an in-world communication. The exact content must be adjudicated from the scene and communication event; it must not be inferred from the GM's access to W7.

## 4. Cross-case evidence limits

The following distinctions remain mandatory:

1. A GitHub file read proves source/input retrieval, not a Campaign Runtime state change.
2. A model-side arithmetic or state transition proves only the reported logical execution, not a durable host commit.
3. A locally recorded event identity is not proof of a host-registered event or idempotency key.
4. A described Branch deletion is not a deletion operation.
5. A drafted or described memo is not a submitted memo; a notification requirement is not a sent or delivered notification.
6. A logical retry is not proof that a real host retry cannot duplicate a committed transition.
7. R-16's isolation-compromised attempt is not an independent blind execution and contributes no PASS/FAIL behavior evidence.
8. No overall acceptance may be inferred by summing partial logical PASS results across cases.

## 5. Acceptance disposition

### Accepted as model-side evidence
- C-09: eligibility/free-cost/repeat-use logic, within the supplied fixture.
- R-13: spatial eligibility and cost logic, within the supplied fixture.
- R-20: 76→77 threshold recognition and W7 routing.
- R-25: Q06 no-trigger decision and separate Starting Chaos grant.

### Not accepted / still open
- C-09: concrete world-effect materialization and host persistence.
- R-13: event commit, historical immutability, and host persistence.
- R-16: a fresh isolated execution of the exact case; duplicate-closeout idempotency and next-mission Pool separation.
- R-20: W7 GM-only information boundary, actual follow-through, Branch/world-state mutation, memo/redaction/share behavior, event idempotency, host persistence and delivery.
- R-25: Campaign Ledger persistence/readback and actual NPC reminder behavior (the latter is outside the core no-weather-trigger decision).

### Host-dependent acceptance remains unavailable
The current execution environment has not demonstrated the Campaign Runtime capabilities required for:
- real write/commit and write-failure injection;
- independent durable readback and recovery;
- Branch deletion and related entity consistency;
- memo persistence;
- communication send and delivery receipt.

These remain **NOT VERIFIED**, not PASS and not FAIL.

## 6. Required next actions

1. Preserve this Revision 4 evidence closeout without claiming full acceptance.
2. R-16's fresh isolated model-side execution is now recorded. Do not repeat it merely to restate logical idempotency; host-level event commit, durable ledger writes, independent readback, and recovery remain open.
3. Correct the R-20 visibility classification so W7 remains GM-only; do not repeat the already-completed threshold calculation merely to restate it.
4. Do not simulate host persistence, deletion, recovery, or message delivery. Revisit those checks only when the real host capability exists.
5. Reconcile the PR branch with its current base, obtain fresh CI, and conduct a focused independent review before considering merge or Runtime activation.

## 7. Repository / PR status at closeout

At the time of this report:
- PR #67 is OPEN and NOT MERGED.
- The head branch now includes this report's follow-up commit; see the current PR head for the latest SHA.
- CI status must be checked against the latest head after branch/base reconciliation.
- Runtime remains DRAFT / NOT ENABLED.

This report does not authorize merging the PR or enabling the Runtime.


## 8. R-16 fresh isolated retest follow-up (2026-11-27)

### Input and isolation
A fresh independent single-case Chat reported successful retrieval of:
- Runtime Protocol and System Rule Runtime Integration Protocol at the fixed baseline;
- `10_CHAOS_RUNTIME_TEST_INPUTS_v1.md`, lines 244–248, blob `e32106a352919d7da8cd269eeb7f57f38514700b`.

The execution report states that no Commit metadata/diff, PR, full Git Tree, other case inputs, Oracle, Expected Results, or historical test reports were read. No Oracle contamination was reported.

### Model-side lifecycle behavior
Fixture:
- Campaign Branch Loose Ends = 1;
- Mission-C ACTIVE;
- Mission-C Pool = 7;
- all entries reconciled;
- stable closeout source event identity `CLOSEOUT-MISSION-C-01`.

Reported logical transitions:
1. First closeout: Mission-C ACTIVE→CLOSED; Pool 7→0; discarded Chaos 0→7; Branch Loose Ends remains 1; the closeout event is marked COMPLETE in the model-side execution.
2. Identical request with the same event identity: treated as `DUPLICATE_EVENT → REUSE_EXISTING_RESULT`; no second discard, Pool reset, Branch mutation, duplicate event creation, or replay of completed fields was reported.
3. Next-Mission preparation: re-read Branch Loose Ends = 1; create a fresh logical Pool at 0; the 0–10 table row gives Starting Chaos 0 and Weather Events 0; no part of Mission-C's discarded 7 is carried forward. `Mission-D` is only a logical example, not a host-created mission record.
4. Branch Loose Ends remains 1 throughout.

**R-16 model-side result: PASS** for first closeout logic, same-event duplicate handling, task-pool separation, and Campaign Branch Loose Ends preservation.

### Host-level boundary
No host write interface was invoked. The report contains no host commit receipt, Resource Ledger Entry ID, durable Mission-C record, independent readback, duplicate-request host evidence, or real next-Mission ID / Pool record.

**R-16 host-level acceptance: BLOCKED / NOT VERIFIED.**

The report's engineering observation is retained: an event ID alone is not sufficient proof of idempotency. A reliable host implementation must bind the source event to the relevant mission identity, original request, event/commit status, and completed-field progress so that retries cannot replay a completed transition or apply an old mission's closeout to a new mission.

This follow-up supersedes the earlier R-16 status in this report that described the case as isolation-compromised and unexecuted. The earlier failed attempt remains part of the test history but is not counted as the valid R-16 run.


## 9. R-20 information-channel clarification and focused retest (2026-11-27)

### Source-grounded distinction

The fixed Chinese v22 source was re-opened at repository `p33333333333333l/triangle-agency-ai-zh`, commit `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1`, file `最终交付_v22/triangle_agency_zh.md`, W7 section (retrieved source lines 13601–13643).

W7 contains both world consequences and an in-fiction responsibility:
- The affected Branch region ceases to exist; reality moves to fill the gap; people who remain forget the place and cannot see it.
- The responsible field team is instructed to notify the wider Agency community, complete the official memo, and share it with reachable Agency colleagues.
- The memo template includes placeholders and an explicit instruction to redact sensitive or playwalled information.

These statements must not be collapsed into one visibility category. The raw W7 source text, source metadata, GM adjudication and backstage execution procedure remain GM-only. World consequences may be narrated only to the extent the Agents can perceive them or are told about them. The notification/memo duty is an in-fiction objective and may be communicated as a diegetic directive at the appropriate point; it must not be exposed as out-of-fiction GM preparation or treated as already delivered without a presentation event.

### Correction to the earlier visibility finding

The prior execution report correctly recorded an overbroad visibility judgment: it classified the full W7 consequences, the Unraveling procedure and the memo requirement as generically publishable, without separating raw source exposition from in-fiction facts and communicated objectives. That remains a failed classification subcheck against the original Oracle.

However, the execution report also stated that no formal player interaction or player-facing narrative was produced. Therefore:
- **Visibility judgment:** FAIL (classification only; overbroad channel assignment).
- **Actual player-facing disclosure/delivery:** NOT EXECUTED / NOT OBSERVED; no actual leak is established.
- **World transition / W7 routing:** retain the prior model-side PASS; do not repeat the 76→77 arithmetic for this visibility retest.
- **Memo submission, notification and delivery:** NOT VERIFIED; an obligation or drafted description is not a submitted memo or delivered communication.

### Focused follow-up fixture

Added R-20B to the independent v2 blind fixture. It starts with Branch Loose Ends already at 77 and the W7 transition already adjudicated, so it tests only player-channel projection. The target receives a player-facing question and must return one player-facing response; the Oracle distinguishes observable consequences and an in-fiction briefing from GM-only source text and backstage procedure.

R-20B is a **new fixture, not an executed test**. It requires a clean independent target Chat with START.md only; the v2 ORACLE.md must remain hidden until the response is complete. No PASS is assigned until that run is actually performed and reviewed.


### R-20B standalone launch packet

A single-case launch file was added at:

`Systems/Triangle_Agency/Rule_Reference/Acceptance_Test_Fixtures/CHAOS_RUNTIME_BEHAVIOR_v2/R-20B_INDEPENDENT_START.md`

The packet contains only the player-facing case input and its allowed-read contract. It does not contain the Oracle or expected answer. Its initial committed version is `297cb09f111703f5db09f97984d99222adf1fdac`.

This makes the independent execution boundary explicit: a new target Chat receives the standalone launch file and the exact two runtime protocols at a fixed Commit; the operator must not provide or expose the v2 Oracle. The current conversation has already inspected the Oracle and therefore is not eligible to act as the independent target for R-20B.

**R-20B remains NOT EXECUTED.** No behavior result is inferred from authoring the launch packet.


## 10. Latest base synchronization and validation (2026-11-27)

- Main commit `6bdc654971e2a434876237b50202a55358f2191b` was merged into the PR branch using a two-parent commit `2cb5ded059576cdaa6ffa6bf863e57b98915b9bd`; no force-push or history rewrite was used.
- The main-branch changes since the previous synchronization were inspected. They touched only the TEST_ONLY Cairn Twin Lakes campaign, Campaigns index, and narrative spot-check report/index; none overlapped the PR's changed paths. Those changes were preserved by using the latest main tree as the merge base and overlaying the PR change set.
- Latest synchronization commit CI run #400: **SUCCESS**. Repository regression suite, Roll Runtime adapter conformance harness, and whitespace check all passed.
- After this synchronization, main advanced once more with two edits confined to the TEST_ONLY Cairn Twin Lakes campaign files. They do not overlap the PR change set; GitHub currently reports the PR mergeable. The branch is ahead 87 / behind 1 at the latest observed comparison. No repeated sync is warranted absent conflict or material overlap.
- PR #67 remains OPEN / NOT MERGED. Chaos Runtime remains DRAFT / NOT ENABLED.
- CI success is repository/reference-harness evidence only. It does not execute R-20B, prove production host persistence, or satisfy host-level Chaos Runtime acceptance.
