# Practical AI Workflows 3-Day Content Factory Handoff — 2026-07-09

Linked hub: [[프로젝트 운영 허브]]

## Current state at save time

Saved: 2026-07-09 14:25 KST.

The project must stop behaving like a single cautious NotebookLM test and switch into a compressed 3-day agentic content factory because the user's 카쫀쿠 / scarce execution window has about 3 days left.

Live site:
- https://practical-ai-workflows.pages.dev
- First public article: https://practical-ai-workflows.pages.dev/notebooklm-vs-chatgpt-for-studying-pdfs/
- GA4: `G-Z1GHN2WDGC`
- GSC verification tag deployed: `fUeVN4-aAJjDqU-6KLZ64yZPnRDjSIblzVicj4bf880`
- Sitemap submitted in GSC.
- GSC URL inspection still temporarily reports stale `robots.txt` block after the earlier noindex/Disallow flip; server is verified as `Allow: /` and article is `index,follow`.

Repo/worktree:
- Local: `/Users/kmnoh/.hermes/obsidian-vault/content-lab/site`
- GitHub: `kmnoh12/practical-ai-workflows`
- Latest relevant commits:
  - `9478b63 Launch first measured indexable article`
  - `ebc692e Record sitemap submission and launch smoke checks`
  - `616a255 Define multi-category content factory backlog`

Key files already created:
- `factory-plan.md`
- `content-queue.csv`
- `metrics.md`
- `distribution/notebooklm-vs-chatgpt-launch-pack.md`
- first article under `content/posts/notebooklm-vs-chatgpt-for-studying-pdfs.md`

## User correction / strategic reset

User correction: do not narrow this to “one article experiment.” The agent advantage is not one careful human-like article. It is nonstop production and orchestration:

- many useful articles across multiple categories,
- traffic-first + money-first + template/download posts,
- safe distribution/viral repackaging,
- AdSense readiness,
- Google ranking attempts via clusters/internal links,
- repeated publishing and measurement without stopping.

Do **not** spend next session making more meta-docs. The next session should start execution immediately.

## 3-day compressed goal

### Day 1 — publish-volume base, not another plan

Target by end of Day 1:
- publish 5 public useful URLs, not drafts only;
- each with one small useful asset/template/checklist;
- create/verify category pages and internal links;
- keep build/QA green and push to Cloudflare;
- create distribution packs for all 5.

Day 1 article set:
1. `How to Use NotebookLM to Study a PDF Without Losing the Source Trail`
   - asset: NotebookLM study checklist
   - purpose: expand AI study cluster from first article
2. `The ChatGPT Prompt I Use to Turn PDFs into Study Guides`
   - asset: copyable PDF study prompt pack
   - purpose: search/autocomplete traffic
3. `Best AI Productivity Tools by Workflow, Not Hype`
   - asset: tool decision matrix
   - purpose: broad AI productivity traffic hub
4. `Make vs Zapier for Creators: Which Automation Tool Should You Pick?`
   - asset: creator automation checklist
   - purpose: money/revenue intent start
5. `Creator Automation Stack for Beginners: Landing Page, Email, Checkout, Delivery`
   - asset: creator stack checklist
   - purpose: money hub/internal link hub

### Day 2 — expand to AdSense/content mass

Target by end of Day 2:
- total public URLs: 15+;
- at least 5 money-intent SaaS/comparison pages;
- at least 5 templates/download assets;
- add `about`, `contact`, `privacy-policy`, and disclosure/editorial pages if missing or weak;
- submit updated sitemap and attempt GSC indexing where available.

Day 2 priority candidates:
- `Kit vs beehiiv for Solo Creators`
- `Gumroad vs Lemon Squeezy for Digital Products`
- `15 Zapier Automation Ideas for Creators That Save Real Time`
- `How to Automate Lead Magnet Delivery Without a Course Platform`
- `Airtable vs Google Sheets for Creator Operations`
- `Notion Content Calendar Automation for Solo Creators`
- `AI Meeting Notes Workflow`
- `AI Content Brief Template`
- `Prompt Library Template`
- `Content Repurposing Checklist`

### Day 3 — distribution and AdSense readiness sprint

