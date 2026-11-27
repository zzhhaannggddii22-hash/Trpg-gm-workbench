# Playwall Unlock & Intermission Integrity Protocol

> System: `triangle_agency`  
> Ruleset: 《三角机构》中文 v22  
> Authority: system-specific execution protocol; the full rulebook and the active Campaign's approved house rules remain authoritative.  
> Scope: all Work/Life Balance track marks, Playwall authorization, document handling, and intermission reconciliation.

## 1. Governing rule

A Playwall document is authorized by a **marked track box that actually contains that document's code**. The code on the marked box—not the track name, character questionnaire, promotion label, mission narrative, or a GM's expectation—controls access.

The Chinese v22 rulebook's Spending Time section (printed p.123) states that when a marked box contains a Playwall document code, the Agent is authorized to find and privately read that document and obtain its listed benefits. The Work/Life Balance sheet (VISUAL_299) separately instructs the table to visit documents matching codes that were marked.

Therefore:

- Check every box mark, not only marks produced by spending Time.
- A free Competency mark from Mission MVP, a free Anomaly mark from Probation, and any other rule-authorized box mark can unlock a code if the marked box contains one.
- A crossed-out box is unavailable; crossing it out does not unlock its code.
- An ordinary benefit that does not mark a box (for example, the Participant connection increase) does not unlock a Playwall document.
- Never read ahead, browse adjacent codes, or treat a code printed elsewhere on the character sheet as authorization.

## 2. Separate the mark event from the Time transaction

### Spending Time

For each actual Time expenditure:

1. Confirm the Campaign's available-Time balance and the chosen track.
2. Mark the earliest available, unmarked box on that track.
3. Cross out one last available box from each of the other two tracks, as required by the rulebook.
4. Apply the chosen track's printed primary benefit.
5. Inspect the newly marked box for a Playwall code and run §3.
6. Record the complete transaction before proceeding to the next Time expenditure.

A Campaign house rule may change **when/how much Time is awarded**. It does not silently change what a marked box does, the cross-out rule, or Playwall authorization. Record the house rule in the Campaign's adjudication file and apply it only within that Campaign.

### Other mark sources

- **Mission MVP:** mark one Competency box; do not cross out boxes on the other tracks. Check the marked box for a code.
- **Probation:** mark one Anomaly box; do not cross out boxes on the other tracks. Check the marked box for a code.
- **Other explicit rule effects:** if they instruct the Agent to mark a Work/Life Balance box, apply the code check unless that rule explicitly overrides it.
- **Participant:** its Connection increase is not a track mark and does not itself unlock a document.

Do not assume a free mark is exempt from Playwall. Do not assume a Time mark is the only way to unlock a document.

## 3. Mandatory Playwall handling for every newly marked box

For each marked box, record and resolve:

1. **Track and exact box position** (1–30, following the printed path direction).
2. **Mark source**: TIME_SPEND / MISSION_MVP / PROBATION / OTHER_RULE.
3. **Code printed in that exact box**: exact code or NONE.
4. **Authorization result**: UNLOCKED / NO_CODE / BLOCKED_OR_UNKNOWN.
5. If unlocked, retrieve **only that exact document** from the authorized v22 source.
6. Read the document privately as GM and extract its complete operative payload: immediate benefits, choices, costs, prerequisites, restrictions, timing, required scenes, follow-up document codes, and any GM/player information boundary.
7. Apply only effects whose prerequisites are met. Do not silently grant future, conditional, or purchasable benefits.
8. Record whether the document was read, what effects were applied or deferred, and what the player was told or shown.

A document's unlock does not mean every paragraph must be dumped into player-facing narration. The document is personal material; share the information/effects relevant to the current game, preserving the document's intended private and reveal structure. Keep GM-only operational notes separate from Player Notes.

If a newly authorized document cannot be retrieved or its source/version cannot be verified, record BLOCKED_OR_UNKNOWN and pause only effects dependent on it. Do not infer the content from a later document, a wiki, model memory, or an adjacent code.

## 4. Code lookup and source discipline

