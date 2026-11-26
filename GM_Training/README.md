# GM 能力培养与运行体系

本目录维护跨规则系统可复用的 GM 能力、运行编排、训练与评价。核心原则是：**GM 能力必须在真实场景中有机联动，最终以综合表现验收；专项文件只负责专业方法，不是彼此隔离的运行模块。**

## 1. 首要入口

- [GM 能力架构](./00_GM_CAPABILITY_ARCHITECTURE.md)：全体系的权威结构、能力联动模型、综合优秀标准和文件职责。
- [TRPG GM Skill](./SKILL.md)：运行入口和现场编排。新对话恢复、风险路由、人物/叙事联动、状态维护与 Session 收束。
- [叙事质量基准](./NARRATIVE_QUALITY_BASELINE.md)：跨专项测试通用的叙事质量标准、信息正确性门槛、错误容忍度、评分锚点与低压力校准方案。
  - [基准场景 GM Packet](./Training_Logs/NARRATIVE_QUALITY_BASELINE_GM_PACKET.md)（GM-only）
  - [基准场景玩家启动提示](./Training_Logs/NARRATIVE_QUALITY_BASELINE_PLAYER_PROMPT.md)
  - [基准场景独立审核表](./Training_Logs/NARRATIVE_QUALITY_BASELINE_REVIEW_CHECKLIST.md)
  - [独立会话执行提示](./Training_Logs/NARRATIVE_QUALITY_BASELINE_EXECUTION_PROMPT.md)
- [综合能力评估框架](./04_EVALUATION_FRAMEWORK.md)：硬门槛、综合体验维度、场景联动评价和整体优秀判定。

## 2. 专业能力规范

| 文件 | 职责 |
|---|---|
| [通用 GM 原则](./01_CORE_GM_PRINCIPLES.md) | 跨系统主持底线、玩家能动性、世界自主性、公平与纠错 |
| [人物模拟 Skill](./CHARACTER_SIMULATION_SKILL.md) | 人物目标、知识、动机、关系、个人印记、行为与自主性 |
| [叙事呈现 Skill](./NARRATIVE_PRESENTATION_SKILL.md) | 空间、环境、信息、对白/动作、场景焦距与节奏 |
| [主持独立性与裁决纪律](./06_IMPARTIALITY_AND_ADJUDICATION_DISCIPLINE.md) | 公平裁定、反迎合与反刁难 |
| [运行控制协议](./07_RUNTIME_CONTROL_PROTOCOL.md) | 风险路由、事实/权限、连续性、T0、Context Assembly / Trace 与错误恢复 |
| [线索与来源账本](./08_CLUE_AND_SOURCE_LEDGER.md) | 线索、公平获取路径、来源和知识边界 |

人物模拟与叙事呈现不是两个独立的现场阶段。人物决定行动，环境影响行动，玩家行动改变局势，叙事呈现把结果交给玩家；主 Skill 负责统一调度。

## 3. 备团、带团与连续性

- [工作流程与 Preflight](./02_WORKFLOW_AND_PREFLIGHT.md)
- [Session Log 模板](./03_SESSION_LOG_TEMPLATE.md)
- [系统/模组登记](./05_MODULE_AND_SYSTEM_REGISTER.md)
- [模组文件夹标准](./09_MODULE_FOLDER_STANDARD.md)
- [技能研究与适配](./10_SKILL_RESEARCH_AND_ADAPTATION.md)
- [模组设计与即兴复盘模板](./11_MODULE_DESIGN_AND_IMPROVISATION_REVIEW_TEMPLATE.md)
- [备团设计与第二轮审核](./12_PREP_DESIGN_AND_SECOND_PASS_REVIEW.md)
- [备团到运行交接](./13_PREP_TO_RUNTIME_HANDOFF_STANDARD.md)
- [高级模型 Prep QA 协议](./ADVANCED_MODEL_PREP_QA_PROTOCOL.md)
- [运行状态模板](./RUNTIME_STATE_TEMPLATE.md)
- [Context Assembly & Trace 设计记录](./Optimization_Reports/CONTEXT_ASSEMBLY_AND_TRACE_DESIGN.md)
- [Context Assembly & Trace 回归夹具 v1](./Acceptance_Test_Fixtures/CONTEXT_ASSEMBLY_TRACE_REGRESSION_v1.md)
- [历史设计归档 · Scene Continuity & Evidence Record 回归夹具 v1](./Acceptance_Test_Fixtures/SCENE_CONTINUITY_AND_EVIDENCE_RECORD_REGRESSION_v1.md)
- [可靠性与体验方向控制协议](./GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md)

