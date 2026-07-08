# Practical AI Workflows

Purpose: build a revenue-oriented content factory, not a noindex evidence lab.

Current experiment: publish one user-facing asset for `notebooklm-vs-chatgpt-for-studying-pdfs` and measure Google/search/social/download behavior for 30 days.

Active files:

- `experiment.md` — hypothesis, asset, success/failure criteria.
- `metrics.md` — weekly traffic/download/signup notes.
- `content/posts/notebooklm-vs-chatgpt-for-studying-pdfs.md` — first article candidate.
- `automation-lab-archive/` — frozen Hermes/Codex evidence and QA lab artifacts.

Build:

```bash
python3 scripts/build.py
python3 scripts/qa.py
```

Next real work: create the public-ready article + free PDF Study Workflow Template + GA4/GSC-ready launch path.
