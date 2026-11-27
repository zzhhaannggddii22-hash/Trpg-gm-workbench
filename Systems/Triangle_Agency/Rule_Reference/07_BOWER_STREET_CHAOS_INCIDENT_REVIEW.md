# Bower Street｜Chaos Runtime Incident Review

> Classification: GM-only system-rule learning record.
> Status: EVIDENCE-LIMITED / USER-CONFIRMED EXPERIENCE.
> Purpose: preserve the observed Chaos failure mode as a system-layer regression input; do not rewrite historical Campaign events.

## 1. Confirmed evidence

Sources inspected:
- `Campaigns/Zarek/模组/Bower_Street/Sessions/SESSION_01.md`
- `Campaigns/Zarek/模组/Bower_Street/Sessions/SESSION_02.md`
- `Campaigns/Zarek/模组/Bower_Street/09_RESOURCE_LEDGER.md`
- `Campaigns/Zarek/模组/Bower_Street/01_GM_PREP.md`

Confirmed from the available records:

1. SESSION 01 recorded an Ask the Agency event, but its Chaos accounting was omitted in the original resolution. A later temporary +5 report was not independently verified. It remains BOWER-RES-001 / PENDING in the historical ledger.
2. SESSION 02 contains one recoverable complete roll event, BS2-ROLL-001, with a verified +5 Chaos generation delta. It was recorded as BOWER-RES-002, but the absolute balance remained UNKNOWN because SESSION 01's prior balance was unresolved.
3. The available ledger records no verified Chaos spending entries for Bower Street. It records the module's ordinary Chaos Pool as reset to 0 at module close, with historical generation records retained.
4. The Bower Street GM Prep already contained a module-specific Chaos Effects palette, effect costs, Domain treatment, anomaly Focus/Domain facts, and a same-event public resource accounting requirement. Therefore, the observed weakness was not simply “the module had no Chaos notes.”
5. The user explicitly reports that the GM did not use Chaos to create meaningful situation changes and also missed generation and spending during play. The user separately confirms that roll-generation handling has since been addressed through the roll-resolution module.

## 2. Evidence limits

- SESSION 01 is a structured log, but it does not contain the complete original dialogue and all roll records.
- SESSION 02 is explicitly a recovered summary, not a verbatim transcript. It preserves only one complete roll event and selected closeout facts.
- The current records do not establish every moment when a Chaos Effect was legally available, the exact Pool at every point, or which specific effect should have been chosen.
- Do not retroactively invent Chaos spends, effects, Anomaly actions, or world changes to make the old ledger look complete.
- Do not infer that every uncanny scene in the module was necessarily a paid Chaos Effect. The module and v22 define specific triggers, costs, Domain states, and exceptions.

## 3. Failure classification

| Failure mode | Evidence status | Interpretation |
|---|---|---|
| Generation accounting omission | CONFIRMED | At least one SESSION 01 roll's Chaos change was omitted and later remained unverified. |
| Generation-to-runtime handoff | CONFIRMED DESIGN GAP | A roll result was not reliably converted into a verified current public Pool at the point of play. |
| Spending/accounting omissions | USER-CONFIRMED; detailed events unavailable | User reports missed spending; current ledger contains no verified spend entries. Exact missed transactions cannot be reconstructed. |
| Active world-effect use | USER-CONFIRMED EXPERIENCE | GM treated Chaos mainly as a balance to record rather than an active tool to alter situations. |
| Exact missed trigger/effect pairs | UNKNOWN | The recovered Session 02 summary cannot support a complete event-by-event reconstruction. |

## 4. Root-cause hypothesis

The likely architectural failure was a one-way resource pipeline:

`roll -> calculate Chaos delta -> update balance`

with no reliable return path:

`world event / Anomaly goal / Focus boundary -> valid Chaos opportunity -> effect selection -> resource spend -> world-state transition`

The second path was not made an explicit runtime responsibility. The module's effect palette existed in prep, but no lightweight trigger-driven procedure reliably connected it to the active scene, Anomaly behavior, Domain state, and world consequences.

This is a hypothesis about the workflow architecture, not a claim that the recovered logs prove every internal decision.

## 5. Corrective requirements

The Triangle Agency Chaos Runtime Protocol must:

1. Consume the roll module's committed generation event rather than reimplementing roll generation.
2. Accept independent system generation sources such as Special Rules and Disruptive Minor Anomalies.
3. Detect valid Anomaly opportunities (beyond Focus, near-Agent supernatural action, interference with established goals, prepared behavior) without polling on every player message.
4. Proactively evaluate a fitting effect when a valid opportunity exists; do not wait for the player to ask the GM to use Chaos.
5. Reject arbitrary adversity when no actor, motive, trigger, target, or rule basis supports the effect.
6. Apply Domain cost rules and preserve unresolved source ambiguity.
7. Apply resource spend and material world-state changes as one stable event.
8. Keep public Pool current and visible; preserve GM-only information boundaries.
9. Reset unused Pool at mission end and never carry it across missions.
10. Prove both proactive trigger recognition and no-trigger performance through regression.

## 6. Non-goals

- Do not change Bower Street's historical Session Logs or fabricate missing Chaos transactions.
- Do not add a generic Chaos concept or Chaos fields to `GM_Training/`.
- Do not hard-code Triangle Agency Chaos mechanics into generic runtime or dice routing.
- Do not force a Chaos Effect into every scene or every Session.
- Do not make Chaos spending a punishment mechanism detached from Anomaly Focus, established goals, and scenario facts.
