# Zarek Campaign｜Playwall Unlock Ledger

> Status: ACTIVE LEDGER  
> System: `triangle_agency` / 《三角机构》中文 v22  
> Scope: Zarek's complete Work/Life Balance mark history and Playwall authorization.  
> Information class: GM-only. Single-player default: no separate player-private-read or player-sharing receipt is required; player-facing projections still exclude genuinely GM-only secrets.

## 1. Current state (2026-11-27)

| Item | Confirmed state |
|---|---|
| Competency boxes marked | 5 |
| Competency path positions | 1–5 |
| Codes encountered on marked boxes | A3 only |
| Authorized Playwall documents | A3 |
| Other Playwall documents | No authorization established |
| Time spent historically | 2 |
| Bower Street Time award | +1 available Time; not yet spent |
| Bower Street Mission MVP | Free Competency mark already included in the 5 marked boxes |
| Current intermission | OPEN; next Time expenditure and planned VHS-girl interaction not yet executed |

The fifth Competency mark is a free Mission MVP mark from Bower Street. The next Competency code on the v22 path is D4 at position 6. This does **not** authorize D4: no sixth mark has occurred.

## 2. Verified Competency path

The Chinese v22 Work/Life Balance sheet's Competency track follows the printed path from the upper-left start across the top row, turns at the right, then returns along the bottom row from right to left.

| Position | Code | Historical mark state |
|---:|---|---|
| 1 | NONE | MARKED — Dead Quiet Mission MVP |
| 2 | NONE | MARKED — Dead Quiet Time spend |
| 3 | A3 | MARKED — Ice Cream Truck Mission MVP; A3 unlocked |
| 4 | NONE | MARKED — Ice Cream Truck Time spend |
| 5 | NONE | MARKED — Bower Street Mission MVP |
| 6 | D4 | UNMARKED — not authorized |
| 7–8 | NONE | UNMARKED |
| 9 | G3 | UNMARKED — not authorized |
| 10–11 | NONE | UNMARKED |
| 12 | J3 | UNMARKED — not authorized |
| 13–14 | NONE | UNMARKED |
| 15 | N3 | UNMARKED — not authorized |
| 16–17 | NONE | UNMARKED |
| 18 | Q3 | UNMARKED — not authorized |
| 19–20 | NONE | UNMARKED |
| 21 | T3 | UNMARKED — not authorized |
| 22–23 | NONE | UNMARKED |
| 24 | W8 | UNMARKED — not authorized |
| 25–26 | NONE | UNMARKED |
| 27 | Y2 | UNMARKED — not authorized |
| 28–30 | NONE | UNMARKED |

The exact code sequence is **A3 → D4 → G3 → J3 → N3 → Q3 → T3 → W8 → Y2**. Do not treat the code list as an unordered pool.

## 3. Historical mark and unlock audit

### 3.1 Dead Quiet — first formal module

| Order | Mark source | Track | Position | Code | Result |
|---:|---|---|---:|---|---|
| 1 | Mission MVP | Competency | 1 | NONE | No Playwall document |
| 2 | Time spend | Competency | 2 | NONE | No Playwall document |

Evidence: `Campaigns/Zarek/模组/死寂/04_REWARDS_AND_SUPERLATIVES.md` records the MVP free Competency mark and one Time Competency mark. The recorded mark count and order are consistent with positions 1 and 2. Both boxes are blank on the v22 track.

**Audit result:** no Playwall unlock was missed in the recorded Dead Quiet growth.

### 3.2 Ice Cream Truck — second formal module

| Order | Mark source | Track | Position | Code | Result |
|---:|---|---|---:|---|---|
| 3 | Mission MVP | Competency | 3 | A3 | A3 unlocked |
| 4 | Time spend | Competency | 4 | NONE | No additional Playwall document |

Evidence: `Campaigns/Zarek/模组/冰淇淋车_Ice_Cream_Truck/03_RUNTIME_STATE.md` and the formal character card record the third Competency mark as the Associate promotion / A3 unlock, followed by the fourth Time Competency mark. The same Runtime record documents the A3 Vault Request and the designed/ purchased requisition.

