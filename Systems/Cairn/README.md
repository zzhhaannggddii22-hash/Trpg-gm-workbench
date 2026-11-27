# Cairn /《石冢》

> system_id: `cairn`
> 规则版本：Cairn Second Edition（2e）
> 中文参考：社区简体中文 SRD（非官方翻译）
> 状态：candidate（第二套系统接入准备中；尚未开放正式运行）

本目录是 Cairn 系统级规则知识的唯一入口。它与 `Systems/Triangle_Agency/` 完全隔离。Cairn 被用户指定为 GM Workbench 的第二套系统；本次接入按独立系统完成，不能把 Triangle Agency 的规则、资源、术语或运行惯例带入。

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
   - 本仓库公开。遵守项目总 README 的第三方内容边界：不提交受版权保护的规则书或模组全文；仅保存自写规则摘要、定位、来源链接与必要的兼容性说明。

## 系统定位

Cairn 是以探索、风险决策和涌现叙事为中心的轻量级冒险游戏。它采用无职业结构、背景驱动角色创建、三属性豁免、攻击直接造成伤害、装备格与疲劳管理，以及明确的地城/荒野探索程序。

其主持原则强调：中立裁定、先看虚构情境、如实且充分地提供可观察信息、随机表生成局势而非预写剧情、NPC 有自身利益与求生意愿。它并非“无规则叙事游戏”：时间、光源、库存、疲劳、危险事件和致命伤害构成了重要的程序化压力。

## 目录

- [Rule_Reference/README.md](./Rule_Reference/README.md)：规则来源优先级、检索与裁定边界。
- [Rule_Reference/CORE_RULE_INDEX.md](./Rule_Reference/CORE_RULE_INDEX.md)：核心机制导航与规则摘要。
- [Rule_Reference/CORE_RULES_RUNTIME.md](./Rule_Reference/CORE_RULES_RUNTIME.md)：按触发条件、输入、步骤、状态变化规范化的核心规则运行手册。
- [RUNTIME_PROTOCOL.md](./RUNTIME_PROTOCOL.md)：桌面阶段循环、规则调用卡、状态提交与官方原文回查策略。
- [Rule_Reference/WARDEN_GUIDE_INDEX.md](./Rule_Reference/WARDEN_GUIDE_INDEX.md)：监守手册中的 NPC、知识/感知、豁免、地城/荒野探索与成长原则。
- [GM_SKILL.md](./GM_SKILL.md)：Cairn 专属主持执行草案。
- [PREFLIGHT.md](./PREFLIGHT.md)：Cairn 专属开团前核验。
- [Testing/CANDIDATE_VALIDATION_MANIFEST.md](./Testing/CANDIDATE_VALIDATION_MANIFEST.md)：Candidate 受控验证的隔离清单与运行模板。
- [Research/INITIAL_RESEARCH.md](./Research/INITIAL_RESEARCH.md)：设计研究、单人测试风险与短团候选。
- [Testing/L3_NPC_PC_RESOURCE_AND_AUTONOMY_TEST_PLAN.md](./Testing/L3_NPC_PC_RESOURCE_AND_AUTONOMY_TEST_PLAN.md)：将 1–2 次短团同时用于 L3 NPC 的 PC 级资源与自主性验证。
- [Testing/L3_NPC_SYNTHETIC_SELFPLAY_REPORT_2026-11-27.md](./Testing/L3_NPC_SYNTHETIC_SELFPLAY_REPORT_2026-11-27.md)：8 回合、3 分支的 L3 NPC 合成自运行报告。
- [Testing/CORE_RULE_RUNTIME_REGRESSION_MATRIX.md](./Testing/CORE_RULE_RUNTIME_REGRESSION_MATRIX.md)：核心规则运行回归用例。
- [Testing/CORE_RULE_RUNTIME_EXECUTION_REPORT_2026-11-27.md](./Testing/CORE_RULE_RUNTIME_EXECUTION_REPORT_2026-11-27.md)：65 项基础核心规则手动回归记录。
- [Testing/STATE_TRANSITION_REGRESSION_v1/START.md](./Testing/STATE_TRANSITION_REGRESSION_v1/START.md)：状态转换扩展测试入口；输入与 Oracle 分离。
- [Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md](./Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md)：状态转换扩展测试预期结果，仅供测试执行者核对。
- [Testing/STATE_TRANSITION_EXECUTION_REPORT_2026-11-27.md](./Testing/STATE_TRANSITION_EXECUTION_REPORT_2026-11-27.md)：CRT-66–87 自执行记录与限制。
- [Testing/L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md](./Testing/L3_NPC_REENCOUNTER_REGRESSION_REPORT_2026-11-27.md)：扩展离场—重逢连续性回归。

## 运行边界

- 当前状态为 candidate。研究、规则学习和隔离测试可以进行；在完成本目录的规则核验、Preflight、正反例与跨系统隔离测试前，不得将其标记为 active，也不得伪装成已完成正式接入。
- Campaign 必须单独建立 `SYSTEM_BINDING.md`，绑定 `system_id: cairn` 和精确规则版本。当前没有已批准的 Cairn Campaign。
- Cairn 的属性、豁免、HP、STR/DEX/WIL 损伤、护甲、疲劳、库存格、背景、法术书、成长和探索程序均属于 Cairn 专属规则。
- 不把 Cairn 的豁免或伤害流程移入 Triangle Agency；也不把 Triangle Agency 的 Chaos、QA、Burnout、Harm 或 Playwall 概念映射进 Cairn。
- 单人玩家测试属于待验证的桌面规模，不代表规则默认支持单人队伍。优先使用规则内的 hirelings 等支持方式；任何超出规则的调整必须明确标记为桌面适配并经用户批准。
- Cairn 短团还承担 Workbench L3 NPC 测试：明确登记的 L3 NPC 使用 PC 级资源账本和独立目标/计划模型。此为 Workbench 的人物模拟要求，不是 Cairn 官方要求所有 NPC 按 PC 创建；规则裁定仍按 Cairn 2e。

## 运行时规则调用

常规游戏不以在线搜索作为规则运行方式。Warden 先读取 Campaign Binding 与 Runtime Snapshot，再按 [RUNTIME_PROTOCOL.md](./RUNTIME_PROTOCOL.md) 调用 [CORE_RULES_RUNTIME.md](./Rule_Reference/CORE_RULES_RUNTIME.md) 中的规则 ID。官方 Cairn 2e 原文用于建档核验、特殊条目/表格、未收录规则、冲突与高后果边界回查。已规范化的常规核心规则在版本未变且无特殊覆盖时直接调用，不重复搜索网页。任何 PARTIAL / MODULE_DEPENDENT 条目仍须按协议回查。

## 激活门槛

1. 官方 2e 玩家手册与监守手册关键规则逐项核验，中文 SRD 逐项交叉核对。
2. 完成规则索引、系统专属 GM Skill、Preflight 和规则疑点记录。
3. 完成至少一轮规则正例、反例与边界案例测试。
4. 完成 Triangle Agency / Cairn 跨系统污染测试。
5. 建立独立 Cairn Campaign 与模组资料，完成真实 Preflight。
6. 通过短团实测并复盘后，才评估是否从 candidate 升级为 active。
