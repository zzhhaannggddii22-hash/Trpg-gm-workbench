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

- **问题**：中文核心 SRD 很丰富，但不能将其视作完整商业规则书与完整 Doskvol 设定集。
- **官方交叉核验**：官方 Licensing 页面明确指出，SRD 许可不包含 SRD 以外的素材，示例包括 Duskwall/Doskvol 设定、NPC、艺术和地图。
- **当前处理**：核心机制按 SRD 研究；正式 Campaign 使用的城市/派系/NPC/地图设定另需合法来源。未拿到设定原文时，不把 SRD 机制示例当成可任意复制的官方设定事实。
- **状态**：已确认边界。

## R-004｜Downtime Activity 与自由行动的区别

- **问题**：可能误读为 Downtime 阶段只能进行规定的六项活动。
- **官方交叉核验**：官方 Downtime Activities 说明只有列表上的 Downtime Activities 受次数限制；玩家仍可在休整期间自由移动、交谈、搜集情报、进行普通行动。
- **当前处理**：活动预算只约束六项正式 Downtime Activity，不限制所有叙事互动。
- **状态**：已确认。

## R-005｜Resistance 与 Armor 的时序

- **问题**：中文翻译容易让“抵抗后果”和“使用护甲”在执行时混成一个步骤。
- **官方交叉核验**：官方 v8.2 把 Resistance Roll 单独列出；Armor 是可消耗的装备格，按角色/组织状态在下一次 Score 开始的 Load 选择时恢复。
- **当前处理**：先确定后果，玩家决定是否用 Armor 或 Resistance；不得对同一后果把二者重复计算成两次抵抗。特殊护甲按对应能力明文处理。已标记 Armor 在下一次 Score 选择 Load 时恢复，不是在进入 Downtime 时恢复。
- **本轮审查修正**：发现 Runtime Manual 与 Runtime Protocol 的旧表述曾将恢复时点写成 Downtime；已依据官方 Resistance & Armor 页面更正，并将时点加入 BLD-T46 回归覆盖。
- **状态**：时序已按官方来源核验；Campaign 版本锁定前仍保留版本复核。

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
