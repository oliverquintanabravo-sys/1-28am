# Backlink Pass

## What this workflow is
Wires the brain together: adds `[[wikilinks]]` across `brain/` so reading one note surfaces the related ones (readable as a graph in Obsidian). Run once the brain passes ~20 notes, then after every bulk import.

## Process
1. Read every note in `brain/`.
2. Add `[[wikilinks]]` connecting notes that genuinely share a client, a decision, a project, a person, or a lesson.

## Rules
- Link text must match the target note's filename exactly (without `.md`), so links resolve in Obsidian.
- Only add a link where following it would teach the reader something real. Relationships, not keyword matches.
- Most notes should end up with 2–5 links. If a note honestly connects to nothing, leave it alone and report it — never force a link.
- **Add links only.** Do not rewrite, trim, or improve any other content — the git diff must be pure and reviewable.

## Report when done
- How many links were added
- Which notes are orphans with no connections (these usually need expanding or merging)
- The three most surprising connections found

## Quality gates
- [ ] `python3 execution/check_brain.py` reports no broken links
- [ ] Git diff contains only added link syntax, no content changes
