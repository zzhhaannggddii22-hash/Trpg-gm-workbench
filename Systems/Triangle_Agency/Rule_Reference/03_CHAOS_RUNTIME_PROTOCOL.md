# Triangle Agency｜Chaos Runtime Protocol

> system_id: `triangle_agency`
> ruleset_version: 用户指定的《三角机构》中文 v22
> Status: DRAFT / PENDING BEHAVIORAL VALIDATION
> Scope: 系统规则层。定义 Chaos Pool 如何从规则事件进入运行、如何被转化为世界效果，以及任务边界如何结算。
> Does not replace: Dice Resolution, Campaign Resource Ledger, Module Closeout, Loose Ends & Weather Events, anomaly-specific rules, or the authoritative v22 text.

## 1. Design intent

Chaos is not merely a balance to display or preserve. In v22 it is anomalous energy that can empower hostile Anomalies and be used to create Chaos Effects. Its runtime therefore has two inseparable responsibilities:

1. **Accounting:** maintain the correct public Chaos Pool and apply only authorized generation/spending.
2. **World operation:** recognize valid opportunities for system actors or forces to use Chaos, select a fitting effect, and materialize its consequences in the fiction and state.

A correct balance with no meaningful Chaos Effects is an incomplete runtime. Equally, dramatic complications without a valid rule trigger, effect, or established cause are not valid Chaos use.

## 2. Authority and source map

Use the active Campaign Binding for system/version and applicable table rulings. For Chinese v22, the relevant source locations are:

- Field Agent Manual, `Chaos`: PDF physical page 37 / printed page 33 — roll-based generation.
- Field Agent Manual, `Threats in the Field`: PDF physical page 30 / printed page 26 — Chaos Pool, Minor Anomalies, and unused Chaos disappearing at the end of each mission.
- General Manager Toolkit, `Chaos & Chaos Effects`: PDF physical page 160 / printed page 156 — Chaos as anomalous energy, Focus, nearby action, public pool, GM influence, no-target-Anomaly missions, human-caused effects, and Domain Benefits.
- General Manager Toolkit, `Chaos Effects Chart`: PDF physical page 162 / printed page 158 — standard effects and costs.
- General Manager Toolkit, `Minor Anomaly Chart`: PDF physical page 163 / printed page 159 — Disruptive Minor Anomaly generation modifier.
- General Manager Toolkit, `High Pressure Situations`: PDF physical page 164 / printed page 160 — high-pressure pacing guidance.
- General Manager Toolkit, `Personalized Chaos Effects`: PDF physical page 165 / printed page 161 — mission preparation, Special Rules, and New Chaos Effects.
- General Manager Toolkit, `Loose Ends & Weather Events`: PDF physical pages 168–173 / printed pages 164–169 — branch Loose Ends, starting environmental Chaos, Weather Events, and escalating consequences.

The upstream Chinese v22 Markdown is the normal complete-text source. PDF pages are only required for the documented visual/layout or extraction ambiguities.

## 3. Runtime state and lifecycle

The system adapter must expose or resolve these values from the existing Campaign / Module Resource Ledger and event history; do not create a parallel ledger:

- `chaos_pool_current`: current public balance for this active mission.
- `chaos_pool_last_verified`: last fully verified balance and its event/time anchor.
- `chaos_pool_pending_dependencies`: any unresolved event that could change the current balance.
- `chaos_pool_events`: references to the stable events that generated, spent, or otherwise changed Chaos.
- `active_anomaly`: the current target Anomaly, if any, and its established Focus / Impulse / Domain / goals.
- `active_domain`: whether the current action is within that Anomaly's Domain.
- `mission_status`: active / closed, with the authoritative mission boundary.

These are semantic fields, not a mandate to duplicate existing storage. Bind them to the actual project schema. If a field does not exist, identify the correct existing field or record a schema gap; do not silently add a second source of truth.

### Lifecycle

