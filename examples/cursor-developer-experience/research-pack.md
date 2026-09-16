# Scope and assumptions / 范围与假设

Question: How can an AI coding tool experience article describe a developer workflow without turning product documentation into unsupported claims?

问题：面向开发者写 AI 编程工具体验文章时，如何描述工作流，又不把产品文档写成未经验证的结论？

Scope: Use Cursor's public official documentation as the source set. This is a writing example based on documented capabilities, not a hands-on benchmark, pricing comparison, or adoption survey.

范围：只使用 Cursor 官方公开文档。这是一份基于文档能力说明的写作示例，不是上手实测、价格横评或采用情况调查。

Access date: 2026-09-16.

# Executive answer / 核心答案

Cursor's documentation presents Agent as an assistant for autonomous coding tasks, terminal commands, and code editing [S1]. Its documentation hub groups the product around Agent mode, Rules, Skills, MCP servers, CLI, models, and team or enterprise setup [S2].

对开发者文章来说，更稳妥的写法是把这些能力放回一个具体工作流里，再把“文档确认的能力”和“需要实际体验后才能下的判断”分开。

# Verified findings / 已核验发现

- The Agent overview describes Cursor as an assistant for autonomous coding tasks, terminal commands, and code editing [S1].
  Agent 概览页将 Cursor 描述为可用于自主编码任务、终端命令和代码编辑的助手 [S1]。
- Cursor's documentation hub explicitly lists Agent mode, Rules, Skills, MCP servers, CLI, models, and Teams & Enterprise setup as documentation areas [S2].
  Cursor 文档首页明确列出 Agent mode、Rules、Skills、MCP servers、CLI、models 以及 Teams & Enterprise 等文档板块 [S2]。

# Reasonable inferences / 合理推断

- An experience article can use “提出任务—查看上下文—执行修改—运行命令—人工复核” as its narrative frame. This is an editorial structure, not a claim that every task is autonomous or error-free.
  体验文章可以用“提出任务—查看上下文—执行修改—运行命令—人工复核”组织叙事。这是写作结构，不代表所有任务都能自动完成或一次成功。
- A useful review should report the concrete task, the edits suggested, the commands actually run, and the review work left to the developer. Those details require a real hands-on session before publication.
  真正有价值的体验稿还应记录具体任务、建议修改、实际执行的命令，以及开发者仍需完成的复核工作。这些细节需要真实上手后再补充。

# Unknown or needs confirmation / 未知或待确认

- Coding accuracy, latency, model quality, pricing, quota limits, and failure rates are not established by these pages.
- No claim about personal productivity or team adoption should be made without a reproducible hands-on test and a defined sample.

# Suggested editorial angle / 建议写法

Use a small bug-fix or refactor as the article's example task. Mark any observed result as a hands-on observation, and keep the official capability description tied to [S1] or [S2].

# Source ledger / 来源台账

| ID | Title | Publisher | Date | URL | Relevant passage | Evidence |
|---|---|---|---|---|---|---|
| S1 | Overview | Cursor | accessed 2026-09-16 | https://cursor.com/docs/agent | “Assistant for autonomous coding tasks, terminal commands, and code editing” | Direct official documentation |
| S2 | Cursor Docs — Agent, Rules, MCP, Skills & CLI | Cursor | accessed 2026-09-16 | https://cursor.com/docs | The documentation hub lists Agent mode, Rules, Skills, MCP servers, CLI, models, and Teams & Enterprise setup | Direct official documentation |
