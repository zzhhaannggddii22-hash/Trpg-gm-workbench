# Campaign System Binding｜NQB-01 Runtime Test

```yaml
campaign_id: nqb01_v03_test
campaign_type: isolated_test
canon_status: TEST_ONLY_NON_CANON
system_id: triangle_agency
system_entry: Systems/Triangle_Agency/README.md
adjudications_entry: Campaigns/NQB01_Runtime_Test/RULE_ADJUDICATIONS.md
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
- 规则原文：[中文 v22 PDF](https://github.com/p33333333333333l/triangle-agency-ai-zh/blob/main/最终交付_v22/triangle_agency_zh.pdf)
- 多系统隔离协议：[SYSTEM_CONTEXT_PROTOCOL.md](../../SYSTEM_CONTEXT_PROTOCOL.md)

## 本 Campaign 的隔离约束
1. 唯一绑定 `triangle_agency` / 中文 v22；不得混入其他系统机制。
2. 所有状态、角色、NPC、事件与记录均为 `TEST_ONLY_NON_CANON`。
3. 不引用 Zarek Campaign 的规则适配、角色档案、NPC、模组、资源、人物记忆或运行状态。只共享系统级规则权威入口和通用 GM Training 规范。
4. 本 Campaign 不继承任何正式战役桌规；测试专用裁定必须写入本 Campaign 的 `RULE_ADJUDICATIONS.md` 并经用户明确批准。
5. 当前无测试专用桌规。遇到规则缺口时按系统规则协议保留 UNKNOWN，不从 Zarek 桌裁或其他系统填补。
6. 场景默认是普通日常互动。系统机制没有被行动触发时不强行调用；一旦需要角色数值/能力/资源裁定，而测试角色档案尚未补齐，暂停受影响行动，不得临时编造角色数据。
