# Cairn 2e Runtime Protocol

> 适用范围：仅 `system_id: cairn` / `Cairn Second Edition`。
> 状态：candidate runtime protocol v0.2。正式运行必须与 Campaign 的 `SYSTEM_BINDING.md` 一起使用；受控验证使用 TEST_ONLY_NON_CANON Validation Manifest。
> 目的：让 GM 在桌面运行中直接调用已规范化规则，避免每次行动都在线搜索或临场重建规则。

## 1. 运行原则

1. **规则本地化**：常用核心规则以 `Rule_Reference/CORE_RULES_RUNTIME.md` 为运行速查；不在每次行动中重新搜索网页。
2. **权威性不降级**：官方 Cairn 2e 原文仍是最终来源。速查不覆盖、改写或取代原文。
3. **按需回查**：只在规则未收录、标记 PARTIAL、涉及未本地化表格/特殊能力、出现冲突、版本不明，或高后果边界尚未被 VERIFIED_CORE 条目完整覆盖时查官方原文。高后果本身不要求重复联网检索；完整本地规则按原步骤执行并保留状态事务。
4. **先情境后机制**：先判断虚构情境是否可行、是否存在真实风险，再调用对应机制；不得为了展示规则而制造无意义掷骰。
5. **显式状态变更**：任何时间、位置、HP、属性、库存、Fatigue、Armor、条件、金钱、口粮、光源等变化都必须写入 Runtime State。
6. **无跨系统借用**：不得从 Triangle Agency 或其他系统导入检定、资源、战斗、伤害、恢复或时间机制。
7. **不确定性可控**：未知规则标记 `UNKNOWN` 并定位问题；暂停依赖该规则的动作，不冻结无关互动。

## 2. 规则来源与调用层级

运行时按以下顺序调用：

1. Campaign `SYSTEM_BINDING.md`：确认 system_id、精确版本、适配和本桌约定。
2. 当前 Runtime Snapshot：确认角色、位置、时间、资源、已触发/待结算事件。
3. 本文件第 4 节的阶段流程。
4. `Rule_Reference/CORE_RULES_RUNTIME.md`：按规则 ID 检索对应标准步骤。
5. `Rule_Reference/WARDEN_GUIDE_INDEX.md`：处理主持程序、NPC、知识与探索原则。
6. 官方 Cairn 2e 对应章节/表格：仅在需要核验细节、例外或 PARTIAL 条目时回查。
7. 经用户批准的 Table Adaptation：仅在绑定文件明确记录后应用。

规则分类必须明确：
- `SOURCE`：已核对官方 2e 原文。
- `TABLE_ADAPTATION`：本桌明确批准的适配。
- `GM_INFERENCE`：官方未明确覆盖时的主持推论。
- `UNKNOWN`：尚未核实。
- `DISPUTED`：来源冲突未解决。

不得将 GM 推论或临时处理写回 SOURCE 规则。

## 3. 规则调用卡（Rule Call）

每次有机制影响的行动，GM 内部按以下字段组织：

```yaml
rule_call:
  system_id: cairn
  ruleset_version: "Cairn Second Edition"
  rule_id: "CR-SAVE"
  trigger: "当前行动存在真实风险"
  actor: "角色ID"
  target: "对象或环境"
  inputs:
    attribute: "DEX"
    current_value: 9
  procedure:
    - "核对行动可行性与风险"
    - "掷d20"
    - "按属性阈值判定"
  roll: null
  result: null
  consequences: []
  state_delta: []
  source_status: "SOURCE"
  source_locator: "Player's Guide / Core Rules / Saves"
  unresolved: []
```

这是逻辑记录模板，不要求每次都向玩家展示 YAML。玩家侧只需获得足以理解行动、显著风险、代价与结果的信息。

## 4. 标准桌面循环

### 4.1 通用行动循环

