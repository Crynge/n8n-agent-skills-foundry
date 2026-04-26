# Cursor Installation

Cursor doesn't use Claude skill folders directly, so this repo ships a Cursor adapter under `adapters/cursor/`.

## Install

1. Copy `adapters/cursor/AGENTS.md` into your target project or merge it into an existing `AGENTS.md`.
2. Copy `adapters/cursor/.cursor/rules/` into your project’s `.cursor/rules/`.
3. Keep `skills/` accessible as the long-form knowledge base.

## Recommended usage

- Use Cursor rules for routing and behavior.
- Use the canonical `skills/` folder as the detailed reference corpus.
- For complex n8n work, explicitly ask Cursor to apply the relevant skill names from this repo.

