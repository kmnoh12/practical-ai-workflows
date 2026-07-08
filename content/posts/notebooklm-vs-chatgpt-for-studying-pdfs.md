---
title: "NotebookLM vs ChatGPT for Studying PDFs: Same-Source Test"
slug: "notebooklm-vs-chatgpt-for-studying-pdfs"
status: "day-15-public-candidate-evidence-required"
noindex: true
category: "AI Study Workflows"
order: 1
updated: "2026-07-08"
cta: "PDF-to-Study-Guide Workflow Checklist"
---

# NotebookLM vs ChatGPT for Studying PDFs: A Same-Source Test

## Short verdict

This is the first public candidate article for Practical AI Workflows, but it is not indexable yet.

No winner is declared here because the required raw outputs, screenshots, scoring sheet, and unsupported-claim checks have not been captured. The final verdict will be evidence-based and situation-specific: source grounding, study guide quality, quiz quality, and review planning may point to different tools.

Do not use either tool as a final authority without checking the PDF.

## What I tested

This comparison is designed around one controlled study PDF, one shared prompt, one measurement rubric, and the same capture rules for both tools.

The test question is narrow:

> If a student gives NotebookLM and ChatGPT the same PDF and the same study prompt, which output is more useful and safer for learning?

The final version of this article will include the test date, visible tool/model details, screenshots, raw outputs, claim-level checks, and a filled scoring sheet. Until those items exist, this page remains a pre-publication scaffold.

## Why this test matters

Students do not need generic AI summaries. They need source-grounded notes, useful retrieval practice, accurate answer keys, and a way to catch claims that drift away from the PDF.

This test matters because the risky failure mode is subtle. An AI output can sound helpful while adding unsupported facts, skipping important source concepts, or creating quiz answers that do not match the material. A same-source test makes that easier to inspect.

## The source PDF

The source is a synthetic, narrow study handout about attention, working memory, long-term memory, retrieval practice, spacing, recognition, recall, and a three-day review plan.

Local metadata currently available:

| Field | Value |
|---|---|
| PDF file | `same-source-study-notes.pdf` |
| Page count | 1 page |
| PDF text-stream word tokens | 196 |
| Source Markdown word tokens | 318 |
| Source type | Synthetic notes created for this evidence pack |

The final capture pass should verify that the uploaded PDF renders as expected in both tools before scoring outputs.

## The exact prompt

Readers can copy this prompt for their own source-grounded PDF study tests:

```text
Use only the provided source. Do not add outside facts.

Tasks:
1. Create a one-page study guide.
2. Create 10 quiz questions with answers hidden under an answer key.
3. Identify the three concepts a student is most likely to confuse.
4. Build a three-day review plan.
5. Explain the difference between recognition and recall in simple language.

If the source does not support a claim, write: Not in source.
```

This prompt tests four things: source grounding, quiz quality, weak-concept detection, and review planning.

The central constraint is "Use only the provided source." Without it, the test becomes a generic writing comparison instead of a PDF-grounded study workflow comparison. The "Not in source" instruction is a source-drift trap: if a tool invents unsupported material instead of admitting the source does not support it, that matters for the final score.

## How I scored the outputs

The final scoring will use measurement-oriented criteria rather than a vague preference ranking.

| Criterion | Measurement |
|---|---|
| Source grounding | Ratio of atomic claims that are supported by the source |
| Unsupported claims | Count of claims that are not in the source |
| Citation usefulness | Whether a citation or quote lets the reader verify the claim |
| Study guide coverage | Number of source key concepts included |
| Quiz quality | Recognition, recall, and application question mix |
| Answer key accuracy | Share of answers that match the source |
| Weak concepts | Whether likely source-specific confusions are identified |
| Review plan | Whether retrieval, spacing, and a repair loop are included |
| Student safety | Whether the output warns readers to verify and source-check |

The score sheet should be filled only after both tools have been run with the same PDF and the same prompt.

## Results summary

### Results summary - pending capture

The results table below describes the fields that will be filled after evidence capture. It does not contain scores yet.

| Criterion | NotebookLM field to fill | ChatGPT field to fill | Winner rule | Evidence required |
|---|---|---|---|---|
| Source grounding | Supported-claim ratio and unsupported-claim count | Supported-claim ratio and unsupported-claim count | Higher supported ratio, fewer unsupported claims | Claim map and unsupported claims log |
| Study guide usefulness | Covered source concepts, missing concepts, structure notes | Covered source concepts, missing concepts, structure notes | More complete and usable study guide | Raw output and scoring sheet |
| Quiz quality | Recognition/recall/application mix and answer-key accuracy | Recognition/recall/application mix and answer-key accuracy | Better retrieval practice with accurate answers | Quiz output and answer-key check |
| Weak-concept detection | Source-specific confusions identified | Source-specific confusions identified | More accurate source-specific weak concepts | Claim map and raw output |
| Review plan | Retrieval, spacing, and repair loop present or absent | Retrieval, spacing, and repair loop present or absent | More actionable source-specific plan | Raw output and scoring sheet |
| Student safety | Verification/source-checking warnings | Verification/source-checking warnings | Better warnings against unsupported use | Raw output and scoring sheet |

## Source grounding

This section will answer: which tool stayed closer to the PDF?

The final version should include unsupported-claim counts, citation behavior, source-check examples, and links to the raw outputs or screenshots. NotebookLM citations and ChatGPT file-upload behavior are feature-scope reasons to run this test, not proof that either answer is accurate.

## Study guide quality

This section will compare structure, completeness, missing concepts, clarity, and usefulness for a student.

The source concepts to check include attention, working memory, long-term memory, retrieval practice, spacing, recognition, recall, transfer questions, and the three-day review plan.

## Quiz quality

