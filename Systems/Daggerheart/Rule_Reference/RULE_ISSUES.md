# 规则来源与版本问题登记

> 建立日期：2026-11-28  
> 范围：Daggerheart Core Set；SRD 2.0 为公开检索基础。  
> 状态：持续更新。未解决问题不得静默当成规则事实。

## DH-I-001｜SRD 2.0 同时收录 Core Set 与 Hope & Fear

- 状态：PARTIALLY_RESOLVED
- 影响：SRD 2.0 不是纯 Core Set 数据集。它同时包含扩展职业、Dread Domain、敌人、环境、种族、社群、装备、战利品与 Transformations。
- 处理：结构化数据按 Core_Set / Hope_and_Fear 分库；默认只加载 Core_Set。
- 剩余：部分通用章节列出混合选项，已整体隔离到 Mixed_Version。

## DH-I-002｜Core 与 Hope & Fear 条目分类

- 状态：SOURCE_SPLIT_CREATED
- Core Set 数据量：9 职业、18 子职业、9 领域、189 领域卡、18 种族、9 社群、24 Beastforms、129 敌人、19 环境、183 武器、34 护甲、60 物品、60 消耗品。
- Hope & Fear 数据量：4 职业、8 子职业、Dread 领域、21 Dread 卡、7 条种族数据记录（其中 Elemental Kin 是父级介绍，实际新增可选种族 6 个）、6 社群、135 敌人、28 环境、132 武器、35 护甲、60 物品、60 消耗品、6 种 Transformations。
- 依据：与旧 SRD 1.0 的结构化类别数据逐项比较，并对照 SRD 2.0 官方 Changelog 与 Core / Hope & Fear 官方 Downloads 分类。
- 处理：拆分方式与限制见 [VERSION_SPLIT_METHOD.md](../Reference_Data/VERSION_SPLIT_METHOD.md) 和 [DATASET_MANIFEST.json](../Reference_Data/DATASET_MANIFEST.json)。
- 注意：本次分类是工程来源划分，不替代对每个印刷卡牌/规则勘误的最终核验。

## DH-I-003｜Character Creation / Classes / Domains 属于混合版本章节

- 状态：ISOLATED
- 情况：SRD 2.0 的三个章节在同一段文本中列出 Core 与 Hope & Fear 的职业、领域、种族等选项。直接放入 Core 数据将导致扩展选项误加载。
- 处理：三段原始章节整体移至 `Reference_Data/Mixed_Version/mixed_rule_sections.json`。基础选项由分类 JSON 和核心角色索引提供。
- 规则运行时：不自动加载 Mixed_Version。

## DH-I-004｜Supplemental Campaign Mechanics 不属于默认基础流程

- 状态：SEPARATED
- 内容：可选战役机制章节包括 Faction Tracking、Feasts、Everyday Hero 起始装备，以及 Grimdark、Tech-based、Western、Colossal Adversaries、Floating Magic School、Fairy Tale、Monster Hunting、Hex Crawl 等可选程序。
- 处理：单独存放于 `Reference_Data/Optional_Procedures/supplemental_campaign_mechanics.json`；默认不加载。
- 注意：其中某些程序可能适用于特定 Campaign，但需先由用户选择并单独核验。

## DH-I-005｜Campaign Frames 的许可边界

- 状态：EXCLUDED
- 依据：DPCGL 2.0 将 SRD 2.0 列为 Public Game Content，但 Campaign Frame 的完整文本、地图及专有设定另受分享限制；除实际游玩内容外，不得以普通资料格式重新发布或改编成新文字作品，除非另有书面许可。
- 处理：不导入 SRD 数据仓库中的 `campaign_frames/` 文件，不复制官方地图或 Campaign Frame 正文。仅记录官方入口和一般机制摘要。
- 来源：官方 DPCGL 2.0 §1.9.3、§2.1；详见 [LICENSE_AND_ATTRIBUTION.md](../Reference_Data/LICENSE_AND_ATTRIBUTION.md)。

## DH-I-006｜旧版 SRD 1.0 的九件武器未出现在 SRD 2.0 当前武器数据中

- 状态：VERSION_CHANGE_RECORDED
- 情况：对比旧版结构化数据，旧版武器表中有 9 个条目没有出现在 SRD 2.0 的武器表。
- 名称：Axe of Fortunis、Blessed Anlace、Ghostblade、Runes of Ruination、Widogast Pendant、Gilded Bow、Firestaff、Mage Orb、Ilmari's Rifle。
- 处理：不把旧版条目自动恢复到当前 Core 数据。待核实这是 SRD 修订删除、迁移到其他内容、印刷规则书独有内容还是数据抽取差异。

## DH-I-007｜Adversary 名称调整与别名

- 状态：NORMALIZED_WITH_ALIAS
- 六个旧版名称与 SRD 2.0 名称不同：
  - Fallen Warlord: Realm-Breaker → Realm-Breaker
  - Fallen Warlord: Undefeated Champion → Undefeated Champion
  - Outer Realms Corruptor → Outer Realms Corrupter
  - Volcanic Dragon: Obsidian Predator → Obsidian Predator
  - Volcanic Dragon: Molten Scourge → Molten Scourge
  - Volcanic Dragon: Ashen Tyrant → Ashen Tyrant
