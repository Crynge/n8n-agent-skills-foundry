# Compatibility Matrix

| Surface | Claude Code | Cursor | Qwen Code | MiniMax |
|---|---|---|---|---|
| Canonical `skills/` corpus | Native | Reference corpus | Reference corpus | Reference corpus |
| Root `AGENTS.md` routing | Native | Merge into project `AGENTS.md` | Use as bootstrap prompt basis | Use as bootstrap prompt basis |
| Cursor rules | No | Native | No | No |
| Prompt-pack installation | Optional | Optional | Primary | Primary |
| GitHub CI validation | Yes | Yes | Yes | Yes |

## Practical interpretation

- Claude Code can consume the skill corpus directly.
- Cursor uses adapter rules plus the canonical skill corpus as reference.
- Qwen Code and MiniMax use the canonical corpus through prompt or agent bootstrap instructions.
- CI and docs stay shared across all four environments.

