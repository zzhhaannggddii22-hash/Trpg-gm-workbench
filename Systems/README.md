# 规则系统目录

本目录保存每套 TRPG 规则系统的独立知识环境。每个子目录以唯一 system_id 命名。

## 当前系统

- [Triangle Agency / 三角机构](./Triangle_Agency/README.md) — `system_id: triangle_agency`；当前正式实战规则版本为用户指定的中文 v22。

## 接入约定

每个系统目录必须有 README，记录正式名称、system_id、规则版本、权威来源、状态、规则索引、专属 Skill 与适配边界。

系统之间完全隔离。研究某系统不代表它已被当前战役采用；运行某个 Campaign 时，以其 SYSTEM_BINDING 文件为准。不要仅凭仓库默认系统、用户过去玩过的系统或常见 TRPG 习惯推断当前系统。

通用 GM 能力统一维护在 `GM_Training/`。系统规则、术语、裁定和专属研究只维护在对应 `Systems/<system_id>/`，不复制到通用 Skill。
