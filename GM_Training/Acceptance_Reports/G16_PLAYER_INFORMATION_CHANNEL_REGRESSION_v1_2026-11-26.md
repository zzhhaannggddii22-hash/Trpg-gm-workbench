# G-16 Player Information Channel Regression｜2026-11-26

> Test ID: G16-CHANNEL-01  
> Fixture: G16_PLAYER_INFORMATION_CHANNEL_REGRESSION_v1  
> Target Workbench commit: 9decd556ef63eebb7505631191bb7e36e937a803  
> Execution mode: SINGLE_SESSION_SELF_TEST  
> Review mode: post-run oracle review  
> Overall: **PARTIAL**  
> Scope: output-channel behavior in this fixture only; not a platform-level isolation test or real-session qualification.

## 1. Source verification

The executor reported reading the fixture and required runtime files at the exact target commit. The reviewer independently fetched START.md and ORACLE.md at that commit.

| File | Reported Blob SHA |
|---|---|
| Acceptance_Test_Fixtures/G16_PLAYER_INFORMATION_CHANNEL_REGRESSION_v1/START.md | 26fefa805b6f20da994a5babd4157148d6a096c3 |
| SKILL.md | 9d3aa4411ab1f6c3abaeab880cf19f90470dc529 |
| CHARACTER_SIMULATION_SKILL.md | 4eaecb2ffa7e8a6128e705f35ac093d7e7f21e80 |
| NARRATIVE_PRESENTATION_SKILL.md | cabec206cef41176830c1dda8647f384e2e53a56 |
| 07_RUNTIME_CONTROL_PROTOCOL.md | f4e300080de2206a827e70bdff0b58ba6630fe43 |
| SELF_TESTING_PROTOCOL.md | b1ccc1912528223b46c196e08edfd7e8fc2ace7e |

Oracle Blob SHA: 3a8b3ffd6e3a49d873fe0e6d43672d4c7be0eccb. The oracle was fetched by the reviewer only after the executor supplied all three branch outputs.

## 2. Branch results

### Branch A — PASS

Observed output:
- Lin Yue looks at the key, brings the register closer, opens it and checks pages.
- Her only dialogue is: “我先核对一下登记簿。”
- No narration or dialogue reveals that she saw the key the previous evening, the time, the archive counter, or her recognition/memory.

No private-memory leakage observed.

### Branch B — PASS

Observed dialogue:
> 「见过。昨晚大概七点四十左右，我在档案室柜台上见过这把系蓝线的钥匙。」

The disclosure occurs in actual NPC dialogue. The follow-up “当时它就在柜台上” repeats the established location detail; it does not add a new source, owner, incident, motive, or other hidden fact.

No premature disclosure or material fact expansion observed.

### Branch C — PASS

Observed output describes a brief gaze toward the key, moving and opening the register, picking up the pen, and checking pages. These are observable actions. It does not state that Lin Yue recognized the key, recalled the previous evening, or experienced a hidden emotion.

No private-memory leakage or hidden-psychology assertion observed.

## 3. Cross-branch isolation

**UNKNOWN (output-level non-contamination observed; internal reset not independently verifiable).**

The outputs for A and C contain no information disclosed in B, and B does not rely on player knowledge from another branch. However, all branches were generated in one assistant response in one Chat. The executor's statement that each branch was reset to the same snapshot is a procedural self-report, not an independently observable state-reset trace.

The fixture therefore demonstrates correct compartmentalized output in this sample, but does not establish true runtime/session state isolation.

## 4. Overall decision

**PARTIAL**

- Branch A: PASS
- Branch B: PASS
- Branch C: PASS
- Cross-branch isolation: UNKNOWN
- Hard leakage in this sample: none observed

The PARTIAL result is due solely to insufficient evidence for independent state isolation. It is not a branch-level output failure.

## 5. Evidence boundary and follow-up

1. This is a single-session self-test, not an independent blind test.
2. It does not establish hidden platform runtime behavior, cross-chat memory isolation, or performance in a real player session.
3. The prior Stress Test 01 information-channel FAIL and G-16 OPEN status remain unresolved; this sample does not erase historical failure evidence.
4. Do not close G-16, promote any narrative capability to T3/T4, or claim runtime-wide reliability from this report.
5. Next useful step: a targeted high-pressure information-channel regression, followed by review of the original Stress Test failure path. Prefer an independently executed target Chat if isolation is part of the claim.
