# P0 第三轮回归增量夹具 v3

> 本文件叠加于 v1 与 v2；不替代既有测试。只使用合成系统与数据，禁止读取或修改正式 Campaign。

## 0. 固定边界与基线

- 必须同时执行 v1 RT-01～RT-18、v2 全部 REG 项，以及本文件 REG-16C/D-PERSIST、REG-13-RISK、REG-12-RAW、REG-PRIVACY。
- 测试对象：Ember Protocol 0.9.4 / Iron Dice 3.2 合成系统。
- 每个子测试从独立隔离快照开始；保存真实文件写入、故障注入、进程重启和独立读回证据。
- 无法执行真实持久化/独立进程冷读时标 SIMULATED 或 NOT TESTABLE，不得写 PASS。
- 不得修改正式 Campaign、Module、角色卡、Session Log、Runtime State、Player Notes 或 CANON。

## 1. REG-16C-PERSIST｜重复事件争议必须持久化

### 初始 PREPARE

~~~yaml
batch_id: BATCH-C-PERSIST
base_revision: 7
target_revision: 8
events:
  - event_id: EVT-C-21
    payload_version: 1
    payload_fingerprint: sha256:aaa111
    visibility: PLAYER_VISIBLE
    recipient_scope: player
    projection_targets: [RUNTIME_STATE, SESSION_LOG, PLAYER_NOTES]
~~~

### 故障注入数据

Session Log 在同一 batch 中出现两条有效记录：

~~~yaml
- event_id: EVT-C-21
  batch_id: BATCH-C-PERSIST
  base_revision: 7
  target_revision: 8
  payload_version: 1
  payload_fingerprint: sha256:aaa111
  record_locator: session_log/events/line-41
  content: "Mira said the west gate was closed at dusk."
- event_id: EVT-C-21
  batch_id: BATCH-C-PERSIST
  base_revision: 7
  target_revision: 8
  payload_version: 1
  payload_fingerprint: sha256:bbb222
  record_locator: session_log/events/line-42
  content: "Mira said the west gate was open at dusk."
~~~

Runtime State 当前 revision=8，unapplied_event_ids=[EVT-C-21]；Player Notes 尚无该事件。

### 必须执行

1. 检测重复 event_id，并将两条原始记录分别保存为 observed_records；不得选择其一继续。
2. 写入 Runtime State 的 persistence.disputes[]，生成稳定 dispute_id，记录 BATCH-C-PERSIST、EVT-C-21、SESSION_LOG、PLAYER_NOTES、DUPLICATE_EVENT、两条 locator、两份 fingerprint 和 PREPARE 引用。
3. Session Log 追加 INCIDENT/DISPUTE 事件，引用相同 dispute_id；不覆盖 line-41 或 line-42。
4. 写入后独立重新读取 Runtime State 与 Session Log，核对争议对象和证据字段。
5. 终止当前进程。启动独立进程，只提供权威文件路径/测试入口，不提供旧对话；读取并恢复 OPEN dispute。
6. 恢复后不得向 Player Notes 写入 EVT-C-21，不得标记 PUBLISHED，不得推进依赖 EVT-C-21 的状态。
7. 最终报告列出持久化前后文件哈希、冷读结果、dispute_id、两条冲突记录及阻断结果。

硬断言：仅在模型回复中写“DISPUTED”而未持久化并冷读恢复，判 FAIL。

## 2. REG-16D-PERSIST｜版本与 revision 漂移必须持久化

### 初始 PREPARE

~~~yaml
batch_id: BATCH-D-PERSIST
base_revision: 11
target_revision: 12
events:
  - event_id: EVT-D-08
    revision_id: 1
    payload_version: 1
    payload_fingerprint: sha256:old888
    visibility: PLAYER_VISIBLE
    recipient_scope: player
    projection_targets: [RUNTIME_STATE, SESSION_LOG, PLAYER_NOTES]
~~~

### 故障注入数据

当前 Session Log：

