# Publish Checklist

Purpose: objective pre-publication checklist for exactly one first public URL.

First candidate slug: `notebooklm-vs-chatgpt-for-studying-pdfs`.

## 1. Scope Gate

| Check | Status |
| --- | --- |
| One URL only is being considered for public/indexable launch. | PENDING |
| First candidate slug is `notebooklm-vs-chatgpt-for-studying-pdfs`. | PENDING |
| No other posts are public/indexable. | PENDING |
| No AdSense, affiliate, social/email funnel, or programmatic SEO work is bundled into this launch. | PENDING |

Pass only if exactly one URL is in scope.

## 2. Final URL Gate

| Check | Status |
| --- | --- |
| `public_base_url` is final and uses `https://`. | PENDING |
| `robots_at_host_root` is `true` only after host-root `/robots.txt` is verified. | PENDING |
| Canonical URL uses the final URL. | PENDING |
| Sitemap URL is absolute and final. | PENDING |
| GitHub Pages or other staging/project subpath URL is not treated as the public canonical unless explicitly accepted as the final URL policy. | PENDING |

Pass only if canonical, robots, and sitemap all point to the same final URL policy.

## 3. Content Evidence Gate

Required evidence for the first candidate:

| Evidence item | Status |
| --- | --- |
| Same PDF used for NotebookLM and ChatGPT. | PENDING |
| Same prompt used for NotebookLM and ChatGPT. | PENDING |
| Raw NotebookLM output preserved. | PENDING |
| Raw ChatGPT output preserved. | PENDING |
| Screenshots preserved. | PENDING |
| Evidence manifest updated. | PENDING |
| Claim map complete. | PENDING |
| Unsupported claims log complete. | PENDING |
| Scoring sheet complete. | PENDING |
| No fabricated or placeholder scores. | PENDING |
| No unresolved `FACT CHECK`, `TODO`, `VERIFY`, or `needs evidence` remains in the public article. | PENDING |

Pass only if the recommendation follows from measured evidence.

## 4. Article Quality Gate

| Check | Status |
| --- | --- |
| Reader-first short verdict appears near the top. | PENDING |
| Measured results are shown, not generic claims. | PENDING |
| Situation-specific recommendation explains when to use NotebookLM, ChatGPT, or both. | PENDING |
| Limitations are explicit. | PENDING |
| Official source touchpoints include checked dates. | PENDING |
| Article does not overclaim from one document, one prompt, or one test date. | PENDING |

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
| `python3 scripts/build.py` passes. | PENDING |
| `python3 scripts/qa.py` passes. | PENDING |
| `git diff --check` passes. | PENDING |
| Generated HTML has `index,follow` only for the approved URL. | PENDING |
| All non-public pages/posts remain noindex or excluded according to build behavior. | PENDING |
| Sitemap includes exactly approved public URL(s), currently max 1. | PENDING |
| Canonical, meta robots, and sitemap do not conflict. | PENDING |
| Public HTML contains no unresolved markers. | PENDING |

Pass only on generated HTML, not source markdown alone.

## 6. Measurement Gate

| Check | Status |
| --- | --- |
| GA4 is configured with a valid real ID only when real. | PENDING |
| GSC verification is configured only when real. | PENDING |
| `page_view` can be verified. | PENDING |
| Outbound/tool official link click can be verified. | PENDING |
| Evidence link click can be verified if an evidence link is available. | PENDING |
| Later `affiliate_click` remains disabled until affiliate links are approved and disclosed. | PENDING |
| Internal traffic handling is documented before interpreting baseline data. | PENDING |

Pass only if test traffic is treated as technical verification, not audience validation.

## 7. Policy/Trust Gate

| Page or policy | Status |
| --- | --- |
| About page status tracked. | PENDING |
| Contact page status tracked. | PENDING |
| Privacy page status tracked. | PENDING |
| Editorial/Methodology page status tracked. | PENDING |
| Affiliate/Advertising Disclosure status tracked. | PENDING |
| No affiliate links exist before approval and disclosure. | PENDING |
| No ad-click encouragement, fake traffic, or monetization language is added. | PENDING |

Pass only if trust gaps are either closed or explicitly recorded as blockers for monetized use.

## 8. Post-Launch 7-Day Baseline Gate

| Check | Status |
| --- | --- |
| URL Inspection submitted or checked. | PENDING |
| Sitemap submitted or checked. | PENDING |
| GA4 realtime/manual page-view test documented. | PENDING |
| Outbound/evidence click test documented where applicable. | PENDING |
| Daily technical notes table is started in `reports/day-21-public-launch-baseline.md`. | PENDING |

Pass only if the first 7 days are treated as technical observation.

## 9. Final Decision

| Decision | Action |
| --- | --- |
| PASS | Publish exactly one URL: `notebooklm-vs-chatgpt-for-studying-pdfs`. Do not publish any other post. Update `reports/day-21-public-launch-baseline.md` with real launch data. |
| FAIL | Keep noindex/staging. Do not change post public gates. Write or update `reports/day-21-public-launch-baseline.md` as a dry-run report using `PENDING`, `NOT RUN`, or `NOT CONFIGURED` for missing real data. |
