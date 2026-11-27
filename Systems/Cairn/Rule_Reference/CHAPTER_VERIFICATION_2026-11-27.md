# Cairn 2e 官方章节核验记录

> 核验日期：2026-11-27
> 权威来源：官方 Cairn 2e SRD 与其公开源仓库 yochaigal/cairn（main）。
> 范围：Player's Guide 6 章、Warden's Guide 23 章，共 29 个官方指南章节；社区中文 SRD 所称“31 个核心章节”与本次官方章节清单口径不同，故本记录按官方网页实际导航计数，不把两种计数混为一谈。背景页 20 项单独列为角色数据条目，不计入上述 29 章。
> 结果：章节来源与用途分类已完成。此结果不代表所有怪物、法术书、遗物、背景、模组表格均已逐项本地化，也不代表 Candidate 已通过真实跑团验收。

## 1. Player's Guide（6/6）

| 章节 | 状态 | 核验结果 |
|---|---|---|
| Character Creation | VERIFIED_SOURCE | 背景选择、起始物品、属性、HP、Traits、Inventory、Bonds、Omens。背景页是独立的逐条数据；当前 Campaign 的 Fieldwarden 与 Bonekeeper 需按各自官方背景页和锁定人物卡执行。 |
| Core Rules | VERIFIED_SOURCE | Attributes、Saves、Healing & Recovery、Deprivation/Fatigue、Armor、Reaction、Morale、Hirelings、Die of Fate、Combat、Scars、Magic。属性恢复与 Hireling 创建/工资已补入本地运行手册。 |
| Marketplace | VERIFIED_SOURCE | Armor、Weapons、Transport、Upkeep/Recovery、Hireling 日薪、Gear。价格表作为官方参考数据；具体可用性受地点与虚构经济影响。 |
| Overview & Principles | VERIFIED_SOURCE | Neutrality、Classless、Death、Fiction First、Growth、Player Choice，以及玩家/监守原则；作为主持行为约束，不新增数值机制。 |
| Procedures | VERIFIED_SOURCE | Dungeon Exploration、Panic、Light/Doors/Traps、Wilderness Watches/Points/Travel/Weather/Events/Actions、Sleep/Make Camp、Downtime。Downtime 已补入 Runtime Protocol §4.6。 |
| Vald | VERIFIED_SOURCE | 默认世界设定、Wood、Roots；仅在 Campaign 绑定 Vald 时作为设定依据，不强加给非 Vald 战役。 |

## 2. Warden's Guide（23/23）

逐章结果与用途分类见 WARDEN_GUIDE_INDEX.md。本次确认的边界：

- 运行原则/主持章节：Combat、Dungeon Exploration、Growth、Knowledge and Perception、Saves、Variable Difficulty。
- 具体规则章节：Detachments；与 Player's Guide 对应规则联合调用。
- 生成程序：Creating Backgrounds、Creating Monsters、Dungeon Seeds、Forest Seeds、Naming Procedures、Pointcrawls、Setting Seeds。
- 数据目录：Bestiary、NPC Tables、Reliquary、Spellbooks。
- 示例/设定/参考：About the Example Party、Bibliography、Bonds and Omens、Vald、Wilderness Exploration（示例）。

上述分类意味着：生成工具不应被当成每轮强制流程；数据目录按具体对象查原文；示例和默认设定不自动成为所有 Campaign 的 Canon。

## 3. Backgrounds（20 项独立数据条目）

官方 2e 有 20 个独立 Background 页面。它们不是额外的核心章节，但其装备、能力、表格、特殊触发必须以对应页面为准。

