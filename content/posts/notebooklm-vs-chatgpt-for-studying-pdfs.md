---
title: "NotebookLM vs ChatGPT for Studying PDFs: Same-Source Test"
slug: "notebooklm-vs-chatgpt-for-studying-pdfs"
status: "staging-evidence-captured-noindex"
noindex: true
category: "AI Study Workflows"
order: 1
updated: "2026-07-08"
cta: "PDF-to-Study-Guide Workflow Checklist"
---

# NotebookLM vs ChatGPT for Studying PDFs: A Same-Source Test

## Short verdict

This is the first public candidate article for Practical AI Workflows, but it is not indexable yet.

The first same-source capture is complete, but this page stays noindex until the ChatGPT source-check follow-up and final editorial QA are done. Initial scoring favors NotebookLM for source-grounding affordances, while study-guide usefulness, quiz quality, weak-concept handling, and review-plan quality are effectively tied in this small test.

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

Capture note: macOS file-picker automation was unreliable, so the captured run used source-equivalent copied text from the same evidence pack rather than a completed PDF upload. The PDF remains archived for repeat testing.

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

The initial score sheet has been filled from one NotebookLM run and one ChatGPT Pro web run using the same source text and prompt. The page remains noindex because final public QA is not complete.

## Results summary

### Results summary - initial captured run

| Criterion | NotebookLM | ChatGPT | Initial read |
|---|---|---|---|
| Source grounding | Strong, with visible citation/source affordances | Strong, but one simple-language example goes beyond exact source wording | NotebookLM edge |
| Study guide usefulness | Complete and structured | Complete and student-friendly | Tie |
| Quiz quality | 10 questions and answer key, source-aligned | 10 questions and hidden answer key, source-aligned | Tie |
| Weak-concept detection | Correctly says only recognition/recall are supported and third is not in source | Correctly says recognition vs recall, then Not in source for slots 2 and 3 | Tie |
| Review plan | Reproduces the source-specific 3-day plan | Reproduces the source-specific 3-day plan | Tie |
| Student safety | Better source/citation UI affordances | Good constraint following, fewer source affordances visible | NotebookLM edge |


## Source grounding

Initial claim mapping found both outputs mostly source-grounded. NotebookLM had the stronger source-verification affordance because its answer included source/citation chips in the visible UI. ChatGPT followed the source constraint well, but its simple-language answer-sheet example is an explanatory extrapolation rather than a direct source claim.

## Study guide quality

Both outputs covered attention, working memory, long-term memory, retrieval practice, spacing, recognition, recall, transfer questions, the photosynthesis example, and the three-day review plan. ChatGPT read more like a student-facing Korean explanation; NotebookLM read more like a citation-backed source summary.

## Quiz quality

Both tools created 10 source-aligned quiz questions with answer keys. The answer keys matched the source in the initial claim map. ChatGPT used a hidden answer-key details block; NotebookLM included source markers/citation chips around answer statements.

## Weak concepts and review plan

Both tools handled the “three concepts likely to confuse” trap correctly: the source only supports recognition vs recall, so both refused to invent unsupported extra confusion concepts. Both reproduced the Day 1/Day 2/Day 3 retrieval and repair loop from the source.

## What each tool got wrong

Initial review found no major unsupported educational claims in either primary output. ChatGPT added a small answer-sheet example to explain recognition vs recall; that is consistent with the source definition but not directly stated in the source, so it is logged as partial/explanatory rather than a source fact. A ChatGPT self-check follow-up is still required before removing noindex.

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
3. The archived PDF is one page; local extraction found 196 PDF text-stream word tokens and 318 source Markdown word tokens.
4. The captured web run used source-equivalent copied text because file-picker automation was unreliable.
5. ChatGPT model details beyond the Pro web session were not captured.
6. Tool updates can change results.
7. No real student exam outcome is measured.
8. Screenshots were automatically redacted for account/sidebar areas, but still need final human review before public indexing.