1. **Previous mission close:** close the old mission's Pool by recording its remaining balance as discarded when known and setting that mission's final Pool to 0.
2. **New mission creation:** instantiate a distinct Pool for the new mission at 0; never reuse the previous mission's Pool.
3. **Mission setup:** read the current Campaign-owned Branch Loose Ends total, resolve the v22 table row, and apply its Starting Chaos to the new Pool as a separate grant. Resolve Weather Event count and cumulative restrictions as separate outputs.
4. **During mission:** accept Chaos generation from the already integrated roll-resolution event and other explicit system rules. Keep the public balance current. Evaluate Chaos Effects only when a valid world-action opportunity occurs; do not poll or spend on every player message.
5. **Effect resolution:** verify eligibility, cost, Domain treatment, selected effect, target, timing, and resulting state. Apply the resource transition and world consequence under one stable event.
6. **Recovery / retry:** reuse the same stable event and its completed fields. Never re-roll, re-spend, re-apply a world effect, or reinitialize the Pool because a response or Session was retried.

## 4. Generation: input contract, not a second dice engine

The roll-resolution module owns the base Chaos generated by the resolved roll. This protocol owns the Triangle Agency-specific generation modifiers and final Chaos delta. Neither module may apply the same modifier twice.

- Each die that does not show `3` adds `1` Chaos, subject to the system's explicit exceptions and the final resolved roll rules.
- A standard 6d4 roll can generate up to 6 Chaos before other modifiers.
- Stable Success / Triscendence exceptions and Burnout handling belong to the Dice Resolution adapter; use its final verified Chaos delta.
- Other explicit system effects can add Chaos independently. Examples in v22 include a personalized Special Rule that adds Chaos when a stated trigger occurs and each nearby Disruptive Minor Anomaly adding `+1` whenever Chaos is generated.
- Do not add Chaos merely because an event is dramatic, dangerous, or supernatural unless a rule or approved adaptation authorizes it.

**Generation handoff contract:** the roll adapter submits `event_id`, `source_event_id`, `base_delta`, rule basis, and resolved roll result. The Chaos Runtime applies eligible system-specific modifiers (including each eligible nearby Disruptive Minor Anomaly) exactly once, then produces `applied_modifiers[]` and `final_delta`. The ledger accepts only `final_delta`, never an ambiguous `chaos_delta`. Preserve an eligibility snapshot and commit status. Independent Special Rule generation enters the same normalizer with its own source event. Modifiers attach to the triggering generation event and do not recursively trigger themselves. Replays reuse the original source-event identity and modifier snapshot; a genuinely new trigger remains a new event.

## 5. Starting Chaos and Branch pressure

The v22 source (General Manager Toolkit, printed page 165 / PDF physical page 169) requires the GM to check the **current Branch Loose Ends total before every mission**. The table determines three distinct outputs: starting environmental Chaos, Weather Event count, and cumulative Branch restrictions. This is a mission-setup procedure, not a permanent Campaign starting-pool override.

### Mission-start procedure

1. Read the current authoritative Branch Loose Ends total from the Campaign state / Branch ledger.
2. Find the applicable threshold row in the printed-page-165 table. A listed threshold applies from that value up to (but not including) the next listed threshold. Do not interpolate or calculate a smooth formula.
3. Read the row's Starting Chaos, Weather Event count, and cumulative Branch restrictions.
4. Keep the Branch Loose Ends total and Weather Event history as separate persistent state.
5. Create the new mission Pool at 0, then apply the row's Starting Chaos as the mission-start grant. Record these as distinct transitions: NEW_MISSION_POOL_CREATED (0), followed by BRANCH_STARTING_CHAOS_GRANTED (+N). Never reuse the closed mission's Pool.
6. Record the row's Weather Event count as a separate mission-setup output. The v22 source procedure normally calls for rolling a d20 for each Weather Event indicated by the current row during mission preparation; repeated results advance from initial (Xa) to enhanced (Xb) to extreme (Xc), and results divisible by 3 cause the Agency to remove Loose Ends immediately, which may change how many remaining dice must be rolled.
7. **Campaign-scoped override:** an active Campaign Binding may explicitly narrow when the Weather Events procedure is invoked. Such a trigger is a Campaign ruling, not a claim that the printed v22 procedure itself is optional. If no explicit override is present, follow the v22 mission-preparation procedure as written.
8. When the active Campaign's trigger condition is met, follow the exact v22 Weather Events procedure and use the current table output/history. Do not invent extra events or reroll already-resolved events. If a resolved Weather Event explicitly changes Branch Loose Ends, update Campaign state as its own event and recalculate only the remaining Weather Event count at the timing specified by v22; do not blindly continue the original count. This affects only the remaining Weather Event procedure: it does not rerun mission initialization or change the already-committed Starting Chaos grant. If the result does not explicitly change Loose Ends, do not alter it.
9. Record the source total, selected row, Weather Event count, whether the active Campaign's trigger condition occurred, and any actual event/result in the existing Campaign / Module Resource Ledger or Campaign state record. A table count alone is not evidence that weather events occurred.
10. If the Branch total or applicable row cannot be verified, mark only the dependent setup outputs PENDING; do not substitute 0.

