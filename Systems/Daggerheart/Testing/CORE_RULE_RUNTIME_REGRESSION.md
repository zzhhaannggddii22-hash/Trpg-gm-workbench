# Core Rule Runtime Regression Matrix

> 状态：PARTIALLY EXECUTED / DESK TEST  
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

## 测试执行记录

| 字段 | 当前值 |
|---|---|
| 测试版本 | Core Set / SRD 2.0 (2026-08-25) |
| 扩展范围 | CORE_ONLY |
| 矩阵状态 | DESK-SIMULATED (45/45; NOT AUTOMATED) |
| 已执行测试 | 45 / 45 (desk simulation) |
| 已通过 | 45 (desk simulation) |
| 已失败 | 0 |
| 阻塞 | 0 |

本矩阵仍是测试清单兼状态记录。DH-T01–DH-T45 的桌面模拟输入与结果见 DESK_TEST_BATCH_01.md、DESK_TEST_BATCH_02.md、DESK_TEST_BATCH_03.md。桌面逻辑模拟不等同于代码自动测试或完整规则书验收。盲测、短场景主持测试与完整 Core Rulebook 对照仍待完成。
