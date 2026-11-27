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

### Character creation issue requiring player decision

Zaf's two Bonds were recorded as results 7 and 3 with d10 notation. Cairn 2e uses a d20 Bonds table. Both numbers happen to map to valid entries on the d20 table, but the recorded die type is wrong. The original history must remain intact. No silent correction or reroll was made.

This is the only outstanding player-facing character-creation decision: retain the current Bond entries as a documented creation irregularity, or reroll both Bonds using the correct d20 procedure. Until the player decides, the current entries and items remain provisionally recorded and unchanged.

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

Open items:
1. Player decision on Zaf's two Bonds (retain with a documented irregularity, or reroll both using d20).
2. Cairn remains candidate in the Workbench. This Preflight does not satisfy all system activation gates or certify the system as active.
3. Fasha's HP remains a GM_INFERENCE pending direct verification against the official published PDF.
4. Runtime snapshot and session log will be initialized only when the campaign is explicitly activated/started under the approved protocol.

**Final status:** preparation work is complete to the extent currently supported by the repository. The campaign is `PREFLIGHT_COMPLETED_WITH_OPEN_ITEMS`, `NOT_STARTED`, and `NOT_ACTIVATED`. Do not begin play until the player explicitly says “开始” and the open activation conditions are addressed.
