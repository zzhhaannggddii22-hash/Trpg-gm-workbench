# Playwall Intermission Integrity Regression v1

> Type: synthetic acceptance fixture  
> System: Triangle Agency / Chinese v22  
> Purpose: verify that the GM checks every Work/Life Balance box mark, including free marks, and does not read unauthorized documents.  
> Information class: GM/QA only. Do not send the Oracle to a player-facing target.

## START

The target GM receives:
- The Triangle Agency Chinese v22 ruleset binding.
- A synthetic Work/Life Balance sheet with the following Competency path positions:
  - Position 1: blank
  - Position 2: blank
  - Position 3: A3
  - Position 4: blank
  - Position 5: blank
  - Position 6: D4
- No prior Playwall authorization.
- A synthetic Campaign rule: one available Time is awarded at complete module close. This house rule changes only the award timing/amount, not the printed mark or unlock procedure.

## ACTIONS

1. A complete module closes. The Agent receives one available Time.
2. The Agent receives Mission MVP.
3. The player chooses to mark the first Competency box for the free MVP mark.
4. The Agent spends the available Time and marks the next Competency box.
5. The player receives another Mission MVP and marks the next Competency box.
6. The player asks whether D4 can now be read.

## ORACLE

Expected resolution:

- Action 3 marks Competency position 1. It is blank; no Playwall document is unlocked.
- Action 4 marks position 2. It is blank; no Playwall document is unlocked. The Time-spend cross-outs on the other two tracks must also be recorded.
- Action 5 marks position 3. It contains A3; A3 becomes authorized even though this is a free Mission MVP mark and no Time is spent.
- The GM must retrieve/read only A3 and apply its actual conditions. The GM must not infer or grant D4.
- Position 6/D4 remains unmarked and unauthorized. The player's question does not create authorization.
- The next module cannot inherit an undocumented A3 effect or a guessed D4 unlock.

## PASS CRITERIA

- Every mark is separately recorded with source, track, position, code, benefit, and cross-outs where applicable.
- The GM checks codes after both Time and free MVP/Probation marks.
- A3 is unlocked on the third mark; D4 remains locked.
- No Playwall document is read before its code is marked.
- Player-facing disclosure is limited to information/effects appropriate to the authorized document and current game.
- Unknown track positions, document reads, or effect applications remain UNKNOWN rather than being guessed.

## FAIL CONDITIONS

- Only Time-spend marks trigger code checks.
- The GM assumes a free MVP mark cannot unlock Playwall.
- The GM reads D4 because it is the next document or because the player asks.
- The GM records a document as read/applied without evidence.
- The GM treats a Time award as if a track box has already been marked.
- A Player Notes projection contains GM-only Playwall material not yet appropriately disclosed.
