# 通用/专属掷骰路由分拆｜单会话自测报告

> 类型：SINGLE_SESSION_SELF_TEST
> 结果：PASS（设计级行为）；NOT PRODUCTION ACCEPTANCE
> 测试方式：同一会话内按现行 SELF_TESTING_PROTOCOL 顺序执行；未调用外部 AI 复审。
> 基线 main：ec54bc100dceaf1da370edd811da22dc48f07a42
> 被测设计提交：9ae553e864408cbe5678cdf9f93a0e61e5219eaf
> 场景夹具 ref：qa/roll-resolution-generic-system-split-fixtures-v1_3
> 最终夹具：GM_Training/Testing/Fixtures/ROLL_RESOLUTION_GENERIC_SYSTEM_SPLIT_v1/

## 1. 测试结果总览

| 测试层 | 结果 | 说明 |
|---|---:|---|
| 顺序场景夹具 | 11/11 PASS | ACTION_01–ACTION_11 顺序执行，最后才读取 ORACLE |
| 通用路由/系统机制参考模型 | 31/31 PASS | 绑定、行动分类、系统专属发起权、Ask、基础骰池、Conflict Resolution |
| 随机来源策略 | 3/3 PASS | 工具 CSPRNG 优先；不可用时仍默认助手掷骰并标记 MODEL_GENERATED；用户自掷优先 |
| Dice UI Schema 测试向量 | 11/11 PASS | 使用 Draft 2020-12 本地镜像验证正例/反例；实际 Schema 文件另做 JSON 解析与结构检查 |
| 跨文件静态契约检查 | 25/25 PASS | SYSTEM_CONTEXT、Binding、Runtime、Resource Ledger、Q04、Playwall、UI 投影与索引 |

31 项确定性参考模型断言使用本会话内的临时测试 harness 执行；该 harness 不是生产引擎，也未作为可执行代码提交到仓库。可复现的版本化场景证据是下方 11-action fixture。Schema 测试向量使用从实际 Schema 结构构造的 Draft 2020-12 本地镜像；实际 Schema 文件另行通过 JSON 解析与字段/边界静态检查。以上是设计/参考模型测试，不代表已部署的 Runtime 或 UI 通过生产验收。

## 2. 关键场景结论

1. **玩家提问不等于行动**：询问能否攀爬湿滑外墙，不创建掷骰；玩家实际尝试时，Triangle Agency 使用 Default Failure，不创造通用技能检定。
2. **Ask 前置条件**：缺少 Causality Chain 时暂停，不生成骰面；补充可信因果链后才进入 6d4。
3. **执行者与发起者分离**：玩家明确发起 Ask，助手按用户偏好默认执行掷骰；玩家明确自掷时才改为 PLAYER_REPORTED。
4. **自然 Triscendence**：原始骰面恰好三个 3，立即成功、0 Chaos、等待玩家选奖励；不进入普通 Burnout/QA/Chaos。三项奖励为 All Hands、Circle Back、Employee of the Moment。
5. **Circle Back**：玩家选择后恢复 2 点 Empathy QA 与 1 点 Initiative QA；只在测试内存状态中记录，没有写入真实 Resource Ledger。
6. **Stability 与 Triscendence 分离**：原始骰面只有两个 3，玩家花费 1 Subtlety QA 把第 5 枚骰改为 3，最终恰好三个 3，触发 Stability、0 Chaos，但不触发自然 Triscendence，也不产生奖励选择。
7. **Burnout 边界**：2 层 Burnout、原始只有 1 个 3；移除该 3 后，第二层仍增加 1 Chaos。剩余 5 枚非 3 骰各贡献 1 Chaos，总计 7 Chaos，结果失败。
8. **Conflict Resolution**：第一轮累计 A=6、B=6，平局继续；第二轮 A=7、B=6，A 唯一领先胜出。没有普通 QA/Burnout/Chaos/Triscendence；当前单骰池 UI 不接管冲突，文本回退。
9. **Playwall 未解锁**：沿用 Campaign Playwall Ledger 的 BLOCKED_OR_UNKNOWN；不读取文档、不推断内容。
10. **Playwall 已解锁但骰子整合未完成**：测试专用合成文档使用特殊 2d6 骰池。仅将依赖该骰池的子结算标记 UNSUPPORTED_PENDING_RULE_REVIEW；不套用普通 6d4。此为合成测试规则，不是真实 Playwall 文档。
11. **跨系统隔离**：当前 Binding 为 Triangle Agency 时，D20 问题不切换系统、不导入其他系统检定。

## 3. 测试中发现并修正的问题

这些问题均在最终 v1.3 场景夹具与候选设计提交前修正，没有被计为通过：

