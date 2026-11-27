# Triangle Agency｜Module Closeout Adapter
## 中文 v22 · System-specific rules adapter

> 归属：`Systems/Triangle_Agency/Rule_Reference/`
> 对应通用规范：[Module Closeout & Resource Reconciliation Protocol](../../../GM_Training/MODULE_CLOSEOUT_AND_RESOURCE_RECONCILIATION_PROTOCOL.md)
> 适用版本：Triangle Agency 中文 v22。
> 本文件只声明系统专属规则与适配要求；Campaign 的批准桌规和具体模组触发证据仍保存在对应 Campaign / Module 权威记录中。

---

## 1. 适配边界

- 本适配器不改变通用事务阶段、操作身份、PREPARE Manifest、字段应用、独立读回或最终发布语义。
- 具体奖励数值、任务目标、报告评级、MVP 资格、Demerits 变化、Time 奖励数量和资源恢复时点，必须回到当前 Module 原文、中文 v22 规则及 Campaign 已批准桌规核验。
- 不得把 Bower Street 的数值和特殊桌规直接套用到其他 Module。
- Campaign 桌规可以调整规则明确开放的配置点（例如 Time 的奖励时机/数量），不能默默改变 Work/Life Balance 标记、交叉划除、Playwall 授权或其他未被开放的规则效果。

## 2. 系统资源与字段分类

| 字段 | 结团适配要求 | 权威/证据要求 |
|---|---|---|
| QA（按 Quality） | 逐项处理；不得合并为一个通用 QA 池。恢复时按适用规则和最终上限处理 | Resource Ledger 保留消耗/恢复 Entry；人物卡保存最终跨模组快照 |
| Burnout | 独立于 QA 记录；按具体规则与当前桌裁处理 | 需要对应检定/事件证据；不得从 QA 消耗反推 |
| 普通 Chaos Pool | 先由 Campaign/Module 规则确定作用域、初值和重置节点；不得默认跨模组持续 | 当前余额按 Runtime/Resource Ledger 的唯一权威读取；未核实余额不得写 0 |
| Commendations | 按规则与已确认奖励逐项核算；按 Campaign 账本/人物卡约定作为持续字段 | 每项奖励有资格身份、触发事件、规则依据和应用证明 |
| Demerits | 作为持续字段逐笔核算；不能因旧人物卡显示 0 就忽略后续事件 | 必须追溯实际处分/事件；缺失时保持 UNKNOWN / DISPUTED |
| Time（可使用） | 与 Work/Life Balance 的已花费/剩余字段分开；按有效规则分别记账 | 每次奖励/消费与相应轨迹标记分别记录，不以一字段推算另一字段绝对值 |
| Work/Life Balance 轨迹格 | 精确到 Track 与 Box Position；标记来源区分 TIME_SPEND、MISSION_MVP、PROBATION、OTHER_RULE | 每次标记及跨轨迹划除分别记录，不能只记“成长 +1” |
| Loose Ends | 区分 Campaign 基线与本 Module 净增量；明确无变化时记 +0 | Module 结算记录增量；Campaign State 保存累计值 |
| 关键道具充能/次数 | 逐项判断是否存在跨模组一次性/不可恢复限制；仅按规则恢复 | Resource Ledger 保留消耗和恢复；人物卡保留结团后快照 |

普通 Chaos Pool 的作用域、初值和结束重置必须由当前 Campaign/Module 配置；例如 Bower Street 采用“模组内资源、模组结束清零”，不能将此配置推广到所有 Campaign。

## 3. 奖励与成长的分项核验

结团时分别建立资格与事件，不得合并成一个“完成任务奖励”：

1. 核心任务/异常处理结果；
2. 任务报告内容与评级；
3. 玩家事前已获知的每项可选目标；
4. R&D/部门或其他授权行为；
5. Mission Superlatives（MVP、Probation、Participant）；
6. 其他规则明确的奖励或处分；
7. 免费轨迹标记、轨迹格收益、玩家选择和实际 Time 支出。

每项奖励需关联唯一 `reward_eligibility_id`、规则条款、Module/事件身份、触发证据、玩家事前知情状态和应用状态。相同资格从不同结算入口重复出现时，复用同一 Eligibility ID。

未公开的可选目标不得事后追加奖励。奖励数值不得从其他 Module、旧模板或 Bower Street 结算表推断。

## 4. 依赖图：Module Closeout 与 Intermission 分离

Triangle Agency 需要将“模组结团”和“幕间处理”视为相邻但不同的规则阶段。

### 4.1 Module Closeout 阶段

由 Module 原文、系统规则和 Campaign 桌规决定具体 DAG。至少检查：
- 最终任务结果；
- 任务报告及其评级；
- 奖励/处分资格；
- Mission Superlatives 资格；
- 本次已确认的免费成长/轨迹标记；
- Time 奖励及相关持续字段；
- 资源作用域、自动恢复/重置；
- Loose Ends 等 Module 指标；
- 结团后的源 Module 状态与交接字段。

