# Publish Checklist

Purpose: objective pre-publication checklist for exactly one first public URL.

First candidate slug: `notebooklm-vs-chatgpt-for-studying-pdfs`.

Current dry-run date: 2026-07-08.

Current decision: **FAIL / NO PUBLIC LAUNCH**. The candidate is ready as an evidence-backed staging/noindex article, but the final URL/custom domain, GA4, GSC, stable public evidence-link handling, and launch checklist are not complete.

## 1. Scope Gate

| Check | Status |
| --- | --- |
| One URL only is being considered for public/indexable launch. | PASS - dry run scope is one candidate only; no URL published. |
| First candidate slug is `notebooklm-vs-chatgpt-for-studying-pdfs`. | PASS |
| No other posts are public/indexable. | PASS - zero public/indexable posts. |
| No AdSense, affiliate, social/email funnel, or programmatic SEO work is bundled into this launch. | PASS |

Pass only if exactly one URL is in scope.

## 2. Final URL Gate

| Check | Status |
| --- | --- |
| `public_base_url` is final and uses `https://`. | FAIL - not configured. |
| `robots_at_host_root` is `true` only after host-root `/robots.txt` is verified. | FAIL - host-root robots not verified. |
| Canonical URL uses the final URL. | FAIL - final canonical host not decided. |
| Sitemap URL is absolute and final. | FAIL - no final sitemap URL; staging sitemap remains empty. |
| GitHub Pages or other staging/project subpath URL is not treated as the public canonical unless explicitly accepted as the final URL policy. | PENDING USER DECISION - custom domain/final URL not selected. |

Pass only if canonical, robots, and sitemap all point to the same final URL policy.

## 3. Content Evidence Gate

Required evidence for the first candidate:

| Evidence item | Status |
| --- | --- |
| Same PDF used for NotebookLM and ChatGPT. | PASS WITH LIMITATION - same source pack and source-equivalent text were used; PDF file is archived, but web captures used copied text because file-picker automation was unreliable. |
| Same prompt used for NotebookLM and ChatGPT. | PASS |
| Raw NotebookLM output preserved. | PASS |
| Raw ChatGPT output preserved. | PASS |
| Screenshots preserved. | PASS |
| Evidence manifest updated. | PASS |
| Claim map complete. | PASS |
| Unsupported claims log complete. | PASS |
| Scoring sheet complete. | PASS |
| No fabricated or placeholder scores. | PASS |
| No unresolved `FACT CHECK`, `TODO`, `VERIFY`, or `needs evidence` remains in the public article. | PASS |

Pass only if the recommendation follows from measured evidence.

## 4. Article Quality Gate

| Check | Status |
| --- | --- |
| Reader-first short verdict appears near the top. | PASS |
| Measured results are shown, not generic claims. | PASS |
| Situation-specific recommendation explains when to use NotebookLM, ChatGPT, or both. | PASS |
| Limitations are explicit. | PASS |
| Official source touchpoints include checked dates. | PASS |
| Article does not overclaim from one document, one prompt, or one test date. | PASS |

Pass only if the article is useful to a reader without pretending the test proves more than it does.

## 5. Technical QA Gate

Run:

```bash
python3 scripts/build.py
python3 scripts/qa.py
git diff --check
```

| Check | Status |
| --- | --- |
| `python3 scripts/build.py` passes. | PASS on 2026-07-08 dry run. |
| `python3 scripts/qa.py` passes. | PASS WITH WARNINGS on 2026-07-08 dry run: base-path host-root robots caveat plus old non-public draft `FACT CHECK` markers. |
| `git diff --check` passes. | PASS on 2026-07-08 dry run. |
| Generated HTML has `index,follow` only for the approved URL. | PASS - no approved URL exists; generated HTML remains noindex/nofollow. |
| All non-public pages/posts remain noindex or excluded according to build behavior. | PASS |
| Sitemap includes exactly approved public URL(s), currently max 1. | PASS - zero approved public URLs, empty sitemap. |
| Canonical, meta robots, and sitemap do not conflict. | PASS for staging/noindex dry run; FAIL for public launch because no final host exists. |
| Public HTML contains no unresolved markers. | PASS - no public HTML exists; candidate source has no blocked markers. |

Pass only on generated HTML, not source markdown alone.

## 6. Measurement Gate

| Check | Status |
| --- | --- |
| GA4 is configured with a valid real ID only when real. | NOT CONFIGURED |
| GSC verification is configured only when real. | NOT CONFIGURED |
| `page_view` can be verified. | NOT RUN |
| Outbound/tool official link click can be verified. | NOT RUN |
| Evidence link click can be verified if an evidence link is available. | NOT RUN - stable public evidence-link handling is not decided. |
| Later `affiliate_click` remains disabled until affiliate links are approved and disclosed. | PASS |
| Internal traffic handling is documented before interpreting baseline data. | PASS - documented in `docs/measurement-plan.md`; no real baseline data exists. |

Pass only if test traffic is treated as technical verification, not audience validation.

## 7. Policy/Trust Gate

| Page or policy | Status |
| --- | --- |
| About page status tracked. | PASS - page exists, still staged/noindex by build behavior. |
| Contact page status tracked. | FAIL FOR PUBLIC LAUNCH - page exists but contains `[email to add]`. |
| Privacy page status tracked. | FAIL FOR PUBLIC LAUNCH - draft placeholder requires review before launch. |
| Editorial/Methodology page status tracked. | PASS WITH LIMITATION - page exists as a methodology draft. |
| Affiliate/Advertising Disclosure status tracked. | PASS WITH LIMITATION - page exists; no approved affiliate programs or links. |
| No affiliate links exist before approval and disclosure. | PASS |
| No ad-click encouragement, fake traffic, or monetization language is added. | PASS |

Pass only if trust gaps are either closed or explicitly recorded as blockers for monetized use.

## 8. Post-Launch 7-Day Baseline Gate

| Check | Status |
| --- | --- |
| URL Inspection submitted or checked. | NOT RUN - no GSC property or public URL. |
| Sitemap submitted or checked. | NOT RUN - no GSC property; staging sitemap is empty. |
| GA4 realtime/manual page-view test documented. | NOT RUN - GA4 not configured. |
| Outbound/evidence click test documented where applicable. | NOT RUN - measurement and stable public evidence-link handling not configured. |
| Daily technical notes table is started in `reports/day-21-public-launch-baseline.md`. | PASS - dry-run table started with no-launch values. |

Pass only if the first 7 days are treated as technical observation.

## 9. Final Decision

| Decision | Action |
| --- | --- |
| PASS | Publish exactly one URL: `notebooklm-vs-chatgpt-for-studying-pdfs`. Do not publish any other post. Update `reports/day-21-public-launch-baseline.md` with real launch data. |
| FAIL | Keep noindex/staging. Do not change post public gates. Write or update `reports/day-21-public-launch-baseline.md` as a dry-run report using `PENDING`, `NOT RUN`, or `NOT CONFIGURED` for missing real data. |
