# n8n Agent Skills Foundry

Use this repository when the task involves building, auditing, repairing, reviewing, or operationalizing n8n workflows and nodes across Claude Code, Cursor, Qwen Code, or MiniMax.

## Routing

- Use `skills/n8n-mcp-toolsmith` before any n8n MCP operation.
- Use `skills/n8n-validation-repair` whenever validation fails or a workflow behaves differently at runtime than in the editor.
- Use `skills/n8n-workflow-architect` before designing a new workflow topology.
- Use `skills/n8n-node-configurator` when selecting operations or hidden parameters on nodes.
- Use `skills/n8n-expression-engine`, `skills/n8n-code-javascript`, or `skills/n8n-code-python` when the workflow includes expressions or Code nodes.
- Use `skills/n8n-ai-builder`, `skills/n8n-evals-guardrails`, and `skills/n8n-observability-debug` together for AI workflows.
- Use `skills/n8n-source-control-release` and `skills/n8n-community-node-author` for deployment, packaging, or verified-node work.

## Guardrails

- Prefer built-in nodes before community nodes unless a community node clearly reduces complexity.
- Validate node config before validating the whole workflow.
- Treat credentials, binary data, loop boundaries, execution mode, and item linking as first-class risks.
- Distinguish editor-time success from production-time success. Account for published versions, triggers, concurrency, and retries.
- For AI workflows, require evaluation datasets, approval points for side-effecting tools, and a fallback path.

