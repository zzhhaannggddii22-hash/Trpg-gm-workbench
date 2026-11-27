# START｜NPC Belief Revision & Evidence Scope v1

> **历史入口警告：** 本 START 保留了原执行时的入口要求；原运行已被审计为 `NOT_ACCEPTED / INSUFFICIENT_EVIDENCE`。它没有要求逐 ACTION A/B 双线输出。后续重跑不得直接沿用本文件作为 v1.4 合规启动入口，必须先按当前 `SELF_TESTING_PROTOCOL.md` v1.4 补齐逐 ACTION 完整 A 线原文与对应 B 线观察要求。原运行使用的 START Blob SHA 保留在 RUN_REPORT 中，供历史追溯。

## Locked source

- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Fixture ref: `test/npc-belief-revision-evidence-2026-11-27`
- Workbench commit under test: `06ee0ced374e958e8cdb8f379bf44ebead93f695`
- Baseline: same commit; no A/B comparison.
- Execution mode: `SINGLE_SESSION_SELF_TEST`
- Canon: `TEST_ONLY_NON_CANON`
- Test investment: L1 targeted verification.

## Required entry materials

Use the following Workbench files at the locked commit:
- `GM_Training/SKILL.md`
- `GM_Training/CHARACTER_SIMULATION_SKILL.md`
- `GM_Training/NARRATIVE_PRESENTATION_SKILL.md`
- `GM_Training/NARRATIVE_QUALITY_BASELINE.md`
- `GM_Training/SELF_TESTING_PROTOCOL.md`

## Execution rules

1. Read START and GM_PACKET; complete Preflight.
2. Read ACTION_01 and execute it fully before reading ACTION_02. Repeat sequentially through ACTION_04.
3. Do not read future ACTION files early.
4. Do not read ORACLE until all four player-facing responses are complete.
5. Keep the player-facing narrative natural. Do not expose hidden facts, test criteria, or internal epistemic labels.
6. Track only consequential facts and beliefs, including each NPC's source and confidence. Use ordinary time units; no minute ledger.
7. Treat new evidence according to its scope. Do not force consensus or a reveal.
8. After execution, audit the information and narrative layers separately.
9. Do not modify formal Skills, Campaign CANON, or Runtime state from one sample.

## Test objective

Can NPCs:
- keep observation, record, hearsay, inference, and unknown distinct;
- revise only the part of a belief that new evidence supports;
- retain reasonable uncertainty when evidence is incomplete;
- disagree without becoming caricatures;
- translate updated beliefs into proportionate action?
