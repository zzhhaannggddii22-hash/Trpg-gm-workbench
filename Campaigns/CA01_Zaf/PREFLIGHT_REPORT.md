# Twin Lakes｜Cairn 2e Preflight Report

> Campaign: `CA01_Zaf`
> Branch: `feat/cairn-second-system-integration`
> Review date: 2026-11-27
> Result: `PREFLIGHT_COMPLETED_WITH_OPEN_ITEMS`
> Activation: `BLOCKED / NOT ACTIVATED`
> Game start: `NOT STARTED`

## 1. Scope and hard boundaries

This review prepares the Twin Lakes campaign only. It does not start play, advance in-game time, create fictional events, resolve encounters, or alter character state.

Twin Lakes is bound to Cairn Second Edition only. Triangle Agency continuity is isolated. The two read-only historical snapshots in `跨战役基准快照/` remain the sole baseline for the corresponding Triangle Agency characters at Twin Lakes' eventual start. No Twin Lakes event, memory, relationship, item, injury, growth, or world consequence may be written back to Triangle Agency.

## 2. Authoritative branch and campaign records

All campaign-specific files were checked on `feat/cairn-second-system-integration`, not inferred from the repository default branch.

- Campaign: `Campaigns/CA01_Zaf/README.md`
- Binding: `Campaigns/CA01_Zaf/SYSTEM_BINDING.md`
- Zaf: `Campaigns/CA01_Zaf/人物档案/Zaf_人物卡.md`
- Catherine: `Campaigns/CA01_Zaf/人物档案/凯瑟琳_人物卡.md`
- Triangle Agency frozen snapshots: `Campaigns/CA01_Zaf/跨战役基准快照/`

Both character cards and the binding were found on the authoritative branch. No character-card values were changed during this Preflight.

## 3. System and rules readiness

Bound system: Cairn Second Edition. Official English SRD is authoritative; the community Chinese SRD is a reading aid only.

Reviewed system references:
- `Systems/Cairn/README.md`
- `Systems/Cairn/PREFLIGHT.md`
- `Systems/Cairn/RUNTIME_PROTOCOL.md`
- `Systems/Cairn/GM_SKILL.md`
- `Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md`
- `Systems/Cairn/Rule_Reference/CORE_RULE_INDEX.md`
- `Systems/Cairn/Rule_Reference/CHARACTER_CREATION_AND_BACKGROUNDS.md`
- `Systems/Cairn/Rule_Reference/WARDEN_GUIDE_INDEX.md`
- `Systems/Cairn/Testing/CANDIDATE_VALIDATION_MANIFEST.md`

The runtime manual is v0.2 and explicitly remains incomplete as a full rules audit. Some rules are marked PARTIAL or MODULE_DEPENDENT. The system index also lists topics still requiring further verification, including complete growth, hireling, pointcrawl, Warden tools, and other detailed procedures. Therefore this Preflight does not certify Cairn as an active system. Any such rule encountered in play must be checked against the relevant official Cairn 2e text; unknown rules remain UNKNOWN rather than being filled from another system.

## 4. Party and character audit

Party control:
- Zaf: player-controlled PC.
- Catherine: assistant-controlled, independent PC.
- No hirelings are currently registered.
- Catherine is not a subordinate, equipment carrier by default, or automatic bodyguard. She has independent goals, judgement, risk limits, and resource accounting.

Starting character values and inventories were read from the two authoritative character cards. No random result was regenerated.

| Character | Background | STR | DEX | WIL | HP | Armor | Inventory | Backpack |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Zaf | Fieldwarden | 14 | 13 | 13 | 2 | 1 | 8/10 | 3/6 |
| Catherine | Bonekeeper | 9 | 10 | 13 | 5 | 0 | 7/10 | 4/6 |

Resources and notable items:
- Zaf: rations 3 uses; torches 3 uses; repellent 3 uses (player-selected target: beasts); bloodied bone knife d6; hand axe d6; sling d6; brigandine Armor 1, Bulky; wolf-tooth necklace (custom, once per module); two Bond Petty items; 14 GP.
- Catherine: rations 3 uses; lantern; oil 6 uses; stake d6; 10-foot chain; plague doctor mask; pulley; crystal prism Bond item; 9 GP.
- Catherine currently has no Fatigue. Her armor is 0.
- All Petty items and money pouches remain outside slot accounting, as recorded on the cards.

### Character creation audit: Bonds decision resolved

Zaf's two Bonds were originally recorded as results 7 and 3 with d10 notation. Cairn 2e uses a d20 Bonds table. Both numbers map to valid entries on the d20 table, but the original die-type notation is incorrect.

