# Campaign System Binding｜CA01_Zaf

```yaml
campaign_id: ca01_zaf
campaign_name: Twin Lakes
campaign_directory: Campaigns/CA01_Zaf
system_id: cairn
system_entry: Systems/Cairn/README.md
ruleset:
  name: "Cairn / 石冢"
  edition: "Second Edition"
  language: "zh-CN"
  authority: "Cairn 2e 官方英文 SRD；社区简体中文 SRD 作为阅读参考"
status: controlled_live_candidate
activation: USER_AUTHORIZED_CONTROLLED_LIVE_USE
canon_status: in_progress
system_maturity: candidate
runtime_readiness: RECONCILIATION_REQUIRED
runtime_authorization:
  scope: CA01_Zaf_ONLY
  system_promotion: NOT_GRANTED
  cross_session_resume: HOLD_PENDING_RECONCILIATION
player_characters:
  - Zaf
assistant_controlled_party_members:
  - Jubilo
resting_characters:
  - Catherine
next_session_party:
  - Zaf
  - Jubilo
```

## 跨战役连续性隔离（硬性规则）

Twin Lakes（Cairn 2e）与 Triangle Agency 是两条完全独立的战役连续性。它们共享部分角色的身份/人格建模参考，但不共享事件因果、记忆、成长或世界状态。

### Triangle Agency 的冻结基准

Twin Lakes 战役开始时，Triangle Agency 中扎雷克与凯瑟琳的状态，以本目录下的**只读历史人物信息快照**为唯一基准：

- [扎雷克｜Triangle Agency 人物快照（2026-11-27）](./跨战役基准快照/TA_Zarek_2026-11-27_Snapshot.md)
- [凯瑟琳｜Triangle Agency 人物快照（2026-11-27）](./跨战役基准快照/TA_Catherine_2026-11-27_Snapshot.md)

快照记录的是开启 Twin Lakes 时，Triangle Agency 已建立的人物信息与发展状态。它们是历史锚点，不随 Triangle Agency 后续人物卡更新而变化，也不由 Twin Lakes 事件改写。

### 隔离规则

- Twin Lakes 中发生的任何事件、关系变化、经历、物品、伤害、成长、资源变化、记忆与世界后果，**不得回写、传递或影响 Triangle Agency 的 CANON**。
- Twin Lakes 中凯瑟琳作为 VR 玩家角色的行动与经历，不会成为 Triangle Agency 凯瑟琳的亲历、记忆或人物发展。
- Twin Lakes 中 Zaf 的经历也不会成为 Triangle Agency 扎雷克的经历、记忆或成长。
- Triangle Agency 中扎雷克与凯瑟琳在快照基准之后的发展，只沿 Triangle Agency 自身战役记录继续；不得将 Twin Lakes 的后续内容当作其发展素材。
- 两条战役可以复用用户明确允许共享的角色身份/人格参考，但不能据此建立跨战役记忆、关系、资源、伤害、物品或事件因果。
- 只有用户明确提出跨战役迁移某项内容时，才可针对该项内容另行处理；默认禁止迁移。

## 规则与状态边界

- 本 Campaign 仅绑定 Cairn Second Edition；不得混入 Triangle Agency 规则、资源、术语或运行逻辑。
- Cairn 在 GM Workbench 中仍为 candidate。用户授权的 CA01_Zaf 受控实战仅对本 Campaign 有效，不构成系统级 active 认证，也不自动授权其他 Cairn Campaign。
- 本 Campaign 已进入实际运行；candidate 是系统成熟度，不得再被解释为“战役尚未开始”或“没有玩家可见事件”。
- 跨会话续接当前为 RECONCILIATION_REQUIRED。恢复前不得从 GM-only Prep 重建玩家经历、NPC 认知或玩家摘要；具体边界以本目录 03_RUNTIME_STATE.md、04_SESSION_LOG.md 和 05_PLAYER_NOTES.md 为准。
- 规则入口：[Systems/Cairn](../../Systems/Cairn/README.md)。
- 核心运行手册：[CORE_RULES_RUNTIME.md](../../Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md)。
- 角色创建与背景速查：[CHARACTER_CREATION_AND_BACKGROUNDS.md](../../Systems/Cairn/Rule_Reference/CHARACTER_CREATION_AND_BACKGROUNDS.md)。
- Campaign 目录命名：[CAMPAIGN_NAMING.md](../../CAMPAIGN_NAMING.md)。

## 角色扮演约定

- Zaf 是玩家在 Twin Lakes VR 游戏世界中的角色，由玩家本人控制。
- Zaf 的实际性格、台词、语气与行动由玩家现场扮演；骰出的角色特征仅作为特征表结果记录，不替玩家决定人格或说话风格。
- 外貌以扎雷克形象为准；Cairn 的外貌特征骰只记录为风格特性，不覆盖既有外观。
- 凯瑟琳是独立 PC，由助手控制，具有独立人物卡、资源与行动逻辑；她不得读取 GM-only 信息，也不得为了配合 Zaf 而自动服从。下次开局她休止，不随队、不参与该次冒险；人物卡与状态继续保留。
- 凯瑟琳的既有视觉身份与人格风格可以作为角色扮演参考；Triangle Agency 的背景履历、异常能力、QA、Chaos、Burnout、机构关系与资源不适用于 Cairn。
- 凯瑟琳本人是在玩 VR 游戏，以她自己的风格游玩，不必扮演游戏角色随机生成的性格。
- 队伍 Omen：Zaf 为当前最年轻角色，触发 Omen；结果 d20 = 2，已向玩家公开，见 README 与 Zaf 人物卡。
- 茱比洛（Jubilo）是本战役正式 L3 NPC 队员，由助手控制，采用本战役配置的 PC 等价资源与机制；她有独立目标、判断、资源管理与行动权，不是测试角色。
