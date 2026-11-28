# Live Table Voice & NPC Characterization Regression v1｜执行与修订记录

- Date: 2026-11-28
- Status: local same-session regression / synthetic; not independent blind validation
- Canon: TEST_ONLY_NON_CANON
- Fixture: `GM_Training/Testing/Fixtures/LIVE_TABLE_VOICE_AND_NPC_CHARACTERIZATION_REGRESSION_v1.md`

## 1. Incident evidence

Observed in the EBB opening exchange:
- GM output used third-person literary editorial phrasing, including narrator interpretation of character state/relationship posture, rather than consistently presenting the playable moment.
- Jubilo's established personality (energetic, warm, direct, action-oriented, uncomplicated) was summarized in generic measured dialogue. The visible response converged toward a polite, cautious, advisory NPC voice.
- Player relationship distance was correctly established as unfamiliar, but the output treated personality as mostly generic rather than actively rendering it.

This was an execution defect. The information and prep rules existed, but did not reliably shape the generated player-facing response.

## 2. Root cause

1. **Execution-path gap:** the orchestrator said specialist skills should be continuously followed, but did not clearly select a default *live tabletop voice mode* that excludes story-author editorial framing. The narrative skill itself contained many techniques and boundaries, but no compact runtime contract for this distinction.
2. **Soft constraint dilution:** the detailed NPC skill correctly allowed personality signals to be subtle and not every turn to display them. In generation, this restraint collapsed into a generic, safe, measured NPC voice; there was no explicit distinction between “not overacting” and “personality absent.”
3. **Preflight false confidence:** READY and material assembly are not evidence of successful style/personality execution. Prior tests often assessed correctness, information boundaries, continuity, autonomy, and broad narrative dimensions, while live voice-mode selection and audible personality were not consistently treated as focused regression targets.
4. **Checklist overload is not the remedy:** the workbench is large. Adding another turn-by-turn checklist would worsen usability and likely dilute execution. The fix should be short, routed through the orchestrator, and triggered only at generation.

## 3. Repair

Committed to `main`:
- `GM_Training/NARRATIVE_PRESENTATION_SKILL.md`: added §0.1 Live Table Voice contract and §0.2 runtime NPC voice/personality application.
- `GM_Training/SKILL.md`: added §3.2-A Live Table Voice Enforcement, explicitly routing live Session output through these defaults.
- Added this fixture to catch regressions without adding a per-turn audit ritual.

Rules distinguish normal live GM response from explicit story-writing requests. Third-person prose remains available for epilogues, story fragments and requested narrative artifacts.

## 4. Synthetic regression examples

### Case 1 — live scene
**Stimulus:** “我推门进入房间，看看里面的人。”

**Target response shape:** “门内是…… [observable scene and people doing something]. 你能看到……/若要进一步观察…… [action affordance].”

**Result:** PASS conceptually; direct scene presentation is the target, not an authored narrator's interpretation. This case was not run in an independent target chat.

### Case 2 — Jubilo
**Stimulus:** PC establishes names, unfamiliar relationship, and asks to plan routes/enemies.

**Corrected response sample:**
“茱比洛！对，就是这个名字。你是 Zaf，对吧？好，我记住了！……唔，道路最近，不过有士兵的话就麻烦了。森林？我倒是想进去看看！等等，晚上是不是得带火把？你觉得呢？我不想让洛伦兹遇上危险。”

**Assessment:** The sample is more recognizable through initiative, enthusiasm, direct phrasing and immediate practical concern; it does not require a narrator to explain her personality. It remains a single corrected sample, not stability evidence.

### Case 3 — explicit third-person story
**Stimulus:** User asks for a third-person epilogue.

**Expected:** story prose is permitted and the live-table contract is not applied as a prohibition.

**Result:** PASS by design; not executed as an independent generation.

## 5. Evidence boundary

- The observed initial output is direct real-session evidence of the defect in this chat.
- The repairs are committed documentation/orchestrator changes.
- The corrected Jubilo sample is a local illustrative retest, not an independent blind test.
- No claim of platform-level enforcement, stable capability, or independent validation is made.
- The EBB test tabletop remains paused; no game time, route or encounter has advanced.

## 6. Conclusion

Root cause was a **generation-mode routing and constraint-application gap**, not a lack of documented principles. A compact live-output contract is now explicitly wired into the orchestrator and Narrative Presentation skill. The fix is landed on `main`; independent blind and multi-turn validation remain open.
