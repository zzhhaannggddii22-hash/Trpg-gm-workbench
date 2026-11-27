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

1. **Mission setup:** verify the active mission, current Branch Loose Ends tier, starting environmental Chaos (if applicable), target Anomaly / no-target condition, Focus, Domain, Impulse, and prepared effect palette.
2. **During mission:** accept Chaos generation from the already integrated roll-resolution event and any other explicit system rule (e.g. Special Rule or Disruptive Minor Anomaly). Keep the public balance current. Evaluate Chaos Effects when a valid world-action opportunity occurs; do not poll or spend on every player message.
3. **Effect resolution:** verify eligibility, cost, Domain treatment, selected effect, target, timing, and resulting state. Apply the resource transition and world consequence under one stable event.
4. **Mission close:** reconcile all generated/spent/other changes, then clear all unused Chaos at the mission boundary. Do not carry a leftover pool into the next mission.
5. **Recovery / retry:** reuse the same stable event and its completed fields. Never re-roll, re-spend, or re-apply a world effect because the response was retried.

## 4. Generation: input contract, not a second dice engine

The roll-resolution module owns the standard roll's generation calculation and result. This protocol consumes its committed result; it must not recalculate or override it.

- Each die that does not show `3` adds `1` Chaos, subject to the system's explicit exceptions and the final resolved roll rules.
- A standard 6d4 roll can generate up to 6 Chaos before other modifiers.
- Stable Success / Triscendence exceptions and Burnout handling belong to the Dice Resolution adapter; use its final verified Chaos delta.
- Other explicit system effects can add Chaos independently. Examples in v22 include a personalized Special Rule that adds Chaos when a stated trigger occurs and each nearby Disruptive Minor Anomaly adding `+1` whenever Chaos is generated.
- Do not add Chaos merely because an event is dramatic, dangerous, or supernatural unless a rule or approved adaptation authorizes it.

**Integration seam:** when the roll module commits a generation event, this runtime receives `event_id`, `chaos_delta`, rule basis, and final result. It applies that delta exactly once and makes the new balance available to the world-effect loop.

## 5. Starting Chaos and Branch pressure

The v22 source includes a Branch Loose Ends table that relates regional Loose Ends to starting environmental Chaos (printed page 165). This is the **system-level default**. It is not permission to ignore the active Campaign Binding or a specifically approved Campaign adaptation.

At mission setup, resolve the value in this order:

1. Read the active Campaign Binding and its approved adjudication entry.
2. If an explicit, valid Campaign-scoped ruling overrides the v22 starting-Chaos table, apply that ruling only within its declared scope.
3. Otherwise, use the v22 Branch Loose Ends table and the verified current Branch count.
4. If the Binding, adjudication record, module prep, or source interpretation conflict, mark the starting value PENDING / DISPUTED and resolve the provenance before opening the Pool. Do not silently choose 0 or infer a value.

The printed page 165 table lists these rows:

| Branch Loose Ends | Starting Chaos |
|---:|---:|
| 0 | 0 |
| 11 | 5 |
| 22 | 10 |
| 33 | 15 |
| 44 | 20 |
| 55 | 25 |
| 66 | N/A; mission-ending / retirement rules apply |
| 77 | N/A; regional removal rule applies |

Do not invent a smooth formula or extrapolate beyond the printed table. If the current Loose Ends count falls between listed rows and the table's band/threshold interpretation is not established by the active source, verify that interpretation before assigning a value.

An escaped Anomaly adds 7 Loose Ends to the Branch total; this is not itself a direct +7 Chaos event. Loose Ends / Weather Events remain a separate system subsystem. This protocol consumes their verified starting-Chaos result and must not duplicate their roll, escalation, removal, or retirement procedures.

**Known provenance issue to preserve for review:** the current Zarek Campaign Binding records a default ordinary Chaos Pool start of 0 unless the module says otherwise, while Bower Street prep records a concern that the v22 Branch Loose Ends starting-Chaos rule may need to be reconciled and that the 0 default was not represented in Q01–Q04. This is a Campaign-layer authority/provenance issue, not a reason to rewrite the system rule. Before applying it in a future Zarek module, verify that the 0 default has a valid Campaign-scoped approval record or resolve the discrepancy. Do not migrate this Zarek default to another Campaign.

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

Before spending, verify:

1. The mission is active and the pool balance is verified.
2. The acting Anomaly / force is eligible and has a supported reason to act.
3. The effect is in the standard Chaos Effects chart, a prepared New Chaos Effect, or a Special Rule with its own exact trigger.
4. The target and scope are supported by the effect text and current facts.
5. The correct Domain cost treatment is applied.
6. The resource transition and world effect can be resolved and recorded together.

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

### Domain Benefits and source ambiguity

The v22 Domain Benefits paragraph on printed page 156 says:
- Chaos Effects costing `3` or less can manifest for free inside the Anomaly's Domain.
- Any Chaos that is spent has its actual cost multiplied by three.

The personalized-effects paragraph on printed page 161 says effects costing **less than** `3` can be used infinitely within the Domain. The difference between “3 or less is free” and “less than 3 is infinitely usable” is preserved as a source-text ambiguity about the unlimited-use statement at exactly 3. Until resolved by the source owner / user, apply the explicit Domain Benefits cost statement (3 or less manifests free), but do not claim the text unambiguously grants infinite repeated use at exactly 3. Record the ambiguity for review.

