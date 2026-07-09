# Ethical Distribution Agent Workflow

Site: `https://practical-ai-workflows.pages.dev`  
Current live unit: `notebooklm-vs-chatgpt-for-studying-pdfs`  
Principle: make each article genuinely useful in the places where the audience already asks that question. No fake traffic, no engagement pods, no spam, no mass posting, no automated account behavior.

## 1. Operating loop

Run this loop once per approved article. Do not start a second article's distribution until the first one has at least one real distribution attempt and a measurement note.

```text
Article approved
→ Distribution Fit Agent
→ Asset Pack Agent
→ Community Rules Agent
→ Human Approval Gate
→ Manual / assisted posting
→ Feedback Capture Agent
→ Metrics Agent
→ Decision: keep, revise, expand, or stop
```

### Agent roles

1. **Distribution Fit Agent**
   - Reads the article, template/download asset, and intended audience.
   - Selects only 3-5 plausible channels.
   - Labels each channel as: `high fit`, `maybe`, or `do not post`.
   - Output: channel list, audience rationale, risk notes.

2. **Asset Pack Agent**
   - Creates platform-native versions from the research, not copy-pasted article text.
   - Produces Reddit/community posts, X/Threads thread, LinkedIn post, short-video script, feedback DMs, and a downloadable/template CTA.
   - Output: one launch pack under `distribution/{slug}-launch-pack.md`.

3. **Community Rules Agent**
   - Checks posting rules before any community post.
   - Flags self-promo bans, flair requirements, link restrictions, karma/account-age expectations, and preferred post formats.
   - Output: `allowed`, `allowed without link`, `ask mods first`, or `do not post`.

4. **Human Approval Gate**
   - User approves final copy, target channel, link placement, disclosure, and posting timing.
   - Required for Reddit, Hacker News, Product Hunt, LinkedIn, X/Threads, replies, DMs, and any logged-in account action.

5. **Feedback Capture Agent**
   - Records real comments, objections, questions, downloads, signups, and quote-worthy user language.
   - Does not argue, astroturf, or manipulate votes.

6. **Metrics Agent**
   - Updates `metrics.md` weekly with external signals only.
   - Separates organic search, referral visits, downloads, email signups, direct feedback, and platform comments.

## 2. Per-article asset checklist

For each article, create this bundle before posting anywhere:

| Asset | Required? | Purpose |
| --- | --- | --- |
| Canonical article URL | Required | Search/indexable destination. |
| Downloadable/template/checklist | Required | Gives people a reason to save or share. |
| 1-sentence positioning | Required | Explains the practical outcome, not the topic. |
| 3 title variants | Required | Use per platform, not keyword stuffing. |
| Reddit/community version A | Required | Text-first, link optional, asks for specific feedback. |
| Reddit/community version B | Optional | Different angle for a different community; never duplicate-post. |
| X/Threads thread | Required | 5-8 useful posts, link only at end. |
| LinkedIn post | Required | Professional/workflow framing, one clear takeaway. |
| Short-form video script | Required | 30-45 sec screen recording or talking-head script. |
| Feedback DM template | Optional | For 5 personalized asks, not mass outreach. |
| Visual card / screenshot idea | Optional | One simple checklist/table screenshot. |
| Comment response bank | Required | Helpful answers to likely questions; no canned spam. |
| Metrics row | Required | Add baseline row in `metrics.md`. |

## 3. Channel strategy

### Reddit

Use only when the post can stand alone without the link.

- Best fit for this site: student/productivity/AI-tool communities where people already ask about PDF studying, NotebookLM, ChatGPT workflows, prompts, or AI study habits.
- Post format: native text post, practical test summary, narrow question, link only if rules allow.
- Cadence: max 1 subreddit per article per week; no duplicate copy; no cross-post blast.
- Approval gate: rules checked + user approves exact subreddit and copy.
- Good CTA: "What would make this checklist more useful for a real study session?"
- Bad CTA: "Please read/upvote/share my article."

### X / Threads

Use for concise insights and repeatable frameworks.

