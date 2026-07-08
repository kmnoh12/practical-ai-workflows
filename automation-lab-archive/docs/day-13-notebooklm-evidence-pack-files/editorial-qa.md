# Editorial QA note - NotebookLM vs ChatGPT same-source test

Date: 2026-07-08

Status: **final editorial QA pass complete for staging/noindex evidence consistency**

Scope reviewed:

- Candidate article: `content/posts/notebooklm-vs-chatgpt-for-studying-pdfs.md`
- Evidence overview: `docs/day-13-notebooklm-evidence-pack.md`
- Evidence files in `docs/day-13-notebooklm-evidence-pack-files/`
- Four local screenshot PNGs in `docs/day-13-notebooklm-evidence-pack-files/screenshots/`

Findings:

- The article keeps `noindex: true` and staging status unchanged.
- Winner language is limited to a single captured run.
- NotebookLM's stated edge is limited to source-grounding/source-verification affordances.
- No major unsupported educational claims were found in the primary outputs during local claim review.
- ChatGPT's recognition/recall answer-sheet example remains logged as partial/explanatory rather than a direct source fact.
- The evidence docs do not claim AdSense readiness, public indexing, revenue, or a final domain.
- Repository screenshot redaction review found no visible account email or private identifier in the four inspected PNGs. This review used local file metadata plus direct visual inspection only.

Remaining blockers before public indexing:

- Decide final URL and sitemap/indexing behavior.
- Decide analytics or measurement setup, if used.
- Decide whether repository evidence artifacts are copied into `dist/`, replaced, omitted, or converted to stable public URLs.
- Optional: repeat capture with actual PDF attachment if file-picker automation becomes reliable.