**Audit result:** A3 was correctly unlocked at the third Competency mark, which was the Ice Cream Truck Mission MVP free mark—not the subsequent Time mark. The A3 promotion and Vault Request effects were substantively applied. The historical files do not contain a separate timestamped “A3 privately read” receipt or a verbatim player disclosure record. Under the single-player execution mode now adopted, neither is a required progression record. The A3 unlock and downstream A3 use are supported; no missed unlock or omitted A3 benefit is identified.

### 3.3 Nosedive — third formal module

The user-confirmed final closeout explicitly awarded no Mission MVP, no Time, no Competency/Reality/Anomaly growth, and no other rewards. No Work/Life Balance box was marked.

**Audit result:** no Playwall unlock opportunity occurred; no omission detected.

### 3.4 Bower Street — fourth formal module

| Order | Mark source | Track | Position | Code | Result |
|---:|---|---|---:|---|---|
| 5 | Mission MVP | Competency | 5 | NONE | No Playwall document |

Evidence: Bower Street's 2026-11-27 final closeout and the formal character card record the fifth Competency mark as the free MVP mark. The box is blank on the v22 Competency path.

The module awarded +1 available Time, but the Time has **not** yet been spent. A Time award alone does not mark a track box and does not unlock a Playwall document.

**Audit result:** no Playwall unlock was missed in the recorded Bower Street growth so far. The intermission remains OPEN until the +1 Time is spent or explicitly retained, the associated track effects are resolved, and any resulting code is checked.

## 4. Cross-track strike-outs

Two historical Time expenditures each require one terminal available box to be crossed out from the other two tracks. The campaign records confirm that the Reality and Anomaly tracks were each shortened twice.

The historical character sheet text does not preserve exact box coordinates for those four strike-outs. Do not invent positions or claim a code was/was not crossed out based only on a summary. Recover the visual Work/Life Balance sheet before the next expenditure and reconcile the current available-box positions. A crossed-out box does not itself unlock a document.

## 5. Current open work

- [ ] Recover/verify the current visual Work/Life Balance sheet, including Reality and Anomaly crossed-out positions.
- [ ] Record the pending Bower Street +1 available Time as an award already granted but not yet spent.
- [ ] When the player chooses a track, mark the earliest available box and perform the complete Playwall check before advancing.
- [ ] If a code is marked, retrieve only that exact authorized document from the pinned Chinese v22 source.
- [ ] Complete the planned VHS-girl intermission scene and ability/requisition design only after the rules and unlock dependencies are resolved; do not pre-record the ability as unlocked or purchased.
- [ ] Read back the character card, this ledger, and the relevant Campaign state before closing the intermission.

## 6. Append-only event template

```yaml
mark_event_id: "zarek/playwall/<module>/<sequence>"
module_id: ""
source_event_id: ""
mark_source: TIME_SPEND | MISSION_MVP | PROBATION | OTHER_RULE
track: COMPETENCY | REALITY | ANOMALY
box_position: null
box_state_before: AVAILABLE_UNMARKED
box_state_after: MARKED
time_spent: false
cross_outs:
  - track: ""
    box_position: null
track_benefit:
  description: ""
  status: APPLIED | PARTIAL | DEFERRED | UNKNOWN
playwall:
  code: NONE
  authorization: NO_CODE | UNLOCKED | BLOCKED_OR_UNKNOWN
  source_ref: null
  retrieval_status: NOT_APPLICABLE | RETRIEVED | BLOCKED_OR_UNKNOWN
  effect_status: NOT_APPLICABLE | APPLIED | PARTIAL | DEFERRED | UNKNOWN
evidence_refs: []
notes: ""
```

Historical corrections must be appended with a correction reference; never rewrite the original event row or upgrade UNKNOWN without new evidence.


## 7. 2026-11-27｜Bower Street 幕间成长追加记录

> 本节追加修订 §1、§3.4、§5 的历史状态。Bower Street 结团时的原始快照保持不变；本节记录结团后实际发生的幕间成长。

### 7.1 Competency 第 6 格

| Order | Mark source | Track | Position | Code | Mark state | Playwall state |
|---:|---|---|---:|---|---|---|
| 6 | Bower Street intermission / Time spend | Competency | 6 | D4 | MARKED | **AUTHORIZED / RETRIEVAL NOT YET VERIFIED** |

