# Evidence manifest - NotebookLM vs ChatGPT same-source test

Status: **CAPTURED / NOINDEX REVIEW**. NotebookLM and ChatGPT same-source outputs captured; claim map and scoring sheet filled for staging review. Public indexing still blocked until screenshot redaction and source-check follow-up are complete.

| Field | Value |
|---|---|
| Test date | 2026-07-08 |
| Tester | Hermes / Practical AI Workflows |
| Article slug | notebooklm-vs-chatgpt-for-studying-pdfs |
| Source file name | same-source-study-notes.pdf plus source-equivalent Markdown text fallback for NotebookLM/ChatGPT web input |
| Source PDF page count | 1 |
| Source PDF word count | 196 PDF text-stream word tokens extracted locally; source Markdown has 318 word tokens |
| Source file SHA256 | 943164f12d9bef7f9e7fe93706a7e9c06a16ee7aa58c5cc0b8605b6d8b42c6a6 |
| Prompt file | same-source-prompt.txt |
| Rubric file | evaluation-rubric.md |
| NotebookLM account/plan | Logged-in Google account; visible UI showed NotebookLM PRO badge; account identifier not committed |
| ChatGPT plan | Logged-in ChatGPT Pro web session |
| ChatGPT model | Not captured; default/new-chat model selector visible as Pro/extended UI only |
| ChatGPT tools enabled | Not captured |
| NotebookLM settings | Default notebook/chat mode; copied-text source inserted |
| Runs per tool | NotebookLM: 1 captured run. ChatGPT: 1 captured run after 3m 19s generation time. |
| Regeneration used? | No regeneration recorded |
| Any manual edits to outputs? | NotebookLM output extracted from AX visible text; no semantic edits. ChatGPT output extracted from AX visible text; no semantic edits. |
| Redactions | Screenshots were automatically redacted for browser chrome/sidebar/account areas before commit. Account identifiers are not written in manifest. |

## Local metadata notes

- Page count was derived from the PDF `/Count 1` page tree and one `/Type /Page` object.
- PDF word count was derived from visible text strings in the PDF text stream, not from an external PDF parser.
- Source Markdown word count was computed separately from `same-source-study-notes.md`.
- PDF upload through the macOS Open Panel was attempted, but automation could not complete file selection reliably. NotebookLM capture used the same source text via the “copied text” source flow.
- ChatGPT web capture used the same source text appended under `SOURCE:` because file upload would have required the same unreliable Open Panel path.
- Do not publish/index the article until screenshot redaction, ChatGPT source-check follow-up, and final QA approval are complete.
