# Screenshot checklist - NotebookLM vs ChatGPT same-source PDF test

Status: **CAPTURED FOR REPOSITORY EVIDENCE / REDACTION REVIEW COMPLETE**

Captured screenshots:

- `01_notebooklm_source_inserted_copied_text.png` - NotebookLM copied-text source visible.
- `03_notebooklm_answer_visible.png` - NotebookLM prompt/output visible with source citation chips.
- `09_chatgpt_prompt_sent_incomplete.png` - ChatGPT prompt/source text during incomplete attempt; blocker screenshot, not score evidence.
- `10_chatgpt_study_guide_output_top.png` - ChatGPT captured output view.

Local file inspection on 2026-07-08:

- `file` identified all four files as PNG images.
- `sips` reported all four files as 1568 x 948 PNGs with no alpha channel.
- Direct visual inspection found browser chrome/sidebar/account regions cropped or redacted enough for repository evidence. No account email or private identifier was visible in the inspected PNGs.
- A `strings` scan was attempted but not used as evidence because compressed PNG bytes produced noisy false positives.

Limitations:

- This is a repository-evidence redaction review, not approval for public publishing.
- No screenshot captures a ChatGPT source-check follow-up in the web UI; that follow-up was completed from local evidence and is documented in `source-claim-map.md` and `unsupported-claims-log.md`.
- No screenshot captures an actual PDF file attachment flow because file-picker automation was unreliable; the run used source-equivalent copied text.
- Before public indexing, decide whether these repository screenshots should be copied to `dist/`, replaced, omitted, or converted to stable public evidence URLs.
