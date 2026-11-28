# 《匕首心》规则项目

> system_id: `daggerheart`  
> 标识：Daggerheart™ Compatible（非官方个人研究工作台）  
> 规则基线：Daggerheart Core Set  
> 公开参考：Official Daggerheart SRD v2.0（2026-08-25；混合收录 Core Set 与 Hope & Fear 内容）  
> 状态：candidate（64项规则与GM专项已完成桌面逻辑模拟；42项参考执行器自动化测试通过；生产Runtime与实际短场景仍未验收）

本目录是《匕首心》系统级规则资料的唯一入口。与 Triangle Agency、Cairn、Blades in the Dark 完全隔离。当前阶段以基础版 Core Set 为默认规则集，先建立可准确检索、可直接主持的本地规则和数据资料，再通过短场景验证。初版控制复杂度，不默认引入 Hope & Fear。

## 规则版本与范围

- **默认规则集：Daggerheart Core Set。** 核心角色选项、九大领域、核心装备、敌人/环境和核心 GM 规则属于默认范围。
- **公开检索基准：官方 SRD v2.0（2026-08-25）。** 官方将 SRD 2.0 纳入 DPCGL 2.0 Public Game Content，但它同时收录 Core Set 与 Hope & Fear 内容；不能将整个 SRD 直接视作纯基础版。
- **扩展默认关闭：Hope & Fear。** 四个新职业、Dread Domain、转化、扩展种族/社群/装备/敌人/环境均单独存放。只有用户明确启用或 Campaign Binding 指定时才加载。
- **混合章节隔离。** SRD 2.0 的 Character Creation、Classes、Domains 章节列出 Core 与扩展选项，整段单独存档；默认 Core 数据库不加载它们。
- **可选战役程序隔离。** Supplemental Campaign Mechanics 单独保存，不默认纳入常规流程。
- 条目来源无法区分时标记 `VERSION_UNRESOLVED`，不擅自进入默认运行。
- SRD 2.0 对基础规则的措辞修订可以采用，但要记录与 Core Set 印刷文本、官方勘误之间的差异。

## 权威来源与中文资料

