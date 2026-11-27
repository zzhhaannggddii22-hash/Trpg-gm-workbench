# NQB-01 v0.3｜操作者执行与信息隔离提示

> Fixture: NQB-01 v0.3
> Status: OPERATOR PROTOCOL / EXECUTION BLOCKED UNTIL A PRE-EXISTING ISOLATED TEST CAMPAIGN IS AVAILABLE
> Canon: TEST_ONLY_NON_CANON
> 本文件定义操作者如何组织测试。它不是完整的 GM 提示包，不得把其中的审核目标、行动序列或审核表转交目标 GM。

## 0. 强制准入：先确认存在正确的 TRPG 运行入口

**本测试必须通过仓库正式 GM 运行入口执行，不得绕过 Skill、Preflight 或 Runtime 自行扮演 GM。**

执行前必须同时满足：
1. 已存在一个由项目正式登记的、专供测试的 Campaign / Test Campaign，且它有自己的 SYSTEM_BINDING.md、唯一 system_id、精确规则版本、合法初始 Runtime 检查点和隔离存储位置。
2. 该测试 Campaign 与所有正式 Campaign 完全分离；不得使用 Zarek 或其他正式角色、NPC、关系、装备、记忆、模组、Session Log、Runtime State 或玩家笔记作为测试起点。
3. 测试 Campaign 和测试 Module 必须在本次测试前已经存在并经用户授权使用。操作者不得为了让测试继续而自行创建 Campaign、角色卡、SYSTEM_BINDING、Runtime State、Session Log、NPC 档案或其他运行环境。
4. 测试执行使用正常入口：GM_Training/SKILL.md → GM_Training/02_WORKFLOW_AND_PREFLIGHT.md → SYSTEM_CONTEXT_PROTOCOL.md → 测试 Campaign 的 SYSTEM_BINDING / Runtime 检查点 → 对应系统入口、规则与 Skill → 测试 Module 的 GM Prep / Runtime Context。按标准流程完成 Context Assembly、Preflight 和运行身份核验。
5. NQB 场景资料只作为该测试 Campaign 下的 test-only Module/场景输入，在正常 Prep-to-Runtime 交接后加载；不得将 GM Packet 当作独立 GM 提示词或自行搭建一个平行的“迷你 GM 环境”。
6. 测试运行必须使用预先存在的隔离状态目标。若标准 Runtime 会将事件写入正式 Campaign，或无法证明测试数据只写入隔离位置，立即 BLOCK，不得试跑。

**当前仓库准入检查：** Campaigns/README.md 当前登记的正式 Campaign 只有 Zarek / 扎雷克；本测试没有已登记的专用 Test Campaign。因此，在用户明确提供/授权使用一个已经存在的隔离测试 Campaign 之前，NQB-01 v0.3 的真实 Runtime 执行状态必须保持 BLOCKED_NOT_RUN。不得改用 Zarek Campaign，不得自行创建替代环境，也不得把先前 A-mode 独立提示包模拟当成 Runtime 测试。

如果上述任一条件不满足，只能继续完善测试设计和静态文件检查；不得声称完成了正式入口测试。

## 一、版本锁定

仓库：zzhhaannggddii22-hash/Trpg-gm-workbench
Workbench commit：执行前必须填写精确 SHA，不得只写分支名。
同时记录测试 Campaign ID、SYSTEM_BINDING 修订、Runtime checkpoint、测试 Module ref 与隔离存储目标。任一来源无法固定则 BLOCK。

## 二、资料访问隔离

**目标 GM 通过正式 Preflight 和 Context Assembly 实际装配所需资料。** 下列列表只用于确认资料按权限装配，不得取代正常入口。

目标 GM 可获得：
1. 正式入口所需的通用 GM 运行文件与 Skill；
2. 当前测试 Campaign 的 SYSTEM_BINDING、对应系统规则/专属 Skill、合法测试 Runtime 起点；
3. NQB 场景资料中 GM-only 的场景状态与人物资料；
4. 玩家侧启动材料中可公开的场景信息。

操作者 / 审核者专用，不得提供给目标 GM：
1. GM_Training/Testing/Baselines/NQB01_V03_SPEC.md
2. GM_Training/Testing/Baselines/NQB01_V03_ACTION_SEQUENCE.md
3. GM_Training/Testing/Baselines/NQB01_V03_REVIEW_CHECKLIST.md
4. 本执行协议及其测试覆盖目标、长度统计目标和审核结论。

GM 不得提前获知测试轮数目标、预设行动路径、审核维度或单段回复长度目标。GM 应像普通跑团一样，根据当前玩家行动和已经发生的事实自然主持；不得为了达到某个篇幅、轮数或评分指标而填充内容。

## 三、执行模式

