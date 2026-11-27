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

- **普通 Chaos Pool：**每个模组独立建池，初始值为 0，除非当前模组原文明确规定其他初始值；完整模组结团时关闭该模组池并重置为 0，不继承上一模组余额。模组内池与区域 Loose Ends / Weather Effects 分开记录。
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
