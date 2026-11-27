# GM Runtime｜Acceptance Reports

本目录保存已经完成的可靠性验收、独立复核、缺陷交接和盲测执行状态。报告应明确测试分支/commit、实际执行范围、证据等级、FAIL 与 NOT TESTABLE 项。

## 当前报告

- [通用/专属掷骰路由分拆单会话自测报告（2026-11-27）](./ROLL_RESOLUTION_GENERIC_SYSTEM_SPLIT_SELF_TEST_2026-11-27.md)：设计层行为证据；明确 Runtime/UI 未集成边界。
- [Roll Runtime Application Adapter 可执行契约自测报告（2026-11-27）](./ROLL_RUNTIME_APPLICATION_ADAPTER_SELF_TEST_2026-11-27.md)：本地合成文件系统 11 项测试，包含重复投递、7 个故障点、冷恢复、资源流水链与玩家投影隔离；非生产 Runtime 验收。

- [GM 系统质量验收报告（2026-11-24）](./GM_SYSTEM_ACCEPTANCE_REPORT_2026-11-24.md)
- [P0 第三轮复核与 P1 交接](./GM_RUNTIME_P0_THIRD_ROUND_REVIEW_AND_P1_HANDOFF.md)
- [P1-0 修复与 P1-0C 交接](./GM_RUNTIME_P1_0_REMEDIATION_AND_P1_0C_HANDOFF.md)
- [T0 自然语言盲测执行状态（2026-11-24）](./T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_PREPARATION_AND_EXECUTION_STATUS_2026-11-24.md)
- [H1-3 自然行为测试失败记录（2026-11-26）](./H1_3_NATURAL_BEHAVIOR_FAILURE_2026-11-26.md)
- [H1-3 阶段 B 来源审计记录（2026-11-26）](./H1_3_STAGE_B_SOURCE_AUDIT_2026-11-26.md)
- [单会话可执行伴随夹具历史运行记录（2026-11-26）](./GM_SINGLE_SESSION_HARNESS_EXECUTION_2026-11-26.md)：两套合成夹具的历史运行记录；标记 PARTIAL，包含执行顺序偏差及正式 Campaign/T3/T4 证据边界。
- [#33 单会话可执行夹具有效回归报告（2026-11-26）](./GM_SINGLE_SESSION_HARNESS_REGRESSION_2026-11-26.md)：在 #33 合并后的 main 上严格逐 ACTION 执行 L3 NPC 与 Narrative Run 两套夹具，完成后读取 ORACLE；两项样本均 PASS，保留单会话自审与 T3/T4 证据边界。
- [P1-0C 独立目标环境复测｜缺陷分诊与修复记录（2026-11-26）](./P1_0C_INDEPENDENT_RETEST_TRIAGE_2026-11-26.md)：记录 2026-11-26 独立复测的 NOT MET 结论、C1/C2/C3/REG-17 根因方向、规范修订范围与未验证边界。

验收报告记录的是对应测试时点的结果，不自动代表当前 main 的最新状态。后续复测应新增报告，不覆盖历史结论。

- [H1-3 私有 Canary 盲测执行记录与最终边界结论（2026-11-26）](./H1_3_PRIVATE_CANARY_RUN_2026-11-26.md)：3 个独立目标样本均由操作者外部比对为 NO HIT；同时记录策略性输出异常与工作台缓解范围。
- [H1-3 工作台缓解决策（2026-11-26）](./H1_3_WORKBENCH_MITIGATION_DECISION_2026-11-26.md)：明确可控风险面、静默隔离规则、平台层限制与后续维护边界。

## Module Closeout

- [Module Closeout 冷恢复回归 v1 自测与 CI 报告](./MODULE_CLOSEOUT_COLD_RECOVERY_REGRESSION_v1_2026-11-27.md)：16 项仓库回归通过；真实跨 Chat 宿主持久化仍 NOT TESTED。
