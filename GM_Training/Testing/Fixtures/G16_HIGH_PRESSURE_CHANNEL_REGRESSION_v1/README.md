# G-16 High-Pressure Information Channel Regression v1

> Test ID: G16-CHANNEL-HP-01  
> Type: targeted high-pressure regression / SINGLE_SESSION_SELF_TEST  
> Status: TEST_ONLY_NON_CANON

验证 GM 在多重现场负荷下能否继续区分 NPC 私人记忆、实际对白和玩家可观察行为。采用一个连续场景、三个按时间推进的玩家行动，不使用同回复内的伪独立分支。

## Files

- START.md：目标 Chat 唯一执行输入。
- ORACLE.md：执行后审查标准；执行结束前不得读取。

## Execution

1. 按专项模式 B 建立真正空白的目标 Chat，并固定被测 Workbench commit。
2. 目标 Chat 按 START.md 读取必要 Skill 与 Runtime 资料。
3. 目标 Chat 只接收 START.md 和必要权威资料，不提供 ORACLE。
4. 目标 Chat 按三个阶段顺序自动执行；这是同一连续场景，不重置状态。
5. 保存目标 Chat 的完整原始输出、实际读取来源和版本信息。
6. 将结果粘贴到独立审核会话；审核者再读取 ORACLE 并给出结论。目标 Chat 不自评，不把目标输出直接称为独立审核 PASS。

## Evidence boundary

本夹具测试单会话内高压情境下的信息渠道控制，不证明跨 Chat 隔离或真实 Session 稳定性。PASS 仅代表本样本未观察到泄露，不自动关闭 G-16。