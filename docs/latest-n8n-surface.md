# Latest n8n Surface Map

This repository is aligned to current official documentation as of **April 27, 2026**.

## Core node and workflow surface

Official docs list current core nodes and related areas including:

- `AI Transform`
- `Data Table`
- `Evaluation`
- `Evaluation Trigger`
- `Execution Data`
- `Guardrails`
- `MCP Client`
- `MCP Server Trigger`
- `Local File Trigger`
- `Chat Trigger`
- `Execute Sub-workflow`

Source: [n8n integrations docs](https://docs.n8n.io/integrations/)

## AI workflow surface

Official AI docs describe:

- advanced AI workflows
- cluster-node based AI architecture
- agents vs chains
- memory options such as Simple Memory, Redis Chat Memory, Postgres Chat Memory, Xata, and Zep
- human-in-the-loop tool approvals
- evaluations

Sources:

- [Advanced AI](https://docs.n8n.io/advanced-ai/)
- [LangChain in n8n](https://docs.n8n.io/advanced-ai/langchain/overview/)
- [Light evaluations](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/)
- [Human-in-the-loop for AI tool calls](https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/)

## Enterprise and operations surface

Official docs also cover:

- source control and environments
- external secrets
- log streaming
- insights
- workflow history
- sharing and collaboration
- save/publish mechanics

Sources:

- [Source control and environments](https://docs.n8n.io/using-n8n/enterprise-key-features/source-control-environments/understand/)
- [Workflow history](https://docs.n8n.io/workflows/history/)
- [Save and publish](https://docs.n8n.io/workflows/publish/)
- [Sharing](https://docs.n8n.io/workflows/sharing/)

## Notable current details worth encoding in skills

- The `Evaluation Trigger` node uses Data Tables or Google Sheets as evaluation dataset sources.
- The `Evaluation` node can log outputs and metrics back into evaluation surfaces.
- The `Guardrails` node can sanitize text or use LLM-based policy checks, and LLM-based checks require a connected chat model.
- The `MCP Client` node supports Bearer, generic header, and OAuth2 auth, while `MCP Client Tool` exposes selected or all tools to agents.
- The `MCP Server Trigger` node supports SSE and streamable HTTP, and official docs warn that multi-webhook-replica deployments need dedicated routing for `/mcp*` traffic.
- External secrets support 1Password, AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager, and HashiCorp Vault. Official docs also note multiple vaults per provider from n8n `2.10.0`.

## Community node verification and publishing

Official docs state that from **May 1, 2026**, nodes submitted for verification through the Creator Portal must be published using **GitHub Actions with a provenance statement**.

Sources:

- [Submit community nodes](https://docs.n8n.io/integrations/creating-nodes/deploy/submit-community-nodes/)
- [Verification guidelines](https://docs.n8n.io/integrations/creating-nodes/build/reference/verification-guidelines/)

## Implication for this repo

The skill packs here deliberately include not just workflow-building guidance, but also:

- evaluation strategy
- guardrails strategy
- MCP and AI tool-routing strategy
- source-control and release strategy
- verified-node publishing guidance
- enterprise observability and security guidance

See also:

- [Skill Coverage Matrix](./skill-coverage-matrix.md)
- [Hyper-Technical Runbooks](./hyper-technical-runbooks.md)
