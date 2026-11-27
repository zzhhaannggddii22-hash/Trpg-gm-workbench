# Twin Lakes｜Runtime State（GM-only）

> Visibility: GM_ONLY  
> Campaign: `CA01_Zaf`  
> System: `cairn / Cairn Second Edition`  
> Module: `CAS-1`  
> Status: `RECONCILIATION_REQUIRED`  
> This file is a recovery shell, **not** a reconstructed Session snapshot or proof of external host persistence.

## 1. Authority and current binding

- Campaign binding: [SYSTEM_BINDING.md](./SYSTEM_BINDING.md)
- Campaign authorization: `USER_AUTHORIZED_CONTROLLED_LIVE_USE`, scoped only to `CA01_Zaf`
- System maturity: `candidate`; no system-wide promotion to `active`
- Campaign / Module: Twin Lakes / CAS-1
- Current party baseline: Zaf (player-controlled PC) and Jubilo (assistant-controlled L3 NPC); Catherine is resting and not part of the current party.
- Player-visible knowledge projection: [05_PLAYER_NOTES.md](./05_PLAYER_NOTES.md)
- GM-only operational record: [04_SESSION_LOG.md](./04_SESSION_LOG.md)

## 2. Recovery state

```yaml
runtime_status: RECONCILIATION_REQUIRED
snapshot_kind: RECOVERY_SHELL_NOT_HISTORICAL_CHECKPOINT
system_id: cairn
ruleset_version: Cairn Second Edition
campaign_id: ca01_zaf
module_id: CAS-1
resume:
  mode: CONTINUE_RECONCILIATION
  current_chat_continuation: ONLY_FROM_ACTUALLY_VISIBLE_CURRENT_TRANSCRIPT
  cross_session_continuation: HOLD_PENDING_RECONCILIATION
  full_recap_generation: HOLD_PENDING_PLAYER_PROJECTION_REVIEW
  can_claim_historical_checkpoint: false
session:
  session_id: UNKNOWN
  session_number: UNKNOWN
  game_time: UNKNOWN
  current_location: UNKNOWN
  current_scene_id: UNKNOWN
  current_scene_status: UNKNOWN
  last_event_id: UNKNOWN
  last_player_action: UNKNOWN
  last_gm_response: UNKNOWN
  pending_player_choice: UNKNOWN
history:
  prior_session_events: NOT_RECONSTRUCTED
  state_deltas: NOT_RECONSTRUCTED
  player_presentation_anchors: INCOMPLETE
  npc_knowledge_projection: REQUIRES_REVIEW
  player_knowledge_projection: SEE_05_PLAYER_NOTES
incidents:
  - ref: https://github.com/zzhhaannggddii22-hash/Trpg-gm-workbench/issues/87
    status: OPEN
    category: PLAYER_FACING_INFORMATION_BOUNDARY
    campaign_knowledge_effect: NO_AUTOMATIC_KNOWLEDGE_GRANT
```

## 3. Field-level known / unknown state

| Domain | Current value | Authority / recovery rule |
|---|---|---|
| System and ruleset | Cairn 2e | SYSTEM_BINDING |
| Campaign and module identity | Twin Lakes / CAS-1 | SYSTEM_BINDING and campaign README |
| Current party baseline | Zaf + Jubilo | Campaign README and SYSTEM_BINDING |
| Catherine participation | Resting; not in current party | SYSTEM_BINDING |
| Public Omen | d20 = 2; winter arrives early; frost patterns resemble a map | Publicly disclosed campaign record; also in 05_PLAYER_NOTES |
| Session identity and sequence | UNKNOWN | Recover only from original session evidence |
| In-game time and current location | UNKNOWN | Do not infer from module timelines or prep |
| Last scene / last player action / last GM response | UNKNOWN | Recover from actual transcript or valid Session/Event Log |
| Character resources at the latest played moment | UNKNOWN | Read the authoritative character sheet plus actual post-sheet changes |
| PC knowledge beyond 05_PLAYER_NOTES | NOT_RECONSTRUCTED | Require an actual presentation/acquisition event |
| NPC knowledge after live play | REQUIRES_REVIEW | Rebuild only from lawful acquisition and statement/action sources |

## 4. Information-boundary incident gate

Issue #87 records that GM-only module information entered a player-visible handoff summary.

Required handling:

1. The user's exposure to the handoff text is a player-side information incident; it is not, by itself, an in-fiction acquisition event by Zaf or any NPC.
2. Do not grant PCs or NPCs knowledge based on the leaked handoff, a GM-only source file, a previous summary, or model recollection.
3. Do not let an affected detail select a destination, NPC, investigation route, explanation, or later NPC recommendation.
4. Preserve the original player-visible disclosure as incident evidence; do not silently rewrite history or claim the player never saw it.
5. Only restore a specific fact to character knowledge when an independent in-game acquisition/presentation event is recovered or occurs and its recipient and precision are established.
6. If the source event or recipient cannot be verified, retain `UNKNOWN / QUARANTINED`; do not complete it from GM-only prep.

## 5. Resume gate

**Before a new cross-session continuation or historical recap:**

- Recover the actual session transcript / event evidence available for CA01_Zaf.
- Match each material player-known fact to its actual presentation event, recipient and precision.
- Independently review Zaf and Jubilo/Catherine knowledge; do not copy GM global knowledge into any character.
- Reconcile character sheets, resource changes, location, scene status, last answered action and pending choice from event evidence.
- Update this file and the GM-only Session Log; update Player Notes only with the filtered public projection.
- Read back the saved files and verify that the player projection contains no GM-only or unresolved fields.

Until these steps are complete, do not claim a complete historical restore or produce a full recap from GM-only sources. This gate does **not** prevent unrelated preparation or safe administrative work. A same-chat action may be handled from the actual, visible current transcript and its valid facts; it must not depend on unreconciled leaked content.

## 6. Persistence evidence

- Repository branch at creation: `fix/cairn-runtime-player-projection-a`
- This file's repository presence must be read back from the saved branch before being called committed.
- External runtime-host persistence / automatic recovery: `NOT_VERIFIED`
- No platform-level context access control is claimed by this repository file.
