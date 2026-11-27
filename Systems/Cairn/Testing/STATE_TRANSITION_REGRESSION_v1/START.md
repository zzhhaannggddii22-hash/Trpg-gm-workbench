# Cairn 2e State Transition Regression v1 — Runner Start

**Mode:** CANDIDATE_VALIDATION / TEST_ONLY_NON_CANON
**System:** cairn / Cairn Second Edition
**Purpose:** Test runtime execution from action input through persistent state commit and handoff recovery.

## Runner discipline

1. Use a clean target chat/runtime. Do not load prior campaign canon or other-system state.
2. Read this file, CASES.md, and the referenced runtime documents only:
   - Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md
   - Systems/Cairn/RUNTIME_PROTOCOL.md
3. Do not read the maintainer regression matrix or ORACLE.md until all cases have been executed and the runner has written its own expected outcomes.
4. Treat every fixture character, location, event, item and timeline as TEST_ONLY_NON_CANON.
5. For each case, report initial state, action, Rule IDs, raw rolls, intermediate values, state delta, after state, pending effects, event IDs, and PASS/FAIL/BLOCKED.
6. Do not silently repair a mismatch. Preserve the failed trace.
7. No case authorizes a formal Cairn Campaign or a change to the system's candidate status.

## Cases to execute

Execute CRT-66 through CRT-87 from CASES.md. Use only the supplied inputs. If a necessary value is missing, state the missing input rather than inventing one.

## Output

Write a case-by-case execution trace and a concise summary. Only after that, compare it against ORACLE.md and record any disagreement. A same-model run is not an independent blind test; identify the execution mode honestly.
