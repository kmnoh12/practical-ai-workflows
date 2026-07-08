# Source claim map - NotebookLM vs ChatGPT same-source test

Status: **CAPTURED / CHATGPT SOURCE-CHECK FOLLOW-UP COMPLETE**

| Tool | Output section | Claim | Source support | Source page/line | Notes |
|---|---|---|---|---|---|
| NotebookLM | Study guide | Attention selects specific information for deeper processing while ignoring other information. | Supported | same-source-study-notes.md Core ideas | Matches source. |
| NotebookLM | Study guide | Working memory temporarily holds a small amount of information for manipulation. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Long-term memory stores knowledge over longer periods. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Rereading notes without retrieval is a common study mistake. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Retrieval practice means recalling information before checking the answer. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Retrieval feels harder than rereading, and difficulty is part of the learning signal. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Spacing spreads review over time instead of cramming. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Spaced retrieval combines recall, waiting, and later recall. | Supported | Core ideas | Matches source. |
| NotebookLM | Study guide | Transfer question applies a learned idea to a new example. | Supported | Three-day review plan | Matches source. |
| NotebookLM | Example | Photosynthesis study should not only reread the definition. | Supported | Example | Matches source. |
| NotebookLM | Example | Student should ask what enters, what leaves, and where light energy fits. | Supported | Example | Matches source. |
| NotebookLM | Example | Student should compare answers against source and repair mistakes. | Supported | Example | Matches source. |
| NotebookLM | Quiz answer | Attention is the answer to the information-selection question. | Supported | Core ideas | Accurate. |
| NotebookLM | Quiz answer | Working memory is the answer to the temporary workspace question. | Supported | Core ideas | Accurate. |
| NotebookLM | Quiz answer | Long-term memory is the answer to durable knowledge store question. | Supported | Core ideas | Accurate. |
| NotebookLM | Quiz answer | Rereading without retrieval is the common study mistake. | Supported | Core ideas | Accurate. |
| NotebookLM | Quiz answer | Spreading review sessions over time defines spacing. | Supported | Core ideas | Accurate. |
| NotebookLM | Weak concepts | Recognition and recall are explicitly named as confused concepts. | Supported | Weak concept warning | Accurate. |
| NotebookLM | Weak concepts | A third likely-confused concept is not in source. | Supported | Weak concept warning | Good Not-in-source behavior. |
| NotebookLM | Review plan | Day 1 read once, summarize, answer five recall questions. | Supported | Three-day review plan | Matches source. |
| NotebookLM | Review plan | Day 2 answer same questions without notes, add transfer questions, review mistakes. | Supported | Three-day review plan | Matches source. |
| NotebookLM | Review plan | Day 3 teach aloud and write weak-points checklist. | Supported | Three-day review plan | Matches source. |
| ChatGPT | Study guide | Attention is a limited mental process selecting information and ignoring other information. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Working memory temporarily stores a small amount of information for manipulation. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Long-term memory stores knowledge longer term. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Retrieval practice means trying to remember before seeing the answer. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Retrieval practice feels harder but that difficulty is part of the learning signal. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Spacing means dividing review instead of cramming. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Spaced retrieval combines retrieval practice and spacing. | Supported | Core ideas | Matches source. |
| ChatGPT | Study guide | Rereading notes without retrieval is a common mistake. | Supported | Core ideas | Matches source. |
| ChatGPT | Example | Photosynthesis learner should close notes and answer source questions. | Supported | Example | Matches source. |
| ChatGPT | Example | Learner should compare with source and repair wrong parts. | Supported | Example | Matches source. |
| ChatGPT | Weak concepts | Recognition vs recall is the only explicit source confusion. | Supported | Weak concept warning | Matches source. |
| ChatGPT | Weak concepts | Second likely-confused concept is Not in source. | Supported | Weak concept warning | Good Not-in-source behavior. |
| ChatGPT | Weak concepts | Third likely-confused concept is Not in source. | Supported | Weak concept warning | Good Not-in-source behavior. |
| ChatGPT | Quiz answer | Attention chooses what to process deeply and what to ignore. | Supported | Core ideas | Accurate. |
| ChatGPT | Quiz answer | Working memory temporarily holds information for manipulation. | Supported | Core ideas | Accurate. |
| ChatGPT | Quiz answer | Long-term memory stores knowledge over longer periods. | Supported | Core ideas | Accurate. |
| ChatGPT | Quiz answer | Retrieval practice recalls before looking at answer. | Supported | Core ideas | Accurate. |
| ChatGPT | Quiz answer | Transfer question applies an idea to a new example. | Supported | Three-day review plan | Accurate. |
| ChatGPT | Review plan | Day 1 read source once, write summary, answer five recall questions. | Supported | Three-day review plan | Matches source. |
| ChatGPT | Review plan | Day 2 answer without notes, add transfer questions, review mistakes. | Supported | Three-day review plan | Matches source. |
| ChatGPT | Review plan | Day 3 teach aloud and write weak-points checklist. | Supported | Three-day review plan | Matches source. |
| ChatGPT | Recognition explanation | Recognition is like feeling “I have seen this” when looking at the answer. | Partial | Weak concept warning | Simple-language elaboration consistent with source but exact answer-sheet example is not directly in source. |

## Notes

- Source support is based on `same-source-study-notes.md`, the source-equivalent text used for the web captures.
- This claim map is sufficient to prevent unsupported winner claims. Repository screenshot redaction review is complete; public indexing still needs a stable public evidence-link decision.

## ChatGPT source-check follow-up

Status: **complete from local evidence on 2026-07-08**.

Method: compared `chatgpt-output.md` and `chatgpt-output-clean-display.md` against `same-source-study-notes.md`. No external web UI was opened, and no new ChatGPT self-check response was fabricated.

| Category | ChatGPT claim area | Source-check result | Action |
|---|---|---|---|
| Supported | Core concept definitions: attention, working memory, long-term memory, retrieval practice, spacing, and spaced retrieval. | Directly supported by `Core ideas`. | Keep as source-grounded evidence. |
| Supported | Common study mistake: rereading without retrieval. | Directly supported by `Core ideas`. | Keep as source-grounded evidence. |
| Supported | Photosynthesis example questions and repair loop. | Directly supported by `Example`. | Keep as source-grounded evidence. |
| Supported | Quiz questions and answer key. | Answers map to `Core ideas`, `Weak concept warning`, `Three-day review plan`, and `Terms`. | Keep as source-grounded evidence. |
| Supported | Weak-concept behavior: recognition vs recall is named; slots 2 and 3 are `Not in source`. | Source names only recognition vs recall as a common confusion. | Keep as positive source-bound behavior. |
| Supported | Three-day review plan. | Directly supported by `Three-day review plan`. | Keep as source-grounded evidence. |
| Partial / explanatory | Simple-language recognition/recall example using an answer sheet. | Consistent with the source definitions, but the answer-sheet scenario is not directly stated in the source. | Keep logged as harmless explanatory extrapolation, not a source fact. |
| Unsupported | Major educational claims in the primary ChatGPT output. | None found in this local follow-up. | Preserve single-run uncertainty; do not overstate a winner. |
