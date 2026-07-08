# Ingest Sources

## What this workflow is
Turns raw material — PDFs, decks, video/meeting transcripts, conversations, research, books, courses — into dated, linked, deduplicated brain notes. This is how the knowledge system grows. Run it whenever new files land in `sources/` or valuable information surfaces in a session.

## Prerequisites
- Context files: `context/work.md` (to judge relevance)
- Scripts: `execution/extract_text.py`, `execution/check_brain.py`

## Inputs
| Field | Required | Description |
|---|---|---|
| Source file(s) or pasted content | yes | Anything in `sources/`, or content from the conversation |
| Kind | yes | course/book → skill file; meeting → meeting note; everything else → brain notes |

## Process
1. **Extract (script).** `python3 execution/extract_text.py <file>` → text in `.tmp/extracted/`. Never retype content by hand from a file a script can read.
2. **Survey (AI).** Read the extraction. List candidate facts/lessons worth keeping. Skip anything generic — if a note wouldn't change future output, don't write it.
3. **Dedupe (AI, mandatory).** For each candidate, search `brain/INDEX.md` and note filenames for existing coverage. Existing note → update it in place (refresh its date line, note what changed). New → proceed.
4. **Write notes (AI).** One fact per note via `templates/brain_note.md` (decisions get `templates/decision.md`; courses/books/masterclasses get a `skills/SKILL_BIBLE_<topic>.md` via `templates/skill.md`). Filename `YYYY-MM-DD_slug.md` — the date is the capture date. Cite the source at the bottom of every note.
5. **Link (AI).** Add `[[wikilinks]]` between genuinely related notes — shared project, person, decision, or lesson; 2–5 per note; never forced. Link text must match the target filename (without `.md`) exactly.
6. **Index (AI).** Add one line per new note to `brain/INDEX.md` under the right category.
7. **Verify (script).** `python3 execution/check_brain.py` — fix anything it flags.
8. **Mark the source.** Update `sources/README.md`: what was mined, when, into which notes.

## Quality gates
- [ ] Every new note is dated in the filename and cites its source
- [ ] No note duplicates an existing one (step 3 actually performed)
- [ ] Notes contain specifics — numbers, names, exact phrasings — not summaries
- [ ] `check_brain.py` passes clean
- [ ] INDEX.md updated

## Edge cases
- Source contradicts an existing note → keep both temporarily, flag the conflict to Oliver, let him rule; the loser gets marked superseded, not deleted.
- Source contains personal data about third parties (students, staff) → capture roles and lessons, not unnecessary personal details.
- Scanned/image-only PDF → extraction returns little text; read page images directly if possible, otherwise flag for manual handling.
- A fact is valuable but unverifiable → capture it with an explicit "[unconfirmed — source said X]" marker.
