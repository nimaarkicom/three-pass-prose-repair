#!/usr/bin/env python3
"""validate_frontmatter.py: check that SKILL.md's YAML frontmatter parses.

This project shipped once with an unquoted colon inside the frontmatter
description field. GitHub's own frontmatter parser broke on it silently;
the skill still rendered as plain markdown with no error, just no working
routing. This script exists so that class of bug fails CI instead of
shipping.

Checks:
  1. The file starts with a "---" line, has a second "---" line closing
     the frontmatter block, and the text between them parses as valid
     YAML.
  2. The parsed frontmatter is a mapping (not a string, list, or None,
     which is what an unclosed or malformed block silently produces).
  3. Required keys are present and non-empty: name, description.

Usage:
    python3 scripts/validate_frontmatter.py SKILL.md
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(1)

REQUIRED_KEYS = ("name", "description")


def extract_frontmatter(text: str) -> str | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_frontmatter.py FILE", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"error: {path} does not exist", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    raw = extract_frontmatter(text)
    if raw is None:
        print(f"FAIL: {path} has no closed '---' frontmatter block")
        return 1

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        print(f"FAIL: {path} frontmatter is not valid YAML: {exc}")
        return 1

    if not isinstance(data, dict):
        print(f"FAIL: {path} frontmatter did not parse to a mapping (got {type(data).__name__})")
        return 1

    missing = [k for k in REQUIRED_KEYS if not data.get(k)]
    if missing:
        print(f"FAIL: {path} frontmatter is missing required key(s): {', '.join(missing)}")
        return 1

    for key in REQUIRED_KEYS:
        value = data[key]
        if not isinstance(value, str):
            print(f"FAIL: {path} frontmatter key '{key}' should be a string, got {type(value).__name__}")
            return 1

    print(f"PASS: {path} frontmatter parses and has required keys: {', '.join(REQUIRED_KEYS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
