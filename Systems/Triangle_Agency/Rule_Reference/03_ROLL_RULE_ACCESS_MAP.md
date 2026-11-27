# Triangle Agency Rule Access Map｜掷骰机制调用索引（设计稿）

> 状态：DESIGN / 未获运行批准
> 规则版本：中文 v22
> 基线：PR #52 review head d600e24 的修订分支
> 页码：均指中文 v22 PDF 物理页码；具体行动仍须回查完整原文

本索引用于快速定位候选机制，不替代原文核验。索引未覆盖的例外不得被视为不存在。

| mechanic_id | 玩家语言触发 / 行动类别 | 权威原文定位 | 必须核对 | 结算路径 | 当前状态 |
|---|---|---|---|---|---|
| NO_ROLL_DEFAULT_FAILURE | 普通可行行动、危险/困难的常人行动、可行性询问 | v22 pp.37, 47–51 | 玩家是否声明执行；普通因果是否可行；Default Failure 是否适用 | 不创建骰子事件；说明限制与合法替代路径 | 基础路径已整理，逐次核验 |
| ASK_THE_AGENCY_BASE | 明确请求机构提供效果/答案 | v22 pp.47–51；原骰与结果 pp.42–46 | 请求效果、可信常人因果链、相关 Quality、已确立事实、自由意志限制、失败地点力竭 | 通过请求门槛后基础 6d4；自然三重升华先分流；否则普通 Burnout/QA/最终结果 | 基础路径纳入本轮 |
| ANOMALY_ABILITY_BASE | 明确调用异常能力，且能力条文不依赖 Playwall 专属解锁/覆盖 | v22 pp.47–50；逐项能力原文另查 | 角色资格、ARC、Quality、Trigger、Cost、骰型、成功/失败；能力专属覆盖 | 基础 6d4 仅在条文确认适用时使用；任何未核验专属覆盖暂停 | 有条件支持；不代表能力目录已逐项核验 |
| NATURAL_TRIPLE_ASCENSION | 基础机构掷骰的原始骰面恰好三个 3 | v22 pp.43–46 | 必须是任何调整前的原始骰面；不得把能力添加的 3 当作自然骰面 | 独立分支：成功、零 Chaos、等待玩家选择奖励；跳过普通 Burnout/QA/Chaos 路径 | 纳入本轮 |
| ORDINARY_BURNOUT_QA_CHAOS | 未命中自然三重升华的普通基础机构掷骰 | v22 pp.38, 40–46；QA 细节 pp.46–50 | 原始触发、Burnout、对应 Quality QA、逐骰修改、最终骰面、Stability、Chaos | 按已核验规则顺序处理；Zarek Q04 只在该 Campaign Binding 生效 | 纳入本轮；桌裁作用域受限 |
| CONFLICT_RESOLUTION | 两方/多方目标冲突，需要按冲突机制解决 | v22 pp.56–58 | 参与者、双方目标、玩家同意/发起边界、同步轮次、累计 3 数与平局续掷 | 独立多人多轮路径；累计至少六个 3 且独占第一才结束；不调用普通 QA/Burnout/Chaos/三重升华 | 规则路径已登记；当前单骰池 UI Schema 不支持，使用文本回退 |
| HARM_LIFE_INSURANCE | 伤害与人寿保单防护 | v22 pp.40–41, 46, 54 | Harm 类型、保单状态、可用 QA、适用防护条文 | 独立防护流程，不作为普通检定跨 Quality QA 的先例 | 本轮不实现骰子 UI 自动结算 |

## 调用纪律

1. 先判断是否需要掷骰，再识别具体机制。
2. 先匹配候选机制，再按机制原文确认发起者与执行者。
3. 对动态角色资格、资源和 Campaign 桌裁按当前状态核验；静态条文仍可复用已核验定位。
4. ANOMALY_ABILITY_BASE 不是“所有异常能力均支持”的承诺。遇到 Playwall 解锁、专属骰型、特殊费用、免掷或其他未核验覆盖，立即转 UNSUPPORTED_PENDING_RULE_REVIEW。
5. Conflict Resolution 不得进入单骰池状态机；在多参与者/多轮投影验收前使用文本回退。
6. 任何索引缺失、原文不可读或关键条件不明，标记 MAP_GAP 并暂停受影响分支。

## 状态说明

- SUPPORTED_IN_THIS_REVISION：本轮明确覆盖且有基础流程/验收夹具的范围。
- CONDITIONAL_SUPPORT：只有逐项规则原文与角色资格核验通过才可使用。
- TEXT_FALLBACK_ONLY：机制路径可被识别，但当前 UI 契约不能完整表示。
- UNSUPPORTED_PENDING_RULE_REVIEW：专属规则尚未核验或实现，禁止套用基础流程。
