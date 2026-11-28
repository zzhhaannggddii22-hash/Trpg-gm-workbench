# Daggerheart 规则检阅与裁定协议

> 适用范围：仅 `system_id: daggerheart`，默认规则集为 Daggerheart Core Set。  
> 当前状态：candidate / 初版资料建档。  
> 公开规则参考：Official Daggerheart SRD v2.0（2026-08-25）。

## 1. 版本锁定

每次规则检索首先确认：

- `system_id: daggerheart`
- `ruleset_version: Daggerheart Core Set`
- 适用的官方勘误版本与核对日期
- `expansion_scope: CORE_ONLY`（默认）
- SRD 条目本身是否包含 Hope & Fear 扩展内容
- 本次规则是否受 Campaign Frame、卡牌、敌人/环境数据或桌面适配覆盖

SRD v2.0 同时收录 Core Set 与 Hope & Fear 内容。不能仅凭“条目出现在 SRD v2.0”就认定它属于核心规则。无法判定来源时标记 `VERSION_UNRESOLVED`，不进入默认运行集合。

## 2. 来源优先级

1. 当前 Campaign 绑定的官方 Core Set 规则书与官方 Core Set 勘误。
2. 官方 Daggerheart SRD v2.0 中已确认属于 Core Set 的规则条目；SRD 对规则措辞的澄清或修订须记录与印刷核心书的差异。
3. 官方 Core Set 辅助资料（角色卡、主持人速查、卡牌打印文件等），用于确认数据字段、卡牌与流程。
4. 本目录已核验的自写索引、摘要和运行条目。
5. 中文 HTML SRD、Role Initiative、灰机 Wiki 等社区资料，用于阅读、交叉检查和发现问题，不作为冲突时的最终裁判。

Hope & Fear 的专属规则与内容只通过扩展目录检索；用户明确开启扩展或 Campaign Binding 指定时方可加载。

## 3. 规则来源分类

所有规则条目至少带一个来源分类：

- `CORE_SOURCE`：已确认出自 Core Set。
- `CORE_ERRATA`：官方 Core Set 勘误。
- `SRD_CORE_CLARIFICATION`：SRD v2.0 中属于核心体系的澄清/修订，已核对适用范围。
- `HOPE_AND_FEAR`：扩展专属内容，默认关闭。
- `CAMPAIGN_FRAME`：战役框架规则；必须另外标注框架名称及是否属于 Core Set。
- `TABLE_ADAPTATION`：用户明确批准的桌面适配。
- `GM_INFERENCE`：官方规则未明确覆盖时的主持推论。
- `VERSION_UNRESOLVED`：版本或来源未能确认。
- `DISPUTED`：官方、翻译或不同版本之间存在未解决冲突。

不得将 GM 推论、社区建议或临时处理写回为官方规则。

## 4. 核心规则核验字段

每项有机制影响的规则，至少核对：

- Rule ID、规则名称与触发条件；
- 行动主体、目标、范围与适用场景；
- 输入值、属性/修正、资源成本与次数限制；
- 完整结算步骤及前后顺序；
- 希望/恐惧结果、成功/失败分支与关键成功等边界；
- 持续时间、状态变化、结束条件与延迟触发；
- 卡牌、敌人、环境、战役框架或其他规则的覆盖关系；
- 官方来源章节/页码、版本、勘误和核对日期；
- 中英术语差异、尚未解决的问题与测试案例。

规则索引只负责导航。规则条文未规范化前，不能仅凭索引摘要处理高影响或有争议的结算。

## 5. 运行时设计原则

后续 Runtime 应保持轻量：

1. 先理解角色的意图与虚构情境，判断是否有真实风险或明确机制触发。
2. 只在需要时调用规则；不把自由描述强行转换为动作掷骰。
3. 使用对应 Rule ID 的完整步骤进行结算；避免拆分成多轮无意义确认。
4. 对资源、生命、压力、伤害、状态、位置、聚焦、恐惧点和延迟效果提交可追溯的状态差分。
5. 已 VERIFIED 且版本未变的常规规则从本地资料调用，不要求每次在线搜索。
6. 规则缺口、来源冲突、版本变化、特殊卡牌/敌人能力或本地条目未覆盖的边界，再定向回查官方资料。
7. 只暂停依赖 UNKNOWN / DISPUTED 条目的行动，不冻结无关互动。

以上是建设原则，不代表当前已经完成 Runtime 或规则验收。

## 6. 规则缺口处理

发现缺口时：

1. 将问题标记为 `UNKNOWN`、`VERSION_UNRESOLVED` 或 `DISPUTED`。
2. 写明受影响的 Rule ID、行动与最小待核信息。
3. 优先核对官方 Core Set 原文及勘误，再查看官方 SRD。
4. 若 SRD 同时包含扩展条目，检查该内容是否来自 Hope & Fear。
5. 仍无法解决时，保留缺口；只有在必须继续游戏时才提出明确的 `GM_INFERENCE`，并说明影响。
6. 若要形成长期桌规，必须由用户明确批准，并记录在独立桌面适配文件中。

严禁用其他 TRPG 系统的相似机制填补 Daggerheart 规则缺口。

## 7. 版权与仓库边界

本仓库公开。只保存自写规则摘要、来源定位、术语表、勘误索引、核验记录和合法来源链接。不得复制第三方商业规则书、完整翻译、完整卡牌文本或付费模组全文。SRD 与自制内容的引用、衍生和再发布遵守 Darrington Press Community Gaming License 与原来源许可。
