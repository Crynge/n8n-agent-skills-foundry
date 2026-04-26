# Qwen Code Installation

Qwen Code does not have a standardized universal skill folder equivalent across all deployments, so this repo provides a prompt-pack adapter.

## Install

1. Keep the `skills/` folder in the repo.
2. Use `adapters/qwen-code/AGENTS.md` as the top-level instruction pack.
3. Reference individual skill names in your session bootstrap prompt when working on n8n tasks.

## Suggested bootstrap

Tell Qwen Code to:

- consult `n8n-mcp-toolsmith` before MCP use
- apply `n8n-validation-repair` when validation fails
- apply `n8n-ai-builder` plus `n8n-evals-guardrails` for AI workflows

