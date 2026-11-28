# Blades in the Dark｜规则疑点、译文问题与版本差异

> 状态：持续更新  
> 原则：解决后保留记录，不静默覆盖；官方规则、中文翻译、GM 解释与桌面适配分开。

## R-001｜Long-Term Project 的 Critical 进度

- **中文来源位置**：`content/5-downtime/04-index.md` 的 Long-Term Project 段落与 `content/5-downtime/06-index.md` 的总结段。
- **问题**：中文正文一处写 Critical 推进 4 格，另一处写 5 格。
- **官方交叉核验**：官方 Full Player's Kit v8.2 的 Downtime 速查表写明 1–3=1、4/5=2、6=3、Critical=5；官方 Downtime Activities 网页也使用 5 格。
- **当前处理**：采用 5 格。
- **状态**：<badge>待锁定 Campaign 规则版本</badge>。该结论在选定正式版本后再做最终锁定。

## R-002｜SRD 版本编号缺失

- **问题**：中文 SRD 页面没有清晰标注它所翻译的 SRD 修订号；上游中文网站仓库的最后核验快照为 2023-08-15。
- **官方交叉核验**：官方 Player's Kit 文件标注 v8.2，但玩家工具包版本不自动等同于核心规则书的出版版本。
- **当前处理**：系统状态保持 candidate。正式 Campaign Binding 必须写明所采用版本；任何无法确认的差异要标记来源。
- **待办**：取得并对照用户选择的商业核心规则版本及官方勘误。

## R-003｜SRD 与世界设定边界

- **问题**：中文核心 SRD 不能视作完整商业规则书与完整 Doskvol 设定集。
- **官方交叉核验**：官方 Licensing 页面明确指出，SRD 许可不包含 SRD 以外的素材，示例包括 Duskwall/Doskvol 设定、NPC、艺术和地图。
- **新增来源**：用户已提供完整《暗夜刀锋》中文版规则书 V1.3；其 PDF pp.243–314 包含多斯科沃城市指南、地区、派系、NPC 与附录工具表。
- **当前处理**：城市设定已有合法的用户提供本地来源，私人原书作为查阅基准；公开仓库只放原创城市指南索引，不复制完整城市设定正文。
- **状态**：来源缺口已解决；本地结构化索引仍待继续完善。

## R-004｜Downtime Activity 与自由行动的区别

- **问题**：可能误读为 Downtime 阶段只能进行规定的六项活动。
- **官方交叉核验**：官方 Downtime Activities 说明只有列表上的 Downtime Activities 受次数限制；玩家仍可在休整期间自由移动、交谈、搜集情报、进行普通行动。
- **当前处理**：活动预算只约束六项正式 Downtime Activity，不限制所有叙事互动。
- **状态**：已确认。

## R-005｜Resistance 与 Armor 的时序

- **问题**：中文翻译与不同官方速查资料容易让普通 Armor 使用格与 Playbook Special Armor 能力资源的恢复节点混成一个步骤。
- **核心规则书核验**：用户提供的《暗夜刀锋》中文版规则书 V1.3 对应英文原版版权页标注 v8.2。核心规则书 PDF 第 39 页明确写明：普通 Armor 使用格在“为下一次刻痕选择负载时”恢复。
- **Special Armor 核验**：核心规则书 V1.3 的多个 Playbook 能力条目（PDF pp.68、72、76、81、85、89、93）明确写明 Special Armor 在 Downtime 开始时恢复。
- **资料冲突**：Full Player's Kit v8.2 的 Downtime 速查表将 Armor 恢复列在 Downtime；完整核心规则书正文则把普通 Armor 的恢复时点写为下一次 Score 选择 Load。官方 SRD 的 Resistance & Armor 网页同样写为选择下一次 Score 的 Load 时恢复。
- **当前处理**：以完整核心规则书正文为普通 Armor 的运行基准：下一次 Score 选择 Load 时恢复。Special Armor 是独立资源，按具体 Playbook 能力文本在 Downtime 开始时恢复。不得把二者合并成统一的“Downtime 恢复全部 Armor”。
- **证据优先级判断**：完整核心规则书正文高于玩家速查表的简写/汇总；速查表冲突保留为来源注记，不再阻止运行。
- **状态**：RESOLVED FOR V1.3 / English v8.2 baseline；其他版本仍需按其原文核验。

## R-006｜0d Action Roll

- **中文来源**：基本规则的 Action Dice 条目。
- **处理**：0d 或负骰池掷 2d，取低值；按本系统规则不会产生 Critical。关键裁定前仍需用 Campaign 锁定版规则再核对。
- **状态**：已录入；待测试用例。

## 后续疑点登记模板

```yaml
issue_id: R-XXX
scope: rule_id_or_topic
source_version: unknown
source_location: file/page/section
problem: ""
source_text: ""
translation_or_version_conflict: ""
runtime_impact: ""
current_handling: ""
status: OPEN
```