This section will compare whether each tool creates useful retrieval practice instead of only recognition-style questions.

The final scoring should classify quiz questions as recognition, recall, or application, then check the answer key against the source.

## Weak concepts and review plan

This section will compare whether each tool identifies likely confusions from the source and builds a useful review loop.

The expected review-plan elements are retrieval practice, spacing, and repair of missed concepts. A generic plan that does not respond to the source should score lower.

## What each tool got wrong

This section is mandatory before publication.

It should name unsupported claims, missing source concepts, weak quiz items, inaccurate answer-key entries, overconfident recommendations, and any place where a tool ignored the "Not in source" instruction.

## Recommended workflow

The evidence-backed workflow should be:

1. Upload the PDF.
2. Ask for a source-grounded study guide.
3. Ask for quiz questions with an answer key.
4. Check atomic claims against the PDF.
5. Log unsupported claims.
6. Turn missed concepts into a three-day retrieval plan.

## Use NotebookLM when...

Use NotebookLM when the final source-grounding score shows it stays closer to the uploaded PDF, exposes useful citations or source references, and produces fewer unsupported claims.

This is pending capture. The article should not claim NotebookLM is the better choice until the claim map and scoring sheet support it.

## Use ChatGPT when...

Use ChatGPT when the final study-guide, clarity, formatting, quiz, or review-plan scores show a measurable advantage.

This is pending capture. The article should not claim ChatGPT is the better choice until the captured output supports it.

## Use both when...

Use both only with a source-checking workflow: compare outputs, verify claims against the PDF, log unsupported claims, and convert weak spots into retrieval practice.

The best workflow may end up being tool-specific, but the current safe recommendation is verification first.

## Limitations

This page is still pre-publication. Known limitations:

1. The test uses one source and one prompt.
2. The source is a synthetic English study handout.
3. The PDF is one page; local extraction found 196 PDF text-stream word tokens and 318 source Markdown word tokens, so the final capture pass should verify the uploaded PDF rendering.
4. ChatGPT plan and model are pending capture.
5. ChatGPT tools enabled are pending capture.
6. NotebookLM account/plan and settings are pending capture.
7. Runs per tool and regeneration status are pending capture.
8. Tool updates can change results.
9. No real student exam outcome is measured.

## Evidence archive

The evidence package is kept near the article but should be treated as a pre-publication archive until the missing captures exist. The links below point to the source-repo evidence package for staging review; before public indexing, publishable evidence artifacts must either be copied into the static `dist/` output or converted to stable public evidence URLs.

| Evidence item | Link or status |
|---|---|
| Source PDF | [same-source-study-notes.pdf](../../docs/day-13-notebooklm-evidence-pack-files/same-source-study-notes.pdf) |
| Source notes | [same-source-study-notes.md](../../docs/day-13-notebooklm-evidence-pack-files/same-source-study-notes.md) |
| Shared prompt | [same-source-prompt.txt](../../docs/day-13-notebooklm-evidence-pack-files/same-source-prompt.txt) |
| Evaluation rubric | [evaluation-rubric.md](../../docs/day-13-notebooklm-evidence-pack-files/evaluation-rubric.md) |
| Evidence manifest | [evidence-manifest.md](../../docs/day-13-notebooklm-evidence-pack-files/evidence-manifest.md) |
| NotebookLM raw output | `notebooklm-output.md` pending capture |
| ChatGPT raw output | `chatgpt-output.md` pending capture |
| Scoring sheet | [scoring-sheet.csv](../../docs/day-13-notebooklm-evidence-pack-files/scoring-sheet.csv) |
| Unsupported claims log | [unsupported-claims-log.md](../../docs/day-13-notebooklm-evidence-pack-files/unsupported-claims-log.md) |
| Source claim map | [source-claim-map.md](../../docs/day-13-notebooklm-evidence-pack-files/source-claim-map.md) |
| Screenshots folder | [screenshots/README.md](../../docs/day-13-notebooklm-evidence-pack-files/screenshots/README.md) |

## Final recommendation

No single winner yet.

For PDF content that must not drift from the source, the winner is pending the source-grounding score. For flexible explanation and formatting, the winner is pending the study-guide and clarity score. For quiz and retrieval practice, the winner is pending the quiz and answer-key score.

The best workflow is already clear: use a source check, claim log, and review loop. Do not use NotebookLM or ChatGPT as a final authority without checking the PDF.

## Pre-publication checklist and transparency notes

This article must remain `noindex: true` until the evidence package is complete and QA passes.

Before public indexing:

| Gate | Required state |
|---|---|
| Raw outputs | NotebookLM and ChatGPT raw outputs saved |
| Screenshots | Source upload, prompt, outputs, quiz, citations/source checks, and settings captured |
| Same-source integrity | Same PDF, prompt, rubric, and capture rules confirmed |
| Model/settings log | ChatGPT model/plan/tools and NotebookLM settings recorded |
| Claim trace | At least 20 atomic claims per tool checked |
| Unsupported claims log | Filled from source checks |
| Scoring sheet | Filled from captured outputs only |
| Winner claims | Based only on measured evidence |
| noindex | Keep `true` until all evidence and QA gates pass |
| Sitemap | Do not include a public/indexable URL before approval |

I checked official product docs because both tools change. NotebookLM describes source-grounded citations in its help documentation, and ChatGPT supports file uploads for summarization, transformation, and extraction. This test does not assume either tool is always accurate.

Official source touchpoints:

- [NotebookLM](https://notebooklm.google/)
- [Learn about NotebookLM](https://support.google.com/notebooklm/answer/16164461?co=GENIE.Platform%3DDesktop&hl=en)
- [Use chat in NotebookLM](https://support.google.com/notebooklm/answer/16179559?hl=en)
- [OpenAI File Uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)
