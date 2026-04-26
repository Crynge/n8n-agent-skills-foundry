# Architecture

## Canonical model

The repository treats each skill under `skills/` as the canonical domain artifact. Platform adapters transform that corpus into environment-specific usage patterns.

## Layers

### 1. Canonical skill layer

`skills/*/SKILL.md`

- concise activation metadata
- procedural workflow guidance
- references for deeper detail

### 2. Adapter layer

`adapters/`

- Claude Code installation guidance
- Cursor rules and prompts
- Qwen Code prompt packs
- MiniMax prompt packs

### 3. Governance layer

`.github/workflows/`

- lint all skills
- build catalog
- run tests

### 4. Catalog layer

`data/integration-catalog.json`

- integration families
- auth patterns
- recommended skill routing
- built-in versus HTTP fallback guidance

## Routing philosophy

- Select the narrowest skill that fully covers the active problem.
- Compose skills for cross-cutting cases like AI workflows with side effects.
- Defer long catalogs and matrices to references or data files.