### Printed-page-165 table

| Current Branch Loose Ends | Starting Chaos | Weather Event count | Cumulative Branch restriction |
|---:|---:|---:|---|
| 0–10 | 0 | 0 | Only restrictions in the Agency employment contract |
| 11–21 | 5 | 1 | Relationships spontaneously remind Agents of Agency duties and the importance of reducing Loose Ends during otherwise normal conversation |
| 22–32 | 10 | 2 | To receive Triscendence effects, Agents must give a short speech affirming their commitment to eliminating Loose Ends and stabilizing Reality |
| 33–43 | 15 | 3 | Agents must count to 3 (aloud or equivalently) before every roll |
| 44–54 | 20 | 4 | Agents are ineligible for Mission MVP awards until Branch Loose Ends fall below 44 |
| 55–65 | 25 | 5 | Read the book's stated warning about contract termination at 66 and the overtime option to remove 6 Loose Ends alone |
| 66–76 | N/A | N/A | At the end of the current mission, the active field team is forcibly retired; apply the book's retirement and Loose Ends reduction rules |
| 77+ | N/A | N/A | The Unraveling is imminent; the Branch region is removed from existence as directed by the book |

The source table prints thresholds at 0, 11, 22, 33, 44, 55, 66, and 77. The interval notation above operationalizes those thresholds without interpolation: a total of 1 uses the 0 row; 10 also uses the 0 row; 11 enters the 11 row. The special 66 and 77 outcomes take precedence over ordinary Chaos initialization.

### Special threshold lifecycle handoff

- The `66–76` row is not a numeric Chaos initialization. At mission setup, or when a verified in-mission Loose Ends change first crosses 66, create a stable `RETIREMENT_PENDING_AT_MISSION_CLOSE` transition for the active field team. Continue the current mission; do not terminate it immediately. At closeout, apply the v22 consequences through the existing Campaign / Closeout process: reduce Branch Loose Ends by 11, plus a further 11 for each Agent who uses a function-provided retirement option. Resolve each Agent's available option from the character/Playwall authority; do not assume an option exists.
- The `77+` row is not a numeric Chaos initialization. It enters the book-directed Unraveling / Branch-removal procedure (the source directs to W7); the Branch region is removed from existence as directed by the book. Do not create a normal mission Pool or convert `N/A` to zero.
- After any verified Branch Loose Ends mutation during a mission, re-evaluate whether a special threshold has been crossed and record a transition request with its source event. The system adapter emits the required state transition; the Campaign lifecycle owns the resulting Campaign state. Do not silently execute a second reset or mutate historical events.
- If a threshold is crossed and then the total changes again before closeout, preserve both source events and the pending transition. Where the rule text does not explicitly define cancellation or reversal timing, mark that specific transition PENDING for source-based adjudication rather than automatically cancelling or inventing a reversal.
- Special threshold transitions must be idempotent by source event and mission ID. Recovery resumes incomplete lifecycle fields and must not retire the team twice or repeat Branch removal.

