# Session Log — 2026-07-08

## Purpose

Record the actual sequence and outcome of the Day 13–21 Practical AI Workflows work so future Hermes/Codex sessions can recover context without rereading the whole chat.

Related hub/docs:

- [Current phase](current-phase.md)
- [Day 15–21 overhaul plan](day-15-21-overhaul-plan.md)
- [Day 13 NotebookLM evidence pack](day-13-notebooklm-evidence-pack.md)
- [Publish checklist](publish-checklist.md)
- [Day 21 public launch baseline](../reports/day-21-public-launch-baseline.md)

## Starting context

The project was already reframed from an AdSense/revenue sprint into a staging/noindex SEO/content automation learning experiment. GPT-5.5 Pro/frontier feedback had pushed the project toward:

1. do not treat AdSense as current goal;
2. decide final URL/custom domain before public indexing;
3. keep fake GA4/GSC/domain/AdSense values out of the repo;
4. make one evidence-backed public candidate before scaling;
5. fail closed with noindex/staging until gates pass.

The first candidate remained:

```text
notebooklm-vs-chatgpt-for-studying-pdfs
```

## Work completed

### 1. NotebookLM and ChatGPT same-source evidence capture

Evidence folder:

```text
docs/day-13-notebooklm-evidence-pack-files/
```

Completed artifacts include:

- `same-source-study-notes.md`
- `same-source-study-notes.pdf`
- `same-source-prompt.txt`
- `notebooklm-output.md`
- `notebooklm-output-clean-display.md`
- `notebooklm-output-ax-visible.txt`
- `chatgpt-output.md`
- `chatgpt-output-clean-display.md`
- `chatgpt-output-ax-visible.txt`
- `source-claim-map.md`
- `unsupported-claims-log.md`
- `scoring-sheet.csv`
- screenshot PNGs under `screenshots/`

Important operational lesson:

> Do not idle during long ChatGPT/NotebookLM generation. After verifying the external UI is generating, use the wait window to update manifests, checklists, claim maps, scoring sheets, redaction notes, build/QA, and commit prep. Poll opportunistically rather than blocking the whole agent loop.

### 2. ChatGPT delayed completion handled correctly

ChatGPT initially appeared stuck at Korean UI markers like `답변 마무리 중` / `답변 중지`. Instead of treating that as success, it was recorded as incomplete. Later, a recheck showed the ChatGPT answer had completed, including answer key / quiz material and a `3m 19s` generation indicator.

The incomplete attempt was preserved separately, then the real completed output replaced the blocker for scoring/evidence purposes.

### 3. Source-check follow-up completed from local evidence

Codex was asked to perform the pending ChatGPT source-check follow-up from local files only. It compared saved ChatGPT output against `same-source-study-notes.md` and updated:

- `source-claim-map.md`
- `unsupported-claims-log.md`
- `evidence-manifest.md`
- `capture-checklist.md`
- `day-13-notebooklm-evidence-pack.md`
- the article body where source-check status was mentioned

Result:

- no major unsupported educational claims found in ChatGPT primary output;
- one minor partial/explanatory issue remains: ChatGPT's simple-language answer-sheet example for recognition vs recall is consistent with source definitions but not directly stated in the source;
- single-run uncertainty preserved;
- noindex/staging status preserved.

### 4. Editorial QA and screenshot redaction review completed

Codex then performed a consistency/editorial QA pass. It removed stale `pending capture` / missing source-check language and tightened winner claims.

A new file was added:

```text
docs/day-13-notebooklm-evidence-pack-files/editorial-qa.md
```

Current article stance:

- NotebookLM has an edge only for visible source-grounding/source-verification affordances.
- ChatGPT is competitive for student-facing explanation, quiz, and review-plan quality in this single run.
- The article is an evidence-backed noindex staging candidate, not a public/indexable page.

Screenshot state:

- local PNG screenshots were reviewed/redacted for repository evidence;
- no account email/private identifier was visible in the inspected PNGs;
- this is repository-evidence review, not final public evidence-link approval.

### 5. Day 21 launch baseline converted to real no-launch dry run

Codex updated launch/measurement docs so they reflect actual state instead of placeholders or fake launch values.

Updated docs include:

- `reports/day-21-public-launch-baseline.md`
- `docs/publish-checklist.md`
- `docs/current-phase.md`
- `docs/day-15-21-overhaul-plan.md`

Current launch decision:

```text
Published one URL? No.
```

Reason:

- final URL/custom domain not decided;
- GA4 not configured;
- GSC not configured;
- host-root robots behavior not verified;
- stable public evidence-link handling not decided;
- launch checklist not passed.

No fake values were added for:

- custom domain;
- GA4 ID;
- GSC property;
- AdSense;
- revenue;
- traffic;
- impressions;
- clicks;
- indexing status.

## Verification performed

Commands run after the Codex passes:

```bash
git diff --check
python3 scripts/build.py
python3 scripts/qa.py
```

Observed result:

```text
Built 4 posts into dist
Static site QA ... OK
```

Expected warnings remain:

- `dist/robots.txt` may not live at host root because this is a base-path/GitHub Pages-style build;
- three older non-public drafts still contain `FACT CHECK` markers.

Those warnings are not blockers for the NotebookLM/ChatGPT candidate because the candidate remains noindex/staging.

Fail-closed checks performed:

- `dist/robots.txt` contains `Disallow: /`;
- `dist/sitemap.xml` is empty;
- generated HTML pages contain noindex behavior;
- candidate article frontmatter still has `noindex: true`.

## Git commits produced

Latest relevant commits on `main`:

```text
6ce7ac6 Complete noindex launch dry run gates
5c59d91 Capture NotebookLM ChatGPT study evidence
65602e8 Implement evidence-first launch gates and planning docs
8e5913c Add Day 13 NotebookLM evidence pack
6f364ef Complete Day 12 evidence gate pass
```

Latest push target:

```text
https://github.com/kmnoh12/practical-ai-workflows.git
origin/main
```

## Current project state

The candidate article is now:

```text
evidence-backed noindex staging candidate
```

It is not:

- public/indexable;
- AdSense-ready;
- GA4/GSC-ready;
- proof of SEO traction;
- proof of revenue potential;
- a reason to scale publishing yet.

## Remaining decisions

The next human decision is one of:

1. **custom domain / final URL path**
   - choose/buy/use a domain;
   - set final canonical host;
   - verify HTTPS and host-root `robots.txt`;
   - configure GA4/GSC;
   - then consider opening exactly one URL.

2. **continue no-domain staging**
   - keep all posts noindex;
   - do not pursue AdSense;
   - continue evidence-backed article production and dry-run QA;
   - clean older draft `FACT CHECK` markers only when they become candidates.

3. **fix public evidence-link handling before launch**
   - decide whether evidence artifacts are copied to `dist`, omitted from public pages, replaced by curated screenshots, or moved to stable public evidence URLs.

## Operational notes for future Hermes/Codex

- Do not remove `noindex: true` unless final URL, GA4/GSC, sitemap, evidence-link policy, and publish checklist all pass.
- Do not add fake measurement IDs or fake domains.
- Do not treat Codex's final report as proof; Hermes must inspect diff and rerun build/QA.
- Codex raw logs/prompts for this session were left in `/tmp` and were not committed. The durable record is this session log plus the edited docs.
- If asked “where did this stop?”, start from `reports/day-21-public-launch-baseline.md` and `docs/publish-checklist.md`.
