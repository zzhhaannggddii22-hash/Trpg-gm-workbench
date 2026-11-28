# Countdown 与长期项目运行程序

> 规则范围：Daggerheart Core Set  
> 来源基准：Official Daggerheart SRD 2.0（2026-08-25）  
> 状态：规则整理完成；参考执行器 DH-REF-103–109 已于 Run 11 以 109/109 全套测试通过  
> 性质：运行程序摘要，不替代官方规则文本。

## 1. 通用原则

Countdown 从起始值开始，推进时剩余值减 1；降至 0 时触发其预先定义的效果。不要把“推进”理解为数值增加。每个 Countdown 必须记录：名称/ID、类型、起始值、剩余值、触发效果、推进来源、事件去重标识，以及是否循环。

GM 应在创建时说明玩家角色可察觉的时间压力或进度意义。倒计时不是隐藏的任意惩罚器：触发效果必须事先由虚构情境或能力文本支持。

## 2. 类型与推进时机

| 类型 | 推进时机 | 结果 |
|---|---|---|
| Standard | 每次 PC Action Roll | 每次减 1 |
| Dynamic Progress | 每次相关 Action Roll | 按 Hope/Fear 结果推进 0–3 |
| Dynamic Consequence | 每次相关 Action Roll | 按 Hope/Fear 结果推进 0–3 |
| Long-term | 休息或其他明确的长期时间节点 | 通常每次 Long Rest 减 1；扩展时间跳跃按 Campaign 处理 |

标准倒计时不使用动态表。若卡牌/敌人/环境明确写明 Countdown [n]，按 Standard Countdown 处理，初始值为 n。

### Dynamic Countdown 推进表

| Action Roll 结果 | Progress Countdown | Consequence Countdown |
|---|---:|---:|
| Failure with Fear | 0 | 3 |
| Failure with Hope | 0 | 2 |
| Success with Fear | 1 | 1 |
| Success with Hope | 2 | 0 |
| Critical Success | 3 | 0 |

Critical Success 作为 Hope 结果处理。Tag Team Roll 对追踪 Action Roll 次数的 Countdown 只计一次，不能因两名 PC 各掷一组骰而推进两次。

## 3. 事件去重与触发

- 每个 Action Roll / Rest Event 应有稳定唯一 ID。
- 同一事件对同一 Countdown 最多结算一次；不同 Countdown 可以分别响应同一事件。
- 当 Countdown 已到 0，后续推进仍保持 0，不产生负数，也不重复触发已结算的效果。
- 一个事件的推进值为 0 时，仍应记录该事件已被处理，避免重复结算。
- Countdown 达到 0 后，执行预先定义的效果并记录结果；若是 Loop Countdown，按其明确设定重置。不要默认所有倒计时自动循环。

## 4. Work on a Project（Long Rest Move）

这是 Long Rest 专属 Move。GM 必须先批准项目；项目适合需要较长时间、但角色可在休息期间推进的目标，例如破译古文或制作特殊武器。

### 建立项目

1. 玩家说明目标、用途和希望达成的结果。
2. GM 判断是否适合用长期项目表示，并批准或说明为什么无需项目倒计时。
3. 首次使用 Work on a Project 时建立一个 Progress Countdown。
4. GM 根据项目复杂度、工具/材料可用性和故事影响确定起始值。规则没有提供固定公式；不要伪造统一换算表。
5. 记录项目负责人、参与者、所需资源、当前阶段、完成效果与可能的外部风险。

### 推进项目

- **Simple Project：** 每次合法使用 Work on a Project Move，Progress Countdown 自动减 1。
- **Complex Project：** GM 要求进行 Action Roll，以判定推进程度；将已结算的 Action Roll 结果用于 Progress Countdown 动态推进表。
- 项目推进应与实际工作方式、工具和已建立局势相符。若行动完全没有不确定性，GM 可将项目归为 Simple，而不是为了复杂感强迫掷骰。
- 每名 PC 每次 Long Rest 最多两个 Downtime Move；Work on a Project 占用其中一个。
- 未获 GM 批准、不是 Long Rest、未建立起始值、复杂项目缺少 Action Roll 结果、或该 PC 已用完两个 Move 时，不推进倒计时。
- Countdown 到 0 时，执行事先约定的项目完成效果；若成果存在代价、限制或后续工作，应在项目定义时写清楚，不要在完成时临时改变目标。

## 5. Long Rest 的长期世界推进

正常 Long Rest 结束时，GM 获得 1d4 + PC 数量 Fear，并可推进一个自己选择的 Long-term Countdown。该倒计时应代表正在后台发展的威胁、势力目标或时间变化。它与 PC 的 Work on a Project 是两件不同的事：

- Work on a Project：PC 花费自己的 Downtime Move，推进自己的 Progress Countdown。
- GM Long-term Countdown：GM 在 Long Rest 后选择推进一个世界侧长期倒计时。

若有多个世界侧倒计时，不要机械地全部推进；选择最符合当前局势、最可能在玩家休息期间持续发展的那一项。Campaign Frame 或特定能力另有规定时按其文本。

### 中断休息的边界

SRD 明确规定：中断 Short Rest 时 PC 不获得该次休息收益；中断 Long Rest 时 PC 只获得 Short Rest 收益。SRD 对这种中断是否仍结算 GM 的休息 Fear 与 Long-term Countdown 后果没有给出足够明确的统一说明。本工程继续保留桌面裁定标记，不将“未自动结算”误写成官方规定 GM 后果为零。

## 6. GM 快速检查

- [ ] 这个倒计时代表什么可理解的局势变化？
- [ ] 它是 Standard、Progress、Consequence 还是 Long-term？
- [ ] 推进时机是否明确，是否与行动/休息事件正确绑定？
- [ ] 同一 Action Roll 是否只推进一次？
- [ ] Tag Team 是否只计一个 Action Roll？
- [ ] 达到 0 后的效果是否预先定义？
- [ ] 项目是否获 GM 批准，是否确实属于长期项目？
- [ ] Simple / Complex 的判断是否基于项目实际复杂度，而非为了多掷骰？
- [ ] 是否正确扣除 PC 的 Downtime Move 名额？
- [ ] 是否将玩家项目与 GM 世界侧长期倒计时分开？

## 7. 来源

- Official Daggerheart SRD 2.0：Countdowns、Downtime、Projects During Downtime。  
  https://www.daggerheart.com/srd/
- 可检索章节镜像：  
  https://daggerheartsrd.com/rules/  
  https://daggerheartsrd.com/rules/downtime/
- 非官方镜像仅用于定位和交叉阅读；发生差异时回到官方 SRD 2.0。