- Use the exact Work/Life Balance sheet and the current character's actual marked/crossed-out state.
- Follow the printed track path; do not sort codes alphabetically or assume a code list is the path order.
- The Competency track's reconstructed path in v22 proceeds from the upper-left start across the top row, turns at the right, then returns along the bottom row from right to left. Its Playwall codes occur at marked positions 3, 6, 9, 12, 15, 18, 21, 24, and 27: **A3 → D4 → G3 → J3 → N3 → Q3 → T3 → W8 → Y2**.
- Reality and Anomaly codes must be read from the exact v22 track diagram and the actual character sheet. Do not infer their box positions from an unordered list of codes. If the diagram/character sheet is unavailable or ambiguous, keep the position/code UNKNOWN until verified.
- ARC self-assessment codes (for example, the codes printed beside Anomaly questionnaire answers) are not Work/Life Balance marks and do not authorize those documents.

## 5. Intermission sequence

Run this sequence whenever the Campaign reaches its authorized growth point:

1. Confirm the module is closed and determine which rewards/penalties actually apply.
2. Reconcile persistent resources and automatic module-end resets according to the Campaign's resource-scope rules.
3. Determine Time awarded under the active Campaign rule; record award and available balance separately.
4. Determine all applicable Superlatives and their free track marks.
5. Resolve each mark as an independent event in actual order. For each mark, apply cross-outs if and only if required, grant its track benefit, and check its code.
6. Read and resolve newly unlocked Playwall documents before moving to later dependent choices.
7. Complete required scenes and player choices. Do not convert a proposed plan into a completed event.
8. Update the character sheet, Work/Life Balance sheet, Campaign Playwall ledger, relevant module Runtime/Session records, and Player Notes projection as applicable.
9. Independently read back the updated records and reconcile every mark, code, document, effect, and balance.
10. Close the intermission only when no required mark/document/effect is pending or explicitly recorded as BLOCKED/DEFERRED with a reason.

A module may be narratively closed while its intermission remains OPEN. Do not begin the next module's Preflight as though growth were complete if a mandatory Playwall item remains unresolved.

## 6. Required ledger fields

Each mark event must preserve:

- `mark_event_id`, Campaign, module, and source Session/event;
- track, exact box position, prior state, new state;
- mark source and whether Time was spent;
- cross-outs applied to the other tracks, including exact positions;
- track benefit and its application status;
- exact Playwall code or NONE;
- authorization, source document/version, retrieval/read status;
- document effects: APPLIED / PARTIAL / DEFERRED / NOT_APPLICABLE / UNKNOWN;
- player-facing disclosure status and evidence reference;
- character-sheet / Runtime / Player Notes synchronization references.

Never backfill a missing historical read, application, presentation, or player choice. Use UNKNOWN / NOT_RECORDED where evidence is absent. Corrections are append-only; do not erase the original history.

## 7. Failure handling

- **A marked code was not checked:** intermission integrity failure. Stop dependent progression, reconstruct the mark from source records, then retrieve only the now-authorized document and resolve it.
- **A code was unlocked but document effects were omitted:** append a corrective entry; preserve what the player already experienced; do not rewrite prior scenes.
- **A document was read before authorization:** record the access incident; do not treat the content as player/character knowledge or grant its effects. Follow the Campaign's incident protocol.
- **Track position or source evidence is missing:** do not guess. Keep the affected mark/document status UNKNOWN and request/locate the authoritative sheet or historical evidence.
- **A historical audit has incomplete evidence:** distinguish confirmed omission from missing proof. Absence of a log entry is not proof that the document was never read; applied benefits may be corroborating evidence but should be identified as such.

## 8. Rule references

- 《三角机构》中文 v22, printed p.123, “Spending Time”.
- 《三角机构》中文 v22, printed pp.127–128, “Competency in Detail” and related track rules.
- 《三角机构》中文 v22, printed p.134, Mission Superlatives (MVP / Probation / Participant).
- Work/Life Balance sheet, `VISUAL_299`, including the instruction to visit documents matching marked codes.
- Playwalled Documents section, beginning at printed p.198.

This protocol operationalizes those rules; it does not replace the rulebook or authorize any currently locked document.
