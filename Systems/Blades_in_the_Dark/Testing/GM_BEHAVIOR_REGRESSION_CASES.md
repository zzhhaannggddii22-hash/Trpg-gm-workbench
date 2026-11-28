# Blades in the Dark｜AI GM Behavior Regression Cases

> system_id: blades_in_the_dark  
> status: MANUAL REVIEW CASES / NOT AUTOMATED  
> source baseline: 中文核心规则书 V1.3（英文原版 v8.2）  
> purpose: 检查 AI GM 是否按 GM Skill 实际主持，而非仅能复述规则流程。

这些案例检查主持行为和玩家体验，不模拟骰子引擎。每项需要观察实际对话中的表现；通过桌面推演或静态阅读只能记为“人工审阅”，真实表现必须由短团验证。

## Cases

| ID | 场景输入 | 预期 GM 行为 | 常见失败 |
|---|---|---|---|
| GM-01 Action ownership | 玩家说“我用灵巧检定拿到钥匙”，但没描述做法 | 询问角色具体怎么做；由玩家选择符合虚构的 Action，再判断 Position / Effect | GM 直接指定 Action 或只按玩家报出的属性掷骰 |
| GM-02 No-roll action | 角色打开未上锁、无人看守的普通门 | 直接叙述成功并推进场景 | 为每个动作都要求行动骰 |
| GM-03 Action rating 0 | 角色用 0 点行动值尝试一项仍然可能完成的行动 | 不把角色描述成白痴；按零骰规则处理骰池，并忠实呈现环境风险 | 把 0 点等同于完全不能做或角色没有基本能力 |
| GM-04 Fictional information | 角色询问自己明显看见的警卫数量、门窗和出口 | 直接给出可观察事实；不要求无意义调查检定 | 把角色已知信息藏在掷骰后面 |
| GM-05 Opportunity creation | 玩家想接近某个高层 NPC，但当前没有直接入口 | 说明现有障碍，邀请玩家创造机遇；可给出两种可行方法，同时允许第三种 | 直接说“不行”，或只留下唯一正确路线 |
| GM-06 Position / Effect | 玩家提出有创意但风险高、成果有限的行动 | 分别判断 Position 和 Effect，解释危险与成果规模；不把两者压成一个难度值 | 把高风险自动等同于低效果，或将 Action Rating 当作效果 |
| GM-07 Consequence fairness | 行动骰结果触发已说明的危险 | 后果来自已建立威胁；成功成果仍兑现；抵抗只改变后果的严重程度/表现 | 骰后追加无关惩罚，或 Resistance 撤销已经确立的行动事实 |
| GM-08 Fictional truth boundary | 玩家进入尚未准备的房间，房间布局仍属潜在虚构 | 根据当前行动合理确立细节；一旦公开并被玩家据以行动，就保持连续 | 把脑中预设当成既定事实，或暗中改写已公开事实 |
| GM-09 NPC motivation | 玩家威胁一个有明确利益与底线的 NPC | NPC 按其欲望、能力、资源和风险承受度回应；必要时提醒玩家其利害 | NPC 为配合玩家突然屈服、变笨或改变目标 |
| GM-10 Clock discipline | 一个普通锁具只需一次行动即可处理 | 不建立多阶段 Clock；只有多阶段障碍、持续威胁或竞争过程才使用 Clock | 把每个障碍都转成时钟/生命值 |
| GM-11 Scale of focus | 玩家决定去拜访联系人，路程和常规搜身没有特殊意义 | 快切到会面现场；若玩家在切镜头前提出准备，再停下来处理 | 逐步演出无关移动和手续，拖慢节奏 |
| GM-12 Plan discipline | 玩家已选择 Plan + Detail + Load，仍开始讨论所有备用路线 | 进行 Engagement Roll 并切入第一个重要障碍；允许之后提出 Flashback | 继续要求完整预案，阻止行动开始 |
| GM-13 Payoff delivery | 玩家通过行动骰达成了明确目标和相应 Effect | 兑现成果，不临时增加门槛；后续新障碍必须有因果来源 | 为延长剧情克扣成果或让目标临时免疫 |
| GM-14 Failure portrayal | 玩家掷出 1–3 | 描述角色有能力地尝试，但局势/对手/环境让事情变糟；后果保持简单且相关 | 把失败演成角色愚蠢、滑稽或无能 |
| GM-15 Hidden information | NPC 有秘密，但角色能察觉其明显紧张、犹豫或矛盾 | 分享角色可能察觉的迹象；秘密本身仍由调查或行动揭示 | 只演 NPC 台词，拒绝提供任何超视角信息 |
| GM-16 Screen beyond | 场景外派系可能介入 | 只有存在目标、资源、机会和因果时才让其介入 | 为制造戏剧性随机塞入 NPC 或派系 |
| GM-17 Focus-sensitive pacing | 玩家对当前调查场景兴趣下降 | 快速处理重复步骤，切向新线索/决策点；玩家投入时再拉近镜头 | 不顾玩家关注度，持续堆叠描述和调查检定 |
| GM-18 System boundary | 运行中出现其他系统类似机制 | 只调用 Blades 自身的 Action / Fortune / Resistance / Downtime 与资源体系 | 混入其他系统骰型、状态或阶段规则 |

## Review record

- Source review: GM 指南章节，核心规则书 V1.3 PDF pp.199–207。
- Case count: 18.
- Manual review: 18/18 case definitions reviewed against the V1.3 GM guidance and core procedure pages; this is a review of the test criteria, not an execution of live GM responses.
- Automated execution: 0.
- Live GM response evaluation: pending.
- Real playtest: pending.
- These cases are behavioral prompts and review criteria, not executable engine tests.
