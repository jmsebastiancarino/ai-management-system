#!/usr/bin/env python3
"""
validate_ai_controls.py — integrity checks for the AI control catalog.

An AI control is only "done" when it (a) has the required descriptive fields,
(b) is tagged to at least one valid AI lifecycle stage, (c) maps to at least
one framework with at least one reference, and (d) names at least one evidence
artifact with a source and a cadence.

Usage:
    python scripts/validate_ai_controls.py [path/to/ai-controls.yaml]

Exit 0 = all controls valid; 1 = one or more failures (fails the build).
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip install pyyaml")

REQUIRED_TEXT_FIELDS = ("id", "title", "statement")
KNOWN_FRAMEWORKS = ("iso_42001", "nist_ai_rmf", "iso_23894", "iso_27001")
VALID_STAGES = (
    "data", "development", "validation",
    "deployment", "operation", "retirement",
)


def load_controls(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    controls = data.get("controls")
    if not isinstance(controls, list):
        sys.exit(f"ERROR: {path} has no top-level 'controls:' list")
    return controls


def validate_control(ctrl: dict) -> list[str]:
    problems: list[str] = []

    for field in REQUIRED_TEXT_FIELDS:
        if not str(ctrl.get(field, "")).strip():
            problems.append(f"missing required field '{field}'")

    # lifecycle stage: >=1 valid stage
    stages = ctrl.get("ai_lifecycle_stage")
    stages = stages if isinstance(stages, list) else [stages] if stages else []
    if not stages:
        problems.append("no ai_lifecycle_stage — every AI control attaches to a stage")
    for s in stages:
        if s not in VALID_STAGES:
            problems.append(f"invalid lifecycle stage '{s}'")

    # framework mapping: >=1 framework with >=1 reference
    maps_to = ctrl.get("maps_to") or {}
    mapped = {fw: refs for fw, refs in maps_to.items() if refs}
    if not mapped:
        problems.append("maps_to is empty — control answers no framework")
    for fw in maps_to:
        if fw not in KNOWN_FRAMEWORKS:
            problems.append(f"unknown framework key '{fw}'")

    # evidence: >=1 item, each with source + artifact + cadence
    evidence = ctrl.get("evidence") or []
    if not evidence:
        problems.append("no evidence — an AI control with no provable artifact isn't done")
    for i, ev in enumerate(evidence):
        for key in ("source", "artifact", "cadence"):
            if not str(ev.get(key, "")).strip():
                problems.append(f"evidence[{i}] missing '{key}'")

    return problems


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else \
        Path(__file__).resolve().parent.parent / "controls" / "ai-controls.yaml"

    controls = load_controls(path)
    seen_ids: set[str] = set()
    failures = 0
    framework_hits: dict[str, int] = {fw: 0 for fw in KNOWN_FRAMEWORKS}
    stage_hits: dict[str, int] = {s: 0 for s in VALID_STAGES}

    print(f"Validating {len(controls)} AI controls in {path}\n")

    for ctrl in controls:
        cid = str(ctrl.get("id", "<no-id>"))
        problems = validate_control(ctrl)

        if cid in seen_ids:
            problems.append(f"duplicate id '{cid}'")
        seen_ids.add(cid)

        for fw, refs in (ctrl.get("maps_to") or {}).items():
            if refs and fw in framework_hits:
                framework_hits[fw] += 1
        stages = ctrl.get("ai_lifecycle_stage") or []
        for s in (stages if isinstance(stages, list) else [stages]):
            if s in stage_hits:
                stage_hits[s] += 1

        if problems:
            failures += 1
            print(f"  [FAIL] {cid}")
            for p in problems:
                print(f"         - {p}")
        else:
            n_fw = sum(1 for refs in (ctrl.get("maps_to") or {}).values() if refs)
            print(f"  [ OK ] {cid:<13} {ctrl.get('title','')}  ({n_fw} frameworks)")

    print("\nFramework coverage:")
    for fw, n in framework_hits.items():
        if n:
            print(f"  {fw:<13} {n} control(s)")
    print("\nLifecycle coverage:")
    for s, n in stage_hits.items():
        print(f"  {s:<13} {n} control(s)")

    print()
    if failures:
        print(f"RESULT: {failures} AI control(s) failed validation.")
        return 1
    print(f"RESULT: all {len(controls)} AI controls valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
