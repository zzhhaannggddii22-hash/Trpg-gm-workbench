# GM Runtime｜Optimization Reports

本目录保存 GM 运行性能与工程优化计划、方案和实施记录。质量优先于速度。性能优化默认采用低风险、近乎无损的方式；不要求为每项优化执行复杂回归测试。必要的局部核查按风险决定；未执行的验证必须如实记录，不得宣称质量已通过。涉及显著质量、可靠性、功能或权限取舍时暂停并交由用户决定。

- [P1 性能与执行效率验证计划](./GM_RUNTIME_P1_PERFORMANCE_PLAN.md)：目标环境基线、成本拆分与阶段门槛。
- [P1-1 性能审计与优化记录 · 2026-11-26](./GM_RUNTIME_P1_1_PERFORMANCE_AUDIT_2026-11-26.md)：同次 Preflight 复用、本机读取对照和验证边界。
- [Context Assembly & Trace 设计记录](./CONTEXT_ASSEMBLY_AND_TRACE_DESIGN.md)：基于 P1-1 优化后 Preflight 结构的上下文装配、可观测性与实施决策。
- [P0/P1 场景上下文与调查记录修复实施记录](./P0_P1_SCENE_CONTEXT_EVIDENCE_REMEDIATION_2026-11-25.md)：本轮架构盘点、最小修复范围、已写入文件与待验证项。
- [GM 系统优化方案](./GM_SYSTEM_OPTIMIZATION_PLAN_2026-11-24.md)
- [GM 系统实施记录](./GM_SYSTEM_IMPLEMENTATION_RECORD_2026-11-24.md)

验收结论请查看 `Acceptance_Reports/`。计划和方案不是测试通过证明。
