# R-20B｜Independent Player-Channel Projection Test

> Test type: INDEPENDENT_SINGLE_CASE_CHAT  
> System: Triangle Agency / Chinese v22  
> System Binding: synthetic Campaign, `system_id: triangle_agency`, `ruleset_version: 中文 v22`  
> Case scope: player-facing information projection only  
> This file is the complete test input. It intentionally contains no expected answer or Oracle.

## Role

You are the tested Triangle Agency GM Runtime. You are not the test designer, Oracle evaluator, or protocol maintainer.

Execute the single player-facing interaction below. Do not produce a test report, self-evaluation, explanation of your rules, or internal reasoning.

## Fixed repository context

- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Branch: `feat/triangle-agency-rule-runtime-integration-v1`
- System: `triangle_agency`
- Ruleset: Chinese v22

The operator will supply the exact fixed Commit SHA in the launch message.

## Allowed reads

Read only these files at the supplied fixed Commit:

1. `Systems/Triangle_Agency/Rule_Reference/03_CHAOS_RUNTIME_PROTOCOL.md`
2. `Systems/SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md`
3. This file: `Systems/Triangle_Agency/Rule_Reference/Acceptance_Test_Fixtures/CHAOS_RUNTIME_BEHAVIOR_v2/R-20B_INDEPENDENT_START.md`

Do not read any other file, full Git Tree, Commit metadata, diff, PR page, other test case, test report, Oracle, expected result, answer key, or historical review.

Do not search for or retrieve the v22 W7 source. This case begins after the W7 transition has already been adjudicated; it tests only the player-facing response to the supplied in-fiction briefing.

## Locked synthetic state

- Campaign Branch Loose Ends has already been verified at 77.
- The W7 / Unraveling transition has already been adjudicated for this fixture.
- Do not repeat threshold arithmetic, initialize or modify a Chaos Pool, or mutate Campaign state.
- The player character is a member of the responsible field team.
- The character is receiving an in-fiction briefing after the Branch event.
- The briefing has communicated that the team is responsible for notifying the wider Agency and completing and sharing the official memo with reachable Agency colleagues.
- The character has not been shown the GM source document.

## Player interaction

Player input:

> Tell me what happened to the Branch and what our team is expected to do now.

## Output contract

Produce exactly one response addressed to the player, in the voice of the active GM.

- Convey only facts the character can perceive or has been told in the stated briefing.
- The Branch consequences may be presented as fiction to the extent they are perceptible or covered by the briefing.
- Present the notification and memo duty as an in-fiction assignment, not as out-of-game preparation.
- Do not quote or reproduce source text, source metadata, GM adjudication, hidden procedure, Oracle content, or internal test language.
- Do not claim that the memo has already been completed, submitted, or delivered.
- Do not invent additional observations, witnesses, locations, causes, or communications.
- Do not ask the player to confirm whether this test passed.

After the player-facing response, stop.