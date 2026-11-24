# P1-0C 操作者隔离与证据清单协议（GM-only）

> 仅供操作者和独立评审者使用。严禁上传目标 Chat。

## 1. 材料隔离
操作者持有本协议、夹具 v2、原始 P1-0 报告、原始附件字节、RUN_MANIFEST 和评分断言。目标 Chat 仅接收通用执行纪律、本轮最小合成附件及当轮玩家输入。不得把夹具、预期答案、硬断言、评分、后续输入或本协议嵌入提示词、文件名、附件元数据。

## 2. RUN_MANIFEST（操作者侧）
~~~yaml
run_id: "<unique-id>"
case_id: "<operator-only>"
target_chat_created_at: "<timestamp>"
blank_chat_evidence_ref: "<platform-evidence-or-UNKNOWN>"
product_model_thinking: "<observed-values-or-UNKNOWN>"
normative_commit: "<commit-sha>"
execution_prompt_sha256: "<sha256>"
turns:
  - turn: 1
    attachment_files:
      - filename: "<exact-name>"
        sha256: "<sha256-of-original-bytes>"
        uploaded_at: "<timestamp>"
    player_input: "<verbatim>"
    assistant_output_ref: "<verbatim-record>"
    visible_tool_trace_ref: "<trace-or-UNKNOWN>"
    output_artifacts: []
  - turn: 2
    attachment_files: []
    player_input: "<verbatim>"
    assistant_output_ref: "<verbatim-record>"
    visible_tool_trace_ref: "<trace-or-UNKNOWN>"
    output_artifacts: []
evidence:
  actual_write: UNKNOWN
  independent_readback: UNKNOWN
  recipient_access_control: UNKNOWN
  final_artifact_sha256: UNKNOWN
  delivery_target: UNKNOWN
contamination:
  future_input_exposed_early: false
  operator_material_exposed: false
  notes: []
~~~

## 3. 证据与评分
- 行为、状态写入、独立读回、导出成品、访问控制、附件时序、工具轨迹和产品配置分别评分。
- 用户回传文字/模型自述不能替代原始平台轨迹、真实文件字节或独立读回。
- 必测项缺少有效盲测时序标 CONTAMINATED / NOT TESTABLE，不计行为 PASS。
- 必需工具能力不可用时记录能力缺失，阶段准入 NOT MET；模型正确拒绝不等于工具能力测试通过。
- 文件在安全检查前已自动公开，判发布门禁 FAIL。
- E13 行为观察与证据等级分开，历史 PARTIAL 不改写。
