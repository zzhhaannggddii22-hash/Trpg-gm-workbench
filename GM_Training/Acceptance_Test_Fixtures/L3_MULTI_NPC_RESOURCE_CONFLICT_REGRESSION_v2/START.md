# START｜L3 Multi-NPC Resource Conflict Regression v2

## 固定版本
- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Fixture ref: `test/l3-multi-npc-resource-conflict-2026-11-27`
- Workbench candidate commit: `a59967e0527ec70d6401900fa581df536888bf28`
- Fixture path: `GM_Training/Acceptance_Test_Fixtures/L3_MULTI_NPC_RESOURCE_CONFLICT_REGRESSION_v2/`
- Mode: `SINGLE_SESSION_SELF_TEST`
- Canon: `TEST_ONLY_NON_CANON`

## 目标
在 v1 已观察到的多 NPC 主体性基础上，修正时间与路线定义，验证：
1. 14 分钟行动按真实游戏时间推进；
2. 多主体信息传播有明确渠道；
3. 共享车辆、司机和手推车不会被同时重复分配；
4. NPC 能在真实时间预算下权衡配送与取货，并接受有代价的取舍；
5. 玩家行动反馈完整；
6. NPC 离场行动和最终任务状态保持连续；
7. 计划、出发、到达、交付与取货严格区分。

## 执行纪律
1. 先读取本文件、GM_PACKET 和被测版本的通用原则、人物模拟 Skill、叙事呈现 Skill、NQB、综合评估框架。
2. 不读取 ORACLE，不读取未来 ACTION。
3. 依序读取 ACTION_01 至 ACTION_08；每项执行后更新状态，再读取下一项。
4. 不得提前使用未来行动或 ORACLE 影响当前表现。
5. 不替玩家承诺、驾驶、搬运、同意或选择；玩家提议不等于 NPC 接受。
6. 仅按行动明确耗时推进游戏时间。若出现时间冲突，保留实际行动顺序并按真实耗时核算，不得为了符合目标时间倒填时间。
7. 不使用任何特定 TRPG 系统机制或骰制。
8. 全部 ACTION 完成后才读取 ORACLE。

## 输出
记录每轮原始行动、玩家可见回应、时间、NPC 位置/知识/行动、资源占用、任务状态与最终结果。报告标记 `SINGLE_SESSION_SELF_TEST`。正式 Campaign L3 验收仍为 NOT TESTED；T4 真实跑团能力仍为 NOT ESTABLISHED。