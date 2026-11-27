# System Rule Runtime Integration Protocol

> Scope: shared architecture contract for system-specific rule runtimes.
> Location: `Systems/`
> This document defines how a rule system's mechanics become operational. It does not define any game's mechanics and must not be copied into `GM_Training/`.

## 1. Purpose and ownership

The workbench is a multi-system TRPG platform. Generic GM capabilities remain in `GM_Training/`; game mechanics, system resources, triggers, costs, effects, timing, and system-specific state belong to the bound system under `Systems/<System>/`.

This protocol is the shared integration contract between those layers:

- **Generic GM layer:** understands player intent, maintains a coherent world, narrates consequences, and follows the active system's declared runtime contract. It does not own or invent system mechanics.
- **System layer:** defines the actual rule, trigger conditions, legal transitions, resource semantics, exceptions, and system-specific outputs.
- **Campaign layer:** stores the current campaign's state, approved table adaptations, and event history. It does not redefine system-wide rules.
- **Module / Session layer:** supplies local facts and scenario conditions. It does not silently override system mechanics.

A system adapter may implement only the mechanics that exist in that system. No mechanic, resource, term, or workflow is assumed to exist across all systems. A resource-handling interface is optional: it is a reusable execution pattern, not a platform-wide resource mechanic. A system with no declared GM-operated resource does not instantiate that interface, create placeholder balances, or perform resource checks.

## 2. Event-driven integration, not per-action polling

System mechanics are integrated by **trigger**, not by adding a checklist to every player message.

- A passive rule that shapes ordinary adjudication is internalized as a default behavior. It does not require a fresh file read or an announced procedure on every action.
- A resource or subsystem is activated only when the active system adapter declares that it exists and a declared rule trigger, state transition, explicit player action, world event, or scheduled system phase makes it relevant.
- If the bound system declares no GM-operated resource adapter, there is no resource subsystem to inspect. Do not scan for one, ask whether a resource exists, or add generic resource state.
- Once a static rule source has been verified for the active ruleset, reuse it in the current context. Re-read only when version, scope, evidence, exception, or unresolved dependency requires it.
- Do not scan all system rules after every action. Do not poll every subsystem when no trigger has occurred.
- A triggered subsystem may evaluate its own pending consequences without requiring unrelated subsystems to run.

The cost of a rule integration is justified when it prevents missed rules or state drift. If it adds recurring work without a rule trigger or material benefit, redesign it.

## 3. Rule-to-runtime contract

Each system-specific runtime protocol should state, where applicable:

1. **Identity and scope:** system ID, exact ruleset version, and any Campaign-scoped adaptations.
2. **Trigger:** the event or condition that activates the mechanic.
3. **Inputs:** authoritative state fields and their sources.
4. **Eligibility:** actors, targets, capabilities, permissions, and preconditions.
5. **Resolution:** legal choices, sequence, costs, randomization, and exceptions.
6. **Effects:** what changes in the world, characters, resources, relationships, or scenario state.
7. **Timing:** immediate, deferred, phase-based, or end-of-session/module.
8. **Visibility:** what is public, private, or GM-only.
9. **Persistence:** fields to update, event evidence, and reset/expiry conditions.
10. **Failure and uncertainty:** what remains unresolved and which dependent sub-action must pause.

Do not invent a field or rule merely to complete this template. Mark unsupported items as unknown or not applicable.

## 4. Separate resource accounting from world-state execution

A system resource is not operational merely because its balance is correct.

When a triggered mechanic consumes or changes a resource, the runtime must distinguish:

- **Resource transition:** the verified before-value, source event, delta, and after-value.
- **Rule effect:** the specific outcome authorized by the mechanic.
- **World consequence:** the resulting change to locations, people, threats, access, time, information, or other system-defined state.
- **Presentation:** what the player can perceive or is entitled to know.

These may be recorded as one stable event with linked effects. Do not claim a world effect occurred merely because a resource was spent; do not deduct a resource merely because an effect would be dramatic. Both require the system's rule basis.

## 5. Active pressure and opportunity loops

If a system defines a resource or subsystem that can actively change the world, its adapter must explain how the GM recognizes meaningful opportunities to use it.

The adapter should define:

- which world events or player actions create a legitimate opportunity;
- which eligible system actor can cause the effect;
- what that actor is trying to achieve, according to established goals and system rules;
- what the effect can change and what it cannot;
- whether the effect requires a resource payment, has a free-use exception, or is independent of the resource;
- how the effect changes the next state of play.

This is not permission to manufacture arbitrary adversity. The world effect must be supported by system rules, established actor motives, scenario facts, and the current state. The GM should not wait passively when a valid system opportunity is already present, but should not force an effect when its trigger or fictional cause is absent.

## 6. Runtime efficiency

Use three operating scopes:

- **Ambient default:** passive rule guidance already in the active context; no repeated retrieval.
- **Triggered resolution:** load or apply only the relevant system adapter when its trigger occurs.
- **High-impact verification:** inspect the complete authoritative rule text when an exception, conflict, irreversible outcome, or missing rule detail could change the result.

A new Session re-confirms the system binding and dynamic state. It does not require re-reading every static rule file. A new system requires its own adapter; no other system's mechanics may be used as a fallback.

## 7. Validation

A system adapter is not accepted solely because its documentation exists or links resolve. Validate:

- trigger recognition and non-trigger controls;
- legal resource changes and no double application;
- world effects actually materialize when authorized;
- effects do not occur without authorization;
- timing, expiry, reset, and scope;
- player/GM information boundaries;
- no extra work on ordinary actions;
- isolation from other systems.

Tests must distinguish documentation/static checks from behavioral execution. A passing repository suite does not prove a model will invoke the mechanic correctly in live play.


## 8. Mechanism activation and state ownership

A system adapter may declare a mechanism using these status semantics. This is a routing contract, not a requirement to build a plugin framework:

| Status | Runtime behavior |
|---|---|
| NOT_APPLICABLE | Skip entirely; do not create fields or perform checks. |
| DISABLED | Mechanism exists in the system but is not enabled for this Campaign / Module; do not execute. |
| ENABLED | Execute only on its declared triggers and lifecycle boundaries. |
| UNKNOWN | Verify during Preflight only if the current task depends on the mechanism. |
| PENDING | Pause only the operation that depends on the unresolved configuration or state. |

The adapter declaration should identify trigger classes, required dynamic inputs, authoritative state owner, permitted writes, and reset / expiry rules. A missing optional mechanism is NOT_APPLICABLE, not UNKNOWN and not a Preflight failure.

Dynamic Campaign facts (including current Branch Loose Ends totals) belong to Campaign state records, never to a system-wide rules protocol. A Module may preserve a timestamped initialization snapshot, but that snapshot does not become the current Campaign authority.

For a resource with mission scope, close the previous mission's resource instance at 0, then instantiate a new mission-scoped instance at 0 before applying any rule-defined starting grant. The reset of a closed instance and the grant to a new instance are distinct events with distinct mission IDs. This pattern is system-neutral; the amount and grant rule remain system-specific.

## 9. Reuse existing commit and recovery controls

System adapters must map each multi-field event to the existing Runtime Control / Module Closeout commit manifest. Track dependent fields separately (resource, world state, visibility, presentation, persistence). An event is not complete merely because one field committed. Recovery resumes incomplete fields and must not repeat completed fields. Do not introduce a second transaction engine or duplicate ledger.

Stable event IDs must be anchored to their originating action / roll / world event and adjudication state. ID uniqueness alone is insufficient to prevent semantic duplicates after context compression or Session recovery.