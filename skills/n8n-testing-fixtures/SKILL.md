---
name: n8n-testing-fixtures
description: Use for test datasets, fixture design, replayable workflow checks, regression packs, evaluation corpora, and workflow verification strategy in n8n.
---

# n8n Testing Fixtures

Use this skill when the team needs evidence that a workflow will keep working.

## Quick workflow

1. Identify the highest-risk branches and data shapes.
2. Build fixtures that cover nominal, edge, and failure cases.
3. Preserve realistic headers, auth-free payloads, and timing cues where needed.
4. Run checks before and after significant workflow edits.
5. Turn recurrent incidents into permanent test cases.

## Core rules

- A workflow without fixtures is hard to change safely.
- Replays should reflect real production data shapes, scrubbed for secrets.
- AI workflows need both task fixtures and evaluation fixtures.
- Tests should cover duplicates, empties, and partial failures, not just happy paths.

## Deep references

- fixture design guide: [references/fixture-design.md](references/fixture-design.md)

