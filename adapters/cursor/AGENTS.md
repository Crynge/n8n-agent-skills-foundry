# Cursor n8n Adapter

When the task involves n8n:

- route first to `n8n-mcp-toolsmith` for any MCP interaction
- route to `n8n-workflow-architect` before building new workflows
- route to `n8n-validation-repair` when validation or runtime mismatches appear
- route to `n8n-ai-builder` and `n8n-evals-guardrails` for AI workflows
- route to `n8n-source-control-release` for deployment or Git-backed promotion work

Always prefer native n8n nodes before HTTP Request unless the native node is missing, immature for the target operation, or introduces credential/auth friction that the HTTP path avoids.

