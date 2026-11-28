# 二元骰概率与行动经济研究（Core Set）

> 规则范围：Daggerheart Core Set  
> 规则基准：Official Daggerheart SRD 2.0（2026-08-25）  
> 计算方式：枚举两颗 d12 的全部 144 种有序结果  
> 状态：CALCULATED / DESK-VERIFIED；未包含 Advantage / Disadvantage 等额外骰的完整组合模型

## 1. 结论先行

1. **Hope / Fear 倾向与 Difficulty 无关。** Hope Die 大于 Fear Die 的概率为 45.83%；Fear Die 大于 Hope Die 的概率也为 45.83%；两骰相同的 Critical Success 概率为 8.33%。
2. **总体 Hope 结果概率为 54.17%。** 其中包括 45.83% 的 Hope Die 较高结果，以及 8.33% 的 Critical Success。Critical Success 视为 Hope 结果。
3. **GM 每次 Action Roll 获得 Fear 的基础概率恒为 45.83%。** Difficulty 不改变这个概率；在 Fear 未达上限且忽略休息/能力等其他来源时，平均每 10 次 Action Roll 产生约 4.58 Fear。
4. **GM 获得 Spotlight 的概率随有效难度上升。** Success with Fear、Failure with Hope、Failure with Fear 都会把 Spotlight 交给 GM；只有 Success with Hope 和 Critical Success 留在玩家侧。
5. **这不是固定回合经济。** GM 获得 Spotlight 后可以选择一个合适 Move，也可能花 Fear 追加 GM Move、额外敌人 Spotlight 或 Fear Feature。不能把“GM Turn 次数”简单等同于敌人行动次数。

## 2. 基础骰面概率

两颗 d12 有 144 种等概率有序组合。

| 事件 | 组合数 | 概率 |
|---|---:|---:|
| Hope Die > Fear Die | 66 | 45.83% |
| Fear Die > Hope Die | 66 | 45.83% |
| 两骰相同（Critical Success） | 12 | 8.33% |
| Hope 结果（Hope 较高 + Crit） | 78 | 54.17% |
| Fear 结果 | 66 | 45.83% |

这里的 Hope / Fear 指骰子倾向，不是行动成功或失败。Difficulty 只改变成功/失败的分布，不改变 Hope / Fear 的基础比例。

## 3. 成功率与 GM Spotlight 转移率

为避免把 Trait、Experience 与 Difficulty 混在一起，定义：

**有效难度 = 原始 Difficulty − 所有固定加值**

以下数据假设：
- 只掷两颗基础 d12；
- 不含 Advantage / Disadvantage 额外骰；
- 不含其他随机加值；
- Critical Success 无论总值是否达到有效难度，都自动成功并按 Hope 结果处理。

| 有效难度 | 总成功率（含 Crit） | 成功且 Hope（含 Crit） | Success with Fear | Failure with Hope | Failure with Fear | Spotlight 转给 GM |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 77.8% | 43.1% | 34.7% | 11.1% | 11.1% | 56.9% |
| 11 | 72.2% | 40.3% | 31.9% | 13.9% | 13.9% | 59.7% |
| 12 | 65.3% | 36.8% | 28.5% | 17.4% | 17.4% | 63.2% |
| 13 | 58.3% | 33.3% | 25.0% | 20.8% | 20.8% | 66.7% |
| 14 | 50.0% | 29.2% | 20.8% | 25.0% | 25.0% | 70.8% |
| 15 | 43.1% | 25.7% | 17.4% | 28.5% | 28.5% | 74.3% |
| 16 | 36.1% | 22.2% | 13.9% | 31.9% | 31.9% | 77.8% |
| 18 | 25.0% | 16.7% | 8.3% | 37.5% | 37.5% | 83.3% |
| 20 | 16.7% | 12.5% | 4.2% | 41.7% | 41.7% | 87.5% |
| 22 | 11.1% | 9.7% | 1.4% | 44.4% | 44.4% | 90.3% |
| 24 | 8.3% | 8.3% | 0.0% | 45.8% | 45.8% | 91.7% |

说明：
- “成功且 Hope”包含 Critical Success。
- “Spotlight 转给 GM” = Success with Fear + Failure with Hope + Failure with Fear。
- Difficulty 24 时，只有双骰相同的 Critical Success 能自动成功；其他组合的总和都低于 24。

