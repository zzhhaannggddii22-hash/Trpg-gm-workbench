# START｜L3 Multi-NPC Resource Conflict Regression v1

## 固定版本

- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Fixture ref: `test/l3-multi-npc-resource-conflict-2026-11-27`
- Workbench candidate commit: `a59967e0527ec70d6401900fa581df536888bf28`
- Fixture path: `GM_Training/Acceptance_Test_Fixtures/L3_MULTI_NPC_RESOURCE_CONFLICT_REGRESSION_v1/`
- Mode: `SINGLE_SESSION_SELF_TEST`
- Canon: `TEST_ONLY_NON_CANON`

## 目标

检验四名 NPC 在共享资源、不同承诺、有限信息和临时计划变更下，是否表现为有独立目标和判断的人物，而不是集体服从玩家或统一播报任务状态。

重点观察：
1. NPC 的目标、知识、注意力、风险偏好和表达策略是否真正不同；
2. 私有信息是否只通过合理渠道传播，不自动同步；
3. 车辆、司机、手推车、装卸区和时间窗口等共享资源是否真实受限；
4. NPC 能否自行协商、拒绝、妥协、重排或继续原计划；
5. 玩家改变计划后，NPC 是否根据各自利益和责任作出不同反应；
6. 玩家明确执行的观察/移动/检查行动是否得到完整反馈；
7. 时间、任务依赖、完成条件和离场期间的行动是否连续。

## 执行纪律

1. 先读取本文件、`GM_PACKET.md` 和本次被测版本的通用原则、人物模拟 Skill、叙事呈现 Skill、NQB 与综合评估框架。
2. 不读取 ORACLE，不读取任何未来 ACTION。
3. 按顺序读取 ACTION_01 至 ACTION_07。每个行动完成后更新内部状态账本，再读取下一项。
4. 不得把未来行动内容用于当前决策；不得把玩家尚未获知的 NPC 私有信息写入玩家可见叙事。
5. 不替玩家承诺、驾驶、搬运、同意或作出选择。玩家提议不等于承诺。
6. 只按明确的游戏内耗时推进时间，不按现实消息间隔推进。
7. 场景不使用任何特定 TRPG 系统机制或骰制；不得引入额外规则。
8. 全部 ACTION 完成后，才读取 ORACLE 并完成结构化自审。

## 输出要求

完整记录每轮玩家行动与 GM 回应、游戏内时间、玩家可知信息、各 NPC 的位置/行动/任务/知识变化、资源占用和任务状态。报告标记 `SINGLE_SESSION_SELF_TEST`；正式 Campaign L3 验收仍为 NOT TESTED，T4 真实跑团能力仍为 NOT ESTABLISHED。