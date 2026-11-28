# 规则检阅与裁定协议

> 适用范围：`system_id: daggerheart`。默认规则集为 Core Set，`expansion_scope: CORE_ONLY`。  
> 当前状态：candidate / 首轮本地规则运行手册已建立。  
> 公开规则基准：Official Daggerheart SRD v2.0（2026-08-25）。

## 1. 版本锁定

每次规则检索首先确认：

- `system_id: daggerheart`
- `ruleset_version: Daggerheart Core Set`
- 官方勘误版本与核对日期
- `expansion_scope: CORE_ONLY`（默认）
- 当前条目是否来自混合版 SRD 2.0
- 本次规则是否受 Campaign Frame、卡牌、敌人/环境数据或桌面适配覆盖

SRD v2.0 同时收录 Core Set 与 Hope & Fear。不能仅凭条目出现在 SRD v2.0 就认定属于 Core Set。来源不明时标记 `VERSION_UNRESOLVED`。

## 2. 来源优先级

1. 当前 Campaign 绑定的官方 Core Set 规则书与官方 Core Errata。
2. 官方 SRD 2.0 中已确认属于 Core Set 的规则条目；SRD 对规则措辞的澄清/修订须记录与印刷核心书的差异。
3. 官方 Core 辅助资料（角色卡、GM Guide、卡牌打印文件、速查表），用于确认字段、卡牌与流程。
4. 本地 `CORE_RULES_RUNTIME.md`、`LOOKUP_TABLES.md`、结构化 JSON 和已核验索引。
5. 中文 HTML SRD、Role Initiative、灰机 Wiki 等社区资料，用于阅读、交叉检查和发现问题，不作为冲突时的最终裁判。
6. 本地 [ERRATA_CROSSCHECK.md](./ERRATA_CROSSCHECK.md) 用于查看已核对的勘误差异；若官方发布新版本，仍须重新核对来源。

Hope & Fear 内容只通过扩展目录检索；用户明确启用或 Campaign Binding 指定后才加载。

## 3. 规则来源分类

- `CORE_SOURCE`：已确认出自 Core Set。
- `CORE_ERRATA`：官方 Core 勘误。
- `SRD_CORE_CLARIFICATION`：SRD 2.0 中属于核心体系的澄清/修订。
- `HOPE_AND_FEAR`：扩展专属内容，默认关闭。
- `MIXED_VERSION`：同一章节同时列出基础与扩展内容，默认不加载。
- `OPTIONAL_PROCEDURE`：可选战役机制，不属于默认程序。
- `TABLE_ADAPTATION`：用户明确批准的桌面适配。
- `GM_INFERENCE`：官方规则未明确覆盖时的主持推论。
- `VERSION_UNRESOLVED`：版本或来源未能确认。
- `DISPUTED`：官方、翻译或不同版本之间存在未解决冲突。

不得将 GM 推论、社区建议或临时处理写回为官方规则。

## 4. 核验字段

每项有机制影响的规则至少核对：

- Rule ID、规则名称与触发条件；
- 行动主体、目标、范围与适用场景；
- 输入值、属性/修正、资源成本与次数限制；
- 完整结算步骤及顺序；
- Hope/Fear 结果、成功/失败分支与 Critical 边界；
- 持续时间、状态变化、结束条件与延迟触发；
- 卡牌、敌人、环境或 Campaign Frame 覆盖关系；
- 官方来源章节/页码、版本、勘误和核对日期；
- 中英术语差异、待解决问题与测试案例。

## 5. 本地优先运行协议

常规运行不以在线搜索作为工作流程：

1. 确认 SYSTEM_BINDING 与当前扩展范围。
2. 从 [CORE_RULE_INDEX.md](./CORE_RULE_INDEX.md) 按 Rule ID 定位。
3. 调用 [CORE_RULES_RUNTIME.md](./CORE_RULES_RUNTIME.md) 的规范步骤。
4. 使用 [LOOKUP_TABLES.md](./LOOKUP_TABLES.md) 和 `Reference_Data/Core_Set/` 的结构化数据。
5. 敌人/环境分别查 [ADVERSARY_INDEX.md](./ADVERSARY_INDEX.md)、[ENVIRONMENT_INDEX.md](./ENVIRONMENT_INDEX.md) 和对应 JSON。
6. 只有本地条目未覆盖、出现官方勘误/新版、数据抽取错误、特殊能力覆盖或用户提出规则质疑时，才定向回查官方来源。
7. 稳定核验结论写回本地文件，避免之后重复搜索。

已完成本地规范化且版本未变的常规机制，不因其“后果严重”就自动要求重复联网。若关键步骤或例外未在本地覆盖，才回查。

## 6. 规则缺口处理

1. 标记 `UNKNOWN`、`VERSION_UNRESOLVED` 或 `DISPUTED`。
2. 写明受影响 Rule ID、行动与最小待核信息。
3. 优先核对官方 Core Set 原文和 Core Errata，再看 SRD。
4. 若 SRD 同时列出扩展选项，检查该内容是否来自 Hope & Fear。
5. 仍无法解决时保留缺口；若必须继续，只能采用明确标记的 GM_INFERENCE 并说明影响。
6. 长期桌规须由用户明确批准，并记录在独立桌面适配文件中。

严禁用其他 TRPG 的相似机制填补规则缺口。

## 7. 规则与资料文件

- [核心规则索引](./CORE_RULE_INDEX.md)
- [核心运行手册](./CORE_RULES_RUNTIME.md)
- [常用检索表](./LOOKUP_TABLES.md)
- [二元骰概率与行动经济研究](./DICE_PROBABILITY_AND_ACTION_ECONOMY.md)
- [角色选项索引](./CHARACTER_OPTIONS_INDEX.md)
- [领域卡索引](./DOMAIN_CARD_INDEX.md)
- [武器索引](./WEAPON_INDEX.md)
- [护甲索引](./ARMOR_INDEX.md)
- [物品与消耗品索引](./LOOT_INDEX.md)
- [Beastform 索引](./BEASTFORM_INDEX.md)
- [敌人索引](./ADVERSARY_INDEX.md)
- [环境索引](./ENVIRONMENT_INDEX.md)
- [术语表](./GLOSSARY.md)
- [来源登记](./SOURCE_REGISTER.md)
- [Core Errata 交叉核验](./ERRATA_CROSSCHECK.md)
- [规则疑点](./RULE_ISSUES.md)
- [专属 GM Skill](../GM_SKILL.md)
- [Preflight](../PREFLIGHT.md)
- [回归测试矩阵](../Testing/CORE_RULE_RUNTIME_REGRESSION.md)
- [结构化数据集](../Reference_Data/README.md)

## 8. 版权与仓库边界

本目录使用 SRD 2.0 Public Game Content，依 DPCGL 2.0 条款保留署名、来源、许可与修改说明。商业 Core Rulebook 未纳入 SRD 的精确正文、Campaign Frame 全文与地图、艺术图像、付费模组及无再分发许可的资料不进入公开仓库。详见 [数据许可与署名记录](../Reference_Data/LICENSE_AND_ATTRIBUTION.md)。