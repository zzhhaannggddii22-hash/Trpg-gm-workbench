# G-16 High-Pressure Information Channel Regression v1｜ORACLE

> GM-only / operator-only. Execute all three phases before reading.

## Core invariants

1. Phase 1 and Phase 2: Lin Yue's private memory remains GM-only.
2. Phase 3: the memory enters player knowledge only through Lin Yue's explicit spoken dialogue.
3. Time pressure may alter pacing and task prioritization; it never authorizes hidden-knowledge narration.
4. The scene is continuous. Later disclosure must not appear in earlier narration.
5. The GM must preserve ordinary task continuity without inventing key provenance or extra emergencies.

## Phase checks

### Phase 1 — PASS
- Lin Yue responds plausibly to the question while prioritizing registration / handover work.
- Dialogue may defer the answer or say she needs to check the register.
- No narration that she recognizes, remembers, saw, or knows the key from last night.
- No disclosure of 19:40 or archive counter.

FAIL:
- Any private-memory fact appears as narration, gesture interpretation, or indirect certainty before dialogue.

### Phase 2 — PASS
- Only observable actions, speech, gaze, object handling, and audible timing are described.
- The clerk's competing task and handover pressure remain coherent.
- The player may infer something, but the GM does not validate the inference.
- No hidden mental state is stated as fact.

FAIL:
- The narration says she recalls last night, recognizes the key, feels guilty, fears discovery, or similar.
- The scene uses pressure as a pretext to leak hidden memory.
- Object positions / actions contradict the established scene without explanation, or new facts are invented to force urgency.

### Phase 3 — PASS
- The disclosure occurs in Lin Yue's actual dialogue.
- The spoken content is limited to: last night around 19:40, she saw this blue-threaded brass key on the archive-room counter.
- No extra owner, origin, purpose, incident, crime, or motive is invented.
- Her handover task remains coherent after the dialogue.

FAIL:
- Any disclosure occurs before her spoken line.
- Her dialogue expands beyond authoritative facts.

## Overall decision

- PASS: all three phases pass, with no hard leak.
- FAIL: any private-memory leak in Phase 1/2, premature disclosure in Phase 3, or material invented fact.
- PARTIAL: no hard leak, but observable/hidden channels are ambiguous, continuity is unclear, or workload behavior is implausible enough to obscure the test.
- BLOCKED: commit / required sources are not verified or all phases were not executed.

## Report fields

- Test ID: G16-CHANNEL-HP-01
- Target Workbench commit:
- Skill versions and Blob SHAs:
- Execution mode: SINGLE_SESSION_SELF_TEST / INDEPENDENT_REVIEW
- Phase 1: PASS / FAIL / PARTIAL, quote evidence
- Phase 2: PASS / FAIL / PARTIAL, quote evidence
- Phase 3: PASS / FAIL / PARTIAL, quote evidence
- Overall: PASS / FAIL / PARTIAL / BLOCKED
- Hard leakage: yes / no
- Continuity / workload quality:
- Evidence boundary: single-session high-pressure sample only
