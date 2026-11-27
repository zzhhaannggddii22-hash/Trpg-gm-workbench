# Training & Runtime Quality Assurance｜训练与运行时质量保证

> 版本：0.1
> 建立基线：main@ac551b5e04d7a7c9dc5e3314e30be1658e019f5e（2026-11-26）
> 状态：IMPLEMENTED AS GOVERNANCE / BEHAVIORAL VALIDATION PENDING
> 适用范围：跨系统通用 GM 训练、叙事能力沉淀、能力迁移与实际运行质量审计
> 核心约束：QA 尽可能离线化；Runtime 不增加逐轮全量评分、全量扫描或重复检查。

## 1. 目的

本规范把现有训练、叙事基准、综合测试、能力迁移、Runtime Context Trace 和实战复盘连接为一条可追踪的质量闭环。

目标不是增加一套平行 GM 架构，而是回答四个问题：

1. 训练是否让目标能力产生了可观察改善？
2. 新能力是否损害既有能力或触发新的硬性错误？
3. 训练成果是否经由现有 Skill / Prep / Preflight 路径进入实际主持？
4. 实际表现不佳时，能否区分能力不足、上下文/状态缺失、接口问题与执行问题？

**最终验收对象是实际玩家互动中的综合 GM 表现，而不是训练文本、文档更新或单个测试分数。**

## 2. 设计原则与非目标

### 2.1 质量原则

- **硬门槛不可补偿。** 规则、事实、信息权限、玩家能动性和关键连续性硬失败，不得被文笔、气氛、速度或平均分抵消。
- **基准版本化。** 已验收基准保留原版本和证据；新版本只有在明确评估、无不可接受退化后才能晋级。不得随训练自动抬高基准或回写历史结果。
- **专项诊断、综合验收。** 专项练习只证明局部方法；综合场景检验能力联动；真实 Session 检验实战迁移。
- **能力与执行条件分开诊断。** 缺少必要资料、状态或接口时，不把执行失败简单归咎于叙事能力。
- **证据分层。** 模型自评、合成自测、独立测试、用户反馈、真实 Session 证据分别记录，不互相冒充。
- **保持玩家体验。** 测试不得诱导玩家配合指标、强制触发遭遇或限制合理行动；微型箱庭首先是一场值得玩的游戏。

### 2.2 性能与复杂度约束

本体系不要求：
- 每个玩家回合运行叙事质量评分；
- 每轮创建完整 Context Manifest / Trace；
- 每次训练后执行全仓库扫描或完整回归套件；
- 将全部训练日志、能力登记表或评价标准装入 Runtime 提示词；
- 新建第二套 Runtime State、NPC 知识库、证据账本或 Context Trace；
- 为方便评分而设置固定对白比例、描写字数、细节数量或 NPC 行为配额。

离线测试、登记与会话后审计是默认方式。Runtime 只使用现有 Skill、Session Invariants、Active Scene Context 和风险路由；按需调用适用方法，不把 QA 变成玩家可见流程。

## 3. 现有权威文件与职责映射

本规范是导航与协同规则，不取代下列文件的专业定义。

