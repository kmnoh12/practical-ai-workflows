---
title: "Build a Source-to-Claim Map Before You Summarize a PDF"
description: "A practical source-to-claim mapping workflow for verifying PDF notes, controlling source drift, and handing clean evidence from NotebookLM to ChatGPT."
slug: "build-a-source-to-claim-map-before-summarizing-a-pdf"
status: "published"
noindex: false
category: "AI Study Workflows"
order: 6
updated: "2026-07-10"
indexable: true
qa_approved: true
cta: "Copy the Source-to-Claim Map Template"
---

## Tested with

| Field | Value |
|---|---|
| Source | 1 synthetic PDF-style study handout |
| Runs | 1 NotebookLM run + 1 ChatGPT run |
| Mapping artifact | Completed source-claim map with claim-level support decisions |
| Last checked | 2026-07-10 |

## What this is based on

The worked rows come from the site's [public evidence pack](../notebooklm-chatgpt-pdf-study-evidence/). The broader schema and decision rules are a reusable editorial method, not evidence that the small local run measured every possible PDF failure.

## A summary is the wrong first artifact

A PDF summary compresses. A source-to-claim map controls the compression.

That distinction matters because the first AI response often becomes the hidden foundation for everything that follows: the study guide, quiz, memo, slide deck, or executive brief. If an unsupported interpretation enters at that stage, later prompts can polish and repeat it until it looks like part of the document.

A source-to-claim map interrupts that process. It is a compact ledger in which each important claim is paired with a location in the PDF, an evidence status, and a decision about how the claim may be used. It does not need to read well. It needs to make checking cheap.

The practical sequence is:

1. map the document,
2. break the proposed summary into atomic claims,
3. locate support for each claim,
4. classify the support,
5. resolve weak rows,
6. summarize only the verified set.

This adds a verification pass before prose generation. It also produces a reusable artifact that can move safely between tools.

## What the artifact contains

The smallest useful map has six fields:

| Field | What belongs there | Why it exists |
|---|---|---|
| `ID` | Stable label such as `C-07` | Lets prompts and reviewers refer to a claim without copying it. |
| `Claim` | One checkable proposition | Prevents several assertions from hiding in one sentence. |
| `Source location` | Page, section, table, figure, or exact source cue | Provides a route back to the PDF. |
| `Support` | `supported`, `partial`, `unsupported`, or `unclear` | Makes uncertainty visible. |
| `Evidence` | Short quote, faithful paraphrase, or visual/table note | Records what the classification is based on. |
| `Action` | `keep`, `rewrite`, `verify`, `label`, or `remove` | Converts review into an editorial decision. |

For serious work, add four more fields:

- `Claim type`: definition, number, causal statement, comparison, recommendation, interpretation, or example.
- `Scope/conditions`: population, date range, exceptions, assumptions, or experimental conditions.
- `Layer`: source fact, source-based interpretation, or generated teaching material.
- `Reviewer note`: the reason a row was changed or accepted.

The map should contain claims, not topics. "Working memory" is a topic. "Working memory temporarily holds a small amount of information for manipulation" is a claim. "The report discusses falling costs" is too vague. "The report states that unit cost fell 12 percent from 2024 to 2025" can be checked.

One row should normally contain one proposition. If a sentence uses `and`, `therefore`, `because`, `best`, `more effective`, or a numerical comparison, test whether it needs multiple rows. A sentence can have a supported first half and an unsupported second half.

## Build the map in five passes

### 1. Check whether the PDF is readable

Before asking for claims, inspect extraction quality. A clean prose PDF, a scanned report, and a slide deck exported as PDF are different inputs. Tables may lose columns. Footnotes may attach to the wrong paragraph. Page numbers in a viewer may differ from printed page numbers. OCR can turn decimal points, minus signs, and proper names into new facts.

Record these defects at the top of the map. If a key table is unreadable, mark claims from it `unclear`; do not let a model reconstruct the values from context.

### 2. Inventory the document before interpreting it

Ask for title, section hierarchy, appendices, tables, figures, and obvious gaps. This coverage pass gives you a denominator. Without it, a summary may faithfully describe three easy sections while silently omitting the fourth.

A suitable first prompt in NotebookLM is:

```text
Use only the uploaded source. Do not summarize it yet.
List the document's sections, tables, figures, and appendices.
For each, give a source cue and one sentence describing its function.
If text or a visual is unreadable, mark it Unclear.
Do not infer missing content.
```

Compare that inventory with the PDF's table of contents and visible pages. Source-grounded interfaces reduce navigation friction, but the original file remains the authority.

### 3. Extract atomic claims

Now ask for the claims that a useful summary would need. Require one proposition per row and request source cues. Avoid fixed quotas when the source may not support them. "Find exactly ten risks" pressures the output to fill slots. "List the risks explicitly supported by the source" permits a short, honest result.

