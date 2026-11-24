# PR #3 修复回归

在仓库根目录运行以下命令。依赖 Python 3.12、PyYAML、Node.js 与 npm。Markdown 解析器 `marked` 固定为仓库内随附的 4.0.19（MIT License），通过 `package.json` 的本地 file dependency 和 `package-lock.json` 锁定；无需访问 npm registry。首次安装或依赖变更后执行 `npm ci --ignore-scripts --offline`。在提交或暂存所有待核 Markdown 后运行，链接扫描以 Git 索引的文件集合为准。

```sh
npm ci --ignore-scripts --offline
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check 6c6109202d92d7bbacd638d5aa37d00418262d2b..HEAD
```

`RepositoryChecks` 检查实际绑定、规则范围、CLOSED、算术、导航和正文约束。`ReferenceExercises` 是合成资料的测试适配器，使用实际临时文件读写和独立 Python 进程。它没有连接 Workbench 的生产运行入口，也没有替代目标 Chat。T0 和跨系统交互中的参考响应为确定性测试值，实际模型行为须另行实测。

半提交复测使用修订 1、余额 7 和同一 +3 合成事件，分别在只写入 Log、只写入 Runtime、发布成功但回执丢失时退出，随后重新读取、补缺项和重试。独立检查最终余额、实际补写次数及接收者篡改后的争议状态。玩家投影测试核对两个独立输出的最终字节，另测试含受限附录及无法读回的负例。
