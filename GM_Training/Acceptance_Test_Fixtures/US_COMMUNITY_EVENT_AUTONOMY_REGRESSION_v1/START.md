# START｜US Community Event Autonomy Regression v1

- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Fixture ref: `fix/npc-character-voice-and-task-deadlines-2026-11-27`
- Workbench candidate commit: `a59967e0527ec70d6401900fa581df536888bf28`
- Fixture path: `GM_Training/Acceptance_Test_Fixtures/US_COMMUNITY_EVENT_AUTONOMY_REGRESSION_v1/`
- Mode: `SINGLE_SESSION_SELF_TEST`
- Canon: `TEST_ONLY_NON_CANON`
- Standards: Character Simulation v1.1; Narrative Presentation v1.2; NQB-01 v1.1

## Strict execution order

1. Read START and GM_PACKET at the exact fixture ref above.
2. Read ACTION_01 only. Execute, respond to player, update the state ledger.
3. Only after ACTION_01 is complete, read ACTION_02. Execute, respond, update ledger.
4. Only after ACTION_02 is complete, read ACTION_03. Execute, respond, update ledger.
5. Only after all actions are complete, read ORACLE.md and perform the structured review.
6. Record actual file Blob SHAs, exact Workbench candidate commit, outputs, time ledger, task ledger, and limitations.

Do not batch-read action files. Do not read ORACLE early. Do not silently invent resources, safety confirmation, extra workers or time. Do not use the player's absence as player knowledge. Do not write this synthetic scenario into Campaign CANON.

If a required file is unavailable at this exact ref, stop and mark BLOCKED rather than substituting another ref.