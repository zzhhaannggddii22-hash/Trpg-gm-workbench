# Blades in the Dark｜Candidate Validation Manifest

> system_id: `blades_in_the_dark`  
> ruleset: 中文《暗夜冷锋》SRD（上游快照 2023-08-15；规则修订号待核）  
> status: CANDIDATE_VALIDATION  
> 本文件不是正式 Campaign Binding，不允许把测试状态写入任何正式战役。

## 1. 验证目标

验证本系统专属规则运行文件在一个干净会话中是否能够：
- 只加载 Blades 自己的规则和状态；
- 正确分流 Action / Fortune / Resistance / Downtime；
- 按规则处理 Position、Effect、Consequence 和资源变化；
- 从 Score Setup 连续运行到 Payoff、Heat、Entanglements、Downtime；
- 在 PC、Crew、Faction、Cohort 与 Clocks 之间维持状态连续性；
- 不在普通互动中额外执行无关检查；
- 不把 Triangle Agency、Cairn 或其他系统的机制带入。

## 2. 固定输入

测试只使用合成状态，不继承任何现有 Campaign：

```yaml
validation:
  system_id: blades_in_the_dark
  ruleset_version: "Blades in the Dark SRD / Chinese translation snapshot 2023-08-15"
  fixture_id: BITD_CANDIDATE_V01
  status: TEST_ONLY_NON_CANON
crew:
  tier: 0
  hold: strong
  rep: 0
  turf: 0
  coin: 2
  heat: 0
  wanted_level: 0
pc:
  action_ratings:
    hunt: 1
    study: 1
    survey: 0
    tinker: 1
    finesse: 1
    prowl: 2
    skirmish: 1
    wreck: 0
    attune: 0
    command: 1
    consort: 1
    sway: 1
  stress: 0
  trauma: []
  harm: []
  vice: "TEST_ONLY"
factions: []
clocks: []
```

## 3. 范围边界

包含：基础骰型、PC 行动、抵抗、伤害、压力与创伤、时钟、调查、Score、Flashback、Teamwork、Downtime、Heat、Wanted、Entanglements、Crew 成长、Faction/Cohort、Magnitude、Ritual、Invention、Crafting、Modification、Drawbacks，以及七种核心 PC Playbook / 六种 Crew 的已拥有能力触发。

不包含：未经获取和核对的商业核心书独占内容、官方城市地图/派系设定/完整 NPC、未许可的角色表或工具包、任何未批准的 Fan-made Playbook/Crew/Score。

## 4. 验收顺序

1. 先做静态规则一致性检查：规则索引 ID、运行手册、Runtime Protocol、GM Skill 与 Preflight 是否使用相同术语和顺序。
2. 做单条规则正例/反例。
3. 做跨机制组合测试：Action → Resistance/Armor → 状态写入；Score → Settlement → Downtime。
4. 做 Magnitude、Ritual、Invention、Crafting、Modification、Drawbacks 的正例/反例与组合测试。
5. 做七种核心 PC Playbook / 六种 Crew Ability 的触发、资源、范围、次数、重置与冲突测试。
6. 做跨系统隔离测试。
7. 做一次受控短团或真实短团，检查主持行为、信息公平、节奏和状态连续性。
8. 记录失败样例并修订规则文件，再重复受影响测试。

## 4-A. Arcane & Crafting regression cases

- [ARCANE_CRAFTING_REGRESSION_CASES.md](./ARCANE_CRAFTING_REGRESSION_CASES.md)：13 个基于核心规则书 V1.3 PDF pp.228–231 的预期结果案例，覆盖仪式、发明、制作、改造和缺点。
- 13/13 为人工对照原文审阅；尚未自动执行，也不代表完整引擎模拟或真人跑团验证。


以下项目全部完成后才能考虑评估为 active：
- 规则版本与官方勘误/适用补充来源明确；
- 所有当前角色/组织能力与常用资源条目按战役实际需求核验；
- 核心规则、超自然/制造与核心能力触发回归用例通过；
- 跨系统污染测试通过；
- Preflight 能在干净上下文正确加载；
- 至少一次独立短团实测，并对游戏体验和 GM 行为复盘；
- 用户确认建立正式 Campaign。

通过文档检查或合成用例不等于真实跑团验收。Candidate 不会自动升级为 active。


## 自动化检查追加记录（2026-11-28）

- [AUTOMATED_CANDIDATE_CHECKS_2026-11-28.md](./AUTOMATED_CANDIDATE_CHECKS_2026-11-28.md)：31 项文档不变量/确定性微模型检查 PASS。
- 本轮没有完整规则引擎执行、全部 75 固定场景自动重放或真人短团测试；Armor 来源冲突 R-005 仍 OPEN。


## 集成引擎模拟（子集）

- [ENGINE_SIMULATION_REPORT_2026-11-28.md](./ENGINE_SIMULATION_REPORT_2026-11-28.md)；[Harness](./ENGINE_SIMULATION_V1.js)。本轮对 harness 逻辑进行独立 inline replay：23/23 通过，含 1,000 组 Heat 边界 fuzz 输入。
- 提交的 standalone harness 源文件未在此聊天环境的 Node runtime 中直接执行；模拟覆盖有限，不应称为完整引擎认证。
