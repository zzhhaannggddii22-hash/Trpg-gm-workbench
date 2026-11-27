# Issue 独立编号规范

## 目的

GitHub 在同一仓库中为 Issue 与 Pull Request 共用原生编号序列。原生编号是平台定位符，不适合作为本项目唯一的缺陷/需求编号。

本仓库从本规范生效起，使用独立的项目级 Issue ID。Issue ID 与 GitHub 原生编号一一映射，但两者不可互换。

## 编号规则

- 格式：`ISSUE-NNN`，三位数字起步，例如 `ISSUE-001`、`ISSUE-010`。
- Issue ID 只分配给 GitHub Issue，不分配给 Pull Request。
- 编号按首次登记顺序单调递增；已分配编号永久保留，不因关闭、重复、取消或删除而回收。
- 不按优先级、模块、年份或状态编码，避免分类变化导致改号。
- GitHub 原生编号只用于链接和平台操作，必须带有明确语境，例如“ISSUE-001（GitHub #22）”。
- 日常讨论、复盘报告、测试报告、提交说明和计划统一引用 `ISSUE-NNN`；不得把裸 `#NN` 当作项目 Issue ID。
- PR 仍使用 GitHub 原生 PR 编号并明确写作“PR #NN”；PR 不占用 Issue ID 序列。PR 关联 Issue 时必须同时写出双方完整标识，例如“修复 ISSUE-001，见 PR #37”。

## 分配流程

1. 创建新 Issue 前，先查看本文件的“编号登记表”，取下一个未使用的编号。
2. 创建 GitHub Issue 时，在标题开头写入 `[ISSUE-NNN]`。
3. 在 Issue 正文顶部写明 `Project Issue ID: ISSUE-NNN`，并记录 GitHub 原生编号和链接。
4. 随即更新本登记表，补充标题、原生编号、状态和关联 PR。
5. 关闭 Issue 不删除登记；重开时继续使用原 ID。重复 Issue 保留原 ID，并在登记表注明其重复目标。
6. 若创建失败且 GitHub Issue 未生成，可释放尚未正式登记的预留编号；一旦生成并登记，编号不得复用。

## 编号登记表

| Project Issue ID | GitHub Issue | 标题 | 状态 |
|---|---:|---|---|
| ISSUE-001 | #22 | 优化《三角机构》规则处理模块：检定结算未完整执行 Chaos Pool | OPEN |
| ISSUE-002 | #23 | 历史 NPC 与线索接续失误 | OPEN |
| ISSUE-003 | #24 | NPC 跟随关系与队伍空间连续性丢失 | OPEN |
| ISSUE-004 | #25 | NPC 随行状态与场景空间连续性错误 | OPEN |
| ISSUE-005 | #26 | 场景全局状态维护失误：车辆驾驶者与座位状态丢失 | OPEN |
| ISSUE-006 | #27 | NPC 信息权限泄露：引用未获知的 GM-only 地点 | OPEN |
| ISSUE-007 | #41 | 资料不完整时过度阻断分析与调查推进 | OPEN |
| ISSUE-008 | #42 | Chaos Pool 变化未被持续记录，导致公开资源状态丢失 | OPEN |
| ISSUE-009 | #43 | Bower Street VHS 对话出现无依据的隐藏空间描述与异常机制提示 | OPEN |
| ISSUE-010 | #46 | 调查推进中补造未经证实的空间线索 | OPEN |

**下一个可分配编号：`ISSUE-011`**

> 本表记录的是项目级 Issue ID；GitHub 原生编号仍以 GitHub 页面为准。修改标题或状态时同步维护本表，不得根据 GitHub 原生编号推算项目编号。