- Post format: 5-8 post thread with a useful takeaway before the link.
- Cadence: 1 launch thread, then 2-3 derivative posts over 7 days if there is a distinct angle.
- Examples of derivative angles:
  - one prompt from the article;
  - one comparison table;
  - one mistake to avoid;
  - one screenshot of the template.
- Do not auto-reply to trending posts with links.
- Do not tag large accounts unless the post genuinely discusses their work and adds value.

### LinkedIn

Use for workflow, education, creator-ops, and professional productivity framing.

- Post format: 150-300 words, practical lesson, one question for feedback.
- Cadence: 1 post per article; optional follow-up only if comments reveal a real angle.
- Good angles:
  - "what process makes AI output checkable?"
  - "how to turn a PDF into retrieval practice;"
  - "source-grounding before explanation."
- Avoid exaggerated thought-leader language and fake certainty.

### Hacker News

Use rarely. Only submit if the article is technical, novel, tool-like, or has a strong build/evidence angle.

- Fit for current NotebookLM vs ChatGPT study article: probably low/medium fit, unless reframed as a reproducible same-source evaluation with data and code/template.
- Better HN candidates from queue:
  - Cloudflare Pages + GSC setup for a free static site;
  - AI tool comparison template with transparent rubric;
  - static-site analytics/measurement write-up.
- Cadence: max 1 submission when genuinely HN-fit; do not ask anyone to upvote.
- Never coordinate votes or comments.

### Product Hunt

Use only for a real product/tool/template, not a plain article.

- Fit for current site: not yet, unless the downloadable template becomes a packaged mini-tool or template library.
- Launch requirement:
  - named product/template;
  - landing page;
  - clear screenshots;
  - free download/use path;
  - maker comment;
  - support plan for comments.
- Do not launch every article.

### Communities, newsletters, Discords, forums

Use only where the community welcomes resources and where the agent can identify an existing question/problem.

- Preferred motion: answer a specific question with useful detail; include link only as optional further reading if allowed.
- Cadence: 3-5 personalized community/outreach attempts per article, not mass posting.
- Ask moderators first when rules are unclear.

### Short-form video

Use for discovery, not as fake virality.

- One 30-45 sec script per article.
- Format: problem → mini-test/workflow → checklist/template → link in profile/comments if platform norms allow.
- Cadence: 1 video per article; optionally cut into 2 variants if the first gets real watch/comment signal.
- Do not use misleading hooks or fake results.

## 4. Cadence for the first 30 days

Goal: get real signal, not volume.

### Day 0: prep

- Verify article URL, download asset, metadata, and GA4/GSC setup.
- Create launch pack.
- Add metrics baseline row.
- Choose 3-5 target channels.

### Day 1: first public distribution

- Post one high-fit channel only.
- For current article, recommended first attempt: one Reddit/community text post or one LinkedIn post asking for workflow feedback.
- Record URL, time, copy version, and expected signal.

### Day 2-3: listen and respond

- Reply only to real comments with useful answers.
- Do not bump, repost, or ask friends for engagement.
- Capture objections/questions into a feedback note.

### Day 4-5: second channel

- Publish X/Threads thread or LinkedIn post using a different angle.
- Link at end; lead with the insight/template.

### Day 7: first metrics check

- Update `metrics.md` with: referral visits, downloads, comments, signups, feedback.
- Make one improvement if feedback is clear: title, CTA, template preview, or missing section.

### Day 10-14: third channel or derivative asset

- If there is positive signal: publish short video or community version B.
- If no signal: revise positioning before posting more.

### Day 21: search and referral check

- Check GSC impressions/clicks if available.
- Check which channel produced actual visits/downloads.
- Decide whether to create a follow-up article or improve the template.

### Day 30: decision

- Continue, revise, expand, or kill/pivot based on real metrics.

## 5. Approval gates

### Must be Green before posting

- Article is public/indexable and QA-approved.
- Download/template link works.
- Claims are not overstated.
- Community rules checked.
- Copy is platform-native and not duplicated across communities.
- Human approves the exact text and target channel.
- Affiliate/sponsorship disclosure present if relevant.