1. **读取状态**：读取当前地点、时间、角色状态、库存、光源、正在进行的行动和待结算事件。
2. **呈现局势**：描述角色能观察到的事实、即时危险、空间关系和显著代价。
3. **接收声明**：玩家说明意图与具体做法；不要替玩家补全关键选择。
4. **情境裁定**：判断可行性、所需时间、工具、知识、位置、资源和真实风险。
5. **选择机制**：无风险则直接解决；有风险则调用最适当的规则 ID；多条规则按其依赖顺序调用。
6. **声明风险**：在玩家作出不可逆选择前，说明角色能够理解的显著风险和资源成本。
7. **结算行动**：执行骰子、表格、对抗、伤害或其他程序；保留原始骰值与关键中间值。
8. **提交状态**：逐项应用状态差分；检查上限、归零、触发条件和后续结算。
9. **处理世界后果**：推进时间，处理 NPC、环境、遭遇、光源、口粮、Fatigue 等已触发程序。
10. **回到玩家**：呈现可观察结果与新的选择空间。

### 4.2 地城循环

调用 `EX-DUNGEON`，严格按：
`Describe → Declare → Resolve → Record → Event Check → Next Cycle`

每个 Cycle 都要判断是否触发 `EX-DUNGEON-EVENT`。维护当前地点/区域、Cycle 计数、光源、行动耗时、噪音和事件触发原因。Loss 必须先解决再继续；Exhaustion 选择 Rest 时建立新的独立 Event Roll。不要在事件已触发时静默跳过，也不要把一次触发重复计算。

### 4.3 荒野循环

调用 `EX-WILDERNESS`：
1. 读取当前 Watch（Morning / Afternoon / Night）、Point、目的地、队伍分组和各角色本 Watch 已使用的行动。
2. 核算旅行 Watch 成本：路径距离 + 路径类型 + 地形 + 天气 + 队伍状态；特别广阔地形可额外 +0 至 +2 Watches。每项修正须记录来源，不得重复叠加同一因素。
3. 每名角色本 Watch 选择一项 Wilderness Action。Travel 通常由整个队伍共同执行，作为一次队伍行动；Explore / Supply 等可由一名或多名角色参与。
4. Travel 开始时建立唯一 travel_id，记录路线、总 Watches、已完成 Watches、当前 Point/路段、迷路检定与修正；掷 1d6 判断迷路，并应用路径基础风险及地图、技能、向导等修正。若迷路，按官方程序决定是否需要额外 Wilderness Action 找回路线；不得在同一 travel_id 的 Session 恢复时重掷迷路骰。
5. 处理行动结果，按程序掷 Wilderness Events；夜间旅行必须掷两次。每个 Wilderness Cycle 记录唯一 cycle_id 与 Event Roll ID，恢复时不得重复掷同一 Cycle 的事件。
6. 每推进一个 Watch，记录 Watch 消耗、地点/路线进度、口粮使用次数、光源、Fatigue、Deprived 和其他资源变化。多 Watch 行程不得在第一 Watch 就提前把队伍移动到最终 Point；只有完成所需旅程进度后才提交抵达。
7. 每日最后一个 Watch 通常安排 Make Camp：每名角色及坐骑消耗 1 Ration（按每份 3 uses 的口粮账本扣 1 use），安排守夜；能够休息者清除全部 Fatigue。
8. 若跳过 Make Camp，每名角色增加 1 Fatigue 并进入 Deprived；睡眠不足旅行时地形难度提高一级。若 Deprived 超过一天，再按 CR-FAT 逐日增加 Fatigue；记录 deprived_since 与每次已结算的 fatigue_tick_id，跨 Session 不重算已结算日期。

核心路径、距离、地形、天气与迷路基础值已在 CORE_RULES_RUNTIME.md 本地核准；仅当具体地图路线、沿途地形/天气变化或向导/地图/坐骑等特殊修正未记录时，才定向回查官方表格或 Campaign Quick Reference。不得凭印象填值。单人队伍的守夜安排必须显式裁定，不得默认凭空存在守夜人。

### 4.4 战斗循环

调用 `CR-COMBAT`，按以下顺序：
1. 确认战斗参与者、位置、环境、武器/护甲、特殊能力。
2. 首轮对每名 PC 检查 DEX Save（规则豁免除外）。
3. PC 声明行动。
4. 对手声明行动。
5. 同一方行动结算时，保留行动同时发生的规则含义，不用叙述顺序随意取消行动。
6. 对每次攻击调用 `CR-ATTACK`，需要时调用 `CR-MOD`、`CR-ARM`、`CR-SCARS` 或 `CR-CRITICAL`。
7. 处理 Morale、Retreat、Blast、Detachments 与特殊能力。
8. 更新 HP、属性、Armor、位置、条件、死亡/稳定状态。
9. 进入下一轮，直至战斗结束或一方撤离。

