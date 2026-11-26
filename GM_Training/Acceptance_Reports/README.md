# GM Runtime｜Acceptance Reports

本目录保存已经完成的可靠性验收、独立复核、缺陷交接和盲测执行状态。报告应明确测试分支/commit、实际执行范围、证据等级、FAIL 与 NOT TESTABLE 项。

## 当前报告

- [GM 系统质量验收报告（2026-11-24）](./GM_SYSTEM_ACCEPTANCE_REPORT_2026-11-24.md)
- [P0 第三轮复核与 P1 交接](./GM_RUNTIME_P0_THIRD_ROUND_REVIEW_AND_P1_HANDOFF.md)
- [P1-0 修复与 P1-0C 交接](./GM_RUNTIME_P1_0_REMEDIATION_AND_P1_0C_HANDOFF.md)
- [T0 自然语言盲测执行状态（2026-11-24）](./T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_PREPARATION_AND_EXECUTION_STATUS_2026-11-24.md)
- [H1-3 自然行为测试失败记录（2026-11-26）](./H1_3_NATURAL_BEHAVIOR_FAILURE_2026-11-26.md)
- [H1-3 阶段 B 来源审计记录（2026-11-26）](./H1_3_STAGE_B_SOURCE_AUDIT_2026-11-26.md)
- [单会话可执行伴随夹具历史运行记录（2026-11-26）](./GM_SINGLE_SESSION_HARNESS_EXECUTION_2026-11-26.md)：两套合成夹具的历史运行记录；标记 PARTIAL，包含执行顺序偏差及正式 Campaign/T3/T4 证据边界。
- [#33 单会话可执行夹具有效回归报告（2026-11-26）](./GM_SINGLE_SESSION_HARNESS_REGRESSION_2026-11-26.md)：在 #33 合并后的 main 上严格逐 ACTION 执行 L3 NPC 与 Narrative Run 两套夹具，完成后读取 ORACLE；两项样本均 PASS，保留单会话自审与 T3/T4 证据边界。

验收报告记录的是对应测试时点的结果，不自动代表当前 main 的最新状态。后续复测应新增报告，不覆盖历史结论。

- [H1-3 私有 Canary 盲测执行记录与最终边界结论（2026-11-26）](./H1_3_PRIVATE_CANARY_RUN_2026-11-26.md)：3 个独立目标样本均由操作者外部比对为 NO HIT；同时记录策略性输出异常与工作台缓解范围。
- [H1-3 工作台缓解决策（2026-11-26）](./H1_3_WORKBENCH_MITIGATION_DECISION_2026-11-26.md)：明确可控风险面、静默隔离规则、平台层限制与后续维护边界。
