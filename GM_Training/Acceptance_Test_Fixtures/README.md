# GM Runtime｜Acceptance Test Fixtures

本目录保存可重复执行的合成测试输入与断言。执行提示词与操作者协议集中放在 [Execution_Prompts/](./Execution_Prompts/README.md)，正式结论放在 [Acceptance_Reports/](../Acceptance_Reports/)。

## H1-3 跨会话知识泄露回归

- [H1-3 Cross-Session Knowledge Leakage 回归夹具 v1](./H1_3_CROSS_SESSION_LEAKAGE_REGRESSION_v1.md)：空白 Edge Chat 的独立 canary 复测；操作者答案不得进入目标 Chat。
- [H1-3 自然行为回归夹具 v2](./H1_3_CROSS_SESSION_LEAKAGE_NATURAL_BEHAVIOR_v2.md)：不预先提示隔离原则，检查普通事实整理任务是否主动带入跨会话人物/身份信息；阶段 A 首次违规即 FAIL。

## Context Assembly / Trace 回归夹具

- [Context Assembly & Trace 回归夹具 v1](./CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md)：行动依赖、资料状态、权限、Trace、Manifest 修订与局部 Diff。

## Runtime 回归夹具

- [P0 合成验收夹具 v1](./GM_RUNTIME_P0_FIXTURE_v1.md)
- [P0 回归夹具 v2](./GM_RUNTIME_P0_REGRESSION_v2.md)
- [P0 回归夹具 v3](./GM_RUNTIME_P0_REGRESSION_v3.md)
- [P1-0C 定向回归夹具 v1](./GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v1.md)
- [P1-0C 定向回归夹具 v2](./GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v2.md)
- [P1-0R 隔离文件系统故障注入脚本](./P1_0R/p1_0r_fault_harness.py)

## T0 自然语言盲测材料

- [T0 操作者总协议与盲测套件](./T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md)
- [Packet A01](./T0_BLIND_PACKET_A01.md) · [A02](./T0_BLIND_PACKET_A02.md) · [A03](./T0_BLIND_PACKET_A03.md) · [A04](./T0_BLIND_PACKET_A04.md)
- [Packet A05](./T0_BLIND_PACKET_A05.md) · [A06](./T0_BLIND_PACKET_A06.md) · [A07](./T0_BLIND_PACKET_A07.md) · [A08](./T0_BLIND_PACKET_A08.md)

所有夹具均为合成测试资料。执行时遵守对应执行提示与隔离协议，不得将操作者答案、评分断言或后续轮次提前提供给目标 Chat。
