# Public URL Policy

## Recommendation

If Practical AI Workflows is a serious 90-day experiment, buy/use a custom domain now and keep AdSense deferred. The domain is not for branding polish; it stabilizes canonical URLs, sitemap submission, robots.txt location, and future AdSense eligibility checks.

If this is not a committed 90-day experiment, wait on the domain and keep AdSense completely out-of-scope. Continue as a staging SEO/content automation lab until one public evidence post and measurement pipeline are proven.

## Current repo state

- No final public domain is configured.
- `site-manifest.json` has `base_path: "/practical-ai-workflows"` for subpath-compatible builds.
- No fake `site_url`, GA4, GSC, AdSense, or affiliate values should be added.
- All posts remain staging/noindex.

## GitHub Pages subpath caveat

Project Pages-style subpaths such as `/practical-ai-workflows/` create two risks:

- AdSense site application risk: AdSense review expects a standard site URL, not a path-based application URL.
- Robots root risk: `robots.txt` applies at the root of the host. A project subpath file such as `/practical-ai-workflows/robots.txt` is not the same as host-root `/robots.txt`.

Cloudflare Pages with a root project URL is cleaner than a GitHub Pages project subpath, but the same policy still applies: do not index until the final canonical host and root robots behavior are known.

## Decision tree

| Decision | Use when | Policy |
| --- | --- | --- |
| Buy/use domain now | 90-day serious experiment, name stable enough, one evidence post likely within 14 days. | Attach domain, verify HTTPS, set final canonical host, confirm root `/robots.txt`, then prepare GA4/GSC. AdSense still deferred. |
| Wait 7 days | Brand/name is still moving, but the experiment is likely to continue. | Keep staging/noindex and do not apply to AdSense. Revisit after the first evidence candidate is finished. |
| Do not buy | 90-day commitment is unclear, fully free infrastructure is a hard constraint, or no public post is likely in 14 days. | Keep AdSense out-of-scope. Continue only as an SEO/content automation learning experiment. |

## Indexing rule

No final public indexing until all are clear:

- Final public host.
- Canonical URL format.
- Host-root robots.txt behavior.
- Sitemap policy that includes only public/indexable URLs.
- GA4/GSC measurement plan.
- One post passing evidence and QA gates.

## Fail-closed post gate

A post is public/indexable only when all frontmatter gates are explicit:

- `status: "published"`
- `indexable: true`
- `qa_approved: true`
- `noindex: false`

Missing or ambiguous values default to non-public. `status: "published"` by itself is a QA failure, not a public signal.
