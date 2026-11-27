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
  - rule_id: Q06
    scope: CAMPAIGN
    approval_ref: "User confirmation in conversation, 2026-11-27"
    effective_from: "2026-11-27"
```

| rule_id | 触发条件 | 本桌执行 | 原文定位 |
|---|---|---|---|
| Q01 | 异常域界的免费混沌效果边界 | 费用 ≤3 免费，且在 Domain 内可重复使用；该重复使用口径为本 Campaign 已批准桌裁 | v22 PDF 物理页 182、192；重复使用适用范围按本桌裁定 |
| Q02 | 适用域界花费调整，实际产生费用 | 乘以三后向上取整 | v22 PDF 物理页 182–183 |
| Q03 | 角色确实适用人寿保单保障项目 1 且承受多点 Harm | 可用任意素质 QA 防护。剩余 1 Harm 且无其他防护时按已确认口径处理为死亡，不自动计部分抵消 | v22 PDF 物理页 54 |
| Q04 | 当前裁定涉及 QA 和 Burnout 顺序 | 先检查 Burnout，再检查 QA。同次 QA 消耗不在同次检定产生即时 Burnout | v22 PDF 物理页 40–46 |
| Q05 | Time 成长的触发条件与联动字段记账 | 每完成一个完整模组才增加 1 点可使用 Time；Session 结束不自动增加。可使用 Time 增加 n 点时，剩余可用 Time 同步减少 n 点；两个字段分开记录 | 用户于 2026-11-27 明确确认；仅适用于本 Campaign |
| Q06 | Weather Events 任务准备触发 | 只有特别极端且与当前任务相关的天气才执行 Weather Events 掷骰程序；普通天气不掷天气事件骰。触发后仍按 v22 处理天气历史及其 Loose Ends 反馈 | 用户于 2026-11-27 明确确认；仅适用于本 Campaign |

[历史裁定和批准依据](../../Systems/Triangle_Agency/Rule_Reference/04_规则疑点与裁定记录.md#后续用户裁定)


## Q05｜Time 成长触发与联动记账

- **触发时点：** 每完成一个完整模组，增加 1 点可使用 Time；单独结束一个 Session 不触发该奖励。一个模组包含多个 Session 时，只在整个模组结团时结算一次。
- **联动变化：** 每次可使用 Time 增加 n 点，剩余可用 Time 同步减少 n 点。两者是不同字段，变化方向相反，必须分别记账，不得合并或互相替代。
- **余额边界：** 人物卡中“总量 30 / 已花费 2 / 剩余 28”是剩余可用 Time 的轨迹记录，不是当前可使用 Time 的绝对余额。不能由该组数字推算当前可使用 Time。
- **流水要求：** 记录可使用 Time 的前值/增量/后值，以及剩余可用 Time 的前值/减量/后值，并引用同一模组结团事件。若任一前值待核，只记已确认增量，不猜绝对余额。
- **成长用途与购买分离：** 获得 Time 不等于自动购买能力。玩家可指定将其用于哪项成长；实际购买仍需单独确认能力、价格、效果和支付。

本条是用户确认的 Zarek Campaign 桌面约定，不冒充中文 v22 的通用规则，也不得迁移到其他 Campaign。


## Q06｜Weather Events 触发范围

- **本桌触发条件：**只有特别极端、且与当前任务有实质关联的天气，才执行 v22 Weather Events 掷骰程序。普通降雨、常规风雪、温度变化或单纯氛围描写不自动触发天气事件骰。
- **规则边界：**这是用户批准的 Zarek Campaign 运行裁定，不是对 v22 原文的改写。v22 默认任务准备程序仍保留；其他 Campaign 未批准同样裁定时，按各自绑定与 v22 原文执行。
- **触发后的处理：**按当前 Campaign Loose Ends 对应的 Weather Event count 和既有天气历史结算。若某次天气结果明确使机构移除 Loose Ends，立即更新 Campaign 总数，并依 v22 重新确定剩余天气骰次数；不得机械完成旧数量，也不得回头重做已提交的本任务 Starting Chaos。
- **记录：**记录是否满足极端天气触发条件、触发依据、实际掷骰、结果阶段（Xa/Xb/Xc）、Loose Ends 变化及剩余天气骰数量。没有触发时记录 NOT_TRIGGERED，不伪造天气事件历史。
