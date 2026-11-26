# P1-0C 修复方案独立审查提示词

你是独立技术审查者。请只审查，不修改仓库、不代替目标 Chat 执行测试、不读取或接触任何正式 Campaign/真实玩家资料。

## 审查目标
判断 P1-0 最终报告所暴露的四项历史硬失败及独立审查 C1-C6 是否被当前修订完整、最小且一致地覆盖；重点找遗漏、冲突、重复、无法执行的要求和过度承诺。

## 必须读取
- GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md（重点 §12.3、§13、§14.1–14.18）
- GM_Training/GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md（重点 §6、§11、§12，注意仅保留一套授权/路由职责）
- GM_Training/RUNTIME_STATE_TEMPLATE.md
- GM_Training/03_SESSION_LOG_TEMPLATE.md
- GM_Training/SKILL.md
- GM_Training/GM_RUNTIME_P1_PERFORMANCE_PLAN.md
- GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v1.md
- GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/GM_RUNTIME_P1_0C_EXECUTION_PROMPT.md
- GM_Training/Acceptance_Test_Fixtures/Execution_Prompts/GM_RUNTIME_P1_0C_OPERATOR_PROTOCOL.md（GM-only，仅审查，不上传目标 Chat）
- GM_Training/Acceptance_Test_Fixtures/GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v2.md（GM-only，仅审查，不上传目标 Chat）
- GM_Training/Acceptance_Reports/GM_RUNTIME_P1_0_REMEDIATION_AND_P1_0C_HANDOFF.md
- GM_Training/README.md
- 原始基线报告：GM_RUNTIME_P1_0_BASELINE_REPORT_2026-11-24.md（由操作者另行提供）

## 审查问题
1. C1 / REG-14：last_answered_event_id、实际 GM 回复、presentation_status 与 Player Notes 的关系是否足以阻止近义重播？是否存在玩家明确要求回顾时的正确例外？
2. C2 / REG-17：Runtime checkpoint 与 Session Log 的应用标记是否构成真正可交叉核验的证据？字段缺失、旧存档、部分合并、后续事件、事件排序和 revision 变化是否处理一致？模板是否有歧义或重复字段？
3. C3 / REG-11：T0 原则、风险摘要、授权规则与 Runtime 行动路由是否只有一套明确操作流程？每轮是否覆盖 GM 建议、NPC 接触、玩家代述、地点移动和派生事件？安全互动是否可能被错误放宽？
4. C4 / 隐私导出：Player Artifact 与 GM Audit Artifact 的访问边界是否真实可执行？扫描范围是否准确区分可读与不可读部分？NOT_VERIFIABLE 是否会被错误当作通过？纯文本/复杂文档的判据是否明确？
5. C5 / E13：现有正向路由是否被保留？第四轮 Sol 的未来意向是否被误当作实际联系或调查推进？PARTIAL 证据等级是否仍被保留？
6. C6 与跨文件一致性：Skill、Runtime、T0、模板、P1 计划、夹具、执行提示词和操作者协议之间是否存在引用断裂、字段不一致、相互矛盾或重复维护？
7. 修订是否增加了不必要的每轮审计成本，是否会损害普通绿色互动速度？能否只在必要触发点执行？
8. 是否有新增的安全性或连续性回归风险？哪些是规范问题，哪些必须靠真实目标 Chat 行为才能验证？

## 输出格式
请给出：
- 总体结论：APPROVE / APPROVE WITH CONDITIONS / REJECT。
- 文件逐项审查表：通过、问题、证据位置。
- P0/P1 级阻断问题：具体条款、失败路径、最小修复建议。
- 非阻断建议：维护性、性能和表达方面的改进。
- 必须由目标 Chat 实测的项目，明确区分不可由静态审查证明的行为。
- 任何你无法读取的文件、工具或证据缺口。

## 审查纪律
- 不要因为文档写了要求就认为模型会执行。
- 不要将用户回传文字当作独立工具轨迹或原始文件字节。
- 不要将规范层面的修复宣称为 P1-0 通过。
- 不得改写旧失败报告或删除旧失败样本。
- 如果发现证据不足，明确标记 UNKNOWN，不要猜测。

## 本轮新增审查要求（C1-C6）
核对已呈现内容回滚冲突、不可变字段级 manifest、领域争议与持久化争议分离、T0 授权/行动语义、发布前隔离门禁、接收者/片段级呈现，以及目标执行提示词和操作者材料的隔离。每项给出文件路径与准确条款；不可观察的真实行为标 UNKNOWN。
