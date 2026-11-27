# Resource Ledger｜Blame It on the Trains

> GM-only。模组级资源唯一流水。当前为空账本；禁止从历史人物卡快照猜测本模组开场余额。

## 开场核对

- Session：NOT STARTED
- Character snapshot source：待 Preflight 核对正式人物卡
- Previous module close source：Bower Street 最新结案记录
- Time：结团 +1 已确认；绝对可用余额待权威流水核对
- Disputed values：若存在冲突，先登记 DISPUTED，不计算、不覆盖

## 结团后开场基线（权威字段；Preflight 必须回读）
- Commendations：18（人物卡 2026-11-27 结团后快照）。
- QA：任务间恢复满额；Attentiveness 上限/可用 2/2；其他素质按人物卡核验。
- Demerits：非零，精确余额 UNKNOWN；不得沿用旧快照 0 或猜测。
- Harm：UNKNOWN / NEEDS RULE-BASED RECONCILIATION。
- 普通 Chaos Pool：模组内临时资源；Bower Street 结团时清零，本模组建立独立初值，不继承旧池。
- Ripple Gun：结团按规则恢复满额 1/1；Preflight 点交。
- Loose Ends：Campaign 基线 1；Bower Street 模组增量 +0；本模组单独记录增量。
- Time：Bower Street 完整结团 +1 已确认；绝对余额 UNKNOWN，不从 Work/Life Balance 轨迹反推。

## 资源作用域
- QA：Session 内消耗；任务间按规则恢复至上限。
- 普通 Chaos Pool：模组内临时资源，模组结团清零；保留历史流水。
- Ripple Gun：记录使用流水；按规则在任务间/模组结束恢复满额。
- Commendations、Demerits、Time：跨模组持续资源，逐笔记账。
- Loose Ends：模组级累计指标，记录 Campaign 基线与本模组增量；+0 也要明确记录。

## Ledger

| Entry ID | Session | Timestamp | Resource | Delta | Balance After | Source/Event | Verification |
|---|---|---|---|---:|---:|---|---|
| — | — | — | — | — | — | EMPTY | — |

## 记账规则

1. 每笔资源交易在发生时追加唯一 Entry ID。
2. 资源余额只由本账本流水计算；不在 Session Log、Runtime State 或模组 README 重复维护余额。
3. Session Log 只引用 Entry ID。
4. 模组公共资源与角色资源分开标注 owner。
5. Session 结束对账；模组结团时结算系统规定的奖励/惩罚。
6. Time 的本桌触发条件为完整模组结团 +1；单独 Session 结束不增加。
7. 无来源的历史数值标记 UNKNOWN，不以倒推方式填补。
