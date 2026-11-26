# 仓库结构变更通知｜2026-11-26

> 状态：已合并至 `main`
> 变更提交：`979d4a74a4795ff28a5d675b96076c40a6a66045`

本次对 GM 测试资料进行集中归档。此通知供所有后续读取本仓库的 Chat、操作者和维护者恢复最新目录认知。

## 新的权威入口

- `GM_Training/Testing/README.md`：测试资料总入口。
- `GM_Training/Testing/Fixtures/`：可重复夹具、合成输入、START/ACTION/ORACLE。
- `GM_Training/Testing/Execution_Prompts/`：目标 Chat 执行提示词、操作者协议和历史提示。
- `GM_Training/Testing/Reports/`：验收报告、运行记录、失败审计和复核。
- `GM_Training/Testing/Baselines/`：叙事质量基准的执行材料。

## 兼容与保留

- 根目录的 P0/P1/T0 提示词文件仅作为旧路径兼容入口；权威正文在 `Testing/Execution_Prompts/`。
- `GM_SYSTEM_ACCEPTANCE_PROMPT.md` 已归档到 `Testing/Execution_Prompts/Historical/`，不属于默认执行入口。
- 旧的 `Acceptance_Test_Fixtures/`、`Acceptance_Reports/` 和旧执行提示目录暂保留为兼容副本/历史入口；新文档与新工作流应只链接 `Testing/`。
- L3 NPC 与 Narrative Runtime 两套单会话夹具因 START 文件绑定固定 Fixture ref、固定根目录和被测 commit，继续保留在 `Acceptance_Test_Fixtures/` 原路径。不得仅凭目录迁移改写其 ref 或内部路径。
- `P1_0R/p1_0r_fault_harness.py` 继续保留在原路径，作为独立脚本例外；Testing Fixtures 索引链接到它。
- NQB 评分标准本体仍在 `GM_Training/NARRATIVE_QUALITY_BASELINE.md`；只迁移执行包和运行记录。
- `Training_Logs/`、`Optimization_Reports/`、`Core/`（未建立/未迁移）、根目录 `tests/`、Campaign 专属 QA 均未改名或搬迁。

## 使用规则

1. 新增测试资料一律进入 `GM_Training/Testing/` 对应子目录。
2. 新增训练过程与能力观察仍进入 `Training_Logs/`；工程性能审计与优化实施仍进入 `Optimization_Reports/`。
3. 固定历史 ref 的测试严格按 START 文件所指定的 ref 和路径读取；不要自动改用 main 最新目录。
4. 迁移只改变资料归档入口，不代表任何测试被重新执行或通过。
