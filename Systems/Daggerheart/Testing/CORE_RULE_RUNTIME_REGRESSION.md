# Core Rule Runtime Regression Matrix

> 状态：DH-T01–T45 与 DH-GM-01–10、DH-GD-01–09 共 64/64 DESK-SIMULATED；参考执行器最近一次可核验记录为 42/42，当前脚本 51 项（新增 9 项待复跑）；LIVE RUNTIME VALIDATION PENDING  
> DH-T01–DH-T45 已进行确定性桌面逻辑模拟（非代码自动测试）。详情见三个 DESK_TEST_BATCH 文件。

| ID | 场景 | 预期结果 / 关键断言 | 类型 |
|---|---|---|---|
| DH-T01 | Action Roll 总值高于 Difficulty，Hope Die 高于 Fear Die | Success with Hope；PC +1 Hope；不自动触发 GM Fear Move | Static |
| DH-T02 | Action Roll 总值高于 Difficulty，Fear Die 高于 Hope Die | Success with Fear；GM +1 Fear；成功仍成立，同时有代价/复杂状况 | Static |
| DH-T03 | Action Roll 总值低于 Difficulty，Hope Die 较高 | Failure with Hope；PC +1 Hope；GM Move 产生较轻后果 | Static |
| DH-T04 | Action Roll 总值低于 Difficulty，Fear Die 较高 | Failure with Fear；GM +1 Fear；产生重大后果 | Static |
| DH-T05 | Duality Dice 点数相同 | Critical Success；自动成功、PC +1 Hope、清除 1 Stress；攻击另加暴击伤害 | Synthetic |
| DH-T06 | Reaction Roll 出现 Hope/Fear 高低差 | 不产生 Hope / Fear，不触发额外 GM Move | Static |
| DH-T07 | Reaction Roll Critical Success | 忽略该次本会承受的影响；不获得 Hope，也不清除 Stress | Static |
| DH-T08 | 角色所有 Stress Slots 已标记，再受到要求标记 Stress 的后果 | 依通用 Stress 规则改标记 1 HP；记录触发来源 | Synthetic |
| DH-T09 | 角色所有 Stress Slots 已标记，尝试使用明确要求支付 Stress 的 Move | 不能使用该 Move；不能以改标记 HP 替代 Move 成本 | Static |
| DH-T10 | 角色标记最后一个 Stress | 获得 Vulnerable；至少清除 1 Stress 后解除由满 Stress 产生的 Vulnerable | Synthetic |
| DH-T11 | 一个普通 Advantage 来源加两个 Disadvantage 来源 | 一对一抵消后只掷 1d6 Disadvantage | Static |
| DH-T12 | 多个 PC Help an Ally 同一个 Action Roll | 每名帮助者各掷 Advantage d6；行动者只加所有相关优势骰中的最高值 | Synthetic |
| DH-T13 | Group Action 中一个协助者 Reaction 成功、另一个失败 | 领头者 Action Roll 修正净值 +0；协助者 Reaction 不产生 Hope/Fear | Synthetic |
| DH-T14 | Tag Team Roll 两组骰均已完成，选择其中一组应用 | 只将选定结果应用于协同动作；Hope/Fear 按参与 PC 人数结算；Countdown 只计一个 Action Roll | Synthetic |
| DH-T15 | Tag Team 成功攻击且两名 PC 伤害类型不同 | 合并伤害总值作为单一来源；由参与玩家选择最终伤害类型 | Static |
| DH-T16 | PC 对 Adversary 发起攻击 | Attack Roll 的 Difficulty 等于目标 Adversary Difficulty | Static |
| DH-T17 | Adversary 标准攻击 PC | GM 使用 d20 + Attack Modifier 与 PC Evasion 比较；不使用 Duality Dice | Synthetic |
| DH-T18 | Adversary 进行未写明检定的普通动作，PC 可影响其结果 | 默认不为敌人额外掷 Action Roll；由相关 PC Reaction Roll 应对 | Static |
| DH-T19 | Adversary 进行与 PC 无关的高风险戏剧性动作 | GM 可按规则用单 d20 对 Difficulty 检定；需要时先花 Fear 加相关 Experience | Static |
| DH-T20 | PC 最终伤害低于 Major Threshold | 标记 1 HP；若伤害降至 0 或以下则不标记 HP | Synthetic |
| DH-T21 | PC 最终伤害达到 Major、低于 Severe | 标记 2 HP | Synthetic |
| DH-T22 | PC 最终伤害达到 Severe | 标记 3 HP；若启用 Massive Damage 可另按可选规则判 4 HP | Synthetic |
| DH-T23 | PC 用 Armor Slot 降低 Severe 伤害一级 | Severe→Major，仍标记 2 HP；不得再次用同一 Slot 减伤 | Synthetic |
| DH-T24 | Adversary 对物理伤害有 Resistance，后续还可以标记 Armor Slot | 先应用 Resistance，再比较阈值/执行 Armor 减伤 | Synthetic |
| DH-T25 | Direct Damage 命中 PC | Armor Slot 不能降低 Direct Damage；仍按该效果规则结算 | Static |
| DH-T26 | 多个来源同时造成伤害 | 同时伤害先合计，再比较 Damage Threshold | Synthetic |
| DH-T27 | PC 在危险中进行 Action Roll，移动至 Close 内位置 | 可将移动包含在该行动中；不能把这项规则扩大到无检定移动 Very Far | Static |
| DH-T28 | 角色获得 Hidden 后攻击 | 攻击结束后失去 Hidden；若是 Cloaked 等特殊状态，按其特性文本处理 | Static |
| DH-T29 | PC 拥有超过五张 Domain Cards | Loadout 最多 5 张，其余在 Vault；子职业、Ancestry、Community 卡不占该上限 | Static |
| DH-T30 | PC 非休息期间从 Vault 调回领域卡 | 支付该卡 Recall Cost 对应 Stress；若 Loadout 已满，另移一张到 Vault | Synthetic |
| DH-T31 | 连续进行第三次 Short Rest 后再尝试 Short Rest | 下次必须 Long Rest | Static |
| DH-T32 | Short Rest 被敌人打断 | 本次不获得 Short Rest 收益；不得继续应用 Downtime Moves | Static |
| DH-T33 | Long Rest 被敌人打断 | 只能获得 Short Rest 收益；不得结算 Long Rest 专属效果 | Static |
| DH-T34 | Long Rest 恢复 Fear | GM 获得 1d4 + PC 数量 Fear；上限为 12 | Synthetic |
| DH-T35 | Standard Countdown 存在时一次 Action Roll 结算 | 每次 Action Roll 推进一次；同一事务不能重复推进 | Synthetic |
| DH-T36 | Dynamic Countdown 遭遇不同结果 | 按 Progress / Consequence 推进表分别推进；不能把两个方向混用 | Synthetic |
| DH-T37 | Enemy Fear Feature 需花 Fear，且此前 GM 已花 Fear 抢夺 Spotlight | Fear Feature 成本另行支付；不能认为抢夺 Spotlight 的花费已覆盖 | Static |
| DH-T38 | 两个 Adversaries 使用共享 Pool | Token 进入共享 Pool，不放入某个敌人独立卡；场景结束清空 | Synthetic |
| DH-T39 | Enemy Evolution 触发一次后再次满足条件 | 同一场景不得再次触发该 Evolution，除非 Stat Block 明确规定 | Static |
| DH-T40 | PC 标记最后一个 HP | 立即选择并执行 Blaze of Glory / Avoid Death / Risk It All 之一 | Synthetic |
| DH-T41 | Campaign Binding 为 Core Only，尝试创建 Assassin / Brawler / Warlock / Witch | 角色创建数据拒绝扩展职业；不得从混合章节误载 | Static |
| DH-T42 | Campaign Binding 为 Core Only，尝试选取 Dread Domain | 不得选取 Dread 领域或其卡牌 | Static |
| DH-T43 | 角色尝试装备高于自身 Tier 的武器/护甲 | 不允许装备，除非有明确规则覆盖 | Static |
| DH-T44 | 同时有多个相同类型 Resistance | 抵抗不叠加；只按规则应用一次 | Synthetic |
| DH-T45 | Hope Feature 需要 3 Hope，Action Roll 结果获得 1 Hope | 该次获得的 Hope 可立即用于同次行动的 Hope Feature；其他未声明资源不得事后补加 | Synthetic |

