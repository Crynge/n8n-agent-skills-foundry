# AI Patterns

## Current n8n AI surfaces

- AI Agent and tool sub-nodes
- Chat Trigger
- AI Transform
- Guardrails
- Evaluation and Evaluation Trigger
- MCP Client Tool
- memory nodes such as Redis, Postgres, Xata, and Zep variants when available in the environment

## Architecture choices

- deterministic chain when the answer path is known
- agent when tool routing and recovery need autonomy
- retrieval-first when grounding matters more than freeform reasoning

## Safety checks

- tool approval boundary
- context truncation policy
- model timeout and fallback
- evaluation dataset availability