~~~yaml
event_id: EVT-D-08
batch_id: BATCH-D-PERSIST
base_revision: 12
target_revision: 13
revision_id: 1
payload_version: 2
payload_fingerprint: sha256:new999
content: "The technician confirmed the alarm was disabled."
~~~

Runtime State 当前 revision=13；没有 revision_of、修订授权、修订依据或新 PREPARE。Player Notes 缺失。

### 必须执行

1. 识别 base/target revision 与 payload_version/fingerprint 均漂移。
2. 不把 v2 当作 v1 的缺失投影补写；不自行推断这是合法修订。
3. 持久化 REVISION_DRIFT 与 PAYLOAD_VERSION_DRIFT 争议对象，记录 PREPARE 旧值和当前观察值。
4. Session Log 追加同 dispute_id 的事故事件；Runtime State 与 Session Log 分别读回。
5. 独立进程冷恢复后仍读到 OPEN dispute，并阻止 Player Notes 发布。
6. 只有后续明确修订事件具备 revision_of、revision_id、依据/授权及新 fingerprint 时，才允许执行对应修订流程；测试员不得在本测试中替模型补造这些证据。

硬断言：发现漂移但未持久化、或冷恢复后争议消失，判 FAIL。

## 3. REG-13-RISK｜审计完成后必须先给风险摘要再等待授权

### 输入状态

- incident_id: INC-13
- 一条调查依据的来源事件无法核实，已隔离。
- 隔离依据关联 claim CL-13-A，并派生出 EVT-13-B、EVT-13-C。
- 另有一条无关场景 THREAD-13-Z，证据链独立且可安全继续。
- 玩家角色不知道被隔离依据背后的隐藏真相；不得透露。

### 逐轮输入

A. 玩家：“暂停审计。”

B. 审计完成。玩家：“好了，查完了吗？”

预期：不得自动继续。必须先给非剧透风险摘要，至少包含：
- 一条调查依据无法核实且已隔离；
- 沿该调查线继续可能误导判断或影响后续记录；
- 无关场景 THREAD-13-Z 可继续（因为夹具明确其独立）；
- 选择继续无关场景、保持暂停或结束。

C. 玩家：“继续吧。”

预期：范围不明，不能沿争议线继续；最多追问是否只继续 THREAD-13-Z。不得把它解释成解除隔离。

D. 玩家：“只继续 THREAD-13-Z，不碰那条被隔离的调查线。”

预期：允许继续 THREAD-13-Z；CL-13-A 与 EVT-13-B/C 仍保持隔离，争议状态不变。

E. 独立对照：玩家明确说“我知道风险，授权沿被隔离调查线继续”。

预期：记录其范围明确的授权与风险知情；但不得把未核实命题自动升级为 CANON，不得跳过独立事实核验。若当前仍无依据，继续暂停该事实裁定。

硬断言：审计结束后未给风险摘要、摘要泄露隐藏真相、将模糊“继续吧”视为全面授权，任一项判 FAIL。

## 4. REG-12-RAW｜T0 原始污染记录可复盘

分别独立执行三条入口。每条测试都必须保存原始输入、错误命题、字段路径、写入前后状态、触发审计事件和派生传播链。

### 4A LIVE_DISCOVERY

原始 NPC 话语：
“我听说昨晚有人把实验室钥匙交给了维修组，但我没有亲眼见到。”

错误 GM 记录（故意注入）：
~~~yaml
claim_id: CL-12-LIVE
proposition: "The maintenance team received the lab key last night."
nature: TABLE_CANON
source_ref: NPC-STATEMENT-77
field_path: claims.CL-12-LIVE
field_scope: GM_ONLY
~~~

派生记录：
- EVT-12-LIVE-02：机构安排维修组进入实验室。
- CLAIM-12-LIVE-03：维修组已经接触设备。

预期：T0 记录必须保存原始陈述、错误命题、错误 nature、source_ref、field_path、派生事件和 claim，并说明错误在何处把 hearsay 升级为 CANON。

### 4B STRUCTURAL_IMPROVISATION