- 玩家明确将 Bower Street 结团获得的 +1 可使用 Time 投入 Competency。
- 成长后 Competency 累计标记 6 格；按已核实的 v22 轨迹顺序，第 6 格代码为 D4。
- D4 对应 Playwall 文档现已获得授权。读取与核对正文后，才可将 retrieval_status 更新为 RETRIEVED；本记录不复制或披露隐藏文档正文。
- 本次轨迹成长收益：Duplicity QA 上限 +1（1 → 2），由玩家明确确认。
- 本次 Competency 成长奖励：+3 Commendations；Requisition「空白片段（Blank Interval）」随后购买 -20 Commendations。

### 7.2 交叉轨迹划除坐标

- 规则要求本次 Time 支出对 Reality 与 Anomaly 轨迹各划除一个末端可用格。
- 历史两次 Time 支出的四个划除坐标仍未从原始视觉 Work/Life Balance 表恢复；本次划除坐标同样暂记 **UNKNOWN / PENDING VISUAL RECONCILIATION**。
- 不得仅凭轨迹摘要推测坐标或代码。恢复原始视觉表后追加坐标核验；划除本身不产生 Playwall 解锁。

### 7.3 当前进度覆盖视图

| Item | Current confirmed state |
|---|---|
| Competency boxes marked | **6** |
| Competency path positions | **1–6** |
| Codes encountered on marked boxes | **A3, D4** |
| Authorized Playwall documents | **A3, D4** |
| D4 document retrieval | **PENDING VERIFICATION** |
| Bower Street Time award | +1 granted and now spent on Competency |
| Duplicity QA cap | 2 |
| Commendations after growth and Requisition purchase | 1 |

### 7.4 Append-only event

- mark_event_id: `zarek/playwall/bower-street/intermission-006`
- module_id: `Bower Street`
- mark_source: `TIME_SPEND`
- track: `COMPETENCY`
- box_position: `6`
- box_state_before: `AVAILABLE_UNMARKED`
- box_state_after: `MARKED`
- time_spent: `true`
- track_benefit: `Duplicity QA cap +1; APPLIED`
- playwall: `D4; UNLOCKED; retrieval PENDING VERIFICATION`
- cross_outs: `Reality UNKNOWN; Anomaly UNKNOWN; pending visual reconciliation`
- evidence_refs: `Bower Street Resource Ledger BOWER-RES-016–021; formal character card 2026-11-27 intermission entry`


## 8. 2026-11-27｜D4 文档读取与交叉轨迹坐标重建

> 本节覆盖 §1 的历史状态快照、§7.1 的 D4 retrieval pending、§7.2 的坐标 UNKNOWN，以及 §7.3 中 D4 pending verification 的旧状态。原事件记录保持不变。

### 8.1 D4 retrieval

| 字段 | 核验结果 |
|---|---|
| 授权来源 | Competency 第 6 格，D4 |
| 授权状态 | UNLOCKED |
| 文档读取 | **RETRIEVED / SOURCE VERIFIED** |
| 权威来源 | 中文 v22 固定提交 `7f6d52f40bbd3ff1a6c383ba2431c9aecda283b1` |
| 源 PDF 页码 | 216–217 |
| 印刷页码 | 212–213 |
| 文档代码 | 两页均标记 D4；按连续两页完整读取 |
| 读取范围 | 仅 D4 两页；未读取 D5 或其他相邻代码 |

**已应用的角色收益与玩家可知内容：**

- Triage 应用程序访问权限已开放，包含 OPUS、GRETA、BIX 三项工具。
- D4 提供涟漪（Ripple）与大厅（Lobby）的基础说明。
- D4 涟漪驱动补给目录现可查询：iPond（9）、Gripples（15）、Li'l Rebels Talking Dolls（9）、The Bouncer（6）、AnglerVision（6），单位均为 Commendations。
- 目录解锁不自动购买补给；本次没有发生 D4 目录购买，当前 Commendations 余额为 1。
- 第 6 格同时对应 Senior Associate（高级助理）晋升；正式人物卡职级已更新。

### 8.2 Reality / Anomaly cross-out reconstruction

**证据基础：**