## GM Move / Fear / Spotlight 专项回归（桌面模拟完成）


| DH-GM-01 | Success with Fear，但现场没有敌人 | PC 成功；GM 获得 Fear；选择与现场相符的非攻击 Move | Desk-Simulated |
| DH-GM-02 | Failure with Hope | PC 失败并获得 Hope；GM 采取较轻 Move；不得额外生成 Fear | Desk-Simulated |
| DH-GM-03 | Critical Success | PC 获得 Hope、清除 Stress；不触发 Fear 收入或额外 GM Turn | Desk-Simulated |
| DH-GM-04 | Reaction Roll Critical | 不获得 Hope、不清除 Stress；按 Reaction Roll 规则忽略该次影响 | Desk-Simulated |
| DH-GM-05 | GM 花 Fear 抢夺 Spotlight 后启用 Fear Feature | 两笔成本分别支付 | Desk-Simulated |
| DH-GM-06 | GM 额外 Spotlight 第二名敌人 | 每次额外敌人 Spotlight 按规则支出；第一名敌人行动不自动授权其他敌人 | Desk-Simulated |
| DH-GM-07 | 敌人拥有 Relentless (2) | 按特性在同一 GM Turn 内获得最多两次 Spotlight；额外重复聚焦按规则支付 Fear | Desk-Simulated |
| DH-GM-08 | 12 Fear 时再次获得 Fear | 不超过上限，不产生隐藏溢出 | Desk-Simulated |
| DH-GM-09 | 玩家忽略已预告的环境危险 | GM 可按已建立后果使用 Hard Move；不得改变危险原本的作用范围 | Desk-Simulated |
| DH-GM-10 | Hope 结果下出现高强度敌方威胁 | 本次回应优先使用 Soft Move；强硬后果需由独立触发或已成立的不可避免后果支持，不得作为本次 Hope 结果的默认回应 | Desk-Simulated |

