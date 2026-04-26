from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^name:\s*(.+)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)


def main() -> int:
    failures: list[str] = []
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            failures.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---"):
            failures.append(f"{skill_dir.name}: missing YAML frontmatter")
            continue
        name_match = NAME_RE.search(text)
        desc_match = DESC_RE.search(text)
        if not name_match:
            failures.append(f"{skill_dir.name}: missing frontmatter name")
        if not desc_match:
            failures.append(f"{skill_dir.name}: missing frontmatter description")
        if "## Quick workflow" not in text:
            failures.append(f"{skill_dir.name}: missing Quick workflow section")
        if len(text.splitlines()) < 20:
            failures.append(f"{skill_dir.name}: skill too short to be operational")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"Validated {len(list(SKILLS_DIR.iterdir()))} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