| 质量职责 | 现有权威来源 | 本规范如何使用 |
|---|---|---|
| 叙事质量标准 | [NARRATIVE_QUALITY_BASELINE.md](./NARRATIVE_QUALITY_BASELINE.md) | 唯一叙事质量基准；不在本文件复制评分锚点 |
| GM 综合评价 | [04_EVALUATION_FRAMEWORK.md](./04_EVALUATION_FRAMEWORK.md) | 硬门槛、体验维度、跨场景覆盖和证据类型 |
| 训练周期与成熟度 | [NARRATIVE_TRAINING_PROGRAM.md](./NARRATIVE_TRAINING_PROGRAM.md) | 综合观察、根因诊断、专项修复、整合、迁移、实战回访及 T0–T4 |
| 缺陷来源与优先级 | [Training_Logs/OPEN_TRAINING_BACKLOG.md](./Training_Logs/OPEN_TRAINING_BACKLOG.md) | 持续维护开放问题，不因新训练主题开始而自动关闭 |
| 箱庭与实战双向迁移 | [MICRO_SANDBOX_LAB/CAPABILITY_TRANSFER_PROTOCOL.md](./MICRO_SANDBOX_LAB/CAPABILITY_TRANSFER_PROTOCOL.md) | 方法抽象、边界、E0–E4 证据等级和双向迁移 |
| 自测执行纪律 | [SELF_TESTING_PROTOCOL.md](./SELF_TESTING_PROTOCOL.md) | 固定 commit、隔离起点、执行有效性和证据边界 |
| Runtime 上下文与根因 | [07_RUNTIME_CONTROL_PROTOCOL.md](./07_RUNTIME_CONTROL_PROTOCOL.md) §13.7–13.8、§14.20 | 使用既有错误恢复分类和 Context Assembly / Trace |
| 常驻叙事约束 | [00_GM_CAPABILITY_ARCHITECTURE.md](./00_GM_CAPABILITY_ARCHITECTURE.md) §4.1 | 常驻约束、场景上下文、按需专业方法；不新增逐轮清单 |
| 性能质量边界 | [GM_RUNTIME_P1_PERFORMANCE_PLAN.md](./Optimization_Reports/GM_RUNTIME_P1_PERFORMANCE_PLAN.md) | 性能收益不能抵消质量、可靠性、权限或体验退化 |

现有重点夹具：
- [NQB-01 低压叙事基准](./NARRATIVE_QUALITY_BASELINE.md) 及其训练记录；
- [叙事训练成果向实际跑团迁移回归](./Testing/Fixtures/NARRATIVE_RUNTIME_TRANSFER_REGRESSION_v1.md)；
- [L3 NPC 主动性与离场连续性回归](./Testing/Fixtures/L3_NPC_AUTONOMY_AND_DORMANT_CONTINUITY_REGRESSION_v1.md)；
- [叙事运行单会话综合可执行伴随夹具](./Acceptance_Test_Fixtures/NARRATIVE_RUNTIME_SINGLE_SESSION_HARNESS_v1/README.md)；
- [Narrative Stress Test 01](./Testing/Reports/NARRATIVE_STRESS_TEST_01_DESIGN.md)；
- [Context Assembly / Trace 回归夹具](./Testing/Fixtures/CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md)。

新增夹具前，必须先确认上述现有夹具是否能够覆盖问题；优先修订现有夹具，不为同一问题建立重复测试。

## 4. 质量保证闭环

### 4.1 观察与问题登记

问题优先来自真实 Session、完整综合场景、用户明确反馈或可复现测试事件。记录原始行动、GM 实际回应、相关上下文和玩家可观察结果。

开放问题统一进入 OPEN_TRAINING_BACKLOG；具体样本和证据留在对应 Training Log、Acceptance Report 或 Session Log。不要只记“叙事不好”“NPC 不自然”等无可复现的抽象结论。

### 4.2 根因诊断

先定位最早偏离点，再决定训练还是工程修复。沿用 Runtime §13.7 的错误恢复原则，并按下列诊断标签记录主因（允许一个主因和若干次因）：

| 根因标签 | 判定问题 | 主要修复方向 |
|---|---|---|
| CAPABILITY_GAP | 必要上下文正确、方法适用，但 GM 未能稳定产生合格表现 | 专项训练与综合再整合 |
| CONTEXT_GAP | 需要的权威资料、场景上下文或人物信息未装配/读取 | Context Assembly、Preflight、资料路由 |
| STATE_GAP | Runtime State、事件、位置、知识或玩家已知投影缺失/过时 | 既有 Runtime / Session Log / 事件应用机制 |
| INTERFACE_GAP | 信息存在，但没有沿正确层间接口传到需要使用的环节 | Skill 路由、Handoff、接口契约 |
| EXECUTION_GAP | 条件与资料齐备，适用方法已可用，但运行时没有执行或执行错误 | Skill 入口、常驻约束、风险路由或模型行为验证 |
| SCENARIO_GAP | 测试场景未真实触发目标能力、测试前提不成立或 Oracle 不充分 | 修订/替换测试设计，不直接判能力失败 |
| POLICY_CONFLICT | 规范重复、冲突、优先级不清或存在过期入口 | 修订唯一权威规范与导航 |

