# n8n Agent Skills Foundry

Advanced n8n skill packs and platform adapters for **Claude Code**, **Cursor**, **Qwen Code**, and **MiniMax**.

This repository is a broader, more operational follow-up to [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills). It keeps the strong foundations of expression syntax, MCP tool usage, workflow patterns, validation, and Code node guidance, then expands into:

- current n8n AI and MCP surfaces
- latest core-node areas such as `AI Transform`, `Data Table`, `Evaluation`, `Evaluation Trigger`, `Guardrails`, `MCP Client`, `MCP Server Trigger`, `Execution Data`, and `Local File Trigger`
- enterprise operations like source control, external secrets, log streaming, and insights
- deployment and release engineering for verified community nodes
- multi-agent adapter packs so one knowledge base works across multiple coding assistants

## Why this repo exists

The reference repo is useful, but it is intentionally Claude-first and compact. This repo is designed for teams that want:

- more than seven skills
- deep reference packs behind each skill
- more than one assistant runtime
- deeper AI workflow coverage
- better operational guidance
- current n8n capability coverage
- CI, validation, and machine-readable catalogs

## What the audit found

The audit is documented in [docs/audit-reference-repo.md](./docs/audit-reference-repo.md). The short version:

- The reference repo is narrowly centered on 7 Claude Code skills.
- It does not provide first-class adapters for Cursor, Qwen Code, or MiniMax.
- It does not cover several current n8n surfaces reflected in official docs, including `AI Transform`, `Data Table`, `Evaluation`, `Evaluation Trigger`, `Guardrails`, `MCP Client`, and `MCP Server Trigger`.
- It has no visible GitHub Actions workflow layer, despite modern n8n community-node verification now requiring GitHub Actions provenance for verified publishing.
- It has limited operational material for source control, release engineering, external secrets, log streaming, insights, and enterprise governance.

## Skill Packs

This repository ships 27 canonical skills:

1. `n8n-mcp-toolsmith`
2. `n8n-expression-engine`
3. `n8n-workflow-architect`
4. `n8n-validation-repair`
5. `n8n-node-configurator`
6. `n8n-code-javascript`
7. `n8n-code-python`
8. `n8n-webhooks-api`
9. `n8n-data-flow-ops`
10. `n8n-ai-builder`
11. `n8n-evals-guardrails`
12. `n8n-credentials-security`
13. `n8n-observability-debug`
14. `n8n-source-control-release`
15. `n8n-community-node-author`
16. `n8n-integration-selector`
17. `n8n-triggers-scheduling`
18. `n8n-databases-sql`
19. `n8n-files-binary`
20. `n8n-subworkflow-orchestration`
21. `n8n-queue-scale`
22. `n8n-enterprise-admin`
23. `n8n-forms-chat-ux`
24. `n8n-testing-fixtures`
25. `n8n-data-tables`
26. `n8n-version-migration`
27. `n8n-error-handling-retries`

Each skill now ships with a `references/` pack for deeper operational and technical guidance.

## Platform Adapters

- [Claude Code](./docs/installation/claude-code.md)
- [Cursor](./docs/installation/cursor.md)
- [Qwen Code](./docs/installation/qwen-code.md)
- [MiniMax](./docs/installation/minimax.md)
- [Compatibility Matrix](./docs/compatibility-matrix.md)
- [Skill Coverage Matrix](./docs/skill-coverage-matrix.md)
- [Hyper-Technical Runbooks](./docs/hyper-technical-runbooks.md)

The canonical skill content lives under `skills/`. Platform adapter folders translate that content into the conventions of each environment.

## Latest n8n surface area captured here

This repo intentionally reflects current official docs around:

- advanced AI workflows and LangChain-style clusters
- light evaluations and evaluation triggers
- current core node surface including `AI Transform`, `Data Table`, `Guardrails`, `Execution Data`, `MCP Client`, and `MCP Server Trigger`
- source control and environments
- external secrets
- log streaming
- insights
- verified community node publishing via GitHub Actions provenance

See [docs/latest-n8n-surface.md](./docs/latest-n8n-surface.md) for the source-backed map.

## Repository layout

```text
skills/                       Canonical n8n skill packs
adapters/                     Assistant-specific adapter packs
docs/                         Audit, installation, architecture, capability map
data/integration-catalog.json Curated integration catalog
scripts/                      Linting, catalog build, smoke checks
tests/                        Repository-level tests
.github/workflows/            CI and catalog workflows
```

## Local validation

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/lint_skills.py
python scripts/build_catalog.py
python scripts/smoke_check.py
python -m pytest -q
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python .\scripts\lint_skills.py
python .\scripts\build_catalog.py
python .\scripts\smoke_check.py
python -m pytest -q
```

## Audience

- AI agents that build or audit n8n workflows
- teams standardizing how coding assistants touch n8n
- maintainers of internal automation platforms
- authors of verified community nodes
- AI workflow engineers operating production n8n systems
