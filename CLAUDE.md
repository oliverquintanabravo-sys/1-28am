# Oliver's AI Operating System — Master Operating Manual

This repository is Oliver's second brain and AI operating system. Read this file first, every session. The model is the employee; this folder is the company.

## 1. Architecture: DOE

Three layers with hard boundaries:

- **Directives** (`directives/`) — WHAT to do. Step-by-step SOPs in plain English, one markdown file per workflow.
- **Orchestration** (you, the AI agent) — the decision maker. Reads context, picks the SOP, makes judgment calls, checks quality.
- **Execution** (`execution/`) — HOW deterministic work gets done. Scripts for extraction, file work, formatting, API calls.

**The boundary rule:** if a step should produce the same output every time given the same input, it belongs in a script. If it requires judgment, taste, or reading context, it stays with the AI. When in doubt: extraction, conversion, validation, and indexing are scripts; interpretation, writing, linking decisions, and quality review are AI. See `execution/README.md` for the full rubric.

**Model independence:** everything important lives in markdown files, never inside AI conversations. Plain text survives every model migration. If something valuable was learned in a session, it must be written into a file before the session ends, or it is lost.

## 2. Directory map

| Folder | Purpose |
|---|---|
| `context/` | Who Oliver is: work, goals, vision, writing style, philosophy, preferred workflows |
| `directives/` | SOPs — one markdown file per workflow |
| `execution/` | Deterministic scripts the SOPs call |
| `skills/` | Deep domain expertise files (`SKILL_BIBLE_<topic>.md`), each citing source and date |
| `projects/` | One folder per project: overview + dated log |
| `clients/` | One folder per client relationship (empty until needed; templates ready) |
| `brain/` | Dated, wiki-linked notes: decisions, notes, references, metrics, ideas |
| `sources/` | Raw material (PDFs, decks, exports, transcripts) waiting to be mined into the brain |
| `templates/` | Every reusable template: SOPs, skills, projects, clients, notes, decisions, meetings |
| `.tmp/` | Scratch space and extraction output — never committed |

## 3. Context loading order

Before any task, load in this order (read `brain/INDEX.md` before opening brain notes; open only what is relevant):

1. `context/work.md` — always (what Oliver does and where)
2. `context/philosophy.md` — always (how he operates; check work against it)
3. `context/goals_and_vision.md` — for planning, prioritization, or new initiatives
4. `context/writing_style.md` — for anything Oliver's name goes on
5. `context/workflows.md` — for how to collaborate and deliver
6. `projects/{name}/*.md` or `clients/{name}/*.md` — for project- or client-specific work
7. `skills/` relevant files — domain expertise for the task
8. `directives/` the matching SOP — the workflow itself

## 4. Orchestration flow

1. Parse the request.
2. Find the matching directive. If none exists, do the task with Oliver narrating standards, then write the directive from that session using `templates/sop.md`.
3. Load context per the order above.
4. Execute — deterministic steps via `execution/` scripts, judgment steps yourself.
5. Run the directive's quality gates before delivering.
6. Deliver, then run the self-improvement check (section 7).

## 5. Knowledge import pipeline

Whenever new information arrives (PDF, video transcript, meeting notes, conversation, research, book, course), follow `directives/ingest_sources.md`. The contract:

1. Raw file lands in `sources/` (or is referenced from a conversation).
2. Extract text deterministically (`execution/extract_text.py` → `.tmp/extracted/`).
3. **Check for duplicates before writing**: search `brain/INDEX.md` and existing note titles. If a note on the fact exists, update it (and its date) rather than creating a twin.
4. Mine into dated notes — one fact per note, `YYYY-MM-DD_slug.md`, specifics not summaries, source cited at the bottom.
5. Add `[[wikilinks]]` to genuinely related notes (relationships, not keyword matches; 2–5 per note).
6. Update `brain/INDEX.md` — one line per note.
7. Verify with `execution/check_brain.py` (index consistency, orphans, broken links).

## 6. Quality gates (global)

Every deliverable passes these before Oliver sees it; directives add their own on top:

- [ ] **No fabricated facts.** Never invent numbers, names, results, dates, or policies. Placeholders plus a question beat confident fiction. Facts pulled from sources cite the source.
- [ ] **Dated.** Brain notes, decisions, metrics, and history entries carry `YYYY-MM-DD` in the filename or heading.
- [ ] **Specific.** Notes and skill files contain numbers, names, templates, or exact phrasings — otherwise they change nothing.
- [ ] **Voice-checked.** Anything written in Oliver's voice is checked against `context/writing_style.md`.
- [ ] **Values-checked.** Work is checked against `context/philosophy.md`.
- [ ] **In the right layer.** No SOP logic buried in scripts; no deterministic work left to AI improvisation.

## 7. Self-improvement protocol

After every task:

- An error occurred → fix the script AND update the directive that called it.
- A better approach was found → update the relevant skill file or directive.
- A new edge case appeared → add it to the SOP's edge-cases section.
- Oliver gave a correction or preference → encode it in the right context file immediately.
- A meaningful decision was made → write it to `brain/decisions/` with the reasoning.

Nothing breaks the same way twice, because every failure becomes an edit to the system.

## 8. Standing operating principles

1. **Never fabricate.** (See quality gates — this is the first law.)
2. **Date everything.** An undated fact is a landmine once the business changes its mind.
3. **Ask before destroying.** Additive changes proceed freely; deletions, renames of Oliver's content, or anything hard to reverse get explained and approved first.
4. **Store less, operationalize more.** The test of this system is whether an AI can pick up a task cold, load the right files, and produce work that passes the quality bar.
5. **Ten messy real notes beat a beautiful empty taxonomy.** Bias toward capturing.
6. **Keep the repo maintainable.** Refactor and simplify as it grows; future models must be able to understand it cold.
7. **`.tmp/` for drafts, never committed.** Secrets live in `.env`, never in git.
8. **Audit on a schedule.** Run `directives/contradiction_audit.md` every few weeks; an unaudited brain becomes a brain you can't trust.

## 9. Current state (update when it changes)

- Context files are partially populated: facts marked **[verified]** come from Oliver's own documents in `sources/`; placeholders in brackets await Oliver's input.
- Active project: `projects/team_lead_toolkit/`.
- `sources/intern-to-team-lead-toolkit.zip` is partially mined (see `sources/README.md`).
- `clients/` is empty by design — Oliver's current work is project-shaped, not client-shaped. The layer exists for when that changes.

*Last updated: 2026-07-08*
