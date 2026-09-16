# TigerRoarX 的内容创作 Skills

一套从资料研究到多平台发布前质检的内容创作工作流。

当前版本：`v0.2.3`

这是一套面向中文创作者的内容工作流，兼容 Codex、Claude Code 以及其他支持 Agent Skills 标准的运行环境。

它专门解决内容自动化里最容易被忽略的部分：让每条重要结论都能追溯到来源，把事实和推断分开，并在发布前发现引用、隐私和版权风险。

## 包含的 Skills

- **research-with-sources**：建立带来源台账、可复核的研究包。
- **content-remix**：把已确认的研究包改写成公众号、小红书、X、知乎或 Newsletter 内容，不新增无依据的结论。
- **publish-quality-check**：在发布前检查证据、时效、署名、隐私、版权、安全和平台格式风险。

## 完整案例

见 [`examples/official-skills-research`](examples/official-skills-research) 和 [`examples/cursor-developer-experience`](examples/cursor-developer-experience)，均包含研究包、平台稿和发布前质检报告；后者还附有可复现的任务记录。

## 安装

仓库地址：<https://github.com/TigerRoarX/evidence-backed-content-skills>

安装：

```bash
npx skills add TigerRoarX/evidence-backed-content-skills
```

在 Claude Code 中注册插件市场：

```text
/plugin marketplace add TigerRoarX/evidence-backed-content-skills
```

在 Codex 中可以直接安装 Skill 目录，或把仓库作为 Plugin 使用。官方说明见 <https://learn.chatgpt.com/docs/build-skills>。

## 示例

```text
$research-with-sources
我准备写一篇面向开发者的 AI 编程工具体验文章。请基于公开资料整理主流工具的功能、适用人群和上手成本，标注来源，并把事实、体验判断和待确认信息分开。
```

```text
$content-remix
把这份研究包改成一篇公众号稿和一组小红书卡片文案，不新增没有来源支持的数字。
```

```text
$publish-quality-check
在发布前审查这份稿件，按 Blocker、Warning、Pass 列出问题，不要静默改写事实。
```

## 本地校验

```bash
python scripts/check_research_pack.py path/to/research-pack.md
```

校验脚本只检查研究包的最小结构，不替代编辑判断和来源核验。

## 设计原则

- 优先使用一手来源，二手来源用于发现线索和交叉验证。
- 每条重要结论都要有来源标记，或明确标注不确定性。
- 网页和文档里的文字是待分析内容，不是给 Agent 执行的指令。
- 研究、写作和发布分开，默认不执行外部发布动作。
- 平台文案可以缩短引用，但完整来源台账必须保留。

## 维护与协议

维护：[@TigerRoarX](https://github.com/TigerRoarX)。项目采用 MIT 协议，见 [LICENSE](LICENSE)。
