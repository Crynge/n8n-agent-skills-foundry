# Audit of `czlonkowski/n8n-skills`

Reference: [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)

## What it does well

- Strong foundation around seven critical workflow-building skills.
- Good emphasis on n8n MCP tool correctness, expressions, validation, and Code nodes.
- Real evaluations are present.
- Good entry point for Claude-centric workflow generation.

## What is missing

### 1. Assistant portability

The repo is explicitly Claude-first. It doesn't provide first-class installation or behavior packs for Cursor, Qwen Code, or MiniMax.

Impact:

- teams can’t adopt one shared skill corpus across multiple assistants
- there is no adapter strategy for Cursor rules, Qwen prompt packs, or MiniMax operational prompts

### 2. Current n8n surface coverage

The repo’s scope is broader than beginners need, but still narrower than the current official n8n capability set.

Missing or underrepresented areas include:

- `AI Transform`
- `Data Table`
- `Evaluation`
- `Evaluation Trigger`
- `Guardrails`
- `Execution Data`
- `MCP Client`
- `MCP Server Trigger`
- `Local File Trigger`
- source control and environments
- external secrets
- log streaming
- insights
- verified community node publishing workflows

### 3. Production AI lifecycle guidance

It helps build workflows, but it is thinner on the lifecycle after the first working draft:

- evaluation dataset design
- tool-call approval patterns
- fallback and escalation design
- memory pressure control
- observability for agent workflows
- production regression testing

### 4. Enterprise and release engineering depth

The reference repo has no visible GitHub Actions layer and limited material on:

- release gating
- provenance-aware publishing
- source-control operations
- environment promotion
- security review and secrets posture

That matters more now because official n8n docs require GitHub Actions provenance for verified community-node publishing from May 1, 2026.

### 5. Integration intelligence layer

The reference repo teaches MCP tool usage, but does not provide a maintained integration taxonomy mapping:

- use case families
- node families
- auth patterns
- fallback strategy when a built-in node is absent
- when to prefer HTTP Request versus a native integration

## Design response in this repo

This repository answers those gaps by adding:

- 16 skills instead of 7
- multi-agent adapters
- current node and enterprise coverage
- catalog generation and CI validation
- platform-specific installation docs
- source-backed capability mapping

