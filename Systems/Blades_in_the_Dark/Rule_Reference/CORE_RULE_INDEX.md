# Blades in the Dark｜核心规则索引

> system_id: `blades_in_the_dark`  
> 当前阶段：candidate / 核心与专题运行规则已整理，尚待行为验证  
> 核心规则来源：用户提供《暗夜刀锋》中文版规则书 V1.3（英文原版 v8.2）；中文 SRD 与官方 Player's Kit v8.2 用于交叉核验  
> 规则正文镜像：存放于用户私人资料库；本公开仓库只保留授权来源、原创摘要与运行逻辑。

本索引用于按触发定位运行规则。它不要求每轮把整本规则重新加载，也不替代 Campaign 指定版本的完整原文。

## 1. 系统路由与规则 ID

| 规则域 | Rule IDs | 触发条件 | 运行入口 |
|---|---|---|---|
| 骰型与裁定 | BLD-DICE-01–05 | 出现行动、结果不确定或抵抗 | [CORE_RULES_RUNTIME §2](./CORE_RULES_RUNTIME.md#2-骰型与基础结算) |
| Action / Position / Effect | BLD-ACT-01–08 | 玩家试图克服危险/麻烦障碍 | [§3](./CORE_RULES_RUNTIME.md#3-action-roll行动骰) |
| Consequence / Resistance / Armor | BLD-CNS-01–06 | Action Roll 产生后果、玩家决定抵抗 | [§4](./CORE_RULES_RUNTIME.md#4-consequenceresistance-与-armor) |
| Clocks / Fortune / Gather Info | BLD-CLK-01–05 | 存在持续进度、未知程度或调查问题 | [§5](./CORE_RULES_RUNTIME.md#5-clocksfortune-与-gather-information) |
| Score / Plan / Engagement | BLD-SCR-01–06 | Crew 确定一个任务目标并进入行动 | [§6](./CORE_RULES_RUNTIME.md#6-score计划与-engagement-roll) |
| Flashback / Teamwork | BLD-FLB-01–04 | 玩家补充过去准备或团队协作 | [§7](./CORE_RULES_RUNTIME.md#7-flashback-与-teamwork) |
| Downtime | BLD-DOW-01–08 | Score 结束、进入组织休整阶段 | [§8](./CORE_RULES_RUNTIME.md#8-downtime-活动) |
| Payoff / Heat / Entanglement | BLD-SET-01–05 | 每次 Score 结算 | [§9](./CORE_RULES_RUNTIME.md#9-score-结算payoffheatentanglements) |
| Crew / Factions / Cohorts | BLD-CRW-01–07 | 组织成长、派系关系或同伙受影响 | [§10](./CORE_RULES_RUNTIME.md#10-crewfactions-与-cohorts) |
| XP / Advancement / Vice | BLD-ADV-01–05 | Session 结束、XP 结算、角色成长 | [§11](./CORE_RULES_RUNTIME.md#11-pc-与-crew-成长) |
| Ritual / Magnitude / Crafting | BLD-ARC-01–08 | 超自然仪式、Magnitude、发明/打造/改造与炼金物品 | [ARCANE_AND_CRAFTING_RUNTIME.md](./ARCANE_AND_CRAFTING_RUNTIME.md) |
| PC / Crew Ability | BLD-ABIL-01–04 | 创建角色/组织、获得能力、触发特殊能力效果 | [ABILITY_RUNTIME_MATRIX.md](./ABILITY_RUNTIME_MATRIX.md)；[PLAYBOOKS_AND_CREW_REFERENCE.md](./PLAYBOOKS_AND_CREW_REFERENCE.md) |
| Doskvol City Guide | BLD-CITY-01 | 地区、派系、NPC、街头流言与城市生成表 | [DOSKVOL_CITY_GUIDE_INDEX.md](./DOSKVOL_CITY_GUIDE_INDEX.md) |
| Optional Playsets | BLD-EXT-01–03 | Campaign 明确启用红水之城/义警/利维坦之歌 | [RED_WATERS_CITY_RUNTIME.md](./RED_WATERS_CITY_RUNTIME.md)；[VIGILANTES_PLAYSET_RUNTIME.md](./VIGILANTES_PLAYSET_RUNTIME.md)；[LEVIATHAN_SONG_RUNTIME.md](./LEVIATHAN_SONG_RUNTIME.md) |
| Items / Load / Armor Loadout | BLD-ITEM-01–04 | Score 负载、标准物品、护甲携带与消耗 | [STANDARD_ITEMS_AND_LOAD_REFERENCE.md](./STANDARD_ITEMS_AND_LOAD_REFERENCE.md) |
| Crew Creation / Hunting Grounds / Claims | BLD-CRW-START-01、BLD-CRW-HUNT-01–02、BLD-CRW-CLAIM-01–03 | 建立组织、偏好业务奖励、夺取/失去 Claim | [CREW_CLAIMS_AND_STARTUP_REFERENCE.md](./CREW_CLAIMS_AND_STARTUP_REFERENCE.md) |

## 2. Action 与 Attribute 对照

| Attribute | Actions |
|---|---|
| Insight | Hunt（狩猎）、Study（研究）、Survey（勘察）、Tinker（修补） |
| Prowess | Finesse（灵巧）、Prowl（潜行）、Skirmish（冲突）、Wreck（破坏） |
| Resolve | Attune（同调）、Command（命令）、Consort（交际/勾结）、Sway（动摇） |

行动选择必须与角色当前正在做的事情匹配。不能为了使用高点数行动而脱离虚构情境。上述中文术语沿用本项目目前的工作译法；正式 Campaign 应在 SYSTEM_BINDING 中锁定术语表版本。

## 3. 主要流程索引

```text
FREE PLAY
  ├─ 普通互动 / Gather Information
  ├─ 建立目标、关系、机会
  └─ SCORE
       ├─ 目标 → Plan + Detail → Load
       ├─ Engagement Roll → 初始 Position
       ├─ 行动循环 / Flashback / Teamwork / Clocks
       └─ 目标结局 → PAYOFF → HEAT → ENTANGLEMENT
                                  ↓
                               DOWNTIME
                                  ├─ PC Activities
                                  ├─ NPC/Faction Downtime
                                  └─ 返回 FREE PLAY
```

## 4. 当前规则覆盖状态

| 规则域 | 文档状态 | 交叉核验 | 行为验证 |
|---|---|---|---|
| 骰型、Action Roll、Position、Effect | 已整理 | 中文 SRD + 官方 v8.2 | 对应合成用例通过；真人待测 |
| Consequence、Resistance、Armor | 已整理 | 中文 SRD + 官方 v8.2 | 对应合成用例通过；真人待测 |
| Clocks、Fortune、Gather Info | 已整理 | 中文 SRD + 官方规则页 | 对应合成用例通过；真人待测 |
| Score、Engagement、Flashback、Teamwork | 已整理 | 中文 SRD + 官方规则页 | 对应合成用例通过；真人待测 |
| Downtime、Payoff、Heat、Entanglement | 已整理 | 中文 SRD + 官方 v8.2 | 对应合成用例通过；真人待测 |
| Crew、Faction、Cohort、成长 | 已补充 Cohort 生命周期与 Faction Downtime | 官方 Crew / Faction Game 页面及 v8.2 | T26、T55–T61 合成通过；真人待测 |
| Ritual、Magnitude、Crafting | 已建立完整触发式专题手册 | 官方 Magnitude / Rituals / Crafting 页面及 Player's Kit v8.2 | T62–T69 合成通过；真人待测 |
| 七种核心 Playbook / 六种 Crew Ability | 已建立触发、成本、范围与边界矩阵 | 官方 Full Player's Kit v8.2 | T70–T75 与既有能力用例合成通过；真人待测 |
| Doskvol / NPC / District 设定 | 来源已取得并建立城市指南索引；地区/派系/NPC 细项仍待拆解 | 核心规则书 V1.3 城市指南 | 未测 |

## 5. Playbook / Crew 能力调用

- 新建 PC / Crew 或选择成长能力时，先定位对应 Playbook / Crew Type。
- 记录角色/组织实际拥有的 Ability ID（使用官方英文名作为稳定 ID）。
- 运行时只检查当前事件相关的已拥有能力，不扫描全部未选择能力。
- 特殊能力改变骰池、Position、Effect、Resistance、Armor、Stress、Load、Downtime、Heat、Rep 或 Cohort 行为时，按其触发时点即时应用。
- 能力原文、角色卡版本或例外条件不明确时，回查 Campaign 指定版本的卡面；摘要不能替代完整能力文字。

## 6. 使用约定

- 规则触发时只调用对应 Rule ID；普通叙事互动不扫描全索引。
- 关键裁定须回到 Campaign 指定版本的完整原文核对条件、成本、时序、例外和状态变化。
- 任何规则缺口应记录到 [RULE_ISSUES.md](./RULE_ISSUES.md)，不借用其他 TRPG 机制填补。
- 社区 Playbook、Crew、Score 或扩展规则必须显式标记为 OPTIONAL / FAN-MADE，并在 Campaign Binding 中批准后才使用。