若隐藏平台 Prompt、产品内部调度或不可见运行时无法观测，明确标记 UNKNOWN / NOT OBSERVABLE；不得声称已定位平台内部机制。

### 4.3 专项修复与历史能力保护

- 一轮训练优先处理一个主要根因或少量紧密相关变量。
- 训练前锁定当前 NQB 基准版本、相关综合样本和候选 Skill commit。
- 训练后先做目标能力检查，再做相关历史能力保护检查。
- 目标能力提升但出现硬失败，或对其他重要能力造成明显退化，不通过。
- 修复结果必须保留成功证据、失败证据、适用边界和未解决项。
- 不因单次正向样本自动关闭持续性问题；Backlog 关闭须引用足够的复现/反例检查和跨场景证据。

### 4.4 综合再整合与跨场景验证

训练成果至少经历：
1. 目标问题的专项验证；
2. 完整场景综合验证；
3. 变体/留出场景验证，改变人物、地点、关系、体验重心或玩家行动；
4. 对适用的能力，验证绿色普通互动、重要互动、场景切换和预案外行动中的自然表现。

不要求每轮测试覆盖全部能力。根据变更影响选择最小充分测试组合；测试未覆盖的维度标 N/A / UNKNOWN，不推定通过。

### 4.5 进入 Skill 与实际 Runtime

训练成熟度沿用 NARRATIVE_TRAINING_PROGRAM 的 T0–T4，不另造一套晋级尺度：

- T0/T1：观察或候选，留在训练/研究记录。
- T2：多样本重复有效，可进入综合场景试用；保留反例与边界。
- T3：经过综合再整合与跨场景验证，方法进入对应 Skill；必须建立能力迁移登记。
- T4：在真实跑团多个适用情境中有效，且未产生明显副作用；由真实 Session 证据支持。

**T3 是 Skill 集成状态，不代表实际 Runtime 已自然调用；T4 才是实战稳定性结论。**

能力成熟度 T0–T4 与箱庭迁移协议的证据等级 E0–E4 是两个不同维度：前者描述训练/集成阶段，后者描述证据强度。不得互相换算或把 E2 自动等同于 T2。

### 4.6 实战回访与双向反馈

真实 Session 是最终迁移环境，也是高价值缺陷来源：
- 记录适用能力在真实情境中是否自然出现、是否被过度泛化、是否有副作用；
- 区分玩家实际反馈、可观察行为、GM 自评和推断；
- 真实 Session 暴露的问题去除战役专属事实后，可反向形成箱庭训练样本；
- 不把箱庭 NPC、道具、解法、骰制或战役秘密带入其他 Campaign；
- 只有足够的多次真实应用证据才能支持 T4；单次实战成功仅作为该样本证据。

## 5. 运行时审计：低开销、按需、会话后

### 5.1 运行时只保留什么

运行时持续生效的内容以现有 GM Session Invariants 和 Active Scene Context 为准。它们在 Preflight/恢复时建立，并按场景和依赖变化更新。

只有与当前场景相关、已达到 T3 的方法才通过既有 Skill / Prep / Preflight 路径自然可用。能力登记表是审计索引，不是需要在每轮加载的提示词或运行时清单。

绿色普通互动不新增叙事评分、Manifest 或 Trace 要求。黄色/红色行动及实际需要上下文证明的行动，沿用 Runtime §14.20 的 Context Assembly / Trace；不得重复建设第二套来源追踪。

### 5.2 会话后审计触发

默认在 Session 收束、用户提出质量反馈、出现明显叙事退化、重要场景/人物状态发生异常，或某项迁移能力需要复核时执行定向审计。

审计只抽取有代表性的片段和必要证据：
- 玩家行动与意图；
- GM 实际呈现；
- 场景/人物/状态变化；
- 适用的 Skill 与 T3 登记项；
- 必要时对应 Context Trace / Manifest；
- 玩家反馈及其时间点；
- 观察到的副作用和未覆盖项。