## 4. 训练、复盘与缺陷追踪

- [综合训练体系](./NARRATIVE_TRAINING_PROGRAM.md)：综合诊断、专项修复、重新整合、跨场景迁移与实战验证。
- [微型箱庭实验室](./MICRO_SANDBOX_LAB/README.md)：可玩的短小开放场景，用于综合互动训练、稳定性观察和游戏体验验证。
- [微型箱庭 ↔ 实际跑团双向迁移协议](./MICRO_SANDBOX_LAB/CAPABILITY_TRANSFER_PROTOCOL.md)：规定训练方法如何进入真实跑团，以及真实 Session 的缺陷如何反向成为箱庭训练样本。
- [训练题库](./NARRATIVE_TRAINING_QUESTION_BANK.md)：专项题与综合题候选；题库不定义能力标准。
- [开放训练问题清单](./Training_Logs/OPEN_TRAINING_BACKLOG.md)：尚未解决的问题及后续验证要求。
- [2026-11-25《雨前过桥》箱庭实测记录](./Training_Logs/2026-11-25_MICRO_SANDBOX_001_BRIDGE_BEFORE_RAIN_REVIEW.md)：首个完成的箱庭运行样本、玩家反馈、观察和待验证项。
- [Narrative Stress Test 01｜社区中心暴雨撤离](./Training_Logs/NARRATIVE_STRESS_TEST_01_DESIGN.md)：持续压力下综合叙事质量与信息显著性动态升格测试设计。
- [Narrative Stress Test 01｜首轮运行记录](./Training_Logs/NARRATIVE_STRESS_TEST_01_RUN_RECORD.md)：八个合成行动的单会话自测；仅作内部诊断，不是独立盲测或真实跑团证据。
- [Narrative Stress Test 01｜玩家信息边界复核补遗](./Training_Logs/NARRATIVE_STRESS_TEST_01_PLAYER_INFORMATION_BOUNDARY_AUDIT.md)：纠正首轮自审遗漏，确认 ACTION 01 存在重大玩家信息通道泄露。
- [2026-11-24 场景描绘与动态叙事综合训练记录](./Training_Logs/2026-11-24_SCENE_AND_DYNAMIC_NARRATIVE_INTEGRATED_TRAINING.md)：便利店、搬家夫妻、仓库交接、医院走廊、旧办公楼、人物兴趣与日常场景等完整训练沉淀。
- [2026-11-24 NPC 对话与交流流畅度训练](./Training_Logs/2026-11-24_NPC_DIALOGUE_AND_CONVERSATIONAL_FLOW.md)
- [人物塑造与互动研究](../Research/CHARACTER_AND_INTERACTION_TRAINING_2026-11-24.md)
- [叙事工艺研究](../Research/NARRATIVE_CRAFT_RESEARCH_2026-11-23.md)
- [专业能力迁移机制](../CAPABILITY_TRANSFER.md)

训练成果只有经过重复验证，才能进入正式运行规范；文档更新不代表能力提升。新能力必须经过综合场景验证，确认没有造成旧能力退化。

## 5. 多系统隔离

- [多系统上下文隔离协议](../SYSTEM_CONTEXT_PROTOCOL.md)
- [系统目录](../Systems/README.md)
- [规则研究路线图](../Research/SYSTEM_RESEARCH_ROADMAP.md)

通用 GM 能力不包含任何具体系统的规则机制。规则、术语、官方裁定与系统专属适配统一归入 Systems 对应系统目录；战役人物、CANON、模组和状态归入 Campaigns。

