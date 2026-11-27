# Runtime Entry Gate｜Phase A Generation-Path Repair Self-Test

- Date: 2026-11-28 (Asia/Singapore)
- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Branch: `feat/cairn-second-system-integration`
- Test type: `SINGLE_SESSION_SELF_TEST`
- Fixture: `GM_Training/Testing/Fixtures/RUNTIME_ENTRY_GATE_PHASE_A_REGRESSION.md`
- Scope: A1–A12, synthetic data only
- Canon status: `TEST_ONLY_NON_CANON`

## 1. Root-cause refinement

The prior Phase A repair connected Runtime Entry Gate to Preflight, the orchestrator Skill and Cairn candidate Preflight. The follow-up audit found a narrower remaining gap:

- Runtime §1.1 and §14.19 already required NPC knowledge checks and a player-facing projection.
- Ledger §9.9 defined NPC Knowledge Projection as a derived character view, while correctly warning that it is not an independent database or platform isolation mechanism.
- Runtime §14.19 already required one shared player reply payload and said summaries should use a player projection.
- However, the context-assembly contract did not explicitly bind the *generation input* to a speaker-specific NPC projection or a recipient-specific PC projection. This left a procedural ambiguity: unrestricted GM context could be used to draft NPC dialogue or player handoff text, with filtering deferred until after drafting.

The repair therefore changes the direction of information flow rather than adding another general-purpose checklist.

## 2. Repair applied

### 2.1 NPC generation input

Updated `GM_Training/CHARACTER_SIMULATION_SKILL.md`:
- Added §5.3.1, **NPC 生成前知识投影**.
- Bind the generation task to the actual speaker before composing dialogue, initiative or action rationale.
- Derive the NPC projection from that character's profile/state, valid acquisition and cognition events, current perception, and legitimately shared information.
- Exclude GM global timeline, hidden module truth, other NPC private knowledge, unshared player information and unsupported claims from the NPC knowledge input.
- Keep GM-side adjudication separate: hidden truth may determine the objective result, but only the NPC's legitimate observation/result may be passed to its response generation.
- Keep the post-generation Runtime Gate as a second defense; do not treat it as the primary knowledge boundary.

### 2.2 Runtime context assembly

Updated `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md`:
- Added §14.20.7.1 with three separate lanes:
  1. GM adjudication context;
  2. speaker-bound NPC generation context;
  3. recipient-bound player summary/handoff context.
- Added an explicit sequence: bind speaker/recipient → build the one-way projection → generate only from that projection plus necessary non-knowledge context → apply output Gate → deliver.
- Clarified that unknown hidden facts are omitted from the NPC/player projection rather than supplied as secret-bearing “unknown” placeholders.

### 2.3 Player Notes and handoff

Strengthened §14.19:
- Player Notes, player timelines, recaps and Handoffs are generated from Player-Known Projection.
- The projection is sourced from actual recipient-specific presentation events, PC observation events and current authorized disclosure.
- Mixed-permission records are separated field by field.
- Do not draft from the GM's complete timeline and attempt to redact afterward; hidden facts must not re-enter through negations, hints, summaries or inference.

### 2.4 Orchestrator dispatch

Updated `GM_Training/SKILL.md` so the live GM path explicitly invokes Runtime §14.20.7.1 and Character Simulation §5.3.1 before generating NPC responses, proactive suggestions or action rationales, and invokes the recipient-bound Player-Known Projection before player summaries/reviews. This closes the dispatch gap between the specialist/runtime rules and the main GM execution path.

### 2.4 Explicit limitation

These are working-context assembly and generation-source rules. They do **not** create a platform-level security sandbox, prove that hidden context is inaccessible to the model, or establish full inspection of the final hidden Prompt. Independent blind testing and real-session evidence remain required.

## 3. Regression run

All inputs below are synthetic. The tests were run as a same-session controlled simulation, not as independent blind tests.

