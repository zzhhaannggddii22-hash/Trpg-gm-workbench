# Blame It on the Trains｜模组入口

> 正式战役模组。状态：**DELIVERED / PREP RULE VALIDATION COMPLETE / PREFLIGHT NOT STARTED**。文件化交付与可访问中文来源下的核心规则核验已完成；官方英文原版逐页校勘为非阻塞来源质量项。用户未说“开始”前不得启动。
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
| [07_SOURCE_AND_RULE_CROSSCHECK.md](./07_SOURCE_AND_RULE_CROSSCHECK.md) | 来源定位、规则交叉核验、审查与测试证据 | GM-only |
| [08_RUNTIME_QUICK_REFERENCE.md](./08_RUNTIME_QUICK_REFERENCE.md) | 现场快速调用索引 | GM-only |
| [09_RESOURCE_LEDGER.md](./09_RESOURCE_LEDGER.md) | 本模组资源交易唯一流水；开团前空账本 | GM-only |
| [10_PLAYER_FACING_GATE.md](./10_PLAYER_FACING_GATE.md) | 玩家视角信息披露闸门 | GM-only |
| [11_REMEDIATION_AND_TEST_LOG.md](./11_REMEDIATION_AND_TEST_LOG.md) | 本轮缺陷修复、测试执行与交付清单 | GM-only |

## 当前门禁

- 文件交付：DELIVERED（固定 Commit 下文件存在并已回读）。
- 备团设计：REVIEWED；这不代表规则验证完成。
- 来源核验：PARTIAL / NON-BLOCKING；中文精翻第 191–208 页已分页回读，官方英文原版逐页校勘仍未完成。
- Prep Rule Validation：COMPLETE AGAINST AVAILABLE CHINESE SOURCES；见 07 §3、§10。设备持有人、角色余额和实际天气/环境设置留待 Preflight。
- Runtime/单人路径可执行性：PARTIAL；已完成规则映射 v2、10 项确定性机械测试与 15 项单人路径测试，并执行 6 条主持续接轨迹；完整信息等价性与真实玩家运行仍未验证。
- 正式 Preflight：NOT STARTED / WAITING FOR USER “开始”。Preflight 负责本次资源、装备、持有人、天气/环境状态与玩家选择的恢复，不补做已关闭的规则研究。
- 用户开团许可：WAITING FOR USER “开始”。
- 内部复审：本轮由凯西独立执行缺陷复核、结构测试、合成状态测试和单人路径案头模拟；详细记录见 07 与 11。
- 独立 Prep QA：NOT RUN（可选；本轮由凯西内部逐项核验与自测，不宣称独立审查）。
- Preflight：NOT STARTED；Prep Rule Validation 已关闭，但必须等待用户明确“开始”。
- Session：NOT STARTED。
- 玩家启动许可：仅用户明确说“开始”后生效。

## 运行恢复顺序（仅在门禁解除后）

1. 读取 Campaign 当前正式人物卡、最新战役交接、当前模组 Resource Ledger。
2. 读取本目录 README、07、01、02、03；按需读取规则 v22 对应条文。
3. 核实角色状态冲突；存在冲突时标记 DISPUTED 并暂停相关结算，不猜余额。
4. 形成无剧透玩家简报；不把 GM Prep 转述给玩家。
5. 等待明确开团指令。

## 备团迭代记录

- v0.1（对话内准备）：曾声称完成结构性备团，但未形成可验证仓库交付；不作为 READY 证据。
- v1.0（首次交付）：从中文精翻恢复来源并建立文件化备团；曾误报 READY，现已由本轮状态门禁纠正。
- v1.1（本轮独立修复）：修复规则核验阶段、Runtime 检查点、资源账本幂等、系统/通用规则分层、状态冲突和索引；测试及未关闭项见 11。本轮修复已通过 PR #62 合并至 main；合并 Commit：`975ca83ced73d7d95d72a1396d819c354dd49830`。
