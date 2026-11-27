# Module Closeout 冷恢复回归 v1｜单会话自测报告

> Status: RUN_COMPLETE_SINGLE_SESSION / CI_PASS
> Test type: SINGLE_SESSION_SELF_TEST + test-only Python reference-runtime fault injection
> Result: **PASS（协议逻辑与测试参考实现） / NOT TESTED（真实宿主持久化与跨 Chat 恢复）**
> Date: 2026-11-27

## 1. 固定版本与读取证据

- Repository: `zzhhaannggddii22-hash/Trpg-gm-workbench`
- Test branch: `feat/recoverable-module-closeout-v0.3-main-sync-2026-11-27`
- Tested commit: `7ec3377a537a670005afbf0b51bcda95f7da7d9a`
- Fixture: `GM_Training/Testing/Fixtures/MODULE_CLOSEOUT_COLD_RECOVERY_REGRESSION_v1.md`
- Fixture Blob SHA: `016e897407f6fd467f1d9a0a5420b3000bd6a1df`

本次读取均显式使用测试分支 ref。关键文件与 Blob SHA：

| File | Blob SHA |
|---|---|
| `GM_Training/MODULE_CLOSEOUT_AND_RESOURCE_RECONCILIATION_PROTOCOL.md` | `d9df85f0b736c571ee0e977aaf9d4a32f480a092` |
| `Systems/Triangle_Agency/Rule_Reference/03_MODULE_CLOSEOUT_ADAPTER.md` | `89cf09a75ee8d3597931bbe740490b604b0c1ee7` |
| `GM_Training/Testing/Fixtures/MODULE_CLOSEOUT_COLD_RECOVERY_REGRESSION_v1.md` | `016e897407f6fd467f1d9a0a5420b3000bd6a1df` |
| `GM_Training/07_RUNTIME_CONTROL_PROTOCOL.md` | `85d144598974ec87ecb2137e31289fd445e2c221` |
| `GM_Training/02_WORKFLOW_AND_PREFLIGHT.md` | `d42b75d5dc912212bdace368f31ef8d652641575` |
| `GM_Training/09_MODULE_FOLDER_STANDARD.md` | `7f7f7708d629b71f0a1cf3856b35e4c98a6b7824` |
| `GM_Training/13_PREP_TO_RUNTIME_HANDOFF_STANDARD.md` | `61de3b3e0563475fb7783ee06daa435781214306` |
| `tests/reference_runtime.py` | `1851b3a7ca83c4756f632bed45768bf85b307c26` |
| `tests/test_pr3_repair.py` | `eba6f2eef157a63b6810709853df73222da9f0ec` |
| `Campaigns/Zarek/模组/Bower_Street/03_RUNTIME_STATE.md` | `4255e7c451af8a95cf018af3677ae72db8115ba6` |
| `Campaigns/Zarek/模组/Bower_Street/09_RESOURCE_LEDGER.md` | `65ebc65ee207bac95a1fd811352ed8e9154bf0e7` |

## 2. 执行范围

在当前会话中，按 START → ACTION → ORACLE 顺序对合成状态执行一次冷恢复模拟。模拟输入刻意不提供历史聊天内容，只提供仓库身份、现有 GM-only Operational Diagnostics 记录、Runtime persistence Manifest 引用、PREPARE Manifest 和各字段读回证据。

这验证的是协议决策是否闭合、状态分类是否一致、重试是否幂等；不模拟真实 GitHub 并发条件更新，也不声称跨真实 ChatGPT 会话的宿主持久化已通过。

## 2.1 自动化回归执行

GitHub Actions PR validation #247：
- Python regression suite：16 tests passed（RT20–RT23 包含在内）；
- 新增 RT20–RT23：部分写入恢复、最终发布回执丢失、CLOSED 单一发布边界、身份发现/冲突、计划冻结、依赖 DAG 与局部阻塞均通过；
- RT-16 Markdown link check：389 个 Markdown 文件、523 个本地链接、0 个缺失路径、0 个候选失效锚点；
- git diff --check：PASS；
- Workflow conclusion：success。

首次 CI 的 Python 回归套件已通过，但补丁检查发现 Handoff 文件末尾多一个空行；已修正并重跑，最终运行全绿。

测试参考实现位于 tests/reference_runtime.py，只是测试用合成模型，不是生产 Runtime，不加载真实 Campaign 存档。

## 3. 正向场景结果

