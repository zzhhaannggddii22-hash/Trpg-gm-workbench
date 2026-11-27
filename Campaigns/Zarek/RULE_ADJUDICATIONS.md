# Zarek 桌裁启用清单

仅适用于 `triangle_agency`、`中文 v22`、`campaign_id: zarek`，且须由本 Campaign 的 SYSTEM_BINDING 选中。下列批准证据为既有 Zarek Binding 指向的 2026-11-23 本桌用户裁定。适用范围延续原「当前桌面」，不扩到其他 Campaign，也不作为规则勘误。绑定系统/版本改变、用户撤销或有新批准取代时失效。模组特例须明确单列模组、触发条件与批准依据。目前清单没有新启用的模组特例。

```yaml
system_id: triangle_agency
ruleset_version: "中文 v22"
campaign_id: zarek
approved_rules:
  - rule_id: Q01
    scope: CAMPAIGN
    approval_ref: 'Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定'
    effective_from: "2026-11-23"
  - rule_id: Q02
    scope: CAMPAIGN
    approval_ref: 'Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定'
    effective_from: "2026-11-23"
  - rule_id: Q03
    scope: CAMPAIGN
    approval_ref: 'Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定'
    effective_from: "2026-11-23"
  - rule_id: Q04
    scope: CAMPAIGN
    approval_ref: 'Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定'
    effective_from: "2026-11-23"
  - rule_id: Q05
    scope: CAMPAIGN
    approval_ref: "User confirmation in conversation, 2026-11-27"
    effective_from: "2026-11-27"
```

| rule_id | 触发条件 | 本桌执行 | 原文定位 |
|---|---|---|---|
| Q01 | 异常域界的免费混沌效果边界 | 费用 ≤3 免费 | v22 PDF 物理页 182、192 |
| Q02 | 适用域界花费调整，实际产生费用 | 乘以三后向上取整 | v22 PDF 物理页 182–183 |
| Q03 | 角色确实适用人寿保单保障项目 1 且承受多点 Harm | 可用任意素质 QA 防护。剩余 1 Harm 且无其他防护时按已确认口径处理为死亡，不自动计部分抵消 | v22 PDF 物理页 54 |
| Q04 | 当前裁定涉及 QA 和 Burnout 顺序 | 先检查 Burnout，再检查 QA。同次 QA 消耗不在同次检定产生即时 Burnout | v22 PDF 物理页 40–46 |
| Q05 | Time 成长的触发条件与联动字段记账 | 每完成一个完整模组才增加 1 点可使用 Time；Session 结束不自动增加。可使用 Time 增加 n 点时，剩余可用 Time 同步减少 n 点；两个字段分开记录 | 用户于 2026-11-27 明确确认；仅适用于本 Campaign |

[历史裁定和批准依据](../../Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定)


## Q05｜Time 成长触发与联动记账

- **触发时点：** 每完成一个完整模组，增加 1 点可使用 Time；单独结束一个 Session 不触发该奖励。一个模组包含多个 Session 时，只在整个模组结团时结算一次。
- **联动变化：** 每次可使用 Time 增加 n 点，剩余可用 Time 同步减少 n 点。两者是不同字段，变化方向相反，必须分别记账，不得合并或互相替代。
- **余额边界：** 人物卡中“总量 30 / 已花费 2 / 剩余 28”是剩余可用 Time 的轨迹记录，不是当前可使用 Time 的绝对余额。不能由该组数字推算当前可使用 Time。
- **流水要求：** 记录可使用 Time 的前值/增量/后值，以及剩余可用 Time 的前值/减量/后值，并引用同一模组结团事件。若任一前值待核，只记已确认增量，不猜绝对余额。
- **成长用途与购买分离：** 获得 Time 不等于自动购买能力。玩家可指定将其用于哪项成长；实际购买仍需单独确认能力、价格、效果和支付。

本条是用户确认的 Zarek Campaign 桌面约定，不冒充中文 v22 的通用规则，也不得迁移到其他 Campaign。
