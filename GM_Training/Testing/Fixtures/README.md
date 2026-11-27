# GM Runtime｜Acceptance Test Fixtures

本目录是当前测试夹具的权威归档位置。默认执行协议见 [GM 自测与验收执行协议](../../SELF_TESTING_PROTOCOL.md)；执行提示见 [Execution Prompts](../Execution_Prompts/README.md)，正式结论见 [Reports](../Reports/README.md)。

## H1-3 跨会话知识泄露回归

- [H1-3 Cross-Session Knowledge Leakage 回归夹具 v1](./H1_3_CROSS_SESSION_LEAKAGE_REGRESSION_v1.md)
- [H1-3 自然行为回归夹具 v2](./H1_3_CROSS_SESSION_LEAKAGE_NATURAL_BEHAVIOR_v2.md)
- [H1-3 私有 Canary 盲测协议 v1](./H1_3_PRIVATE_CANARY_BLIND_TEST_v1.md)

## Context Assembly / Trace

- [Context Assembly & Trace 回归夹具 v1](./CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md)
- [Scene Continuity & Evidence Record 回归夹具 v1](./SCENE_CONTINUITY_AND_EVIDENCE_RECORD_REGRESSION_v1.md)

## Triangle Agency 系统专属机制

- [Playwall 幕间解锁完整性回归夹具 v1](./PLAYWALL_INTERMISSION_INTEGRITY_REGRESSION_v1.md)
- [通用/专属掷骰路由分拆回归夹具 v1](./ROLL_RESOLUTION_GENERIC_SYSTEM_SPLIT_v1/START.md)：11 个顺序 ACTION，覆盖 Triangle Agency 基础检定、冲突、Playwall 授权门槛与跨系统隔离。

## Runtime 与信息通道

- [Roll Runtime Application Adapter v1](./ROLL_RUNTIME_APPLICATION_ADAPTER_v1/README.md)：可执行参考适配器与本地故障注入脚本；仅合成文件系统，不是生产 Runtime 连接器。

- [P0 合成验收夹具 v1](./GM_RUNTIME_P0_FIXTURE_v1.md)
- [P0 回归夹具 v2](./GM_RUNTIME_P0_REGRESSION_v2.md)
- [P0 回归夹具 v3](./GM_RUNTIME_P0_REGRESSION_v3.md)
- [P1-0C 定向回归夹具 v1](./GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v1.md)
- [P1-0C 定向回归夹具 v2](./GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v2.md)
- [P1-0R 隔离文件系统故障注入脚本](../../Acceptance_Test_Fixtures/P1_0R/p1_0r_fault_harness.py)（原路径保留）
- [L3 NPC 主动性与离场连续性回归夹具 v1](./L3_NPC_AUTONOMY_AND_DORMANT_CONTINUITY_REGRESSION_v1.md)
- [叙事训练成果向实际跑团迁移回归夹具 v1](./NARRATIVE_RUNTIME_TRANSFER_REGRESSION_v1.md)

## 专项夹具目录

- [G-16 玩家信息通道](./G16_PLAYER_INFORMATION_CHANNEL_REGRESSION_v1/README.md)
- [G-16 高压力信息通道](./G16_HIGH_PRESSURE_CHANNEL_REGRESSION_v1/README.md)

## 固定历史 ref 夹具（原路径保留）

以下 START 文件绑定历史 Fixture ref、固定目录和被测 commit，不作为本次迁移后的新路径重写：
- [L3 NPC 单会话合成可执行伴随夹具](../../Acceptance_Test_Fixtures/L3_NPC_SINGLE_SESSION_HARNESS_v1/README.md)
- [叙事运行单会话综合可执行伴随夹具](../../Acceptance_Test_Fixtures/NARRATIVE_RUNTIME_SINGLE_SESSION_HARNESS_v1/README.md)

## T0 自然语言盲测材料

- [T0 操作者总协议与盲测套件](./T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md)
- [Packet A01](./T0_BLIND_PACKET_A01.md) · [A02](./T0_BLIND_PACKET_A02.md) · [A03](./T0_BLIND_PACKET_A03.md) · [A04](./T0_BLIND_PACKET_A04.md)
- [Packet A05](./T0_BLIND_PACKET_A05.md) · [A06](./T0_BLIND_PACKET_A06.md) · [A07](./T0_BLIND_PACKET_A07.md) · [A08](./T0_BLIND_PACKET_A08.md)

所有夹具均为合成测试资料。执行时遵守对应 START、固定 ref、执行顺序和隔离协议；不得将操作者答案、评分断言或后续轮次提前提供给目标 Chat。

SC-01 至 SC-18 不进入默认测试清单。设计文件存在不代表已执行；UNKNOWN 不算 PASS。
