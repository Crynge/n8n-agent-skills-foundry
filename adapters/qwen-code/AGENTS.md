# Qwen Code n8n Adapter

Use the canonical skill folders in `skills/` as the authoritative guidance for n8n work.

## Routing

- `n8n-mcp-toolsmith` for MCP
- `n8n-workflow-architect` for topology
- `n8n-validation-repair` for failures
- `n8n-ai-builder` plus `n8n-evals-guardrails` for agentic flows
- `n8n-community-node-author` for custom nodes and verified publishing

## Operating rules

- validate node configs before validating whole workflows
- call out editor-vs-production behavior differences
- surface risk around credentials, loops, binary data, and published versions

