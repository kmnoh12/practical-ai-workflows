# Capture checklist - notebooklm-vs-chatgpt-for-studying-pdfs

Date: PENDING CAPTURE

## Source files

- `same-source-study-notes.md`
- `same-source-study-notes.pdf`
- `same-source-prompt.txt`
- `evaluation-rubric.md`
- `evidence-manifest.md`

## Required external captures before public indexing

- [ ] `notebooklm-output.md`
- [ ] `notebooklm-output-clean-display.md`
- [ ] `chatgpt-output.md`
- [ ] `chatgpt-output-clean-display.md`
- [ ] `source-claim-map.md` filled with at least 20 atomic claims per tool
- [ ] `unsupported-claims-log.md` filled from source checks
- [ ] `scoring-sheet.csv` filled from captured outputs
- [ ] `screenshots/01_notebooklm_source_upload_source_list.png`
- [ ] `screenshots/02_notebooklm_prompt_in_chat.png`
- [ ] `screenshots/03_notebooklm_study_guide_output_top.png`
- [ ] `screenshots/04_notebooklm_study_guide_output_middle.png`
- [ ] `screenshots/05_notebooklm_quiz_output_answer_key.png`
- [ ] `screenshots/06_notebooklm_citation_or_source_quote_expanded.png`
- [ ] `screenshots/07_notebooklm_settings_or_chat_mode.png`
- [ ] `screenshots/08_chatgpt_model_and_pdf_attached.png`
- [ ] `screenshots/09_chatgpt_same_source_prompt.png`
- [ ] `screenshots/10_chatgpt_study_guide_output_top.png`
- [ ] `screenshots/11_chatgpt_study_guide_output_middle.png`
- [ ] `screenshots/12_chatgpt_quiz_output_answer_key.png`
- [ ] `screenshots/13_chatgpt_source_check_followup.png`
- [ ] `screenshots/14_chatgpt_file_attachment_visible.png`

## Capture rules

- Use the exact PDF and prompt in this folder.
- Do not edit the prompt between NotebookLM and ChatGPT runs, except for tool-specific upload instructions.
- Save the date/time, account/tool mode, ChatGPT model, ChatGPT plan, tools enabled, NotebookLM plan, and NotebookLM settings if visible.
- Keep the primary result to the same prompt. Built-in study guide or quiz features can be appendix evidence, but should not replace the same-prompt comparison.
- If regeneration is used, record it in `evidence-manifest.md`.
- Record whether any manual edits were made to outputs.
- Redact account emails or private identifiers before committing screenshots.
- If screenshots cannot be captured cleanly, still save raw tool output into `notebooklm-output.md` and `chatgpt-output.md`, clearly labeled as not screenshots.

## ChatGPT source-check follow-up

After saving the primary ChatGPT output, ask:

```text
List any claims in your answer that are not directly supported by the uploaded PDF. If all claims are supported, say "No unsupported claims found."
```

Record this follow-up separately as self-check behavior. Do not include it in the primary output score.
