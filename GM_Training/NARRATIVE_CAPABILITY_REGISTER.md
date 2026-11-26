# Narrative Capability Register｜叙事能力迁移登记表

> 版本：0.2
> 建立基线：main@ac551b5e04d7a7c9dc5e3314e30be1658e019f5e
> 最近盘点：2026-11-26
> 状态：INITIAL INVENTORY COMPLETE / T3 QUALIFICATION NOT MET
> 目的：让 T2 候选、T3 集成能力与 T4 实战能力均有可追溯来源、运行位置、适用条件和证据边界。

## 1. 登记范围

本表同时追踪候选能力与已晋级能力，但不同成熟度必须清楚区分：
- T0/T1 观察与候选可登记为待验证项目，不得作为正式运行要求。
- T2 重复有效的方法可供综合场景试用，必须保留反例与边界；不等于已集成的稳定运行能力。
- T3 必须指向实际 Skill 文件与版本，并记录训练样本、综合再整合和跨场景验证来源。
- T4 必须由多个真实 Session 中的适用表现及副作用检查支持。
- 本表是审计索引，不是 Runtime 提示词；现场不需要加载整张表或逐项打勾。

成熟度 T0–T4 沿用 [NARRATIVE_TRAINING_PROGRAM.md](./NARRATIVE_TRAINING_PROGRAM.md)。证据等级 E0–E4 沿用 [箱庭双向迁移协议](./MICRO_SANDBOX_LAB/CAPABILITY_TRANSFER_PROTOCOL.md)，两者不得混用。

## 2. 当前盘点结论

详细依据见 [T3 Narrative Capability Inventory｜2026-11-26](./Training_Logs/NARRATIVE_T3_CAPABILITY_INVENTORY_2026-11-26.md)。

| 统计项 | 当前值 | 说明 |
|---|---:|---|
| 已确认 T3 能力 | 0 | 来源顺序、Skill 版本和跨场景综合验证链尚不完整 |
| 已确认 T4 能力 | 0 | 尚无登记项具备多次真实 Session 证据 |
| T2 候选 | 2 | 场景/行动融合；NPC 性格差异表达 |
| T1 / 局部观察 | 3 | NPC 自主事务；高压综合叙事；动态显著性 |
| 硬失败阻断 | 1 | 玩家信息通道；G-16 OPEN |
| 待补来源映射 | 2 项优先 | CAP-NAR-01、CAP-NAR-02 |

**0 项 T3 不表示仓库没有已集成方法。** 它表示目前没有任何单项能力同时满足可追溯来源、Skill 版本映射、综合再整合、跨场景验证和硬门槛要求。

## 3. 能力登记表

| Capability ID | 能力名称 | 当前成熟度 | Skill / 版本 | 主要证据 | 状态 |
|---|---|---|---|---|---|
| CAP-NAR-01 | 场景、空间与行动反馈的融合呈现 | T2 CANDIDATE | Narrative Presentation v1.1 | NQB RUN-01/02/03；Micro-Sandbox 001 | NEEDS_T3_PROVENANCE_AND_CROSS_SCENE |
| CAP-NAR-02 | NPC 性格差异通过行为、对白与关系互动呈现 | T2 CANDIDATE | Character Simulation v1.0；Narrative Presentation v1.1 | NQB RUN-01/02/03；NPC Calibration 01；Micro-Sandbox 001 | NEEDS_T3_PROVENANCE_AND_CROSS_SCENE |
| CAP-NAR-03 | NPC 自主事务与并行行动 | T1 / NEEDS_MORE_EVIDENCE | Character Simulation v1.0 §6 | Stress Test 01；Micro-Sandbox 001 | NEEDS_MORE_EVIDENCE |
| CAP-NAR-04 | 高压下的综合叙事与节奏维持 | T1 / PARTIAL | Narrative Presentation v1.1 §1/4；GM Skill v0.7 | Stress Test 01 | G-14 OPEN |
| CAP-NAR-05 | 玩家信息通道与 NPC 私有认知隔离 | NOT QUALIFIED | Narrative Presentation v1.1 §3；Character Simulation v1.0 §5；GM Skill v0.7 | NQB RUN-01/02 PASS；Stress Test 01 corrective audit FAIL；G-16 低压回归 PARTIAL；G-16 高压回归 PASS（单会话自测） | BLOCKED_BY_G-16 |
| CAP-NAR-06 | 动态显著性与普通细节升格 | T1 / NEEDS_MORE_EVIDENCE | Narrative Presentation v1.1 §2.4 | Stress Test 01 | G-15 OPEN |


