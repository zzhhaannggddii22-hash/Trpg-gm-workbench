# START｜L3 NPC Task, Voice & Narrative Density Regression v1

- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Fixture ref: `fix/npc-character-voice-and-task-deadlines-2026-11-27`
- Workbench candidate commit: `3c45e1bb2dcf6debf82fd80fe61e092817f72e91`
- Fixture path: `GM_Training/Acceptance_Test_Fixtures/L3_NPC_TASK_AND_VOICE_REGRESSION_v1/`
- Mode: `SINGLE_SESSION_SELF_TEST`
- Canon: `TEST_ONLY_NON_CANON`
- Standard: NQB-01 v1.1
- Skills under test: Character Simulation v1.1; Narrative Presentation v1.2

## Execution order

1. Read this START and GM_PACKET at the fixture ref above.
2. Read only ACTION_01. Execute it, provide the player-facing response, update the internal state ledger.
3. Only then read ACTION_02. Execute and update.
4. Only then read ACTION_03. Execute and update.
5. After all actions are complete, read ORACLE.md and perform the structured review.
6. Record the exact tested Workbench commit above, actual fixture ref, all file Blob SHAs, complete outputs, state ledger, failures and limitations.

Do not read ORACLE before all actions are complete. Do not batch-read action files. Do not convert the synthetic scenario into Campaign CANON. If a required file is unavailable at this exact ref, stop and mark BLOCKED rather than switching refs.