# NQB-01 v0.3｜常规游戏强度基线执行提示

> Fixture: NQB-01 v0.3
> Status: DESIGN / NOT YET EXECUTED
> Intended mode: A 同会话自动化自测；B/C 按现有 SELF_TESTING_PROTOCOL 分流。
> Canon: TEST_ONLY_NON_CANON

## 一、版本锁定与资料读取

仓库：`zzhhaannggddii22-hash/Trpg-gm-workbench`
Workbench commit：执行前必须填写精确 SHA，不得只写分支名。

目标 GM 执行阶段读取：
1. `GM_Training/NARRATIVE_QUALITY_BASELINE.md`
2. `GM_Training/Testing/Baselines/NQB01_V03_GM_PACKET.md`
3. `GM_Training/Testing/Baselines/NQB01_V03_PLAYER_PROMPT.md`
4. `GM_Training/Testing/Baselines/NQB01_V03_SPEC.md`

操作者/审核者专用：
- `GM_Training/Testing/Baselines/NQB01_V03_ACTION_SEQUENCE.md`
- `GM_Training/Testing/Baselines/NQB01_V03_REVIEW_CHECKLIST.md`

目标 GM 不得读取完整行动序列或审核表。B 模式目标 Chat 不得接触 Oracle、审核标准或后续行动计划。A 模式的模拟玩家每轮只读取当前行动意图，GM 角色不得利用后续行动信息提前安排回应。

## 二、执行要求

1. 本测试是普通日常场景，不引入战斗、强制冲突、倒计时或必需谜题。
2. 目标覆盖 12–16 轮有效互动，推荐 14 轮；自然收束可以提前结束，但需报告覆盖不足。
3. 让玩家行动自然决定互动方向。不要强迫追完三条事务线。
4. NPC 必须保持不同的注意力、目标、表达和知识边界；不要每轮都让所有 NPC 发言。
5. 复合行动应得到清晰回应；玩家改变目标时自然跟随。
6. 等待期间世界可以缓慢变化，但不得人为制造事件。
7. 维护服务请求、承诺、物件位置、人物位置、时间变化、已披露信息和未完成事务。
8. 回复长短由行动复杂度决定。目标是比 v0.2 更接近常规游戏的内容负荷，整体原始对话量粗略目标为 v0.2 的 4–6 倍；不允许为达字数而重复或堆砌。
9. 不向玩家展示 GM 状态账本、内部行动计划、审核表或测试覆盖项目。
10. 只依据当前玩家行动回应；不得提前写入后续行动或结果。

## 三、证据与交付

- A：保存逐轮模拟玩家行动和 GM 原始回应；明确标记合成自测与模型自评。
- B：干净目标 Chat 只交付完整原始输出和执行元数据；独立审核者在回传后读取审核表。
- C：真实玩家逐回合互动，不得补造玩家输入；不足 12 轮只说明覆盖范围有限。

交付至少包括：精确 commit、资料读取证据、实际轮数、逐轮原始记录、状态账本、文本负荷粗略比较、基础正确性结果、交互质量与叙事表现评分、持续叙事负荷评分、失败严重度和证据边界。

**完成运行不等于通过。** 只有实际证据达到门槛，才能给出相应结论。
