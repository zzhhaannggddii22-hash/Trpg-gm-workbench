# Narrative Capability Register｜叙事能力迁移登记表

> 版本：0.1
> 建立基线：main@ac551b5e04d7a7c9dc5e3314e30be1658e019f5e
> 状态：INITIAL REGISTER / RECONCILIATION REQUIRED
> 目的：让已进入 T3（Skill 集成）的叙事能力有明确来源、运行位置、适用条件和实战验证记录。

## 1. 登记范围

本表只登记具备可追溯来源、已达到 T3 或正在接受 T3 准入核验的通用能力。

- T0/T1 观察与候选继续保留在 Training Logs / Research。
- T2 重复有效的方法可以在综合场景试用，但不登记为已集成的稳定运行能力。
- T3 必须指向实际 Skill 文件与版本，并记录训练样本、综合再整合和跨场景验证来源。
- T4 必须由多个真实 Session 中的适用表现及副作用检查支持。
- 本表是索引，不是 Runtime 提示词；现场不需要加载整张表或逐项打勾。

成熟度 T0–T4 沿用 [NARRATIVE_TRAINING_PROGRAM.md](./NARRATIVE_TRAINING_PROGRAM.md)。证据等级 E0–E4 沿用 [箱庭双向迁移协议](./MICRO_SANDBOX_LAB/CAPABILITY_TRANSFER_PROTOCOL.md)，两者不得混用。

## 2. 当前登记状态

截至建立本表的 main 基线，最新可访问的 #33 单会话有效回归报告将 T3_TRANSFER 标记为 NOT TESTABLE，原因是缺少可追溯的 T3 来源。

因此本表从空登记开始。**空表表示当前尚未完成可追溯登记，不表示仓库内不存在任何已集成叙事方法，也不擅自把现有 Skill 内容降级。** 下一步须逐项核对 Skill、训练记录和综合样本，再决定哪些项目满足 T3。

| 统计项 | 当前值 | 说明 |
|---|---:|---|
| 已登记 T3 能力 | 0 | 尚未完成来源与版本映射 |
| 已登记 T4 能力 | 0 | 尚无登记项具备本表要求的多次真实 Session 证据 |
| 待核验候选 | 未统计 | 需要逐项对照现有 Skill 与 Training Logs |
| 已登记但待修订/退役 | 0 | 初始登记 |

## 3. 能力登记表

| Capability ID | 能力名称 | 当前成熟度 | Skill / 版本 | 训练与综合证据 | Runtime 迁移证据 | 状态 |
|---|---|---|---|---|---|---|
| — | 暂无已完成来源核验的登记项 | — | — | — | — | RECONCILIATION REQUIRED |

## 4. 单项登记模板

新增能力时复制本节模板。每项只记录一个边界清楚、可观察的能力；多个相互独立的方法应拆分登记。

### CAP-NAR-XXX｜能力名称

- **当前成熟度：** T3 / T4
- **状态：** T3_INTEGRATED_PENDING_RUNTIME / RUNTIME_SUPPORTED / T4_FIELD_VALIDATED / REVISE / RETIRED
- **能力定义：** 可观察、可判断的主持行为，不写抽象人格标签。
- **适用问题 / 场景：** 哪些真实问题或场景适用。
- **触发信号：** 何时应自然调用。
- **执行方法：** 最小、可执行的方法说明。
- **不适用条件 / 反模式：** 何时不调用；不得产生什么机械套路。
- **依赖上下文：** 所需人物、场景、事实、规则或状态资料。
- **Skill 位置：** 文件路径、章节、Skill 版本/commit。
- **训练来源：** Training Log、研究记录及精确版本。
- **综合验证：** 场景、夹具、变体、结果与证据等级。
- **Runtime 入口：** 通过哪个既有 Skill / Prep / Preflight 路径可用；不得新增每轮加载。
- **Runtime 验证：** 迁移夹具或实际 Session 的具体事件引用；未执行写 NOT TESTED。
- **真实 Session 证据：** 日期、Session 引用、适用情境、玩家反馈/可观察结果。
- **副作用与反例：** 退化、过度泛化、失效条件和未覆盖情境。
- **回退条件：** 出现何种质量损失时修订或撤回。
- **最后复核：** 日期、审查者/审查方式、结论。

## 5. 状态定义

| 状态 | 含义 |
|---|---|
| T3_INTEGRATED_PENDING_RUNTIME | 已进入 Skill 且来源可追溯；尚未证明在正常 Runtime 入口自然应用 |
| RUNTIME_SUPPORTED | 已在受控 Runtime 迁移测试中观察到自然应用；仍不等于真实 Session T4 |
| T4_FIELD_VALIDATED | 多个真实 Session 的适用场景中持续有效，且没有明显副作用 |
| REVISE | 发现副作用、适用边界错误或表现退化，需要修订 |
| RETIRED | 已被更好方法替代或不再适用；保留历史记录 |

登记项不得仅因文档存在、合成测试一次 PASS 或模型自评而进入 T4。

## 6. 登记维护规则

1. 先检查现有 Training Log、Skill、Evaluation Report 和测试报告，引用现有证据，不复制大段材料。
2. 缺少精确 commit、训练来源、跨场景证据或 Skill 位置时，保持待核验，不补造。
3. T3 登记完成后，才可将该能力作为 NARRATIVE_RUNTIME_TRANSFER_REGRESSION_v1 的具体迁移对象。
4. 每次 Skill 发生影响该能力的修改时，更新 Skill 版本映射并按影响选择回归测试。
5. 每次真实 Session 发现失效或副作用，更新状态并关联 OPEN_TRAINING_BACKLOG。
6. 退役能力不得删除历史来源；说明替代项与退役原因。
7. 本表不替代 Backlog、Session Log、Runtime State、Context Trace 或综合评价框架。