### 4.5 休息与营地

必须区分：
- 短暂休息 + 饮水：HP 恢复；
- 地城 Turn Rest：需要光源与安全地点，可恢复全部 HP，不清除 Fatigue；
- 荒野 Make Camp：消耗口粮，处理守夜/睡眠，符合条件者清除 Fatigue；
- Deprived：阻止 HP、属性与 Fatigue 恢复；超过一天按规则增加 Fatigue；
- 属性恢复：独立于 HP 恢复，通常需要一周休息与适当治疗支持。

不可把这些合并成通用“长休/短休”。

## 5. 运行时状态提交协议

每次有机制影响的行动后，记录：

| 字段 | 内容 |
|---|---|
| Before | 行动前相关状态 |
| Trigger | 触发的规则 ID 与原因 |
| Inputs | 使用的属性、骰值、伤害骰、Armor、时间、物品等 |
| Resolution | 中间步骤与最终结果 |
| Delta | 实际状态变化 |
| Follow-up | 新触发的 Scars、Critical Damage、Morale、Event、Deprivation 等 |
| After | 行动后相关状态 |
| Source | SOURCE / TABLE_ADAPTATION / GM_INFERENCE / UNKNOWN |

提交前执行：
- 库存格是否超过 10；Fatigue 是否占格；背包容量是否正确；
- HP 是否恰好 0 或低于 0，是否调用正确分支；Scars 只因攻击伤害使 PC HP 恰好降至 0；库存满格、Panic 等非攻击效果造成 HP=0 不触发 Scars；hp_zero_cause 是否正确；Critical Damage 是否先扣溢出 STR，STR 归零是否先于 Save 判死；
- Panic 状态是否独立记录：Panicked 角色 HP 降至 0、首轮不行动、攻击 Impaired，须在自己回合以行动 + WIL Save 克服；解除 Panic 不自动恢复 HP；
- 陷阱是否先呈现谨慎观察可发现的信息；陷阱伤害是否按属性伤害处理，并仅在虚构情境适用时扣 Armor；
- 光源是否记录点燃次数、油罐使用、当前点燃状态与环境熄灭；Ration 是否按 3 uses 维护并逐次扣减；
- Critical Damage 是否先扣溢出 STR 再以新 STR Save；
- Armor 是否仅减伤一次，是否遵守 3 上限；
- 时间是否推进，是否触发地城/荒野事件；
- Deprived 是否影响恢复；是否到了增加 Fatigue 的时间；deprived_since 与 fatigue_tick_id 是否避免重复结算；
- NPC/敌方士气是否因本次事件触发；
- 同一事件是否重复结算；pending_effects 是否正确创建、等待、触发、消费并跨 Session 保留；
- 角色知识是否有来源，NPC 是否获得了不应知晓的信息。

若状态差分无法解释，暂停后续依赖该状态的结算，先修复账本；不得通过叙事跳过不一致。

## 5-A. 状态事务与延迟效果生命周期

本节定义 Workbench 状态持久化方式，不增加 Cairn 官方机制。官方规则决定效果；本节确保同一效果只应用一次，并能跨 Session 恢复。

### A.1 原子事务与幂等

每个改变游戏状态的行动/事件必须有唯一 event_id。提交前保留 before、trigger、inputs、resolution、delta、after、commit_status（prepared / committed / blocked）与 source_class（SOURCE / TABLE_ADAPTATION / GM_INFERENCE / UNKNOWN）。

同一 event_id 已是 committed 时，恢复只读取结果，不重复执行 delta。若事务 prepared 但未 committed，先检查外部状态是否已部分落账；无法确认时暂停该事务，禁止盲目重放。

### A.2 HP=0 原因与伤害事务

Runtime State 至少记录 hp_zero_cause: damage_scars | panic | inventory_overload | other_rule | null。伤害结算按 CR-DAMAGE-TX 执行；Panic/Inventory Overload 等直接设置 HP=0 的规则不创建伤害事务，不触发 Scars。解除 Panic 或腾出库存格不自动回填 HP；正常 HP 恢复另建事件。

