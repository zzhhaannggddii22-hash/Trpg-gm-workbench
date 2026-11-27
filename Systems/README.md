# 规则系统目录

本目录保存每套 TRPG 规则系统的独立知识环境。每个 system_id 有唯一规范入口。按下列登记表提供的精确路径加载。目录名与 ID 独立。

## 当前系统

- [Triangle Agency / 三角机构](./Triangle_Agency/README.md) — `system_id: triangle_agency`；当前正式实战规则版本为用户指定的中文 v22。
- [Cairn /《石冢》](./Cairn/README.md) — `system_id: cairn`；Cairn Second Edition；第二套系统接入准备中，当前为 candidate，尚未开放正式运行。

```yaml
systems:
  - system_id: triangle_agency
    system_entry: Systems/Triangle_Agency/README.md
    ruleset_versions: ["中文 v22"]
    status: active
  - system_id: cairn
    system_entry: Systems/Cairn/README.md
    ruleset_versions: ["Cairn Second Edition"]
    status: candidate
```

## 接入约定

每个系统目录必须有 README，记录正式名称、system_id、规则版本、权威来源、状态、规则索引、专属 Skill 与适配边界。

系统之间完全隔离。研究某系统不代表它已被当前战役采用；运行某个 Campaign 时，以其 SYSTEM_BINDING 文件为准。不要仅凭仓库默认系统、用户过去玩过的系统或常见 TRPG 习惯推断当前系统。

通用 GM 能力统一维护在 `GM_Training/`。系统规则、术语、裁定和专属研究只维护在登记的对应系统目录，不复制到通用 Skill。

## Cairn 接入状态

Cairn 已建立独立系统入口、初步规则索引、专属 GM Skill 草案、Preflight 草案与初步研究。状态保持 candidate，直至官方规则核验、正反例测试、跨系统隔离测试及 1–2 次短团实测完成。详见 [Cairn 接入研究](./Cairn/Research/INITIAL_RESEARCH.md)。