The player explicitly chose to **retain the existing results 7 and 3 without rerolling**. The two Bond entries and their associated items are therefore confirmed and remain unchanged. The original d10 notation is preserved as a historical audit note; it is not silently rewritten as a d20 roll and is not represented as correct official procedure. This decision is closed and must not be raised again as an unresolved player choice.

## 5. Module archive

The CAS-1 official source archive and GM-only preparation have been placed under:

- `Campaigns/CA01_Zaf/MODULES/CAS-1/SOURCE/CAS1_OFFICIAL_SOURCE.md`
- `Campaigns/CA01_Zaf/MODULES/CAS-1/GM_ONLY_PREP.md`
- `Campaigns/CA01_Zaf/MODULES/CAS-1/MANIFEST.md`

The source archive retains the upstream attribution and CC-BY-SA 4.0 license notice. The GM-only preparation is separated from player-facing records. It must never be surfaced as Catherine's knowledge or presented to the player as discovered facts.

Known source discrepancy retained in the module manifest: the upstream Markdown does not show Fasha's HP, while the 2026-03-31 official release note says HP was added. The 10 HP value in the existing prep is a provisional GM_INFERENCE supported by a secondary PDF text copy, not a directly verified official-PDF value. It must not be described as official until the official PDF is directly checked. This does not justify inventing a replacement value.

## 6. Module and party risk

CAS-1 was prepared as a Cairn 2e adventure. Its two central mysteries are independent causal threads; shared people and locations do not make them one conspiracy. Module-specific event clocks and encounter procedures are preserved in GM-only prep.

The current party has two PCs, one of whom is assistant-controlled. Zaf begins with only 2 HP and Catherine with 5 HP; Cairn combat is dangerous. No difficulty reduction, hidden protection, extra hireling, or rule modification has been applied. Before play, the Warden must present observable risks honestly and allow retreat, avoidance, negotiation, and other approaches. Catherine's independent-PC role must not be used to erase the party's resource or action constraints.

## 7. Omen

The party Omen is already recorded and publicly disclosed: d20 = 2, winter arrives early and frost patterns resemble a map. It is an established world fact, but no connection to a specific CAS-1 location, NPC, or event has been assumed.

## 8. Runtime and session state

No `03_RUNTIME_STATE.md` or `04_SESSION_LOG.md` existed in `Campaigns/CA01_Zaf` on the checked branch. Neither was fabricated during this Preflight.

No in-game time, location, encounter, NPC action, resource expenditure, or event has been initialized. No runtime checkpoint was created. The campaign remains not started.

## 9. Exit assessment

Completed:
- Correct branch and authoritative campaign records verified.
- Cairn 2e system binding and isolation boundaries reviewed.
- Both character cards and initial resource ledgers audited.
- Party control and Catherine's independent-PC status confirmed.
- Omen recorded as public information without pre-assigning meaning.
- CAS-1 official source archive and GM-only prep stored in the campaign directory.
- Module source discrepancy documented.
- Player decision on Zaf's Bonds recorded: retain results 7 and 3; no reroll. Original d10 notation remains a historical audit note.

Open items:
1. Cairn remains candidate in the Workbench. This Preflight does not satisfy all system activation gates or certify the system as active.
2. Fasha's HP remains a GM_INFERENCE pending direct verification against the official published PDF.
3. Runtime snapshot and session log will be initialized only when the campaign is explicitly activated/started under the approved protocol.

**Final status:** preparation work is complete to the extent currently supported by the repository. The campaign is `PREFLIGHT_COMPLETED_WITH_OPEN_ITEMS`, `NOT_STARTED`, and `NOT_ACTIVATED`. Do not begin play until the player explicitly says “开始” and the open activation conditions are addressed.


---

## 10. Post-Preflight party update｜2026-11-27

本节记录原 Preflight 审核完成后的正式队伍变更；不回写或伪装成原审核当时已经存在的状态。

- 茱比洛（Jubilo）已正式加入 Twin Lakes（CA01_Zaf），身份为 Cairn 2e 战役内 L3 NPC 队员，由助手控制。她不是测试角色。其人物卡与完整初始状态见 `人物档案/茱比洛_Jubilo.md`。
- 茱比洛采用本战役为该 L3 NPC 配置的 PC 等价资源与机制，并拥有独立目标、判断、资源管理、关系和行动权。该配置不宣称为 Cairn NPC 的通用规则。
- **下次开局的实际队伍仅为 Zaf 与茱比洛。凯瑟琳休止，不随队、不参与该次冒险；她的人物卡、已建立状态和跨战役隔离记录全部保留。**
- 原第 4 节关于 Zaf 与凯瑟琳两名角色的资源审计，保留为原 Preflight 时点的历史记录。茱比洛的初始状态以其人物卡为准。
- 本更新不代表战役已经开始，也不改变 Cairn 的系统激活状态；开局和系统激活仍须遵循原有门槛及用户明确指令。
