# GM Training Testing｜测试资料中心

本目录是 GM Runtime 与综合叙事质量测试的唯一当前入口。测试资料按用途分区；训练过程与工程优化仍分别归入 `Training_Logs/` 和 `Optimization_Reports/`。

| 目录 | 内容 | 使用规则 |
|---|---|---|
| [Fixtures](./Fixtures/README.md) | 可重复夹具、START/ACTION/ORACLE、合成测试输入 | 先读对应 START；遵守固定 ref、执行顺序和信息隔离要求 |
| [Execution Prompts](./Execution_Prompts/README.md) | 目标 Chat 提示词、操作者协议、执行交接 | 先区分目标 Chat、操作者和独立复核角色 |
| [Reports](./Reports/README.md) | 验收报告、运行记录、失败审计与复核 | 历史结论不可覆盖；新运行新增报告 |
| [Baselines](./Baselines/README.md) | NQB 基准场景包、玩家启动材料、审核表和执行提示 | 基准标准本体仍以 `../NARRATIVE_QUALITY_BASELINE.md` 为准 |

## 执行边界

- `SC-01` 至 `SC-18` 不属于默认回归清单；历史设计或操作者材料不得自动变成目标 Chat 的执行任务。
- 固定历史 ref 的夹具必须严格按 START 指定的 ref 和路径读取；不得自行替换为 main 最新版本。
- `P1_0R/p1_0r_fault_harness.py` 保留在原路径，作为独立脚本例外；从 Fixtures 索引链接过去。
- GM-only、操作者协议和 ORACLE 的标记不构成 GitHub 访问控制。不得把隐藏答案上传目标 Chat。
- 设计文件存在不代表测试已执行或通过；报告必须记录版本、证据等级和未测试边界。
