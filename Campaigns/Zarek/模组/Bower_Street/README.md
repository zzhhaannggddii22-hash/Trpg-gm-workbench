# 《Bower Street》｜模组档案

> 状态：BLOCKED（2026-11-25 第三轮独立审查后，凯西已完成定向修订与自检；等待用户决定是否接受当前备团）。尚未进入 Preflight 或开团。
> 系统：`triangle_agency`｜规则：《三角机构》中文 v22。
> 来源：Haunted Table Games，《The Vault: Missions for Triangle Agency》，Kay W.；中文精翻母稿 `the_vault_zh.docx`，源 PDF 41–49，印刷页 76–93。
> 信息权限：本目录除 `05_PLAYER_NOTES.md` 外均为 GM-only；不得把本目录内容粘贴到玩家侧回复。

## 文件索引

| 文件 | 用途 | 权限 |
|---|---|---|
| [01_GM_PREP.md](./01_GM_PREP.md) | 模组事实基石、调查/场景、NPC、线索、异常行为、分支与主持控制 | GM-only |
| [02_NAME_INDEX.md](./02_NAME_INDEX.md) | 中英文名称、别名、规范 ID | GM-only |
| [03_RUNTIME_STATE.md](./03_RUNTIME_STATE.md) | 当前唯一有效运行快照；开团前由 Preflight 填入 | GM-only |
| [04_SESSION_LOG.md](./04_SESSION_LOG.md) | 实际发生的 Session 历史；当前为空 | GM-only |
| [05_PLAYER_NOTES.md](./05_PLAYER_NOTES.md) | 玩家角色实际获得的信息；当前为空白 | 玩家侧 |
| [06_POSTMORTEM.md](./06_POSTMORTEM.md) | 结团后复盘；当前未执行 | GM-only |
| [07_SOURCE_AND_RULE_CROSSCHECK.md](./07_SOURCE_AND_RULE_CROSSCHECK.md) | 原文定位、规则核验、差异、审查和压力测试记录 | GM-only |

## 调用顺序

- 备团复核：README → 07 Source Crosscheck → 01 GM Prep → 02 Name Index。
- 正式开团 Preflight：读取本 Campaign 最新角色卡、战役交接、SYSTEM_BINDING、Zarek 桌裁启用清单，再读取本目录 03 Runtime State、最近 Session Log、01 GM Prep 的相关片段与 02 Name Index；核对当时实际装备和资源。
- 运行中：按场景/行动需要调用 01；状态变化写入 04 并同步 03；只把角色真实获知内容写入 05。
- 结团后：结算与 CANON 核验后更新 README、03、05、06，并同步 Campaign 层资料。

## 版本与迭代

- v0.1：初步场景结构、NPC、线索与遭遇梳理（此前聊天中曾输出，不作为最终版本）。
- v1.0：初次备团版本；后经独立审查发现现场应用与规则边界问题，原 READY WITH OPEN ITEMS 结论撤销。
- v1.1-audit-fix：根据第一轮独立审查修订 Domain/Corrupt、泳池、时间线、NPC/线索、收束条件、资源与结算；第二轮独立审查确认首要两项已修复，但发现 C1–C7 新阻塞。
- v1.2-targeted-fixes：针对第二轮独立审查修订厨房追逐条件、Ripple Gun 结果结算、手机双猫资源冲突与脱困、双人恢复触发、Jodie/社区信息门槛、Aftermath 分支、分部 Pool 核算流程、Expand 与布娃娃索引。
- v1.3-third-audit-fixes：根据第三轮独立报告修正卧室按事件时 Domain 状态裁定、手机信息披露层级与无剧透暂停说明、街道测量和 Jodie 信息来源边界；补齐 Cooper/Fumiko/Justin 的条件性 Aftermath、历史记录标签。凯西已完成跨文件自检；不等同于独立复审或真实玩家测试。
- 压力测试为案头推演，未执行真实玩家测试；不得把压力测试写成实战验证。
- 当前仍为 BLOCKED / AWAITING USER REVIEW；本轮修订与自检没有自动放行 Preflight。若用户决定继续，Preflight 内再核对当前角色卡、装备、QA/Burnout、任务配给、实际地方分部累计 Loose Ends 与开局普通 Chaos Pool。模组原文未提供的异常独立数值档案不得自行补造。