### A.3 持续条件与待处理效果

将状态分为 ongoing_conditions（当前生效条件）与 pending_effects（已产生但尚未达到结算时点的后续效果）。例如 Panicked、Deprived、Broken Limb、Hamstrung、Deafened、Mortal Wound、稳定/爬行状态属于持续条件；Scars 的“恢复后掷骰/增加最大值”、Doomed 的下一次 Critical Damage Save 属于待处理效果。

每条 pending_effect 至少包含 effect_id、source_event_id、source_rule_id、actor_id、effect、trigger_condition、due_when、status（pending / ready / consumed / expired / cancelled）、created_at、consumed_at、resolution_event_id、source_class 与必要说明。

**生命周期**
1. 触发时先创建 ongoing condition / pending effect，再提交本次 Scars/事件结果。
2. 条件尚未满足时保持 pending；不得提前掷后续成长骰或移除伤势。
3. 条件满足时转为 ready，创建新的 resolution event。
4. 完成效果后记录骰值、状态差分、consumed_at 与 resolution_event_id，再转为 consumed。
5. Handoff 原样保存所有 pending/ready 项；恢复时先核对状态，不重掷、不重复应用。
6. 只有明确规则条件满足或用户批准的桌面处理才能取消/过期；不得因 Session 结束而清空。

### A.4 Scars 延迟效果映射

即时伤势与后续成长分开保存：
- Lasting Scar / Rattling Blow：部位/即时状态和 1d6 最大 HP 检查在本次 Scars 事务内完成。
- Walloped：Deprived 持续至休息数小时；满足恢复条件后执行 1d6 最大 HP 增加。
- Broken Limb：骨折持续至治愈；治愈后执行 2d6 最大 HP 检查。
- Diseased：疾病持续至痊愈；痊愈后执行 2d6 最大 HP 检查。
- Reorienting Head Wound：属性骰在触发时完成并记录，不延迟。
- Hamstrung：行动/移动限制持续至严肃帮助与休息；恢复后执行 3d6 最大 DEX 检查。
- Deafened：失聪持续至获得非凡援助；WIL Save 与最大 WIL 增加按官方表执行。
- Re-brained / Sundered：依官方条目即时执行的骰与条件分别记录。
- Mortal Wound：Deprived、失去行动能力及一小时救治时限必须持续保存；恢复后执行 2d6 最大 HP。
- Doomed：保存 next_critical_damage_save 触发器；只绑定下一次 Critical Damage Save，普通 Save 不消费；成功/失败后消费。

以上只规范化官方 Scars 表中的延迟条件，不创造额外恢复方式。若恢复条件无法客观确认，保持 pending 并记录 UNKNOWN。

### A.5 Deprivation、Fatigue 与口粮账本

- deprived_since 记录本次持续 Deprived 的游戏内起点；deprivation_causes[] 记录食物、睡眠或其他缺失原因。
- 跳过 Make Camp 造成的即时 Fatigue 与 Deprived 是一个有来源的事件；之后超过一天的 Deprived 依 CR-FAT 继续逐日增加 Fatigue，不把即时 Fatigue 误算成第一天的周期 tick。
- 每次周期 Fatigue 增加使用唯一 fatigue_tick_id；同一时间边界不得重复结算。
- 每份 Ration 记录 uses_remaining: 0..3；Make Camp 每名角色/坐骑消耗一次 use。use 降至 0 才移除该份 Ration。
- 角色恢复需求后记录 deprivation_ended_at；恢复 Fatigue 仍须满足官方安全休息条件。Deprived 期间不恢复 HP、属性或 Fatigue。

### A.6 多 Watch 旅行

每个行程维护 travel_plan：travel_id、起点/目标、路径分段、各项惩罚来源、total_watch_cost、watches_elapsed、watches_remaining、迷路骰值/修正/结果、当前 Point/路段、额外找路 Action、待处理 Wilderness Event 与 status（planned / travelling / delayed / lost / arrived / abandoned）。

每次 Wilderness Cycle 只提交本 Cycle 已完成的进度和事件；未完成总 Watch 成本前不得提交抵达最终 Point。天气或地形变化影响剩余路段时，记录新依据并重新计算剩余成本，不追溯改写已完成的 Watch。Travel 检定与每个 Cycle 的 Event Roll 使用不同 ID；Session 恢复不能重掷已提交骰。

