# Daggerheart 来源登记

> 建档日期：2026-11-28  
> 默认规则集：Core Set  
> 核验策略：官方来源裁定规则；中文与社区资料提高检索效率。

## A. 官方规则来源

### A1. Official Daggerheart SRD v2.0

- URL: https://www.daggerheart.com/srd/
- 发布/修订日期：2026-08-25。
- 定位：官方公开系统参考文档，覆盖核心机制、角色创建、骰子系统及可供 Daggerheart Compatible 创作使用的规则与内容。
- 重要版本边界：SRD v2.0 的官方 Changelog 明确说明，它新增了 Core Set 与 Hope & Fear 两套产品中的战役框架机制，并纳入 Hope & Fear 的 Dread Domain、敌人、环境、种族、社群、战利品、装备、四个职业及转化内容。
- 用法：可作为公开规则检索、术语和规则措辞的主要入口；必须依据原书来源拆分 Core / Hope & Fear。SRD v2.0 不是核心规则书的完整替代品。

### A2. Daggerheart Core Set / Core Rulebook

- 官方入口：https://www.daggerheart.com/buy/
- 定位：基础规则集的主要权威来源。角色创建、完整规则说明、示例、世界设定和主持建议以核心规则书及官方勘误为准。
- 当前状态：已登记为最高优先级来源；尚未取得并逐章核验完整规则书及实物卡牌资料。
- 规则版本更新时，记录印刷文本、SRD 及勘误之间的差异，不静默合并。

### A3. Official Downloads

- URL: https://www.daggerheart.com/downloads/
- Core 资料：快速入门冒险、角色卡与指南、角色创建辅助表、GM Guide、核心战役框架材料、核心卡牌打印文件、空白地图、Core Errata。
- Hope & Fear 资料：扩展职业辅助表、扩展角色卡/指南、扩展卡牌、扩展战役框架材料与 Hope & Fear Errata。
- 用法：按官方页面的 Core / Hope & Fear 分区存取；初版只整理 Core 部分。

### A4. Daggerheart: Hope & Fear

- 官方介绍：https://www.daggerheart.com/daggerheart-hope-fear-is-now-available/
- 官方扩展，独立于 Core Set。扩展含四个职业（Assassin、Brawler、Warlock、Witch）、新子职业、Dread Domain、转化卡、扩展种族/社群、敌人、环境、装备与战役框架。
- 本工程默认不启用。详细隔离项目见 `../Expansions/Hope_and_Fear/README.md`。

## B. 中文规则与辅助资料

### B1. 匕首之心 HTML SRD

- URL: https://www.daggerheart.cn/SRD/
- 定位：社区翻译组维护的公开 SRD 双语 HTML 检索站；可浏览章节、搜索正文、查敌人和环境资料。
- 优点：便于中文阅读、逐条定位和交叉比较英文原文。
- 版本注意：页面收录了可识别的 Hope & Fear 新内容；具体页面是否已完整同步 SRD v2.0、每项数据来自 Core 还是扩展，仍须逐项核对。不得把站点收录范围等同于 Core Set。
- 用法：作为中文阅读入口与检索镜像，不作为版本归属不明时的最终证据。

### B2. Role Initiative｜匕首之心

- URL: https://ttrpg.shinkan42.cn/rule/dagger_heart/
- 车卡指南：https://ttrpg.shinkan42.cn/rule/dagger_heart/guide/character_creation.html
- 基础规则说明：https://ttrpg.shinkan42.cn/rule/dagger_heart/guide/general_rule.html
- 战斗规则：https://ttrpg.shinkan42.cn/rule/dagger_heart/guide/combat.html
- 领域索引：https://ttrpg.shinkan42.cn/rule/dagger_heart/brief_ref/domain.html
- 敌人设计研究：https://ttrpg.shinkan42.cn/rule/dagger_heart/brief_ref/adversary_design.html
- 定位：中文规则讲解、主持研究与机制设计资料。部分页面明确区分核心内容和 Hope & Fear 扩展，并标注依据为官方 SRD 2.0。
- 用法：适合梳理流程、寻找规则边界和建立主持知识；遇到精确数值、成本、触发条件、例外或冲突，回到官方规则原文核验。

### B3. 灰机 Wiki

- 定位：中文社区百科和补充索引。
- 用法：作为术语、条目与历史翻译的辅助搜索源；页面版本和完备度不统一，未经核验的内容不进入 VERIFIED 规则。

## C. 官方简体中文版出版状态

- 项目页：https://zhongchou.modian.com/item/159038.html
- 出版方/项目方：三局两胜工作室（BO3 Studio）。
- 项目内容：核心规则书简体中文版，以及独立的《匕首心：希望与恐惧》扩展中文版；两者分别提供书籍和电子文档回报选项。
- 当前记录：众筹已成功结束；项目页面显示预计回报发放时间为 2027 年 6 月内。
- 使用限制：截至本次建档日（2026-11-28），不能将尚未交付的官方中文版当作已可取得的规则文本。交付后优先用于确认官方中文术语、卡牌翻译和规则措辞，再更新本目录。

## D. 来源分类与更新规则

每条规则的来源字段使用以下值之一或组合：

- `CORE_SOURCE`
- `CORE_ERRATA`
- `SRD_CORE_CLARIFICATION`
- `HOPE_AND_FEAR`
- `CAMPAIGN_FRAME`
- `TABLE_ADAPTATION`
- `GM_INFERENCE`
- `VERSION_UNRESOLVED`
- `DISPUTED`

每次引用来源时记录 URL、具体章节/页码或卡牌名称、规则版本、核对日期。中文资料与官方英文资料冲突时，先判断是不是翻译差异或版本混用，再按官方来源处理；不能只改中文术语而不保留对应原文名称。
