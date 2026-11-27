# 规则系统目录

本目录保存每套 TRPG 规则系统的独立知识环境。每个 system_id 有唯一规范入口。按下列登记表提供的精确路径加载。目录名与 ID 独立。

## 当前系统

- [Triangle Agency / 三角机构](./Triangle_Agency/README.md) — `system_id: triangle_agency`；当前正式实战规则版本为用户指定的中文 v22。

```yaml
systems:
  - system_id: triangle_agency
    system_entry: Systems/Triangle_Agency/README.md
    ruleset_versions: ["中文 v22"]
    status: active
```

## 跨系统规则运行集成

- [System Rule Runtime Integration Protocol](./SYSTEM_RULE_RUNTIME_INTEGRATION_PROTOCOL.md)：跨系统共享的规则运行集成契约。它只规定系统规则如何按触发进入运行、如何连接资源与世界状态，不包含任何具体游戏机制。

## 接入约定

每个系统目录必须有 README，记录正式名称、system_id、规则版本、权威来源、状态、规则索引、专属 Skill 与适配边界。

系统之间完全隔离。研究某系统不代表它已被当前战役采用；运行某个 Campaign 时，以其 SYSTEM_BINDING 文件为准。不要仅凭仓库默认系统、用户过去玩过的系统或常见 TRPG 习惯推断当前系统。

通用 GM 能力统一维护在 `GM_Training/`。系统规则、术语、裁定和专属研究只维护在登记的对应系统目录，不复制到通用 Skill。
