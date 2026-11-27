# 《Bower Street》｜模组档案

> 当前运行与推进许可见 [Runtime State](./03_RUNTIME_STATE.md)、[Session Log Index](./04_SESSION_LOG.md) 和 [Resource Ledger](./09_RESOURCE_LEDGER.md)。请按运行协议核验检查点。
> 系统：`triangle_agency`｜规则：《三角机构》中文 v22。
> 来源：Haunted Table Games，《The Vault: Missions for Triangle Agency》，Kay W.；中文精翻母稿 `the_vault_zh.docx`，源 PDF 41–49，印刷页 76–93。
> 信息权限：本目录除 `05_PLAYER_NOTES.md` 外均为 GM-only；不得把本目录内容粘贴到玩家侧回复。

## 文件索引

| 文件 | 用途 | 权限 |
|---|---|---|
| [01_GM_PREP.md](./01_GM_PREP.md) | 模组事实基石、调查/场景、NPC、线索、异常行为、分支与主持控制 | GM-only |
| [02_NAME_INDEX.md](./02_NAME_INDEX.md) | 中英文名称、别名、规范 ID | GM-only |
| [03_RUNTIME_STATE.md](./03_RUNTIME_STATE.md) | 运行快照和检查点；启动时核验 | GM-only |
| [04_SESSION_LOG.md](./04_SESSION_LOG.md) | 编号 Session 日志的入口 | GM-only |
| [05_PLAYER_NOTES.md](./05_PLAYER_NOTES.md) | 玩家侧调查记录；仅供指定玩家接收 | 玩家侧 |
| [06_POSTMORTEM.md](./06_POSTMORTEM.md) | 结团后复盘；当前未执行 | GM-only |
| [07_SOURCE_AND_RULE_CROSSCHECK.md](./07_SOURCE_AND_RULE_CROSSCHECK.md) | 原文定位、规则核验、差异、审查和压力测试记录 | GM-only |
| [08_PLAYER_FACING_GATE.md](./08_PLAYER_FACING_GATE.md) | 每轮玩家可见回复的信息来源、NPC 知识、空间事实与泄露处理闸门 | GM-only |
| [09_RESOURCE_LEDGER.md](./09_RESOURCE_LEDGER.md) | 本模组资源交易流水、余额快照与待核对账；Session Log 引用其 Entry ID | GM-only |

## 调用顺序

- 备团复核：README → 07 Source Crosscheck → 01 GM Prep → 02 Name Index。
- 正式开团 Preflight：读取本 Campaign 最新角色卡、战役交接、SYSTEM_BINDING、Zarek 桌裁启用清单，再读取本目录 03 Runtime State、最近 Session Log、09 Resource Ledger、01 GM Prep 的相关片段、02 Name Index，以及 08 Player-Facing Gate（必须作为活动 Session 常驻约束装配）；核对当时实际装备和资源。
- 运行中：按场景/行动需要调用 01；实际事件写入 04；资源变化在同一轮只写入 09；Session Log 引用资源 Entry ID；Runtime State 不复制资源余额；只把角色真实获知内容写入 05。
- 续接、下一 Session 与待核资源沿 03、09 和最近 Session Log 定向读取；入口索引只负责定位。
- 每次 Session 结束：先完成 09 的资源对账，再将角色资源与关键道具快照更新至正式人物卡；更新 Runtime State 的场景快照，不复制资源余额。完整模组结团后再更新 README、05、06，并同步 Campaign 层资料。

## 版本与迭代

- v0.1：初步场景结构、NPC、线索与遭遇梳理（此前聊天中曾输出，不作为最终版本）。
- v1.0：初次备团版本；后经独立审查发现现场应用与规则边界问题，原 READY WITH OPEN ITEMS 结论撤销。
- v1.1-audit-fix：根据第一轮独立审查修订 Domain/Corrupt、泳池、时间线、NPC/线索、收束条件、资源与结算；第二轮独立审查确认首要两项已修复，但发现 C1–C7 新阻塞。
- v1.2-targeted-fixes：针对第二轮独立审查修订厨房追逐条件、Ripple Gun 结果结算、手机双猫资源冲突与脱困、双人恢复触发、Jodie/社区信息门槛、Aftermath 分支、分部 Pool 核算流程、Expand 与布娃娃索引。
- v1.3-third-audit-fixes：根据第三轮独立报告修正卧室按事件时 Domain 状态裁定、手机信息披露层级与无剧透暂停说明、街道测量和 Jodie 信息来源边界；补齐 Cooper/Fumiko/Justin 的条件性 Aftermath、历史记录标签。凯西已完成跨文件自检；不等同于独立复审或真实玩家测试。
- 压力测试为案头推演，未执行真实玩家测试；不得把压力测试写成实战验证。
- 历史备团与首次 Preflight 的证据见 07；运行事故与状态变化见编号 Session 日志及 Runtime。
