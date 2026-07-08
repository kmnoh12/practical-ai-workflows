# Day 15–21 Overhaul Plan

## Current Objective

The Day 15-21 objective is **one evidence-backed public candidate + final URL/measurement/indexing pipeline**, not first revenue or AdSense readiness.

The first candidate remains `notebooklm-vs-chatgpt-for-studying-pdfs`. It should not become public/indexable until the final URL, evidence pack, generated HTML QA, GA4/GSC readiness, and publish checklist all pass.

## Scope Correction

This week is a publishing-pipeline proof, not a monetization sprint.

| Area | Week 15-21 scope |
| --- | --- |
| AdSense | Out of scope this week. Do not apply, prepare fake application data, or treat the current site as AdSense-ready. |
| Affiliate revenue | Out of scope this week. No affiliate links before approval, disclosure, and `rel` policy are ready. |
| Social, email, programmatic SEO | Out of scope this week. Do not add distribution systems before the first public candidate and launch baseline are proven. |
| More posts | Out of scope until the first evidence article and technical launch baseline are proven. |

## Correct Sequencing

Use this order:

> final URL/domain → public shell/trust pages → build/index rules → GA4/GSC → content evidence → generated HTML QA → publish one URL → URL Inspection/sitemap → 7-day technical measurement

1. Final URL/domain.
2. Public shell/trust pages.
3. Build/index rules.
4. GA4/GSC.
5. Content evidence.
6. Generated HTML QA.
7. Publish one URL.
8. URL Inspection/sitemap.
9. 7-day technical measurement.

Content quality work matters, but it cannot compensate for an unstable canonical URL, broken robots/sitemap behavior, or missing measurement. The first public URL is a pipeline test before it is an SEO test.

## Dependency Links

- [Current phase](current-phase.md)
- [Public URL policy](public-url-policy.md)
- [Measurement plan](measurement-plan.md)
- [Monetization readiness gates](monetization-readiness-gates.md)
- [Publish checklist](publish-checklist.md)
- [Day 21 public launch baseline](../reports/day-21-public-launch-baseline.md)
- [NotebookLM evidence pack overview](day-13-notebooklm-evidence-pack.md)
- [NotebookLM evidence pack files](day-13-notebooklm-evidence-pack-files/)

## Day-by-Day Plan

| Day | Focus | Actions | Pass gate | Fail gate |
| --- | --- | --- | --- | --- |
| Day15 | Freeze scope and decide final URL policy | Decide custom domain now versus explicit AdSense out-of-scope while using non-final/free infrastructure. Confirm homepage, post URL pattern, evidence URL pattern, canonical policy, and host-root robots requirement. | Final URL policy is documented; AdSense is either later on a valid final domain or explicitly out of scope. No fake domain or public base URL is added. | Final URL is undecided, robots root behavior is unknown, or docs still imply near-term AdSense readiness. Keep staging/noindex. |
| Day16 | Public shell/trust pages inventory | Inventory About, Contact, Privacy, Editorial/Methodology, and Affiliate/Advertising Disclosure requirements. Track what exists, what is missing, and what must be linked from nav/footer before public launch. | Trust-page status is known and missing pages are explicit blockers or accepted launch risks for a non-monetized technical baseline. | Required policy/trust pages are unknown, placeholder-only, or imply monetization that is not active. Keep staging/noindex. |
| Day17 | Measurement design and GA4/GSC readiness | Define GA4/GSC setup for the final URL. Keep GA4/GSC IDs empty unless real. Confirm intended events: `page_view`, official outbound/tool click, evidence link click if available, and later disabled `affiliate_click`. | Measurement plan is tied to a final URL, uses no fake IDs, and includes internal/test traffic handling notes. | GA4/GSC cannot be configured for a real final URL, or the only available data would be self-test traffic. Keep staging/noindex and document the gap. |
| Day18 | NotebookLM/ChatGPT same-source capture | Run the same PDF and same prompt through NotebookLM and ChatGPT. Preserve raw outputs, screenshots, test date, tool/account context, and limitations in the evidence pack. | Same-source raw outputs and screenshots exist, with an evidence manifest updated from real captures. | Either tool is missing, outputs are partial, screenshots are absent, or test conditions diverge. Do not publish a comparison. |
| Day19 | Claim map, unsupported claims log, scoring sheet | Map article claims to evidence, update unsupported claims log, and fill scoring sheet only from captured evidence. Remove or rewrite unsupported conclusions. | Claim map, unsupported claims log, and scoring sheet are complete with no fabricated or placeholder scores. | Scores are guessed, claims lack evidence, or unresolved `FACT CHECK`, `TODO`, `VERIFY`, or `needs evidence` markers remain. Keep staging/noindex. |
| Day20 | Article rewrite from measured evidence + publish dry run | Rewrite the article from measured evidence. Run generated HTML QA. Confirm canonical, robots, sitemap, noindex, title/meta, and evidence links in built output before changing any public gate. | Publish dry run shows exactly one candidate could become public/indexable on the final URL with clean generated HTML. | Generated HTML fails QA, sitemap/canonical/noindex conflict, or more than one URL would become public. Keep staging/noindex. |
| Day21 | One-URL launch checklist or dry-run report | Run [publish checklist](publish-checklist.md). If every gate passes, publish exactly one URL and begin the baseline. If any gate fails, keep staging/noindex and fill the baseline as a dry-run report. | PASS: one URL only is public/indexable, final canonical is used, sitemap/GSC/GA4 checks are documented, and [Day 21 public launch baseline](../reports/day-21-public-launch-baseline.md) is updated. | FAIL: no public/indexable post is opened; baseline report records pending blockers with `PENDING`, `NOT RUN`, or `NOT CONFIGURED` values. |

## Stop Conditions

Stop and keep the site noindex/staging if any of these are true:

- Final URL policy is not decided.
- Public `public_base_url` would require a fake or temporary value.
- Host-root robots behavior is not verified.
- GA4/GSC cannot be configured or checked against a real final URL.
- NotebookLM/ChatGPT same-source evidence is incomplete.
- Claim map, unsupported claims log, or scoring sheet still contains placeholders.
- Generated HTML contains unresolved `FACT CHECK`, `TODO`, `VERIFY`, or `needs evidence`.
- Sitemap would include any non-public or non-approved URL.
- More than one post would become public/indexable.

When a stop condition is hit, do not publish. Keep noindex/staging and update [Day 21 public launch baseline](../reports/day-21-public-launch-baseline.md) as a dry-run report.

## Not Evidence Yet

The Day 21 baseline is technical readiness evidence. It can show that the publishing pipeline works, the page is eligible for crawl/indexing, measurement fires, and QA is reproducible.

It is not evidence of:

- SEO validation.
- A winning article angle.
- AdSense eligibility.
- Affiliate conversion.
- Long-term traffic potential.
- Repeatable content-market fit.

Do not use a one-URL technical baseline to justify AdSense, affiliate links, programmatic SEO, or scaled publishing.
