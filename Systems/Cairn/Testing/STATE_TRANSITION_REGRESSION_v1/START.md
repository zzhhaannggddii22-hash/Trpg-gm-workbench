# Cairn 2e State Transition Regression v1 — Runner Start

**Mode:** CANDIDATE_VALIDATION / TEST_ONLY_NON_CANON
**System:** cairn / Cairn Second Edition
**Purpose:** Blind execution test of state transitions, delayed effects, event handling, and handoff recovery.

## Runner discipline

1. Use a clean target chat/runtime. Do not load prior campaign canon, other-system state, or prior test results.
2. Read only these files at the fixed source commit:
   - This file
   - `Systems/Cairn/Testing/STATE_TRANSITION_REGRESSION_v1/CASES.md`
   - `Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md`
   - `Systems/Cairn/RUNTIME_PROTOCOL.md`
   - `Systems/Cairn/Testing/L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md` (only as the fixed input record for CRT-86)
3. Do **not** read `ORACLE.md`, `CORE_RULE_RUNTIME_REGRESSION_MATRIX.md`, execution reports, PR discussions, or other evaluator/maintainer materials. The evaluator will compare your committed output against the Oracle after receiving your report.
4. Do not browse the web or retrieve additional repository files during this fixed-snapshot test. If the supplied runtime documents leave a necessary rule detail unresolved, label it UNKNOWN/BLOCKED and identify the exact missing information; do not silently fill the gap.
5. Treat every fixture character, location, event, item, and timeline as TEST_ONLY_NON_CANON. No state may enter a formal Campaign.
6. Execute CRT-66 through CRT-87 exactly once each. Do not skip a case because it appears repetitive. Do not ask the user questions or wait for confirmation.
7. For each case, report initial state, action, applicable Rule IDs, raw rolls, intermediate values, state delta, resulting state, pending effects, transaction/event IDs, and PASS / FAIL / BLOCKED. Distinguish SOURCE, TABLE_ADAPTATION, GM_INFERENCE, UNKNOWN, and DISPUTED.
8. Do not silently repair a mismatch or rewrite an input. Preserve the failed trace and explain the smallest blocking condition.
9. For CRT-86, use the cited re-encounter report as fixed test input. Do not treat that report's prior CONDITIONAL PASS as evidence that the current execution passes.

## Cases to execute

Execute CRT-66 through CRT-87 from CASES.md. Use only the supplied inputs and the explicitly permitted CRT-86 setup report. If a necessary value is missing, state the missing input rather than inventing one.

## Output

Return one complete case-by-case execution report, followed by:
- a compact result table for CRT-66–CRT-87;
- total PASS / FAIL / BLOCKED counts;
- material rule ambiguities or runtime defects;
- whether any result depended on GM_INFERENCE;
- a clear statement of the execution mode and its limits.

Do not compare against or quote the Oracle. Do not claim that this is a formal Campaign or an independent multi-model validation. The evaluator in a separate chat will perform Oracle comparison after your report is returned.
