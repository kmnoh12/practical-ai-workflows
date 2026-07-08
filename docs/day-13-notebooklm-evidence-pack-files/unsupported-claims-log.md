# Unsupported claims log - NotebookLM vs ChatGPT same-source test

Status: **CAPTURED / INITIAL REVIEW FILLED**

Log only claims that are unsupported, partially supported, or impossible to verify from the source.

## NotebookLM

| Output section | Claim | Issue type | Source check | Action for article |
|---|---|---|---|---|
| Weak concept detection | “The source explicitly notes two concepts that learners often confuse… third: Not in source.” | Supported source-bound refusal | Source says learners often confuse recognition with recall; it does not name a third confusion concept. | Positive evidence for source-bound behavior. |

## ChatGPT

| Output section | Claim | Issue type | Source check | Action for article |
|---|---|---|---|---|
| Weak concept detection | Second and third likely-confused concepts are “Not in source.” | Supported source-bound refusal | Source explicitly names only recognition vs recall as a confusion. | Positive evidence for source-bound behavior. |
| Recognition explanation | “답안지를 보고 익숙하다고 느끼는 건 recognition이고…” | Partial / explanatory extrapolation | Source defines recognition as feeling an answer looks familiar when seeing it; answer-sheet example is not directly in source. | Mention as harmless simple-language example, not a source fact. |

## Source-check follow-up

Not yet run. Public/indexed version should ask ChatGPT the follow-up after the primary output capture:

```text
List any claims in your answer that are not directly supported by the uploaded PDF. If all claims are supported, say "No unsupported claims found."
```
