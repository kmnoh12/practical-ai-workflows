# Day 21 Public Launch Baseline

Status: **DRY RUN / NO PUBLIC LAUNCH**

Dry-run date: **2026-07-08**

Purpose: technical baseline, not SEO performance or revenue report.

Use `PENDING`, `NOT RUN`, or `NOT CONFIGURED` when real launch data does not exist. Do not invent traffic, indexing, revenue, impression, click, conversion, GA4, GSC, AdSense, affiliate, or domain values.

## 1. Launch Decision Summary

| Field | Value |
| --- | --- |
| Published one URL? | No |
| If no, why not? | Final URL/custom domain not decided; GA4/GSC not configured; stable public evidence-link handling not decided; launch checklist not passed. |
| Final URL used / pending | PENDING - no `public_base_url`, custom domain, or final canonical host configured. |
| Candidate slug | `notebooklm-vs-chatgpt-for-studying-pdfs` |
| Candidate state | Evidence-backed noindex candidate; not a public/indexable page. |
| Launch decision date | 2026-07-08 |
| Decision owner/checker | Codex documentation worker dry run; Hermes review pending. |

## 2. URL and Indexing State

| Field | Value |
| --- | --- |
| Canonical URL | NOT FINAL - staging build uses the configured base path because `public_base_url` is empty. |
| Robots state | STAGING/NOINDEX - `dist/robots.txt` blocks with `Disallow: /` while zero public posts exist. |
| Sitemap state | EMPTY - no public/indexable post URLs included. |
| Sitemap URL | NOT CONFIGURED - no final public host. |
| GSC URL Inspection state | NOT RUN |
| Host-root `/robots.txt` verified? | No |
| Public/indexable URL count | 0 |

## 3. Build/QA Evidence

| Command | Result |
| --- | --- |
| `python3 scripts/build.py` | PASS - built staging output into `dist`. |
| `python3 scripts/qa.py` | PASS WITH WARNINGS - base-path build warning and old non-public draft marker warnings remain. |
| `git diff --check` | PASS |

Paste results manually after launch or dry run.

Warnings/failures:

- `python3 scripts/qa.py` warns: base-path build means `dist/robots.txt` may not live at host root; do not rely on it for public indexing control.
- `python3 scripts/qa.py` also warns that old non-public draft posts still contain `FACT CHECK` markers: `beehiiv-vs-kit-convertkit-for-solo-creators`, `creator-automation-stack-for-beginners`, and `make-vs-zapier-for-creators`.
- These are not launch failures because no posts are public/indexable, the candidate article has no blocked markers, and all generated pages remain noindex/nofollow.

## 4. Content Evidence State

| Evidence item | State |
| --- | --- |
| Raw NotebookLM output present? | COMPLETE |
| Raw ChatGPT output present? | COMPLETE |
| Screenshots present? | COMPLETE - four local PNGs preserved and redaction-reviewed. |
| Evidence manifest complete? | COMPLETE |
| Claim map complete? | COMPLETE |
| Unsupported claims log complete? | COMPLETE |
| Scoring sheet complete? | COMPLETE |
| Article recommendation matches evidence? | COMPLETE for staging/noindex candidate; limited to one source, one prompt, and copied-text web capture fallback. |

## 5. Measurement State

| Field | State |
| --- | --- |
| GA4 configured? | NOT CONFIGURED |
| GA4 ID/source | NOT CONFIGURED |
| `page_view` tested? | NOT RUN |
| Outbound click tested? | NOT RUN |
| Evidence link click tested? | NOT RUN - stable public evidence-link handling not decided. |
| GSC configured? | NOT CONFIGURED |
| Internal traffic notes | Documented in `docs/measurement-plan.md`; no real baseline data exists. |

## 6. Seven-Day Technical Observation Log

| Date | GSC indexing/status notes | GA4 notes | Crawl/sitemap notes | Content/QA changes | Decision |
| --- | --- | --- | --- | --- | --- |
| Day 1 - 2026-07-08 | NOT RUN - no public URL or GSC property. | NOT RUN - GA4 not configured. | Staging build only; sitemap empty. | Evidence/article QA complete for noindex candidate. | No launch; pause for final URL and measurement decisions. |
| Day 2 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Day 3 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Day 4 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Day 5 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Day 6 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Day 7 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |

## 7. What This Baseline Can and Cannot Prove

Can prove:

- Pipeline works.
- Crawl/indexing eligibility is possible on the final URL.
- Measurement fires.
- QA is reproducible.

Cannot prove:

- SEO winning angle.
- AdSense eligibility.
- Affiliate conversion.
- Long-term traffic.

## 8. Next Decision

Choose one before any public/indexable launch:

| Option | Use when |
| --- | --- |
| choose custom domain | User wants a serious 90-day experiment with stable canonical URLs, host-root robots, GA4, GSC, and future monetization eligibility. |
| continue no-domain staging | User wants to keep the lab noindex/staging and defer AdSense/public SEO until a final URL decision is worth making. |
| fix URL | Canonical, domain, robots, sitemap, or redirect policy is unstable. |
| fix evidence links | Decide whether repo evidence artifacts are copied into `dist`, replaced, omitted, or converted to stable public evidence URLs. |
| fix measurement | GA4/GSC or event verification is incomplete. |
| prepare second candidate | The first URL has a clean technical baseline and no unresolved evidence or measurement blockers. |

Selected next decision: **pause - user decision needed: custom domain/final URL versus continued no-domain staging.**