## Evidence archive

The evidence package is kept near the article but should be treated as a pre-publication archive until the missing captures exist. The links below point to the source-repo evidence package for staging review; before public indexing, publishable evidence artifacts must either be copied into the static `dist/` output or converted to stable public evidence URLs.

| Evidence item | Link or status |
|---|---|
| Source PDF | [same-source-study-notes.pdf](../../docs/day-13-notebooklm-evidence-pack-files/same-source-study-notes.pdf) |
| Source notes | [same-source-study-notes.md](../../docs/day-13-notebooklm-evidence-pack-files/same-source-study-notes.md) |
| Shared prompt | [same-source-prompt.txt](../../docs/day-13-notebooklm-evidence-pack-files/same-source-prompt.txt) |
| Evaluation rubric | [evaluation-rubric.md](../../docs/day-13-notebooklm-evidence-pack-files/evaluation-rubric.md) |
| Evidence manifest | [evidence-manifest.md](../../docs/day-13-notebooklm-evidence-pack-files/evidence-manifest.md) |
| NotebookLM raw output | [notebooklm-output.md](../../docs/day-13-notebooklm-evidence-pack-files/notebooklm-output.md) |
| ChatGPT raw output | [chatgpt-output.md](../../docs/day-13-notebooklm-evidence-pack-files/chatgpt-output.md) |
| Scoring sheet | [scoring-sheet.csv](../../docs/day-13-notebooklm-evidence-pack-files/scoring-sheet.csv) |
| Unsupported claims log | [unsupported-claims-log.md](../../docs/day-13-notebooklm-evidence-pack-files/unsupported-claims-log.md) |
| Source claim map | [source-claim-map.md](../../docs/day-13-notebooklm-evidence-pack-files/source-claim-map.md) |
| Screenshots folder | [screenshots/README.md](../../docs/day-13-notebooklm-evidence-pack-files/screenshots/README.md) |

## Final recommendation

Initial single-run recommendation: NotebookLM has the edge when the priority is source-grounding workflow and visible source affordances. ChatGPT is just as useful for a student-facing explanation in this small test, and its quiz/review-plan output was competitive.

The best workflow is still not “trust one tool.” Use one tool to generate the study guide, then check atomic claims against the source, log unsupported claims, and turn missed concepts into retrieval practice. Do not use NotebookLM or ChatGPT as a final authority without checking the source.

## Pre-publication checklist and transparency notes

This article must remain `noindex: true` until ChatGPT source-check follow-up, final editorial QA, and static build QA pass.

Before public indexing:

| Gate | Required state |
|---|---|
| Raw outputs | NotebookLM and ChatGPT raw outputs saved — done |
| Screenshots | Source upload, prompt, outputs, quiz, citations/source checks, and settings captured |
| Same-source integrity | Same PDF, prompt, rubric, and capture rules confirmed |
| Model/settings log | ChatGPT model/plan/tools and NotebookLM settings recorded |
| Claim trace | At least 20 atomic claims per tool checked — initial pass done |
| Unsupported claims log | Filled from source checks |
| Scoring sheet | Filled from captured outputs only — initial pass done |
| Winner claims | Based only on measured evidence |
| noindex | Keep `true` until all evidence and QA gates pass |
| Sitemap | Do not include a public/indexable URL before approval |

I checked official product docs because both tools change. NotebookLM describes source-grounded citations in its help documentation, and ChatGPT supports file uploads for summarization, transformation, and extraction. This test does not assume either tool is always accurate.

Official source touchpoints:

- [NotebookLM](https://notebooklm.google/)
- [Learn about NotebookLM](https://support.google.com/notebooklm/answer/16164461?co=GENIE.Platform%3DDesktop&hl=en)
- [Use chat in NotebookLM](https://support.google.com/notebooklm/answer/16179559?hl=en)
- [OpenAI File Uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)