Outside the Domain, use the listed effect cost. Inside the Domain, apply the printed-page-156 rule: effects at 3 or less cost 0; effects above 3 consume three times their listed cost. Do not multiply free effects by three.

### Custom effects and Special Rules

- **Special Rule:** a specific, consistent rule tied closely to an Anomaly's Focus/function may occur without spending Chaos. It must have an exact trigger and stable behavior. Examples include a rule that adds Chaos when someone screams. This is not a free-form GM complication.
- **New Chaos Effect:** a flexible action related to the Anomaly's powers but not a strict standing rule. Define its effect and cost; greater disruption to Reality's narrative should cost more. The source gives examples at 2 / 4 / 6 / 8 Chaos. Effects costing less than 3 are described as infinitely usable within the Domain; preserve the ambiguity at exactly 3 noted above.
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

A single event can contain a resource delta and several linked world effects. Apply each field once. A retry reads back the same event and does not repeat its delta or effect.

If the current balance depends on unresolved events, mark the current value pending rather than inventing a balance. A verified zero delta leaves the verified value unchanged. The public Chaos Pool must remain queryable as a current value during the active mission.

## 11. Mission boundary

The Field Agent Manual explicitly states that all unused Chaos disappears at the end of each mission.

At Module Closeout / mission completion:
1. Verify the mission's final Chaos balance and all relevant generation/spend events.
2. Record the amount discarded as unused Chaos.
3. Set the active mission pool to 0 for the closed mission.
4. Do not carry it into the next mission.
5. Do not confuse mission-level Chaos reset with Branch Loose Ends, Weather Events, or other persistent campaign/system state.

## 12. Runtime trigger checklist (internal, event-driven)

This is a trigger-specific prompt, not a per-message checklist. Invoke it only when a valid opportunity from §6 or an explicit rule trigger occurs:

- Is the mission active, and is the current pool verified?
- Is there an eligible actor / force and a concrete reason to act?
- Is this a standard effect, a prepared New Chaos Effect, or a Special Rule?
- Is the target and scope valid?
- Is the action inside the Domain? Apply free-cost / triple-cost treatment and preserve the 3-cost ambiguity.
- What exact world-state fields change?
- Apply resource and world changes once under one stable event.
- Present the effect and its observable consequences without leaking GM-only information.

## 13. Validation status and required tests

This protocol is DRAFT until behavioral validation passes. At minimum test:

1. **No-trigger control:** ordinary player action with no Chaos opportunity causes no pool poll, no spend, and no extra delay.
2. **Generation handoff:** dice module's committed delta updates Chaos exactly once; retry does not duplicate it.
3. **Independent generation:** explicit Special Rule and Disruptive Minor Anomaly modifiers apply exactly when their trigger occurs.
4. **Anomaly opportunity:** active Anomaly acts beyond Focus / near Agents; runtime recognizes the opportunity and evaluates a fitting effect.
5. **GM initiative:** a valid opportunity is not silently ignored merely because the GM is waiting for the player to ask.
6. **No arbitrary adversity:** no effect is spent without supported actor, motive/behavior, target, and rule basis.
7. **Domain costs:** free 1/2/3 effects, triple-cost paid effects above 3, and no triple charge for free effects.
8. **Cost-3 ambiguity:** no claim of unlimited repeated use at exactly 3 without an authoritative ruling.
9. **World materialization:** spend changes the relevant world state, not just the displayed balance.
10. **No-target-Anomaly mission:** Chaos remains tracked and can be used only with an established cause.
11. **Human-caused analogue:** similar event occurs without a Chaos spend when grounded in human behavior.
12. **Mission close:** unused Chaos is discarded and pool is reset to 0; no cross-mission carry.
13. **Player projection:** public pool and effect description are presented; hidden motives and GM-only facts remain protected.
14. **Platform isolation:** the shared Systems runtime contract is used, but no Triangle Agency terms/mechanics leak into Generic GM Training or other system adapters.

## 14. Source-derived rules vs GM operating guidance

**Directly supported by v22 source:** roll-based Chaos generation; public tracking; Chaos as anomalous energy; Anomalies draw on ambient Chaos beyond Focus; near-Agent supernatural action requires spending; GM may nudge Anomalies to spend; no-target-Anomaly missions still track Chaos; human events may resemble Chaos Effects without spending; Domain free/triple-cost rule; standard effect chart; Special Rules and New Chaos Effects; Minor Anomaly and Disruptive generation rules; unused Chaos disappears at mission end.

**Operational interpretation introduced here:** event-driven opportunity recognition; the minimal opportunity signals in §6; the requirement to materialize world-state changes; no per-message polling; event-field shape; validation suite. These are integration rules for executing the source faithfully, not claims that the rulebook itself specifies a formal software state machine.

**Open source ambiguity:** printed page 156 says Domain effects costing 3 or less can manifest for free; printed page 161 says effects costing less than 3 can be used infinitely in the Domain. The unlimited-repeat boundary at exactly 3 is not silently resolved here.
