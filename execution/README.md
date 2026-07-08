# Execution Layer

Deterministic scripts. Same input → same output, every time. The AI calls these instead of improvising the work they cover.

## Deterministic vs. AI reasoning — the rubric

| Task | Layer | Why |
|---|---|---|
| Extracting text from PDFs/decks/docs | **script** (`extract_text.py`) | Mechanical conversion; AI retyping invites transcription errors |
| Creating a dated note + index entry | **script** (`new_note.py`) | Filename/date/index formatting must never drift |
| Checking index drift, broken links, undated files | **script** (`check_brain.py`) | Rule-based validation; a checklist, not a judgment |
| Deciding what in a source is worth keeping | **AI** | Requires knowing what Oliver already knows and cares about |
| Writing the note content | **AI** | Compression with judgment |
| Deciding which notes genuinely relate (wikilinks) | **AI** | Relationships, not keyword matches |
| Contradiction rulings | **AI + Oliver** | Judgment, and often only Oliver knows current truth |
| Quality-gate review | **AI** | Reading against voice/values files is interpretive |

## Recommended future scripts (build when the bottleneck is real, not before)

- `render_work_plan.py` — fill the Center's work-plan form layout from a completed markdown plan (deterministic formatting; the plan content stays AI+Oliver)
- `weekly_snapshot.py` — append a dated metrics note from whatever numbers Oliver tracks
- Delivery integrations (Google Docs export, notifications) — per blueprint Phase 9, only when needed

## Dependencies

Python 3 standard library, except PDF extraction which needs `pymupdf` (`pip install pymupdf`). Everything else — docx, pptx, html — is stdlib only, on purpose: fewer dependencies means the system keeps working across environments and years.