不要求逐轮为所有能力打分，不要求每个普通动作生成结构化记录。没有相关 Trace 时标记 NOT_RECORDED，不补造。

### 5.3 迁移审计的关键问题

1. 当前场景是否适用某项已登记能力？
2. 必要的 Skill 方法是否在当前运行入口可用？
3. 必要上下文是否实际装配并核验？
4. GM 是否自然地使用该方法，还是机械展示训练技巧？
5. 玩家行动是否得到符合事实、规则和人物动机的响应？
6. 方法是否损害其他能力、玩家行动空间或自然节奏？
7. 结论是否有真实玩家互动证据，还是只有合成自测？

## 6. 质量矩阵与不可补偿门槛

评价维度以 NARRATIVE_QUALITY_BASELINE 与 04_EVALUATION_FRAMEWORK 为唯一评分定义。本规范只规定覆盖关系，不复制评分细则。

| 覆盖面 | 主要权威评价来源 | 重点保护 |
|---|---|---|
| 基础正确性 | NQB 第一层 | 世界事实、NPC/玩家信息边界、隐藏信息、规则、玩家行动权 |
| 场景与空间 | NQB / 综合评价 | 清晰、可感知、可行动；不退化成物件清单 |
| NPC 与人物 | 综合评价 / Character Simulation | 主体性、差异、知识、动机与关系连续 |
| 信息组织 | NQB / 线索账本 | 交付准确、不过度解释、保留玩家推理空间 |
| 行动响应与即兴 | 综合评价 | 预案外行动、因果、真实后果 |
| 节奏与压力 | NQB / Stress Test | 压力下仍清楚、有层次；不变成状态播报 |
| 连续性 | Runtime §13 / 综合评价 | 时间、空间、物品、知识、事件和已呈现内容 |
| 训练迁移 | 本规范 §4–5 / 迁移夹具 | Skill 集成的方法在实际适用情境自然生效 |

任一硬门槛 FAIL 均单独保留，不得由体验分数或其他能力的提升抵消。UNKNOWN、NOT TESTED、NOT TESTABLE 不等于 PASS。

## 7. 测试选择与版本管理

### 7.1 默认采用定向测试，不要求每次跑全套

- 叙事 Skill/表达方法修改：优先 NQB 低压基准 + 对应综合场景或变体。
- 高压/多主体/时间窗口相关修改：选择 Stress Test 或其修订版，并检查低压场景是否退化。
- NPC 主体性/离场连续性修改：选择 L3 NPC 回归夹具。
- T3 迁移或 Runtime 入口修改：选择 Narrative Runtime Transfer Regression。
- Context Assembly、Trace、资料状态或风险路由修改：选择 Context Assembly / Trace 夹具。
- 信息通道、隐藏信息或玩家知识边界修改：必须选择覆盖相应硬门槛的针对性测试；G-16 相关修复不得只靠文风样本验收。
- 跨层架构、大范围入口或多个权威规范变化：根据影响范围组合多个相关夹具；确有必要时再执行完整回归。

若现有夹具不能覆盖缺陷，先记录缺口，再新增最小复现夹具；不为追求测试数量而扩张。

### 7.2 固定基线

- 记录被测 main/候选 commit SHA、夹具版本、依赖文件 SHA 和测试环境。
- A/B 对照必须从同一不可变起点复制状态，分支之间不得共享已变更状态。
- 固定基准样本保留历史版本，用于纵向观察；隐藏/变体样本用于降低过拟合。
- 修改基准必须说明新增要求、证据、旧版本兼容性和潜在副作用；历史报告不回写。
- 只在实际执行后更新测试状态。文件存在、提示词准备好或模型自评均不是 PASS。

## 8. 当前基线审计快照（2026-11-26）

本节记录建立本规范时可核验的仓库状态；后续变化应追加更新，不得覆盖历史证据。

