---
title: "How to Audit an AI-Generated Study Guide Against the Source"
description: "A practical claim-by-claim audit workflow for checking AI study guides, answer keys, examples, and source drift before you study from them."
slug: "how-to-audit-an-ai-generated-study-guide-against-the-source"
status: "published"
noindex: false
category: "AI Study Workflows"
order: 4
updated: "2026-07-10"
indexable: true
qa_approved: true
cta: "Audit Your AI Study Guide"
---

## Tested with

| Field | Value |
|---|---|
| Source | 1 synthetic PDF-style study handout |
| Runs | 1 NotebookLM run + 1 ChatGPT run |
| Audit artifacts | Raw outputs, source-claim map, scoring sheet, unsupported-claims log |
| Last checked | 2026-07-10 |

## What this is based on

This column uses the saved [public evidence pack](../notebooklm-chatgpt-pdf-study-evidence/), not a fresh benchmark or a memory of what the tools produced. The pack includes the source-equivalent notes, shared prompt, raw outputs, screenshots, scoring sheet, and claim-level follow-up.

## A polished study guide is still an unverified draft

The dangerous AI study guide is not necessarily the one full of absurd inventions. It is the one that reads cleanly, covers familiar concepts, and slips in a small explanation that the source never made.

That distinction matters because a study guide is meant to be rehearsed. If an unsupported sentence lands in an essay draft, you may catch it during revision. If it lands in an answer key, you can practice it until it feels true.

My rule is blunt: do not audit the guide as prose. Audit it as a set of claims.

That means breaking definitions, comparisons, examples, quiz answers, and study instructions into checkable units. Each unit gets a source location and a disposition: keep, rewrite, label, or remove. The job is not to decide whether the model "understood" the document. The job is to decide which pieces are safe to study.

The local evidence behind this column is deliberately narrow: **one synthetic handout, one NotebookLM run, and one ChatGPT run**. Both tools received the same source-equivalent text and the same prompt. This is not a benchmark, a student outcome study, or evidence that either product will behave the same way on another document. It is enough to show what a real audit trail looks like and why a claim ledger catches problems that a quick read can miss.

