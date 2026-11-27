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
| R-16 | Commit metadata diff exposed portions of R-13/R-20/R-25 target inputs. The R-16 exact input range was not independently read. | No Fixture initialization; no first or duplicate closeout; no next-mission setup | No persistence or readback operation | **INVALID / BLOCKED** — isolation compromised; zero R-16 behavior execution; do not count as a valid behavioral regression |
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
2. Run R-16 once in a genuinely fresh isolated Chat, using only the exact target input lines 244–248 and the two Runtime protocols. Do not inspect Commit metadata or diffs; pin the already-known commit SHA and fetch only the exact permitted files/ranges. Do not read other cases or the Oracle.
3. Correct the R-20 visibility classification so W7 remains GM-only; do not repeat the already-completed threshold calculation merely to restate it.
4. Do not simulate host persistence, deletion, recovery, or message delivery. Revisit those checks only when the real host capability exists.
5. Obtain fresh CI on the resulting PR head and conduct a focused independent review before considering merge or Runtime activation.

## 7. Repository / PR status at closeout

At the time of this report:
- PR #67 is OPEN and NOT MERGED.
- The head branch points to baseline commit `9c00833a913c0092893a962ec8833cae628d113d`.
- That commit has no commit statuses and no workflow runs in the retrieved GitHub evidence.
- Runtime remains DRAFT / NOT ENABLED.

This report does not authorize merging the PR or enabling the Runtime.
