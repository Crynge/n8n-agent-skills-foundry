from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def assert_exists(relative_path: str) -> None:
    path = ROOT / relative_path
    if not path.exists():
        raise FileNotFoundError(relative_path)


def main() -> int:
    required = [
        "README.md",
        "AGENTS.md",
        "docs/audit-reference-repo.md",
        "docs/latest-n8n-surface.md",
        "docs/compatibility-matrix.md",
        "adapters/cursor/AGENTS.md",
        "adapters/cursor/.cursor/rules/01-n8n-routing.mdc",
        "data/integration-catalog.json",
        ".github/workflows/ci.yml",
    ]
    for item in required:
        assert_exists(item)
    print(f"Smoke check passed for {len(required)} paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

