# Cairn 2e 官方内容目录（离线优先）

> 本地化日期：2026-11-27
> 上游：Yochai Gal 的官方 Cairn 2e 源仓库 https://github.com/yochaigal/cairn/tree/main/second-edition
> 许可：Cairn 文本采用 CC BY-SA 4.0。此目录保留作者/出版方署名、原始来源路径与上游文件；本地副本及其改编须按 CC BY-SA 4.0 署名并以相同方式共享。
> 使用优先级：Campaign/角色卡锁定事实 > 本地官方来源快照 > 本地 Runtime 规范化规则 > 官方在线当前版本（仅在发现版本变化、差异或本地未覆盖时回查）。
> 本地快照用于离线快速查阅；它们不是对规则的二次解释。若做了中文摘要或规则适配，必须另行标记 SOURCE / GM_INFERENCE / TABLE_ADAPTATION。

## 1. 完整目录快照

上游逐文件 blob SHA 与本地文件对应关系见 [OFFICIAL_CATALOG_SNAPSHOT_MANIFEST.md](./OFFICIAL_CATALOG_SNAPSHOT_MANIFEST.md)。

| 内容 | 本地文件 | 上游官方来源 | 覆盖范围 |
|---|---|---|---|
| Bestiary | [CAIRN2E_BESTIARY.md](./CAIRN2E_BESTIARY.md) | [Warden's Guide / Bestiary](https://github.com/yochaigal/cairn/blob/main/second-edition/wardens-guide/bestiary.md) | 84 个怪物条目；属性、HP、Armor、攻击、能力与 Critical Damage 均按条目原文保存。 |
| Spellbooks | [CAIRN2E_SPELLBOOKS.md](./CAIRN2E_SPELLBOOKS.md) | [Warden's Guide / Spellbooks](https://github.com/yochaigal/cairn/blob/main/second-edition/wardens-guide/spellbooks.md) | d100 法术书目录，100 项法术名称、效果描述与附带特征。 |
| Reliquary | [CAIRN2E_RELIQUARY.md](./CAIRN2E_RELIQUARY.md) | [Warden's Guide / Reliquary](https://github.com/yochaigal/cairn/blob/main/second-edition/wardens-guide/reliquary.md) | 46 件遗物的完整效果、使用次数、库存属性及 Recharge 条件（原文未给 Recharge 的条目不自行补造）。 |
| NPC Tables | [CAIRN2E_NPC_TABLES.md](./CAIRN2E_NPC_TABLES.md) | [Warden's Guide / NPC Tables](https://github.com/yochaigal/cairn/blob/main/second-edition/wardens-guide/npc-tables.md) | 姓名、Quirks、Background、Goals、Virtues、Vices 等生成表。 |
| Creating Monsters | [CAIRN2E_CREATING_MONSTERS.md](./CAIRN2E_CREATING_MONSTERS.md) | [Warden's Guide / Creating Monsters](https://github.com/yochaigal/cairn/blob/main/second-edition/wardens-guide/creating-monsters.md) | 怪物设计、能力与 stat block 创建/转换指南。 |
| Creating Backgrounds | [CAIRN2E_CREATING_BACKGROUNDS.md](./CAIRN2E_CREATING_BACKGROUNDS.md) | [Warden's Guide / Creating Backgrounds](https://github.com/yochaigal/cairn/blob/main/second-edition/wardens-guide/creating-backgrounds.md) | 自制背景原则与构建指南。 |

## 2. 全部官方 Backgrounds（20/20）

每个背景文件均保存完整原文，包括姓名表、起始装备、背景专属随机表、能力、特殊规则与结果。角色创建时必须读取所选背景的完整文件，不能只读摘要。

| d20 | Background | 本地文件 |
|---:|---|---|
| 1 | Aurifex | [BG_AURIFEX.md](./BG_AURIFEX.md) |
| 2 | Barber-Surgeon | [BG_BARBER_SURGEON.md](./BG_BARBER_SURGEON.md) |
| 3 | Beast Handler | [BG_BEAST_HANDLER.md](./BG_BEAST_HANDLER.md) |
| 4 | Bonekeeper | [BG_BONEKEEPER.md](./BG_BONEKEEPER.md) |
| 5 | Cutpurse | [BG_CUTPURSE.md](./BG_CUTPURSE.md) |
| 6 | Fieldwarden | [BG_FIELDWARDEN.md](./BG_FIELDWARDEN.md) |
| 7 | Fletchwind | [BG_FLETCHWIND.md](./BG_FLETCHWIND.md) |
| 8 | Foundling | [BG_FOUNDLING.md](./BG_FOUNDLING.md) |
| 9 | Fungal Forager | [BG_FUNGAL_FORAGER.md](./BG_FUNGAL_FORAGER.md) |
| 10 | Greenwise | [BG_GREENWISE.md](./BG_GREENWISE.md) |
| 11 | Half-Witch | [BG_HALF_WITCH.md](./BG_HALF_WITCH.md) |
| 12 | Hexenbane | [BG_HEXENBANE.md](./BG_HEXENBANE.md) |
| 13 | Jongleur | [BG_JONGLEUR.md](./BG_JONGLEUR.md) |
| 14 | Kettlewright | [BG_KETTLEWRIGHT.md](./BG_KETTLEWRIGHT.md) |
| 15 | Marchguard | [BG_MARCHGUARD.md](./BG_MARCHGUARD.md) |
| 16 | Mountebank | [BG_MOUNTEBANK.md](./BG_MOUNTEBANK.md) |
| 17 | Outrider | [BG_OUTRIDER.md](./BG_OUTRIDER.md) |
| 18 | Prowler | [BG_PROWLER.md](./BG_PROWLER.md) |
| 19 | Rill Runner | [BG_RILL_RUNNER.md](./BG_RILL_RUNNER.md) |
| 20 | Scrivener | [BG_SCRIVENER.md](./BG_SCRIVENER.md) |

## 3. 模组级资料不混入系统通用目录

Campaign-specific content must remain in its own Campaign directory.

- CAS-1: Trouble in Twin Lakes 官方原文归档：`Campaigns/CA01_Zaf/MODULES/CAS-1/SOURCE/CAS1_OFFICIAL_SOURCE.md`
- CAS-1 GM-only 主持准备：`Campaigns/CA01_Zaf/MODULES/CAS-1/GM_ONLY_PREP.md`
- CAS-1 快速检索索引：`Campaigns/CA01_Zaf/MODULES/CAS-1/REFERENCE_INDEX.md`

模组 NPC、专属怪物数值、事件时序、遭遇表、地点/房间、陷阱、独特 Relics、结局分支与特殊程序均以 Campaign 的官方原文归档及 GM-only Prep 为准。禁止将这些模组事实提升为 Cairn 通用规则，也禁止把 GM-only 内容复制进玩家可见资料。

## 4. 使用规则

1. 遇到具体怪物，先查 Bestiary；若不在目录中，再查 Campaign 模组或其他明确来源。
2. 使用 Spellbook 时，读取法术完整描述；施法成本、Fatigue 和风险处理仍按 Core Rules / Runtime Protocol。
3. 使用 Relic 时，逐项读取使用次数、效果、库存属性和 Recharge 条件。没有写 Recharge 的条目，不代表可以自行设计 Recharge。
4. 角色创建或复核人物卡时，读取对应 Background 的完整表格与能力，核对实际掷骰结果和已锁定结果。
5. NPC Tables 仅提供生成素材；不能代替 NPC 的知识、动机、资源和时间线账本。
6. 模组特殊程序先读模块索引，再读 GM-only Prep 的对应完整章节和官方归档；不得用系统级通用程序覆盖模块明确的特殊规则。
7. 本地快照若与当前官方在线版出现差异，先记录版本差异，再判断当前 Campaign 锁定的规则版本是否需要更新；不得静默覆盖已锁定的战役事实。

## 5. 来源与归属

- Cairn 2e 规则作者：Yochai Gal。
- 出版/项目：Cairn Press。
- 官方项目入口：https://cairnrpg.com/second-edition/
- 官方源仓库：https://github.com/yochaigal/cairn/tree/main/second-edition
- 文本许可：Creative Commons Attribution-ShareAlike 4.0 International（CC BY-SA 4.0）。
