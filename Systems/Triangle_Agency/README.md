# Triangle Agency /《三角机构》

> system_id: `triangle_agency`  
> 当前正式规则版本：用户指定的《三角机构》中文 v22  
> 状态：active（当前扎雷克战役使用）

本目录是《三角机构》全部**系统级**规则知识的唯一入口。战役人物、CANON、NPC 与模组过程记录仍保存在 `Campaigns/Zarek/`，并通过其 SYSTEM_BINDING 绑定本系统。

```yaml
system_id: triangle_agency
ruleset_versions: ["中文 v22"]
status: active
```

## 权威规则来源

- [中文 v22 主规则书 PDF](https://github.com/p33333333333333l/triangle-agency-ai-zh/blob/main/最终交付_v22/triangle_agency_zh.pdf)
- [中文 v22 主规则书 Markdown](https://github.com/p33333333333333l/triangle-agency-ai-zh/blob/7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1/最终交付_v22/triangle_agency_zh.md)
- [上游 v22 交付目录](https://github.com/p33333333333333l/triangle-agency-ai-zh/tree/main/最终交付_v22)

规则摘要、索引与速查用于定位和恢复知识，不替代完整原文。具体裁定必须回查当前 Campaign 指定版本的相关原文、页码和适用条件。

## 目录

- [Rule_Reference/](./Rule_Reference/README.md)：规则检阅协议、基础规则与现场裁定、规则疑点及本桌裁定记录。
- [Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md](./Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md)：Triangle Agency 中文 v22 专属掷骰执行说明（DESIGN / 未启用）。
- [Dice_UI/](./Dice_UI/README.md)：玩家骰子视图规范与只读 Schema（DESIGN / 未部署）。
- [Playwall 专属能力骰子管线整合暂缓登记](./Rule_Reference/PLAYWALL_DEFERRED_REGISTER.md)：不覆盖现有 Playwall 解锁与文档处理流程。
- [Research/](./Research/README.md)：Triangle Agency 专属 AI GM 架构、规则索引、GM 研究、参考资料与单特工桌面配置研究；历史审查材料归入 Research/Archive。
- [Templates/](./Templates/README.md)：三角机构专属历史模板，不作为跨系统通用模板。

## 系统专属运行分派（runtime_dispatch）

以下入口只在 Campaign Binding 锁定 `system_id: triangle_agency` / 中文 v22 后使用；其他系统不得加载本节内容。

```yaml
runtime_dispatch:
  rule_entry: Systems/Triangle_Agency/Rule_Reference/05_常规规则调用路由.md
  progression_entry: Systems/Triangle_Agency/Rule_Reference/02_PLAYWALL_UNLOCK_AND_INTERMISSION_PROTOCOL.md
  mechanisms:
    chaos_runtime:
      status: DISABLED
      readiness: DRAFT_PENDING_BEHAVIORAL_VALIDATION
      entry: Systems/Triangle_Agency/Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md
    dice_resolution:
      status: DISABLED
      readiness: DESIGN_NOT_ENABLED
      entry: Systems/Triangle_Agency/Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md
```

`DISABLED` 表示机制虽已定义但不得作为正式运行时执行。Chaos Runtime 的具体验收门槛以其协议 §13 和独立验收记录为准；本 README 的登记不构成启用授权。Playwall 解锁、文档读取与非骰子效果仍按 progression_entry 正常执行；骰子专属能力整合的暂缓范围见 `PLAYWALL_DEFERRED_REGISTER.md`。

## 系统边界

- 不将其他 TRPG 的通用技能检定、先攻、行动经济、属性结构、资源或伤害惯例带入本系统。
- 不把本桌适配写成官方规则；官方规则、用户确认桌规、临时裁定与推论分开记录。
- 角色能力、Playwall、任务状态和隐藏资料必须按角色当前解锁状态与信息权限处理。
- 规则疑点保留为疑点；不能用其他系统的相似机制补齐。
- 任何跨系统可迁移的 GM 方法应提炼后进入 `GM_Training/`，但系统规则本身留在本目录。

## 运行入口

当前 Campaign：[扎雷克战役](../../Campaigns/Zarek/README.md)  
系统绑定：[SYSTEM_BINDING.md](../../Campaigns/Zarek/SYSTEM_BINDING.md)  
多系统隔离协议：[SYSTEM_CONTEXT_PROTOCOL.md](../../SYSTEM_CONTEXT_PROTOCOL.md)
