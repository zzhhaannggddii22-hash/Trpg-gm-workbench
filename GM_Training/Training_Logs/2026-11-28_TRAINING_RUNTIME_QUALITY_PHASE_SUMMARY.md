# 2026-11-28｜Training & Runtime Quality 阶段总结

## 本轮结论

本轮训练与测试收尾。现有合成样本显示 NPC 人格差异、单会话自主性与信息边界表现有所改善；这些结果用于指导真实跑团观察，不代表独立盲测或长期能力验证。

## 已完成

- **NPC Personality C2/C3 合成自测**：测试个人偏好/效率取舍，以及共同经历/关系独特性。三名样本均通过本夹具的局部自评检查。
- **L3 Single-session autonomy harness**：交流、玩家离场、方案改变三个固定情境的合成执行样本通过硬门槛。
- **Fresh cohort anonymous NPC discrimination self-audit**：使用全新临时 NPC、统一场景与输入进行模拟辨识。样本映射匹配 3/3；仅记作 LOCAL_SAMPLE_PASS，未建立独立盲评证据。

## 当前观察所得

NPC 人格差异更有效的呈现途径是：
- 注意力落点不同；
- 行为与选择不同；
- 判断与决策方式不同；
- 主动程度不同；
- 边界、偏好和条件不同。

应避免仅靠口癖、夸张动作或刻意“特立独行”制造差异。表现要融入自然场景，保持细腻和可信。

## 证据边界与未关闭事项

- 这些测试以同一执行者生成并自审为主，不能称为独立盲测。
- 尚未建立独立评审者证据、长期多会话证据或充分真实玩家交互验证。
- G-03、G-04、G-17、G-19 仍保持 OPEN。
- 不晋级 T2/T3/T4，不据此修改能力等级。
- 本轮没有发现足以要求进一步修改 Character Simulation Skill 的新缺陷。

## 后续运行原则

1. 停止扩张合成测试数量，转向真实跑团观察。
2. QA 维持离线执行与会话后审计；不在日常跑团过程中增加检查步骤或耗时。
3. 观察真实 NPC 是否自然体现偏好、行动、判断、主动性与边界，以及时间/事务连续性和信息隔离。
4. 只有出现具体、可复现的缺陷证据时，才做轻量修复与复测。
5. 继续遵守个人维护、轻量直接、只用 main 的项目工作方式。

## 相关报告

- [C2/C3 NPC Personality Synthetic Selfplay](../Training_Logs/2026-11-28_L3_NPC_PERSONALITY_C2_C3_SYNTHETIC_SELFPLAY.md)
- [L3 NPC Single-session Harness Execution](../Testing/Reports/L3_NPC_SINGLE_SESSION_HARNESS_EXECUTION_2026-11-28.md)
- [Fresh Cohort Anonymous NPC Discrimination Self-audit](../Testing/Reports/2026-11-28_FRESH_COHORT_ANONYMOUS_NPC_DISCRIMINATION_SELF_AUDIT.md)

**状态：本轮收尾；下一阶段以真实跑团观察为主。**