1. **最高规则来源**：官方 Core Set 规则书及官方 Core Errata。用户未来提供合法取得的规则书时，用于补齐 SRD 未覆盖内容。
2. **公开规则参考**：[官方 SRD 2.0](https://www.daggerheart.com/srd/)。它属于 DPCGL 2.0 明确列出的 Public Game Content，可按许可条件使用。
3. **官方辅助材料**：[官方 Downloads](https://www.daggerheart.com/downloads/)，其中 Core 与 Hope & Fear 的角色卡、卡牌、GM Guide、地图材料和勘误分栏。
4. **中文检索**：[匕首之心 HTML SRD](https://www.daggerheart.cn/SRD/)，用于中文阅读与定位，版本覆盖和翻译差异需核对。
5. **中文主持研究**：[Role Initiative｜匕首之心](https://ttrpg.shinkan42.cn/rule/dagger_heart/)，用于机制解释、角色创建、战斗、敌人与主持方法研究；不替代官方原文。
6. **官方简体中文版**：核心规则书与《希望与恐惧》中文版项目已完成众筹；众筹项目页曾公布预计 2027 年 6 月交付；但官方 2026-07-30 的 Daggerheart Next 更新将简体中文版 Core Set 与 Hope & Fear 标为 Q4 2026。两个公开时间点不一致，当前应视为待确认的出版计划，不以任一日期保证实际到货。交付前不将未取得的中文版作为规则来源。

来源、许可和版本详情见 [SOURCE_REGISTER.md](./Rule_Reference/SOURCE_REGISTER.md) 与 [数据许可说明](./Reference_Data/LICENSE_AND_ATTRIBUTION.md)。

## 快速入口

- [规则检阅协议](./Rule_Reference/README.md)：来源优先级、规则分类、缺口处理。
- [核心规则索引](./Rule_Reference/CORE_RULE_INDEX.md)：Rule Area 与 Rule ID 导航。
- [核心规则运行手册](./Rule_Reference/CORE_RULES_RUNTIME.md)：已规范化的高频核心机制，可按触发直接调用。
- [专属 GM Skill](./GM_SKILL.md)：Core Set 主持原则、场景节奏、GM Move、Fear、NPC 与战斗准备。
- [GM 运行专题：Hope / Fear、GM Moves 与 Spotlight](./GM_RUNTIME_FIELD_GUIDE.md)：细化骰子结果、聚焦转移、GM Move 严重度、Fear 收支、敌人 Spotlight 和运行测试。
- [GM 设计专题：后果选择、战斗叙事与敌人行为](./GM_DESIGN_FIELD_GUIDE.md)：后果选择、战斗节奏、敌人动机与类型、环境使用、敌人设计及轻量备团方法。
- [单人 PC 适配研究](./Rule_Reference/SINGLE_PC_ADAPTATION_RESEARCH.md)：仅在 1 PC Campaign 中使用的非默认桌面适配边界与测试计划。
- [常用规则检索表](./Rule_Reference/LOOKUP_TABLES.md)：六属性难度基准、敌人/环境 Tier、遭遇 BP、范围、休息和 Fear 预算。
- [二元骰概率与行动经济研究](./Rule_Reference/DICE_PROBABILITY_AND_ACTION_ECONOMY.md)：144 种基础骰面枚举、成功率、Hope/Fear 分布与 GM Spotlight 转移率。
- [核心角色选项索引](./Rule_Reference/CHARACTER_OPTIONS_INDEX.md)：九职业、领域和子职业导航。
- [领域卡索引](./Rule_Reference/DOMAIN_CARD_INDEX.md)：189 张 Core 领域卡按 Domain / Level 检索。
- [武器索引](./Rule_Reference/WEAPON_INDEX.md)：183 件 Core 武器按 Tier / Primary / Secondary 检索。
- [护甲索引](./Rule_Reference/ARMOR_INDEX.md)：34 件 Core 护甲的阈值与 Armor Score。
- [物品与消耗品索引](./Rule_Reference/LOOT_INDEX.md)：Core 物品与消耗品 d12 表格检索。
- [Beastform 索引](./Rule_Reference/BEASTFORM_INDEX.md)：24 种 Core Beastform 检索。
- [敌人检索索引](./Rule_Reference/ADVERSARY_INDEX.md)：按 Tier 检索 Core 敌人。
- [环境检索索引](./Rule_Reference/ENVIRONMENT_INDEX.md)：按 Tier 检索 Core 环境。
- [装备检索索引](./Rule_Reference/GEAR_INDEX.md)：Core 武器、护甲、物品与消耗品。
- [本地优先检索协议](./Rule_Reference/LOCAL_FIRST_RETRIEVAL.md)：运行时如何先查本地资料。
- [结构化规则与检索数据](./Reference_Data/README.md)：Core 与 Hope & Fear 分开的 JSON 数据集合。
- [规则来源登记](./Rule_Reference/SOURCE_REGISTER.md)：官方、中文和社区资料。
- [规则疑点登记](./Rule_Reference/RULE_ISSUES.md)：来源差异、版本疑点和未解决问题。
- [Core Errata 交叉核验](./Rule_Reference/ERRATA_CROSSCHECK.md)：旧版官方勘误与 SRD 2.0 当前条目逐项抽样对照。
- [Preflight](./PREFLIGHT.md)：Campaign / Session 开始前核验。
- [回归测试矩阵](./Testing/CORE_RULE_RUNTIME_REGRESSION.md)：64 项规则与 GM 专项已完成桌面逻辑模拟（非程序自动测试）；42 项参考执行器测试为代码自动化。详见 [GM 专项桌面模拟记录](./Testing/GM_DESK_SIMULATION_01.md)。实际短场景和外部盲测仍待验证。
- [术语表](./Rule_Reference/GLOSSARY.md)：中英术语与暂定工作译名。
- [Hope & Fear 扩展隔离清单](./Expansions/Hope_and_Fear/README.md)：扩展默认关闭及启用条件。

## 本地优先规则

日常主持不应每次联网检索。默认顺序：

1. 确认 Campaign Binding / 规则版本 / 扩展范围。
2. 查本地 Rule ID 与 `CORE_RULES_RUNTIME.md`。
3. 查 `LOOKUP_TABLES.md` 与 `Reference_Data/Core_Set/` 的 JSON。
4. 本地数据不足或遇到来源冲突，再读取 SRD 对应章节或官方勘误。
5. 核验结论写回本地运行手册、数据索引或 RULE_ISSUES。

公开仓库保存已授权的 SRD 2.0 Public Game Content 结构化数据、自写摘要、索引与运行协议；不收录商业 Core Rulebook 未公开的精确正文、Campaign Frame 全文/地图、艺术插画或未获许可的模组。私人仓库用于保存个人研究与用户合法提供的原始材料索引；私人仓库本身不改变版权许可。

## 运行边界

- 当前状态为 `candidate`。允许研究、检索、规则核对和隔离测试；不代表已完成正式 Campaign 接入。
- 正式 Campaign 必须建立独立 `SYSTEM_BINDING.md`，绑定精确规则版本、官方勘误、扩展范围和桌面适配。
- 不借用 Triangle Agency 的 Chaos / QA / Burnout、Cairn 的豁免 / Fatigue / 库存程序或 Blades in the Dark 的 Position / Effect / Score 流程。
- 已核验规则从本地调用；未知规则标记并定向回查，不冻结无关互动。
- 叙事节奏优先：将复杂动作合并处理，减少无意义确认；规则步骤仍须正确结算。

## 初版建设状态

已完成：来源与许可登记、Core / Hope & Fear 数据拆分、规则索引、核心运行手册、常用难度与遭遇检索表、敌人/环境索引、译名表、版本差异登记、Errata 抽样核验、GM Skill、Preflight 草案、64 项规则/GM 桌面逻辑模拟、42 项参考执行器自动化测试，以及 GM 专题与二元骰概率研究。

待完成：穷尽核对官方 Core Errata、取得合法核心规则书后补齐 SRD 未覆盖的 GM 指导与示例、执行规则正反例回归、Blind GM 测试和短场景实测。