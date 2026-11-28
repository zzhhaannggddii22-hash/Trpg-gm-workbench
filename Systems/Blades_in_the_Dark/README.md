# Blades in the Dark /《暗影之刃》

> system_id: `blades_in_the_dark`  
> 核心核验基准：《暗夜刀锋》中文版规则书 V1.3（英文原版版权页标注 2017 Digital Release v8.2）；中文 SRD 作为辅助对照（其修订号未标明）  
> 作者：John Harper  
> 出版商：Evil Hat Productions  
> 中文译者：洪伟  
> 状态：candidate（规则研究完成基础准备；已建立 Campaign 01 备团目录，等待玩家建团与实战验证）

本目录是《暗影之刃》（Blades in the Dark）系统级资料的独立入口。仓库内以用户采用的名称“暗影之刃”称呼本系统；现有中文 SRD 使用的译名是“暗夜冷锋”。两者指向同一作品，不代表不同版本。

本系统与 Triangle Agency、Cairn 完全隔离。系统规则仍处于 candidate；已按用户授权建立独立 Campaign 01 备团目录，但尚未开始游戏。Campaign 的建立不等于系统已 active，也不把本系统机制并入通用 GM Runtime 或其他系统。

```yaml
system_id: blades_in_the_dark
ruleset_versions:
  - "核心规则书：中文《暗夜刀锋》V1.3（英文原版 v8.2）"
  - "中文 SRD / 《暗夜冷锋》译本（修订号待核，辅助对照）"
status: candidate
runtime_dispatch:
  rule_entry: Systems/Blades_in_the_Dark/RUNTIME_PROTOCOL.md
  progression_entry: Systems/Blades_in_the_Dark/Rule_Reference/CORE_RULES_RUNTIME.md
  readiness: CANDIDATE_RUNTIME_DRAFT_COMPLETE_VALIDATION_PENDING
  mechanisms:
    action_resolution:
      status: DOCUMENTED_CANDIDATE
    score_procedure:
      status: DOCUMENTED_CANDIDATE
    flashback:
      status: DOCUMENTED_CANDIDATE
    downtime:
      status: DOCUMENTED_CANDIDATE
  source_conflicts:
    armor_recovery:
      status: RESOLVED_FOR_V1_3_BASELINE
      tracking: Rule_Reference/RULE_ISSUES.md#r-005
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
- [Rule_Reference/DOSKVOL_CITY_GUIDE_INDEX.md](./Rule_Reference/DOSKVOL_CITY_GUIDE_INDEX.md)：核心规则书多斯科沃城市指南的本地检索入口。
- [Rule_Reference/DOSKVOL_DISTRICTS_REFERENCE.md](./Rule_Reference/DOSKVOL_DISTRICTS_REFERENCE.md)：多斯科沃 12 个地区的特征值与场景速查。
- [Rule_Reference/DOSKVOL_FACTIONS_REFERENCE.md](./Rule_Reference/DOSKVOL_FACTIONS_REFERENCE.md)：多斯科沃 26 个详细派系条目与其他派系简表的运行索引。
- [Rule_Reference/DOSKVOL_GM_TABLES_REFERENCE.md](./Rule_Reference/DOSKVOL_GM_TABLES_REFERENCE.md)：城市事件、流言、NPC、超自然与刻痕生成工具的运行索引。
- [Rule_Reference/RED_WATERS_CITY_RUNTIME.md](./Rule_Reference/RED_WATERS_CITY_RUNTIME.md)：红水之城替代世设与三种新 Crew。
- [Rule_Reference/VIGILANTES_PLAYSET_RUNTIME.md](./Rule_Reference/VIGILANTES_PLAYSET_RUNTIME.md)：义警 Crew 游玩套件。
- [Rule_Reference/LEVIATHAN_SONG_RUNTIME.md](./Rule_Reference/LEVIATHAN_SONG_RUNTIME.md)：利维坦猎船、航行与狩猎扩展。
- [Rule_Reference/PLAYBOOK_SHEETS_REFERENCE.md](./Rule_Reference/PLAYBOOK_SHEETS_REFERENCE.md)：角色卡/集团卡模板字段索引。
- [Research/SOURCE_INTAKE_2026-11-28.md](./Research/SOURCE_INTAKE_2026-11-28.md)：本轮原始资料清单、版本基线与版权边界。
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
- [GM 行为回归案例](./Testing/GM_BEHAVIOR_REGRESSION_CASES.md)：18 个基于核心规则书 GM 指南设计的 AI 主持行为检查点，不是规则模拟器。
- [自动化检查报告](./Testing/AUTOMATED_CANDIDATE_CHECKS_2026-11-28.md)：有限的文档不变量与确定性微模型检查，仅作辅助质量门槛，不代表 GM 能力或真人验收。
- [历史规则模拟报告](./Testing/ENGINE_SIMULATION_REPORT_2026-11-28.md) 与 [模拟 harness](./Testing/ENGINE_SIMULATION_V1.js)：仅为规则流程/状态边界的有限实验材料，不是本系统的 GM 运行主体，也不构成完整引擎。后续优先级以 GM Skill、Runtime Protocol、真实主持表现与复盘为准。
- [Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28.md](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28.md)、[第二轮报告](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28_R2.md)、[第三轮报告](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28_R3.md) 与 [第四轮报告](./Testing/SYNTHETIC_EXECUTION_REPORT_2026-11-28_R4.md)：四轮共 75 个固定输入合成用例的执行记录；不等同于自动化测试或真人跑团验收。
- [Research/CHINESE_SRD_SOURCE_REVIEW_2026-11-28.md](./Research/CHINESE_SRD_SOURCE_REVIEW_2026-11-28.md)：中文 SRD 来源审查。
- [Research/EXTERNAL_RESOURCES.md](./Research/EXTERNAL_RESOURCES.md)：官方免费资料、社区扩展与额外资料入口。

## Campaign

- [Campaign 01｜灰烬与欠账](./Campaigns/DOSKVOL_01_ASH_AND_DEBTS/README.md)：多斯科沃开放式 Crew 战役；规则版本已绑定，战役状态、派系调用、NPC 名册、Score 机会生成、Session 01 准备与 GM-only 资料已建立。当前等待玩家任务卡、PC 与 Crew 建档；用户明确说“开始”前不启动游戏。

## 系统边界

- 所有骰型、行动、属性、资源、后果、成长、案件流程与术语均以本系统自身规则为准。
- 不导入 Triangle Agency 的 QA、Burnout、Chaos、Harm 或 Playwall；不导入 Cairn 的豁免、HP、疲劳、库存格或探索程序。
- 从本系统得到的 GM 技巧只有经过跨系统验证后，才可提炼到 `GM_Training/`；具体规则和专属流程始终留在本目录。
- 当前 candidate 阶段只用于学习、查证和建立索引。未来正式开团时，必须另建 Campaign 并通过 `SYSTEM_BINDING.md` 锁定精确规则版本与规则来源。

## 当前完成度与激活前待完成事项

已完成：
- 本轮新增的 7 个原始 PDF/XLSX/ZIP 已归档至私人资料库 `/TRPG/Blades in the Dark/Source Files/`；公开仓库只保存原创整理与索引。
- 已确认核心规则书 V1.3 对应英文原版 v8.2，并建立章节导航、多斯科沃城市指南总索引、12 个地区速查、26 个详细派系条目索引和 GM 生成工具速查。
- 已建立系统专属核心规则索引、Runtime Manual、Runtime Protocol、GM Skill、Preflight 和术语表；GM Skill 现以 AI 如何实际主持对话、提供机遇、扮演 NPC、控制镜头与处理玩家能动性为核心。
- 已建立七种核心 PC Playbook 与六种 Crew 的能力目录及触发式运行矩阵；角色/组织只按实际选取的能力进行触发式加载。
- 已建立来源与授权索引、额外资料目录、规则疑点登记，以及 Candidate 验证矩阵；75/75 固定输入合成用例已通过四轮人工推演。
- 已将中文 SRD、官方 Player's Kit v8.2 与完整核心规则书 V1.3 纳入来源对照；Armor 普通护甲/特殊护甲恢复时序已按完整规则书拆分处理。
- 已建立红水之城、义警、利维坦之歌三个独立扩展运行入口，以及角色卡/集团卡字段索引。

仍待完成：
1. 未来 Campaign 必须锁定具体核心规则版本与勘误；中文 SRD 页面自身未提供清晰修订号。
2. 七种核心 PC Playbook 与六种 Crew 的能力已建立触发式运行矩阵，但每项能力仍须在实际角色/组织建档时按所选版本卡面核对触发条件、成本、持续时间和例外；Veteran 来源、实际选中能力的完整卡面、升级/Claims 与具体公式/仪式效果仍需按实际战役版本回查。
3. 75 条 Candidate 合成回归用例已通过；仍需补做独立跨系统隔离测试，并至少完成一次短团实测和复盘。
4. Campaign 01 已建立独立 Campaign Binding；仍需完成玩家任务卡、PC/Crew 建档与首次战役 Preflight，系统继续保持 candidate。
5. 普通 Armor 与 Special Armor 的恢复时序已按 V1.3 核心规则书分别处理；其他版本仍需重新核验，见 [R-005](./Rule_Reference/RULE_ISSUES.md#r-005resistance-与-armor-的时序)。
6. 多斯科沃地区、派系和 GM 生成工具已有本地索引；仍待把重要 NPC、完整地区细节与派系当前情况按战役需求进一步拆分为可直接调用的战役资料。
7. 红水之城仍是预览版；义警与利维坦之歌仍需按各自版本完成规则交叉核验与模块测试。

因此，当前已形成可供进一步测试的规则运行草案，但尚不标记 active，也不用于任何正式 Campaign。
