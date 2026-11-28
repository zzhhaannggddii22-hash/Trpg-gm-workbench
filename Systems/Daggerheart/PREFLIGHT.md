# 开团前核验（Preflight）

> 系统：daggerheart  
> 默认规则集：Daggerheart Core Set  
> 默认扩展范围：CORE_ONLY  
> 当前系统状态：candidate；本文件为 Preflight 草案，尚未验收。

Preflight 用于在任何正式 Session 开始前确认规则、资料、角色状态与主持条件。完成 Preflight 不等于自动开始游戏；只有用户明确说“开始”后才进入正式场景。

## 1. Campaign Binding

- [ ] 存在独立的 SYSTEM_BINDING.md。
- [ ] system_id 为 daggerheart，规则版本明确为 Core Set 或明确指定的版本。
- [ ] 官方 SRD / Core Rulebook 版本与已采用的 Errata 已记录。
- [ ] 扩展范围明确；默认 CORE_ONLY。若启用 Hope & Fear，逐项列明，不用“整套扩展”含混授权。
- [ ] 任何桌面适配与可选规则都有明确记录及用户批准。
- [ ] 这是新 Campaign / 新 Session / Candidate 测试，不继承其他系统角色卡或状态。

## 2. 规则资料与版本

- [ ] 读取 Systems/Daggerheart/README.md。
- [ ] 读取当前版本对应的 CORE_RULES_RUNTIME.md、LOOKUP_TABLES.md 与 CORE_RULE_INDEX.md。
- [ ] 角色、卡牌、敌人、环境和装备数据优先从本地 Reference_Data/Core_Set/ 检索。
- [ ] 若本次使用的规则包含未核实条目，先检查 RULE_ISSUES.md。
- [ ] 检查官方 Core Errata 是否有新增版本；只在版本改变或具体条目未核实时回查。
- [ ] 不把 Mixed_Version/、Optional_Procedures/ 或 Hope_and_Fear/ 自动加载到基础游戏。

## 3. PC 与队伍

- [ ] 所有 PC 的职业、子职业、Ancestry、Community、六项 Traits 已确认。
- [ ] Evasion、HP、Stress、Hope、Proficiency、Level、Tier 已按 Core 规则计算。
- [ ] 两个 Experiences 的名称、适用范围与 +2 修正已确认；避免过于宽泛或直接给予超常能力。
- [ ] Active Weapons、Armor、Armor Score、Damage Thresholds、Inventory、Gold、Consumables 已核对。
- [ ] Domain Loadout 最多 5 张；Vault 与 Recall Cost 记录清楚。
- [ ] 每张领域卡的级别、职业领域归属、使用次数和刷新条件已核验。
- [ ] 单人队伍或特殊人数配置已明确标注；不自动补入 NPC 队友资源。

## 4. 场景与模组

- [ ] 模组/战役资料来源、版本、许可和使用范围明确。
- [ ] 场景入口、角色可知信息、NPC 动机、威胁与至少一个可行动目标已准备。
- [ ] 若有战斗，检查 Battle Points、敌人 Tier/Type、目标、场地、危险和退出路径。
- [ ] 环境 Feature、敌人 Action / Reaction / Passive / Fear Feature 的触发条件与资源成本清楚。
- [ ] Countdown 有类型、起始值、推进条件、触发结果和状态记录方式。
- [ ] 为需要的信息设置多个可行调查/互动路径，不把唯一线索或单一成功检定作为硬锁。

## 5. 运行状态

- [ ] 当前 PC / NPC / Enemy 状态快照已建立。
- [ ] Hope 与 Fear 资源初始值正确；Campaign 开始时 GM Fear = PC 数量（每名 PC 1 Fear）；Fear 上限 12。
- [ ] HP、Stress、Armor Slots、Conditions、Countdown、使用次数和延迟效果可追踪。
- [ ] 已明确休息次数、上次 Short / Long Rest 与待刷新效果。
- [ ] 关键敌人的共享 Pool / Evolution / Token 状态有记录。
- [ ] 当前时间、地点和场景危险有足够记录，不模拟与结果无关的琐碎时间。

## 6. GM 准备

- [ ] 阅读 GM_SKILL.md，确认场景叙事与规则运行边界。
- [ ] 场景以局势和动机为主，不预写固定剧情。
- [ ] GM Moves 与 Fear 消耗有明确叙事目的。
- [ ] 玩家知道角色可观察到的事实与主要风险。
- [ ] 无需检定的行动不强制掷骰；有意义的掷骰先说明赌注。
- [ ] 玩家重要选择、角色行为与 NPC 信息权限得到尊重。

## 7. 信息隔离与版权

- [ ] GM-only 信息与玩家可见信息分离。
- [ ] 不把角色未知信息作为玩家已知。
- [ ] 不在公开输出中泄露隐藏 Stat Block、幕后动机或模组解答，除非角色已取得。
- [ ] 不把商业 Core Rulebook 未公开正文、地图、插画或 Campaign Frame 全文写入公开仓库。
- [ ] 公开 SRD 数据按 DPCGL 2.0 署名；私人资料仍遵守实际取得许可。

## 8. 开始门槛

Preflight 完成后，向用户简要报告：
- 采用规则版本与扩展范围；
- PC / 队伍状态是否就绪；
- 本次场景的主要风险与规则缺口；
- 尚未解决的 UNKNOWN / DISPUTED。

**等待用户明确说“开始”后，才进入正式游戏场景。**
