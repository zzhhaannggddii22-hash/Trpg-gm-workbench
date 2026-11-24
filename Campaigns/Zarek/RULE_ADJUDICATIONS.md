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
```

| rule_id | 触发条件 | 本桌执行 | 原文定位 |
|---|---|---|---|
| Q01 | 异常域界的免费混沌效果边界 | 费用 ≤3 免费 | v22 PDF 物理页 182、192 |
| Q02 | 适用域界花费调整，实际产生费用 | 乘以三后向上取整 | v22 PDF 物理页 182–183 |
| Q03 | 角色确实适用人寿保单保障项目 1 且承受多点 Harm | 可用任意素质 QA 防护。剩余 1 Harm 且无其他防护时按已确认口径处理为死亡，不自动计部分抵消 | v22 PDF 物理页 54 |
| Q04 | 当前裁定涉及 QA 和 Burnout 顺序 | 先检查 Burnout，再检查 QA。同次 QA 消耗不在同次检定产生即时 Burnout | v22 PDF 物理页 40–46 |

[历史裁定和批准依据](../../Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定)