### Campaign data boundary

This system protocol contains no current Branch Loose Ends value. The current total is dynamic Campaign state and must be read from the active Campaign's authoritative state record at each mission boundary. A prior mission snapshot is evidence of the value at that time, not a permanent rule default. Never copy a Campaign's current total into this system-wide rules file.

An escaped Anomaly adds 7 Loose Ends to the Campaign-owned Branch total; this is not itself a direct +7 Chaos event. Loose Ends / Weather Events remain separate persistent state. This protocol consumes the verified mission-start table outputs and must not duplicate their roll, escalation, removal, or retirement procedures.

## 6. When Chaos becomes an active world mechanism

The GM should evaluate Chaos Effects when the fiction presents a valid opportunity, not at arbitrary intervals.

### Valid opportunity signals

Consider the Chaos runtime when one or more of these are true:

- An active Anomaly is trying to act beyond its Focus and must draw on ambient Chaos.
- An active Anomaly is attempting a supernatural action in the direct vicinity of Agents; v22 says it cannot do so without spending Chaos.
- Agents have interfered with, resisted, exposed, or disrupted an Anomaly's established goal, Focus, or current plan, creating a credible opportunity for the Anomaly to respond.
- A prepared Anomaly goal, impulse, special rule, or established behavior gives it a concrete reason to use Chaos now.
- A mission has no target Anomaly, but the roll-generated Chaos or another established force can plausibly manifest as an unforeseen consequence or as an effect wielded by an interested force.
- A system-defined effect or special rule explicitly triggers a Chaos change or Chaos Effect.

These are evaluation triggers, not automatic permission to spend. Confirm the acting force, motive/behavior, target, and rule basis before resolving.

### Actor and motive

With an active Anomaly, choose effects that express its established Focus, Impulse, goals, and behavior. The rulebook explicitly permits the GM to use the Agency's influence to nudge Anomalies toward spending Chaos. That means the GM should actively look for a fitting use when an opportunity exists, rather than waiting passively for the Anomaly to act on its own.

This is not a license to punish the player or to spend simply because the pool is large. Chaos should help the Anomaly act, resist interference, express its nature, or create a meaningful obstacle/consequence consistent with its established agenda.

Without a target Anomaly, identify the established source of the effect: the Agents' own anomalous power having unforeseen consequences, another force watching or manipulating the team, or another explicit system cause. Do not invent a hidden manipulator as fact merely to justify spending; mark it as GM preparation/inference until established.

Human behavior may also create events resembling Chaos Effects without spending Chaos. Such an event must be grounded in human motives, choices, or established circumstances; do not charge the pool for it unless a rule says so.

## 7. Spending and effect selection

Before a positive-cost spend, verify:

1. The mission is active and the pool balance is verified.
2. The acting Anomaly / force is eligible and has a supported reason to act.
3. The effect is in the standard Chaos Effects chart, a prepared New Chaos Effect, or a Special Rule with its own exact trigger.
4. The target and scope are supported by the effect text and current facts.
5. The correct Domain cost treatment is applied.
6. The resource transition and world effect can be resolved and recorded together.

A verified free Domain effect, a human-caused event that spends no Chaos, or a passive rule independent of the current balance must not be blocked merely because the absolute Pool is UNKNOWN. A known generation delta may be recorded against an unknown starting balance, but the absolute balance remains UNKNOWN until reconciled. UNKNOWN blocks only operations whose legality or cost actually depends on knowing the current balance.

### Standard Chaos Effects