若某个已确认的 MVP 免费 Competency 标记会提高某项 QA 上限，且当前适用规则要求 QA 在幕间恢复至新上限，则 DAG 必须包含：
`MVP eligibility → player track choice → apply new QA cap → restore QA to final cap`。

不得将这一示例写成通用层固定顺序；只有适配器在规则版本与 Campaign 配置中确认该依赖后才执行。

### 4.2 Intermission 阶段

Module CLOSED 不自动代表 Intermission 已完成。按中文 v22 与当前 Campaign 适配规则，幕间可能还需处理：
1. 确认 Module 已关闭及适用奖励/处分；
2. 对账持续资源和模组结束自动重置；
3. 按有效 Campaign 规则确定 Time 奖励，并分别记录奖励与可使用余额；
4. 确定所有适用 Superlatives 及其免费轨迹标记；
5. 按实际顺序逐项执行标记；每项标记分别检查轨迹收益与 Playwall 代码；
6. 只读取已授权的精确 Playwall 文档，并处理其适用效果；
7. 完成规则要求的场景与玩家选择；不得把计划写成已完成；
8. 同步人物卡、Work/Life Balance、Campaign Playwall Ledger、相关 Module/Session 记录与玩家投影；
9. 独立回读并核对每个标记、代码、文档、效果和余额；
10. 只有没有待处理必需步骤，或每项均已明确 BLOCKED/DEFERRED 且有理由时，才关闭 Intermission。

未完成的幕间选择不自动改变源 Module 已发布的 CLOSED；但它可能阻止依赖该选择/效果的特定成长、购买或目的 Module READY。具体阻塞由目的 Module 依赖清单判断。

## 5. Playwall 的授权与披露边界

Playwall 必须严格按中文 v22 的标记授权处理：

- 只有实际被标记、且该格确实印有对应代码的轨迹格，才授权读取该文档。
- 检查每个实际标记来源，包括 Time Spend、Mission MVP、Probation 和其他明确授权的标记；不要只检查 Time 标记。
- 精确记录 Track、Box Position、标记来源、该格代码、授权结果和文档版本。
- 只检索该格实际授权的精确文档；不得提前浏览相邻代码、未来文档或未授权资料。
- 已标记格没有代码时记录 NONE；划除的格不能视为解锁。
- 文档解锁、文档读取、效果应用、玩家呈现是不同状态，不得合并成一个“已解锁”标记。
- 隐藏文档、未解锁内容、未来条件与 GM-only 秘密不得提前向玩家揭晓。

### 单人桌配置

当前 Campaign 框架为单人桌。精确代码解锁后，GM 可直接检索并阅读完整的已授权文档，使用其裁定角色收益并准备必要场景；不要求额外的玩家私读确认，也不追踪玩家是否与其他玩家分享。该简化只移除多人桌的私读/分享门槛，不改变解锁条件、精确文档限制、先决条件或 GM-only 内容边界。

如果 Campaign 改为多人桌，恢复中文 v22 对玩家私读和玩家控制分享的处理，不沿用单人桌简化。

## 6. 资源与标记事件记录

每个结算/幕间事件应保留适用字段：
- event_id / reward_eligibility_id / mark_event_id；
- Campaign、Module、Session、Run 身份；
- 资源/轨迹、Track、精确 Box Position；
- 变化前、变化量、变化后（未知项保持 UNKNOWN）；
- 触发原因、规则条款、规则版本和桌规引用；
- 标记来源及是否实际花费 Time；
- 其他轨迹划除的位置（如规则要求）；
- QA 上限变化与恢复结果；
- Playwall 代码、授权、精确文档版本及读取/效果状态；
- 玩家选择与确认依据；
- 字段应用证明、发布批次和人物卡同步引用。

一次标记不等于一次 Time 消费。Mission MVP 的免费 Competency 标记不执行 Time Spend 的跨轨迹划除；仍须检查该格是否含有 Playwall 代码。Participant 等不产生轨迹标记的收益，不得误触发 Playwall 解锁。

## 7. 当前可用规则依据

- `01_基础规则与现场裁定.md`：QA 与 Quality 对应、Burnout/QA 时序及资源记录要求。
- `02_PLAYWALL_UNLOCK_AND_INTERMISSION_PROTOCOL.md`：轨迹格授权、Time Spend、免费标记、Playwall 精确读取、单人桌执行边界及幕间步骤。
- `04_规则疑点与裁定记录.md`：尚未解决的规则疑点；遇到相关问题必须回查，不得把未裁定项当成规则。
- Campaign 的 `RULE_ADJUDICATIONS.md`：仅在其明确适用范围内生效。
- 当前 Module 的 GM Prep、结算报告、Session Logs 与 Resource Ledger：用于确认实际触发事件和数值，不替代规则来源。

若规则原文、系统摘要与 Campaign 桌规冲突，按当前桌面既定权威层级处理并记录差异；本适配器不自行裁决尚未解决的规则疑点。