- 处理：数据采用 SRD 2.0 当前名称；今后检索旧备团笔记时可使用别名映射。

## DH-I-008｜中文译名尚未冻结

- 状态：OPEN
- 影响：中文 HTML SRD、Role Initiative、灰机 Wiki 之间可能使用不同译名；官方简体中文版尚未交付。
- 处理：英文原词是稳定检索键；当前中文仅作工作译名。官方简体中文版交付后统一复核，不静默覆盖历史译名。

## DH-I-009｜SRD 2.0 与完整 Core Rulebook 的覆盖差异

- 状态：OPEN
- 影响：SRD 是公开规则参考，但不包含核心规则书中所有完整解释、实例、叙事指导、插图、地图或专有内容。
- 处理：本工程以 SRD 2.0 建立高频规则运行基础；对 SRD 未覆盖的部分保留官方书籍章节定位。用户合法取得并提供核心规则书后，再补充私人研究笔记与定位。
- 版权处理：不从网络复制商业核心规则书全文。私人仓库可保存用户合法提供的个人资料及自写研究记录，但私人仓库本身不改变版权许可。

## DH-I-010｜Core Errata 与 SRD 2.0 的逐项对应

- 状态：PARTIALLY_RESOLVED
- 来源：官方 Core Errata（2025-09-09）https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-Errata-September9th2025.pdf；官方 SRD 2.0 Changelog 声明其修正拼写并落实勘误；SRD 2.0 PDF：https://www.daggerheart.com/wp-content/uploads/2026/08/DH_SRD_2_2026_08_25.pdf。
- 已抽样核对并在 SRD 2.0 数据中找到对应修正：Powerful Beast 的 Strength +3 / Evasion +1；Spear / Longsword / Glowing Rings 的核心武器数据；Sweet Moss；Glass Snake 的 Armor-Shredding Shards；Adult Flickerfly 的 Hallucinatory Breath 标为 Reaction；Battle Box 的 Relentless (2)；Whirlwind、I See It Coming、Splintering Strike、Book of Grynn 等领域卡。
- Sledgehammer 的 Massive 特性（−1 Evasion）存在于 SRD 2.0 的 Optional Supplemental Campaign Mechanics / Everyday Hero Starting Equipment，不属于默认 Core 武器清单；本工程将该章节隔离，不能将其误当成默认起始装备。
- **仍有术语差异：** 2025 Core Errata 对 Buckler 的 Deflecting 特性使用“available Armor Slots”；SRD 2.0 现行 PDF 和结构化数据写作“available Armor Score”。当前 Core 运行库遵循较新的 SRD 2.0 文本，保留此差异供未来印刷书/新版勘误核对，不擅自替换。
- 2025 Errata 还包括 Core Rulebook 的若干完整书籍示例与不在当前公开结构化数据集中的内容；SRD 2.0 没有逐项暴露的内容仍需保留缺口。
- 处理：已将抽样校验记录放入 [ERRATA_CROSSCHECK.md](./ERRATA_CROSSCHECK.md)。未来若官方更新 Errata 或 Core Rulebook 勘误，继续逐项对照并记录版本，不因 SRD 2.0 Changelog 有“implemented errata”一句就关闭所有差异。

## DH-I-011｜结构化导出源存在第三方格式整理

- 状态：DOCUMENTED
- 来源：JHerrin00/daggerheart-srd-2.0 将官方 SRD 2.0 转为 Markdown / JSON，修正抽取格式并对部分条目做整理。
- 风险：结构化文件不是官方原生数据库；可能存在格式转换、拼写修正、命名调整或字段结构差异。
- 处理：所有高影响数值、规则顺序、特殊能力和用户质疑条目回到官方 SRD 原文/官方 Errata；数据源与修改说明见 [LICENSE_AND_ATTRIBUTION.md](../Reference_Data/LICENSE_AND_ATTRIBUTION.md)。

## DH-I-012｜官方简体中文版待交付

- 状态：PENDING_PUBLICATION
- 记录：官方授权简体中文 Core Set 与 Hope & Fear 项目已完成众筹。众筹项目页曾公布 2027 年 6 月交付；官方 Daggerheart Next 页面（2026-07-30）另标为 Q4 2026。两处时间不一致，需以后续履约通知确认。
- 处理：交付后统一术语、角色选项、领域卡、敌人/环境、卡牌名称与勘误记录；此前译名保持临时状态。

## 后续处理优先级

1. Core Errata 逐项核验。
2. 核心规则运行手册正反例与边界回归。
3. 结构化 JSON 与官方 SRD / 卡牌数据抽样核验。
4. 用户提供的合法核心规则书资料入库后，补充 GM 指导、示例与 SRD 未覆盖细节。
5. 完成 Preflight 与短场景实测。


## DH-I-013｜Elemental Kin 是种族家族总述，不是额外可选种族

