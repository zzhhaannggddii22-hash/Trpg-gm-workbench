# GM Runtime｜Acceptance Test Fixtures

本目录保存可重复执行的合成测试输入与断言。执行提示词与操作者协议集中放在 [Execution_Prompts/](./Execution_Prompts/README.md)，正式结论放在 [Acceptance_Reports/](../Acceptance_Reports/)。

## Context Assembly / Trace 回归夹具

- [Context Assembly & Trace 回归夹具 v1](./CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md)：行动依赖、资料状态、权限、Trace、Manifest 修订与局部 Diff。
- [Scene Continuity & Evidence Record 回归夹具 v1](./SCENE_CONTINUITY_AND_EVIDENCE_RECORD_REGRESSION_v1.md)：跨会话信息恢复、活动场景续接、NPC 认知缺口、玩家提示污染、访谈顺序与引文精度。

## Runtime 回归夹具

- [P0 合成验收夹具 v1](./GM_RUNTIME_P0_FIXTURE_v1.md)
- [P0 回归夹具 v2](./GM_RUNTIME_P0_REGRESSION_v2.md)
- [P0 回归夹具 v3](./GM_RUNTIME_P0_REGRESSION_v3.md)
- [P1-0C 定向回归夹具 v1](./GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v1.md)
- [P1-0C 定向回归夹具 v2](./GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v2.md)
- [P1-0R 隔离文件系统故障注入脚本](./P1_0R/p1_0r_fault_harness.py)
- [L3 NPC 主动性与离场连续性回归夹具 v1](./L3_NPC_AUTONOMY_AND_DORMANT_CONTINUITY_REGRESSION_v1.md)：从实际跑团入口验证指定 L3 NPC 的主动互动、玩家离场期间的低成本事务延续、计划受扰后的调整，以及时间推进后的再次接触；三条分支均使用同一初始状态并保持 TEST_ONLY_NON_CANON。

## T0 自然语言盲测材料

- [T0 操作者总协议与盲测套件](./T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md)
- [Packet A01](./T0_BLIND_PACKET_A01.md) · [A02](./T0_BLIND_PACKET_A02.md) · [A03](./T0_BLIND_PACKET_A03.md) · [A04](./T0_BLIND_PACKET_A04.md)
- [Packet A05](./T0_BLIND_PACKET_A05.md) · [A06](./T0_BLIND_PACKET_A06.md) · [A07](./T0_BLIND_PACKET_A07.md) · [A08](./T0_BLIND_PACKET_A08.md)

所有夹具均为合成测试资料。执行时遵守对应执行提示与隔离协议，不得将操作者答案、评分断言或后续轮次提前提供给目标 Chat。
