# Practical AI Workflows — Evidence-backed SEO & Content Automation Lab

Current phase: **SEO/content automation learning experiment with monetization-readiness gates.**

This project is not currently an AdSense revenue plan, affiliate revenue plan, or scaled content production system. The near-term goal is to prove that one evidence-backed workflow article can be made indexable, measured, and maintained without weakening the evidence or policy gates.

## Build locally

```bash
python3 scripts/build.py
python3 -m http.server 8787 -d dist
```

Open `http://localhost:8787`.

## Current safety setting

`dist/robots.txt` blocks indexing with `Disallow: /` because all posts are still staging/noindex. Do not public-index or submit URLs until the final URL, canonical, sitemap, evidence, and measurement policies are clear.

## Cloudflare Pages

- Build command: `python3 scripts/build.py`
- Output directory: `dist`
- Free URL target: `practical-ai-workflows.pages.dev`
- Final public URL: not decided. Do not add fake domain, GA4, GSC, AdSense, or affiliate values.

## Strategy docs

- [Current phase](docs/current-phase.md)
- [Day 15-21 overhaul plan](docs/day-15-21-overhaul-plan.md)
- [Publish checklist](docs/publish-checklist.md)
- [Day 21 public launch baseline](reports/day-21-public-launch-baseline.md)
- [Public URL policy](docs/public-url-policy.md)
- [Monetization readiness gates](docs/monetization-readiness-gates.md)
- [Measurement plan](docs/measurement-plan.md)
- [Affiliate ledger template](data/affiliate-ledger.yml)

## Do not public-index yet

Before real indexing: remove unresolved markers, attach evidence screenshots/raw outputs, date pricing and tool claims, keep disclosure/methodology pages live, install measurement, and confirm the final host/root robots/canonical/sitemap policy.
