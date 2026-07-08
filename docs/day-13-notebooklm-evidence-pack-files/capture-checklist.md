# Capture checklist - notebooklm-vs-chatgpt-for-studying-pdfs

Date: 2026-07-08

## Source files

- [x] `same-source-study-notes.md`
- [x] `same-source-study-notes.pdf`
- [x] `same-source-prompt.txt`
- [x] `evaluation-rubric.md`
- [x] `evidence-manifest.md`

## Required external captures before public indexing

- [x] `notebooklm-output.md`
- [x] `notebooklm-output-ax-visible.txt`
- [x] `notebooklm-output-clean-display.md`
- [x] `chatgpt-output.md` real answer body
- [x] `chatgpt-attempt-ax-visible-incomplete.txt` attempt log
- [x] `chatgpt-output-clean-display.md`
- [x] `source-claim-map.md` filled with at least 20 atomic claims per tool
- [x] `unsupported-claims-log.md` filled from source checks
- [x] `scoring-sheet.csv` filled from captured outputs
- [x] `screenshots/01_notebooklm_source_inserted_copied_text.png`
- [ ] `screenshots/02_notebooklm_prompt_in_chat.png`
- [x] `screenshots/03_notebooklm_answer_visible.png`
- [ ] `screenshots/04_notebooklm_study_guide_output_middle.png`
- [ ] `screenshots/05_notebooklm_quiz_output_answer_key.png`
- [ ] `screenshots/06_notebooklm_citation_or_source_quote_expanded.png`
- [ ] `screenshots/07_notebooklm_settings_or_chat_mode.png`
- [ ] `screenshots/08_chatgpt_model_and_pdf_attached.png`
- [x] `screenshots/09_chatgpt_prompt_sent_incomplete.png` — blocker screenshot, not score evidence
- [x] `screenshots/10_chatgpt_study_guide_output_top.png`
- [ ] `screenshots/11_chatgpt_study_guide_output_middle.png`
- [ ] `screenshots/12_chatgpt_quiz_output_answer_key.png`
- [ ] `screenshots/13_chatgpt_source_check_followup.png`
- [ ] `screenshots/14_chatgpt_file_attachment_visible.png`

## Capture rules

- Use the exact source PDF/source-equivalent notes and prompt in this folder.
- Do not edit the prompt between NotebookLM and ChatGPT runs, except for tool-specific upload/input wrapper text.
- Save date/time, account/tool mode, model, plan, tools enabled, and settings when visible.
- Keep the primary result to the same prompt. Built-in study guide or quiz features can be appendix evidence, but should not replace the same-prompt comparison.
- If regeneration is used, record it in `evidence-manifest.md`.
- Record whether any manual edits were made to outputs.
- Redact account emails or private identifiers before public distribution.
- If screenshots cannot be captured cleanly, still save raw tool output and clearly label limitations.

## ChatGPT source-check follow-up

Primary ChatGPT output is saved. Follow-up still pending before public indexing. After saving the primary ChatGPT output, ask:

```text
List any claims in your answer that are not directly supported by the uploaded PDF. If all claims are supported, say "No unsupported claims found."
```

Record this follow-up separately as self-check behavior. Do not include it in the primary output score.