| 项目 | 当前证据与限制 |
|---|---|
| NQB-01 | v1.0 为 operational baseline；基准文件存在不代表当前 Skill 自动通过 |
| #33 单会话夹具有效回归 | 两套合成夹具在指定样本中完成有效顺序执行；L3 synthetic behavior 与 Narrative Scene Integration 为该样本 PASS |
| T3 迁移 | #33 报告中的 T3_TRANSFER 为 NOT TESTABLE，缺少可追溯 T3 来源；需先建立能力登记 |
| 正式 Campaign L3 | NOT TESTED |
| 正式 Runtime 持久化 / 隐藏平台运行时 | NOT TESTED |
| 独立盲审 / 真实多轮平台交互 | NOT TESTED |
| Narrative Stress Test 01 | 高压叙事为 PARTIAL；后半段流程化，压力与目标冲突覆盖有限 |
| 玩家信息通道 | Stress Test 01 补充审计判定 FAIL；G-16 仍 OPEN，历史失败不得被后续文档修改抹除 |
| Micro-Sandbox 001《雨前过桥》 | E1 单次箱庭证据；若干能力仍为 CANDIDATE，真实 Session 迁移 NOT TESTED |
| Narrative Runtime Transfer Regression v1 | 夹具已存在；本次审计未找到可证明其已完成 T3 迁移验收的报告 |
| Context Assembly / Trace | 设计与夹具已存在；夹具文件标记待执行，不能据此宣称目标 Chat 行为通过 |
| P1-0C | 仍 DEFERRED；历史 4 FAIL / 1 PARTIAL 与此前 REJECT 保留，性能优化完成不等于地基质量通过 |

本快照依据 main ac551b5e04d7a7c9dc5e3314e30be1658e019f5e 可访问文件建立。它不是新的行为回归，也不替代独立审查或真实玩家 Session。

## 9. 质量记录最小字段

新问题或迁移审计至少记录：
- QA / Defect ID：
- 发生日期、被测 commit、系统/战役/场景范围：
- 来源类型：REAL_SESSION / SYNTHETIC / MICRO_SANDBOX / INDEPENDENT_TEST / USER_FEEDBACK / OTHER：
- 原始玩家行动与 GM 回应引用：
- 预期行为与实际行为：
- 硬门槛：PASS / FAIL / UNKNOWN：
- 主要根因标签及依据：
- 受影响能力 / 已有 T3 登记项：
- 相关 Skill、Runtime、Context Trace / Manifest 引用（若存在）：
- 副作用与未覆盖范围：
- 修复提交与验证证据：
- 状态：OPEN / IN_PROGRESS / FIXED_PENDING_VALIDATION / CLOSED / DEFERRED：

不要求把所有字段写入玩家可见 Session Log。正式 Session 的敏感/GM-only 事实按既有 Campaign 权限边界保存；构造跨场景测试时先剥离战役专属内容。

## 10. 首轮实施顺序

1. **建立可追溯 T3 登记。** 先从现有 Skill、训练日志与样本核对候选来源；未完成证据核验的项目不登记为 T3。
2. **处理 G-16。** 先确认信息通道硬门槛的修复方案和针对性回归覆盖，不用新叙事技巧绕过此问题。
3. **执行迁移夹具。** 至少有一项可追溯 T3 登记后，再执行 Narrative Runtime Transfer Regression；缺少准入条件时保持 NOT TESTABLE。
4. **补充跨场景证据。** 低压、综合、高压与预案外行动分别取样；避免只在同一种压力模板中训练。
5. **进入真实 Session 回访。** 只在适用情境观察迁移；多次真实证据支持后再考虑 T4。
6. **单独恢复地基可靠性阶段。** P1-0C 与 T0/持久化边界按性能阶段交接文件处理，不把本叙事 QA 体系的文档落地视为 P1-0C 通过。

## 11. 维护与变更

- 本文件维护质量闭环、职责路由和验收门槛；基准分数、专项方法、Runtime 状态模型仍归各自权威文件。
- 能力迁移明细统一维护在 [NARRATIVE_CAPABILITY_REGISTER.md](./NARRATIVE_CAPABILITY_REGISTER.md)。
- 叙事质量标准变更同步更新 NQB、综合评价框架和相关夹具索引；不要只改本文件。
- 每次质量迭代结束，更新 Backlog 和相关报告；未执行项目明确保留 NOT TESTED。
- 不为形式完整而增加每轮检查、重复日志或新数据库。
