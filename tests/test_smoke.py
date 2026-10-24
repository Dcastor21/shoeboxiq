"""Proves the toolchain works. Real tests replace this from Step 3 on."""

import tomllib
from pathlib import Path

import shoeboxiq


def test_installed_version_matches_pyproject() -> None:
    pyproject_path = Path(__file__).parents[1] / "pyproject.toml"
    pyproject = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    assert shoeboxiq.__version__ == pyproject["project"]["version"]