1. 中文 v22 的 VISUAL_299 Work/Life Balance 表：三条轨迹均按上排左→右、右端折返、下排右→左读取；末端位于下排最左侧。
2. Reality 轨迹共 30 格；Anomaly 轨迹使用相同的 30 格轨迹布局。
3. 历史 Time 支出顺序由各模组记录确认：Dead Quiet 一次、Ice Cream Truck 一次；Bower Street 幕间为第三次。
4. Dead Quiet 与 Ice Cream Truck 的免费 Mission MVP 标记均为 Competency；Nosedive 没有任何成长；Bower Street Mission MVP 也为 Competency。现有记录未发现 Reality 标记或 Probation 导致的 Anomaly 标记。

**重建结果：**

| Time 支出 | 模组／事件 | 被标记轨迹与格位 | Reality 末端划除 | Anomaly 末端划除 |
|---:|---|---|---|---|
| 1 | Dead Quiet | Competency 第 2 格 | 第 30 格／下排第 1 格（最左） | 第 30 格／下排第 1 格（最左） |
| 2 | Ice Cream Truck | Competency 第 4 格 | 第 29 格／下排第 2 格 | 第 29 格／下排第 2 格 |
| 3 | Bower Street intermission | Competency 第 6 格（D4） | 第 28 格／下排第 3 格 | 第 28 格／下排第 3 格 |

- 当前 Reality 与 Anomaly 均已划除下排第 1–3 格；两轨各剩 27 个可用格（不含其他未来标记）。
- 若后续没有其他轨迹标记改变末端可用位置，下一次 Time 支出的末端划除将是第 27 格／下排第 4 格。
- 坐标证据等级：**RULE-DETERMINISTIC RECONSTRUCTION**。GitHub 与 Library 中未找到扎雷克本人已填写的原始 Work/Life Balance 图片；因此本记录不是图片像素直接核验。坐标由官方版面路径、轨迹长度和完整可恢复事件顺序确定。
- 若未来找到扎雷克本人原始填表图片，应作为独立视觉复核；如图片与本重建不符，保留本事件并追加勘误，不静默覆盖。

### 8.3 Current override

| 项目 | 当前状态 |
|---|---|
| Competency 标记 | 6 格（位置 1–6） |
| 晋升 | Associate → **Senior Associate** |
| Playwall 授权 | A3、D4 |
| D4 retrieval | **RETRIEVED / SOURCE VERIFIED** |
| Time spend | 3 次 |
| Reality cross-outs | 第 30、29、28 格（下排左起第 1–3 格） |
| Anomaly cross-outs | 第 30、29、28 格（下排左起第 1–3 格） |
| 下一末端划除（若无其他标记） | 第 27 格／下排左起第 4 格 |


### 8.4 官方空白人物表的视觉版面复核

- 已从出版方资源页取得官方可打印人物表，并检查第 3 页（Work/Life Balance）。
- 官方表格视觉确认：Competency、Reality、Anomaly 三条轨迹均为 **上下两排、每排 15 格，共 30 格**；路径从上排左→右，到右端折返，再沿下排右→左。
- 因此物理坐标映射已得到官方版面确认：末端第 1 格 = 下排最左格（第 30 格）；末端第 2 格 = 下排左起第 2 格（第 29 格）；末端第 3 格 = 下排左起第 3 格（第 28 格）。
- 官方空白表只验证轨迹几何，不显示扎雷克本人的标记；扎雷克个人已填写版仍未找到。故最终证据等级保持 **RULE-DETERMINISTIC RECONSTRUCTION + OFFICIAL TEMPLATE VISUAL VERIFIED**，不声称已目视核对个人填写版。
- Official publisher source: https://cdn.shopify.com/s/files/1/0581/0464/3719/files/Triangle_Agency_-_Character_Organization_Sheets_-_For_Print.pdf#page=3


## 9. D4 补给目录进入长期可选嘉奖商店

- 玩家明确要求：D4 解锁的五件涟漪驱动补给进入扎雷克的**可选 Commendations 购买商店**。
- 商品目录：iPond（9）、Gripples（15）、Li'l Rebels Talking Dolls（9）、The Bouncer（6）、AnglerVision（6）。
- 此记录代表长期可选购买资格，不代表已购买、已预留预算或自动扣款。
- 每次展示扎雷克可用的嘉奖购买选项时，必须包含这五件商品；即使当前余额不足，也保留在商店目录中并标明暂不可购买。
- 购买必须由玩家明确确认；价格以 Commendations 计，使用时的 QA 消耗按各商品 D4 规则另行支付。
- 记录时当前 Commendations 余额为 1，五件商品当前均不可购买。
