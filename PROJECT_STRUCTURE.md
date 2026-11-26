# 项目目录与文件职责

本文件是仓库结构导航，不覆盖各目录内部 README 的细节，也不改变任何规则、战役或训练事实。

## 顶层结构

```text
.
├── README.md
├── PROJECT_STRUCTURE.md
├── SYSTEM_CONTEXT_PROTOCOL.md
├── CAPABILITY_TRANSFER.md
├── GM_Training/          # 跨系统通用 GM 能力、运行、训练与验收
├── Systems/              # 每套规则系统独立隔离
├── Campaigns/            # 具体战役、模组、CANON 与运行状态
├── Research/             # 跨系统研究与候选方法
├── tests/                # 仓库级自动化检查与测试工具
├── .github/              # CI 与仓库工作流
└── package.json          # 测试工具依赖
```

## 权威归属

| 内容 | 唯一归属 | 不应放入 |
|---|---|---|
| 通用主持原则、GM Skill、人物/叙事能力、跨系统训练 | `GM_Training/` | 任一具体系统目录 |
| 规则、术语、机制、官方裁定、系统专属适配 | `Systems/<System>/` | 通用 GM Skill、其他系统目录 |
| 战役人物、模组、CANON、NPC 关系、Session 与 Runtime 状态 | `Campaigns/<Campaign>/` | Systems、通用 Research |
| 跨系统研究、尚未验证的方法 | `Research/` | 已稳定的规范入口 |
| 系统专属研究、历史审查、系统专属模板 | 对应 `Systems/<System>/` 子目录 | 顶层 Research |
| 自动化代码、夹具解析、Markdown 导航检查 | `tests/` | GM 运行规范 |

## GM_Training 内部组织

- 根目录：当前通用权威规范、主 Skill、训练计划与主要入口。
- `Testing/Reports/`：验收结论、缺陷复核和交接报告。
- `Testing/`：测试资料中心，按 Fixtures、Execution_Prompts、Reports、Baselines 分类。
- `Optimization_Reports/`：性能计划、工程优化方案与实施记录。
- `Training_Logs/`：实际训练样本、反馈与开放问题。
- `MICRO_SANDBOX_LAB/`：跨系统、NON-CANON 的可玩微型箱庭训练子项目。

执行提示词与操作者协议虽集中归档，但公开仓库不提供访问控制；标记 GM-only 只表示使用权限边界，不代表文件对公众保密。

## Testing 内部组织

- `Fixtures/`：可重复测试夹具、START/ACTION/ORACLE 与合成输入。
- `Execution_Prompts/`：目标 Chat 执行提示、操作者协议与历史提示。
- `Reports/`：验收结论、复核、运行记录与缺陷交接。
- `Baselines/`：叙事质量基准的 GM Packet、玩家启动材料、审核表与执行提示。

`Training_Logs/` 继续保存训练过程、能力盘点和开放问题；`Optimization_Reports/` 继续保存工程优化资料。固定历史 ref 的旧目录在其历史提交中保持原样。

## Systems 内部组织

每个系统至少建立 README，登记 `system_id`、规则版本、权威来源、规则索引和专属研究。系统目录互相隔离。当前 `Systems/Triangle_Agency/` 仅承载三角机构系统知识与其历史资料。

- `Rule_Reference/`：规则检阅协议、规则摘要、现场裁定与疑点记录。
- `Research/`：该系统的专属研究与历史审查。
- `Templates/`：只适用于该系统的历史或当前模板。

## Campaigns 内部组织

每个 Campaign 必须通过 `SYSTEM_BINDING.md` 绑定唯一 system_id 与规则版本。非 CANON 测试短团可以归档在 Campaign 内，但必须明确标记测试性质、非 CANON 边界和禁止继承的状态。

## 迁移约定

1. 新文件放到其内容权威归属目录，不按“看起来像文档”统一堆放。
2. 迁移文件时，旧路径尽量保留简短兼容入口，指向新权威位置。
3. 只有在确认不再被引用、且历史追溯不受影响时才删除兼容入口。
4. 目录整理不得重写规则、战役 CANON、测试结论或历史事实。
