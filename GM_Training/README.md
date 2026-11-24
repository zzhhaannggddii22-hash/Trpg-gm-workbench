# GM 能力长期培养项目

本目录只维护跨模组、跨规则系统可复用的 TRPG GM 专业能力：原则、方法、运行技能、叙事与角色模拟规范、评估框架及工作流程。系统规则、术语、机制摘要与系统专属研究统一归入仓库根目录 `Systems/<system_id>/`；战役事实归入 `Campaigns/`。

具体战役事实、人物卡、模组资料、Session 进度、Prep QA 与 Preflight 的执行记录，统一保存在对应 Campaign / Module / Session 目录。本目录不登记某个模组当前进行到哪一步，也不维护单次流程的状态。

## 权威原则
- 本公开仓库是 TRPG 专业资料的唯一工作主仓库。
- 规则以用户指定/提供的系统版本为准；模组事实以合法取得的原文为准。
- 区分 SOURCE、TABLE CANON、GM ADAPTATION、GM INFERENCE 与 UNKNOWN。
- 不把文档完善等同于能力提升；能力结论须由实际场景和复盘证据支持。
- GM-only 资料与玩家可见信息严格隔离；向玩家输出时只提供角色可知且当前有用的信息。

## 系统边界与资源规划

- 本目录不指定当前使用哪套规则，也不维护系统候选优先级；当前桌面由 Campaign 的 SYSTEM_BINDING 锁定。
- 各系统的正式状态、权威来源与专属资料入口见 [Systems/README.md](../Systems/README.md)。
- 尚未采用的系统及长期研究方向见 [TRPG 规则体系长期研究候选池](../Research/SYSTEM_RESEARCH_ROADMAP.md)。
- 引入新系统时，先建立独立规则权威来源、索引、专属 Skill 与系统 Preflight，再由 Campaign Manifest 绑定。未被当前桌面绑定的系统资料不得进入运行上下文。

## 系统隔离入口

- [多系统上下文隔离协议](../SYSTEM_CONTEXT_PROTOCOL.md)：系统绑定、加载顺序、切换和性能边界。
- [系统目录](../Systems/README.md)：各系统的唯一资料入口。

## 核心文件
- [通用 GM 原则](./01_CORE_GM_PRINCIPLES.md)
- [工作流程与 Preflight](./02_WORKFLOW_AND_PREFLIGHT.md)：流程定义、检查标准与执行要求。
- [备团设计与二次审核](./12_PREP_DESIGN_AND_SECOND_PASS_REVIEW.md)
- [高级模型 Prep QA 交接协议](./ADVANCED_MODEL_PREP_QA_PROTOCOL.md)
- [备团—带团联动与运行效率](./13_PREP_TO_RUNTIME_HANDOFF_STANDARD.md)
- [模组文件夹标准](./09_MODULE_FOLDER_STANDARD.md)
- [主持独立性与裁决纪律](./06_IMPARTIALITY_AND_ADJUDICATION_DISCIPLINE.md)
- [运行控制协议](./07_RUNTIME_CONTROL_PROTOCOL.md)
- [运行状态快照模板](./RUNTIME_STATE_TEMPLATE.md)：当前状态、事件增量与场景续接锚点。
- [线索与来源账本](./08_CLUE_AND_SOURCE_LEDGER.md)
- [Session Log 模板](./03_SESSION_LOG_TEMPLATE.md)
- [能力评估框架](./04_EVALUATION_FRAMEWORK.md)
- [TRPG GM Skill](./SKILL.md)
- [GM 可靠性与体验方向控制协议（T0）](./GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md)：模组体验契约、NPC 真相/认知/玩家信息隔离、即兴准入、低成本方向检查、T0 熔断与 GM-only 审计。
- [GM 系统质量验收提示词](./GM_SYSTEM_ACCEPTANCE_PROMPT.md)：交由高级模型对全套 GM 系统进行独立质量验收。
- [角色模拟 Skill](./CHARACTER_SIMULATION_SKILL.md)
- [叙事呈现 Skill](./NARRATIVE_PRESENTATION_SKILL.md)
- [叙事与主持能力训练体系](./NARRATIVE_TRAINING_PROGRAM.md)：训练课程、小说技法迁移、Prep/Runtime 分工与 Skill 沉淀门槛。
- [叙事训练题库](./NARRATIVE_TRAINING_QUESTION_BANK.md)：Casey 自主维护训练题；每次正式训练前先交用户审题。
- [专业能力迁移机制](../CAPABILITY_TRANSFER.md)

## 能力迭代原则
- 从实际运行与复盘中识别问题，区分备团设计、资料调用、现场执行、规则理解和模型推理等不同根因。
- 只把有证据、可复用的改进沉淀为通用规范；单一模组的事实与流程留在模组目录。
- 新增流程前评估其必要性、预期收益和维护成本，避免把偶发问题变成全局强制步骤。
- 训练目标与能力结论由评估框架及具体复盘记录维护，不在本 README 或通用 Skill 中登记单次战役进度。

## 项目边界
本目录维护 GM 专业方法，不重复存放战役人物卡、模组事实或当前运行状态。GM-only 资料不得进入玩家侧输出。高能力模型审查仅限获准的 GM-only 备团草稿，不自动获得玩家私密日志或其他无关档案。
