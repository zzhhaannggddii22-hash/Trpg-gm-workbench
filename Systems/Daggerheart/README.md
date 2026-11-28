# Daggerheart /《匕首心》

> system_id: `daggerheart`  
> 规则基线：Daggerheart Core Set（核心规则）  
> 公开参考：Official Daggerheart SRD v2.0（2026-08-25；混合收录 Core Set 与 Hope & Fear 内容）  
> 状态：candidate（独立规则建档中；尚未开放正式运行）

本目录是《匕首心》（Daggerheart）系统级规则资料的唯一入口。它与 Triangle Agency、Cairn、Blades in the Dark 完全隔离。当前阶段只建立基础版规则资料、来源索引与后续运行化入口，不创建 Campaign，不继承其他系统的机制或状态。

本项目的总体方向是：先建立可准确检索、可实际主持的基础规则，再通过短场景验证 GM 的叙事驱动、人物塑造、场景推进与规则结算能力。初版控制内容规模，避免一次性引入所有扩展选项。

## 规则版本与范围

- **默认规则集：Daggerheart Core Set。** 核心规则书、核心角色选项、核心领域、核心装备、核心敌人与环境，以及核心主持规则属于初版研究范围。
- **公开检索基准：官方 SRD v2.0（2026-08-25）。** 它是当前官方公开的规则参考文档，但并非核心规则书替代品，而且同一份 SRD 也纳入了《Daggerheart: Hope & Fear》的扩展条目。
- **扩展默认关闭：Hope & Fear。** 新职业、Dread Domain、转化卡、扩展种族/社群、扩展装备/敌人/环境及扩展战役框架，不进入默认基础规则集。具体边界见 [扩展隔离清单](./Expansions/Hope_and_Fear/README.md)。
- 当 SRD v2.0 条目无法区分来自 Core Set 还是 Hope & Fear 时，先标记 `VERSION_UNRESOLVED`，暂不纳入默认运行；核对官方原书、官方勘误或独立来源后再决定。
- 基础机制因 SRD v2.0 的措辞修订而更新时，可采用最新官方规则文本，但须记录它与 Core Set 印刷文本的差异，不得静默混合。

## 权威来源与中文资料

1. **核心规则权威**：官方 Core Set 规则书及官方 Core Set 勘误。
2. **公开规则参考**：[官方 Daggerheart SRD](https://www.daggerheart.com/srd/)。使用时必须遵守本目录的 Core / Hope & Fear 分类。
3. **官方辅助材料**：[官方 Downloads](https://www.daggerheart.com/downloads/)；其中 Core 与 Hope & Fear 的角色卡、卡牌、主持人速查和其他材料分栏提供。
4. **中文规则检索**：[匕首之心 HTML SRD](https://www.daggerheart.cn/SRD/)，由社区整理公开 SRD 的双语检索入口；用于阅读和定位，版本覆盖与翻译差异仍需核验。
5. **中文主持研究**：[Role Initiative｜匕首之心](https://ttrpg.shinkan42.cn/rule/dagger_heart/)，作为机制解释、角色创建、战斗、敌人与主持指导的二级研究资料；不能替代官方原文。
6. **官方简体中文出版项目**：核心规则书与《希望与恐惧》中文版已完成众筹，项目页显示预计于 2027 年 6 月交付。交付前不把尚未取得的中文版作为可用规则来源。

来源细节、版本说明和许可边界见 [SOURCE_REGISTER.md](./Rule_Reference/SOURCE_REGISTER.md)。

## 目录

- [Rule_Reference/README.md](./Rule_Reference/README.md)：本系统的规则检阅、来源优先级、版本分类与裁定状态。
- [Rule_Reference/SOURCE_REGISTER.md](./Rule_Reference/SOURCE_REGISTER.md)：官方、中文和社区来源登记。
- [Rule_Reference/CORE_RULE_INDEX.md](./Rule_Reference/CORE_RULE_INDEX.md)：基础版规则导航；仅作定位，不替代规范化运行条目。
- [Rule_Reference/GLOSSARY.md](./Rule_Reference/GLOSSARY.md)：中英术语与暂定工作译名。
- [Expansions/Hope_and_Fear/README.md](./Expansions/Hope_and_Fear/README.md)：扩展条目隔离清单；默认不加载。
- 后续研究完成后再建立：`CORE_RULES_RUNTIME.md`、`RUNTIME_PROTOCOL.md`、`GM_SKILL.md`、`PREFLIGHT.md` 与 Candidate 测试资料。

## 运行边界

- 当前状态为 `candidate`。允许研究、检索、规则核对和隔离测试；不得将其当作已激活的正式战役系统。
- 正式 Campaign 必须建立独立 `SYSTEM_BINDING.md`，绑定精确规则版本、采用的勘误、开放/关闭的扩展和桌面适配。
- 所有核心规则、资源、卡牌、敌人、环境和专属术语均属于 Daggerheart；不得借用 Triangle Agency 的 Chaos / QA / Burnout、Cairn 的属性豁免 / Fatigue / 库存程序或 Blades in the Dark 的 Position / Effect / Score 流程。
- 先按玩家意图和虚构情境判断是否需要规则，再调用已核验机制；不要把每个叙事动作都转换为检定。
- 公开仓库只保存自写摘要、索引、定位、术语和合法来源链接；不复制商业规则书、完整中文翻译或付费模组全文。

## 初版建设顺序

1. 核对 Core Set 基础机制与官方勘误，建立核心规则目录。
2. 按触发、输入、程序、状态变化、例外、结算顺序将高频规则规范化。
3. 独立整理角色创建、职业/子职业、领域卡、装备与成长资料；所有内容标注 Core / Hope & Fear。
4. 整理敌人和环境数据的检索方案，优先提高本地检索效率，不在公开仓库镜像未授权全文。
5. 建立轻量 Runtime Protocol 与 Preflight，再进行规则正反例测试和短场景主持测试。
6. 只有基础规则验证稳定后，才评估是否启用 Hope & Fear 或引入其他扩展内容。
