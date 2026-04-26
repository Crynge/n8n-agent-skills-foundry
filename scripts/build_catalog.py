from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
OUT = ROOT / "catalog" / "skills.generated.json"
NAME_RE = re.compile(r"^name:\s*(.+)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)


def load_skill(skill_dir: Path) -> dict[str, object]:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    name = NAME_RE.search(text).group(1).strip()  # type: ignore[union-attr]
    description = DESC_RE.search(text).group(1).strip()  # type: ignore[union-attr]
    return {
        "id": skill_dir.name,
        "name": name,
        "description": description,
        "references": sorted(str(path.relative_to(skill_dir)) for path in skill_dir.rglob("*.md") if path.name != "SKILL.md"),
        "reference_count": len(list((skill_dir / "references").glob("*.md"))),
    }


def main() -> int:
    skills = [load_skill(skill_dir) for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())]
    OUT.write_text(json.dumps({"skills": skills}, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