```text
Create an atomic claim list from the uploaded source.
Each row must contain one checkable proposition.
Include the source section and page or citation cue.
Separate source claims from your interpretations.
If the source does not support a requested item, write Not in source.
```

### 4. Verify and classify each row

Open the cited location. Read enough surrounding material to capture qualifiers, not just the matching sentence. Then assign one of four statuses:

- `supported`: the source directly supports the claim at the stated scope.
- `partial`: part is supported, but wording, scope, causality, or detail goes beyond the source.
- `unsupported`: no adequate support appears in the provided document.
- `unclear`: extraction, citation, visual quality, or context prevents a reliable decision.

Do not use `partial` as a polite synonym for "probably true." It means the row can identify exactly which part survives and which part must change.

### 5. Resolve the map before writing prose

A map is not finished when every row has a label. It is finished when every row has an action.

Supported claims can enter the summary. Partial claims should be narrowed. Unsupported claims should be removed or explicitly presented as outside analysis, with separate evidence. Unclear claims should remain out until someone checks the original page, table, or image.

Only then ask for a summary, and tell the model to use claim IDs. That makes the transformation auditable:

```text
Write a concise summary using only rows marked Keep.
Preserve the scope and conditions in those rows.
Do not merge claims if doing so creates a new causal or comparative claim.
After each paragraph, list the claim IDs used.
Put any missing information in a separate Gaps section.
```

## A worked example from the local test

The site's local same-source test used one synthetic, one-page study handout about attention, memory, retrieval practice, spacing, recognition, and recall. The same source-equivalent text and one prompt were used for one captured NotebookLM run and one captured ChatGPT run. The repository's claim map checked the outputs against the saved source.

A few rows illustrate the method:

| ID | Output claim | Source support | Decision |
|---|---|---|---|
| `C-01` | Retrieval practice means recalling information before looking at the answer. | Supported by the handout's `Core ideas` section. | Keep. |
| `C-02` | Spaced retrieval combines recall, waiting, and later recall. | Supported by `Core ideas`. | Keep. |
| `C-03` | Three concepts are explicitly identified as likely confusions. | Unsupported. The source names only recognition versus recall. | Remove; report only one pair. |
| `C-04` | Looking at an answer sheet and feeling familiarity is recognition. | Partial. It is consistent with the definition, but the answer-sheet scenario is an added explanation. | Label as generated explanation, not source fact. |

Both captured outputs handled the forced three-item confusion request conservatively. NotebookLM named recognition and recall, then said the third item was not in the source. ChatGPT listed the supported pair and marked items two and three `Not in source`. The local follow-up found no major unsupported educational claim in ChatGPT's primary output. It did log the answer-sheet scenario as a minor explanatory extrapolation.

That is useful workflow evidence, but its scope is narrow. This was one synthetic handout, one prompt, and one captured run per tool. Copied source-equivalent text was used because local file-picker automation was unreliable. No real textbook chapter, research paper, scanned PDF, repeated-run reliability, retention outcome, or exam result was tested. The run does not establish a general accuracy ranking. It shows how a claim map can record supported statements, source-bound refusals, and a small layer shift without pretending they are equivalent.

The raw materials, rubric, unsupported-claims log, and completed map are available in the [public evidence pack](../notebooklm-chatgpt-pdf-study-evidence/).

## Limits

A source-to-claim map improves traceability. It does not prove that the source itself is correct, repair unreadable OCR, or turn one successful check into a model accuracy rate. For high-stakes material, the reviewer still has to open the original page, table, or figure.

## How the map prevents source drift

Source drift is usually incremental. A source says, "retrieval feels harder than rereading, and the difficulty is part of the learning signal." A summary shortens that to "harder studying improves learning." A quiz asks, "Why should study always feel difficult?" The answer key then treats discomfort as the mechanism. Each step sounds related, but the final lesson is not what the source said.

The map blocks several routes into that chain:

1. **Atomic rows expose added logic.** A paraphrase and its new causal conclusion cannot share one status.
2. **Scope fields preserve qualifiers.** "In this sample," "may," and "under these conditions" do not disappear during compression.
3. **Layer labels separate evidence from pedagogy.** A useful metaphor can remain, but it cannot masquerade as a quotation or finding.
4. **Stable IDs survive tool handoffs.** ChatGPT can transform `C-01` without receiving permission to improvise `C-19`.
5. **Decision fields close the loop.** Weak claims are rewritten or removed rather than left in an uncertainty appendix that nobody reads.
6. **Coverage inventory catches omission drift.** The result can show which sections were not summarized, rather than implying complete coverage.

This does not guarantee truth. A reviewer can misread a page, a citation can point to incomplete context, and a PDF parser can corrupt a table. The map provides traceability and a place to record those failures. It makes errors easier to find before they propagate.

