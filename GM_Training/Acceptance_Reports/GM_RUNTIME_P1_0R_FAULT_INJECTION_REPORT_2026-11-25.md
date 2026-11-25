# P1-0R 持久化故障注入报告

- 日期：2026-11-25
- 状态：**PASS（隔离文件系统协议测试）**
- 测试对象：合成 Runtime State、Session Log、PREPARE manifest
- 执行方式：独立临时目录；写入进程在指定提交点后由 `os._exit` 强制终止；随后由全新进程冷读取并恢复
- 可重复脚本：[p1_0r_fault_harness.py](../Acceptance_Test_Fixtures/P1_0R/p1_0r_fault_harness.py)

## 1. 测试目的

验证跨文件保存只完成一侧或两侧均未完成时，恢复过程能够识别不完整批次、保留争议、补齐缺失的审计/争议标记，并且不重放领域事件。

## 2. 三个故障窗口

| 用例 | 故障注入点 | 恢复前持久化状态 | 结果 |
|---|---|---|---|
| A | Runtime marker 已落盘，Log 追加前进程终止 | Runtime 有 marker；Log 无 marker | PASS |
| B | Log incident 已落盘，Runtime 写入前进程终止 | Log 有 marker；Runtime 无 marker | PASS |
| C | PREPARE 已落盘，两个目标写入前进程终止 | Runtime、Log 均无 marker | PASS |

每个场景都由独立恢复进程读取 PREPARE 与两个目标，完成恢复后再启动第二个独立恢复进程验证幂等性。

## 3. 统一验收断言

三个用例在第一次和第二次冷恢复后均满足：

- Runtime 与 Session Log 各恰有一条匹配的 marker。
- marker 的 batch_id、event_id、event_revision_id、payload_fingerprint 与 PREPARE 一致。
- Runtime checkpoint revision 仍为 5，没有推进到 target_revision 6。
- 领域状态 `synthetic_counter` 仍为 0；领域事件没有被重放。
- event 仍在 `unapplied_event_ids`，不在 `applied_event_ids`。
- Runtime branch 为 `DISPUTED`，`can_advance=false`。
- persistence status 为 `INCOMPLETE`。
- 第二次恢复没有重复追加 marker。

## 4. 结论

在本夹具覆盖的故障窗口内，PREPARE 可作为恢复依据；恢复程序按完整事件修订身份和 payload fingerprint 对账，只补齐缺失的争议/审计 marker，不重放领域事件。三个故障窗口均通过，P1-0R 的隔离协议测试完成。

## 5. 证据边界与未覆盖项

本测试证明的是**隔离 Python 文件系统模型中的恢复协议行为**，不是 ChatGPT 产品端、GitHub Connector 或任何真实宿主存储的持久化保证。

未覆盖：
- 目标环境真实工具写入/读回语义；
- 并发写入与竞争条件；
- PREPARE manifest 本身丢失或损坏；
- 故障持续存在（例如磁盘持续不可写、配额耗尽）；
- 主机级断电、文件系统损坏、介质损坏；
- 多进程同时执行恢复的锁与幂等协调。

上述项目留待性能优化结束后的地基质量迭代，不得由本次 PASS 外推。

## 6. 阶段处置

按用户指示，P1-0C 目标环境地基质量回归暂缓。历史 P1-0 的 4 FAIL、1 PARTIAL 与 P1-0C 独立审查 REJECT 均保留，不回写为 PASS。性能优化阶段只启用 T0 识别与告警模式；完整事故处置待用户要求恢复地基质量迭代时再启用。