| 当前 Campaign 相关性 | 背景 | 处理状态 |
|---|---|---|
| CA01_Zaf / Zaf | Fieldwarden | Campaign 人物卡已有锁定结果；其额外 Bonds 规则必须保留。 |
| CA01_Zaf / Catherine | Bonekeeper | 需与人物卡逐项核对该背景的专属起始装备、表格结果和特殊效果；不可仅凭通用角色创建流程推断。 |
| 其余 18 项 | Aurifex、Barber-Surgeon、Beast Handler、Cutpurse、Fletchwind、Foundling、Fungal Forager、Greenwise、Half Witch、Hexenbane、Jongleur、Kettlewright、Marchguard、Mountebank、Outrider、Prowler、Rill Runner、Scrivener | 已确认官方独立页面存在；具体数据按 Campaign 角色背景按需查阅，不复制成一个虚假的通用背景规则。 |

## 4. 本轮落实的规则修订

1. CR-ATTR-REC：从 PARTIAL 改为 VERIFIED_CORE。官方规则已明确：属性损失通常可通过一周休息并由治疗者/适当专业支持恢复；Marketplace 的 Medical Healing 标价 50 gp，但不能推断所有伤势都保证以该价完整治愈。
2. CR-HIRELING：从 PARTIAL 改为 VERIFIED_CORE。官方已明确两种创建流程，Marketplace 提供 12 类雇工与每日工资。通用忠诚/士气检定并未在核心规则中建立，不得自行补入。
3. CR-FAT：保留 Deprived 超过一天后按日增加 Fatigue 的官方规则；精确到哪一个钟点/Watch 执行周期 tick 未被官方明确，运行时 tick 边界必须标记为 GM_INFERENCE / bookkeeping convention。
4. CR-PANIC：官方规定 Panicked 角色 HP=0、首轮不能行动、攻击 Impaired，并须用行动 + WIL Save 克服。解除 Panic 是否自动恢复 HP，官方未说明；不自动回填 HP 是 Workbench 的 GM_INFERENCE。
5. CR-INV：官方规定填满 10 格时 HP 降至 0；清空格子后是否自动恢复 HP，官方未说明；不自动回填 HP 是 Workbench 的 GM_INFERENCE。
6. Downtime：补入一次一项行动、危险/恢复期限制、1–5 Milestones、Costs、Research、Training、Strengthening Ties 的运行程序。官方未规定统一每周次数或固定成长数值。

## 5. 仍然按需查原文的资料，不作为章节核验失败

- 每个具体 Bestiary 生物的完整 stat block 与专属能力；
- 每本具体 Spellbook 的法术效果；
- 每件具体 Relic 的使用次数、能力和 Recharge 条件；
- 角色背景专属表格、能力与物品；
- Campaign/Module 专属地图、NPC、怪物、事件表与特殊规则。

这些属于条目级数据，而不是通用章节缺失。发生实际调用时必须按确切对象查证，不得以摘要、相似名称或其他版本补洞。

## 6. 尚未由章节核验解决的验收事项

章节核验完成不等于 Candidate 激活。以下项目按用户确定的计划在实际跑团中验证，不另建重复的模拟验收替代真实运行：

- Runtime State、Session Log、事件事务、Handoff 与恢复是否在真实宿主环境中连续、幂等、可追溯；
- 规则在实际玩家行动中的正确调用、状态更新、时间/资源推进与边界处理；
- NPC 的知识边界、资源约束、主动性、离场—重逢连续性与现场演绎；
- 单人/双 PC 队伍的旅行、守夜、战斗风险与雇工使用是否可运行。

规则资料剩余不确定性由 GM 继续查官方资料；确无官方明文时，明确标记 GM_INFERENCE，不把推论伪装成 SOURCE。

## 7. 官方来源

- [Second Edition](https://cairnrpg.com/second-edition/)
- [Player's Guide](https://cairnrpg.com/second-edition/players-guide/)
- [Warden's Guide](https://cairnrpg.com/second-edition/wardens-guide/)
- [Official source repository](https://github.com/yochaigal/cairn/tree/main/second-edition)
- [Official Chinese localization index](https://fi.cairnrpg.com/localization/second-edition/chinese/)
