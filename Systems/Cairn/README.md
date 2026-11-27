# Cairn /《石冢》

> system_id: cairn
> 规则版本：Cairn Second Edition（2e）
> 中文参考：社区简体中文 SRD（非官方翻译）
> 状态：candidate（系统级成熟度尚未完成激活验收）；CA01_Zaf 有用户授权的 Campaign 范围受控实战，不代表系统已 active。

本目录是 Cairn 系统级规则知识的唯一入口。它与 Systems/Triangle_Agency/ 完全隔离。Cairn 被用户指定为 GM Workbench 的第二套系统；本次接入按独立系统完成，不能把 Triangle Agency 的规则、资源、术语或运行惯例带入。

## 权威来源与版本

1. **首要规则来源：Cairn 2e 官方英文 SRD**
   - [Second Edition 总入口](https://cairnrpg.com/second-edition/)
   - [Player's Guide](https://cairnrpg.com/second-edition/players-guide/)
   - [Warden's Guide](https://cairnrpg.com/second-edition/wardens-guide/)
2. **中文阅读入口：Cairn 2e 简体中文 SRD**
   - [社区简体中文 SRD](https://fi.cairnrpg.com/localization/second-edition/chinese/)
   - 该中文页面声明覆盖玩家手册、监守手册的 31 个核心章节及 CAS-1 至 CAS-4。当前按非官方社区翻译使用；规则冲突以对应版本的官方英文原文为准。
3. **开放许可**
   - 官方 Cairn 2e 规则文本采用 CC BY-SA 4.0。任何基于其规则文本的再发布/改编须遵守署名与相同方式共享要求。
   - 本仓库公开。Cairn 2e 官方文本采用 CC BY-SA 4.0，允许在遵守署名与相同方式共享条件下复制和改编。本仓库将官方规则目录快照与自写 Runtime 摘要分开保存：官方文本副本保留作者/项目署名、上游路径和来源索引；改编内容继续标注 SOURCE / GM_INFERENCE / TABLE_ADAPTATION。不得将未获相应许可的第三方美术、版式或其他模组全文混入这些目录。

## 系统定位

Cairn 是以探索、风险决策和涌现叙事为中心的轻量级冒险游戏。它采用无职业结构、背景驱动角色创建、三属性豁免、攻击直接造成伤害、装备格与疲劳管理，以及明确的地城/荒野探索程序。

其主持原则强调：中立裁定、先看虚构情境、如实且充分地提供可观察信息、随机表生成局势而非预写剧情、NPC 有自身利益与求生意愿。它并非“无规则叙事游戏”：时间、光源、库存、疲劳、危险事件和致命伤害构成了重要的程序化压力。

## 目录

- [Rule_Reference/README.md](./Rule_Reference/README.md)：规则来源优先级、检索与裁定边界。
- [Rule_Reference/CORE_RULE_INDEX.md](./Rule_Reference/CORE_RULE_INDEX.md)：核心机制导航与规则摘要。
- [Rule_Reference/CORE_RULES_RUNTIME.md](./Rule_Reference/CORE_RULES_RUNTIME.md)：按触发条件、输入、步骤、状态变化规范化的核心规则运行手册。
- [Rule_Reference/CHARACTER_CREATION_AND_BACKGROUNDS.md](./Rule_Reference/CHARACTER_CREATION_AND_BACKGROUNDS.md)：角色创建流程、全部背景索引、Fieldwarden 规则与统一库存 UI 约定。
- 角色创建随机结果锁定：首次掷骰后立即记录到人物卡，后续读取既有结果；不得无故重复随机，详见 [GM_SKILL.md §10](./GM_SKILL.md)。
- [RUNTIME_PROTOCOL.md](./RUNTIME_PROTOCOL.md)：桌面阶段循环、规则调用卡、状态提交与官方原文回查策略。
- [Rule_Reference/WARDEN_GUIDE_INDEX.md](./Rule_Reference/WARDEN_GUIDE_INDEX.md)：Warden's Guide 23 个章节的用途分类、主持原则与按需查表边界。
- [Rule_Reference/CHAPTER_VERIFICATION_2026-11-27.md](./Rule_Reference/CHAPTER_VERIFICATION_2026-11-27.md)：官方 Player's Guide 6 章、Warden's Guide 23 章的章节核验记录，以及本轮规则修订与剩余条目级回查范围。
- [Rule_Reference/OFFICIAL_CATALOG_INDEX.md](./Rule_Reference/OFFICIAL_CATALOG_INDEX.md)：Bestiary、Spellbooks、Reliquary、NPC Tables、怪物/背景创建指南及 20 个官方 Backgrounds 的本地完整来源目录。
- [Campaigns/CA01_Zaf/MODULES/CAS-1/REFERENCE_INDEX.md](../../Campaigns/CA01_Zaf/MODULES/CAS-1/REFERENCE_INDEX.md)：CAS-1 模组 NPC、地点、遭遇、事件时钟、特殊程序与 GM-only 资料的检索入口。
- [GM_SKILL.md](./GM_SKILL.md)：Cairn 专属主持执行草案。
- [PREFLIGHT.md](./PREFLIGHT.md)：Cairn 专属开团前核验。
- [Testing/CANDIDATE_VALIDATION_MANIFEST.md](./Testing/CANDIDATE_VALIDATION_MANIFEST.md)：Candidate 受控验证的隔离清单与运行模板。
- [Research/INITIAL_RESEARCH.md](./Research/INITIAL_RESEARCH.md)：设计研究、单人测试风险与短团候选。
- [Testing/L3_NPC_PC_RESOURCE_AND_AUTONOMY_TEST_PLAN.md](./Testing/L3_NPC_PC_RESOURCE_AND_AUTONOMY_TEST_PLAN.md)：将 1–2 次短团同时用于 L3 NPC 的 PC 级资源与自主性验证。
- [Testing/L3_NPC_SYNTHETIC_SELFPLAY_REPORT_2026-11-27.md](./Testing/L3_NPC_SYNTHETIC_SELFPLAY_REPORT_2026-11-27.md)：8 回合、3 分支的 L3 NPC 合成自运行报告。
- [Testing/CORE_RULE_RUNTIME_REGRESSION_MATRIX.md](./Testing/CORE_RULE_RUNTIME_REGRESSION_MATRIX.md)：核心规则运行回归用例。
- [Testing/CORE_RULE_RUNTIME_EXECUTION_REPORT_2026-11-27.md](./Testing/CORE_RULE_RUNTIME_EXECUTION_REPORT_2026-11-27.md)：65 项基础核心规则手动回归记录。
- [Testing/STATE_TRANSITION_REGRESSION_v1/START.md](./Testing/STATE_TRANSITION_REGRESSION_v1/START.md)：状态转换扩展测试入口。
- [Testing/STATE_TRANSITION_REGRESSION_v1/CASES.md](./Testing/STATE_TRANSITION_REGRESSION_v1/CASES.md)：不含预期结果的测试输入。
- [Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md](./Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md)：仅供评审者核对的预期结果。
- [Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md](./Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md)：状态转换扩展测试预期结果，仅供测试执行者核对。
- [Testing/STATE_TRANSITION_EXECUTION_REPORT_2026-11-27.md](./Testing/STATE_TRANSITION_EXECUTION_REPORT_2026-11-27.md)：CRT-66–87 自执行记录与限制。
- [../../tests/test_cairn_runtime_protocol.py](../../tests/test_cairn_runtime_protocol.py)：20 项 Cairn 状态协议参考模型自动化测试（不是 GM Runtime 本身）。
- [Testing/L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md](./Testing/L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md)：扩展离场—重逢连续性回归。

## 运行边界

- 当前系统级成熟度为 candidate。官方章节来源核验已完成，但真实跑团中的 Runtime、状态持久化、规则调用、NPC 连续性和宿主环境验证尚未完成；在这些事项通过验证并复盘前，不得把系统标记为 active。
- Campaign 必须单独建立 SYSTEM_BINDING.md，绑定 system_id: cairn 和精确规则版本。当前已登记 CA01_Zaf / Twin Lakes，按其 SYSTEM_BINDING 中的用户授权进行 Campaign 范围受控实战；此授权不构成系统激活，也不扩展到其他 Campaign。
- candidate 表示系统级成熟度与验收状态，不等于每个使用该系统的 Campaign 都是 NOT_STARTED。Campaign 的实际状态以其 Binding、Runtime State、Session Log 和真实运行证据为准。
- Cairn 的属性、豁免、HP、STR/DEX/WIL 损伤、护甲、疲劳、库存格、背景、法术书、成长和探索程序均属于 Cairn 专属规则。
- 不把 Cairn 的豁免或伤害流程移入 Triangle Agency；也不把 Triangle Agency 的 Chaos、QA、Burnout、Harm 或 Playwall 概念映射进 Cairn。
- 单人玩家测试属于待验证的桌面规模，不代表规则默认支持单人队伍。优先使用规则内的 hirelings 等支持方式；任何超出规则的调整必须明确标记为桌面适配并经用户批准。
- Cairn 短团还承担 Workbench L3 NPC 测试：明确登记的 L3 NPC 使用 PC 级资源账本和独立目标/计划模型。此为 Workbench 的人物模拟要求，不是 Cairn 官方要求所有 NPC 按 PC 创建；规则裁定仍按 Cairn 2e。

## 运行时规则调用

常规游戏不以在线搜索作为规则运行方式。Warden 先读取 Campaign Binding 与 Runtime Snapshot，再按 RUNTIME_PROTOCOL.md 调用 CORE_RULES_RUNTIME.md 中的规则 ID。角色创建、背景与库存速查见 Rule_Reference/CHARACTER_CREATION_AND_BACKGROUNDS.md。官方 Cairn 2e 原文用于建档核验、特殊条目/表格、未收录规则、冲突与高后果边界回查。已规范化的常规核心规则在版本未变且无特殊覆盖时直接调用，不重复搜索网页。任何 PARTIAL / MODULE_DEPENDENT 条目仍须按协议回查。

## 激活门槛

1. 官方 Player's Guide / Warden's Guide 章节核验与规则来源分类（已完成；见 CHAPTER_VERIFICATION_2026-11-27.md）。
2. 规则索引、系统专属 GM Skill、Preflight 与规则疑点记录保持一致，并在发现新规则缺口时更新。
3. 在实际跑团中验证规则调用、正反例/边界行为、资源与时间推进；不另建模拟测试替代真实运行。
4. 在实际跑团与状态恢复流程中验证 Triangle Agency / Cairn 连续性隔离。
5. 独立 Cairn Campaign、人物卡、模组归档与 Preflight 保持完整。
6. 在真实宿主环境完成实际跑团、Runtime State / Session Log / Handoff 验证并复盘后，才评估是否从 candidate 升级为 active。