- **v1 初版输入缺陷**：ACTION_06/07 未写明检定 Quality。缺少 Quality 时不能靠骰面或资源状态反推。v1.1 明确补入 Subtlety 与 Empathy，旧版保留为历史记录。
- **Playwall 状态混淆**：最初把“无解锁证据”与“已解锁但骰子整合未完成”混成一个状态。v1.3 拆成 BLOCKED_OR_UNKNOWN 与 UNSUPPORTED_PENDING_RULE_REVIEW，并增加仅供测试的合成 A7 文档。
- **通用发起权过度收窄**：早期参考模型把所有系统都要求为玩家发起。修订后由系统专属规则决定玩家、GM 或规则触发，通用层只保留分派。
- **随机来源策略与用户偏好冲突**：修订为优先工具级 CSPRNG；无可用工具 RNG 时仍由助手执行并如实标记 MODEL_GENERATED，不再额外要求用户确认；用户明确自掷时优先采用玩家报告。

## 4. 当前架构分拆

### 通用层
`GM_Training/14_ROLL_RESOLUTION_ROUTING_PROTOCOL.md`

只负责：
- Campaign / system binding 核验；
- 玩家输入语义分类；
- 当前系统的掷骰发起权判定；
- 专属机制路由与原文核验；
- 助手默认执行 / 玩家自掷；
- 向既有 Runtime 交接。

不定义骰型、骰数、成功阈值、资源公式或任何系统的专属机制。

### Triangle Agency 专属层
`Systems/Triangle_Agency/Rule_Reference/02_DICE_RESOLUTION_PROTOCOL.md`

只负责中文 v22 的：
- Default Failure；
- Ask the Agency；
- Anomaly Ability；
- 基础 6d4、Triscendence、Stability、Burnout/QA；
- Conflict Resolution；
- Zarek Q04 的精确 Campaign 作用域。

现有 `triangle-agency-rules-index.md` 继续承担规则导航；没有新建一套重复 Rule Access Map。

### Dice UI
`Systems/Triangle_Agency/Dice_UI/README.md` 与 `player-view.schema.json` 是本系统只读玩家投影规范。没有内部 event/ledger/manifest ID。Conflict Resolution 不进入单骰池 Schema，使用文本回退。

## 5. 资源与持久化边界

静态契约检查确认本设计沿用当前 main 的既有结构：
- Session 内资源交易以当前模组 Resource Ledger 为唯一流水/余额权威；
- Session Log 引用 Resource Ledger Entry ID，不重复建立资源流水；
- Runtime State 不保存资源余额；
- 正式人物卡按 Session 边界对账更新；
- 玩家回复、骰子 UI 与文本回退从 Runtime §14.19 的同一份 player_reply_payload 生成；
- 跨文件持久化证明沿用 Runtime §14.14 reconciliation manifest，不创建骰子专用第二套账本或 Manifest。

场景夹具所有资源变化均为内存模拟，没有修改真实 Campaign、Resource Ledger、Session Log、Runtime State 或人物卡。因此，**真实存储写入、失败恢复、重复提交和读回证据仍未做 Runtime 集成测试**。

## 6. Playwall 处理边界

本轮暂缓的是 Playwall 专属能力与本骰子结算管线的自动化整合，不是现有 Playwall 解锁/文档流程。

现有 Zarek 单人默认继续按 `Campaigns/Zarek/PLAYWALL_UNLOCK_LEDGER.md` 与 `GM_Training/Testing/Fixtures/PLAYWALL_INTERMISSION_INTEGRITY_REGRESSION_v1.md` 执行：代码未解锁时不读；代码解锁后 GM 读取精确完整文档并处理适用效果，不要求额外私读确认/分享回执；保护 GM-only 内容，不读相邻未解锁文档。

只有在精确文档已解锁、已读取，但其骰子专属机制尚未接入本管线时，才暂停该骰子子结算并标记 UNSUPPORTED_PENDING_RULE_REVIEW。

## 7. 尚未通过本轮证明的事项

- 目标 Chat Runtime 是否已真正调用通用路由与 Triangle Agency 专属协议；
- 当前所有 Anomaly Ability 的逐项资格、成本、骰型、成功/失败与例外覆盖；
- Playwall 专属骰子机制的后续逐项整合；
- Resource Ledger 实际写入、部分失败、重试、读回与 §14.14 manifest 的端到端验证；
- Dice UI 的宿主实现、可访问性、移动端布局和真实玩家交互；
- 其他已登记 TRPG 系统的真实专属路由夹具。本轮仅用合成 GM-triggered 路由验证通用层没有硬编码“玩家发起”。

## 8. 最终判断

**PASS：当前设计边界和已覆盖的基础规则分支通过本轮自测。**

**NOT READY FOR LIVE ACTIVATION：** 尚未接入真实 Runtime、Resource Ledger 写入和 UI 宿主。不得仅凭本报告把设计协议改成主 Skill 强制入口，也不得把未覆盖的 Playwall 专属能力视为已支持。

本轮没有调用外部 AI 复审，没有合并 PR，没有修改 main。
