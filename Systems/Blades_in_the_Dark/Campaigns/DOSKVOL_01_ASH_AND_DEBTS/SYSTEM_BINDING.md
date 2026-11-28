# Campaign System Binding

```yaml
campaign_id: bitd_doskvol_01_ash_and_debts
campaign_name: "灰烬与欠账"
system_id: blades_in_the_dark
system_display_name: "Blades in the Dark / 暗影之刃"
status: PREPARED_WAITING_FOR_PLAYER_SETUP
ruleset:
  primary_source: "《暗夜刀锋》中文版核心规则书 V1.3"
  original_release: "2017 Digital Release v8.2"
  language: zh-CN
  auxiliary_sources:
    - "官方 Full Player's Kit v8.2"
    - "中文《暗夜冷锋》SRD（修订号未标明，仅辅助核对）"
  conflict_precedence: "完整核心规则书 V1.3 正文优先"
  errata_policy: "如发现与锁定版本相关的勘误，登记后再决定是否纳入；不静默改版"
setting:
  city: Doskvol
  city_source: "核心规则书 V1.3"
  expansion: null
  optional_rules: []
campaign:
  play_mode: "Crew-driven open campaign"
  module_id: null
  opening_score_id: null
  current_phase: FREE_PLAY
  canon_started: false
players:
  pc_count: null
  player_count: null
  pcs: []
crew:
  type: null
  name: null
  tier: null
  hold: null
  lair: null
  hunting_grounds: null
  claims: []
  upgrades: []
  special_abilities: []
runtime:
  current_score_id: null
  active_factions: []
  active_clocks: []
  open_rule_issues: []
```

## 绑定约束

1. 本 Campaign 只使用 `system_id: blades_in_the_dark`。
2. 任何其他系统的属性、骰型、资源、伤害或阶段规则均不得混入。
3. 角色卡与 Crew Sheet 建立后，按其实际能力触发式加载规则；不扫描未选择能力。
4. 规则疑点优先查本系统 V1.3 私人原始资料，再查公开运行摘要。
5. 如确需使用扩展或社区规则，必须先由玩家明确同意，并记录名称、版本和来源。
6. 角色、Crew、派系、时钟和 Score 的状态变化必须有游戏事件依据。
