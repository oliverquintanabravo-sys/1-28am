# Design: render_work_plan.py

**Status:** SUPERSEDED in practice (2026-07-08) — Oliver asked for a shareable, model-independent tool immediately, so the blueprint below was implemented client-side as **`execution/render_work_plan.html`**: a single-file, zero-dependency browser app (same input contract, same parse/validate/render logic, plus download/print/share). Browser-tested: 5 days render, standards checkboxes correct, downloaded copies work standalone. The Python variant stays unbuilt unless a server-side/batch need appears. The open questions below still need Oliver's answers to finalize the official delivery format.

## Job
Deterministically convert an AI+Oliver-authored markdown work plan into the Center's official "Weekly Team Leader Work Plans" layout. Content decisions stay upstream (AI + Oliver); this script is formatting only — same input, same output, forever.

## Input contract: `plan.md`
One markdown file per week, structured exactly as:

```markdown
---
site: Sierra View
team_leader: Mr. Oliver
week_of: 2026-08-24
---

## Monday — STEM
standards: 1, 2, 3
### Academic Support & Literacy
- ...
### Structured Physical Activity
- ...
### Enrichment
Objective/Description: ...
### Plan B
- ...
### Materials
- paper cups (1 per student)
```

(One `##` block per program day, Monday–Friday; headings fixed; `standards:` line lists checked boxes.)

## Parsing logic
1. Read YAML front matter → header fields (site, team_leader, week_of).
2. Split body on `## {Day} — {Initiative}` headings; validate exactly Mon–Fri present, in order.
3. Within each day, split on the four fixed `###` sections + optional Plan B; `standards:` line parsed into a subset of {1,2,3,4,5,6,6a}.
4. **Fail loudly on any missing day, missing section, empty Materials, or unknown standard token** — a render must never silently produce an incomplete official form (plans are grant/district documents and substitute scripts).

## Rendering logic
- Template target: the official field order per day —
  `{Day} Initiative:` → `*Quality Standards: ☐/☑ 1–6a` → `Materials:` → `Academic Support & Literacy:` → `Structured Physical Activity:` → `Enrichment:` + `Objective/Description:`
- Checkbox row rendered with ☑ for listed standards, ☐ otherwise.
- Plan B appended inside the Enrichment cell (the official form has no Plan B field; policy still requires having one).
- Output format, in order of preference — decide with Oliver:
  a. **HTML file** styled to match the form, printable to PDF (zero dependencies, easy to eyeball) ← recommended default
  b. `.docx` built from `Edited Work Template Doc .docx` as the base (python-docx dependency; closest to "official")
  c. Plain-text layout for pasting into the drive doc
- Deterministic file naming: `.tmp/workplans/{week_of}_workplan.{ext}` (never committed; delivered per SOP step 9).

## Validation hooks (same run)
- Warn if any day has < 2 standards checked, or 1/2 missing during Aug–Nov (dates derived from `week_of`).
- Warn if Wednesday's blocks don't exceed other days' (minimum-day longer hours).
- Exit non-zero on errors, zero-with-warnings otherwise, so the SOP can gate on it.

## Open questions for Oliver (blocking)
1. [WHICH FORMAT DOES YOUR PROGRAM MANAGER ACTUALLY ACCEPT — Google Doc, PDF, printed sheet?]
2. [WHAT IS THE REAL DUE DATE/CADENCE — Friday prior? Monday morning?]
3. [DOES THE OFFICIAL FORM EVER CHANGE PER DISTRICT/YEAR?]