### A｜同会话自动化自测（默认；仅在正式测试 Runtime 已准入后）
- A-mode 只是操作者/玩家模拟方式，不是另一套 GM 运行环境。
- GM 必须从本文件第 0 节规定的正常入口完成 Preflight 和 Runtime 装配；不得直接读取 Packet 后开始表演。
- 当前会话分别模拟操作者、玩家和 GM；完整行动序列仅作为操作者侧资料。模拟玩家每轮只读取当前行动意图，不把后续行动告诉 GM。
- 由于执行者在同一会话中能够访问测试资料，不能宣称实现真正的信息隔离；报告必须标记 SINGLE_SESSION_SELF_TEST，并承认模拟角色间存在上下文污染风险。
- 所有运行时写入必须落入已准入的测试隔离存储；不能证明隔离则 BLOCK。
- 结束后才读取审核规格和 Review Checklist，保存完整逐轮原始记录。

### B｜干净目标 Chat 自动化 + 独立审核（专项）
- B-mode 同样必须先通过已存在的测试 Campaign 正式入口和 Preflight；空白 Chat 本身不等于有效运行环境。
- 目标 GM 只接收正常 Preflight 实际装配的运行资料与当前玩家行动；不接收本文件、SPEC、ACTION SEQUENCE 或 REVIEW CHECKLIST。
- 操作者依据私有行动序列逐轮向目标 Chat 注入一条玩家行动；不得一次性粘贴完整序列。
- 全部结果回传后，独立审核者才读取 SPEC 与 Review Checklist。
- 若无法逐轮注入而必须由目标 Chat 自行模拟玩家，应标记为另一种合成执行，不得声称遵循了本行动序列。

### C｜真实玩家逐回合互动
- 只有在用户明确选择并启动一个已存在的隔离测试 Campaign 后，才可进行。
- 由真实玩家逐轮输入；不得补造玩家输入或强行凑足轮数。
- 测试 Session 的所有状态写入仍必须被隔离；结束后不得自动并入正式 Campaign。
- 明确标记真实玩家证据，不等同于真实线下团或长期稳定能力证明。

## 四、Canon、状态与数据污染防护

- 本测试全部内容、行动、人物、物件、地点、时间、状态、叙述、事件、报告和输出均标记为 TEST_ONLY_NON_CANON。
- 本测试与所有正式 Campaign 的剧情、角色、人物档案、NPC、关系、装备、资源、玩家笔记、Session Log、Runtime State、成长和世界后果无任何继承或回写关系。
- 不读取正式 Campaign 的角色卡、NPC 档案、模组、历史 Session、私有状态或玩家笔记作为测试材料；不以正式角色/NPC 的复制品作为本测试角色。
- 不得将测试事实写入正式 Campaign。不得把测试中发生的关系、承诺、物品移动、资源变化、记忆或人物成长用于正式跑团。
- 测试报告只归档于 GM_Training/Testing/Reports/；测试运行状态只允许写入已准入的专用测试存储。测试结束后不得执行正式 Campaign 的结团、角色卡更新或 CANON 发布流程。
- 如发现任何正式 Campaign 文件、正式 Runtime 检查点或正式 Session 记录被读取为测试写入目标，立即停止，标记 POLLUTION_INCIDENT，保留证据并先处理事故；不得自行清理或覆盖正式数据。
- 不绑定到任何正式 Campaign。若没有预先存在的隔离测试 Campaign 和运行存储，状态为 BLOCKED_NOT_RUN。

## 五、共同主持约束

- 使用测试 Campaign 已绑定的唯一规则系统及其规则原文；不得再以“system-neutral、不掷骰、不使用系统机制”绕过规则系统。只有在绑定系统和测试场景确实不触发某项机制时，才自然不使用。
- 不主动制造测试设计以外的危机、倒计时或强制冲突；也不为覆盖评分表而强行触发事件。
- 不把 NPC 内心、未说出口的记忆或私人意图直接交付给玩家。
- 不替玩家决定情绪、注意力、行动或推理结论。
- 普通细节可以自然补全；玩家开始依赖某项细节后，维护其一致性。
- 不输出 GM 状态表、测试覆盖提示、评分表或内部行动计划。
- 回复长短由当前行动复杂度决定。简单行动可以短答；复杂行动应给出足以支持玩家理解、选择和后续行动的具体反馈。不得机械追求字数。

## 六、交付与审核

执行结束后交付：
- 精确 Workbench commit、夹具版本、执行模式；
- 测试 Campaign ID、SYSTEM_BINDING、system_id / ruleset_version、测试 Module ref、Runtime checkpoint 与隔离存储证明；
- 正式入口实际读取的文件、Skill 版本、Preflight 结果和 Context Assembly 可观测证据；
- 完整逐轮玩家输入与 GM 原始回复；
- 实际轮数与行动覆盖；
- 人物、物件、位置、时间、承诺和信息来源状态记录；
- 可用于字符级统计的原始 GM 回复正文；
- 运行时写入目标、写入记录与污染检查结果；
- 执行过程中的偏差与证据局限。

操作者/审核者再依据 SPEC 与 Review Checklist 统计：
- v0.2 与 v0.3 GM 回复总字符数、段数、平均值、中位数、范围；
- 单段平均字符数倍率和总字符数倍率；
- 基础正确性、交互质量、叙事表现质量与持续叙事负荷。

**完成运行不等于通过。** 未通过正式入口、系统绑定、隔离存储或污染检查的运行，不得计为有效 Runtime 样本；只可报告 BLOCKED / NOT TESTABLE。