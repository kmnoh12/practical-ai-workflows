# Practical AI Workflows — Free Static Site

Zero-cost MVP path for the content lab.

## Build locally

```bash
python3 scripts/build.py
python3 -m http.server 8787 -d dist
```

Open `http://localhost:8787`.

## Current safety setting

`dist/robots.txt` blocks indexing with `Disallow: /` because the first 4 posts are still evidence-needed.

## Cloudflare Pages

- Build command: `python3 scripts/build.py`
- Output directory: `dist`
- Free URL target: `practical-ai-workflows.pages.dev`

## Do not public-index yet

Before real indexing: remove FACT CHECK markers, attach evidence screenshots, date pricing/affiliate claims, and keep disclosure/methodology pages live.
