# Metrics

Purpose: record only external/user/market signals. Do not use this file for internal QA logs.

## Current status

| Field | Value |
| --- | --- |
| Public URL | Deployed staging: `https://practical-ai-workflows.pages.dev` |
| GA4 | Configured: `G-Z1GHN2WDGC` |
| GSC | HTML tag configured: `fUeVN4-aAJjDqU-6KLZ64yZPnRDjSIblzVicj4bf880` |
| Template/download asset | Created: `public/downloads/pdf-study-workflow-template.md` |
| Email capture | Not configured |
| Decision clock | Started 2026-07-09 after public/indexable deploy, GA4/GSC tag deploy, sitemap submission, and URL checks |

## Weekly log

| Date | Public URL | GSC impressions | GSC clicks | Referral visits | Downloads | Email signups | Direct feedback | Decision / next action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 2026-07-08 | Not launched | 0 | 0 | 0 | 0 | 0 | Split decision received; active business experiment separated from operations lab. | Build first publishing unit; do not create more meta-docs. |
| 2026-07-09 | `https://practical-ai-workflows.pages.dev` staging/noindex | 0 | 0 | 0 | 0 | 0 | Cloudflare Pages project created, repo connected, first deployment succeeded; site remains robots Disallow/noindex and GA4/GSC are still not configured. | Next: GA4/GSC values, then one article indexable launch. |
| 2026-07-09 | `https://practical-ai-workflows.pages.dev/notebooklm-vs-chatgpt-for-studying-pdfs/` public/indexable | 0 | 0 | 0 | 0 | 0 | GA4 and GSC HTML tag deployed; robots allows crawl; sitemap submitted in Search Console; GSC URL inspection still temporarily reports old robots block. | Re-test URL inspection after robots cache catches up; then request indexing. |
| 2026-07-09 | Day 1 batch: 6 public URLs including 5 new workflow/automation pages | 0 | 0 | 0 | 0 | 0 | Build, static QA, git diff check, commit/push, robots.txt, sitemap, and five new live article URLs verified by curl. | Next: submit/inspect new URLs in GSC when available; run one platform-native distribution attempt per top article. |

## Decision rules

- If visitors exist but downloads are zero: fix CTA/value prop/template preview.
- If downloads exist but no feedback/signup: improve onboarding and ask for feedback.
- If no visitors: fix distribution and search positioning.
- If everything is near zero after 30 days: pivot or kill; do not add more internal docs.
