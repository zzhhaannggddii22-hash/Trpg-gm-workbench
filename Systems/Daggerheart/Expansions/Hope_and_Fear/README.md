# Daggerheart: Hope & Fear｜扩展隔离清单

> 状态：登记但默认关闭（NOT_LOADED）。  
> 对应规则系统：`system_id: daggerheart`。  
> 扩展版本：Daggerheart: Hope & Fear（2026-08-25 起已正式发布）。

## 为什么单独隔离

官方 Daggerheart SRD v2.0 将 Core Set 与 Hope & Fear 的公开规则内容放在同一份 SRD 中。因而，单纯读取 SRD v2.0 并不能得到纯 Core Set 内容。

本目录用于记录扩展专属内容和混合来源的识别规则，避免初版研究、角色创建或运行时误把扩展内容当作基础选项。SRD 中未能明确归属的条目一律先标记 `VERSION_UNRESOLVED`。

## 已知扩展内容

依据官方 SRD v2.0 Changelog、官方扩展介绍和官方 Downloads 页面，以下内容归入 Hope & Fear：

- 四个新职业：Assassin、Brawler、Warlock、Witch，以及对应子职业。
- Dread Domain（惧怖领域）及其领域卡。
- 六种转化：Demigod、Ghost、Reanimated、Shapeshifter、Vampire、Werewolf。
- 新增种族与社群选项。
- 扩展武器、护甲、物品和消耗品。
- 扩展敌人与环境数据。
- Hope & Fear 的四个战役框架及其配套机制。
- 官方扩展专属辅助表、角色卡、卡牌打印文件与扩展勘误。

以上清单用于版本隔离，不是对每一项具体规则的完整整理。详细条目仍须按官方扩展原书、SRD 和勘误核验。

## 加载条件

默认不加载。只有满足以下任一条件才允许启用：

1. 用户明确要求本次 Campaign 使用 Hope & Fear；
2. Campaign 的 `SYSTEM_BINDING.md` 明确列出希望启用的扩展条目；
3. 某个规则条目无法与 Core Set 区分，而为保证基础机制完整性确有必要引用。此时也必须保留扩展标签，不把它改写成 Core 规则。

启用时应按需加载条目，不要求一次性导入整套扩展。

## 来源

- 官方扩展介绍：https://www.daggerheart.com/daggerheart-hope-fear-is-now-available/
- 官方 SRD：https://www.daggerheart.com/srd/
- 官方辅助资料：https://www.daggerheart.com/downloads/
- 中文双语 SRD：https://www.daggerheart.cn/SRD/
- 中文主持研究：https://ttrpg.shinkan42.cn/rule/dagger_heart/

## 与基础规则的边界

- 希望骰、恐惧骰、Hope、Fear 等基础核心机制不是本扩展独有机制；不要因为系统名称含有 Hope & Fear 就将其整体误判为扩展规则。
- SRD v2.0 收录扩展条目，不代表 Campaign 自动开启扩展。
- 扩展内容不能改写 Core Set 基础条目；若扩展卡牌覆盖基础规则，必须记录明确的覆盖关系。
- 扩展专属规则不得流入 Daggerheart Core Runtime，除非 Campaign Binding 明确允许。
