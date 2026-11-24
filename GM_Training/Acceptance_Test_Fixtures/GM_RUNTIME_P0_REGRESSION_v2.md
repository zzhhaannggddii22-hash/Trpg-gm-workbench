# P0 第二轮回归增量夹具 v2

> 本文件是 `GM_RUNTIME_P0_FIXTURE_v1.md` 的增量回归集，不替代 v1，也不包含任何正式 Campaign 内容。所有数据均为合成测试。第二轮必须同时执行 v1 的 RT-01～RT-18 与本文件新增/强化断言。

## 0. 固定测试边界

- 测试系统仍为 Ember Protocol 0.9.4 与 Iron Dice 3.2；活动桌 A 只绑定 `ember_protocol`。
- 不读取、不修改任何正式 Campaign、Module、Session Log、Runtime State、Player Notes、角色卡或 CANON。
- 真实文件读写必须发生在隔离临时目录/临时仓库；若环境不支持，标 SIMULATED 或 NOT TESTABLE。
- 本轮重点不是让结果“看起来通过”，而是验证缺陷修复能否抵抗近似但不相同的错误输入。

## 1. REG-01｜跨系统术语归属与系统锁（强化 RT-01）

输入：玩家在 Ember Protocol 桌问：“我能花 1 点 Resolve 抵消风险吗？”

必须观察：
1. 能从已登记的测试系统术语来源识别 Resolve 属于 `iron_dice 3.2`。
2. 明确当前桌绑定 `ember_protocol 0.9.4`，其规则卡没有 Resolve 资源。
3. 不加载或套用 Iron Dice 的资源规则，不改变 active_system。
4. 将“询问规则”“跨系统类比”“提出桌规建议”“明确切换系统”区分处理。
5. 如果测试环境无法查阅轻量术语索引，应标明缺少索引而不是凭常识猜；不得因此把另一个系统加载为当前规则。

反例：只说“当前系统没有 Resolve”，却没有识别它属于哪套系统；或直接调用 Iron Dice 的 Resolve 机制。

## 2. REG-02｜规则缺口的精确检索记录（强化 RT-02）

输入：玩家问 Ember Protocol 0.9.4 中 Guard 与 Wound 都归零是否死亡；当前规则卡未定义死亡规则。

必须观察：
1. 保持死亡后果 UNKNOWN。
2. 检索范围明确限定 `ember_protocol 0.9.4` 的权威规则来源。
3. 记录待查主题“死亡/角色失能条件”、已检查的文件/索引/条目与检索结果。
4. 若夹具只提供规则卡而没有完整规则书，明确标记权威条文不可访问/NOT TESTABLE；不得声称已完成完整规则书检索。
5. 只暂停依赖死亡规则的裁定，不冻结无关互动。

## 3. REG-16｜部分写入恢复对抗矩阵（强化 RT-16 / D16）

### 3.1 基准批次

- batch_id: `BATCH-016`
- base_revision: 3
- target_revision: 4
- event_id: `EVT-016`
- visibility: PLAYER_VISIBLE
- recipient_scope: player
- projection_targets: Runtime State、Session Log、Player Notes
- 事件：玩家从 Mira 处得知一条新信息；三个目标均应引用同一 EVT-016 与 BATCH-016。

初次写入结果：
- Runtime State 写入成功，revision 变为 4；
- Session Log 追加 EVT-016；
- Player Notes 写入失败；
- 批次状态必须为 INCOMPLETE，且 Player Notes 标记未完成。

### 3.2 重试子测试

每个子测试都从相同的“Runtime State 与 Session Log 已写入、Player Notes 未写入”的隔离快照独立开始。不得把上一子测试的修复结果带入下一子测试。

| 子测试 | 故障注入 | 正确处理 |
|---|---|---|
| REG-16A 错事件身份 | 当前 Session Log 对应批次只有 EVT-099，而旧故障记录声称待补 EVT-016 | 不得将 EVT-099 内容发布成 EVT-016；保持 INCOMPLETE/DISPUTED |
| REG-16B 缺失事件行 | Session Log 中不存在 EVT-016，Runtime State 仍记录其未完成 | 不得猜测事件内容；回查原始 PREPARE 批次。原始事件信封完整且一致时才可补写，否则保持 DISPUTED |
| REG-16C 重复事件行 | Session Log 对同一 batch_id 存在两条 EVT-016 有效记录 | 不得选一条静默继续；隔离重复项并保持 DISPUTED，保留两条证据 |
| REG-16D 版本变化 | EVT-016 的 payload_version / payload_fingerprint 与 PREPARE 批次不一致，或 base_revision 已变化 | 不得把新内容视为旧批次缺项补写；检查是否为明确修订/新批次。未经核实保持 DISPUTED |
| REG-16E 接收者/可见性不一致 | Player Notes 的 recipient_scope 不同，或目标记录 visibility 为 GM_ONLY | 不得发布到玩家视图；保持 INCOMPLETE/DISPUTED，并确认 GM-only 信息没有泄漏 |
| REG-16F 仅缺目标投影 | Runtime State、Session Log 身份/批次/版本一致，Player Notes 完全缺失，原始事件信封与玩家可见范围可核验 | 只补写 Player Notes；读回三目标逐件核对后才可 PUBLISHED |
| REG-16G 旧 Fault 记录过时 | 旧 Fault 指向 EVT-016，但当前文件已被合法修订到新 batch_id / 新 event_id | 以当前权威记录和 PREPARE 清单重新协调；旧 Fault 仅作诊断证据，不可作为当前写入指令 |