## Hand verified NotebookLM notes to ChatGPT

NotebookLM is useful for the source-facing pass because its workflow keeps uploaded sources and citation cues close to the answer. The handoff to ChatGPT should be a bounded evidence packet, not the entire conversation transcript.

First, verify NotebookLM's important rows against the PDF. Then export only:

1. document metadata and extraction warnings,
2. supported claims with IDs and source cues,
3. narrowed wording for partial claims,
4. separately labeled source examples,
5. an unresolved list that ChatGPT may not fill,
6. the exact transformation task.

Do not paste a citation number without the associated claim and cue. Do not include a rejected claim merely because its row says `unsupported`; models can repeat text supplied in negative instructions. Put rejected material in a short prohibition list or omit it entirely.

Use a handoff prompt like this:

```text
The VERIFIED CLAIMS block below is the complete source of truth for this task.
Use only claims marked KEEP. Preserve their IDs, scope, and qualifications.
Do not add background knowledge, citations, examples, causes, or comparisons.
Items under UNRESOLVED are gaps, not prompts to infer an answer.
If the requested output needs information not present here, write Check source.
Label any example you create Generated example.
For every answer-key item, include the supporting claim ID.
```

ChatGPT can then generate explanations, short-answer questions, application questions, or a review plan. Require IDs in the answer key. Audit any generated example for whether it changes the meaning of the source claim. The model is doing learning design, not evidence discovery.

## Copy the source-to-claim map template

```markdown
# Source-to-claim map

## Document record
- Title:
- File/version/date:
- Reviewed on:
- Printed page vs viewer page convention:
- Extraction/OCR warnings:
- Sections or visuals not readable:
- Intended output:

## Claim map

| ID | Claim | Type | Source location | Evidence or faithful excerpt | Scope/conditions | Support | Layer | Action | Reviewer note |
|---|---|---|---|---|---|---|---|---|---|
| C-01 |  | definition / number / causal / comparison / recommendation / interpretation / example | p. / section / table / figure |  |  | supported / partial / unsupported / unclear | source fact / source interpretation / generated material | keep / rewrite / verify / label / remove |  |

## Coverage check

| Source section | Represented by claim IDs | Omitted intentionally? | Reason |
|---|---|---|---|
|  |  | yes / no |  |

## Resolved partial claims
- Original ID:
- Safe wording:
- Removed wording:
- Reason:

## Unresolved
- Claim or question:
- What must be checked:
- Owner:

## Verified handoff
### KEEP
- [C-__] Claim. Source cue. Scope.

### GENERATED EXAMPLES ALLOWED
- [C-__] Constraints for the example.

### UNRESOLVED: DO NOT INFER
- [U-__] Unavailable or unreadable information.

### TASK
- Requested transformation:
- Required claim-ID references:
- Output format:
```

## Decision rules for real work

Use these rules before a claim enters the verified handoff:

1. **No location, no keep.** If a material claim cannot be routed back to the PDF, mark it `verify` or remove it.
2. **One proposition per row.** Split bundled definitions, comparisons, and causal chains.
3. **A nearby citation is not enough.** Read the surrounding paragraph, note, table title, and qualifiers.
4. **Numbers get direct checks.** Verify units, sign, denominator, time period, and whether the value is estimated or observed.
5. **Causality needs causal language in the source.** Association, sequence, or comparison does not become cause through summarization.
6. **Narrow partial claims.** Keep only the supported portion. Do not average supported and unsupported wording into a vague sentence.
7. **Examples retain provenance.** Mark them `source example` or `generated example`.
8. **Unclear is a valid stopping point.** Never repair unreadable tables or OCR from plausibility.
9. **Fixed list length cannot override evidence.** Return fewer items or `Not in source` rather than filling a quota.
10. **High-stakes claims return to the original PDF.** Definitions, formulas, names, dates, recommendations, and answer keys deserve manual checking.
11. **Handoffs contain verified material, not raw model output.** Preserve IDs and exclusions.
12. **The final summary gets a coverage check.** Record omitted sections and confirm that prose did not create a new claim by combining rows.

## Continue the series

- [How to Audit an AI-Generated Study Guide Against the Source](../how-to-audit-an-ai-generated-study-guide-against-the-source/)
- [Why AI Answer Keys Are the Riskiest Part of a Study Workflow](../why-ai-answer-keys-are-the-riskiest-part-of-study-workflows/)

## Bottom line

A good source-to-claim map is intentionally plain. It shifts effort from polishing sentences to controlling what those sentences are allowed to say. Once that control layer exists, NotebookLM can help navigate the document and ChatGPT can help shape verified notes into useful material. The PDF remains the authority, and every important sentence keeps a route back to it.