以上 10 项已完成桌面逻辑模拟，详情见 [GM_DESK_SIMULATION_01.md](./GM_DESK_SIMULATION_01.md)。这不是代码自动测试或真实桌面验收。专项设计依据见 [GM_RUNTIME_FIELD_GUIDE.md](../GM_RUNTIME_FIELD_GUIDE.md)。


## GM 设计 / 遭遇运行专项回归（桌面模拟完成）

| ID | 场景 | 预期结果 / 关键断言 | 状态 |
|---|---|---|---|
| DH-GD-01 | Success with Fear：玩家成功打开锁门，但巡逻队接近 | 门已打开；后果推动巡逻压力，不得把开门改判为失败 | Desk-Simulated |
| DH-GD-02 | Success with Fear：角色成功说服守卫放行，但守卫记住其面孔 | 放行成功保留；后果是后续关注/身份暴露，不直接撤销许可 | Desk-Simulated |
| DH-GD-03 | Failure with Hope：调查没找到目标证据 | 目标证据未取得；产生可继续推进的轻度变化；不额外增加 GM Fear | Desk-Simulated |
| DH-GD-04 | 战斗中敌人开始蓄力并明确预告攻击 | 玩家获得可理解的回应窗口；若之后兑现，按已建立机制处理 | Desk-Simulated |
| DH-GD-05 | 敌人获得 Spotlight，Motives & Tactics 是“保护祭司、拖延时间” | 优先保护/拖延，而不是默认攻击最近 PC | Desk-Simulated |
| DH-GD-06 | Reaction 的触发条件满足，但敌人当前没有 Spotlight | Reaction 仍按其触发条件结算；不要求敌人获得行动聚焦 | Desk-Simulated |
| DH-GD-07 | GM 试图无成本打断玩家当前 Spotlight | 不将“可在 GM Turn 中自由作 Move”误读为无成本抢夺玩家 Spotlight；打断时按 Fear 规则支付 | Desk-Simulated |
| DH-GD-08 | Environment Feature 造成烟雾遮蔽与路线改变 | 场景提供新的行动选择；不把环境 Feature 一律转换成伤害 | Desk-Simulated |
| DH-GD-09 | Success with Fear：行动成功但后果直接兑现 | 主要成果保留；后果严重度仍为次要，但可以采用 Hard Move 形式，不得混淆严重度与回应窗口 | Desk-Simulated |

