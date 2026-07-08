# Session Log — 2026-07-08

## One-line status

NotebookLM vs ChatGPT candidate is now an **evidence-backed noindex staging candidate**; no public/indexable launch was opened.

## What changed

- Captured same-source NotebookLM and ChatGPT outputs for `notebooklm-vs-chatgpt-for-studying-pdfs`.
- Preserved raw/clean outputs, screenshots, claim map, unsupported-claims log, scoring sheet, and evidence manifest under `docs/day-13-notebooklm-evidence-pack-files/`.
- Completed ChatGPT source-check follow-up from local evidence.
- Completed editorial QA and added `docs/day-13-notebooklm-evidence-pack-files/editorial-qa.md`.
- Converted Day 21 baseline into a real **no-launch dry run** instead of fake public launch data.
- Kept all posts noindex/staging and avoided fake domain, GA4, GSC, AdSense, traffic, revenue, or indexing values.

## Key docs to read next

| Need | File |
| --- | --- |
| Current project state | `docs/current-phase.md` |
| Day 15–21 gates | `docs/day-15-21-overhaul-plan.md` |
| Evidence overview | `docs/day-13-notebooklm-evidence-pack.md` |
| Detailed evidence manifest | `docs/day-13-notebooklm-evidence-pack-files/evidence-manifest.md` |
| Editorial QA | `docs/day-13-notebooklm-evidence-pack-files/editorial-qa.md` |
| Publish gate state | `docs/publish-checklist.md` |
| No-launch baseline | `reports/day-21-public-launch-baseline.md` |

## Verification snapshot

Commands run after Codex/Hermes passes:

```bash
git diff --check
python3 scripts/build.py
python3 scripts/qa.py
```

Observed result:

```text
Built 4 posts into dist
Static site QA ... OK
```

Expected warnings remain:

- `dist/robots.txt` may not live at host root because this is a base-path/GitHub Pages-style build.
- Three older non-public drafts still contain `FACT CHECK` markers.

Fail-closed checks confirmed:

- `dist/robots.txt` contains `Disallow: /`.
- `dist/sitemap.xml` is empty.
- generated pages contain noindex behavior.
- candidate article frontmatter still has `noindex: true`.

## Relevant commits

```text
1498fd7 Add July 8 session log
6ce7ac6 Complete noindex launch dry run gates
5c59d91 Capture NotebookLM ChatGPT study evidence
65602e8 Implement evidence-first launch gates and planning docs
```

## Remaining decisions

1. Choose **custom domain/final URL** vs **continued no-domain staging**.
2. Configure real GA4/GSC only after final URL decision.
3. Decide public evidence-link handling before any indexable launch.
4. Do not remove `noindex: true` until final URL, measurement, sitemap, evidence-link policy, and publish checklist pass.

## Operational lesson

Do not let long external AI generation become idle time. After verifying the UI is generating, use the wait window for independent work: manifests, checklists, claim maps, scoring, redaction notes, build/QA, and commit prep.