## 4. 例子：同一个 Difficulty，不同角色能力

假设原始 Difficulty 为 15：

- PC 固定加值 +0：有效难度 15，总成功率 43.1%，GM 获得 Spotlight 的概率 74.3%。
- PC 固定加值 +2：有效难度 13，总成功率 58.3%，GM 获得 Spotlight 的概率 66.7%。
- PC 固定加值 +4：有效难度 11，总成功率 72.2%，GM 获得 Spotlight 的概率 59.7%。

这说明 GM 评估难度时应考虑 PC 的真实加值，而不是只看原始 Difficulty。高难度不只降低成功率，也会让更多 Action Roll 以失败结束，从而更频繁地把 Spotlight 交给 GM。

## 5. 对 GM 行动经济的意义

### 5.1 不要把 Fear 收入和 Spotlight 转移混为一谈

Fear 收入只取决于 Fear Die 是否高于 Hope Die（Critical Success 除外，且 Crit 计作 Hope），所以每次 Action Roll 的基础 Fear 生成概率固定为 45.83%。

GM 获得 Spotlight 的概率则还包含 Failure with Hope。有效难度越高，Failure with Hope 越多，GM 越容易获得 Spotlight；但这些 Failure with Hope 不会给 GM 增加 Fear。

### 5.2 GM 不缺少自然获得的行动机会

在有效难度 10 时，约 56.9% 的 Action Roll 会把 Spotlight 交给 GM；有效难度 15 时约 74.3%；有效难度 18 时约 83.3%。

因此：
- 不需要为了“让 GM 有回合”而频繁花 Fear 打断玩家。
- Fear 的重要价值是购买额外主动权、额外 Move、额外敌人 Spotlight、Fear Feature 或敌人 Experience，而不是制造每一个普通 GM Turn。
- 高难度会自然提高 GM 接管 Spotlight 的频率；若同时设计大量高伤害 Hard Move，战斗压力可能迅速叠加。
- 每次 Action Roll 都可能改变局势，因此无意义检定不仅拖慢节奏，也会额外生成 GM Spotlight 和 Fear。

### 5.3 每次行动掷骰都应值得

官方 GM Guidance 建议只在有意义的时刻要求掷骰，并在每次 Action Roll 后推进信息、行动或局势变化。

从概率上看，即使一个动作几乎必定成功，仍有 45.83% 的 Fear 倾向；即使动作难度很高，仍有 8.33% 的自动成功 Crit。若一个没有风险、没有有趣后果的动作被要求掷骰，结果可能凭空制造 GM 资源与叙事转折。

所以：
- 轻易成功的动作直接成功；
- 失败只会拖延且没有有趣后果的动作直接成功或改写赌注；
- 只有结果未知、风险真实且不同结果会改变局势时才掷骰。

## 6. 适用边界

本研究只计算基础 Duality Dice：
- 不含 Advantage / Disadvantage d6；
- 不含其他额外骰、Rally Dice、卡牌效果或重掷；
- 不模拟 Hope / Fear 上限、休息收入、能力收入、Fear 支出或多个敌人行动；
- “GM Spotlight 转移率”是每次 Action Roll 的概率，不是每场战斗 GM 总行动次数；
- 不代表正式桌面体验中玩家行动次数、场景时长或战斗平衡的完整预测。

## 7. 来源

- Official Daggerheart SRD 2.0（2026-08-25）：<https://www.daggerheart.com/srd/>
- 官方 SRD 2.0 PDF：<https://www.daggerheart.com/wp-content/uploads/2026/08/DH_SRD_2_2026_08_25.pdf>
- 易检索的非官方 SRD HTML 镜像：<https://daggerheartsrd.com/rules/making-moves-and-taking-action/>
- GM Guidance：<https://daggerheartsrd.com/rules/gm-guidance/>
- 社区索引《贤者恩泽 Sage-Touched》：<https://vcn3zvu2w61p.feishu.cn/wiki/FOziwMdb6iFF4nkU4fkc5jsjnKg>

本文件为独立枚举计算与原创分析，不复制社区文章。待取得并读取《贤者恩泽》中关于概率和行动经济的具体子文章后，再进行逐项比较并记录差异。
