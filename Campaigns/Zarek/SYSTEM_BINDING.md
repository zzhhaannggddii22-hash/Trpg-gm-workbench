# Campaign System Binding｜Zarek

```yaml
campaign_id: zarek
system_id: triangle_agency
system_entry: Systems/Triangle_Agency/README.md
adjudications_entry: Campaigns/Zarek/RULE_ADJUDICATIONS.md
ruleset:
  name: "Triangle Agency / 三角机构"
  edition: "中文 v22"
  language: "zh-CN"
  authority: "用户指定的中文 v22 主规则书"
status: active
```

## 权威入口

- 系统资料：[Systems/Triangle_Agency](../../Systems/Triangle_Agency/README.md)
- 规则检阅：[Rule_Reference](../../Systems/Triangle_Agency/Rule_Reference/README.md)
- 规则原文：[中文 v22 PDF](https://github.com/p33333333333333l/triangle-agency-ai-zh/blob/7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1/最终交付_v22/triangle_agency_zh.md)
- 多系统隔离协议：[SYSTEM_CONTEXT_PROTOCOL.md](../../SYSTEM_CONTEXT_PROTOCOL.md)

## Zarek Campaign operational defaults（非通用系统规则）

以下为本 Campaign 已确认的桌面运行约定；不得自动继承到其他 Triangle Agency Campaign：

- **Chaos Pool：**每次任务开始前，读取当前分部的 Loose Ends 总数，按中文 v22《Loose Ends & Weather Events》印刷页 165 的“分部限制表”确定本次任务的初始 Chaos 与天气事件档位；不得固定初始化为 0，也不得继承上一任务的 Chaos 余额。任务内 Chaos Pool 独立记账，完整任务结团时将未使用余额清零。分部 Loose Ends 总数、天气事件历史与任务 Chaos Pool 是不同状态，分别记录。
- **QA 对应 Quality：**普通检定只消耗本次检定所用 Quality 的 QA；不得跨 Quality 挪用。人寿保单保障项目 1（Q03）是明确例外，可消耗任意 Quality 的 QA 来忽略 Harm。
- **Burnout / QA 时序（Q04）：**先检查并结算本次检定已有 Burnout，再处理 QA；同次检定中消耗 QA 不会反向产生本次检定的即时 Burnout。
- **Time（Q05）：**只有完整模组结团才获得 +1 可使用 Time；单独 Session 结束不触发。可使用 Time 增加与剩余可用 Time 减少是两个独立、反向联动的字段。

以上是 Campaign Binding，不是中文 v22 通用规则的改写。具体适用范围见 RULE_ADJUDICATIONS.md。

## 运行约束

1. 本战役只使用 `triangle_agency` 的中文 v22 规则环境。
2. 本战役中出现的 QA、Burnout、Chaos、Harm、ARC、Playwall 等词均按本系统定义解释，不得借用其他系统同名或近似术语。
3. 当前桌裁由 [Zarek 桌裁清单](./RULE_ADJUDICATIONS.md) 定向启用。系统 Rule_Reference 的历史裁定仅供回查，模组特例须通过同一作用域核对。
4. 不得把其他规则系统的技能检定、先攻、行动经济、角色属性或资源规则带入本战役。
5. 若用户明确要求在其他系统开展游戏，应建立独立 Campaign 绑定；不得把本战役静默切换或改写为另一套规则。
6. 本文件只绑定系统，不替代人物卡、战役交接、模组状态或每次 Preflight。
