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
  rule_entry: Systems/Blades_in_the_Dark/RUNTIME_PROTOCOL.md
  progression_entry: Systems/Blades_in_the_Dark/Rule_Reference/CORE_RULES_RUNTIME.md
  readiness: CANDIDATE_RUNTIME_DRAFT_COMPLETE_VALIDATION_PENDING
  mechanisms:
    action_resolution:
      status: PENDING
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

- [Rule_Reference/README.md](./Rule_Reference/README.md)：规则来源、版本与授权边界。
- [Rule_Reference/CORE_RULE_INDEX.md](./Rule_Reference/CORE_RULE_INDEX.md)：按触发条件调用的核心规则索引与 Rule ID。
- [Rule_Reference/CORE_RULES_RUNTIME.md](./Rule_Reference/CORE_RULES_RUNTIME.md)：骰型、Action/Position/Effect、后果、Score、Downtime、Crew/Faction 等可运行规则摘要。
- [Rule_Reference/ARCANE_AND_CRAFTING_RUNTIME.md](./Rule_Reference/ARCANE_AND_CRAFTING_RUNTIME.md)：Magnitude、Ritual、Invention、Crafting、Modification、Drawbacks 的完整触发式流程。
- [Rule_Reference/RULE_ISSUES.md](./Rule_Reference/RULE_ISSUES.md)：翻译差异、版本疑点与待核规则。
- [Rule_Reference/GLOSSARY.md](./Rule_Reference/GLOSSARY.md)：规则术语与译名对照。
- [Rule_Reference/PLAYBOOKS_AND_CREW_REFERENCE.md](./Rule_Reference/PLAYBOOKS_AND_CREW_REFERENCE.md)：七种核心 PC Playbook 与六种 Crew 的能力目录与摘要。
- [Rule_Reference/ABILITY_RUNTIME_MATRIX.md](./Rule_Reference/ABILITY_RUNTIME_MATRIX.md)：核心 PC/Crew 能力的触发、效果、成本、作用范围与边界矩阵。
- [Rule_Reference/CREW_CLAIMS_AND_STARTUP_REFERENCE.md](./Rule_Reference/CREW_CLAIMS_AND_STARTUP_REFERENCE.md)：六种 Crew 的创建、Hunting Grounds、起始升级、Claim Map 与专属 Claim 收益。
- [Rule_Reference/STANDARD_ITEMS_AND_LOAD_REFERENCE.md](./Rule_Reference/STANDARD_ITEMS_AND_LOAD_REFERENCE.md)：核心装备、Load 与护甲携带规则速查。
- [RUNTIME_PROTOCOL.md](./RUNTIME_PROTOCOL.md)：Free Play / Score / Downtime 的运行状态、调用步骤与持久化边界。
- [GM_SKILL.md](./GM_SKILL.md)：本系统的主持原则、叙事和节奏要求。
- [PREFLIGHT.md](./PREFLIGHT.md)：未来新 Campaign / 新 Session 的启动核验。
- [Testing/](./Testing/CANDIDATE_VALIDATION_MANIFEST.md)：Candidate 验证边界与回归测试矩阵。
- [Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28.md](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28.md)、[第二轮报告](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28_R2.md) 、[第三轮报告](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28_R3.md) 与 [第四轮报告](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28_R4.md)：四轮共 75 个固定输入合成用例的执行记录；不等同于自动化测试或真人跑团验收。
- [Research/CHINESE_SRD_SOURCE_REVIEW_2026-11-28.md](./Research/CHINESE_SRD_SOURCE_REVIEW_2026-11-28.md)：中文 SRD 来源审查。
- [Research/EXTERNAL_RESOURCES.md](./Research/EXTERNAL_RESOURCES.md)：官方免费资料、社区扩展与额外资料入口。

## 系统边界

- 所有骰型、行动、属性、资源、后果、成长、案件流程与术语均以本系统自身规则为准。
- 不导入 Triangle Agency 的 QA、Burnout、Chaos、Harm 或 Playwall；不导入 Cairn 的豁免、HP、疲劳、库存格或探索程序。
- 从本系统得到的 GM 技巧只有经过跨系统验证后，才可提炼到 `GM_Training/`；具体规则和专属流程始终留在本目录。
- 当前 candidate 阶段只用于学习、查证和建立索引。未来正式开团时，必须另建 Campaign 并通过 `SYSTEM_BINDING.md` 锁定精确规则版本与规则来源。

## 当前完成度与激活前待完成事项

已完成：
- 33 份中文 SRD Markdown 正文已镜像至用户私人资料库，供后续优先本地检索；公开仓库不放规则正文镜像。
- 已建立系统专属核心规则索引、初版 Runtime Manual、Runtime Protocol、GM Skill、Preflight 和术语表。
- 已建立七种核心 PC Playbook 与六种 Crew 的能力目录及触发式运行矩阵；角色/组织只按实际选取的能力进行触发式加载。
- 已建立来源与授权索引、额外资料目录、规则疑点登记，以及 Candidate 验证矩阵；75/75 固定输入合成用例已通过四轮人工推演。
- 已将中文 SRD 与官方 Player's Kit v8.2 的关键流程做首轮交叉校对，并记录已发现的译文差异。

仍待完成：
1. 未来 Campaign 必须锁定具体核心规则版本与勘误；中文 SRD 页面自身未提供清晰修订号。
2. 七种核心 PC Playbook 与六种 Crew 的能力已建立触发式运行矩阵，但每项能力仍须在实际角色/组织建档时按所选版本卡面核对触发条件、成本、持续时间和例外；Veteran 来源、实际选中能力的完整卡面、升级/Claims 与具体公式/仪式效果仍需按实际战役版本回查。
3. 75 条 Candidate 合成回归用例已通过；仍需补做独立跨系统隔离测试，并至少完成一次短团实测和复盘。
4. 建立独立 Campaign Binding；在用户确认前，系统继续保持 candidate。

因此，当前已形成可供进一步测试的规则运行草案，但尚不标记 active，也不用于任何正式 Campaign。
