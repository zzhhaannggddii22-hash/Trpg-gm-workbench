# 高级模型审核交接｜通用掷骰流程、三角机构检定与骰子 UI

> 审核对象：设计稿，不是已部署实现
> 设计分支：design/roll-resolution-and-triangle-dice-ui-2026-11-27
> 基线 main：5d19ab9188ac0f02b1b5ecf762f0d4b5f8642ae5
> 审核要求：独立审查；先报告问题，不要直接改写或合并文件。

## 审核任务

你是独立架构审核者。以固定基线 main 为依据审核本分支新增设计，不把设计稿当作已批准规则或已完成实现。

## 一、必须读取

1. GM_Training/ROLL_RESOLUTION_PROTOCOL.md
2. Systems/Triangle_Agency/Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md
3. Systems/Triangle_Agency/Dice_UI/README.md
4. Systems/Triangle_Agency/Dice_UI/roll-event.schema.json
5. GM_Training/SKILL.md
6. GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md
7. SYSTEM_CONTEXT_PROTOCOL.md
8. Systems/Triangle_Agency/README.md
9. Systems/Triangle_Agency/Rule_Reference/00_规则检阅协议.md
10. Systems/Triangle_Agency/Rule_Reference/01_基础规则与现场裁定.md
11. Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md
12. Systems/Triangle_Agency/Research/triangle-agency-rules-index.md
13. Campaigns/Zarek/SYSTEM_BINDING.md
14. Campaigns/Zarek/RULE_ADJUDICATIONS.md
15. Campaigns/Zarek/模组/Bower_Street/09_RESOURCE_LEDGER.md
16. Campaigns/Zarek/模组/Bower_Street/03_RUNTIME_STATE.md
17. Campaigns/Zarek/模组/Bower_Street/04_SESSION_LOG.md

规则条文存在疑问时，回查用户指定的中文 v22 完整原文，不得仅依赖速查摘要。

## 二、审核重点

### A. 通用架构
- 是否真正跨系统通用，有无把单一系统规则误写为通用规则？
- 是否有高效规则索引和按需检索路径？
- 是否清楚区分掷骰发起权与掷骰执行者？
- 默认助手代掷、用户明确自行掷骰的切换是否无歧义？
- 随机来源标记是否诚实，是否存在无法落地的随机源要求？
- 是否覆盖玩家选择权、重试、防重复、状态持久化与文本回退？

### B. Triangle Agency 规则准确性
- 是否准确体现没有通用技能检定、Default Failure、玩家发起掷骰的边界？
- Ask the Agency、Anomaly Ability、Conflict Resolution 是否分路由？
- 6d4 是否只用于适用的 Ask the Agency？
- QA 是否正确绑定本次 Quality，并保留明确例外？
- Q04 是否仅在其 Campaign 适用范围内生效？
- 原始骰面特殊触发、Burnout、QA、逐骰修改、最终结果的先后顺序是否符合 v22 原文与已批准桌裁？
- 是否遗漏骰型、自然结果、移除、重掷、费用、Stability、Triscendence、Chaos 或能力专属效果？
- 是否把规则疑点或本桌推论误写成官方规则？
- 是否把玩家选择错误地交给 GM 自动处理？

### C. 资源账本集成
- 是否复用 Resource Ledger、Runtime State、Session Log、Campaign 人物卡的现有权威分工？
- 是否会重复记账、重复应用或在余额待核时伪造后值？
- 多资源变化是否按字段拆分 Entry？
- 重试时是否沿用已掷骰和已应用交易？

### D. Dice UI
- 是否是独立纯展示组件，职责是否过宽？
- 事件 schema 是否完整、可校验、可版本化？
- 原始骰面、修改轨迹、最终骰面和被移除骰能否准确显示？
- 自然骰面结果是否与修改后结果清晰区分？
- 等待玩家选择、部分待核、完整结算是否有正确中间态？
- UI 是否可能泄露 GM-only 信息？
- UI 不可用时能否无损回退？
- 当前仓库和 ChatGPT 平台是否支持拟议封装？明确区分“设计可行”与“已部署可用”。

### E. 测试设计
提出最小但充分的回归测试矩阵，覆盖正常/异常流程、资源待核、重试、玩家自掷、助手代掷、玩家选择 QA、自然骰面特殊触发和 UI 中间态。

## 三、强制报告格式

1. 总体结论：APPROVE / APPROVE WITH CHANGES / REJECT。
2. P0/P1/P2/P3 问题表：文件/章节、具体问题、证据、影响、修订建议。
3. 规则准确性核验：已核验、待核验、争议条款。
4. 架构冲突检查：特别检查 Runtime §2–§4、§14.14、§14.20 与 Resource Ledger。
5. UI 可实现性：宿主能力、数据输入、渲染方式、平台限制；不得把设计文档说成已运行插件。
6. 测试矩阵：测试 ID、输入、预期行为、失败条件。
7. 推荐修订顺序。
8. 是否适合进入实现阶段及理由。

## 四、审核纪律

- 不要直接修改 main。
- 不要把设计稿写成官方规则、已批准 Campaign 桌规或已部署 UI。
- 不要为了让审核通过而删去未知、例外、权限或随机来源限制。
- 不要读取或引用与本次设计无关的 Campaign 隐藏剧情。
- 只审核掷骰规则调用、结算、资源接口、UI 和工程接入。
- 发现遗漏时提出具体补充内容和验收条件，不要只说“加强测试”。
