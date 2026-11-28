# Blades in the Dark /《暗影之刃》

> system_id: `blades_in_the_dark`  
> 规则版本：Blades in the Dark SRD（中文译本《暗夜冷锋》；中文页面未标明具体修订号）  
> 作者：John Harper  
> 出版商：Evil Hat Productions  
> 中文译者：洪伟  
> 状态：candidate（独立规则研究中；尚无正式 Campaign）

本目录是《暗影之刃》（Blades in the Dark）系统级资料的独立入口。仓库内以用户采用的名称“暗影之刃”称呼本系统；现有中文 SRD 使用的译名是“暗夜冷锋”。两者指向同一作品，不代表不同版本。

本系统与 Triangle Agency、Cairn 完全隔离。当前只建立规则资料与研究入口，不创建 Campaign、不启用正式运行，也不把本系统机制并入通用 GM Runtime 或其他系统。

```yaml
system_id: blades_in_the_dark
ruleset_versions:
  - "Blades in the Dark SRD / 中文《暗夜冷锋》译本（修订号待核）"
status: candidate
runtime_dispatch:
  rule_entry: Systems/Blades_in_the_Dark/Rule_Reference/README.md
  progression_entry: Systems/Blades_in_the_Dark/Rule_Reference/README.md
  readiness: STUDY_ONLY
  mechanisms:
    score_procedure:
      status: PENDING
    flashback:
      status: PENDING
    downtime:
      status: PENDING
```

## 权威来源与资料边界

### 中文规则入口

- [中文《暗夜冷锋》SRD](https://bitd.wayneh.tw/)：当前主要中文规则阅读入口，采用繁体中文。
- [中文化团队的作品说明](https://hazmole.github.io/Free-Open-TRPG-Translation/posts/blade-in-the-dark/)：记录作品、作者、译者、授权与中文规则入口。
- [中文 SRD 来源仓库](https://github.com/wayne930242/bitd)：用于核对中文网站的章节结构与页面更新；不作为独立的规则版本权威。

中文 SRD 页面说明：原系统参考文件由 One Seven Design 以 CC BY 授权发布，中文翻译由洪伟以 CC BY 授权发布。中文页面未标明 SRD 的具体修订号，建团时需要核对所采用的规则版本及勘误。

### 官方补充资料

- [Blades in the Dark 官方下载页](https://bladesinthedark.com/downloads)：提供 Core Play Sheets、Full Player's Kit、角色与组织表单、派系列表等。
- [官方 Full Player's Kit（v8.2 PDF）](http://bladesinthedark.com/sites/default/files/blades_playerkit_v8_2.pdf)：包含基本流程、角色与组织创建、派系、城市与破碎群岛地图、规则速查表。它是玩家工具包，不等同于完整商业规则书。

### 版权与仓库处理

- 中文 SRD 主体按页面声明的 CC BY 授权使用；如引用或改编其规则文本，必须保留原作者、译者、来源与授权信息。
- 中文网站的“非 SRD 部分”明确不在该 CC BY 授权范围内。其中的中文在线工具包包含角色卡、组织卡、派系追踪、监狱权利与尚未完成的灵体角色资料。
- 本仓库公开。遵守仓库总 README 的第三方内容边界：不复制或分发完整商业规则书、完整翻译、未获授权的表单/工具包或模组全文。仓库只保存自写索引、摘要、研究记录、规则定位与来源链接。

## 目录

- [Rule_Reference/](./Rule_Reference/README.md)：中文 SRD 与官方补充资料索引、覆盖范围、版本和授权边界。
- [Research/](./Research/CHINESE_SRD_SOURCE_REVIEW_2026-11-28.md)：中文规则来源审查与初步研究记录。

## 系统边界

- 所有骰型、行动、属性、资源、后果、成长、案件流程与术语均以本系统自身规则为准。
- 不导入 Triangle Agency 的 QA、Burnout、Chaos、Harm 或 Playwall；不导入 Cairn 的豁免、HP、疲劳、库存格或探索程序。
- 从本系统得到的 GM 技巧只有经过跨系统验证后，才可提炼到 `GM_Training/`；具体规则和专属流程始终留在本目录。
- 当前 candidate 阶段只用于学习、查证和建立索引。未来正式开团时，必须另建 Campaign 并通过 `SYSTEM_BINDING.md` 锁定精确规则版本与规则来源。

## 激活前待完成事项

1. 确认未来 Campaign 实际采用的规则版本、修订号与勘误。
2. 逐项核对中文 SRD 的规则覆盖、术语和关键裁定；对 SRD 未覆盖部分回查合法取得的官方原文或官方免费资料。
3. 建立系统专属规则索引、运行路由与 Preflight；不预先复制其他系统的结构性机制。
4. 建立独立 Campaign Binding，并完成规则边界与跨系统隔离验证。
