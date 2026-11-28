# Rule Reference｜规则索引

本目录用于在跑团时直接检索 WWN。优先调用本地摘要和 Data 离线规则数据，避免运行时搜索网页。

## 资料优先级

1. 用户提供或已核验的目标版本官方规则书（Free Edition / Deluxe）：完整说明、例外、示例与页码。
2. 作者发布的 SRD 1.0：仅限明确覆盖的规则机制。SRD 是设计者参考文档，不是完整玩家手册或 GM 工具集。
3. 出版方勘误、补充说明和正式产品资料。
4. 第三方转录/结构化数据：检索辅助，争议规则回到来源文本。
5. 本项目中文摘要：快速运行入口，不覆盖原文。

## 本地入口

- [CORE_RUNTIME_GUIDE.md](./CORE_RUNTIME_GUIDE.md)：检定、战斗、伤势、旅行、探索、NPC 和成长。
- [FACTIONS_AND_MAJOR_PROJECTS.md](./FACTIONS_AND_MAJOR_PROJECTS.md)：Faction Turn、资产行动和重大计划。
- [GM_TOOLKIT_RESEARCH.md](./GM_TOOLKIT_RESEARCH.md)：官方 GM 工具范围、许可边界和研究缺口。
- [Data/README.md](./Data/README.md)：离线规则数据包说明。
- [Data/SRD.md](./Data/SRD.md)：SRD 1.0 原文。
- [Data/wwn-srd-data.jsonld](./Data/wwn-srd-data.jsonld)：完整 JSON-LD 数据图。
- [Data/catalog.json](./Data/catalog.json)：名称、类型和来源定位目录。
- [Data/search-index.json](./Data/search-index.json)：本地全文倒排索引。

## 模块状态

| 模块 | 状态 | 内容 |
|---|---|---|
| 角色创建 | SRD 数据已纳入 | 属性、技能、背景、职业、Foci、成长 |
| 核心判定 | 摘要已完成 | 检定、四类豁免、对抗和协助 |
| 战斗与伤害 | 摘要已完成 | 先攻、行动、攻击、Shock、濒死与恢复 |
| 旅行与探索 | 摘要已完成 | 旅行、远征补给、Hex、地下城 Turn |
| 装备与经济 | 数据已纳入 | 装备、武器、护甲、服务、雇员和表格 |
| 魔法 | 数据已纳入 | 职业能力、法术、Arts、施法机制 |
| 怪物与 NPC | 数据已纳入 | Foe、Reaction、Morale、Instinct |
| 阵营 | 摘要与数据已纳入 | 属性、资产、标签、行动和目标 |
| Major Projects | 摘要与数据已纳入 | Renown、难度、范围、对抗和协助 |
| GM 沙盒工具 | 部分研究 | 官方确认工具类别；完整生成表/标签正文待核验 |

## 调用约定

普通行动直接读取 CORE_RUNTIME_GUIDE；涉及法术、职业、装备、敌人时按本地数据定位；只有阵营结算或跨区域长期目标触发时才读取阵营手册。完整规则书的解释、例外和页码仍待取得 Free Edition / Deluxe 后核验。SRD 中未出现的规则不得从其他系统推断。
