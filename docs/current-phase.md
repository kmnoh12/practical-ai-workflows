# Current Phase

## Phase name

Practical AI Workflows is currently an **SEO/content automation learning experiment with monetization-readiness gates**.

Internal shorthand: **Evidence-backed SEO & Content Automation Lab**.

## What this project is

- A staging/noindex static site for learning whether narrow, evidence-backed AI workflow articles can earn search impressions and useful outbound clicks.
- A publishing pipeline experiment: evidence capture, post structure, QA, canonical/sitemap policy, and measurement.
- A future monetization candidate only after traffic, indexing, evidence, and policy gates are met.

## What this project is not

- Not an AdSense revenue project yet.
- Not an affiliate revenue project yet.
- Not a scaled content production system.
- Not a revenue forecast, traffic forecast, or "monthly income" plan.
- Not ready for public indexing, Search Console submission, AdSense review, or affiliate-link insertion.

## Must do now

- Keep the site in staging/noindex.
- Finish one evidence-backed public candidate: `notebooklm-vs-chatgpt-for-studying-pdfs`.
- Capture reproducible evidence before publishing: same source, same prompt, raw outputs, screenshots, scoring notes, test date, limitations, and official source touchpoints.
- Decide the final URL policy before indexing: custom domain now for a serious 90-day experiment, or explicitly keep AdSense out-of-scope while using free/subpath infrastructure.
- Prepare GA4/GSC as a measurement pipeline, not as vanity setup.
- Keep sitemap empty while there are no public/indexable posts.

## Later

- AdSense application.
- Affiliate monetization expansion.
- Email capture and social distribution.
- Template marketplace.
- Programmatic SEO or scaled publishing.
- CMS migration.
- Revenue projections.

## Repo-adapted 14-day execution plan

This adapts the 01/05 source answer to the current repo state: build and QA already pass in staging, all posts are noindex, GA4/GSC/domain are not configured, and the NotebookLM article is the first public candidate.

| Day | Work | Pass gate |
| --- | --- | --- |
| 1 | Reframe docs from monetization plan to SEO/content automation learning experiment. | README, manifest, and policy docs state monetization is deferred. |
| 2 | Decide public URL path. | Either custom domain is selected for a 90-day serious experiment, or AdSense remains explicitly out-of-scope. |
| 3 | Define GA4 event schema and setup requirements. | Event names are documented before any tracking ID is added. |
| 4 | Define GSC/sitemap readiness flow. | Only public/indexable URLs can enter sitemap; no staging/noindex URLs. |
| 5 | Freeze evidence folder structure for the NotebookLM candidate. | Required evidence files are known and reproducible. |
| 6 | Run same-source NotebookLM vs ChatGPT test. | Same source, same prompt, raw outputs, screenshots, limitations, and test date captured. |
| 7 | Rewrite the NotebookLM article from evidence. | Results, scoring, recommendation, limitations, and checked-date claims are supported. |
| 8 | Strengthen QA only if required by the publish gate. | `python3 scripts/build.py && python3 scripts/qa.py` still pass. |
| 9 | Do a publish dry run. | Exactly one candidate would become indexable; robots/sitemap/canonical behavior is understood. |
| 10 | Publish only after gates pass. | One post only becomes indexable, with final canonical host, sitemap entry, and GA4/GSC ready. |
| 11 | Post-publish technical QA. | HTML source, robots, sitemap, canonical, GSC inspection, and GA4 realtime are checked. |
| 12 | Select the second post candidate. | Narrow scenario with evidence potential; no broad "best tools" article. |
| 13 | Prepare affiliate intent measurement only. | Program shortlist and ledger exist, but no affiliate links are inserted before approval. |
| 14 | Review gate. | Continue only if one public evidence post, measurement, GSC/sitemap, QA, URL policy, and next narrow candidate are clear. |

## Do not do

- Do not unblock the whole site.
- Do not make any post indexable before evidence, measurement, final URL, and QA gates pass.
- Do not apply to AdSense while using an uncertain path-based URL.
- Do not add affiliate links before program approval, disclosure, and `rel` policy are ready.
- Do not add fake GA4, GSC, AdSense, affiliate, domain, or revenue values.
- Do not mass-generate new posts.
- Do not treat robots.txt as a security system.
- Do not migrate to WordPress or another CMS to avoid the real bottleneck: evidence, measurement, indexing, and QA.
- Do not make revenue projections from zero traffic and zero conversion data.
