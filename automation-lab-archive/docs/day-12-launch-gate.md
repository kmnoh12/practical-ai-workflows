# Day 12 launch gate — Practical AI Workflows

Date: 2026-07-06

## Scope

Day 12 reviewed the first 4 launch posts currently exported to the free GitHub Pages static site:

1. `creator-automation-stack-for-beginners`
2. `make-vs-zapier-for-creators`
3. `beehiiv-vs-kit-convertkit-for-solo-creators`
4. `notebooklm-vs-chatgpt-for-studying-pdfs`

## Decision

**Keep staging/noindex. Do not open indexing yet.**

Reason: the live site now has explicit official-source touchpoints and evidence gates, but it still lacks the article-specific screenshots, same-scenario tests, and final recommendation copy required by the editorial policy.

## Completed in Day 12

- Replaced vague live-site launch pages with explicit `day-12-evidence-gated` pages.
- Collected an official source ledger: `12_evidence/official-source-ledger-2026-07-06.md`.
- Added site manifest metadata for `base_path`, `last_day_completed`, and Day 12 status.
- Fixed GitHub Pages subpath behavior in the static build so nav/CSS links resolve under `/practical-ai-workflows`.
- Added QA checks for project-path assets and live robots/noindex blocking.

## Release gate matrix

| Post | Current status | Indexing decision | Blocker |
|---|---|---|---|
| Creator Automation Stack | `day-12-evidence-gated` | Keep blocked | Needs screenshots/pricing evidence for recommended tools. |
| Make vs Zapier | `day-12-evidence-gated` | Keep blocked | Needs same workflow run in Make/Zapier or explicitly labeled simulated analysis. |
| beehiiv vs Kit | `day-12-evidence-gated` | Keep blocked | Needs pricing/feature screenshot evidence and final decision table. |
| NotebookLM vs ChatGPT | `day-12-evidence-gated` | Keep blocked | Needs same-source test screenshots/output. |

## Day 13 target

Pick **one** post, preferably `notebooklm-vs-chatgpt-for-studying-pdfs` because it has the clearest source-grounded test design, and complete the evidence folder. Only then consider changing that single post from `noindex: true` to published/indexable.
