# T0 自然语言盲测 v1｜操作者隔离与证据协议

> 操作者材料。不得上传目标 Chat。仓库为公开仓库，因此“GM-only”表示用途隔离，不代表 GitHub 访问权限隔离。

## 1. 测试边界
- 测试对象：目标 Chat 中运行的 GM；测试主题：T0 自然语言行动路由。
- 规范版本：目标试次开始时记录的 `main` commit；必须同时记录 SKILL 与 Runtime 文件的实际读取版本。
- 测试规模：8 个独立空白 Chat、8 个最小附件、每个 4 轮、共 32 轮。
- 不读取、不修改正式 Campaign、人物卡、模组、CANON、Session Log 或真实玩家资料。
- 不以本操作者 Chat 的推演代替目标 Chat 行为证据。

## 2. 每个试次的隔离流程
1. 操作者新建空白 Chat，并保存可核验的空白状态证据。若无法取得，记录 UNKNOWN，不以口头声称替代。
2. 只给目标 Chat 通用执行提示 `GM_T0_BLIND_EXECUTION_PROMPT_v1.md`。
3. 目标 Chat 读取 `GM_Training/SKILL.md` 和 `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md`。保存实际读取的工具轨迹/引用；若无 GitHub 读取能力，操作者可提供这两份通用规范的副本，并记录原始字节 SHA-256 与上传时间。
4. 仅上传当前试次对应的一个 `T0_BLIND_PACKET_A0N.md`。上传前对原始字节计算 SHA-256，记录文件名、大小、上传时间。
5. 逐轮发送操作者夹具中的四条玩家原话。每次只发送当前轮；不得在开始时粘贴完整四轮输入。
6. 保存完整原始输入、完整原始输出、可见工具轨迹、时间戳和异常。不要让目标 Chat 读取操作者材料。
7. 完成该试次后关闭，不在同一 Chat 继续下一个试次。

## 3. 污染判定
以下情况标记 CONTAMINATED，该试次保留但不计有效盲测通过：
- 目标 Chat 不是空白新 Chat，或存在无法排除的历史上下文；
- 目标 Chat 提前获得本试次后续轮次、其他试次附件或操作者材料；
- 目标 Chat 打开了夹具、答案、评分、RUN_MANIFEST 或本协议；
- 操作者把完整多轮输入一次性粘贴给目标 Chat；
- 目标端实际读取的规范版本无法确认，且该缺口影响行为判断。

## 4. 证据等级
每个试次分别记录：
- E0：仅有操作者摘要/模型自述；不能证明实际执行。
- E1：保存完整逐轮输入与输出，但缺少空白 Chat、附件时序或规范读取证据。
- E2：空白 Chat、附件哈希/上传时序、规范读取版本、逐轮输入输出均可核验。
- E3：E2 + 完整可见工具轨迹及必要产物/读回证据。

本套行动路由测试主要评估自然语言裁定，不要求目标 Chat 写入正式状态文件；因此未触发文件写入的试次不因缺少写入证据而扣分。若目标 Chat 声称保存/更新，则必须额外取得真实写入与独立读回证据，否则该声称单独判 FAIL。

## 5. 评分与复核
- 按 `T0_NATURAL_LANGUAGE_BLIND_SUITE_v1_OPERATOR.md` 的 32 轮量表评分。
- 先评分每轮行为，再评证据等级；不能用行为分数补偿证据缺口。
- 对每项错误记录原始轮次、模型原话、错误类型、对应规范条款、影响范围和修订建议。
- 任何硬失败均保留；总分不抵消硬失败。
- 如由同一助手在已看过答案的上下文中评分，标记 scorer_blinded=false。可进行一致性审查，但不得声称独立盲评。

## 6. RUN_MANIFEST 模板
为每个试次复制以下记录；八个试次使用不同 run_id。

```yaml
run_id: "T0-BLIND-v1-A0N"
case_id: "A0N"
status: "NOT_STARTED"
target_chat_created_at: "UNKNOWN"
blank_chat_evidence_ref: "UNKNOWN"
product_model_thinking: "UNKNOWN"
normative_main_commit: "UNKNOWN"
skill_blob_sha: "UNKNOWN"
runtime_blob_sha: "UNKNOWN"
execution_prompt_sha256: "UNKNOWN"
packet:
  filename: "T0_BLIND_PACKET_A0N.md"
  sha256_original_bytes: "UNKNOWN"
  size_bytes: "UNKNOWN"
  uploaded_at: "UNKNOWN"
turns:
  - turn: 1
    input_verbatim: "NOT_SENT"
    sent_at: "UNKNOWN"
    output_verbatim_ref: "UNKNOWN"
    visible_tool_trace_ref: "UNKNOWN"
  - turn: 2
    input_verbatim: "NOT_SENT"
    sent_at: "UNKNOWN"
    output_verbatim_ref: "UNKNOWN"
    visible_tool_trace_ref: "UNKNOWN"
  - turn: 3
    input_verbatim: "NOT_SENT"
    sent_at: "UNKNOWN"
    output_verbatim_ref: "UNKNOWN"
    visible_tool_trace_ref: "UNKNOWN"
  - turn: 4
    input_verbatim: "NOT_SENT"
    sent_at: "UNKNOWN"
    output_verbatim_ref: "UNKNOWN"
    visible_tool_trace_ref: "UNKNOWN"
contamination:
  status: "UNKNOWN"
  future_input_exposed_early: false
  operator_material_exposed: false
  notes: []
scoring:
  behavior_score: "NOT_SCORED"
  hard_fail: "UNKNOWN"
  evidence_level: "E0"
  scorer_blinded: false
  notes: []
```

## 7. 当前执行者能力边界
本轮助手可准备夹具、检查规范一致性、创建 GitHub 分支/PR 并核验归档；无法从当前 Chat 工具直接创建另一个独立空白 Chat 并在其中逐轮交互。当前 Chat 已接触操作者预期，不能作为目标 Chat。若没有真实空白目标 Chat 证据，必须报告 EXECUTION_NOT_STARTED / ADMISSION_NOT_MET，不得以模拟、角色扮演或当前上下文推演冒充盲测。