You can inspect the [same-source comparison](https://practical-ai-workflows.pages.dev/notebooklm-vs-chatgpt-for-studying-pdfs/) and its [public evidence pack](https://practical-ai-workflows.pages.dev/notebooklm-chatgpt-pdf-study-evidence/) before adopting the method.

## What the small test actually showed

The source was a one-page synthetic handout about attention, working memory, long-term memory, retrieval practice, spacing, recognition versus recall, and a three-day review plan. It also included a photosynthesis study example and defined a transfer question. The prompt told both tools to use only the provided source, create a study guide and ten-question quiz, identify three likely confusions, build a review plan, explain recognition versus recall, and write "Not in source" when support was absent.

Both runs mostly respected that boundary. NotebookLM reproduced the core definitions, quiz answers, example, and review plan. When the source supplied only recognition and recall as an explicit confusion, it declined to invent a third item. ChatGPT likewise marked its second and third confusion slots "Not in source." The local source-claim map found no major unsupported educational claims in ChatGPT's primary output.

One small drift is more instructive than a dramatic hallucination would have been. ChatGPT explained recognition with an answer-sheet scenario. That example was consistent with the source definition, but the handout did not contain the scenario. The audit logged it as a partial, explanatory extrapolation rather than a source fact.

Presentation created different problems. The captured NotebookLM export repeated section headings and included Korean source labels in otherwise English output. ChatGPT's captured response was in Korean and presented a cleaner hidden answer-key block, but it did not show source citations in the visible output. Those are workflow and formatting observations from one run, not universal product rankings.

The lesson is not that one model was accurate and the other was reckless. In this evidence, both were largely source-bound. The lesson is that even a good run needs labels. "Consistent with the source" and "stated in the source" are not the same thing.

## The exact audit workflow

Start with the original source and the complete generated packet side by side. Do not audit from memory, and do not use the AI's summary as a substitute for the document it summarized.

### 1. Freeze the inputs

Save the source, prompt, raw output, and run date before editing anything. If the tool received pasted text rather than the file itself, record that. In the local test, file-picker automation was unreliable, so NotebookLM received copied source text and ChatGPT received the same text under a `SOURCE:` label. That constraint belongs in the record because it describes what was actually tested.

Keep the raw output untouched. Make a separate working copy for corrections. Otherwise, later edits can erase the evidence of what the model originally produced.

### 2. Build a source map

List the source's sections and the concepts each section actually contains. For the synthetic handout, that map was compact:

| Source section | Auditable content |
|---|---|
| Core ideas | Definitions of attention, memory types, retrieval practice, spacing, and spaced retrieval |
| Example | Photosynthesis recall questions and the compare-and-repair step |
| Weak concept warning | Recognition versus recall |
| Three-day review plan | Exact Day 1, Day 2, and Day 3 tasks |
| Terms | Short definitions, including transfer question |

A source map gives you a coverage baseline. Without one, a fluent guide can omit a whole section and still feel complete.

For a fuller source-map workflow, see [How to Use NotebookLM to Study a PDF Without Losing the Source Trail](https://practical-ai-workflows.pages.dev/how-to-use-notebooklm-to-study-a-pdf-without-losing-the-source-trail/).

### 3. Atomize the output

Split compound sentences into individual claims. Consider this sentence from the NotebookLM output in substance: retrieval practice means recalling before checking, it feels harder than rereading, and that difficulty is part of the learning signal. That is three claims, even if the model put them in one bullet.

Create separate rows for:

1. definitions,
2. cause-and-effect statements,
3. comparisons,
4. quantities, dates, formulas, and named steps,
5. source examples,
6. generated examples,
7. quiz questions and every answer-key item,
8. review-plan instructions,
9. statements about what students are likely to confuse.

Do not waste time logging decorative transitions. Log statements a student might remember, repeat, cite, or use to answer a question.

### 4. Check each claim against the source

Use four support labels:

| Label | Meaning | Required action |
|---|---|---|
| `Supported` | The source directly states the claim or an equivalent formulation | Keep and record the source cue |
| `Partial` | Part is supported, or the wording adds an interpretation or example | Rewrite narrowly or label as explanation |
| `Unsupported` | No source passage supports the claim | Remove, or research separately outside this source-bound guide |
| `Not verifiable` | The available source is unreadable, incomplete, or too ambiguous to decide | Hold out of the guide until resolved |

Check the exact wording, not just the topic. A source can discuss spacing without saying "review every day." It can define recognition without using an answer-sheet example. Topic overlap is not sufficient support.

### 5. Audit coverage separately

Grounding asks, "Are the included claims supported?" Coverage asks, "Did the guide include the source's important material?" A guide can be perfectly grounded and still skip half the document.

Compare the source map with the guide. Mark each source section `covered`, `partly covered`, or `missing`. Then check whether the quiz tests only easy definitions or also includes the source's contrasts, examples, and application material.

In the local run, both outputs covered the handout's major concepts, the photosynthesis example, the recognition-recall distinction, and the three-day plan. That finding belongs to this single source and these single runs only.

### 6. Audit the answer key as its own document

Never assume that a grounded study guide produces a grounded quiz. Match every answer to the source independently. If a question cannot be answered from the assigned material, rewrite or delete it. If an answer is broader than the passage, narrow it.

Keep questions and answers paired in the ledger. This catches a particularly costly defect: a reasonable question with an overconfident answer. The local evidence recorded both tools' ten-question answer keys as source-aligned, but that result does not justify skipping the step on the next guide.

For a prompt sequence that includes an explicit answer-key pass, use [The ChatGPT Prompt I Use to Turn PDFs into Study Guides](https://practical-ai-workflows.pages.dev/the-chatgpt-prompt-i-use-to-turn-pdfs-into-study-guides/).

### 7. Repair, then run a final cold read

Apply the disposition in the ledger:

- Keep direct source facts with their cues.
- Rewrite partial claims to match the source.
- Label useful model-created explanations and examples.
- Remove unsupported material.
- Add important omissions from the source.

Then read the repaired guide without looking at the ledger. Check that labels remain visible and the prose does not quietly merge a generated example back into a source fact. Preserve a short `Check source` section for anything unresolved.

## The claim ledger

A claim ledger can be a spreadsheet or Markdown table. The format matters less than preserving the decision trail. Use these columns:

| ID | Output section | Atomic claim | Type | Source cue | Support | Disposition | Note |
|---|---|---|---|---|---|---|---|
| C-01 | Study guide | Attention selects some information for deeper processing while ignoring other information | Definition | Core ideas | Supported | Keep | Equivalent to source wording |
| C-02 | Study guide | Spacing distributes review over time rather than one cramming block | Definition | Core ideas | Supported | Keep | Direct match |
| C-03 | Weak concepts | A third likely confusion exists | Confusion claim | Weak concept warning | Unsupported | Remove | Source names only recognition versus recall |
| C-04 | Simple explanation | Looking at an answer sheet and feeling familiarity is recognition | Generated example | Weak concept warning | Partial | Label | Consistent illustration, not stated in source |
| C-05 | Review plan | Day 2 repeats the same questions without notes, adds two transfer questions, and reviews mistakes | Procedure | Three-day review plan | Supported | Keep | Direct match |

C-03 shows why refusal behavior matters. In the actual runs, neither tool made that unsupported claim. NotebookLM used "Not in source" for the third slot, while ChatGPT did so for the second and third slots because it treated recognition versus recall as one confused pair. The hypothetical row records what the ledger would do if a model filled the requested quota anyway.

C-04 captures the subtle case the local audit did find. Deleting the answer-sheet example would be defensible, but labeling it `Generated example` preserves its teaching value without misrepresenting the handout.

For larger guides, add `priority` and review high-risk rows first: definitions, numbers, formulas, named claims, causal statements, and answer keys. Priority is a triage device, not permission to treat unchecked claims as true.

## A failure taxonomy for study-guide audits

Not every category below appeared in the small local test. This is a reusable review taxonomy, with observed cases identified explicitly.

| Failure | What it looks like | Audit response |
|---|---|---|
| Fabrication | A fact, term, or relationship has no source support | Remove or verify from a separately approved source |
| Explanatory drift | A plausible metaphor, scenario, or interpretation is presented as if the source stated it | Label as generated or rewrite to the source wording |
| Compression error | Important conditions or distinctions disappear in simplification | Restore the limiting language |
| Coverage gap | A major source section never appears | Add it or disclose the omission |
| Quota filling | The model invents items to satisfy "give me three" when the source supports fewer | Require `Not in source`; shorten the list |
| Answer-key mismatch | The answer is wrong, broader than the source, or unsupported by the assigned text | Repair or remove the question |
| Provenance loss | Citations, section cues, or fact/explanation labels vanish during rewriting | Restore the source trail |
| Format contamination | Export artifacts, duplicated headings, or interface labels enter the final guide | Clean the copy while preserving raw evidence |
| Language mismatch | The response language differs from the requested or intended study language | Translate carefully, then re-audit translated claims |

The local evidence contains explanatory drift in ChatGPT's answer-sheet illustration, plus format contamination in NotebookLM's duplicated headings and Korean source labels. ChatGPT's captured answer was also in Korean. The runs did not supply evidence of major fabrication, answer-key mismatch, or broad coverage failure.

Quota filling deserves special attention because the prompt itself can cause it. Asking for three confused concepts when the source names one pair creates pressure to complete the list. Both tools handled that pressure well in this run. Your audit process should still assume that requested quantity is not evidence that the source contains that quantity.

## Copy the audit checklist

Copy this beside any AI-generated study guide:

- [ ] I saved the original source, prompt, raw output, and run date.
- [ ] I recorded whether the tool received the actual file or pasted source-equivalent text.
- [ ] I mapped every major source section before judging the guide.
- [ ] I split definitions, comparisons, examples, procedures, and quiz answers into atomic claims.
- [ ] Every important claim has a page, section, quotation, or other source cue.
- [ ] Each claim is marked `Supported`, `Partial`, `Unsupported`, or `Not verifiable`.
- [ ] Generated explanations and examples are visibly labeled.
- [ ] Source sections absent from the guide are added or disclosed.
- [ ] Every answer-key item was checked independently.
- [ ] Requested list lengths did not force invented coverage.
- [ ] Export artifacts and language mismatches were cleaned without altering the raw record.
- [ ] Unresolved items remain in a visible `Check source` list.
- [ ] The repaired guide received one final cold read.

## Limits

A completed ledger can establish that you compared a particular output with a particular source using explicit support rules. It can show where the guide matched, drifted, omitted material, or added teaching aids. It cannot prove that the source itself is correct, that the guide produces better retention, or that the same model will perform similarly on a different file.

The local evidence does not include real students, exam results, retention measurements, traffic data, or repeated runs. It is one synthetic handout, one NotebookLM run, and one ChatGPT run. The captured model selection for ChatGPT was not recorded, and both web inputs used source-equivalent text because local file selection was unreliable. Those limits are part of the finding, not footnotes to hide.

## Continue the series

- [Build a Source-to-Claim Map Before You Summarize a PDF](../build-a-source-to-claim-map-before-summarizing-a-pdf/)
- [Why AI Answer Keys Are the Riskiest Part of a Study Workflow](../why-ai-answer-keys-are-the-riskiest-part-of-study-workflows/)

## Bottom line

An audit is successful when the final guide makes provenance boringly obvious. You should be able to point from any important sentence to the source, distinguish the model's teaching aid from the author's claim, and delete anything that survives only because it sounds right. That is the standard worth applying before you rehearse the material.