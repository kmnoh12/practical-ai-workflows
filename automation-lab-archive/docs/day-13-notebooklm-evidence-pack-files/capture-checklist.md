# Capture checklist - notebooklm-vs-chatgpt-for-studying-pdfs

Date: 2026-07-08

## Source files

- [x] `same-source-study-notes.md`
- [x] `same-source-study-notes.pdf`
- [x] `same-source-prompt.txt`
- [x] `evaluation-rubric.md`
- [x] `evidence-manifest.md`

## Captured artifacts and screenshot inventory

- [x] `notebooklm-output.md`
- [x] `notebooklm-output-ax-visible.txt`
- [x] `notebooklm-output-clean-display.md`
- [x] `chatgpt-output.md` real answer body
- [x] `chatgpt-attempt-ax-visible-incomplete.txt` attempt log
- [x] `chatgpt-output-clean-display.md`
- [x] `source-claim-map.md` filled with at least 20 atomic claims per tool
- [x] `unsupported-claims-log.md` filled from source checks
- [x] ChatGPT source-check follow-up completed from local evidence
- [x] `scoring-sheet.csv` filled from captured outputs
- [x] `screenshots/01_notebooklm_source_inserted_copied_text.png`
- [ ] `screenshots/02_notebooklm_prompt_in_chat.png` - not captured; non-blocking because `03_notebooklm_answer_visible.png` includes the submitted prompt
- [x] `screenshots/03_notebooklm_answer_visible.png`
- [ ] `screenshots/04_notebooklm_study_guide_output_middle.png` - not captured; raw/clean output files carry the full answer
- [ ] `screenshots/05_notebooklm_quiz_output_answer_key.png` - not captured; raw/clean output files carry the full answer
- [ ] `screenshots/06_notebooklm_citation_or_source_quote_expanded.png` - not captured; visible citation chips are present in `03_notebooklm_answer_visible.png`
- [ ] `screenshots/07_notebooklm_settings_or_chat_mode.png` - not captured; settings are documented in `evidence-manifest.md`
- [ ] `screenshots/08_chatgpt_model_and_pdf_attached.png` - not captured; file attachment was not used because file-picker automation was unreliable
- [x] `screenshots/09_chatgpt_prompt_sent_incomplete.png` — blocker screenshot, not score evidence
- [x] `screenshots/10_chatgpt_study_guide_output_top.png`
- [ ] `screenshots/11_chatgpt_study_guide_output_middle.png` - not captured; raw/clean output files carry the full answer
- [ ] `screenshots/12_chatgpt_quiz_output_answer_key.png` - not captured; raw/clean output files carry the full answer
- [ ] `screenshots/13_chatgpt_source_check_followup.png` - not captured; follow-up was completed from local evidence, not web UI
- [ ] `screenshots/14_chatgpt_file_attachment_visible.png` - not captured; file attachment was not used because file-picker automation was unreliable

## Capture rules

- Use the exact source PDF/source-equivalent notes and prompt in this folder.
- Do not edit the prompt between NotebookLM and ChatGPT runs, except for tool-specific upload/input wrapper text.
- Save date/time, account/tool mode, model, plan, tools enabled, and settings when visible.
- Keep the primary result to the same prompt. Built-in study guide or quiz features can be appendix evidence, but should not replace the same-prompt comparison.
- If regeneration is used, record it in `evidence-manifest.md`.
- Record whether any manual edits were made to outputs.
- Redact account emails or private identifiers before public distribution.
- If screenshots cannot be captured cleanly, still save raw tool output and clearly label limitations.

## Screenshot redaction review

Completed on 2026-07-08 for the four local PNGs currently in `screenshots/`. Direct visual inspection found browser chrome/sidebar/account regions cropped or redacted enough for repository evidence, with no visible account email or private identifier. This does not approve the screenshots for public distribution; public use still needs a launch/evidence-link decision.

## ChatGPT source-check follow-up

Primary ChatGPT output is saved. The follow-up gate was completed from local evidence on 2026-07-08 by comparing `chatgpt-output.md` and `chatgpt-output-clean-display.md` against `same-source-study-notes.md`. No external web UI was opened, and no new ChatGPT self-check response was fabricated.

Result: no major unsupported educational claims were found. Keep the minor recognition/recall answer-sheet example logged as partial/explanatory rather than a direct source fact. Do not include this follow-up in the primary output score.
