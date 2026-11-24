# 模组与系统登记规范

本文件定义登记职责与归档入口，不维护某一系统的规则摘要、当前战役状态或具体模组清单。

## 系统登记

- 系统清单与唯一资料入口见仓库根目录 [Systems/README.md](../Systems/README.md)。
- 每套正式引入的规则系统必须拥有独立的 已登记的系统入口 README，记录名称、版本、规则权威来源、状态、索引和专属 Skill。
- 候选系统与比较研究见 [Research/SYSTEM_RESEARCH_ROADMAP.md](../Research/SYSTEM_RESEARCH_ROADMAP.md)。候选不代表已学习完成、已采用或已可开团。
- 当前桌面使用哪个系统，以对应 Campaign 的 `SYSTEM_BINDING.md` 为唯一入口；不得以本文件或仓库历史默认值推断。

## 战役登记

- 战役清单见 [Campaigns/README.md](../Campaigns/README.md)。
- 每个 Campaign 必须绑定一个明确的 `system_id` 和规则版本。
- 人物卡、战役 CANON、NPC 索引、模组状态与 Session 记录统一归属该 Campaign。
- 不同系统中的角色移植必须建立独立 Campaign / 角色副本，不覆盖原战役记录。

## 模组登记

- 模组属于 Campaign，不属于通用 GM Training 或系统规则目录。
- 每个模组独立建立文件夹，记录来源、版本、完整性、原文定位、Prep、Runtime State、Session Log、玩家便笺和复盘。
- 模组使用规则、文件结构与权限边界见 [09_MODULE_FOLDER_STANDARD.md](./09_MODULE_FOLDER_STANDARD.md)。
- 具体模组状态只写入对应 Campaign / Module 文件，不在本登记规范中维护副本。

## 维护原则

- 这里登记“资料应该去哪里”，不重复复制资料本身。
- 系统规则与研究不进入 Campaign；战役事实与模组秘密不进入 Systems；通用 GM 能力不复制系统规则。
- 更新登记入口时检查链接，不静默移动或删除权威档案。