| Cost | Effect | Operational meaning |
|---:|---|---|
| 1 | Distort | Mundane change to an object or location. |
| 2 | Corrupt | An object/location becomes Anomaly-reflective, unnatural, or dangerous. |
| 3 | Reality Trigger | Activate a character's Reality feature. |
| 4 | Manifest | Create one Minor Anomaly using the chart. |
| 5 | Attract | Draw a small number of mundane entities (e.g. Relationships) into the Domain. |
| 6 | Expand | Expand the Anomaly's Domain to another location; scale follows its Focus. |
| 7 | Double | Create two Minor Anomalies. |
| 8 | Displace | Move a group into an Anomaly-created surreal space; no physical harm can occur there, but the Anomaly controls their experience briefly. |
| 9 | Triple | Create three Minor Anomalies. |
| 10 | Kill | End a mundane person's life; ignores defenses and cannot be prevented, changed, or interrupted by another effect. |
| 30 | Overwhelm | End an Anomaly's life; ignores defenses and cannot be prevented, changed, or interrupted by another Anomaly effect. |

Whenever a Chaos Effect is used, read its complete description to the players, as directed by the source text. Keep the effect's identity unknown until it is actually used; players may recognize patterns through observation.

### Domain Benefits

The v22 Domain Benefits paragraph on printed page 156 states that Chaos Effects costing `3` or less can manifest for free inside the Anomaly's Domain, while any Chaos that is spent has its actual cost multiplied by three.

**Runtime handling:** the source explicitly makes effects costing `3` or less free inside the Domain. Whether that free benefit is repeatable is a Campaign-scoped adjudication, not a universal system default. For Zarek, Campaign Binding Q01 approves repeatable use of effects costing `3` or less; apply that ruling only when the active Campaign Binding selects it. Other Triangle Agency Campaigns must use their own approved ruling or preserve the source ambiguity. Effects costing more than `3` consume three times their listed cost. Do not multiply free effects by three.

Outside the Domain, use the listed effect cost.
### Custom effects and Special Rules

- **Special Rule:** a specific, consistent rule tied closely to an Anomaly's Focus/function may occur without spending Chaos. It must have an exact trigger and stable behavior. Examples include a rule that adds Chaos when someone screams. This is not a free-form GM complication.
- **New Chaos Effect:** a flexible action related to the Anomaly's powers but not a strict standing rule. Define its effect and cost; greater disruption to Reality's narrative should cost more. The source gives examples at 2 / 4 / 6 / 8 Chaos. Effects costing 3 or less are free within the Domain; repeatability follows the active Campaign's approved ruling (Zarek Q01 permits repeat use).
- Do not confuse a Special Rule's independent trigger with a Chaos Effect purchase. A Special Rule may add Chaos, cause an effect, or do both only if its own text says so.

## 8. Materialize the world effect

A spend is not complete when the number is deducted. It is complete when the effect has a clear, rule-supported fictional result and the relevant state is updated.

For each effect, resolve:

- **What changed?** Object/location, person, target group, Domain boundary, Minor Anomaly, life state, access, sensory experience, or another exact target.
- **When did it happen?** Immediately, at a specified later time, or under a trigger in the effect text.
- **What remains true?** Duration, persistence, reversibility, and any explicit immunity / prevention clauses.
- **What can the Agents perceive?** Describe the effect in the fiction and read its full description as required. Do not expose GM-only motive or hidden preparation unless the effect makes it observable.
- **What state must change?** Update only supported fields: location, access, object state, NPC/target status, Domain, Minor Anomaly roster, harm/life state, or other relevant system/campaign fields.

If an effect changes the environment, make the change operational. A locked door changes access; an expanded Domain changes where Domain rules apply; a Manifest effect adds a Minor Anomaly with its own supported behavior; a Displace effect changes the group's immediate experiential environment. Do not leave the effect as flavor text if it is supposed to constrain or alter subsequent play.

Do not invent secondary effects. Consequences may follow from established physics, motives, and rules, but distinguish direct effect from downstream inference.

## 9. High-pressure pacing and player agency

The High Pressure Situations chapter encourages the GM to maintain meaningful player choices while threats are active and to use moments of imminent danger to create opportunities for rolls. This is guidance, not a quota.

