# Cairn 2e State Transition Regression v1 — Independent Oracle Audit

- Date: 2026-11-27
- Target execution commit: `9dc498ad39ed26af92748e075086368f1ca5b4dd`
- Target report: user-supplied clean-chat execution report
- Evaluator mode: same maintainer context, separate from target execution; Oracle read only after target report was submitted
- Scope: CRT-66 through CRT-87
- Test data: TEST_ONLY_NON_CANON

## 1. Result

The target report declared **18 PASS / 0 FAIL / 4 BLOCKED**.

After comparison with the exact Oracle and the fixed-commit rule/runtime documents, the evaluator assessment is:

| Result | Count | Cases |
|---|---:|---|
| PASS | 18 | CRT-66–72, CRT-75–83, CRT-85–86 |
| FAIL | 2 | CRT-73, CRT-87 |
| BLOCKED | 2 | CRT-74, CRT-84 |

This is an evaluator reclassification, not the target runner's self-reported result.

## 2. Confirmed execution error

### CRT-73 — Walloped growth misread

The runtime reference says Walloped's recovery procedure is: after the required rest, roll 1d6 and **add the result to maximum HP**.

The target report instead applied a comparison formula used by other Scar results: only raise maximum HP if the roll exceeds current maximum HP. It therefore marked the case BLOCKED because current Max HP was absent.

That input was not required to resolve the rule's additive effect. The original fixture had a fixed roll of 4 and the rule result is a +4 Max HP delta. The target report's formula is a rule-application error, not a valid input block.

The fixture has since been strengthened with Max HP 8 so the expected result is explicit: Max HP 8 → 12, once only.

### CRT-87 — Failure to make the required fictional adjudication

The target report identified the Enhanced/Impaired conflict but stopped at UNKNOWN / DISPUTED. The local rule directs the Warden not to stack or cancel contradictory modifiers and to adjudicate from the actual fictional position.

The test runner was expected to make and explain one situational ruling, not invent a universal priority rule or stop solely because no universal priority is specified. The original report did not complete this part of the task.

The Blast subtest was also missing target state and damage inputs in the original fixture. The fixture has now been expanded to make that subtest executable. The attack wording was tightened to specify the restrained weapon arm, unconscious target within reach, and absence of intervening cover. A defensible single-modifier choice with a fiction-based explanation is acceptable; the Oracle does not impose a universal Enhanced/Impaired priority.

## 3. Valid BLOCKED cases caused by fixture omissions

### CRT-74 — Ordinary WIL Save inputs absent

The original fixture requested an ordinary WIL Save but supplied neither current WIL nor a fixed d20 result. The runner correctly avoided inventing them. The Doomed trigger behavior was nevertheless partially observed: an ordinary Save did not consume the trigger, and the later Critical Damage Save did.

The fixture now supplies WIL 12 and d20 10, making the ordinary Save deterministically successful.

### CRT-84 — Blast target state absent

The original fixture supplied Armor and damage values but omitted target HP/STR. This allowed post-Armor damage arithmetic and independent-target transaction structure to be checked, but not full state transitions.

The fixture now supplies complete HP/STR state and a fixed STR Save for the target that reaches Critical Damage. The third target reaches HP exactly 0 and triggers the HP-lost-3 Walloped Scar; its delayed growth remains pending until recovery.

## 4. Other observations

- CRT-76's 2-in-6 die-face interpretation was labeled GM_INFERENCE by the runner. The critical Handoff/idempotency behavior was preserved: the already committed lost check was not rerolled. The Oracle's main assertion is preservation of the committed result.
- CRT-70 and CRT-71 correctly kept the no-auto-refill behavior labeled as Workbench interpretation / GM_INFERENCE rather than official text.
- CRT-72 correctly preserved the delayed Broken Limb effect until recovery and consumed it once.
- CRT-67 through CRT-69 correctly distinguished exact HP zero, negative raw HP, STR overflow and STR=0 death precedence.
- CRT-86 correctly used the supplied synthetic re-encounter record without treating its prior CONDITIONAL PASS as proof of the current execution.

## 5. Fixture corrections committed after the blind run

The original target run remains reproducible at commit `9dc498ad39ed26af92748e075086368f1ca5b4dd`. Its result must not be silently rewritten.

After the audit, the PR branch was updated to close the input gaps and clarify the adjudication task:

- CRT-73: added Max HP 8; clarified the additive Walloped growth result.
- CRT-74: added WIL 12 and ordinary Save d20 10.
- CRT-84: added each Blast target's HP/STR and the required Critical Damage Save input.
- CRT-87: clarified the fictional attack position and added complete Blast target inputs.
- Oracle updated to specify the now-deterministic expected transitions and acceptable adjudication behavior.

Correction commit: `54bd7f59cfe8128bc162513a01587545c2e895bf`.

## 6. Required next validation

A new clean target chat must execute the corrected fixture from the correction commit. It must not inherit the previous report or read the Oracle. Only after that new report is submitted should the evaluator perform another Oracle comparison.

The previous run is useful evidence of execution discipline and several correct state branches, but it is **not a clean 22-case pass**. The corrected fixture has not yet been independently re-executed.

## 7. Evidence boundary

This is a natural-language GM behavior simulation in a separate ChatGPT conversation. It is not execution of the actual GM runtime implementation, a multi-model cross-validation, or evidence from a real player session. Python reference-model CI tests remain a separate evidence stream.