Target by end of Day 3:
- total public URLs: 25–30 if quality gate can hold;
- 10 downloadable assets/templates;
- category hubs/internal links solid;
- sitemap public and submitted;
- GA4/GSC verified;
- AdSense readiness pages present;
- at least one distribution attempt per top 10 article.

Distribution must be platform-native, not spam:
- Reddit: value-first text post/comment, link only when allowed or in follow-up if requested.
- X/Threads: 5–8 post thread per article.
- LinkedIn: workflow/business framing.
- HN/Product Hunt only for actual template/tool pages, not generic articles.

## Production rule for next session

Start with file/code execution, not explanation.

Minimum next-session command path:
1. `cd /Users/kmnoh/.hermes/obsidian-vault/content-lab/site`
2. Read `content-queue.csv`, `factory-plan.md`, `scripts/build.py`, `scripts/qa.py`, existing first article/template structure.
3. Generate Day 1 five articles + assets + distribution packs.
4. Add category/internal links.
5. Run:
   - `python3 scripts/build.py`
   - `python3 scripts/qa.py`
   - `git diff --check`
6. Commit and push.
7. Verify live URLs with `curl`.
8. Update `metrics.md`.
9. Only then summarize.

If QA blocks because it was overfit to first article, update QA to validate the broader factory structure instead of reducing output back to one post.

## Active todos to carry forward

- `parallel-research`: traffic/revenue/viral subagents were dispatched in the previous session and may return later; incorporate them if available, but do not wait for them before producing Day 1 content.
- `next-sprint`: convert pending queue into actual public article batch immediately.

## Async delegation results received at 2026-07-09 14:26 KST

Three background subagents finished after this handoff was first created. Incorporate these results immediately in the next session.

### 1) Broad traffic categories

Full summary file:
- `/Users/kmnoh/.hermes/cache/delegation/subagent-summary-0-20260709_142617_123571.txt`

High-traffic English category expansion candidates:
- printable templates, planners, and checklists;
- home organization and cleaning guides;
- appliance and household troubleshooting;
- gardening, houseplants, and lawn care;
- food substitutions and kitchen basics;
- travel packing, itineraries, and local micro-guides;
- consumer software and app tutorials;
- workplace writing templates and everyday communication;
- hobbies, crafts, DIY projects, and patterns;
- kids activities, worksheets, and family entertainment.

Blunt instruction: do not move all of these into Day 1. Use them as expansion lanes after the Practical AI Workflows core starts producing. Best near-term fit for the current site: consumer software/app tutorials, workplace writing templates, printable templates/checklists, and creator/productivity templates. Avoid health, legal, tax, insurance, child-data collection, dangerous appliance/gas/electrical instructions, and thin generic filler.

### 2) Money-first category map

Created artifact:
- `/Users/kmnoh/Library/CloudStorage/OneDrive-개인/Obsidian Vault/content-lab/01_keywords/money-first-category-map-2026-07-09.md`

It contains 12 monetizable clusters and 60 article opportunities with estimated traffic/revenue scores. Treat this as the Day 1/2 re-ranking source. It sampled autocomplete but does not contain paid SEO-tool volume/CPC; scores are strategy estimates.

### 3) Ethical distribution workflow

Created artifact:
- `/Users/kmnoh/Library/CloudStorage/OneDrive-개인/Obsidian Vault/content-lab/site/distribution/ethical-distribution-agent-workflow.md`

Use it as the operating rule for viral/distribution. Per article, generate:
- Reddit/community text-first version;
- X/Threads 5–8 post thread;
- LinkedIn workflow post;
- short-form script;
- comment response bank;
- metrics row.

Do not fake traffic, use engagement pods, mass-post, automate DMs, manipulate votes, or spam communities. Distribution must be value-first and platform-native.

## Success definition

Not success:
- more strategy docs,
- more noindex dry runs,
- one perfect article,
- generic SEO explanation.

Success:
- public URLs shipped,
- assets shipped,
- internal links and sitemap updated,
- distribution copy ready/used,
- GSC/GA4 measurement running,
- AdSense-readiness pages created,
- the site looks like a useful multi-category resource, not an AI meta-project.
