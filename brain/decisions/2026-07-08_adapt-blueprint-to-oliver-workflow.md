# Decision: Adapt the Second Brain Blueprint to Oliver's real workflow, not the agency example

**Date:** 2026-07-08
**Status:** decided

## The decision
This repository follows the DOE architecture from the Second Brain Blueprint (Doby Lanete, 2026-07-05) but is organized around Oliver's actual work — Expanded Learning program leadership and training-system building — instead of the blueprint's agency/client model.

## The reasoning
The blueprint's author runs a client-services agency; Oliver's work as mined from his own documents is project-shaped (work plans, enrichment design, staff training, the Team Lead Toolkit). Copying the agency taxonomy would have produced empty client folders and missing project structure — an architecture describing someone else's business.

## What changed concretely
- Added a first-class `projects/` layer; `clients/` kept but dormant until a client-shaped relationship exists.
- Context files renamed to Oliver's vocabulary: `work.md`, `goals_and_vision.md`, `writing_style.md`, `philosophy.md`, `workflows.md`.
- First real directive is the weekly work plan (see [[2026-07-08_work-plan-format]]), not the blueprint's content-marketing examples.

## Alternatives rejected
- Mirroring the PDF structure verbatim — rejected: the folder must describe Oliver's business, since the folder is the asset.

## Revisit if
Oliver starts client-shaped work (tutoring, consulting, freelance) — then activate `clients/` with `templates/client/`.

## Related
- [[2026-07-08_intern-to-team-lead-workshop]] — the material that revealed the real workflow