> **2026-11-26 evidence addendum:** G-16 High-Pressure Information Channel Regression v1 passed all three Oracle phases in one continuous single-session self-test (target commit `7d93f276983c431859eedca6a9185e972c6ad696`). This is positive sample-level evidence only. The historical Stress Test 01 hard FAIL remains open, and the low-pressure regression remains PARTIAL because branch reset was not independently verifiable. CAP-NAR-05 therefore remains NOT QUALIFIED / BLOCKED_BY_G-16; no T3/T4 promotion is made. See [high-pressure acceptance report](./Acceptance_Reports/G16_HIGH_PRESSURE_CHANNEL_REGRESSION_v1_2026-11-26.md).
## 4. 单项登记模板

新增能力时复制本节模板。每项只记录一个边界清楚、可观察的能力；多个相互独立的方法应拆分登记。

### CAP-NAR-XXX｜能力名称

- **当前成熟度：** T0 / T1 / T2 / T3 / T4 / NOT QUALIFIED
- **状态：** CANDIDATE / NEEDS_MORE_EVIDENCE / T3_INTEGRATED_PENDING_RUNTIME / RUNTIME_SUPPORTED / T4_FIELD_VALIDATED / BLOCKED / REVISE / RETIRED
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
| CANDIDATE | 观察到初步有效表现，尚未达到 T2 |
| NEEDS_MORE_EVIDENCE | 样本不足、边界未测或缺少独立重复 |
| NEEDS_T3_PROVENANCE_AND_CROSS_SCENE | 有 T2 证据且方法已写入 Skill，但训练来源顺序/固定版本跨场景链尚未完成 |
| T3_INTEGRATED_PENDING_RUNTIME | T3 来源、Skill 版本、综合与跨场景验证均可追溯；尚未证明正常 Runtime 入口自然应用 |
| RUNTIME_SUPPORTED | 已在受控 Runtime 迁移测试中观察到自然应用；仍不等于真实 Session T4 |
| T4_FIELD_VALIDATED | 多个真实 Session 的适用场景中持续有效，且没有明显副作用 |
| BLOCKED_BY_G-XX | 存在未解决硬失败，阻止该能力领域晋级 |
| REVISE | 发现副作用、适用边界错误或表现退化，需要修订 |
| RETIRED | 已被更好方法替代或不再适用；保留历史记录 |

登记项不得仅因文档存在、合成测试一次 PASS 或模型自评而进入 T4。任何硬门槛 FAIL 都不能被平均分或其他能力的正向证据抵消。

## 6. 登记维护规则

1. 先检查现有 Training Log、Skill、Evaluation Report 和测试报告，引用现有证据，不复制大段材料。
2. 缺少精确 commit、训练来源、跨场景证据或 Skill 位置时，保持待核验，不补造。
3. T3 登记完成后，才可将该能力作为 NARRATIVE_RUNTIME_TRANSFER_REGRESSION_v1 的具体迁移对象。
4. 每次 Skill 发生影响该能力的修改时，更新 Skill 版本映射并按影响选择回归测试。
5. 每次真实 Session 发现失效或副作用，更新状态并关联 OPEN_TRAINING_BACKLOG。
6. 退役能力不得删除历史来源；说明替代项与退役原因。
7. 本表不替代 Backlog、Session Log、Runtime State、Context Trace 或综合评价框架。
