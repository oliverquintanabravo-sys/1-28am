#!/usr/bin/env python3
"""Create a dated brain note from the template and register it in INDEX.md.

Usage:
    python3 execution/new_note.py <category> <slug> "<one-line summary>"

category: decisions | notes | references | metrics | ideas
Creates brain/<category>/<today>_<slug>.md (decision template for decisions,
brain-note template otherwise) and appends the index line under the right
heading. Refuses to overwrite an existing note.
"""
import datetime
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = ("decisions", "notes", "references", "metrics", "ideas")


def main(argv: list[str]) -> None:
    if len(argv) != 3 or argv[0] not in CATEGORIES:
        sys.exit(__doc__)
    category, slug, summary = argv
    slug = re.sub(r"[^a-z0-9-]+", "-", slug.lower()).strip("-")
    today = datetime.date.today().isoformat()
    filename = f"{today}_{slug}.md"
    note_path = REPO_ROOT / "brain" / category / filename
    if note_path.exists():
        sys.exit(f"Refusing to overwrite existing note: {note_path}")

    template = "decision.md" if category == "decisions" else "brain_note.md"
    body = (REPO_ROOT / "templates" / template).read_text(encoding="utf-8")
    body = body.replace("YYYY-MM-DD", today)
    note_path.write_text(body, encoding="utf-8")

    index_path = REPO_ROOT / "brain" / "INDEX.md"
    index = index_path.read_text(encoding="utf-8")
    heading = f"## {category}/"
    entry = f"- [[{filename[:-3]}]] — {summary}\n"
    if heading not in index:
        sys.exit(f"Heading '{heading}' not found in INDEX.md — add it first.")
    # Insert the entry at the end of the category's section, keeping the
    # blank line that separates sections.
    section_start = index.index(heading)
    next_heading = index.find("\n## ", section_start + len(heading))
    insert_at = len(index) if next_heading == -1 else next_heading
    index = index[:insert_at].rstrip("\n") + "\n" + entry + index[insert_at:]
    index_path.write_text(index, encoding="utf-8")

    print(f"Created {note_path.relative_to(REPO_ROOT)} and indexed it.")
    print("Now fill in the note: replace every [bracketed placeholder].")


if __name__ == "__main__":
    main(sys.argv[1:])