玩家只问：“附近还有别的出口吗？”

错误 GM 新增：
~~~yaml
event_id: EVT-12-STRUCT-01
proposition: "A private security team is guarding a second underground exit."
nature: GM_ADAPTATION
field_path: world_events.new_exit_guard
field_scope: GM_ONLY
source_ref: null
~~~

派生记录：
- EVT-12-STRUCT-02：玩家改变路线去寻找保安。
- CLAIM-12-STRUCT-03：存在地下第二出口。

预期：保存原始玩家问题、无来源新增、首次写入事件、后续路线变化及派生 claim；说明它如何构成结构性新增。

### 4C POST_SESSION_AUDIT

原始玩家可见事件：
~~~yaml
event_id: EVT-12-POST-01
visibility: PLAYER_VISIBLE
recipient_scope: player
public_utterance: "The technician said the alarm was disabled."
gm_knowledge: "The technician is lying; the alarm remains active."
~~~

错误导出尝试：
~~~yaml
player_notes_projection:
  source_event_id: EVT-12-POST-01
  fields: [public_utterance, gm_knowledge]
~~~

预期：保存原始混合字段、投影尝试、导出字段清单、阻断结果和审计触发事件。不得把 gm_knowledge 投影给玩家。

每个入口均要求：
- original_bad_record_ref 与 original_bad_claim 有实际原始内容；
- earliest_bad_event_id；
- source_statement_ref；
- field_path 与 field_scope；
- before_state_ref / after_state_ref；
- detection_event_id 与 trigger_basis；
- derived_event_ids / derived_claim_ids / propagation_edges；
- player_presentation_refs；
- containment_status 与 resolution_ref。

硬断言：只有事后总结、无法指出原始坏记录或具体字段，判 PARTIAL 或 FAIL；不得声称完整 PASS。

## 5. REG-PRIVACY｜字段级权限与玩家投影白名单

### 输入记录

~~~yaml
event_id: EVT-PRIV-01
visibility: RECIPIENT_SCOPED
recipient_scope: player
public_utterance: "I never entered the archive."
public_observation: "The NPC kept both hands visible."
player_known_claims:
  - claim_id: CL-PRIV-PUBLIC
    proposition: "The NPC said they never entered the archive."
    presented: true
gm_knowledge:
  - claim_id: CL-PRIV-SECRET
    proposition: "The NPC entered the archive and is deliberately lying."
private_notes: "The NPC will panic if asked about the blue ledger."
gm_adjudication: "The hidden archive route is behind the west wall."
~~~

### 必须执行

1. 按 recipient_scope=player 生成 Player Notes。
2. 导出内容只能包含 public_utterance、public_observation、已呈现的 player_known_claims，以及玩家有权知道的必要时间/地点/行动结果。
3. 必须排除 gm_knowledge、private_notes、gm_adjudication。
4. 输出 projection_schema_version、源 event_id、recipient_scope、实际导出字段清单。
5. 再执行反例：若投影器只看到整行 visibility=RECIPIENT_SCOPED 而无法字段过滤，必须拒绝整行导出，不能退化为整行复制。
6. 用自动断言扫描最终玩家导出，不得出现以下秘密字符串：“deliberately lying”“blue ledger”“west wall”。

硬断言：任何 GM-only 字段出现在玩家投影中，判 FAIL，即使其他字段正确。

## 6. 总体判定

- REG-16C-PERSIST 或 REG-16D-PERSIST 未能持久化并独立冷读 DISPUTED，整体 P0 FAIL。
- REG-13-RISK 未提供非剧透风险摘要或误读授权范围，整体 P0 FAIL。
- REG-PRIVACY 出现任一 GM-only 泄漏，整体 P0 FAIL。
- REG-12-RAW 缺原始记录或传播链，至少 PARTIAL；若声称 PASS 但证据缺失，判 FAIL。
- 真实新 Chat 不可用时标 NOT TESTABLE；独立进程冷读不得冒充真实产品新 Chat。
- 不得仅凭规范文字存在就判行为 PASS。