## 6. 验收与可靠性测试

- [GM 自测与验收执行协议](./SELF_TESTING_PROTOCOL.md)：默认的 GitHub 版本化夹具、独立测试会话、分阶段输入、BLOCKED 处理和独立审核流程。
- [GM 系统质量验收提示词](./GM_SYSTEM_ACCEPTANCE_PROMPT.md)
- [P0/P1 验收报告与测试夹具](./Acceptance_Reports/)
- [验收测试夹具与执行提示](./Acceptance_Test_Fixtures/README.md)：合成夹具、目标 Chat 执行提示与操作者协议。

合成测试、盲测和真实跑团分别报告。未执行的测试必须标记 NOT STARTED / NOT TESTED；不得以文件已更新推断运行可靠性通过。

## 7. 维护原则

1. 不把具体系统机制写入通用 GM Skill。
2. 不让训练样本变成正式 Campaign CANON。
3. 不以模块分数平均值掩盖关键短板或硬失败。
4. 专项训练后必须进行综合再整合。
5. 不为了目录整齐而进行没有收益的大规模路径搬迁；优先保持现有稳定链接和权威入口。


## 8. 运行可靠性与综合验收材料

- [执行提示词与操作者协议](./Acceptance_Test_Fixtures/Execution_Prompts/README.md)：按目标 Chat 执行、独立审查和操作者隔离分类归档。
- [P1 性能与执行效率验证计划](./Optimization_Reports/GM_RUNTIME_P1_PERFORMANCE_PLAN.md)：性能验证阶段门槛与测量方案。

以下文件属于工程验收和测试执行资料，不代表测试已通过：

- [GM 系统质量验收报告](./Acceptance_Reports/GM_SYSTEM_ACCEPTANCE_REPORT_2026-11-24.md)
- [GM 系统优化方案](./Optimization_Reports/GM_SYSTEM_OPTIMIZATION_PLAN_2026-11-24.md)
- [GM 系统实施记录](./Optimization_Reports/GM_SYSTEM_IMPLEMENTATION_RECORD_2026-11-24.md)
- [P0 第三轮复核与 P1 交接](./Acceptance_Reports/GM_RUNTIME_P0_THIRD_ROUND_REVIEW_AND_P1_HANDOFF.md)
- [P1-0 修复与 P1-0C 交接](./Acceptance_Reports/GM_RUNTIME_P1_0_REMEDIATION_AND_P1_0C_HANDOFF.md)
- [P1-0R 持久化故障注入报告](./Acceptance_Reports/GM_RUNTIME_P1_0R_FAULT_INJECTION_REPORT_2026-11-25.md)
- [性能优化阶段交接与地基质量暂缓清单](./Acceptance_Reports/GM_RUNTIME_PERFORMANCE_PHASE_HANDOFF_2026-11-25.md)
- [P0 合成验收夹具 v1](./Acceptance_Test_Fixtures/GM_RUNTIME_P0_FIXTURE_v1.md)
- [P0 回归夹具 v2](./Acceptance_Test_Fixtures/GM_RUNTIME_P0_REGRESSION_v2.md)
- [P0 回归夹具 v3](./Acceptance_Test_Fixtures/GM_RUNTIME_P0_REGRESSION_v3.md)
- [P1-0C 定向回归夹具 v1](./Acceptance_Test_Fixtures/GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v1.md)
- [P1-0C 定向回归夹具 v2](./Acceptance_Test_Fixtures/GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v2.md)
- [T0 自然语言盲测执行状态](./Acceptance_Reports/T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_PREPARATION_AND_EXECUTION_STATUS_2026-11-24.md)
- [验收执行提示词与操作者协议](./Acceptance_Test_Fixtures/Execution_Prompts/README.md)：P0/P1/T0 执行提示与操作者隔离资料。

运行可靠性测试、叙事综合能力评估和真实跑团体验分别报告。合成测试通过不能证明实际跑团整体优秀；训练样本优秀也不能证明运行可靠性验收通过。
