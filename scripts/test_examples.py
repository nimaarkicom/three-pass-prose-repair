#!/usr/bin/env python3
"""test_examples.py: check that diagnose.py still tells the two example
fixtures apart.

This is the regression check CI runs on every push. It does not test every
signal in isolation; it tests the one thing that actually matters for this
tool to be useful: examples/formulaic.txt must score as more flagged than
examples/natural.txt. If a future change to diagnose.py makes the two
fixtures score the same, or flips the order, this fails the build.

Usage:
    python3 scripts/test_examples.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from diagnose import diagnose  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FORMULAIC = ROOT / "examples" / "formulaic.txt"
NATURAL = ROOT / "examples" / "natural.txt"


def main() -> int:
    failures = []

    for path in (FORMULAIC, NATURAL):
        if not path.exists():
            failures.append(f"missing fixture: {path}")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1

    formulaic_report = diagnose(FORMULAIC.read_text(encoding="utf-8"))
    natural_report = diagnose(NATURAL.read_text(encoding="utf-8"))

    formulaic_flags = formulaic_report["flagged_signal_count"]
    natural_flags = natural_report["flagged_signal_count"]

    print(f"examples/formulaic.txt flagged signals: {formulaic_flags} {formulaic_report['flagged_signals']}")
    print(f"examples/natural.txt flagged signals:    {natural_flags} {natural_report['flagged_signals']}")

    if formulaic_flags <= natural_flags:
        print("FAIL: formulaic.txt did not score as more flagged than natural.txt")
        failures.append("no distinction between fixtures")

    min_gap = 2
    gap = formulaic_flags - natural_flags
    if gap < min_gap:
        print(f"FAIL: gap between fixtures is only {gap}, expected at least {min_gap}")
        failures.append("gap too small")

    if failures:
        return 1

    print("PASS: diagnose.py produces distinct output on the two fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
