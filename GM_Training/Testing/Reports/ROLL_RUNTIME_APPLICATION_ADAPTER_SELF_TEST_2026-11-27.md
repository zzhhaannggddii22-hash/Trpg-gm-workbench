# Roll Runtime Application Adapter｜可执行契约自测报告

> 类型：SINGLE_SESSION_SELF_TEST + 本地文件系统故障注入
> 结果：PASS（参考适配器契约）；NOT PRODUCTION RUNTIME ACCEPTANCE
> 基线：main `53c0774b93fcf990df0e99aa0f4874a230ef57de`
> 范围：合成事件、临时目录、Python 标准库；未读写正式 Campaign 数据。

## 执行结果

`roll_runtime_adapter.py` 实际执行 11 项测试，11 PASS / 0 FAIL：

1. 成功提交后重复投递：返回 IDEMPOTENT_REPLAY；资源流水不重复。
2. AFTER_PREPARE 故障：冷恢复 DISPUTED，不重放领域事件。
3. AFTER_LEDGER 故障：冷恢复 DISPUTED；已写流水保留，不重复追加。
4. AFTER_SESSION_LOG 故障：冷恢复 DISPUTED；Log/流水部分证据保留。
5. AFTER_RUNTIME_CHECKPOINT 故障：冷恢复 DISPUTED；禁止继续推进。
6. AFTER_MANIFEST 故障：Manifest 尚未被 checkpoint 引用，判定 DISPUTED。
7. AFTER_RUNTIME_MANIFEST_LINK 故障：持久化证明完整，冷恢复读回并重建缺失的玩家投影。
8. AFTER_PROJECTION 故障：冷恢复验证既有提交与投影，不重复应用。
9. 玩家投影含内部 event_id：拒绝生成，不产生玩家文件。
10. 连续两笔资源交易：第二笔前值从 Resource Ledger 链计算（2 → 4 → 3），Runtime State 不保存余额。
11. 过期 base_revision：拒绝应用。

## 与现有规范的对齐

- 沿用 Runtime §14.14 的 immutable manifest、base/target revision、逐字段应用证明与 checkpoint manifest 引用。
- Session Log 只引用 Resource Ledger Entry ID；Runtime State 不复制资源余额。
- 资源前后值从 Resource Ledger 的连续流水推导，不把测试快照变成第二份交易账本。
- 玩家投影仅接受 allowlist 字段；内部标识与 GM-only 字段不会进入玩家载荷。
- 部分写入一律 fail-closed；不自动重放可能已经生效的领域效果。

## 发现与边界

本测试证明的是**本地合成文件系统上的参考实现行为**，不是生产运行时集成。没有真实宿主存储 API、并发写入、分布式锁、跨文件原子事务、真实用户交付回执、工具级 RNG、Dice UI 宿主或 Playwall 骰子机制测试。Manifest supersession / correction 全生命周期也未在本夹具实现。

因此，本报告不授权把骰子路由协议启用为主 Skill 强制入口，也不把参考适配器称为已部署 Runtime。进入生产集成前，仍需绑定实际存储 API、并发控制和宿主级故障注入/独立读回。

## 结论

**PASS：参考适配器的 11 项可执行契约测试通过。**

**NOT PRODUCTION ACCEPTANCE：** 当前仓库没有被本次改动连接的生产 Runtime 存储宿主。该实现与报告可作为 main 中的测试/参考契约；真实 Runtime 接入仍是单独的后续工程阶段。
