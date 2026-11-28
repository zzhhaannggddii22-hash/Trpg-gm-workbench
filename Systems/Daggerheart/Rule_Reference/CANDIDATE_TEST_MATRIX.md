# Candidate 规则回归矩阵（Core Set）

> 状态：TESTS_DEFINED / 尚未运行时执行。  
> 目标：验证高频机制的输入、时序、资源变化和关键边界；不把测试设计误报为测试通过。  
> 测试基准：SRD 2.0（2026-08-25），Core Set only。

## 使用方式

- 每个测试从干净状态开始，除非用例明确要求连续状态。
- 骰值由测试用例指定，不随机掷骰。
- 每例记录输入状态、触发规则、预期输出和实际输出。
- 只有实际执行并核对后才将状态改为 PASS。
- 如果规则文本有争议，先标记 BLOCKED / RULE_ISSUE，不把测试预期当成 RAW。

## 核心用例

| ID | 覆盖规则 | 输入/场景 | 预期结果 | 状态 |
|---|---|---|---|---|
| DH-T01 | DH-ACTION | 总值恰好等于 Difficulty；Hope Die 高于 Fear Die | 成功 with Hope；PC +1 Hope；聚焦留在 PC | DESIGNED |
| DH-T02 | DH-ACTION | 总值低于 Difficulty；Fear Die 高于 Hope Die | Failure with Fear；GM +1 Fear；重大后果；聚焦给 GM | DESIGNED |
| DH-T03 | DH-ACTION | Duality Dice 相同 | 自动成功；PC +1 Hope、清除 1 Stress；视作 Hope 结果 | DESIGNED |
| DH-T04 | DH-REACTION | PC Reaction Roll 双骰相同 | 忽略本次成功时本会承受的影响；不获 Hope、不清 Stress、不触发额外 GM Move | DESIGNED |
| DH-T05 | DH-HOPE-FEAR | PC 有 2 Hope，Action Roll 成功 with Hope，同时触发 Class Hope Feature（成本 3） | 本次新获得的 1 Hope 可立即支付，Feature 成功发动后 Hope 余额为 0 | DESIGNED |
| DH-T06 | DH-ADV | 同一行动有 3 个 Advantage 来源、1 个 Disadvantage 来源 | 抵消后只掷 1 个 Advantage d6；不同时掷 Advantage 与 Disadvantage | DESIGNED |
| DH-T07 | DH-ADV | 两名盟友 Help an Ally，行动者也有普通 Advantage | 每位盟友各付 1 Hope 并掷 d6；最终只取所有相关 d6 的最高值 | DESIGNED |
| DH-T08 | DH-GROUP | 两名协助者分别成功、失败；Leader 正常掷 Action Roll | Leader 结果 +1、−1 抵消；协助 Reaction Roll 不产生 Hope/Fear | DESIGNED |
| DH-T09 | DH-TAG-TEAM | 两名 PC 分别掷出不同成败/倾向 | 结算前选择一组结果用于双方；资源按被选结果和参与人数处理 | DESIGNED |
| DH-T10 | DH-DAMAGE | PC 受到等于 Major Threshold 的伤害 | 标记 2 HP；若先标记 Armor Slot，则伤害严重程度下降一级 | DESIGNED |
| DH-T11 | DH-DAMAGE | PC 有 Resistance，受到奇数点对应伤害 | 先将 Incoming Damage 减半并向上取整，再处理 Armor Slots 与阈值 | DESIGNED |
| DH-T12 | DH-STRESS | PC 已标记所有 Stress，又被要求标记 2 Stress | 无法标记 Stress 时改标记 1 HP；不能使用要求其标记 Stress 的 Feature | DESIGNED |
| DH-T13 | DH-REST | Long Rest 中途被敌人打断 | 只获得 Short Rest 收益；Fear 及刷新按 Short Rest 规则结算 | DESIGNED |
| DH-T14 | DH-COUNTDOWN | Progress Countdown(6)；一次 Action Roll 为 Critical Success | 倒计时 tick down 3；只推进一次 | DESIGNED |
| DH-T15 | DH-DEATH | PC 标记最后一个 HP，选择 Avoid Death，Hope Die ≤ Level | PC 昏迷并获得 Scar；永久划掉一个 Hope Slot，记录叙事影响 | DESIGNED |
| DH-T16 | DH-DOMAIN | Loadout 已满，Level Up 取得新 Domain Card | 新卡免费获得；需将一张现有卡移入 Vault 后才能装入 | DESIGNED |
| DH-T17 | DH-ENEMY-ATTACK | GM d20 自然 20，敌人攻击 PC | 自动命中；正常伤害骰 + 伤害骰最高可能值，固定修正不翻倍 | DESIGNED |
| DH-T18 | DH-SPOTLIGHT | PC Failure with Hope 后，GM 作 Move | GM 获得聚焦；后果应为轻微；GM Turn 结束后聚焦回到 PC | DESIGNED |

## 版本与扩展隔离用例

| ID | 覆盖范围 | 检查 | 状态 |
|---|---|---|---|
| DH-V01 | Core / Hope & Fear | Core 角色创建列表只读取 9 Core Classes，不出现 Assassin / Brawler / Warlock / Witch | DESIGNED |
| DH-V02 | Core / Hope & Fear | Core Domains 只包含九大核心领域，不加载 Dread | DESIGNED |
| DH-V03 | Mixed Version | 运行时不会自动加载 Character Creation / Classes / Domains 混合章节 | DESIGNED |
| DH-V04 | Optional Procedures | Supplemental Campaign Mechanics 默认关闭 | DESIGNED |
| DH-V05 | Dataset | Core Adversaries / Environments 数量分别为 129 / 19 | DESIGNED |

| DH-T19 | DH-BUCKLER | Armor Score 3，已有 1 个 Armor Slot 标记；遭受攻击并触发 Buckler: Deflecting | 分别记录 SRD 2.0 PDF 的 “available Armor Score” 与 Errata/网页 Changelog 的 “available Armor Slots” 两种解释；不强行合并 | BLOCKED / DH-I-016 |

## 验收门槛

- 规则时序、资源变化和数值预期均正确；
- 任何失败都能定位到具体 Rule ID 或数据字段；
- 测试不依赖联网查询；
- 扩展隔离测试无泄漏；
- 至少完成一次独立干净上下文的端到端短场景测试，才考虑把 candidate 规则系统接入正式 Campaign。

本文件定义测试，不表示任何用例已经执行。