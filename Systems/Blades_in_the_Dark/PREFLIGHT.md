# Blades in the Dark｜Preflight

> system_id: blades_in_the_dark  
> 状态：CANDIDATE VALIDATION / 尚未批准正式 Campaign  
> 本文件适用于未来新 Campaign / 新 Session 的启动前核验。

## A. 系统绑定核验

- [ ] Campaign 的 SYSTEM_BINDING 明确写明 system_id: blades_in_the_dark。
- [ ] 规则版本/发行版/语言来源已明确；不能只写“中文版”或“SRD”。
- [ ] 系统目录入口指向 Systems/Blades_in_the_Dark/README.md。
- [ ] Campaign 没有混入 Triangle Agency、Cairn 或其他系统的骰型/资源/阶段程序。
- [ ] 若使用自制或社区扩展，标为 OPTIONAL / FAN-MADE，并记录版本、来源和许可。

## B. 规则来源就绪

- [ ] 中文 SRD 镜像可用；读取私人资料库的对应章节。
- [ ] 关键冲突与疑点已查阅 Rule_Reference/RULE_ISSUES.md。
- [ ] 规则版本与官方勘误/免费工具包交叉核验范围明确。
- [ ] 关键角色能力、Crew 能力、装备、Ritual、Crafting 与特殊状态已定位原文。
- [ ] 已读取 `ABILITY_RUNTIME_MATRIX.md`，并只登记当前 PC/Crew 实际拥有的能力。
- [ ] 若当前战役涉及 Ritual / Magnitude / Invention / Crafting，已定位 `ARCANE_AND_CRAFTING_RUNTIME.md` 与具体设计/仪式记录。
- [ ] 未将商业核心书或非 SRD 世界设定当作已公开授权素材。

## C. PC 与 Crew 状态

每名 PC：
- [ ] Playbook、Heritage、Background、Action ratings、Attribute 分组。
- [ ] 特殊能力与 Veteran Ability（如有）已核对。
- [ ] Friend / Rival、Vice / Vice purveyor。
- [ ] Stress、Trauma、Harm、Armor、Healing Clock。
- [ ] XP tracks、Stash、装备清单和 Load 规则。

Crew：
- [ ] Crew Type、声望、Lair、Hunting Grounds、Favored Operation。
- [ ] Tier、Hold、Rep、Turf、Claims。
- [ ] Special Ability、Upgrades、Cohorts 与其 Edges/Flaws。
- [ ] Coin/Vault、Heat、Wanted Level、Faction Status。
- [ ] 相关 Faction 与 NPC 的目标、利益、关系和必要项目钟。

## D. GM 主持能力就绪
- [ ] 已读取 `GM_SKILL.md`，理解 GM 是呈现情境、提供机遇并跟随行动与后果，而非预写剧情。
- [ ] 能通过提问澄清玩家目标，并帮助玩家创造可行机遇，而不是堵死行动路线。
- [ ] 能区分潜在虚构与既定虚构，保持已确立事实连续，同时允许未确立细节灵活调整。
- [ ] NPC 有具体渴望、偏好手段、能力与限制，并据此行动。
- [ ] 能按玩家兴趣调整镜头尺度，避免无意义的细碎掷骰与冗长准备。
- [ ] 能主动提供角色有资格知道的信息，不把所有线索都藏在检定之后。
- [ ] 能保持玩家可见信息与 GM-only 信息隔离。

## E. 规则运行就绪

- [ ] 能按 Action Roll 六步处理目标、Action、Position、Effect、奖励骰和结果。
- [ ] Position 和 Effect 分开判定。
- [ ] 能正确给出 Consequence，并处理 Resistance / Armor / Stress。
- [ ] 能区分 Action Roll、Fortune Roll、Resistance Roll。
- [ ] 能合理建立/推进 Clocks，不将简单障碍变成生命值钟。
- [ ] 能用 Plan + Detail + Load + Engagement Roll 直接切入 Score。
- [ ] 能处理中途 Flashback、Assist、Group Action、Protect、Setup。
- [ ] Score 结算按 Payoff → Heat → Entanglements → Downtime 顺序执行。
- [ ] Downtime 活动预算、额外活动费用、Vice、恢复、项目与成长正确。
- [ ] NPC/Faction Downtime 只推进相关对象，不做全城逐 NPC 模拟。
- [ ] 规则未知时能暂停相关裁定、记录问题并使用对应来源继续核验。

## F. Candidate Validation

当前尚为 candidate。正式 Campaign 开始前，至少完成：
1. 骰型、Action Roll、Position/Effect 与后果的正例/反例测试；
2. Resistance、Armor、Harm、Stress、Trauma 的状态变更测试；
3. Score/Engagement/Flashback/Teamwork 连续流程测试；
4. Payoff、Heat、Entanglement、Downtime、成长的完整结算测试；
5. Crew/Faction/Cohort 与 PC 状态的连续性测试；
6. 与 Triangle Agency、Cairn 的规则隔离测试；
7. Ritual、Magnitude、Invention、Crafting、Modification 与 Drawbacks 的边界测试；
8. 核心 PC/Crew Ability 的触发、资源、范围和重置点测试；
9. 一轮真实短团或明确授权的受控测试，并完成复盘。

Candidate 验证必须使用 TEST_ONLY_NON_CANON Validation Manifest，不创建正式 Campaign 状态。通过模拟测试不等于真实实战验收；通过候选验证也不自动意味着系统已 active。

## G. Session 启动快照

```yaml
active_system:
  system_id: blades_in_the_dark
  ruleset_version: "<locked version>"
  campaign_id: "<campaign_id>"
  module_id: "<module_id or null>"
runtime:
  phase: FREE_PLAY
  current_score_id: null
  pc_state_snapshot: "<current sheet references>"
  crew_state_snapshot: "<current crew sheet reference>"
  active_factions: []
  active_clocks: []
  open_rule_issues: []
```

## H. Preflight 结果

记录本次结果：
- READY：本次行动可按当前规则运行；
- READY_WITH_LIMITS：局部规则缺口不影响当前行动，保留待办；
- BLOCKED：系统绑定、规则版本或当前关键裁定无法确认。

只阻断依赖未解决规则的问题，不因一个规则疑点冻结所有互动。
