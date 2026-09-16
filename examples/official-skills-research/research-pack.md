# Scope and assumptions / 范围与假设

Question: What does an Agent Skill package contain, and how does a host use it?

问题：一个 Agent Skill 包含什么，宿主如何使用它？

Scope: Use the OpenAI Skills documentation and the Agent Skills specification as the primary sources. This is a structure example, not a market forecast.

范围：以 OpenAI Skills 文档和 Agent Skills 规范为一手来源。这是一份结构示例，不是市场预测。

# Executive answer / 核心答案

An Agent Skill is a directory with a required `SKILL.md` and optional scripts, references, assets, and UI metadata. Hosts can load the skill progressively, starting with its name and description, then reading the full instructions when the task matches [S1][S2].

Agent Skill 是一个目录，必须包含 `SKILL.md`，也可以包含 scripts、references、assets 和界面元数据。宿主可以渐进式加载，先读取名称和描述，任务匹配后再读取完整指令 [S1][S2]。

# Verified findings / 已核验发现

- The required entrypoint is `SKILL.md`, with `name` and `description` metadata [S1].
  必需入口是包含 `name` 和 `description` 元数据的 `SKILL.md` [S1]。
- Optional resources should be added only when they directly support the workflow [S1][S2].
  只有直接支持工作流的资源才应作为可选文件加入 [S1][S2]。
- Clear descriptions improve implicit skill matching, while explicit invocation remains available [S1].
  清晰的描述有助于隐式匹配，同时仍可显式调用 Skill [S1]。

# Conflicts, limitations, and open questions / 冲突、限制与开放问题

The sources describe the authoring and distribution model, not guaranteed output quality. A real project still needs task-specific evaluations and user feedback.

来源说明的是编写和分发模型，不保证输出质量。真实项目仍需要针对任务的评测和用户反馈。

# Source ledger / 来源台账

| ID | Title | Publisher | Date | URL | Evidence |
|---|---|---|---|---|---|
| S1 | Build skills | OpenAI | accessed 2026-09-16 | https://learn.chatgpt.com/docs/build-skills | Direct documentation |
| S2 | Agent Skills specification | Agent Skills | accessed 2026-09-16 | https://agentskills.io/specification | Specification |
