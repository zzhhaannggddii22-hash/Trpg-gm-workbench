# Zarek Campaign｜Playwall Unlock Ledger

> Status: ACTIVE LEDGER  
> System: `triangle_agency` / 《三角机构》中文 v22  
> Scope: Zarek's complete Work/Life Balance mark history and Playwall authorization.  
> Information class: GM-only. Player-facing disclosures must be separately projected.

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

**Audit result:** A3 was correctly unlocked at the third Competency mark, which was the Ice Cream Truck Mission MVP free mark—not the subsequent Time mark. The A3 promotion and Vault Request effects were substantively applied. The historical files do not contain a separate timestamped “A3 privately read” receipt or a verbatim player disclosure record; therefore the read itself is **NOT_SEPARATELY_RECORDED**, while the unlock and downstream A3 use are supported. This is an evidence/traceability gap, not a confirmed missed unlock or omitted A3 benefit.

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
  read_status: NOT_APPLICABLE | READ | NOT_SEPARATELY_RECORDED | BLOCKED
  effect_status: NOT_APPLICABLE | APPLIED | PARTIAL | DEFERRED | UNKNOWN
  player_disclosure_status: NOT_APPLICABLE | PRESENTED | PARTIAL | NOT_PRESENTED | UNKNOWN
evidence_refs: []
notes: ""
```

Historical corrections must be appended with a correction reference; never rewrite the original event row or upgrade UNKNOWN without new evidence.
