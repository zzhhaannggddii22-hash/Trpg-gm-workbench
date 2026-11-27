# Twin Lakes｜Session Log（GM-only）

> Visibility: GM_ONLY  
> Campaign: `CA01_Zaf`  
> Module: `CAS-1`  
> Log status: `INCIDENT_RECORD_ESTABLISHED / HISTORICAL_SESSIONS_NOT_RECONSTRUCTED`

## 记录约定

- 本文件保存 GM-only 事件、状态差分与运行事故；不得直接复制为 Player Notes 或玩家交接。
- 游戏内事件必须有实际发生依据。运行事故、仓库维护和测试活动不是游戏内事件，不分配虚构的 session event ID，也不推进游戏时间。
- 历史记录缺失时保留 UNKNOWN；不得从模组 Prep、NPC 档案或模型回忆补写对话、行动顺序、场景和状态差分。
- 玩家可见信息必须单独通过 Runtime §14.8 / §14.19 的字段级准入，再写入 [05_PLAYER_NOTES.md](./05_PLAYER_NOTES.md)。

## 0. 历史 Session 状态

| 项目 | 状态 |
|---|---|
| 既往 Session ID / 编号 | UNKNOWN / NOT_RECONSTRUCTED |
| 游戏内时间线 | UNKNOWN / NOT_RECONSTRUCTED |
| 逐轮行动与 GM 回复 | UNKNOWN / NOT_RECONSTRUCTED |
| 最新地点 / 场景 / 事件节点 | UNKNOWN / NOT_RECONSTRUCTED |
| 历史状态差分与资源变化 | UNKNOWN / NOT_RECONSTRUCTED |
| 玩家呈现锚点 | INCOMPLETE |
| NPC 知识变化 | REQUIRES_SOURCE_REVIEW |

不得将本节解释为“没有发生过游戏”。它只表示当前可访问的权威仓库记录不足以重建历史 Session。

## 1. Operational Incident｜Issue #87

- Incident reference: [GitHub Issue #87](https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/87)
- Incident class: `PLAYER_FACING_INFORMATION_BOUNDARY_FAILURE`
- Severity recorded by issue: `P1`
- Issue registration date: `2026-11-27`（仅登记日期；泄露实际发生时间仍为 `UNKNOWN`）
- Exact in-game occurrence time / Session ID: `UNKNOWN`
- Current status: `OPEN`

### Verified incident scope

A player-visible context handoff summary in the live Twin Lakes / CAS-1 run contained GM-only module information. The original user-visible exposure is acknowledged and remains part of the incident history.

本记录不复制隐藏内容，也不把 GM-only 模组资料重新摘要到 Session Log。Issue #87 保留原始缺陷描述与时间线更正。

### Character-knowledge impact

- User/player exposure and in-fiction PC/NPC acquisition are separate.
- No PC or NPC gains knowledge merely because the user saw the handoff summary.
- Any subsequent PC/NPC suggestion, decision or investigation step that relied on the leaked material is not admitted as character knowledge on that basis.
- Where a specific later utterance or action cannot be traced to a lawful in-fiction source, keep that claim quarantined pending source review.
- Do not undo the user's actual exposure by pretending the disclosure did not occur; preserve the original evidence and append any future correction.

### Required recovery evidence

1. Locate the original accessible handoff/transcript and establish what was actually presented, to whom, and at what point.
2. Trace any subsequent player action or NPC output that depended on the exposed information.
3. Rebuild the player projection only from lawful in-fiction acquisition and presentation events.
4. Verify that NPC knowledge is separately grounded in each NPC's own acquisition history.
5. Run the independent player-channel / handoff regression before considering closure.

### Resolution

`UNRESOLVED`. This entry is an operational incident record, not a fictional event, not a retroactive retcon, and not proof that the issue is fixed. Repository edits and document readback alone do not close Issue #87.

## 2. Future Session records

Append each actual Session below with its real identity and order. Do not backfill a historical scene from GM-only materials.

```yaml
session_record:
  session_id: UNKNOWN
  status: NOT_RECORDED
  in_game_start: UNKNOWN
  in_game_end: UNKNOWN
  events: NOT_RECONSTRUCTED
  player_presentation_refs: UNKNOWN
  runtime_checkpoint_ref: UNKNOWN
```
