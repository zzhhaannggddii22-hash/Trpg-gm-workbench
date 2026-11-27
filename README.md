# Trpg-gm-workbench

跨规则系统的 TRPG GM 专业工作台：规则研究、备团、运行、复盘、训练与能力迭代。

## 核心架构

- [2026-11-26 仓库结构变更通知](STRUCTURE_CHANGE_NOTICE_2026-11-26.md)：测试资料已集中迁移至 GM_Training/Testing；后续会话请先读取该通知与 Testing 总入口。

- [测试资料中心](GM_Training/Testing/README.md)：夹具、执行提示、验收报告与长期基准的统一入口。

- [项目目录与文件职责](PROJECT_STRUCTURE.md)：仓库结构、权威归属与迁移约定。
- [GM 能力架构](GM_Training/00_GM_CAPABILITY_ARCHITECTURE.md)：定义通用 GM 能力如何在真实场景中有机联动，以及整体优秀的验收原则。
- [GM Training](GM_Training/README.md)：通用主持原则、运行 Skill、人物模拟、叙事呈现、备团流程、训练与评价。
- [多系统架构与上下文隔离协议](SYSTEM_CONTEXT_PROTOCOL.md)：系统选择、加载、锁定与切换规则。
- [规则系统目录](Systems/README.md)：各套 TRPG 系统的独立规则环境与专属资料。
- [战役目录](Campaigns/README.md)：各战役的系统绑定与独立状态。
- [通用研究与候选池](Research/README.md)：跨系统研究方法与尚未成熟的候选系统。
- [专业能力迁移机制](CAPABILITY_TRANSFER.md)：从 TRPG 实战中提取可跨场景验证的通用能力。

## 工作分工

1. **GM_Training**：只维护跨系统通用 GM 能力、运行方法、备团/复盘流程、训练和评价。
2. **Systems**：维护系统专属规则、术语、机制、官方裁定和适配方法。
3. **Campaigns**：维护具体战役、模组、人物、CANON、Runtime State 与 Session Log。
4. **Research**：维护跨系统研究材料和尚未成熟的候选方法；系统专属研究留在对应 Systems 子目录。

## 工作流程

1. 确认当前桌面的 system_id 与规则版本；按 SYSTEM_CONTEXT_PROTOCOL 只加载该系统的权威资料。
2. 读取对应 Campaign / Module 资料，建立设定基石、可调用素材、调查链与 NPC/环境因果账本。
3. 按风险与复杂度执行 Prep QA；重要调查链、复杂扩写和关键人物/环境因果须进行第二轮审核。
4. 修订并记录 QA 结果，生成 Runtime Quick Reference 与 Prep-to-Runtime Handoff。
5. 每次新对话/新 Session 执行 Preflight；运行中复用有效快照并按风险回查。
6. Session 后记录真实发生的变化并复盘；专项能力修复后必须回到综合场景验证。

## 质量原则

优秀 GM 不是若干单项能力分别合格，而是规则、事实、玩家能动性、人物、环境、信息、即兴、节奏与连续性在同一场游戏中有机结合，并整体达到优秀。任何硬性错误或关键短板不能由文笔、气氛或速度抵消。

## 信息边界与版权

- GM-only 文件包含秘密、答案或剧透，不得作为玩家资料发送。
- 本仓库公开；战役人物卡与记录亦为公开资料。
- 第三方受版权保护规则书、模组全文及完整翻译文本不在本仓库分发；仅保留合法来源索引与说明。
- 原私人仓库保留非 TRPG 私人资料及《The Vault》中文全文备份；TRPG 专业资料的唯一工作主仓库为本仓库。

## 维护约定

- [Issue 独立编号与登记规范](ISSUE_TRACKING.md)：项目 Issue 使用独立的 ISSUE-NNN 编号，GitHub 原生编号仅作定位符。

- 不静默覆盖已确立的战役事实；更正时记录原因与影响。
- 历史版本保留其历史语境，不把旧文件自动视为当前运行指令。
- 通用能力改进须有跨场景证据；未经验证的经验先作为候选，不直接写入凯西核心规范。
- 公开仓库不得提交凭证、密钥、私人真实身份资料或未经授权的第三方全文。
