# 《希望与恐惧》扩展隔离清单

> 状态：登记但默认关闭（`NOT_LOADED`）。  
> 对应规则系统：`system_id: daggerheart`。  
> 扩展版本：Daggerheart: Hope & Fear，官方于 2026-08-25 发布。

## 为什么单独隔离

官方 Daggerheart SRD v2.0 将 Core Set 与 Hope & Fear 的公开规则内容放在同一份 SRD 中。单纯读取 SRD v2.0 并不能得到纯 Core Set 内容。

本目录用于识别扩展专属内容，避免基础版研究、角色创建或运行时误把扩展选项当成核心选项。来源无法明确归属的条目标记 `VERSION_UNRESOLVED`。

## 已知扩展内容

依据官方 SRD v2.0 Changelog、扩展介绍与官方 Downloads 页面：

- 四个新职业：Assassin、Brawler、Warlock、Witch，以及对应子职业。
- Dread Domain（惧怖领域）及 21 张相关领域卡。
- 六种转化：Demigod、Ghost、Reanimated、Shapeshifter、Vampire、Werewolf。
- 新增种族与社群选项。
- 扩展武器、护甲、物品与消耗品。
- 扩展敌人与环境数据。
- Hope & Fear 的四个 Campaign Frames 及其专属内容。
- 扩展职业辅助表、角色卡、卡牌打印文件与 Hope & Fear Errata。

以上仅是版本隔离目录，不是每项规则的完整解释。

## 本地数据入口

- `../../Reference_Data/Hope_and_Fear/classes.json`
- `../../Reference_Data/Hope_and_Fear/subclasses.json`
- `../../Reference_Data/Hope_and_Fear/domains.json`
- `../../Reference_Data/Hope_and_Fear/domain_cards.json`
- `../../Reference_Data/Hope_and_Fear/ancestries.json`
- `../../Reference_Data/Hope_and_Fear/communities.json`
- `../../Reference_Data/Hope_and_Fear/adversaries.json`
- `../../Reference_Data/Hope_and_Fear/environments.json`
- `../../Reference_Data/Hope_and_Fear/weapons.json`
- `../../Reference_Data/Hope_and_Fear/armor.json`
- `../../Reference_Data/Hope_and_Fear/items.json`
- `../../Reference_Data/Hope_and_Fear/consumables.json`
- `../../Reference_Data/Hope_and_Fear/transformations.json`

## 加载条件

默认不加载。只有满足以下条件之一才允许启用：

1. 用户明确要求本次 Campaign 使用 Hope & Fear；
2. Campaign 的 `SYSTEM_BINDING.md` 明确列出启用的扩展条目；
3. 某个规则条目无法与 Core Set 区分，而为保证规则完整性确有必要引用。此时仍保留扩展标签，不把它改写成 Core。

启用时按需加载具体条目，不要求一次性导入整套扩展。

## 与基础规则的边界

- Hope、Fear、Hope Die、Fear Die 等基础机制并非扩展独有机制；不要因为系统扩展名中包含 Hope & Fear 就误判。
- SRD v2.0 收录扩展条目，不代表 Campaign 自动开启扩展。
- 扩展卡牌覆盖基础规则时，必须记录明确覆盖关系。
- 扩展 Campaign Frame 的完整文字、地图和专有设定不能作为普通资料镜像公开；只保留官方入口与允许分享的规则摘要。

## 来源

- 官方扩展介绍：https://www.daggerheart.com/daggerheart-hope-fear-is-now-available/
- 官方 SRD：https://www.daggerheart.com/srd/
- 官方辅助资料：https://www.daggerheart.com/downloads/
- 中文双语 SRD：https://www.daggerheart.cn/SRD/
- 中文主持研究：https://ttrpg.shinkan42.cn/rule/dagger_heart/
