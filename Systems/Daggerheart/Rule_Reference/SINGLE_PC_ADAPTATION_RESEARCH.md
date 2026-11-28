# 单人 PC 适配研究｜非默认规则

> 状态：DESIGN NOTE / NOT RULES-AS-WRITTEN  
> 适用范围：仅当 Campaign 明确采用 1 名玩家角色（1 PC）时参考。  
> 基准：Daggerheart Core Set；Official SRD v2.0（2026-08-25）；默认不启用 Hope & Fear。

## 1. 核心结论

Daggerheart SRD 对游戏人数的基础描述是 1 名 GM、2–5 名玩家。单 PC 冒险因此不属于 SRD 明确描述的标准人数配置。单人游戏可以尝试，但必须把它视为 Campaign 级桌面适配，并通过短场景验证；不能把“Solo adversary”误读成“单人玩家模式”。

本文件只定义适配边界和测试方法，不擅自修改 Core 数值。

## 2. 明确受到队伍人数影响的机制

| 机制 | 官方基础规则中的人数依赖 | 单 PC 运行注意 |
|---|---|---|
| Group Action | 多名 PC 共同完成行动；一名 Leader 掷 Action Roll，其余参与者各掷 Reaction Roll | 只有一名 PC 时没有其他 PC 协助者；不得凭空生成协助检定或免费 +1 |
| Tag Team Roll | 两名 PC 协同；每名玩家每 Session 可发起一次，支付 3 Hope | 单 PC 无法按原文完成；不能让 NPC 自动冒充 PC 取得相同规则收益 |
| Connections | 角色关系环节主要围绕 PC 与其他 PC 建立 | 可改为 PC 与关键 NPC、组织或重要地点建立关系锚点；明确标记为桌面适配 |
| Battle Points | 基础遭遇预算以 (3 × 参战 PC 数量) + 2 起算，并按敌人类型花费 | 公式代入 1 PC 会得到 5 BP，但官方人数范围从 2 PC 起；5 BP 不应直接视作已验证的单人遭遇预算 |
| Long Rest Fear | GM 获得 1d4 + PC 数量 Fear | 1 PC 时按人数项计入 1；其他 Fear 来源和 12 点上限照常处理 |
| 依 PC 数量设定的场景特性 | 部分敌人、环境或倒计时按场景 PC 数量设定目标数、资源或难度 | 必须按实际 PC 数量读取文本；不要把“队伍”泛化为额外 NPC 角色卡 |

## 3. 建议的适配原则

1. **先减场景负荷，不先改角色规则。** 优先减少同时威胁 PC 的敌人数、攻击来源和并行目标；保留敌人原始属性与能力。
2. **避免多敌人轮番压制。** 单 PC 没有其他玩家角色分担 Spotlight、承伤、控制和救援。一次 GM Turn 中同时激活多个敌人，可能形成远高于表面 BP 的行动压力。
3. **NPC 盟友是叙事资源，不自动成为第二名 PC。** NPC 可提供信息、关系、掩护或剧情行动；只有官方规则明确支持的效果才赋予 Advantage 或其他机制。不得自动给予 Group Action、Tag Team、额外 Hope 或额外 HP。
4. **保留玩家对 PC 的完整控制。** NPC 不替玩家决定行动，不替玩家支付资源，也不代替 PC 掷骰承担后果。
5. **维持原始资源时序。** Hope、Fear、Stress、HP、Armor、Countdown 和休息程序仍按 Core 规则；适配不应悄悄赠送资源。
6. **用环境与目标制造压力。** 优先使用地形、时限、保护/撤离/阻止仪式等非击杀目标，避免用单纯堆高伤害弥补人数差异。
7. **明确记录每项桌规。** 任何额外队友、复活援助、遭遇预算折算或资源补偿都必须在 Campaign Binding 单独列出。

## 4. 第一轮单人测试计划

以下用例只用于确定是否需要桌面适配，不代表适配方案已经通过。

| ID | 场景 | 观察重点 | 验收要求 |
|---|---|---|---|
| DH-SOLO-01 | 1 PC 对单个低压敌人 | 攻击与反应频率、Hope/Fear 流转 | PC 能作出多种有效选择，不因单次失误立即进入死亡螺旋 |
| DH-SOLO-02 | 1 PC 对两个敌人 | GM Turn 中敌人连续聚焦的压力 | 不出现 PC 无机会行动、连续承受无法回应的伤害 |
| DH-SOLO-03 | 1 PC + 叙事型 NPC 盟友 | NPC 提供帮助的边界 | 不把 NPC 自动当作 PC 协助者或免费资源来源 |
| DH-SOLO-04 | 1 PC 的探索场景 | 线索路径、危险反应、Countdown | 不因缺少队友专长而出现单一路径硬锁 |
| DH-SOLO-05 | 1 PC 的 Short / Long Rest | 恢复量、Fear 增长、Downtime Moves | 人数相关数值按 1 PC 计算，其他规则无静默变化 |
| DH-SOLO-06 | 1 PC 的最后 HP / Death Move | 角色死亡后果与 Campaign 连续性 | 预先明确死亡、替代角色或战役结束的处理，不临时免除规则 |

## 5. 尚未决定的事项

- 单 PC 遭遇预算是否需要一个专门的折算表：待测试，不预先规定。
- 是否允许固定 NPC 伙伴参与部分战斗：由 Campaign 决定；若参与，需明确其机制权限与 Spotlight 处理。
- 单 PC 是否获得额外初始资源、Hope、HP 或免费优势：默认不提供，除非用户明确批准桌规。
- 起始 GM Fear：已由官方 SRD 2.0 第 86 页确认，Campaign 开始时 GM 获得每名 PC 1 Fear。1 PC Campaign 因此按 1 Fear 初始化；这是原规则，不是单人桌适配。见 [RULE_ISSUES.md](./RULE_ISSUES.md) 的 DH-I-018。

## 6. 官方依据

- 官方 SRD 2.0 第 2 页：游戏人数描述为 1 GM、2–5 players。
- 官方 SRD 2.0 第 47–48 页：Group Action、Tag Team Roll、Help an Ally 的规则。
- 官方 SRD 2.0 第 90 页：Standard / Dynamic Countdown 规则。
- 官方 SRD 2.0 第 93 页：Battle Points 遭遇预算公式及敌人类型点数。
- 官方 SRD 2.0 第 52 页：Short Rest / Long Rest 与 Fear 增量。
- 官方 SRD 2.0 第 103 页等敌人 Stat Block：Solo 是 Adversary Type，表示敌人类别，不是玩家人数模式。

官方来源：[Daggerheart SRD v2.0](https://www.daggerheart.com/srd/)。
