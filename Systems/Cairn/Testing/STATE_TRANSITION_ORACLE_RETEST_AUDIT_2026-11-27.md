# Cairn 2e｜State Transition Regression v1 第二轮独立 Oracle 审计

日期：2026-11-27  
被审计执行报告：用户提交的第二轮独立盲测报告  
固定测试版本：`43ecb7211bbc19bad92f109ab92eee3d5e146e5d`  
Repository：`zzhhaannggddii22-hash/Trpg-gm-workbench`  
Branch：`feat/cairn-second-system-integration`  
Fixture：`STATE_TRANSITION_REGRESSION_v1`  
范围：CRT-66–CRT-87  
模式：`TEST_ONLY_NON_CANON`

## 1. 审计依据与证据边界

本次独立读取并对照固定 Commit 中的：

- `Systems/Cairn/Testing/STATE_TRANSITION_REGRESSION_v1/ORACLE.md`
- `Systems/Cairn/Testing/STATE_TRANSITION_REGRESSION_v1/CASES.md`
- `Systems/Cairn/Rule_Reference/CORE_RULES_RUNTIME.md`
- `Systems/Cairn/RUNTIME_PROTOCOL.md`

第二轮执行报告声明其读取了 START、CASES、CORE_RULES_RUNTIME、RUNTIME_PROTOCOL，以及 CRT-86 指定的 NPC 再遭遇报告；并声明没有读取 Oracle、回归矩阵或此前审计资料。该隔离声明与报告结构相符，但仅凭交付报告无法独立证明目标会话的实际文件访问历史。

本审计评估的是报告中呈现的规则执行轨迹与 Oracle 一致性，不是实际运行时程序、数据库或宿主持久化层测试。

## 2. Oracle 对照结论

### 行为断言

**22/22 个案例的核心行为断言均与 Oracle 相符；未发现需要判为行为 FAIL 的案例。**

| 案例 | Oracle 审计 | 说明 |
|---|---|---|
| CRT-66–72 | PASS | 伤害边界、Panic、Inventory Overload、Broken Limb 延迟成长符合预期 |
| CRT-73 | PASS | Walloped 的 1d6=4 直接加到最大 HP：8→12；未套用其他 Scar 的“高于当前最大值才提升”条件 |
| CRT-74 | PASS | 普通 WIL Save 不消费 Doomed；后续 Critical Damage Save 成功后才执行 3d6 成长并消费触发器 |
| CRT-75–83 | PASS | 旅行中途状态、Handoff、Fatigue、Ration、Dungeon/Wilderness Event、Reaction 均符合各自边界 |
| CRT-84 | PASS | Blast 三个目标分别结算；A、B、C 的伤害分支与 Walloped 延迟效果符合 Oracle |
| CRT-85–86 | PASS | 已提交事务不重复应用；Mara Bell 的位置、资源、目标和知识边界保持连续 |
| CRT-87 | PASS | Enhanced/Impaired 冲突有单一且有情境依据的裁定；独立 Blast 两目标结算正确 |

### CRT-87：执行报告的 BLOCKED 判定不成立

执行报告将 CRT-87 标为 BLOCKED，理由是普通攻击没有提供实际伤害骰值。

但对照 CASES 与 ORACLE，本案例普通攻击部分要求的是：

1. 根据给定虚构情境选择一个适用修正；
2. 解释选择；
3. 不叠加、不抵消，也不因缺乏通用优先级而拒绝裁定。

案例没有要求完成普通攻击的伤害计算，也没有提供武器伤害骰输入。执行者已选择 Enhanced（d12），并解释了昏迷目标、近距离、无掩体与空闲手仍可完成攻击的情境依据。该部分已满足测试断言。

独立 Blast 部分的两个目标均有固定伤害骰及 STR Save 输入，报告已完整结算。

因此，**CRT-87 应由 BLOCKED 更正为 PASS**。缺少普通攻击伤害骰不构成本案例阻塞。

## 3. 来源分类元数据需要修正

以下是报告标注问题，不改变相应案例的核心状态转换结果：

### CRT-70｜Panic 克服后的 HP 持续为 0

报告将整个结果标为 `SOURCE`。应拆分来源：