## 参考执行器伤害交互回归（代码用例；新增部分待自动复跑）

| ID | 场景 | 关键断言 | 状态 |
|---|---|---|---|
| DH-REF-043 | Direct Damage 同时受到 Resistance | Resistance 仍减半；Direct 只绕过 Armor Slot | Pending rerun |
| DH-REF-044 | Resistance 与 Armor Slot 同时存在 | 先减半、向上取整，再按严重度标记；Armor 再降低一级 | Pending rerun |
| DH-REF-045 | 同类型 Resistance 有多个来源 | Resistance 不叠加，只减半一次 | Pending rerun |
| DH-REF-046 | 单一类型伤害命中 Immunity | 对应伤害归零，不标记 HP | Pending rerun |
| DH-REF-047 | 混合伤害只抵抗其中一种类型 | 不得只减免其中一部分；整体不享受该防护 | Pending rerun |
| DH-REF-048 | 混合伤害两种类型均有 Resistance | 两种类型分别减半并向上取整，再合计比较阈值 | Pending rerun |
| DH-REF-049 | 同时发生的同类型多来源伤害 | 先合计伤害，再比较阈值 | Pending rerun |
| DH-REF-050 | 混合伤害两种类型均有 Immunity | 两种类型伤害均忽略 | Pending rerun |
| DH-REF-051 | 混合伤害分别受到 Resistance 与 Immunity | 两种类型均有防护时，分别应用对应防护再合计 | Pending rerun |

## 自动化参考执行补充

独立参考执行器最近一次有记录的执行为 42/42 通过，见 `AUTOMATED_REFERENCE_EXECUTION_01.md`。之后新增 9 项伤害交互回归（当前脚本共 51 项，新增 DH-REF-043–051）；本次修改后的自动化重跑尚未取得可核验结果，因此仍按 42/42 作为最后一次已验证成绩，新增 9 项均标记待复跑。这些测试验证独立参考执行器与 Core Set 数据，不是生产 GM Runtime 的端到端测试。

## 测试执行记录

| 字段 | 当前值 |
|---|---|
| 测试版本 | Core Set / SRD 2.0 (2026-08-25) |
| 扩展范围 | CORE_ONLY |
| 矩阵状态 | 64/64 项已桌面逻辑模拟；42/42 参考执行器历史自动化测试通过；9 项新增伤害回归待复跑 |
| 已执行测试 | 64 / 64（桌面逻辑模拟）；参考执行器最新可核验记录 42/42；当前脚本 50 项 |
| 已通过 | 64（桌面模拟）；42（参考执行器历史记录） |
| 已失败 | 0 |
| 待执行 | 0（桌面模拟层面）；9（新增自动化回归待复跑） |
| 阻塞 | 0 |

本矩阵仍是测试清单兼状态记录。DH-T01–DH-T45 的桌面模拟输入与结果见 DESK_TEST_BATCH_01.md、DESK_TEST_BATCH_02.md、DESK_TEST_BATCH_03.md；新增 19 项见 GM_DESK_SIMULATION_01.md。桌面逻辑模拟不等同于代码自动测试或完整规则书验收。盲测、短场景主持测试与完整 Core Rulebook 对照仍待完成。
