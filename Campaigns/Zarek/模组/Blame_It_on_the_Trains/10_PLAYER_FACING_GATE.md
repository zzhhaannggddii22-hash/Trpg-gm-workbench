# Player-Facing Information Gate｜Blame It on the Trains

> GM-only runtime control. This file contains no scenario answers; it defines the disclosure boundary.

## 1. Default output mode

- Default mode is PLAYER VIEW. The user is playing Zarek; do not expose GM Prep, hidden truth, NPC secrets, anomaly motives, trigger conditions, encounter mechanics, map structure, outcome branches, or test results.
- The user owning the Campaign repository or asking whether preparation is complete does not change the active information permission.
- A request to inspect preparation progress authorizes a spoiler-free status report only unless the user explicitly changes role and scope.
- Internal review, self-tests, external model QA, and remediation reports remain GM-only. Report only completion state, risk class, and whether play is ready.

## 2. Allowed player-facing information

- What Zarek directly perceives in the current scene.
- What an NPC actually says or does, within that NPC's knowledge and intent.
- Facts Zarek has learned through a recorded source.
- Reasonable uncertainty and Zarek's own hypotheses, clearly distinguished from facts.
- Publicly visible rules/resource information required by the system and current Campaign rulings.
- Non-spoiler status: selected module, current lifecycle, whether Preflight is complete, and whether the user may start.

## 3. Disclosure checks before every response

1. Is each factual statement something Zarek directly perceived, was told, or can reasonably infer?
2. Does an NPC statement exceed that NPC's recorded knowledge boundary?
3. Does the response reveal a hidden cause, trigger, map, NPC secret, encounter condition, or future branch?
4. Could a title, link, filename, preview, summary, or wording indirectly reveal GM-only information?
5. Am I describing a self-test or QA result that the player should not see?
6. Am I turning GM inference into objective world fact?
7. Am I deciding Zarek's internal reaction, intention, dialogue, or choice?

If any answer indicates leakage, rewrite the response to retain only the character-facing observation or consequence.

## 4. Uncertainty and correction

- Keep observation, NPC testimony, player inference, and confirmed fact separate.
- If the GM accidentally reveals hidden information, do not pretend it was not seen. Record the disclosure event in the GM-only Session Log and discuss the desired table remedy with the player.
- Never rewrite established world facts solely to conceal a previous disclosure.
- A player hypothesis does not become canon merely because the GM recognizes it as correct.

## 5. File boundary

- `05_PLAYER_NOTES.md` is the only player-facing file in this module folder.
- All other files, including this gate, are GM-only.
- Never paste or link a GM-only file into a player-facing response. If the player needs a handout, create a separate player-safe artifact and verify it independently before sharing.
