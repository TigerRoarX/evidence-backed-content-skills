# Scope and assumptions / 范围与假设

Question: What can be verified about Qoder's publicly documented product changes from 2026-08-16 through 2026-09-16, and how should those changes be written for developers?

问题：2026 年 8 月 16 日至 9 月 16 日，Qoder 公开资料里有哪些可以核验的产品变化，面向开发者写作时应该如何表达？

Audience: Developers and technical readers who want a concise product-change brief, not an adoption survey or a performance benchmark.

受众：希望快速了解产品变化的开发者和技术读者，不做采用情况调查，也不做性能基准测试。

Evidence boundary: The supplied screenshots are research leads. Their monthly counts, version totals, Credits figures, and summary wording are not treated as verified until each item has a public source. The verified section below uses Qoder's public homepage and Chinese changelog, accessed 2026-09-18.

# Executive answer / 核心答案

Qoder's public homepage positions it as an AI programming platform with intelligent code completion, conversational programming, and automatic code generation, with support for mainstream IDEs including VS Code and JetBrains [S1]. Its official Chinese changelog records concrete updates during the window, including file-opening preferences, real-time voice stability, file-review resource improvements, MCP gateway and Chinese-tool support, and several Agent or workflow refinements [S2][S3][S4].

这些资料足以写一篇“产品最近在往哪些开发工作流靠近”的资料型文章。它们不足以证明代码质量、速度、稳定性、Credits 消耗是否优于其他工具，也不足以支撑截图里未经逐项核验的版本数量或月度汇总。

# Verified findings / 已核验事实

- Qoder describes itself as an AI programming platform offering intelligent code completion, AI conversational programming, and automatic code generation; its homepage says it supports mainstream IDEs such as VS Code and JetBrains [S1].
  Qoder 官网将产品描述为提供智能代码补全、AI 对话式编程和自动代码生成的 AI 编程平台，并称支持 VS Code、JetBrains 等主流 IDE [S1]。
- The official changelog is organized across Qoder IDE, JetBrains plugin, CLI, and QoderWork updates [S2].
  官方更新日志覆盖 Qoder IDE、JetBrains 插件、CLI 和 QoderWork [S2]。
- The 2026-09-12 entry for version 0.2.5 lists file-opening preferences, improved real-time voice stability, lower CPU use when reviewing files with multiple diffs and a terminal open, and profile-page Credits and activity data [S3].
  2026 年 9 月 12 日的 0.2.5 更新记录了文件打开方式选择、实时语音稳定性提升、同时展开多个代码差异并打开终端时降低 CPU 占用，以及个人资料页新增 Credits 与活跃数据 [S3]。
- The 2026-09-12 entry for version 1.1.51 lists connecting MCP services through the Qoder MCP gateway and recognizing Chinese MCP tools [S4].
  2026 年 9 月 12 日的 1.1.51 更新记录了通过 Qoder MCP 网关接入 MCP 服务，以及识别和使用中文 MCP 工具 [S4]。
- The 2026-09-16 entry for version 1.30.1 lists improvements to long-conversation UI performance, Agent preparation, first-response timeout messaging, and WSL startup speed and connection stability [S5].
  2026 年 9 月 16 日的 1.30.1 更新记录了长对话界面性能、Agent 响应前准备流程、首包超时提示，以及 WSL 启动速度和连接稳定性的改进 [S5]。

# Reasonable inferences / 合理推断

- The selected entries suggest that recent Qoder updates are moving beyond code generation into the surrounding development workflow: context and agent preparation, tool connectivity, file review, terminal use, and remote development support. This is a synthesis of the cited entries, not a claim about the complete release history.
  从这些条目可以推断，近期更新不只围绕代码生成，也在补齐上下文与 Agent 准备、工具接入、文件审阅、终端使用和远程开发等周边流程。这是对所引条目的归纳，不代表完整更新历史。
- A useful developer article should describe the change by workflow impact, then state what still needs hands-on verification. A changelog can show what was released; it cannot show whether the change works reliably for a particular project.
  面向开发者的文章可以先按工作流影响来写，再说明哪些结论需要上手验证。更新日志能说明发布了什么，不能直接说明它在某个项目里是否稳定有效。

# Unknown or needs confirmation / 未知或待确认

- The screenshots' claims about the number of releases in the month, total downloads or users, Credits amounts, and an overall “main change” are not independently verified in this pack.
- No comparison of speed, coding accuracy, model quality, pricing, quota, or developer productivity is supported by these sources.
- The changelog is a first-party record. Independent user reports or a reproducible task log would be needed to assess actual experience.

# Source ledger / 来源台账

| ID | Title | Publisher | Date | URL | Relevant passage | Evidence |
|---|---|---|---|---|---|---|
| S1 | Qoder - AI Coding Assistant | Qoder | accessed 2026-09-18 | https://qoder.com | Product description covering code completion, conversational programming, automatic code generation, VS Code, and JetBrains | Direct official product page |
| S2 | Qoder 更新日志 | Qoder | accessed 2026-09-18 | https://qoder.com/zh/changelog | Official changelog description covering IDE, JetBrains plugin, CLI, and QoderWork | Direct official changelog |
| S3 | 日常优化 / version 0.2.5 | Qoder | 2026-09-12 | https://qoder.com/zh/changelog?version=0.2.5 | File opening, real-time voice, file review CPU use, Credits and activity data | Direct official release entry |
| S4 | 增强 MCP 接入与中文工具支持 / version 1.1.51 | Qoder | 2026-09-12 | https://qoder.com/zh/changelog?version=1.1.51 | Qoder MCP gateway and Chinese MCP tools | Direct official release entry |
| S5 | 日常优化 / version 1.30.1 | Qoder | 2026-09-16 | https://qoder.com/zh/changelog?version=1.30.1 | Long-conversation UI, Agent preparation, timeout messaging, and WSL improvements | Direct official release entry |

# Editorial note / 编辑说明

The supplied screenshots can remain as private research references. They should not be uploaded to the public repository unless their provenance and redistribution rights are clear. This example keeps only the public URLs and the claims that can be audited from them.
