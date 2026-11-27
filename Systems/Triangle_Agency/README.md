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
- [Research/](./Research/README.md)：Triangle Agency 专属 AI GM 架构、规则索引、GM 研究、参考资料与单特工桌面配置研究；历史审查材料归入 Research/Archive。
- [Templates/](./Templates/README.md)：三角机构专属历史模板，不作为跨系统通用模板。

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


## 掷骰与结果展示

- [Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md](./Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md)：三角机构专用掷骰检定执行协议（设计稿）。
- [Dice_UI/](./Dice_UI/README.md)：独立骰子结果展示组件契约与事件 Schema（设计稿）。
- 跨系统调用纪律见 [GM_Training/ROLL_RESOLUTION_PROTOCOL.md](../../GM_Training/ROLL_RESOLUTION_PROTOCOL.md)。
