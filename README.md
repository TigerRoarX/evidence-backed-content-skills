# 有证据链的中文内容 Skills

作者：[@TigerRoarX](https://github.com/TigerRoarX)

这是一套面向中文创作者的内容工作流，兼容 Codex、Claude Code 以及其他支持 Agent Skills 标准的运行环境。

它专门解决内容自动化里最容易被忽略的部分：让每条重要结论都能追溯到来源，把事实和推断分开，并在发布前发现引用、隐私和版权风险。

## 包含的 Skills

- **research-with-sources**：建立带来源台账、可复核的研究包。
- **content-remix**：把已确认的研究包改写成公众号、小红书、X、知乎或 Newsletter 内容，不新增无依据的结论。
- **publish-quality-check**：在发布前检查证据、时效、署名、隐私、版权、安全和平台格式风险。

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
研究 2026 年中国 AI 编程工具的团队采用情况。限定中国市场，优先官方资料和公开调研，输出来源台账，并把事实、推断和未知分开。
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

## 作者与协议

作者：TigerRoarX。项目采用 MIT 协议，见 [LICENSE](LICENSE)。
