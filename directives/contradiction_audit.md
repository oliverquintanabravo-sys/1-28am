# Contradiction Audit

## What this workflow is
Keeps the brain trustworthy. Reads all of `brain/` and `context/` looking for notes that disagree — stale facts, reversed decisions, conflicting numbers — flags them, and lets Oliver rule on each. Run every few weeks; a brain that is never audited becomes a brain you can't trust, and then you stop using it.

## Process
1. Run `python3 execution/check_brain.py` first — fix mechanical issues (index drift, broken links, undated files) before judgment work.
2. Read `brain/INDEX.md`, then every note, plus all `context/` files.
3. Hunt for: facts that conflict (old vs. new numbers, schedules, rosters); decisions later contradicted without a superseding note; context files that drifted from reality; anything undated or stale ("current" claims older than ~3 months).
4. Produce the conflict list: each item shows both notes, both dates, and a recommended resolution.
5. Oliver rules on each. Apply rulings: the losing note gets marked superseded, with a wikilink to the winning note (never silently deleted); context files get corrected; `INDEX.md` updated.
6. Log the audit as a dated brain note: what was found, what was ruled.

## Quality gates
- [ ] Every conflict presented with dates and a recommendation — no silent resolutions
- [ ] No note deleted; superseded notes marked and kept
- [ ] Audit logged in `brain/notes/`
