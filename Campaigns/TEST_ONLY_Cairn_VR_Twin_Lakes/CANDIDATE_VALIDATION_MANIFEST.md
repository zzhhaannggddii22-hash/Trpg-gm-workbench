# Candidate Validation Manifest｜Twin Lakes VR

```yaml
validation:
  mode: CANDIDATE_VALIDATION
  canon_status: TEST_ONLY_NON_CANON
  validation_id: CAIRN-VR-TWIN-LAKES-01
  system_id: cairn
  ruleset_version: Cairn Second Edition
  preflight_base_commit: 245fca27b3c2570ea3be0781648bef204e70c36f
  source_archive_commit: 1689b2eff7901df2043a74c357bb52de67210aee
  gm_prep_commit: cc49fa84edd8d11bcb9e7fdbd221d8589f860207
  latest_prep_revision_commit: 16cb335b597732d6d3fc96963c9d40752c01664d
  module_source_path: Campaigns/TEST_ONLY_Cairn_VR_Twin_Lakes/SOURCE/CAS1_OFFICIAL_SOURCE.md
  gm_prep_path: Campaigns/TEST_ONLY_Cairn_VR_Twin_Lakes/GM_ONLY_PREP.md
  module_source_retrieved_at: 2026-11-27
  official_release_note_verified_at: 2026-03-31
  module_source_license: CC-BY-SA-4.0
  fasha_hp_status: GM_INFERENCE_10HP_SECONDARY_PDF_CORROBORATION
  fixture_entry: Campaigns/TEST_ONLY_Cairn_VR_Twin_Lakes/README.md
  runner_chat: "GM preparation in this conversation; character creation in a separate conversation"
  started_at: null
  completed_at: null
  result: pending
  runtime_status: NOT_STARTED
  start_authorization: NOT_GRANTED
  scope:
    - "CAS-1: Trouble in Twin Lakes"
    - "Two-player-character party: user-controlled PC plus assistant-controlled Katherine PC"
    - "Cairn 2e rules execution and exploration"
    - "Katherine PC autonomy, knowledge boundary, continuity, and full PC-level resource and survival rules"
    - "VR roleplay frame with Triangle Agency Katherine personality reference"
  prohibited:
    - importing Triangle Agency mechanics, stats, resources, or campaign state
    - treating this candidate validation folder as a formal active Campaign
    - writing test characters, NPCs, events, or state into a formal Campaign
    - treating synthetic preparation as independent blind validation
    - revealing GM-only module information in player-facing narration or leaking it into Katherine's character knowledge
```

## 桌面约定

- 队伍规模基准为两名玩家角色：用户控制的 PC + 助理控制的凯瑟琳 PC。
- 凯瑟琳在规则身份上就是玩家角色，不是普通 NPC。她完整适用 Cairn 2e 玩家角色规则，包括伤害、生存、HP 归零后的 Scars / Critical Damage、STR 归零死亡、成长和资源消耗；不享有任何 NPC 简化、豁免或保护。
- 两人均有完整、同粒度的玩家级资源账本。凯瑟琳不得拥有免费、无限或不记录的补给。
- 难度评估按两名冒险者进行；不按单 PC 缩放，也不默认凯瑟琳是额外第三名冒险者。
- 用户决定自己 PC 的行动；助理决定凯瑟琳 PC 的行动。凯瑟琳拥有独立目标、偏好、判断和行动权。
- GM 与凯瑟琳的角色决策严格独立。GM-only 信息不会自动成为凯瑟琳的角色知识；她只能依据自身背景、观察、交流和实际经历行动。
- L3 仅表示角色模拟投入等级，不是 Cairn 官方等级，也不改变凯瑟琳的 PC 身份或规则待遇。
- 本次角色卡和游戏世界状态只在本验证目录内有效。
- 角色卡由独立会话创建，最终状态须由用户确认后同步；草案不作为正式输入。
- 只有用户明确授权开始后才进入游戏。

## 系统状态

Cairn 仍为 candidate。此 Manifest 仅授权 TEST_ONLY_NON_CANON 验证，不改变系统登记状态，不创建正式 Campaign Binding。

## 本次 Preflight 归档与状态说明｜2026-11-27

- 已将当前可访问的官方上游 Markdown 完整归档至 `SOURCE/CAS1_OFFICIAL_SOURCE.md`。
- 已建立主持侧专用 `GM_ONLY_PREP.md`，供后续直接读取，不必每次重新搜索网页。
- 官方 Cairn Press 2026-03-31 发布说明称已补入 Fasha HP；当前上游 Markdown 对应数据行仍无 HP。另一个 PDF 文本副本显示 Fasha 为 10 HP，因此当前采用 GM_INFERENCE: 10 HP；官方 PDF 本轮未直接读取，不能将该数值标为官方数据。
- 当前归档包含完整 Markdown 原文；相对图片与链接已规范化为官方站点绝对路径以便 GitHub 显示。PDF 二进制本身未归档。
- 用户 PC 与 Katherine PC 的最终人物卡将在之后提供；本次不生成、不预填。
- Runtime State revision 0、Session Log 空记录保持不变。当前尚未获得开始授权，不建立 NEW START 检查点、不初始化场景、不推进时间。