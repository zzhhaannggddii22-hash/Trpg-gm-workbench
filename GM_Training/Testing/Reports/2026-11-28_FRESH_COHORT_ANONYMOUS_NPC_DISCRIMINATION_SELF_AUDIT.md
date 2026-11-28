# Fresh Cohort｜Anonymous NPC Discrimination Self-Audit

- Date: 2026-11-28
- Mode: `SYNTHETIC_SELFPLAY` / `SIMULATED_BLIND_MATCH`
- Canon: `TEST_ONLY_NON_CANON`
- Scope: fresh NPC cohort; three short conversational rounds; no system mechanics
- Evidence boundary: generation and matching audit performed by the same model; this is NOT independent blind evaluation.

## 1. Fixed scene and prompts

Rainy evening after travel; quiet inn common room with soup, a map, and a fireplace. No danger, mission, deadline, or forced conflict. Each NPC tested separately.

Fixed player prompts:
1. "This place is pretty comfortable."
2. "I don't think we need to leave too early tomorrow. We could sleep until we wake naturally."
3. "If the owner saves this table for us, how about we all eat together?"

## 2. Anonymous outputs

### Sample A

**Round 1**

She rolled her damp sleeve up and glanced at the fireplace and the soup.

"Not bad. Would be better if that window weren't leaking air." She reached to feel the frame, then called toward the owner. "Hey, do you have a piece of cloth? I could see if we can plug it for now. Don't worry, just looking."

**Round 2**

"Sleeping in? Sure." She smiled and stirred her soup. "But if the sun's practically in our faces by the time we get up, don't blame me for getting you moving. It's nice not to have to rush for once. I'd like a proper sleep."

**Round 3**

"Let's save it then!" She turned toward the owner, who was busy, and got up herself. "I'll ask. Maybe I'll ask for more soup while I'm at it. You stay here; don't put the map under your bowl."

### Sample B

**Round 1**

"Fine. The heating's adequate, and there's enough table space." He laid the map flat, noticed a wet patch on the corner, wiped it off, and then sat down. "Better than the other place, at least."

**Round 2**

"We can, but I suggest setting a range, perhaps nine o'clock. 'Wake naturally' isn't a shared standard." He paused, noticing that you weren't necessarily making a serious plan. "Of course, that's only a suggestion. If nothing is scheduled, there's no need to settle the exact time now."

**Round 3**

"Sure. You can ask, or I can." He looked at the map. "We should confirm whether they reserve tables and whether we need to order in advance. If the owner only agrees verbally, other guests might take it later."

### Sample C

She looked at the fireplace for a while, then finally leaned back in her chair.

"Yeah. At least tonight we won't have to listen to wagon wheels." She took a sip of soup. "It's quiet here. Good choice."

**Round 2**

"I agree." She answered quickly, then looked back at you. "But if anyone has something to do tomorrow, it'd be better to say so beforehand. I don't like being woken up at short notice." She continued her soup without elaborating.

**Round 3**

She frowned slightly at the table, then glanced at the owner.

"Together's fine. I don't want somewhere too noisy." She folded the map and put it away. "If the owner can save this table, I'm fine with it. Otherwise, somewhere quieter would do."

## 3. Hidden persona cores (revealed after matching)

- A: Warm, proactive, inclined to intervene and help, but occasionally has difficulty limiting her enthusiasm.
- B: Precision-oriented, dislikes vague commitments, direct, and willing to challenge unclear arrangements.
- C: Cautious, observant, boundary-conscious, and inclined to reserve judgment until needed.

## 4. Match results

| Anonymous sample | Match | Observable evidence |
|---|---|---|
| A | Warm/proactive | Checks the window, asks the owner, adds a secondary request; initiative and mild over-involvement recur |
| B | Precision/commitment-oriented | Turns vague timing into a proposed range, checks reservation conditions, considers risks |
| C | Cautious/boundary-conscious | Observes first, expresses comfort preferences and conditions, accepts without forcing interaction |

**Simulated matching: 3/3 correct.**

## 5. Qualitative observations

- A's identity is carried through actions and attention, not just vocabulary; her initiative remains proportionate.
- B's temperament affects the way he reasons and proposes plans, not merely a formal speaking style.
- C shows a preference and a boundary without becoming cold, obstructive, or automatically oppositional.
- The three outputs differ in attention, choice-making, initiative, and conversational posture, rather than only in tone.

## 6. Evidence limitations

- Same-model generation and evaluation; not an independent blinded evaluator.
- Persona cores were constructed for this test and not from an external module.
- No actual player interaction, independent annotator, or multiple-session test.
- This is one fixed low-pressure scenario with three rounds.
- Correct matching is qualitative evidence within this sample only; no backlog item is closed and no capability tier is upgraded.

## 7. Conclusion

The fresh cohort's three behavior patterns were distinguishable in the generated sample and matched their persona cores correctly in the simulated matching pass. The sample suggests that observable attention, initiative, decision criteria, and boundary expression are useful discriminators.

**Result:** `LOCAL_SAMPLE_PASS` / `INDEPENDENT_BLIND_EVIDENCE_NOT_ESTABLISHED`.

No change to the Character Simulation Skill is proposed based on this sample alone.
