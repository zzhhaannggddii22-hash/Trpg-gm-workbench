# WWN 外部资源目录与版权核查

最后核查：2026-11-28。此文件只登记可访问资源、用途和使用边界；不代表第三方内容已获再分发许可。

## A. 官方与作者来源

### Worlds Without Number Free Edition
- DriveThruRPG：https://www.drivethrurpg.com/product/348809/Worlds-Without-Number-Free-Edition
- 2021 Free Version；出版方Sine Nomine Publishing；免费获取，但仍受版权保护。
- 出版方Deluxe页面明确说明Free Edition已含基础规则、主要Worldbuilding/Adventure/Faction工具；Deluxe另增Heroic、Legate、额外职业及额外GM工具。
- 用途：核对玩家规则和GM工具，优先使用合法取得的原书。
- 归档：只存私人库中用户合法取得的原始文件；不将第三方PDF镜像复制进公开仓库。

### Worlds Without Number Deluxe PDF
- 官方产品页：https://sinenominepublishing.com/products/worlds-without-number-deluxe-pdf
- 当前页面标价US$19.99（价格可能变化）。
- 包含Heroic规则、Legate、额外职业（Invoker、Skinshifter、Beastmaster、Blood Priest、Duelist、Thought Noble）及额外GM工具。
- 版权状态：受版权保护；不得因SRD CC0而推断Deluxe内容也开放。

### Atlas of the Latter Earth
- 出版方WWN系列入口：https://www.sinenominepublishing.com/collections/worlds-without-number/products/atlas-of-the-latter-earth-offset-edition
- 当前页面列出Offset Print Edition，US$64.99；购买后提供PDF/MOBI/EPUB。
- 用途：Latter Earth世界设定和地域资料。版权保护，私人合法持有副本。

## B. CC0规则与结构化数据

### Worlds Without Number SRD v1.0
- 作者Kevin Crawford，日期2024-03-13。
- SRD引言明确以CC0 1.0 Universal放弃文档内版权及相关权利，并明确列出可复制、改编的范围。
- 官方作者许可说明：https://wwn.quadrifons.com/
- 清理版Markdown：https://rpg.blulaktuko.net/wwn/srd.md
- 本地离线数据已收录在 `Rule_Reference/Data/`，不需要运行时联网。

### Worlds Without Number System JSON
- 上游项目：https://github.com/klrkdekira/wwn-system-json
- 在线浏览器：https://cheeleong.dev/wwn-system-json/
- 上游明确：SRD文本与JSON-LD游戏数据为CC0；代码、Schema、构建工具为MIT。
- 覆盖职业、Arts、Foci、法术、装备、怪物、Faction Assets、Faction Actions、Faction Goals、Project Rules、表格等。
- 上游记录总量1,172（1,171游戏实体 + 1来源元数据）；本项目现有离线数据源已记录1171游戏记录。
- 许可核对：只使用CC0游戏数据，不复制MIT程序/Schema到本项目，除非另行按MIT要求保留版权和许可。

## C. 角色创建与角色卡工具

### Characters Without Number — WWN Character Builder
- https://characterswithoutnumber.app/wwn-character-builder/
- 免费浏览器角色创建器；支持Warrior、Expert、Mage、Adventurer及Partial组合，背景、Foci、魔法传统、法术、Arts、Effort、升级与PDF导出。
- Deluxe选项有开关；可用于人工交叉核对角色卡计算。
- 服务条款：https://characterswithoutnumber.app/terms/
- 该站条款禁止自动抓取/过载服务，并禁止发布未经授权的书籍设定内容；仅作为在线工具使用，不抓取其数据。

### WWN Character Creator（GPL-3.0）
- https://github.com/noah-sennett/wwn-character-creator
- 社区浏览器建卡工具，README称数据来自公开WWN版本；仓库标注GPL-3.0。
- 可参考实现与代码结构；若复用代码需遵守GPL-3.0，并单独核对其中规则数据来源。

### Obsidian WWN Markdown
- https://github.com/Obsidian-TTRPG-Community/Obsidian-WWN-Markdown
- 社区Obsidian Vault，含Compendium和角色卡PDF；README说明其以受限制的重写/快速参考方式整理Free版内容。
- 仅作结构与工作流参考；先核查仓库License.md及上游限制，不整库复制到本项目。

### Obsidian TTRPG Share — WWN角色卡
- https://github.com/Obsidian-TTRPG-Community/ObsidianTTRPGShare
- WWN/SWN合并角色卡的社区链接目录：https://github.com/Obsidian-TTRPG-Community/ObsidianTTRPGShare/blob/main/Without-Numbers/templates/character/pdf-links-swn-wwn.md
- 链接由第三方作者托管；仅链接引用，不将外部PDF视为本项目拥有。

## D. VTT与GM生成工具

### Foundry VTT — Worlds Without Number
- https://github.com/SobranDM/foundryvtt-wwn
- GPL-3.0项目；支持PC/NPC角色表、Full/Partial职业、Effort/法术资源、Foci/Arts/Effects、装备、Faction Assets、Morale/Instinct及部分GM生成器。
- README明确Deluxe内容不包含；项目要求用户另有WWN规则。
- 可研究自动计算、Compendium组织和界面交互；不复制其代码或Compendium数据到本工程。代码复用需遵守GPL-3.0，游戏文本另行核对授权。

### Worlds Without Number Random Generators
- https://jdglaser.github.io/ttrpg-generators/
- 提供Free Edition相关随机表的网页交互生成器，可按表格刷新结果。
- 因其内容来自书籍中的表格，按版权内容处理；可在线使用/参考，不抓取或本地重制原表正文。

### World Anvil — WWN Community Statblocks
- https://www.worldanvil.com/community/rpg/system/wwn
- 用户分享的WWN角色/Statblock；页面说明分享作品采用CC BY-SA 4.0。
- 可按署名-相同方式共享条件使用具体作品；逐条核对作者和许可，不批量搬运。

## E. 归档策略

| 类型 | 存放位置 | 处理 |
|---|---|---|
| CC0 SRD及CC0结构化数据 | 本公开工程 `Rule_Reference/Data/` | 已离线收录 |
| Free Edition原始PDF | 私人库 `TRPG/SYSTEMS/Worlds_Without_Number/Sources/Commercial/` | 用户合法取得/提供后存档 |
| Deluxe PDF、Atlas及受保护补充书 | 私人库对应商业源文件目录 | 用户合法取得/提供后存档 |
| GPL/MIT开源工具代码 | 只保留来源链接，确需复用时按许可证处理 | 不整库复制 |
| 第三方在线生成器/角色卡 | 本目录登记链接 | 不抓取受版权保护表格或服务数据 |
| 原创中文摘要、运行规则、检索表 | 本公开工程 | 可供运行时使用 |

## 版权底线
“免费取得”不等于“CC0”；“私人仓库”也不自动产生复制/再分发许可。SRD CC0只覆盖SRD本身明确包含的内容，不延伸到Free Edition/Deluxe未纳入的设定、插画、具体NPC/地点/事件及大部分创意性GM工具。
