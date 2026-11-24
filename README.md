# Multi-System TRPG GM Workbench

独立的 TRPG GM 专业工作台：规则研究、备团、运行、复盘、训练与能力迭代。

## 目录
- [GM_Training/](GM_Training/README.md)：通用 GM 原则、Preflight、裁定纪律、运行控制、线索管理、备团审核与专业能力模块。
- [多系统架构与上下文隔离协议](SYSTEM_CONTEXT_PROTOCOL.md)：系统选择、加载、锁定与切换规则。
- [规则系统目录](Systems/README.md)：每套 TRPG 系统的独立规则环境与专属资料。
- [Triangle Agency 系统资料](Systems/Triangle_Agency/README.md)：《三角机构》专属规则、索引、研究与裁定记录。
- [战役目录](Campaigns/README.md)：各战役的系统绑定与独立状态。
- [扎雷克战役](Campaigns/Zarek/README.md)：绑定《三角机构》中文 v22 的人物档案、战役状态、NPC 索引与模组记录。
- [通用研究与候选池](Research/)：跨系统研究方法与尚未正式引入的候选系统；系统专属研究归入对应 Systems 文件夹。
- [高级模型备团 QA 协议](GM_Training/ADVANCED_MODEL_PREP_QA_PROTOCOL.md)：备团资料交接、独立挑错、修订与验收。
- [专业能力迁移机制](CAPABILITY_TRANSFER.md)：从 TRPG 实战中提取可跨场景验证的通用能力。

## 工作流程
1. 确认当前桌面的 system_id 与规则版本；按 SYSTEM_CONTEXT_PROTOCOL 只加载该系统的权威资料。
2. 读取对应 Campaign / Module 的资料，建立设定基石、可调用素材、调查链与 NPC/环境因果账本。
3. 按风险与复杂度执行第二轮 Prep QA；复杂、扩写多或调查链较长的模组，默认建议交由高能力模型独立挑错。
4. 修订并记录 QA 结果，生成 Runtime Quick Reference 与 Prep-to-Runtime Handoff。
5. 每次新对话/新 Session 独立执行 Preflight；运行后维护状态并复盘。

## 信息边界与版权
- GM-only 文件包含秘密、答案或剧透，不得作为玩家资料发送。
- 本仓库公开，任何人均可读取；其中战役人物卡与记录亦为公开资料。
- 第三方受版权保护规则书、模组全文及完整翻译文本不在本仓库分发；仅保留合法来源索引与说明。
- 原私人仓库保留非 TRPG 私人资料及《The Vault》中文全文备份；TRPG 专业资料的唯一工作主仓库为本仓库。

## 维护约定
- 不静默覆盖已确立的战役事实；更正时记录原因与影响。
- 历史版本保留其历史语境，不把旧文件自动视为当前运行指令。
- 通用能力改进须有实战证据；未经跨场景验证的经验先作为候选，不直接写入凯西核心规范。
- 公开仓库不得提交凭证、密钥、私人真实身份资料或未经授权的第三方全文。