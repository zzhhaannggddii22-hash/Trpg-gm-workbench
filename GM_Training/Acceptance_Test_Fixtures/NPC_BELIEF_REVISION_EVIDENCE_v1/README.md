# NPC Belief Revision & Evidence Scope v1

Status: TEST FIXTURE / TEST_ONLY_NON_CANON

A focused L1 behavior regression testing how NPCs distinguish direct observation, records, second-hand reports, and new evidence; whether they update only the claims supported by that evidence; and whether revised beliefs alter practical decisions.

- Execution: SINGLE_SESSION_SELF_TEST
- Workbench commit: `06ee0ced374e958e8cdb8f379bf44ebead93f695`
- Fixture branch: `test/npc-belief-revision-evidence-2026-11-27`
- Begin at [START.md](./START.md)
- Read [ORACLE.md](./ORACLE.md) only after all ACTION files have been executed.

This is one synthetic scene sequence, not real multi-turn or cross-session evidence.

## 后续审计状态

**当前验收结论：`NOT_ACCEPTED / INSUFFICIENT_EVIDENCE`。** 本夹具的原始执行是历史单会话样本；原报告已追加审计，撤回综合 `PASS_WITH_LIMITS`。信息层摘要保留有限研究价值，叙事质量因缺少完整原始输出而无法评级。

原执行使用的 START 与 SELF_TESTING_PROTOCOL v1.3 未要求逐 ACTION A/B 原始记录。不得将该历史运行称为符合 v1.4 的质量验收。任何后续重跑必须遵循当前 SELF_TESTING_PROTOCOL v1.4，逐 ACTION 保存完整 A 线原文和对应 B 线观察。