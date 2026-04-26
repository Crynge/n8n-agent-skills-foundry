# MCP Surfaces

## Current official MCP surfaces

- instance-level n8n MCP server
- MCP Client node
- MCP Client Tool node
- MCP Server Trigger node

## Design distinctions

- instance-level MCP exposes broader instance capabilities
- MCP Server Trigger exposes workflow-bound tools
- MCP Client uses external MCP servers directly as workflow steps
- MCP Client Tool exposes external MCP tools to AI agents

## Operational notes

- auth method choice matters for both workflow and agent use
- long-lived transports need topology-aware routing

