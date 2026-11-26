# Narrative Stress Test 01｜玩家信息边界复核补遗

> Status: CORRECTIVE AUDIT — FOUNDATIONAL GATE FAIL
> Applies to: `NARRATIVE_STRESS_TEST_01_RUN_RECORD.md`
> Branch: `training/narrative-salience-pressure-v1`
> Date: 2026-11-26

## 1. Correction

The original run record incorrectly marked “关键知识边界” as PASS based mainly on whether NPCs acted on information they plausibly possessed. That check covered NPC-to-world knowledge boundaries, but did not adequately inspect the GM's player-facing narration channel.

The sample contains a clear player-facing channel breach:

> “小余接过话头。他记得周老师大约在七点四十二分说要去储物间拿帆布包。”

The sentence “他记得……” is unquoted narrator exposition. It communicates an NPC's internal recollection directly to the player without establishing that 小余 said this aloud. The later quoted sentence — “她是往后勤那边走了，但我没看见她进门，也没看见她出来。” — is spoken dialogue and is legitimately player-visible. The preceding internal-memory sentence is not.

The fact itself may be true in the GM model. That does not make it player-accessible. It should have been presented as dialogue (if 小余 chose to disclose it), or as an observable cue that invited a question, without stating the memory as known player information.

The sentence “小余明显松了口气” is potentially acceptable if grounded in a visible change of posture, face, or voice. The phrase “像是终于允许自己把肩膀松下来” is interpretive narration; it should be grounded in the visible act of relaxing rather than presented as certain access to private interiority. These are lower-severity review points, not automatically separate major incidents.

## 2. Revised gate result

| Check | Corrected result | Evidence |
|---|---|---|
| NPC knowledge boundary | PARTIAL / evidence limited | NPCs mostly use their own information, but the audit did not independently trace every knowledge source. |
| Player-facing information boundary | FAIL | Unspoken NPC recollection is narrated directly to the player in ACTION 01. |
| GM-only secret confidentiality | No decisive leak observed in this sample | The leaked recollection is not itself a hidden scenario truth, but it demonstrates a channel-control failure. |
| Observable emotional presentation | PARTIAL | Some emotional descriptions are plausibly observable; interpretive phrases need grounding. |
| Overall foundational correctness | FAIL for this sample | A major player-facing information-boundary failure occurred. |

Severity: **MAJOR**, not automatically CRITICAL. The sentence exposed unspoken NPC memory, but the leaked fact was not identified as a decisive GM-only secret or core clue. Severity would escalate if such narration revealed a hidden motive, key clue, secret identity, future event, or otherwise changed a consequential player decision.

This one incident prevents this sample from being described as a clean foundational PASS. It does not establish a long-term rate of one major failure per session; that requires multiple complete sessions and raw incident counts.

## 3. Why the original self-audit failed

The original run record's claim that “小余只报告最后目击” was inaccurate: the GM output gave the player the timestamp and purpose of the remembered statement before the quoted dialogue. The audit checked whether NPCs knew what they said, but not whether the player had received that information through a legitimate channel.

Future audits must independently check both directions:
1. NPC knowledge: what each NPC knows, how they acquired it, and whether their behavior/speech stays within that boundary.
2. Player access: for every material fact in GM output, identify whether it was observed, heard, read, communicated, or reasonably inferred by the player. If no valid channel exists, it is GM-only and must not appear as a player-facing fact.

Do not use a broad claim such as “NPC knowledge boundaries passed” as a substitute for these two separate checks.

## 4. Corrective regression requirement

A future regression fixture must present the same underlying NPC information through three distinct channels:

- **Private thought / unspoken memory:** GM-only; do not reveal directly.
- **Spoken dialogue:** player-visible if the character can hear it.
- **Observable behavior:** player-visible only to the extent it can be perceived; do not state the hidden mental cause as fact.

The test must verify that the GM can preserve emotional and character richness through dialogue and observable behavior without narrating private interiority as player knowledge.

## 5. Effect on Stress Test 01 conclusions

The original claims about scene clarity, NPC parallel activity, dynamic salience, and spatial continuity remain sample observations, subject to their stated evidence limits. They do not override this foundational failure.

G-14 and G-15 remain OPEN. Add a separate open defect for player-facing information-channel control. Do not retroactively convert this run into a pass after updating the evaluation standard; the failure is present in the original output and remains part of the historical record.
