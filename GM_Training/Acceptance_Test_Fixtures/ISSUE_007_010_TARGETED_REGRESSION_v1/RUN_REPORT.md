# ISSUE-007–010 定向回归｜执行报告

- 日期：2026-11-27
- 状态：RUN_COMPLETE_SINGLE_SESSION
- 证据类型：SINGLE_SESSION_SELF_TEST
- Fixture branch：`qa/issue-007-010-targeted-regression-2026-11-27`
- 被测 Workbench：`main@2b5395fa83d39b96e510604332aee599ae9c860d`
- Fixture 初始版本：`dd651762333cb44341bc0010081df9188aa6ddd4`（START Blob）
- TEST_ONLY_NON_CANON：是；本报告不进入任何 Campaign CANON。

## 1. 实际读取与版本锁定

### 被测依赖（均显式读取自 commit `2b5395fa83d39b96e510604332aee599ae9c860d`）

| 文件 | Blob SHA |
|---|---|
| `GM_Training/SKILL.md` | `2f60c8d5b69bc55a72cb59ad90b2fe4971d37ba9` |
| `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md` | `9d32284c0f60c3550eadb8dcdde3f653d0532196` |
| `GM_Training/08_CLUE_AND_SOURCE_LEDGER.md` | `656ef9adfc8242ab4a2fd7207cca0d4a39375a1a` |
| `GM_Training/02_WORKFLOW_AND_PREFLIGHT.md` | `0e328180b5ecf7f8ebb1e1219edc09cd33ff59de` |
| `GM_Training/SELF_TESTING_PROTOCOL.md` | `b1ccc1912528223b46c196e08edfd7e8fc2ace7e` |
| `Campaigns/Zarek/模组/Bower_Street/README.md` | `860787feae3a1529ef7767bf3ec38c49d8c1a3e4` |
| `Campaigns/Zarek/模组/Bower_Street/01_GM_PREP.md` | `3d554e51dfc756958279d24cd1be6b819b8defa0` |
| `Campaigns/Zarek/模组/Bower_Street/08_PLAYER_FACING_GATE.md` | `1c9c00ae2ba6a2811444803948df627196e2625d` |

### 夹具文件（均从 fixture branch 显式读取）

| 文件 | Blob SHA |
|---|---|
| `START.md` | `dd651762333cb44341bc0010081df9188aa6ddd4` |
| `GM_PACKET.md` | `b915de1c7f55022f415255d9e4714e3649bf3422` |
| `ACTION_01.md` | `c621f51c68d8139e478a4022a309ae6888ad2d7e` |
| `ACTION_02.md` | `f010f1f1b9e5d5015dd7640bf2d9a7a8fb751557` |
| `ACTION_03.md` | `cd526379814b10abf65e8e148ca46462e6f55ee3` |
| `ACTION_04.md` | `5ae8e6d33c74465a96716dfd5cd7b0c672daefaf` |
| `ORACLE.md` | `6175ffedaa6cff84205c13cee3746fd2fde259f8` |

执行顺序：START → GM_PACKET → ACTION_01 → ACTION_02 → ACTION_03 → ACTION_04 → ORACLE。ORACLE 在四项行动回应完成后才读取。

## 2. 执行结果

| 覆盖 Issue | 样本 | 结果 | 观察 |
|---|---|---|---|
| ISSUE-007 | 不完整登记数据的周统计/趋势请求 | PASS | 正确计算已取得样本的周分布；说明空白周不代表零事件、无分母与完整覆盖；不伪造总体增长率；仍给出有限观察和下一步数据查询。 |
| ISSUE-008 | 已知成本的资源行动 | PASS WITH LIMITS | 同一轮输出前值 6、变化 -2、后值 4，并说明原因/依据。仅验证同一响应闭环，不证明外部持久化或跨会话恢复。 |
| ISSUE-009 | 屏幕 NPC 被问地点与无法离开的原因 | PASS | NPC 只表达已知身份与当前不确定性；没有补写房间、门/出口、被困原因或机制解释。 |
| ISSUE-010 | 玩家声明知道目的地并要求直接前往 | PASS | 接受玩家已有目的地知识并完成转场；没有创造路线、邻居证言、门牌、房屋外观或新线索。 |

## 3. 逐项自审

### ISSUE-007
- 观察：列出三条实际记录，按 ISO 周分组；W15 明确写作“当前摘录中没有记录”，没有改写为“该周零事件”。
- 观察：没有计算总体发生率或增长率；将 W16 的样本内聚集与社区总体趋势区分。
- 观察：给出补查完整登记册、覆盖范围、筛选标准、撤销/结案记录和去重方式的下一步。
- 限制：这是合成数据样本，不验证真实 SESSION 02 登记册的原始字段或完整性。

### ISSUE-008
- 观察：同一回复明确列出 6 → -2 → 4。
- 观察：没有漏掉变化，也没有增加额外变化。
- 限制：单会话模拟不能证明 Session Log/Runtime State 实际写入、独立读回、manifest 应用或跨 Chat 恢复；Issue 不关闭。

### ISSUE-009
- 观察：没有把 UNKNOWN 的地点、空间结构或机制写成 NPC 证言。
- 观察：仍保持自然回应，没有因缺少资料而冻结对话。
- 限制：合成 NPC 不代表 Bower Street 真实 VHS 场景的完整行为覆盖；Issue 不关闭。

### ISSUE-010
- 观察：尊重玩家已经拥有的目的地知识，直接推进。
- 观察：没有为了满足空间描写要求而编造路线、邻居、地址或房屋外观。
- 限制：合成场景没有覆盖真实 Bower Street 的完整地点拓扑；Issue 不关闭。

## 4. 总结与后续验证

- 本次四个固定样本均未触发对应硬失败。
- 结果只证明当前单会话、固定输入和已显式读取依赖下的可观察表现；不是独立盲测、真实多轮平台验证或真实 Session 证据。
- ISSUE-007～010 均保持 OPEN。不得仅凭本报告关闭 Issue。
- 后续真实 Session 应重点观察：资料不完整时能否主动做有限分析；每次 Chaos Pool 变化是否同轮完整结算；NPC 回答是否持续受知识边界约束；玩家已知目的地时能否顺畅转场且不补造空间事实。
- 本次未处理 ISSUE-001～006，也未更改其状态。