### A.7 Dungeon Event 后续程序

- Loss：记录具体失去/失效对象与范围；必须先解决影响（例如火把熄灭、持续法术失效），才能继续后续 Cycle。
- Exhaustion：必须明确选择官方选项之一：休息（并立即再次掷 Dungeon Events）、增加 Fatigue、或消耗一份 Ration。若选择休息，新的 Event Roll 是新的独立事件；若再次掷出 Exhaustion，继续按规则处理，直到当前事件后续选择完成。
- 每次 Event Roll 与其 follow-up 使用独立 ID；不得因递归事件覆盖父事件，也不得重复扣口粮/疲劳。

### A.8 Wilderness Event 后续程序

- Loss：呈现资源、时间或努力成本，并记录选择与实际差分；不套用 Dungeon Loss 的具体表述。
- Exhaustion：记录障碍及其代价；按情境需要额外时间/额外 Wilderness Action 或增加 Fatigue。不可自动把 Dungeon Exhaustion 的三选一程序套过来。
- 每个 Wilderness Cycle 后按程序掷事件；夜间旅行掷两次。每个骰各有唯一 Event Roll ID。
- Discovery 按官方程序可发现食物、宝藏或其他有用资源；Warden 可改为揭示区域主要特征。结果必须与地图和既有事实相容。

## 6. 官方原文回查策略

**不需要每次上网查的项目**：已标记 VERIFIED_CORE、当前版本未变、没有特殊能力/模组覆盖、且运行输入完全落在规则摘要范围内的常规规则。

**必须回查的情况**：
- 本手册标记 PARTIAL / MODULE_DEPENDENT；
- 本地速查未覆盖的 Scars 例外、表格版本冲突或具体措辞争议；
- 涉及法术、遗物、特殊武器、怪物、雇工、Detachments；
- 本地速查未覆盖的特殊路线修正、地图数据或向导/坐骑/技能特例；
- 模组特殊规则、裁定例外或本手册未覆盖的规则；
- 玩家质疑裁定、规则之间出现冲突；
- 规则版本更新或 Campaign Binding 改变；
- 高后果、不可逆、可能致命的边界情况，且本地速查未给出完整步骤、适用例外或来源版本无法确认。已完整规范化的 STR 归零死亡、Critical Damage 与 Scars 结果不因“高后果”而每次重复联网检索。

回查时记录：官方页面/章节、核对日期、影响的 Rule ID、是否修订速查。查到一次并完成核验后，应把稳定结论规范化回规则库，避免下次重复搜索。

## 7. 规则缺口处理

遇到缺口时：
1. 标记具体问题为 `UNKNOWN` 或 `DISPUTED`。
2. 指明受影响的 Rule ID、行动和需要的最小信息。
3. 检索官方 2e 对应章节/表格。
4. 若仍无明确规定，区分官方明确留白与当前未找到。
5. 只对依赖该问题的行动暂停或采用明确标注的 GM_INFERENCE；其余游戏继续。
6. 需要形成桌规时，先向用户说明影响并取得批准。
7. 将核验结论、来源和测试案例回写规则库。

严禁用 Cairn 1e 或其他系统相似规则补洞。

## 8. Session Handoff

每次暂停/结束时输出最小运行快照：
- system_id / ruleset_version / Campaign / Module；
- 当前游戏内时间、地点、探索阶段/Watch/Cycle/Combat Round；
- PC 与重要 NPC 状态；
- 库存、Fatigue、口粮、光源与其他消耗；
- 已发生但未结算的规则触发；
- ongoing_conditions、pending_effects（含状态、触发条件、到期条件与已消费记录）；
- 未完成事务与其 event_id / commit_status；
- Deprivation 起点、Fatigue tick、口粮 uses_remaining；
- travel_plan（已用/剩余 Watches、迷路检定与待处理事件）；
- 正在进行的行动与 NPC 事务；
- 已作出的 TABLE_ADAPTATION / GM_INFERENCE；
- 未解决 UNKNOWN / DISPUTED；
- 下次恢复时首先执行的检查。

不把现实时间间隔当作游戏时间推进依据。
