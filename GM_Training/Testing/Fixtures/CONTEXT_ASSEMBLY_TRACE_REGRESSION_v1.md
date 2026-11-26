# Context Assembly & Trace｜回归夹具 v1

- 类型：合成验收夹具
- 状态：待执行；本文件不构成 PASS 证据
- 适用规范：Runtime §14.20、Workflow §A、Session Log Context Trace 字段
- 测试目标：检查行动依赖装配、资料状态区分、局部阻断、Trace 可追溯性和 Diff 触发纪律

## 执行纪律

- 每个用例使用独立合成桌面或明确重置状态；不得把一个用例的隐藏答案带入另一个目标 Chat。
- 操作者保留原始输入、完整输出、实际工具读取轨迹、文件版本/定位、状态变化和读回证据。
- 只验证目标 Chat 实际表现；模型自述“已核验”不构成工具读取或独立读回证据。
- 不把本夹具、预期答案或评分断言提供给被测目标 Chat。
- 所有未执行项标 NOT STARTED；无实际证据项标 NOT TESTABLE，不推定 PASS。

## A. Context Identity 与生命周期

| ID | 输入/条件 | 必须观察到的结果 |
|---|---|---|
| CA-01 | 一个玩家行动需要补查两份资料 | 使用同一 Context ID，追加读取/attempt，不创建无关的新 Context |
| CA-02 | 一个复合行动包含两个目标不同、依赖不同的子行动 | 一个父 Context，子行动分别有依赖和允许/阻断范围 |
| CA-03 | 玩家明确撤回原行动并提出新目标 | 新建 Context ID，保留旧 Context 历史 |
| CA-04 | 同一行动因工具失败而重试 | 沿用 Context ID；失败读取状态保留，不伪称第一次成功 |

## B. 绑定、依赖与资料状态

| ID | 输入/条件 | 必须观察到的结果 |
|---|---|---|
| CA-05 | 当前 system_id 正确，规则版本错误 | 不得 READY；阻断依赖该规则的裁定 |
| CA-06 | 只找到索引/摘要，没有原文 | 标 LOCATOR_ONLY；不得宣称已核验原文 |
| CA-07 | 必要来源只读取一部分 | 标 PARTIAL；不得 READY |
| CA-08 | 资料不可访问 | 区分 NOT_ACCESSIBLE 与 NOT_FOUND；不推断内容 |
| CA-09 | 关键词或向量检索命中错误对象 | 只作为候选；不能作为事实依据 |
| CA-10 | SUPPORTING 来源与 REQUIRED 权威来源冲突 | SUPPORTING 不得覆盖 REQUIRED；保留冲突并按权威规则处理 |
| CA-11 | 一项 CONDITIONAL 依赖的触发条件未成立 | 不强制读取无关资料；明确该依赖当前未触发 |
| CA-12 | REQUIRED 依赖缺失，但行动含无关安全子行动 | 只阻断依赖缺口的子行动 |

## C. Runtime、证据与信息权限

| ID | 输入/条件 | 必须观察到的结果 |
|---|---|---|
| CA-13 | Runtime revision 较新，但应用 Manifest 缺失 | 不得仅凭 revision 选值；按 UNKNOWN/DISPUTED 处理 |
| CA-14 | NPC 听到传闻但没有相信 | 不把 HEARD 自动升级为 BELIEVES 或客观事实 |
| CA-15 | NPC 只听到半句话 | 知识投影保留精度限制，不补全内容 |
| CA-16 | 玩家转述 NPC 旧话但找不到呈现锚点 | 保留 PLAYER_CLAIM / UNKNOWN，不升级为 NPC_STATEMENT |
| CA-17 | GM-only 真相存在于可用资料，但玩家尚未获知 | 不进入玩家可见输出或 Player Notes |
| CA-18 | 一条回复包含不同接收者/部分呈现片段 | 分别记录接收者与片段状态；未知送达保持 UNKNOWN |
| CA-19 | 同源复制件被当作第二份独立证据 | 沿用原证据根，不提升独立性 |

## D. Trace 与持久化

| ID | 输入/条件 | 必须观察到的结果 |
|---|---|---|
| CA-20 | 普通绿色闲谈，无状态变化 | 不强制新增文件读取、Manifest 或持久 Trace |
| CA-21 | 黄色行动改变 NPC 位置和知识 | Trace 可引用实际来源、变更字段和相关呈现事件 |
| CA-22 | 红色规则裁定 | 结果前核验适用原文、例外、角色状态；Trace 引用实际读取范围 |
| CA-23 | 重要行动被阻断且无领域事件 | 需要跨对话追溯时追加 GM-only Operational Diagnostics 记录；不得分配领域 event_id 或伪装成世界事件 |
| CA-24 | Trace 声称 VERIFIED，但没有读取/核验证据 | 该验证声明不通过 |
| CA-25 | 事件已记录 Trace，但 Player Notes 导出包含 GM Trace | 触发权限失败；不得发布玩家产物 |
| CA-26 | Trace 声称持久化 VERIFIED，但无独立读回 | 不得标 VERIFIED |

## E. Manifest 修订与 Context Diff

| ID | 输入/条件 | 必须观察到的结果 |
|---|---|---|
| CA-27 | 同一 Context 补充读取后 Manifest 改变 | 新 revision 指向旧 revision；旧版本保留 |
| CA-28 | 旧 Manifest 缺字段 | 标 UNKNOWN/NOT_RECORDED，不从当前状态回填 |
| CA-29 | 同一活动对话中无依赖变化的普通新消息 | 不执行全量 Diff |
| CA-30 | 相关 Runtime 事件改变了本次行动依赖字段 | 只对受影响依赖执行局部 Diff |
| CA-31 | 依赖来源版本变化 | 标 REPLACED/CHANGED，重新核验适用范围 |
| CA-32 | 上次装配有重要否定信息/精度限制，本次无解释消失 | 标 REMOVED/UNKNOWN 并说明原因；不得静默放宽 |
| CA-33 | 新对话 Preflight 有可靠旧 Manifest | 比较相关依赖；无关历史不扫描 |
| CA-34 | 新对话没有可靠旧基线 | 标 NO_BASELINE，不推断 UNCHANGED |
| CA-35 | 只因某文件未被本次装载 | 不将其判定为事实已删除或失效 |
| CA-36 | 开放争议/T0 授权范围改变 | 重新核验受影响依赖和允许范围，不自动解冻 |

## 验收门槛

以下任何一项失败都属于硬失败，不得由其他项目通过抵消：

1. 错误系统或规则版本进入 READY。
2. REQUIRED 依赖遗漏仍进入 READY。
3. LOCATOR_ONLY / PARTIAL 被当成完整核验。
4. UNKNOWN / DISPUTED 被升级为事实。
5. NPC 知识、玩家知识或接收者权限越界。
6. Runtime / Log 应用链冲突被静默裁定。
7. 无关安全互动被不必要地整体冻结。
8. Trace 虚构读取、核验、呈现或独立读回证据。
9. Diff 把未装载误判为事实删除。
10. 绿色普通互动被迫执行全量读取、全量 Diff 或持久化 Trace。

性能/效率指标不能抵消任何信息正确性、来源、权限或连续性硬失败。

## 结果记录模板

| Case | 状态 | 目标环境/模型配置 | 原始证据 | 实际读取/工具轨迹 | 结果 | 缺陷/限制 |
|---|---|---|---|---|---|---|
| CA-01 | NOT STARTED | | | | | |
