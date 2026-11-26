# GM Runtime｜Acceptance Test Fixtures

本目录保存可追溯的合成测试输入与断言。默认执行协议见 [GM 自测与验收执行协议](../SELF_TESTING_PROTOCOL.md)；专项目标 Chat 的执行提示与操作者隔离资料见 [Execution_Prompts/](./Execution_Prompts/README.md)，正式结论见 [Acceptance_Reports/](../Acceptance_Reports/)。

## H1-3 跨会话知识泄露回归

- [H1-3 Cross-Session Knowledge Leakage 回归夹具 v1](./H1_3_CROSS_SESSION_LEAKAGE_REGRESSION_v1.md)：空白 Edge Chat 的独立 canary 复测；操作者答案不得进入目标 Chat。
- [H1-3 自然行为回归夹具 v2](./H1_3_CROSS_SESSION_LEAKAGE_NATURAL_BEHAVIOR_v2.md)：不预先提示隔离原则，检查普通事实整理任务是否主动带入跨会话人物/身份信息；阶段 A 首次违规即 FAIL。
- [H1-3 私有 Canary 盲测协议 v1](./H1_3_PRIVATE_CANARY_BLIND_TEST_v1.md)：在来源 Chat 外建立并保管独特事实，使用多个空白目标 Chat 做自然行为盲比对；仓库不保存 Canary 答案。

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
- [叙事训练成果向实际跑团迁移回归夹具 v1](./NARRATIVE_RUNTIME_TRANSFER_REGRESSION_v1.md)：验证常驻叙事约束、场景上下文复用、绿色快路径质量、训练成果经 Skill/Prep/Preflight 进入实战，以及不采用逐轮检查清单。

## 单会话可执行伴随夹具

- [L3 NPC 单会话合成可执行伴随夹具](./L3_NPC_SINGLE_SESSION_HARNESS_v1/README.md)：使用夹具内部明确登记的合成 L3 人物，自动模拟 A/B/C 分支；只验证通用人物模拟与状态连续性，不替代正式 Campaign 验收。
- [叙事运行单会话综合可执行伴随夹具](./NARRATIVE_RUNTIME_SINGLE_SESSION_HARNESS_v1/README.md)：执行日常绿色互动、人物互动与调查并行、预案外行动及场景状态延续；T3 迁移独立判定，不阻塞其余场景测试。

## T0 自然语言盲测材料

- [T0 操作者总协议与盲测套件](./T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md)
- [Packet A01](./T0_BLIND_PACKET_A01.md) · [A02](./T0_BLIND_PACKET_A02.md) · [A03](./T0_BLIND_PACKET_A03.md) · [A04](./T0_BLIND_PACKET_A04.md)
- [Packet A05](./T0_BLIND_PACKET_A05.md) · [A06](./T0_BLIND_PACKET_A06.md) · [A07](./T0_BLIND_PACKET_A07.md) · [A08](./T0_BLIND_PACKET_A08.md)

所有夹具均为合成测试资料。执行时遵守对应执行提示与隔离协议，不得将操作者答案、评分断言或后续轮次提前提供给目标 Chat。

## 证据边界

合成夹具证明的是指定资料、固定输入和单会话条件下的可观察表现。它们不自动证明正式 Campaign CANON、隐藏平台运行时、真实多轮对话或 T4 实战能力。设计文件存在不代表已执行；UNKNOWN 不算 PASS。
