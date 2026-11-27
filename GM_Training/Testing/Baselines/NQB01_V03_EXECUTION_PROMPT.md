# NQB-01 v0.3｜操作者执行与信息隔离提示

> Fixture: NQB-01 v0.3
> Status: OPERATOR PROTOCOL
> Canon: TEST_ONLY_NON_CANON
> 本文件定义操作者如何组织测试。它不是完整的 GM 提示包，不得把其中的审核目标、行动序列或审核表转交目标 GM。

## 一、版本锁定

仓库：`zzhhaannggddii22-hash/Trpg-gm-workbench`
Workbench commit：执行前必须填写精确 SHA，不得只写分支名。

## 二、资料访问隔离

**目标 GM 执行阶段只读取：**
1. `GM_Training/NARRATIVE_QUALITY_BASELINE.md`
2. `GM_Training/Testing/Baselines/NQB01_V03_GM_PACKET.md`
3. `GM_Training/Testing/Baselines/NQB01_V03_PLAYER_PROMPT.md`

**操作者 / 审核者专用，不得提供给目标 GM：**
1. `GM_Training/Testing/Baselines/NQB01_V03_SPEC.md`
2. `GM_Training/Testing/Baselines/NQB01_V03_ACTION_SEQUENCE.md`
3. `GM_Training/Testing/Baselines/NQB01_V03_REVIEW_CHECKLIST.md)

GM 不得提前获知测试的轮数目标、预设行动路径、审核维度或单段回复长度目标。GM 应像普通跑团一样，根据当前玩家行动和已经发生的事实自然主持；不得为了达到某个篇幅、轮数或评分指标而填充内容。

## 三、执行模式

### A｜同会话自动化自测（默认）

- 当前会话分别模拟操作者、玩家和 GM；完整行动序列仅作为操作者内部资料。
- 模拟玩家每轮只读取当前行动意图，不把后续行动告诉 GM 角色。
- GM 角色只依据 GM 可用资料、已发生的场景状态和当前玩家行动作出回应。
- 由于执行者在同一会话中能够访问测试资料，不能宣称实现了真正的信息隔离；报告必须标记 `SINGLE_SESSION_SELF_TEST`，并承认模拟角色间存在上下文污染风险。
- 结束后才读取审核规格和 Review Checklist，保存完整逐轮原始记录。

### B｜干净目标 Chat 自动化 + 独立审核（专项）

- 操作者建立真正空白的目标 Chat。
- 目标 GM 只接收通用 GM 执行要求、GM Packet 和 Player Prompt；不接收本文件、SPEC、ACTION SEQUENCE 或 REVIEW CHECKLIST。
- 操作者依据私有行动序列逐轮向目标 Chat 注入一条玩家行动；不得一次性粘贴完整序列。
- 目标 GM 每次只回应当前行动，操作者保存完整原始输入与输出。
- 全部结果回传后，独立审核者才读取 SPEC 与 Review Checklist。
- 若无法逐轮注入而必须由目标 Chat 自行模拟玩家，则应标记为另一种合成执行，不得声称遵循了本行动序列。

### C｜真实玩家逐回合互动

- 由真实玩家逐轮输入，GM 每次只回应当前行动。
- 不得补造玩家输入或强行凑足轮数。
- 结束后由审核者读取 SPEC 与 Review Checklist。
- 明确标记真实玩家证据，不等同于真实线下团或长期稳定能力证明。

## 四、共同主持约束

- 本次为独立测试，不继承其他跑团、战役或训练场景的事实。
- 不绑定具体规则系统，不掷骰，不引入其他系统机制。
- 不主动制造谜题、危机、倒计时、强制冲突或必需线索。
- 不把 NPC 内心、未说出口的记忆或私人意图直接交付给玩家。
- 不替玩家决定情绪、注意力、行动或推理结论。
- 普通细节可以自然补全；玩家开始依赖某项细节后，维护其一致性。
- 不输出 GM 状态表、测试覆盖提示、评分表或内部行动计划。
- 回复长短由当前行动复杂度决定。简单行动可以短答；复杂行动应给出足以支持玩家理解、选择和后续行动的具体反馈。不得机械追求字数。

## 五、交付与审核

执行结束后交付：
- 精确 Workbench commit、夹具版本、执行模式、实际读取资料；
- 完整逐轮玩家输入与 GM 原始回复；
- 实际轮数与行动覆盖；
- 人物、物件、位置、时间、承诺和信息来源状态记录；
- 可用于字符级统计的原始 GM 回复正文；
- 执行过程中的偏差与证据局限。

操作者/审核者再依据 SPEC 与 Review Checklist 统计：
- v0.2 与 v0.3 GM 回复总字符数、段数、平均值、中位数、范围；
- 单段平均字符数倍率和总字符数倍率；
- 基础正确性、交互质量、叙事表现质量与持续叙事负荷。

**完成运行不等于通过。** 只有实际证据达到审核标准，才能给出相应结论。
