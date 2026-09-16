# 小红书示例

## 标题

Skill 不是一段提示词，而是一套可复用工作流

## 正文

最近在整理 Agent Skill，发现最容易踩的坑是把它写成一大段万能提示词。

更稳的结构是：

1. `SKILL.md`：触发条件、输入、流程、输出
2. `scripts/`：需要稳定执行的自动化脚本
3. `references/`：只在特定场景读取的资料
4. `assets/`：模板、图片或其他交付资源

Agent 会先看名称和描述，匹配任务后再加载完整指令。这样既方便复用，也不会一开始就占满上下文。[S1]

重点不是把 Skill 写得越长越好，而是把边界和验收标准写清楚。

来源：[S1] https://learn.chatgpt.com/docs/build-skills

## 视觉 brief

做一张中文信息卡：左侧是 `SKILL.md`，右侧是 scripts、references、assets，底部用一条渐进加载箭头连接。所有文字使用中文，示例代码保留英文文件名。
