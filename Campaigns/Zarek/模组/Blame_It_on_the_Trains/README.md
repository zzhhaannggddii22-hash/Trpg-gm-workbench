# Blame It on the Trains｜模组入口

> 正式战役模组。状态：**READY WITH OPEN ITEMS / NOT STARTED**。已完成备团归档与内部复审；独立外部 Prep QA 尚未执行。用户未说“开始”前不得启动。
> 系统：Triangle Agency｜规则唯一权威：《三角机构》中文 v22。
> 来源：Haunted Table Games, *The Vault: Missions for Triangle Agency*；中文精翻母稿 `the_vault_zh.docx`，源 PDF 93–101，印刷页 180–197。
> 权限：除 `05_PLAYER_NOTES.md` 外均为 GM-only。玩家侧文件不得复制任何隐藏真相、幕后因果、NPC 秘密或机制触发信息。

## 文件索引

| 文件 | 职责 | 权限 |
|---|---|---|
| [01_GM_PREP.md](./01_GM_PREP.md) | 模组事实、结构、场景/NPC/线索/风险/收束主持资料 | GM-only |
| [02_NAME_INDEX.md](./02_NAME_INDEX.md) | 稳定实体 ID 与双语别名 | GM-only |
| [03_RUNTIME_STATE.md](./03_RUNTIME_STATE.md) | 当前运行快照；开团前从权威战役状态核验 | GM-only |
| [04_SESSION_LOG.md](./04_SESSION_LOG.md) | Session 日志索引；实际发生后追加 | GM-only |
| [05_PLAYER_NOTES.md](./05_PLAYER_NOTES.md) | 角色已获知事实的空白记录 | 玩家侧 |
| [06_POSTMORTEM.md](./06_POSTMORTEM.md) | 结团复盘；开团前保持未执行 | GM-only |
| [07_SOURCE_AND_RULE_CROSSCHECK.md](./07_SOURCE_AND_RULE_CROSSCHECK.md) | 来源定位、规则交叉核验、审查与测试证据 | GM-only |\n| [08_RUNTIME_QUICK_REFERENCE.md](./08_RUNTIME_QUICK_REFERENCE.md) | 现场快速调用索引 | GM-only |
| [09_RESOURCE_LEDGER.md](./09_RESOURCE_LEDGER.md) | 本模组资源交易唯一流水；开团前空账本 | GM-only |

## 当前门禁

- 备团：READY WITH OPEN ITEMS。关键原文和结构已整理；角色最新绝对资源余额已部分从 2026-11-27 正式人物卡核实；Demerits/Harm/Time 仍有 UNKNOWN。中文 v22 规则逐项核验是 Preflight 前置门槛，未关闭前不得开团。
- 内部复审：已完成一次针对性修订与复核；记录见 07。
- 独立 Prep QA：NOT RUN。该项不是 READY 的默认前提，但本模组单人桌复杂度较高，建议在 Preflight 前执行。
- Preflight：NOT STARTED；规则矩阵未关闭前为 BLOCKED。
- Session：NOT STARTED。
- 玩家启动许可：仅用户明确说“开始”后生效。

## 运行恢复顺序

1. 读取 Campaign 当前正式人物卡、最新战役交接、当前模组 Resource Ledger。
2. 读取本目录 README、07、01、02、03；按需读取规则 v22 对应条文。
3. 核实角色状态冲突；存在冲突时标记 DISPUTED 并暂停相关结算，不猜余额。
4. 形成无剧透玩家简报；不把 GM Prep 转述给玩家。
5. 等待明确开团指令。

## 备团迭代记录

- v0.1（对话内准备）：曾声称完成结构性备团，但未形成可验证仓库交付；不作为 READY 证据。
- v1.0（本次交付）：从原始中文精翻恢复来源，重新建立文件化备团；完成状态、交接与门禁补齐。交付后以 main 的最终 Commit 为准。