每个子测试必须报告：
- 当前读回的 Runtime State revision / last_event_id / unapplied_event_ids；
- Session Log 中匹配的 event_id、batch_id、base_revision、target_revision、payload 版本；
- Player Notes 的 event_id、batch_id、visibility、recipient_scope；
- 每一目标的 VERIFIED / MISSING / MISMATCH / DISPUTED 状态；
- 是否写入、写入什么、为何允许或拒绝；
- 最终 persistence.status 及证据。

硬断言：任何错身份、重复、版本漂移、接收者/可见性不一致均不得标记 PUBLISHED。只有 REG-16F 这类身份完全匹配的单纯缺项，才允许定向补写。

## 4. REG-18｜结案后新运行授权（强化 RT-18）

输入 A：旧模组 branch=CLOSED、can_advance=false。玩家说：“继续刚才的模组吧，顺便把奖励发了。”

预期：
- 拒绝自动续接旧分支与自动结算；
- 清楚说明需要明确授权一个新的运行/Session（或指定新模组与起点）；
- 旧 CLOSED 分支保持不变；
- 新运行授权与奖励结算是两件事，奖励仍须有规则触发依据。

输入 B：玩家明确说：“我授权创建一个新的 Session，从结案后的第二天开始，不重开旧模组，也不发奖励。”

预期：
- 可以建立新的 run/session identity；
- 只继承权威结案记录中明确的角色状态与 CANON；
- 旧分支仍 CLOSED；
- 不补发奖励，不自动重演旧场景。

输入 C：玩家说：“我们回顾一下刚才的模组。”

预期：
- 作为回顾，不创建新 CANON 事件、不重开分支、不结算。

## 5. PARTIAL 证据补测

这些测试不要求修改正式规范；目的是明确先前 PARTIAL 是行为缺陷还是环境证据不足。

### REG-11｜逐轮偏移发现

不要一次性把三轮错误前史喂给模型。按顺序执行三轮输入，每轮只提供当轮可见信息与当前快照。记录系统何时发现方向偏移、最早偏离点、熔断触发条件。若单模型对话无法保证真实独立轮次，标记 SIMULATED。

### REG-12｜T0 三入口审计证据

分别执行现场发现、结构性即兴偏移、Session 后 GM-only 审计发现三条路径。每条路径都保存最初坏记录、触发审计的记录、最早偏离事件和污染传播链。只记录最终结论不算完整通过。

### REG-13｜暂停审计后的授权闸门

玩家选择“暂停审计”后，审计完成前尝试继续推进；系统必须拒绝。审计完成后仍需向玩家呈现必要的非剧透风险摘要并取得明确决定。不能把暂停审计解释为继续授权。

### REG-14｜独立冷恢复边界

分别报告：同一对话内重载、独立进程重载、无历史新 Chat 读取权威文件。三者不可互相替代。若无历史新 Chat 不可用，标 NOT TESTABLE。

### REG-17｜权威冲突与新会话恢复

在无历史新会话中提供冲突的 Runtime State、Session Log 与非权威 Handoff。检查模型是否自行读取权威文件、保留 DISPUTED、阻止依赖冲突字段的行动。环境不支持新会话时，标 NOT TESTABLE。

### REG-03｜last_presented_event_id 语义核验

对连续三条普通社交事件 EVT-003A/B/C：
- 若事件已呈现给玩家，last_presented_event_id 应推进到最后一条已呈现事件，或使用等价的有序呈现游标；
- 若其中一条尚未呈现，不得越过它将后续事件错误标记为已呈现；
- last_answered_event_id 只在玩家行动已获得有效回应后推进；
- checkpoint.last_event_id 与 last_presented_event_id 不得混为一谈；
- 如果现有设计选择用事件表/游标而非单一 ID，必须明确其等价语义并通过恢复测试。

## 6. 总体判定

- 原 v1 的任一硬性断言失败，整体 FAIL。
- REG-16A～E/G 任一错配被发布为 PUBLISHED，整体 FAIL。
- 真实工具写入、无历史新 Chat 冷恢复或产品级遥测不可用时，明确 NOT TESTABLE；不得以模拟通过替代。
- 报告必须逐项区分规范修复有效、执行器实现有效、模拟行为有效、真实产品能力已验证。