- Do not manufacture attacks or force repeated rolls just to farm Chaos.
- Do not require every encounter to contain a Chaos Effect.
- When a threat is active, make its next action and the players' opportunity to respond legible.
- Use Chaos Effects to alter the situation in ways that create meaningful decisions, express the Anomaly, or change the cost/shape of interference.
- Effects can be telegraphed when appropriate. The source specifically suggests revealing the possibility before activation in a Domain, using high pool totals such as 30 as leverage. This is optional guidance, not an automatic threshold trigger.
- Never use Chaos to override a player's already-established action outcome retroactively unless a rule explicitly permits it.

## 10. Event and ledger requirements

Use the existing stable event / Resource Ledger machinery. Do not create a separate Chaos ledger.

For each generation or spend event, record the minimum required fields:

- event_id and mission_id;
- active system / ruleset binding;
- source trigger and rule reference;
- before balance, delta, after balance;
- whether the change is generation, spend, special-rule change, or mission reset;
- for a spend: acting force, effect ID, target/scope, listed cost, Domain modifier, actual cost, and resolved world-state changes;
- timing and duration / expiry where applicable;
- public-facing information and any GM-only information kept separate;
- application status for each dependent field.

A single logical event may contain linked fields, but completion is tracked per field. Reuse the existing Runtime Control / Module Closeout field-level commit and recovery contract; do not create a Chaos-specific transaction engine. Track eligibility, resource transition, each world-state effect, visibility, presentation, and persistence independently. A retry resumes the first incomplete field: if the resource transition committed but a world write failed, complete the world write without charging again; if the effect committed but presentation failed, present it without reapplying; if presentation occurred but checkpointing failed, record it as delivered without replay. Mark COMPLETE only when every required field is committed or explicitly NOT_APPLICABLE.

### Mapping to existing Runtime Control evidence

| Chaos event component | Existing Runtime evidence | Recovery rule |
|---|---|---|
| Eligibility / adjudication | source event, rule basis, actor/target qualification, decision status | Reuse the original decision; do not re-adjudicate as a new event on retry |
| Resource transition | Resource Ledger Entry ID, before/delta/after, application status | If already applied, never debit/credit again |
| World-state effect(s) | canonical entity + field paths, before/after values, per-field application status | Resume only unapplied fields; preserve already-applied effects |
| Visibility | public / GM-only projection and recipient scope | Do not expose hidden fields during recovery |
| Presentation | actual response/delivery evidence and recipient | If already delivered, do not replay; if not delivered, present the committed result once |
| Persistence | Runtime checkpoint revision and Runtime Control §14.14 reconciliation manifest reference | Verify each field against the ordered application chain; event ID alone is not proof |

For a partial commit, use the existing `reconciliation_manifest` and Session Log `runtime_application` fields from Runtime Control §14.14. Track `APPLIED`, `PARTIAL`, or `NOT_APPLIED` at the field level. The event is complete only when every required field is applied or explicitly `NOT_APPLICABLE`; unresolved fields resume from the first incomplete dependency. Do not create a parallel Chaos transaction table, second event registry, or separate recovery engine.

A stable event_id is necessary but insufficient for semantic deduplication. Preserve the originating action / roll / world-event identity, mission ID, trigger, and adjudication status. A repeated description of the same action after context recovery must resolve to the original source event; a genuinely new legal opportunity may create a new event even if similar.

If the current balance depends on unresolved events, mark the current value pending rather than inventing a balance. A known increment from an unknown starting balance may be recorded without asserting an absolute balance. The public Chaos Pool must remain queryable as a current value during the active mission.

## 11. Mission boundary

The Field Agent Manual explicitly states that all unused Chaos disappears at the end of each mission.

At Module Closeout / mission completion:
1. Reconcile the final balance when it is known. If it remains UNKNOWN, preserve that fact; do not invent the pre-closeout balance.
2. Record the unused amount as discarded when known; otherwise record discarded_amount: UNKNOWN.
3. Set the closed mission's Pool to 0 as its post-closeout state, even if the pre-closeout balance was UNKNOWN. This does not resolve the historical balance retroactively.
4. Mark the old mission Pool CLOSED; never reuse it.
5. For the next mission, create a separate Pool at 0, then apply the current Branch table's Starting Chaos as a distinct initialization grant.
6. Do not carry unused Chaos into the next mission.
7. Do not confuse mission-level Chaos reset with Branch Loose Ends, Weather Events, or other persistent Campaign state.