| 检查项 | 观察到的决策 | 结果 |
|---|---|---|
| 旧发布指针仍指向 CP-010 | 不据此推断没有待处理操作；先查 Operational Diagnostics 与 Runtime persistence Manifest references | PASS |
| PREPARE 清单发现 | 按 Campaign/Module/Run/Branch 定位 MAN-ALPHA-001 | PASS |
| 操作身份 | 唯一 CLO-ALPHA-001 被复用，不新建第二个 Operation | PASS |
| 规则与计划冻结 | 使用 PLAN-1、EVENTSET-22 与固定规则/适配器版本，不按当前最新版本重算 | PASS |
| 已应用 Time +1 | 读取 FOP-TIME-PLUS-01 的应用证明，保持 APPLIED，不重复 +1 | PASS |
| 已应用 QA 上限 +1 | 保持 APPLIED；不重复增加上限 | PASS |
| 未应用 Time -1 | 仅在独立读回和操作历史证明未执行后标 NOT_APPLIED，再应用一次 | PASS |
| QA 恢复 | 按适配器依赖，使用最终上限 2，恢复至 2/2 | PASS |
| 人物卡边界快照 | 只在原批次中生成/应用一次，绑定最终 Entry ID | PASS |
| 最终发布 | 将结团结果、必需字段证明、交接字段和 Module CLOSED 放入同一发布批次 | PASS |
| 发布后核验 | 读取发布指针和目标版本，确认 CLOSED；不另做 CLOSED 写入 | PASS |
| 目的 Module | READY 保持 NOT_CHECKED，要求 MOD-SYN-BETA 自己检查 Required Fields | PASS |
| Demerits UNKNOWN | 不填零；只阻止依赖精确余额的动作，不阻止本场景独立结团 | PASS |
| Postmortem 未执行 | 不阻止 CLOSED 或目的 Module Preflight | PASS |

## 4. 负向控制

| 控制 | 预期行为 | 结果 |
|---|---|---|
| NC-1：Manifest 查询不可用/完整性不可证 | PENDING_DISCOVERY / UNVERIFIABLE；不得按旧检查点重新结算 | PASS |
| NC-2：多个活动 Operation，或多个 Manifest 同时声称当前有效计划 | 停止自动结算；明确标记 SUPERSEDED 的旧计划修订不构成多候选 | PASS |
| NC-3：最终发布回执丢失，指针已指向原批次且目标可验证 | 认定原批次已发布，不重复应用 | PASS |
| NC-3：指针仍旧且基准/候选未变 | 只重试原批次条件发布 | PASS |
| NC-3：HEAD/目标漂移或历史不可证 | 停止并对账，不盲写 | PASS |
| NC-4：宿主不支持条件发布 | UNPUBLISHED，交付待保存增量，不宣称 CLOSED | PASS |

## 5. 跨文件静态集成检查

本次对 Generic 协议、Triangle Agency Adapter、Runtime、Preflight、Module Folder、Prep-to-Runtime Handoff、Bower Legacy 状态与测试索引进行了读取回核。Manifest 定位沿用既有 GM-only Operational Diagnostics 记录与 Runtime persistence.prepare_manifest_ref / reconciliation_manifest_refs[]；没有新增独立 Operation Index。

静态集成检查：**13/13 项通过**。具体包括：
- Generic 协议入口、稳定 Operation Identity、独立 PREPARE 发现与 PENDING_DISCOVERY；
- 最终 CLOSED 单一发布边界与 Postmortem 非阻塞；
- Triangle Agency 精确 Playwall 授权与单人桌边界；
- Runtime 沿用既有 PREPARE → APPLY → RECONCILE → PUBLISH；
- Preflight 不再把 Postmortem 当作结团前置条件；
- Module Folder 保留 Resource Ledger 唯一权威，不复制资源流水；
- Handoff 区分源 Module CLOSED 与目的 Module READY，并明确 Prep Delivery Manifest 与 Runtime PREPARE Manifest 不可互相替代；
- Bower Street 旧结团明确标记 LEGACY_CLOSEOUT / LEGACY_UNMIGRATED；
- Bower 当前普通 Chaos Pool 的 RESET 余额与 SESSION 01 历史交易审计缺口分开记录。

## 6. 发现与修订

回读时发现 Bower Street Runtime State 的结团前资源段落仍把普通 Chaos Pool 的 BOWER-RES-001 标成“当前待核”，与最终结团覆盖层的“模组结束自动清零为 0”不一致。已将该段改为历史状态说明，并明确区分：
- 当前模组结团余额：按 Campaign 已确认规则 RESET 为 0；
- SESSION 01 原始交易应用情况：仍是历史审计缺口；
- 两者不再混为同一个当前余额未知项。

另发现 Prep-to-Runtime Handoff 新增章节初版顺序不正确，已调整并重新核对；同时保留 main 新增的 Delivery Manifest、职责角色与提交事务规范，并明确它们不替代 Runtime 的 Module Closeout PREPARE Manifest。

## 7. 结论与限制

**协议逻辑与 test-only 参考实现回归通过。** 对旧指针、PREPARE 冷发现、稳定操作身份、部分字段应用、发布回执丢失、CLOSED 单一发布边界、局部阻塞和目的 Module READY 分离，合成决策与进程级故障测试均通过，没有发现重复应用或错误推进路径。

以下仍为 NOT TESTED：
1. GitHub/宿主是否实际提供 Operation ID 的条件唯一创建；
2. 既有 GM-only Operational Diagnostics 与 Runtime Manifest 引用是否在真实跨 Chat 环境中完整、可查询且可独立读回；
3. 多文件候选写入与最终发布指针是否能进行条件/原子更新；
4. 新 Chat 是否真的能在无历史上下文时定位未发布 Manifest；
5. 实际宿主故障注入下的并发、回执丢失、分支漂移与部分写入恢复。

因此，本报告不能作为真实跨会话恢复或持久化通过证据，也不能据此宣称 v0.3 已具备生产级自动结团能力。下一阶段应检查 ChatGPT/工作台宿主可观察能力，并决定采用自动发布还是人工待保存增量。