- 状态：CLARIFIED
- 证据：SRD 2.0 `ancestries.json` 中 Elemental Kin 记录没有 Ancestry Feature；角色创建可选种族列表列出 Earthkin、Emberkin、Skykin、Tidekin，而不列 Elemental Kin。
- 处理：保留 Elemental Kin 总述数据，便于理解四种元素血统；角色创建可选项仅计四种变体。扩展实际新增可选种族为 Aetheris、Gnome、Earthkin、Emberkin、Skykin、Tidekin，共 6 个。
- 统计口径：Hope & Fear ancestry JSON 为 7 条记录，但实际可选 Ancestry 是 6 个；Core 18 + 扩展 6 = 24。


## DH-I-014｜2025 Buckler Errata 与 SRD 2.0 当前术语不同

- 状态：DOCUMENTED_DIFFERENCE
- 2025-09-09 Core Errata 将 Buckler 的 Deflecting 写为 “available Armor Slots”；2026-08-25 SRD 2.0 PDF 和结构化 JSON 写为 “available Armor Score”。
- 处理：当前运行依较新的 SRD 2.0 文本；不将旧 PDF 的措辞直接覆盖到公开数据。未来取得 Core Rulebook/最新勘误后核验是否为有意改词或印刷书版本差异。

## DH-I-015｜部分 Errata 对象属于可选程序或书本特有内容

- 状态：PARTIALLY_MAPPED
- Sledgehammer 的 Massive 特性是 Everyday Hero Starting Equipment 可选武器表的一部分，而不是标准 Core Tier 1 Weapon Tables。SRD 2.0 将其收录在 Supplemental Campaign Mechanics；公开数据单独隔离，默认不加载。
- 其他不在 SRD 2.0 Core 数据表的 Errata 对象，不能因此推断缺失或失效；可能来自完整 Core Rulebook 示例、Campaign Frame 或未导入的可选章节。需要根据页码和章节归属逐项判断。

## DH-I-016｜Buckler 的网页 Changelog 与 SRD 2.0 PDF 用语冲突

- 状态：DOCUMENTED_SOURCE_CONFLICT / LOCAL_DATA_ALIGNED_TO_PDF
- 2025 Core Errata 与官方 SRD 网页 Changelog 的条目使用 “available Armor Slots”。
- 2026-08-25 官方 SRD 2.0 PDF 第 67 页当前 Buckler 卡面则写作 “available Armor Score”。
- 第三方结构化 JSON 原先也采用 “available Armor Score”；本地曾根据网页 Changelog 将其改成 “available Armor Slots”，这一步不符合本项目当前“SRD 2.0 PDF 为运行基准”的版本选择。
- 处理：本地 Core_Set/weapons.json 已恢复为官方 SRD 2.0 PDF 的 “available Armor Score”。保留两种官方来源文本差异，不把 Changelog 引文误标为 PDF 正文。
- 规则影响：该加值究竟按 Armor Score 总值还是未标记 Armor Slots 计算，可能影响 Buckler 的防御结算；当前运行按 PDF 文本执行，遇到争议时标记 DISPUTED，不自行改写。


## DH-I-017｜SRD 2.0 已整合的 Core 机械修正抽样核验

- 状态：SAMPLE_CHECKED
- 官方 SRD 2.0 Changelog 明确记载：Core 规则的若干机械修正已实施；本轮与本地数据完成以下抽样对照：
  - Powerful Beast：Strength +3、Evasion +1，结构化数据正确。
  - Adult Flickerfly：Hallucinatory Breath 已是 Reaction，结构化数据正确。
  - Spear / Longsword：Tier 1–4 伤害修正按 SRD Changelog 记录，数据正确。
  - Glowing Rings：Tier 1 伤害为 d10+2，数据正确。
  - Splintering Strike：已采用 SRD 2.0 的多目标伤害分配文本，数据正确。
  - Buckler：第三方 JSON 曾误写 available Armor Score；已修正为 available Armor Slots。
- 结论：SRD 2.0 是本地数据更新基准，但第三方结构化导出仍可能有个别字段错误。继续按高影响条目抽样回查；不要将抽样结果表述为完整勘误验收。


## DH-I-018｜GM 起始 Fear 的公开来源尚未定位

- 状态：SOURCE_UNVERIFIED
- 当前运行笔记曾记录“Campaign 开始时 GM 获得每名 PC 1 Fear”。
- 核验结果：在当前官方 SRD 2.0 的 Fear 章节与可检索全文中，已确认 GM 可从玩家掷出 Fear、休息及能力效果获得 Fear；Short Rest 获得 1d4，Long Rest 获得 1d4 + PC 数量，Fear 上限为 12。尚未定位到 Campaign 初始化时“每名 PC 1 Fear”的公开 SRD 条文。
- 处理：核心运行手册已将该项降级为待核来源，不再将其标记为 SRD 2.0 已核实。正式 Campaign 开始前，应对照合法取得的完整 Core Rulebook 或明确的官方勘误/指导确认；在来源未确认前，不自动据此加值。
- 证据边界：这是“当前公开 SRD 未定位到”的检索结论，不等同于证明完整 Core Rulebook 不存在该规则。