## 12. Runtime trigger checklist (internal, event-driven)

This is a trigger-specific prompt, not a per-message checklist. Invoke it only when a valid opportunity from §6 or an explicit rule trigger occurs:

- Is the mission active, and is the current pool verified?
- Is there an eligible actor / force and a concrete reason to act?
- Is this a standard effect, a prepared New Chaos Effect, or a Special Rule?
- Is the target and scope valid?
- Is the action inside the Domain? Apply free-cost / triple-cost treatment and apply the adopted repeatable-free reading for costs ≤3.
- What exact world-state fields change?
- Apply resource and world changes once under one stable event.
- Present the effect and its observable consequences without leaking GM-only information.

## 13. Validation status and required tests

This protocol remains DRAFT / NOT ENABLED until the independent behavior fixtures have been executed in a clean target environment and reviewed. The target GM must receive only the test-input artifact; expected results remain in this GM-only Oracle. R-10–R-12 require host-level write-failure injection and independent readback; without that capability they remain NOT EXECUTED / NOT OBSERVABLE.

This protocol is DRAFT until behavioral validation passes. At minimum test:

1. **No-trigger control:** ordinary player action with no Chaos opportunity causes no pool poll, no spend, and no extra delay.
2. **Generation handoff:** dice module's committed delta updates Chaos exactly once; retry does not duplicate it.
3. **Independent generation:** explicit Special Rule and Disruptive Minor Anomaly modifiers apply exactly when their trigger occurs.
4. **Anomaly opportunity:** active Anomaly acts beyond Focus / near Agents; runtime recognizes the opportunity and evaluates a fitting effect.
5. **GM initiative:** a valid opportunity is not silently ignored merely because the GM is waiting for the player to ask.
6. **No arbitrary adversity:** no effect is spent without supported actor, motive/behavior, target, and rule basis.
7. **Domain costs:** free 1/2/3 effects, triple-cost paid effects above 3, and no triple charge for free effects.
8. **Domain repeatability:** effects costing 3 or less are free and repeatable under the adopted runtime reading.
9. **World materialization:** spend changes the relevant world state, not just the displayed balance.
10. **No-target-Anomaly mission:** Chaos remains tracked and can be used only with an established cause.
11. **Human-caused analogue:** similar event occurs without a Chaos spend when grounded in human behavior.
12. **Mission close:** unused Chaos is discarded and pool is reset to 0; no cross-mission carry.
13. **Player projection:** public pool and effect description are presented; hidden motives and GM-only facts remain protected.
14. **Platform isolation:** the shared Systems runtime contract is used, but no Triangle Agency terms/mechanics leak into Generic GM Training or other system adapters.

## 14. Source-derived rules vs GM operating guidance

**Directly supported by v22 source:** roll-based Chaos generation; public tracking; Chaos as anomalous energy; Anomalies draw on ambient Chaos beyond Focus; near-Agent supernatural action requires spending; GM may nudge Anomalies to spend; no-target-Anomaly missions still track Chaos; human events may resemble Chaos Effects without spending; Domain free/triple-cost rule; standard effect chart; Special Rules and New Chaos Effects; Minor Anomaly and Disruptive generation rules; unused Chaos disappears at mission end.

**Operational interpretation introduced here:** event-driven opportunity recognition; the minimal opportunity signals in §6; the requirement to materialize world-state changes; no per-message polling; event-field shape; validation suite. These are integration rules for executing the source faithfully, not claims that the rulebook itself specifies a formal software state machine.

**Adopted runtime interpretation:** printed page 156 directly establishes that Domain effects costing 3 or less manifest for free. For execution, this protocol treats those free effects as repeatable; this is the selected operational reading of the difference in phrasing on printed page 161, not a claim that the two paragraphs use identical wording.
