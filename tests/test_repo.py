from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_lint_skills_passes() -> None:
    result = subprocess.run([sys.executable, "scripts/lint_skills.py"], cwd=ROOT, check=False, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


def test_build_catalog_creates_skills_json() -> None:
    result = subprocess.run([sys.executable, "scripts/build_catalog.py"], cwd=ROOT, check=False, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads((ROOT / "catalog" / "skills.generated.json").read_text(encoding="utf-8"))
    assert "skills" in payload
    assert len(payload["skills"]) >= 12

