# 参考数据目录

> 规则工作区：`system_id: daggerheart`。  
> 默认加载：`Core_Set/`。  
> 扩展：`Hope_and_Fear/`，默认关闭。  
> 其他：`Mixed_Version/` 与 `Optional_Procedures/` 不自动进入默认规则集。

## Core Set 数据

| 文件 | 数量 | 说明 |
|---|---:|---|
| `Core_Set/classes.json` | 9 | 核心职业完整结构 |
| `Core_Set/subclasses.json` | 18 | 核心职业的两个子职业 |
| `Core_Set/domains.json` | 9 | 九个核心领域 |
| `Core_Set/domain_cards.json` | 189 | 核心领域卡 |
| `Core_Set/ancestries.json` | 18 | 核心种族选项 |
| `Core_Set/communities.json` | 9 | 核心社群 |
| `Core_Set/beastforms.json` | 24 | 核心 Beastform 数据 |
| `Core_Set/adversaries.json` | 129 | 核心敌人 Stat Blocks |
| `Core_Set/environments.json` | 19 | 核心环境 Stat Blocks |
| `Core_Set/weapons.json` | 183 | 核心武器 |
| `Core_Set/armor.json` | 34 | 核心护甲 |
| `Core_Set/items.json` | 60 | Core Set 物品表 |
| `Core_Set/consumables.json` | 60 | Core Set 消耗品表 |
| `Core_Set/core_rules.json` | 12 | 已确认可独立作为核心规则条目的章节 |

## Hope & Fear 数据（默认关闭）

| 文件 | 数量 |
|---|---:|
| `Hope_and_Fear/classes.json` | 4 |
| `Hope_and_Fear/subclasses.json` | 8 |
| `Hope_and_Fear/domains.json` | 1 |
| `Hope_and_Fear/domain_cards.json` | 21 |
| `Hope_and_Fear/ancestries.json` | 7 |
| `Hope_and_Fear/communities.json` | 6 |
| `Hope_and_Fear/adversaries.json` | 135 |
| `Hope_and_Fear/environments.json` | 28 |
| `Hope_and_Fear/weapons.json` | 132 |
| `Hope_and_Fear/armor.json` | 35 |
| `Hope_and_Fear/items.json` | 60 |
| `Hope_and_Fear/consumables.json` | 60 |
| `Hope_and_Fear/transformations.json` | 6 |
| `Hope_and_Fear/transformation_rules.json` | 1 |

## 不自动加载的数据

- `Mixed_Version/mixed_rule_sections.json`：Character Creation、Classes、Domains 三段来自 SRD 2.0 的混合版本说明，其中选项清单同时列出 Core 与 Hope & Fear。为避免把扩展职业、Dread Domain 等误纳入基础选项，整段隔离；具体基础选项已在 Core_Set 分类数据中分离。
- `Optional_Procedures/supplemental_campaign_mechanics.json`：SRD 中的可选战役机制汇总。它们是可按 Campaign 需要加载的可选规则，不是默认基础玩法。
- 不导入 `campaign_frames/`：Campaign Frame 的完整文本、地图和专有设定不属于普通 SRD 规则数据的自由分发范围。

## 数据结构

JSON 结构沿用 SRD 2.0 结构化导出字段，尽量保留原始键名，方便与官方英文术语及源文件交叉核对。常见类别：

- 职业：`name`、`domain_1`、`domain_2`、`evasion`、`hp`、`feature`、`items`、`hope_feature_*`
- 子职业：`name`、`spellcast_trait`、`foundation`、`specialization`、`mastery`
- 领域卡：`name`、`domain`、`level`、`recall`、`type`、`text`
- 敌人：`name`、`tier`、`type`、`difficulty`、`hp`、`stress`、`thresholds`、`atk`、`attack`、`damage`、`feature`
- 环境：`name`、`tier`、`type`、`difficulty`、`description`、`impulses`、`potential_adversaries`、`feature`
- 装备：名称、Tier、武器属性/伤害/范围/负担，或护甲阈值与 Armor Score；物品与消耗品保留表格 roll 值。

## 常用检索索引

- [敌人检索索引](../Rule_Reference/ADVERSARY_INDEX.md)
- [环境检索索引](../Rule_Reference/ENVIRONMENT_INDEX.md)
- [核心角色选项索引](../Rule_Reference/CHARACTER_OPTIONS_INDEX.md)
- [常用规则速查表](../Rule_Reference/LOOKUP_TABLES.md)
- [核心运行手册](../Rule_Reference/CORE_RULES_RUNTIME.md)

数据文件是本地检索副本；对版本归属不明、数据抽取错误、官方勘误或能力文本冲突，应回查本目录的来源登记和官方 SRD。