- WIL Save 成功、移除 Panicked：`SOURCE`。
- 克服 Panic 后 HP 不自动回填、继续保持 0：`GM_INFERENCE`。

CORE_RULES_RUNTIME.md 的 CR-PANIC 已明确说明官方条文没有规定克服 Panic 时恢复 HP；Workbench 不自动回填属于 GM_INFERENCE。

### CRT-71｜Inventory Overload 解除后的 HP

报告将整个结果标为 `TABLE_ADAPTATION`。应将“腾出库存格后 HP 不自动回填”标为 `GM_INFERENCE`，而不是未经批准的桌面适配。

库存满格导致 HP=0 的规则本身属于 `SOURCE`；解除超载后不自动恢复 HP 是 Workbench 状态解释。

### CRT-77｜Deprived 的 25h / 49h Fatigue tick

报告将精确时间边界标为 `SOURCE`。应标为 `GM_INFERENCE`：

- Deprived 超过一天后增加 Fatigue 的规则关系：`SOURCE`。
- 具体采用 25h=1 tick、49h=2 ticks 的 elapsed-full-day 边界：`GM_INFERENCE`，与 Oracle 的分类说明一致。

以上三项建议在报告中按字段拆分来源，不要给混合了规则事实与实现推论的整个事务只贴一个来源标签。

## 4. 延迟效果记录完整性

行为轨迹显示了 pending → ready/恢复 → consumed 的主要处理，但报告没有在所有延迟效果案例中完整展示 RUNTIME_PROTOCOL.md §5-A.3 所要求的最小字段。

例如 CRT-72、CRT-73、CRT-74、CRT-84 的效果记录并非每项都明确展示：

- source_event_id
- source_rule_id
- actor_id
- effect
- due_when
- created_at / consumed_at
- resolution_event_id
- source_class

这属于**报告可审计性/序列化证据不足**，目前不足以据此判定状态转换错误。后续若要验证完整 Runtime State schema，应要求输出这些字段；不需要因此增加新的规则案例。

CRT-84 Target C 的即时结果与 pending 状态正确；未提前掷 Walloped 延迟成长骰。报告同时将 `Walloped` 和 `Deprived` 都列入 ongoing_conditions。现有协议明确要求保存 Deprived 条件与 pending recovery effect；Walloped 作为 Scar 标签是否还应作为独立 ongoing condition，建议后续统一状态表达，避免重复语义。

## 5. 证据边界

第二轮报告自身正确指出：

- CRT-85 验证的是逻辑层对 committed event 的理解，不证明真实存储层幂等。
- 本轮没有执行实际 Runtime 代码或数据库写入。
- 没有验证 prepared → committed 中断、部分提交恢复、并发事务原子性。
- CRT-76 验证已提交 Travel 检定的恢复，不代表完整找回路线流程已验证。
- CRT-84 验证 Walloped 即时触发与 pending 创建，不代表延迟恢复成长已执行。
- CRT-86 是合成 NPC 再遭遇，不是实际玩家团或多 NPC 实战验证。

因此本轮只能作为**独立自然语言 GM 行为轨迹与规则调用一致性证据**，不能替代宿主级持久化验证或真实团验收。

## 6. 最终审计结论

- Oracle 行为断言：**22/22 符合**
- 行为 FAIL：**0**
- 合理 BLOCKED：**0**
- 执行报告中需更正的 BLOCKED：**CRT-87**
- 来源分类元数据需修正：**CRT-70、CRT-71、CRT-77**
- 延迟效果完整字段：**报告展示不完整，尚不能据此确认全 schema 合规**
- 实际 Runtime / 存储层：**未验证**

**结论：第二轮盲测的核心行为结果通过 Oracle 对照。** 与第一轮相比，CRT-73、CRT-74、CRT-84、CRT-87 的前轮问题均已解决；本轮没有发现新的规则执行错误。当前最小后续动作是更正执行报告的 CRT-87 结果及三个来源标签，并在后续有针对性的持久化测试中验证实际宿主层。无需扩大案例数量。

本审计不改变 Runtime、Ruleset、Campaign 或 System Registry 状态；Cairn 继续保持 candidate，Triangle Agency 继续保持唯一 active。
