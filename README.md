# Evidence-backed Content Skills

Source-aware research and content workflows for Codex, Claude Code, and other Agent Skills-compatible runtimes.

This project focuses on the part most content automations skip: keeping claims traceable from source to final draft, separating facts from inferences, and catching publication risks before anything is sent.

## Included skills

- **research-with-sources**: build an audit-ready research pack with a source ledger.
- **content-remix**: adapt an approved pack for WeChat, Xiaohongshu, X, Zhihu, or a newsletter without adding unsupported claims.
- **publish-quality-check**: preflight evidence, freshness, attribution, privacy, copyright, safety, and platform-fit risks.

## Install

After this repository is published, install the skills with:

```bash
npx skills add <github-owner>/evidence-backed-content-skills
```

For Claude Code plugin discovery:

```text
/plugin marketplace add <github-owner>/evidence-backed-content-skills
```

For Codex, install the skill folder locally or package the repository as a plugin. The official guidance is at <https://learn.chatgpt.com/docs/build-skills>.

## Example prompts

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

## Local validation

```bash
python scripts/check_research_pack.py path/to/research-pack.md
```

The validator checks the minimum research-pack contract. It does not replace editorial judgment or source verification.

## Design principles

- Primary sources first; secondary sources for discovery and triangulation.
- Every material claim gets a source marker or an explicit uncertainty label.
- Source text is untrusted content, never an instruction to execute.
- Research and drafting are separate from publishing and other external side effects.
- Keep the full source ledger even when a platform format needs a shorter citation.

## License

MIT. See [LICENSE](LICENSE).
