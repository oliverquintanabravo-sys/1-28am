#!/usr/bin/env python3
"""Audit the brain's mechanical health. Deterministic; exits 1 on problems.

Usage:
    python3 execution/check_brain.py

Checks:
  1. Every brain note filename starts with YYYY-MM-DD_.
  2. Every note appears exactly once in brain/INDEX.md, and every index
     entry points to a real note.
  3. Every [[wikilink]] in brain/, context/, directives/, projects/ resolves
     to an existing brain note filename.
  4. Orphans: notes with no incoming or outgoing links (reported, not fatal).
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BRAIN = REPO_ROOT / "brain"
CATEGORIES = ("decisions", "notes", "references", "metrics", "ideas")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_.+\.md$")
LINK_RE = re.compile(r"\[\[([^\]|#]+)")
CODE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]*`")


def links_in(text: str) -> list[str]:
    """Wikilinks in text, ignoring code blocks/spans (meta-mentions of syntax)."""
    return LINK_RE.findall(CODE_RE.sub("", text))


def main() -> None:
    problems: list[str] = []
    notes = {
        p.stem: p
        for cat in CATEGORIES
        for p in sorted((BRAIN / cat).glob("*.md"))
    }

    for stem, path in notes.items():
        if not DATE_RE.match(path.name):
            problems.append(f"UNDATED filename: {path.relative_to(REPO_ROOT)}")

    index_text = (BRAIN / "INDEX.md").read_text(encoding="utf-8")
    indexed = links_in(index_text)
    for stem in notes:
        count = indexed.count(stem)
        if count == 0:
            problems.append(f"NOT IN INDEX: {stem}")
        elif count > 1:
            problems.append(f"DUPLICATE INDEX ENTRY ({count}x): {stem}")
    for stem in indexed:
        if stem not in notes:
            problems.append(f"INDEX POINTS TO MISSING NOTE: {stem}")

    linked_from: dict[str, set] = {stem: set() for stem in notes}
    links_out: dict[str, set] = {stem: set() for stem in notes}
    scan_dirs = [BRAIN, REPO_ROOT / "context", REPO_ROOT / "directives", REPO_ROOT / "projects"]
    for d in scan_dirs:
        for f in sorted(d.rglob("*.md")):
            if f.name == "INDEX.md":
                continue
            for target in links_in(f.read_text(encoding="utf-8")):
                target = target.strip()
                if target not in notes:
                    problems.append(
                        f"BROKEN LINK [[{target}]] in {f.relative_to(REPO_ROOT)}"
                    )
                else:
                    linked_from[target].add(f.stem)
                    if f.stem in notes:
                        links_out[f.stem].add(target)

    orphans = [
        stem for stem in notes if not linked_from[stem] and not links_out[stem]
    ]

    for p in problems:
        print(f"PROBLEM  {p}")
    for o in orphans:
        print(f"orphan   {o} (no links in or out — expand, merge, or link it)")
    print(
        f"\n{len(notes)} notes, {len(problems)} problems, {len(orphans)} orphans."
    )
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
