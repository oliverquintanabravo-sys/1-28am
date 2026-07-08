# Business Brain — Operating Manual

This folder is the second brain for Oliver's business. Read this file first, every session.

## Architecture: DOE

The system separates three layers. Respect the boundaries.

- **Directives** (`directives/`) — WHAT to do: step-by-step SOPs in plain English, one file per workflow.
- **Orchestration** (the AI agent) — the decision maker: reads context, picks the SOP, makes judgment calls, checks quality.
- **Execution** (`execution/`) — HOW it gets done: deterministic scripts for API calls, formatting, file work.

Rule of thumb: if a step should produce the same output every time given the same input, it belongs in a script. If it requires judgment, taste, or reading context, it stays with the AI.

## Directory map

| Folder | Purpose |
|---|---|
| `context/` | Who we are: identity, voice, values, owner background |
| `directives/` | SOPs — one markdown file per workflow |
| `execution/` | Scripts the SOPs call for deterministic steps |
| `skills/` | Deep domain expertise files (`SKILL_BIBLE_<topic>.md`) |
| `clients/` | One folder per client: profile, rules, preferences, history |
| `brain/` | Dated, linked notes: decisions, references, metrics, ideas |
| `sources/` | Raw exports (transcripts, decks, threads) to be mined into brain notes |
| `.tmp/` | Scratch space for drafts — never committed |

## Context loading priority

Before any task, load in this order:

1. `context/agency.md` — always first (who we are)
2. `context/core_values.md` — always (how we operate; check work against it)
3. `context/brand_voice.md` — for any content creation
4. `clients/{name}/*.md` — for client-specific work
5. `skills/` relevant files — domain expertise for the task
6. `directives/` the matching SOP — the workflow itself

## Orchestration flow

1. Parse the request.
2. Find the matching directive in `directives/`. If none exists, do the task with the owner narrating standards, then write the directive from that session.
3. Load context per the priority above (read `brain/INDEX.md` first, then open only relevant notes).
4. Execute — deterministic steps via `execution/` scripts, judgment steps yourself.
5. Check the output against the directive's quality gates.
6. Deliver.

## Standing rules

1. **Never fabricate numbers, results, or client names.** Use placeholders and ask. Placeholders plus a question beat confident fiction every time.
2. **Date everything.** Brain notes are dated in the filename (`YYYY-MM-DD_slug.md`). An undated fact is a landmine.
3. **Extract specifics, not summaries.** Notes and skill files must contain numbers, names, templates, or exact phrasings — otherwise they change nothing.

## Self-annealing protocol

After every task:
- If an error occurred → fix the script and update the directive.
- If a better approach was found → update the skill file.
- If a new edge case appeared → add it to the SOP's edge cases section.

Nothing breaks the same way twice, because every failure becomes an edit to the system.
