# Monetization Readiness Gates

## Current policy

AdSense and affiliate revenue are deferred. The current project phase is measurement and evidence, not monetization.

## AdSense defer statement

Do not apply to AdSense now. The site has no public/indexable posts, no GA4/GSC data, no verified organic traffic, no final public URL policy, and no AdSense-valid application domain configured.

## AdSense reactivation gates

Resume AdSense preparation only when all gates pass:

| Gate | Requirement |
| --- | --- |
| URL | Custom domain or AdSense-valid standard domain. No path-based application URL. |
| Content | At least 5 public/indexable evidence-backed posts. No unresolved `FACT CHECK`, `TODO`, `VERIFY`, or placeholder language. |
| Evidence | Each public post includes source, prompt, raw output or screenshot, test date, scoring/decision basis, and limitations. |
| Indexing | GSC shows public URLs entering discover/index workflows. |
| Measurement | GA4 page views and outbound click events are working. |
| Traffic | Recent 28-day organic impressions reach 300+ or organic users reach 100+. Zero traffic is not enough. |
| Policy pages | About, Contact, Privacy, Editorial/Methodology, and Affiliate/Ad disclosure pages are live. |
| Technical | Sitemap contains only indexable URLs; robots/noindex/canonical do not conflict. |

## Stricter AdSense apply gates

Apply only after:

- 8-10 indexable evidence-backed posts.
- 300+ organic users in the most recent 28 days.
- At least 30 days of operating logs after public launch.
- Policy and technical QA pass.
- No artificial traffic, click prompting, or self-click testing.

These numbers are internal risk gates, not a claim that Google publishes a fixed post or traffic threshold.

## Affiliate first-30-day strategy

The first 30 days of affiliate work are for **intent measurement**, not revenue.

- Shortlist only 2-3 relevant programs.
- Before approval, link only to official product, pricing, source, or documentation pages.
- Track whether posts generate official tool clicks, pricing clicks, template downloads, and email clicks before inserting affiliate URLs.
- Treat revenue as zero. Use click intent to decide whether a topic deserves another evidence-backed article.
- Keep broad "best AI tools" posts out of scope; use narrow scenarios where evidence can be captured.

## Link, disclosure, and `rel` policy

- If an affiliate link exists, disclose clearly near the top of the post and near the first affiliate call-to-action or comparison link.
- Affiliate links should use `rel="sponsored nofollow"` unless a program gives a stricter requirement.
- Non-affiliate official links can remain normal editorial links unless another policy requires otherwise.
- Never hide disclosure only in the footer.
- Keep approved program status, disclosure text, `rel` attribute, and last-checked date in `data/affiliate-ledger.yml`.

## Invalid traffic and click safety

- Do not click your own ads.
- Do not ask users to click ads.
- Do not buy bot, incentivized, or low-quality traffic.
- Do not run traffic manipulation experiments.
- Do not test AdSense clicks after ads are live.
- Do not place ads or affiliate links in ways that confuse users about what is editorial versus paid.