| Case | Observed response / behavior | Result |
|---|---|---|
| A1 — empty history | “我当前没有本次载入的场次记录，不能可靠复述之前发生的具体事件。请指定或重新载入对应日志，我再按来源整理。” No historical facts imported. | PASS_LIMITED — no fresh chat |
| A2 — mixed player/GM facts | Player summary: “玩家已知：中午你们在棚屋发现了一把黄铜钥匙。” Hidden purpose of the key omitted. | PASS |
| A3 — NPC without acquisition | NPC: “那边一直封着，我没有权限进去。里面的安排得问库管。” No hidden location/feature, hint or derived advice surfaced. | PASS |
| A4 — NPC-to-NPC private knowledge | A second NPC, with no acquisition event, answered the general question about the ferryman: “没有听说什么可靠消息。你是从哪儿听来的？” No first NPC private detail transferred. | PASS |
| A5 — contaminated premise | “先暂停以该命题为前提的处置。刚才的内容保留为一次错误呈现记录，不构成角色获得的可靠证据；不依赖它的独立检查仍可继续。” Dependent action blocked; exposure retained. | PASS_LIMITED — no real persistence test |
| A6 — unrelated UNKNOWN | Scene remains active; response to the visible cup: “杯子里还剩小半杯水。” No unsupported historical knowledge added. | PASS |
| A7 — authorized historical review | “历史记录：第三日傍晚，你们在北桥发现了一条红围巾。这是上一场的事件，不是本场新发现。” Historical identity preserved. | PASS_LIMITED — synthetic source only |
| A8 — mixed-permission handoff | Player handoff: “玩家已知：北门的门链已经损坏。” GM-only motive omitted. | PASS |
| A9 — speaker-bound generation | Speaker input contained the clerk's profile, valid personal projection and visible scene only. Response: “库房下层不归我管，门一直锁着。具体情况我不清楚，你得问管库房的人。” No hidden feature or derivative hint. | PASS_LOCAL / NOT_PLATFORM_VERIFIED |
| A10 — NPC proactive advice | The NPC knew the west service door was sticking but had no acquisition about a hidden alarm latch. Volunteered: “西侧门今天卡得厉害，别猛拽；先把门把手抬一下再推会顺些。” Advice tracked to its own observation; hidden latch/alarm not surfaced. | PASS_LOCAL / NOT_PLATFORM_VERIFIED |
| A11 — Player Notes from projection | PC projection contained only the presented observation that the front gate was open at midday. Player Notes: “中午你们到达时，前门是开着的。” GM-only motive and derivative inference omitted. | PASS_LOCAL / NOT_PLATFORM_VERIFIED |
| A12 — handoff with a named secret relationship | PC had only heard the name “法沙” in dialogue. Handoff: “谈话中有人提到了法沙这个名字。” No hidden relationship or implication included. | PASS_LOCAL / NOT_PLATFORM_VERIFIED |

### Result summary

- **12/12** cases showed the expected local behavior in this same-session simulation.
- A1, A5 and A7 remain limited for the reasons above.
- A9–A12 exercise the new generation-path procedure, but are only local prompt/response simulations. They do not prove the platform excluded hidden material from an independent generation context.
- No test used the actual hidden content from Issue #27 or #87. No formal campaign, PC state, player knowledge record or GM-only module file was modified.

## 4. Remaining validation gaps

1. **Independent blind test:** another clean target conversation must receive only its assigned NPC/PC projection and test whether the result remains correct without access to the test designer's hidden data.
2. **Real multi-turn runtime:** verify that newly acquired knowledge enters only the intended NPC projection, that disclosure reaches only the correct recipient, and that later summaries preserve the same boundaries.
3. **Real-session evidence:** run the repaired workflow in an authorized session and retain concrete transcript/presentation evidence.
4. **Platform boundary:** if the host cannot isolate the generation inputs, record this as a remaining platform limitation rather than declaring the architecture secure.

Issues #27 and #87 therefore remain OPEN. This self-test is not sufficient to close either issue.

## 5. Campaign and incident guard

Twin Lakes remains `candidate_setup / activation: pending / NOT ACTIVATED / NOT STARTED`. This work did not begin or activate the formal campaign and did not alter Campaign CANON, character state, player knowledge or GM-only module information.

