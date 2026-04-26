# Contributing

## Principles

- Keep `SKILL.md` focused on execution guidance.
- Put long catalogs, edge-case tables, and raw references in `references/`.
- Prefer current official n8n documentation for facts about nodes, enterprise features, and verification rules.
- Do not remove existing skills when adding new specializations; evolve routing and overlap guidance instead.

## Workflow

1. Add or update skill content under `skills/`.
2. Run `python scripts/lint_skills.py`.
3. Run `python scripts/build_catalog.py`.
4. Run `python -m pytest -q`.
5. Update docs if the capability surface changed.

