# P1-0 最终基线分析、修复记录与 P1-0C 交接

日期：2026-11-24。依据用户回传的 P1-0 最终报告。原始判定 TARGET_BASELINE_NOT_MET；4 FAIL、1 PARTIAL。仅针对该批合成样本，不外推为模型/账户的一般能力结论。

## 1. 最终基线事实
| 用例 | 判定 | 可见失败/限制 |
|---|---|---|
| REG-14 | FAIL | 恢复锚点正确，但续接时近义复述已回应广播 |
| REG-17 | FAIL | 识别 Runtime/Log 冲突和 reconciliation UNKNOWN，仍选定 player 持有钥匙，未字段级 DISPUTED |
| REG-11 | FAIL | 第 2 轮发现无来源主委托后仍推荐 Sol 并演出接触；第 3 轮只局部阻止直接执行，未保持跨轮冻结 |
| 字段级导出 | FAIL | Controls 正文筛选正确，但同一玩家文件附录泄露其他接收者和未呈现条目的内部 ID 与排除原因 |
| E13 | PARTIAL | 四轮可见路由正确；首轮操作说明输入时序污染，逐轮工具读取证据不足 |

证据边界：目标端原始会话界面、真实工具轨迹、模型/档位界面、导出原始字节及独立读回未完整核验。判定只针对回传文本与已锁定夹具。

## 2. 根因分析
### R1｜连续性只核对事件锚点，没有约束输出增量
系统识别 EVT-014 已呈现/已回应，却把旧回复换一种说法再次交付。恢复时须联查 last_answered_event_id、最近 GM 可见回复与 Player Notes 呈现状态；旧内容只允许必要短指代，不得作为新信息复述。

### R2｜快照权威被误用为冲突裁决权
Runtime 是当前状态快照，Session Log 是变化历史。Runtime 的权威身份不等于它自动证明某条 Log 事件已合并。reconciliation UNKNOWN 时必须保留冲突值，将受影响字段标 DISPUTED，并冻结依赖行动。新记录需要双侧可核验应用标记；旧记录缺证据保持 UNKNOWN，不回填猜测。

### R3｜T0 识别没有持续转化为行动门禁
REG-11 第 2 轮识别无来源摘要，却继续把 Sol 作为该调查线目标。第 3 轮才阻止监控/搜寻的直接执行，但没有回溯受影响命题依赖并持续冻结。每轮必须对玩家行动和 GM 建议做命题依赖检查；按行动目的区分同一 NPC 的普通互动与受影响调查。

### R4｜审计附录绕过玩家字段白名单
Controls 正文安全，EXPORT AUDIT 又列出被排除条目 ID、接收者范围和未呈现状态。玩家交付物混入 GM 审计产物。修复为 Player Artifact 与 GM Audit Artifact 双产物分离；玩家文件不含逐项排除细节；扫描最终成品全文。工具无法读取的元数据/嵌入对象标 NOT_VERIFIABLE，不能虚称全量扫描。

### 正向证据｜E13
E13 四轮可见路由均符合授权边界，尤其第三轮拒绝附带越权请求、第四轮拒绝以笼统授权解冻。保留为正向回归，不把 PARTIAL 证据等级提升为 PASS。

## 3. 修复优先级
1. P1-0C：四项硬失败定向修复与目标环境回归。
2. E13-C：保留正向路由回归并补齐输入时序/逐轮工具证据。
3. P1-0R：独立测试跨文件部分提交与冷恢复。
4. P1-1：只有可靠性门槛通过后才开展性能测量。

禁止用速度、上下文压缩或更短提示词绕过可靠性门禁。

## 4. 本次规范修订
- 07_RUNTIME_CONTROL_PROTOCOL.md：强化 §14.10 合并证据；§14.11 明确为 T0 后续行动路由唯一操作规范；§14.12 限定不可检查文件部分的证据声明。
- GM_RELIABILITY_AND_EXPERIENCE_CONTROL_PROTOCOL.md：§12 改为规范归属说明，避免与 Runtime §14.11 重复维护两套操作流程。
- RUNTIME_STATE_TEMPLATE.md：增加 checkpoint.applied_event_ids 与 reconciliation_manifest_ref；旧存档不补造应用证明。
- 03_SESSION_LOG_TEMPLATE.md：增加回应/呈现与 runtime_application 字段，区分 RESPONDED 与 PRESENTED。
- GM_RUNTIME_P1_PERFORMANCE_PLAN.md：状态改为 P1-0 FAILED；增加 P1-0C 修复与回归门槛，阻止过早开展 P1-0R/P1-1。

上述文件已写入 GitHub；仍须读回核验后才能标记为已核验。

## 5. 执行文件
- 定向回归夹具：GM_RUNTIME_P1_0C_CORRECTIVE_REGRESSION_v1.md
- 目标环境提示词：GM_RUNTIME_P1_0C_EXECUTION_PROMPT.md

旧失败样本永久保留；新样本单独评分。新样本通过不改写旧报告。