### Yellow: revise or ask first

- Community has unclear self-promo rules.
- Post needs a link to make sense.
- Article makes a comparison claim from limited evidence.
- The post mentions a brand/tool in a way that could look like promotion.
- The channel has strong anti-promo norms.

### Red: do not post

- Link dump.
- Same copy posted elsewhere.
- Community bans self-promotion.
- Post asks for upvotes, shares, clicks, or traffic.
- Article has unverified claims or misleading title.
- The only goal is backlink/SEO manipulation.

## 6. What not to do

- No fake traffic, bots, traffic exchanges, paid click farms, engagement pods, or self-clicking ads.
- No asking friends/agents to upvote, comment, or click for signal.
- No mass posting the same copy across Reddit, forums, Discords, X, Threads, LinkedIn, or newsletters.
- No fake testimonials, fake screenshots, fake download counts, fake comments, or fake case studies.
- No automated DMs or cold outreach blasts.
- No pretending to be a student/user/customer if posting as the site owner.
- No link-only posts unless the platform explicitly supports link submissions and the article is a fit.
- No ragebait or exaggerated claims like "X is dead" or "this changes studying forever."
- No posting in communities where the article is off-topic just because traffic is high.
- No HN/Product Hunt submissions unless the asset is genuinely fit for those audiences.

## 7. KPIs and decision thresholds

Track only real external behavior.

| KPI | 7-day signal | 30-day success threshold | Decision use |
| --- | ---: | ---: | --- |
| Referral visits | 1+ | 5+ | Channel produced attention. |
| Template/download clicks | 1+ | 10+ | Asset has utility. |
| Direct feedback/comments | 1+ | 3+ | Audience has a problem worth solving. |
| GSC impressions | Any | 100+ | Search is discovering the page. |
| GSC clicks | Any | 5+ | Title/query fit exists. |
| Email signups | 0 acceptable early | 3+ | Continue building owned audience. |
| Qualified share/save/bookmark comments | Any | 3+ | Topic has repeat value. |
| Product/template requests | Any | 1+ | Consider turning asset into tool/template pack. |

### Decisions

- **Keep:** at least one real external signal appears and feedback is neutral/positive.
- **Revise:** traffic exists but downloads/feedback are zero; improve CTA, template preview, or angle.
- **Expand:** one article gets search/referral/download signal; create adjacent article/template from the same problem cluster.
- **Stop:** no impressions, no referral visits, no downloads, no feedback after 30 days and one honest distribution attempt.

## 8. Current article recommended launch sequence

Article: `NotebookLM vs ChatGPT for Studying PDFs`

1. First attempt: one high-fit Reddit/community post **if rules allow link or text-first resource sharing**. If not, use LinkedIn first.
2. Second attempt: X/Threads thread using the "workflow matters more than winner" angle.
3. Third attempt: LinkedIn post for educators/tutors/productivity people.
4. Fourth attempt: 30-45 sec short video showing the same prompt → output → claim-check checklist.
5. Optional outreach: 5 personalized feedback asks to students, tutors, educators, AI-tool evaluators, or productivity creators.

Do not submit this article to Product Hunt. Do not submit to Hacker News unless it is reframed as a reproducible evaluation/template with stronger technical detail.

## 9. Minimal tracking table per post

Add this to the launch pack or weekly metrics note:

| Date | Article | Channel | URL/post ID | Copy version | Link included? | Visits | Downloads | Comments/feedback | Decision |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- |

## 10. Weekly agent prompt

```text
You are the Metrics Agent for practical-ai-workflows.pages.dev.
Read metrics.md and the latest distribution launch pack.
Update only real external signals: GSC impressions/clicks, referral visits, downloads, signups, comments, and direct feedback.
Do not invent numbers. If data is unavailable, write unavailable.
Recommend exactly one next action: keep, revise CTA, post one more channel, create short video, expand cluster, or stop.
```
