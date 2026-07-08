# Measurement Plan

## Principle

GA4 and GSC are the measurement pipeline for publish decisions. They are not vanity setup and should not be added with fake IDs or placeholder properties.

## Current state

- GA4 is not configured.
- GSC is not configured.
- No public/indexable posts exist.
- Sitemap should remain empty while posts are noindex/staging.
- Internal and test traffic must not be mistaken for organic validation.

## Minimum event schema

Use these event names at minimum:

| Event | Meaning |
| --- | --- |
| `page_view` | Standard page load measurement. |
| `official_tool_click` | Click to an official tool/product homepage or app page. |
| `pricing_click` | Click to official pricing pages. |
| `template_download` | Template or downloadable asset interaction. |
| `affiliate_click` | Approved affiliate link click only after approval/disclosure. |
| `email_click` | Email signup, contact, or mailto click. |

## Event rules

- Do not fire `affiliate_click` for ordinary official links.
- Do not add affiliate events before affiliate links are approved and disclosed.
- Keep event names stable so 7-day and 28-day comparisons are meaningful.
- Use query/source context to evaluate intent, not raw page views alone.

## Internal/test traffic caveat

- Realtime testing can confirm tags work, but it is not audience validation.
- Internal visits, QA checks, local previews, and repeated self-clicks should be excluded or annotated.
- Never click ads for testing. AdSense click testing is out-of-scope and unsafe.

## 7-day technical baseline

| Day | Check | Pass gate |
| --- | --- | --- |
| 1 | GA4 property/data stream is created only when final host is known. | Real measurement ID exists; no fake ID in manifest. |
| 2 | Tag appears in built HTML. | Page view reaches GA4 realtime from a controlled test. |
| 3 | Outbound click events are implemented or manually testable. | Official/pricing/template/email clicks can be distinguished. |
| 4 | GSC property is verified for the final host. | Ownership verified; sitemap submission path known. |
| 5 | Sitemap contains only public/indexable URLs. | No staging/noindex URLs in sitemap. |
| 6 | Internal/test traffic is annotated or filtered. | Test visits are not used as organic performance evidence. |
| 7 | Baseline report is recorded. | Page views, outbound clicks, indexing status, and any errors are logged before new content work expands. |

## Publish measurement gate

The first public post should not be indexed until:

- Final URL policy is decided.
- GA4 page views work.
- Required outbound events are defined.
- GSC property and sitemap flow are ready.
- The post passes evidence and QA gates.
