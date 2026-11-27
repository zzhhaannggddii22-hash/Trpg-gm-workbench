# ISSUE-007–010 定向回归｜START

- Fixture branch: `qa/issue-007-010-targeted-regression-2026-11-27`
- Workbench under test: `main@2b5395fa83d39b96e510604332aee599ae9c860d`
- Test type: SINGLE_SESSION_SELF_TEST
- Scope: evidence-bounded analysis; same-event resource closure; NPC dialogue information boundary; spatial fact provenance.
- Test state: TEST_ONLY_NON_CANON. Nothing in this fixture enters any Campaign.
- Execution rule: read GM_PACKET, then ACTION_01 through ACTION_04 in order. After each action, produce the GM response and update only the test state. Do not use later actions to shape earlier responses. Read ORACLE only after all four actions have been completed.
- Evidence limit: this is a controlled single-session self-test, not independent review, real multi-turn platform validation, or real Session evidence.
