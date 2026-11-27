# 2026-11-27｜备团交付失效复核与流程修订

## 事件摘要

《Blame It on the Trains》曾在对话中被报告为“备团完成”，但在 main 中没有对应模组目录、GM Prep、Name Index、Runtime State、Player Notes、Source Crosscheck 或 Resource Ledger。Campaign README 和模组索引仍将 Bower Street 标记为 PREPARED / NOT STARTED，未同步 2026-11-27 结团状态与新模组选定事实。

这是交付流程失效，不是单纯文件遗漏。

## 证据基线

- 修复前 main HEAD：`864b16e887e6b8480892f8950ffbab583dd193cb`。
- 公开仓库：`https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench`。
- 目标模组目录在该 HEAD 的完整递归文件树中不存在。
- 原始中文精翻 `the_vault_zh.docx` 可从 Library 找回；对应章节标注源 PDF 93–101、印刷页 180–197。
- 历史对话只支持此前形成过 v0.2 框架性思路，未发现旧版完整 Prep 文件。因此本次是从现存来源重建 v1.0，不将其伪称为旧稿恢复。
- 最新 main 的 Bower Street 结团后状态、Time +1、Mission MVP 选择与 VHS 幕间计划已存在于战役交接后段，但入口未同步。

## 根因

1. **状态混淆**：把内部阅读/思考完成当成仓库交付完成。
2. **缺少证据门禁**：用户汇报没有绑定 Commit、文件清单、回读证据和未执行测试。
3. **入口同步遗漏**：模组目录、Campaign README、模组索引、战役交接未作为同一交付批次管理。
4. **流程责任不清**：标准虽规定强制闭环，但缺少状态迁移所需的机器/人工可核验条件。
5. **并行工作流误解**：把上一模组结团与下一模组备团当成先后阻塞，未及时用结团后权威状态校正下一模组。
6. **测试表述过度**：把静态检查、自审与真正执行的玩家路径模拟/独立 QA 混为一谈。

## 本次修复

- 从现有中文精翻重新建立独立模组目录与备团文件。
- 补齐模组索引、Campaign README 与战役交接的状态同步。
- Bower Street 标记为 CLOSED 历史模组；新模组为 READY WITH OPEN ITEMS / NOT STARTED。
- 将角色资源与 Time 余额设为 Preflight 权威核验项，不复制旧快照。
- 在 09_MODULE_FOLDER_STANDARD 中增加可验证交付门禁与并行结团/备团规则。
- 在 13_PREP_TO_RUNTIME_HANDOFF_STANDARD 中增加入口原子化交接、字段所有权和交付关闭条件。
- 增加 Runtime Quick Reference，分离现场导航与详细 Prep。
- 标记中文精翻未充分呈现的视觉表格/规则缺口，不臆造结果。

## 本轮验证范围

- 已验证修复前 main HEAD 与仓库目标目录缺失。
- 已从原始 DOCX 读取目标章节完整文本段落。
- 已在修复分支创建模组目录文件与流程标准修订。
- 尚待执行：对分支全部新增/修改文件逐一回读；链接路径验证；最新 main 比较与合并；独立 Prep QA；完整自动玩家路径压力测试；规则 v22 逐项页码核验。

## 预防性状态门禁

今后只有当以下证据同时存在，才允许把备团标为 READY：
- 固定 Commit 下的完整必需文件；
- Campaign 入口、模组索引、战役交接状态一致；
- 来源与规则关键事实可追溯；
- 至少一轮实质修订和第二轮复审；
- 玩家侧信息隔离回读；
- Runtime 交接和冷启动检查；
- 未执行测试明确标记，不得包装为 PASS。

## 当前结论

本次修复分支建立了可审查的文件化备团和流程修订，但尚未合并 main，且仍有真实 OPEN 项。当前对外状态不得描述为完全 READY，也不得宣称独立 QA 或自动压力测试已通过。
