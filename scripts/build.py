#!/usr/bin/env python3
from pathlib import Path
import re, html, shutil, json
ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'content'
DIST=ROOT/'dist'
SITE_TITLE='Practical AI Workflows'
MANIFEST=json.loads((ROOT/'site-manifest.json').read_text(encoding='utf-8')) if (ROOT/'site-manifest.json').exists() else {}
BASE_PATH=str(MANIFEST.get('base_path','')).rstrip('/')
PUBLIC_BASE_URL=str(MANIFEST.get('public_base_url','')).rstrip('/')
SLUG_RE=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
GA4_RE=re.compile(r'^G-[A-Z0-9]+$')

def site_url(path='/'):
    path='/' + str(path).lstrip('/')
    return (BASE_PATH + path) if BASE_PATH else path

def parse_fm(text):
    data={}
    if text.startswith('---'):
        parts=text.split('---',2)
        if len(parts)>=3:
            for line in parts[1].splitlines():
                if ':' in line:
                    k,v=line.split(':',1)
                    v=v.strip().strip('"')
                    if v.lower()=='true': v=True
                    elif v.lower()=='false': v=False
                    else:
                        try: v=int(v)
                        except Exception: pass
                    data[k.strip()]=v
            return data, parts[2].lstrip()
    return data,text

def fm_bool(fm, key, default=None):
    if key not in fm:
        return default
    v=fm[key]
    if isinstance(v,bool):
        return v
    if isinstance(v,str):
        s=v.strip().lower()
        if s=='true':
            return True
        if s=='false':
            return False
    return default

def is_public_candidate(fm):
    return (
        str(fm.get('status','draft'))=='published'
        and fm_bool(fm,'indexable',False) is True
        and fm_bool(fm,'qa_approved',False) is True
        and fm_bool(fm,'noindex',True) is False
    )

def checked_slug(slug):
    slug=str(slug).strip()
    if '/' in slug or '\\' in slug or '..' in slug or not SLUG_RE.fullmatch(slug):
        raise ValueError(f'invalid slug: {slug!r}')
    return slug

def reserve_slug(slug, seen_slugs):
    if slug in seen_slugs:
        raise ValueError(f'duplicate slug: {slug!r}')
    seen_slugs.add(slug)
    return slug

def manifest_bool(key, default=False):
    return fm_bool(MANIFEST, key, default)

def validate_public_launch_prereqs(public_posts):
    if not public_posts:
        return
    errors=[]
    if not PUBLIC_BASE_URL.startswith('https://'):
        errors.append('public build requires https public_base_url in site-manifest.json')
    if manifest_bool('robots_at_host_root', False) is not True:
        errors.append('public build requires robots_at_host_root: true')
    ga4_id=str(MANIFEST.get('ga4_measurement_id','')).strip()
    if not GA4_RE.fullmatch(ga4_id):
        errors.append('public build requires valid ga4_measurement_id matching ^G-[A-Z0-9]+$')
    if not str(MANIFEST.get('google_site_verification','')).strip():
        errors.append('public build requires google_site_verification')
    if errors:
        raise SystemExit('Refusing public/indexable build:\n- ' + '\n- '.join(errors))

def clean_visible(value):
    return str(value).replace('\u2014',' - ').replace('\u2013',' - ')

def md_inline(s):
    s=html.escape(clean_visible(s))
    s=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',r'<img alt="\1" src="\2">',s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'(?<!! )\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    return s

def md_to_html(md):
    lines=md.splitlines(); out=[]; in_ul=False; in_ol=False; in_pre=False; pre=[]; in_table=False; table=[]
    def close_lists():
        nonlocal in_ul,in_ol
        if in_ul: out.append('</ul>'); in_ul=False
        if in_ol: out.append('</ol>'); in_ol=False
    def flush_table():
        nonlocal in_table,table
        if not in_table: return
        out.append('<div class="table"><table>')
        for i,row in enumerate(table):
            cells=[c.strip() for c in row.strip('|').split('|')]
            if i==1 and all(set(c)<=set('-: ') for c in cells): continue
            tag='th' if i==0 else 'td'
            out.append('<tr>'+''.join(f'<{tag}>{md_inline(c)}</{tag}>' for c in cells)+'</tr>')
        out.append('</table></div>'); in_table=False; table=[]
    for line in lines:
        if line.strip().startswith('```'):
            if not in_pre:
                close_lists(); flush_table(); in_pre=True; pre=[]
            else:
                out.append('<pre><code>'+html.escape('\n'.join(pre))+'</code></pre>'); in_pre=False
            continue
        if in_pre: pre.append(line); continue
        if '|' in line and line.strip().startswith('|'):
            close_lists(); in_table=True; table.append(line); continue
        else: flush_table()
        if not line.strip(): close_lists(); continue
        m=re.match(r'^(#{1,6})\s+(.+)$',line)
        if m:
            close_lists(); lvl=len(m.group(1)); out.append(f'<h{lvl}>{md_inline(m.group(2))}</h{lvl}>'); continue
        if line.startswith('>'):
            close_lists(); out.append('<blockquote>'+md_inline(line.lstrip('> ').strip())+'</blockquote>'); continue
        if re.match(r'^[-*]\s+',line):
            if not in_ul: close_lists(); out.append('<ul>'); in_ul=True
            out.append('<li>'+md_inline(re.sub(r'^[-*]\s+','',line))+'</li>'); continue
        if re.match(r'^\d+\.\s+',line):
            if not in_ol: close_lists(); out.append('<ol>'); in_ol=True
            out.append('<li>'+md_inline(re.sub(r'^\d+\.\s+','',line))+'</li>'); continue
        close_lists(); out.append('<p>'+md_inline(line)+'</p>')
    close_lists(); flush_table()
    return '\n'.join(out)

def absolute_url(path='/'):
    path='/' + str(path).lstrip('/')
    return PUBLIC_BASE_URL + path if PUBLIC_BASE_URL else site_url(path)

def layout(title, body, noindex=False, desc='Independent tests of AI agents, model access, reasoning controls, provider limits, and real workflow failures.', path='/', page_type='website', social_image_path='/assets/social/agent-field-notes-og.png', social_image_alt='Practical AI Workflows field notes on model access, reasoning, agent behavior, and verified fixes', date_modified=''):
    robots='<meta name="robots" content="noindex,nofollow">' if noindex else '<meta name="robots" content="index,follow">'
    page_url=absolute_url(path)
    canonical=f'<link rel="canonical" href="{html.escape(page_url)}">'
    social_image=absolute_url(social_image_path)
    safe_title=clean_visible(title)
    safe_desc=clean_visible(desc)
    safe_alt=clean_visible(social_image_alt)
    social_meta=(
        f'<meta property="og:type" content="{html.escape(page_type)}">'
        f'<meta property="og:site_name" content="{SITE_TITLE}">'
        f'<meta property="og:title" content="{html.escape(safe_title)}">'
        f'<meta property="og:description" content="{html.escape(safe_desc)}">'
        f'<meta property="og:url" content="{html.escape(page_url)}">'
        f'<meta property="og:image" content="{html.escape(social_image)}">'
        f'<meta property="og:image:width" content="1200">'
        f'<meta property="og:image:height" content="630">'
        f'<meta property="og:image:alt" content="{html.escape(safe_alt)}">'
        f'<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{html.escape(safe_title)}">'
        f'<meta name="twitter:description" content="{html.escape(safe_desc)}">'
        f'<meta name="twitter:image" content="{html.escape(social_image)}">'
        f'<meta name="twitter:image:alt" content="{html.escape(safe_alt)}">'
    )
    ga4_id=str(MANIFEST.get('ga4_measurement_id','')).strip()
    ga4=''
    if ga4_id:
        ga4=f'''<script>(function(){{if(/^(localhost|127\\.0\\.0\\.1|::1)$/.test(location.hostname))return;window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}window.gtag=gtag;var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id={html.escape(ga4_id)}';document.head.appendChild(s);gtag('js',new Date());gtag('config','{html.escape(ga4_id)}');document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var href=a.getAttribute('href')||'';var eventName='link_click';if(href.includes('/downloads/'))eventName='template_download_click';else if(href.includes('/evidence/'))eventName='evidence_asset_click';else if(/^https?:/.test(href)&&!href.includes(location.hostname))eventName='outbound_official_tool_click';gtag('event',eventName,{{link_url:a.href,link_text:(a.innerText||'').slice(0,80)}});}});}})();</script>'''
    gsc=str(MANIFEST.get('google_site_verification','')).strip()
    gsc_meta=f'<meta name="google-site-verification" content="{html.escape(gsc)}">' if gsc else ''
    adsense_pub=str(MANIFEST.get('adsense_publisher_id','')).strip()
    adsense=''
    if adsense_pub:
        adsense=f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={html.escape(adsense_pub)}" crossorigin="anonymous"></script>'
    nav=f'<header class="site-header"><div class="nav wrap"><a class="brand" href="{site_url("/")}"><span>Practical</span><span>AI Workflows</span></a><nav class="links" aria-label="Primary"><a href="{site_url("/posts/")}">Investigations</a><a href="{site_url("/editorial-policy/")}">Method</a><a href="{site_url("/about/")}">About</a></nav></div></header>'
    motion_js=''
    footer=f'''<footer class="footer wrap"><p><strong>Practical AI Workflows</strong><br>Independent tests of models, agent runtimes, and the gaps between them.</p><nav aria-label="Footer"><a href="{site_url('/posts/')}">Investigations</a><a href="{site_url('/editorial-policy/')}">Editorial policy</a><a href="{site_url('/privacy-policy/')}">Privacy</a><a href="{site_url('/affiliate-disclosure/')}">Disclosure</a><a href="{site_url('/contact/')}">Contact</a></nav><p>© 2026 Practical AI Workflows.</p></footer>'''
    structured=''
    if page_type=='article':
        schema={
            '@context':'https://schema.org',
            '@type':'Article',
            'headline':safe_title,
            'description':safe_desc,
            'mainEntityOfPage':page_url,
            'image':social_image,
            'datePublished':date_modified,
            'dateModified':date_modified,
            'publisher':{'@type':'Organization','name':SITE_TITLE},
        }
        structured='<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=True).replace('</','<\\/')+'</script>'
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(safe_title)} - {SITE_TITLE}</title><meta name="description" content="{html.escape(safe_desc)}"><meta name="theme-color" content="#f5f1e8">{robots}{canonical}{social_meta}{gsc_meta}{ga4}{adsense}{structured}<link rel="stylesheet" href="{site_url("/assets/style.css")}"></head><body><a class="skip-link" href="#content">Skip to content</a>{nav}<main class="wrap" id="content">{body}</main>{footer}{motion_js}</body></html>'

def write_page(path, html_text):
    path.mkdir(parents=True,exist_ok=True)
    (path/'index.html').write_text(html_text,encoding='utf-8')

if DIST.exists(): shutil.rmtree(DIST)
DIST.mkdir(parents=True)
shutil.copytree(ROOT/'public', DIST, dirs_exist_ok=True)
posts=[]
post_sources=[]
seen_slugs=set()
for p in sorted((CONTENT/'posts').glob('*.md')):
    fm,md=parse_fm(p.read_text(encoding='utf-8'))
    slug=reserve_slug(checked_slug(fm.get('slug',p.stem)), seen_slugs); title=fm.get('title',slug.replace('-',' ').title())
    public=is_public_candidate(fm)
    post_sources.append((p,fm,md,slug,title,public))

public_posts=[{'slug':slug,'title':str(title),'category':str(fm.get('category','Workflow')),'order':int(fm.get('order',99)),'status':str(fm.get('status','draft')),'public':public} for _,fm,_,slug,title,public in post_sources if public]
validate_public_launch_prereqs(public_posts)

for p,fm,md,slug,title,public in post_sources:
    desc=str(fm.get('description','')).strip() or 'A tested investigation into AI model access, agent behavior, runtime controls, and practical failure modes.'
    category=clean_visible(fm.get("category","Investigation"))
    updated=clean_visible(fm.get("updated",""))
    body=f'<article class="post"><header class="article-head"><p class="article-meta"><span>{html.escape(category)}</span><time datetime="{html.escape(updated)}">Updated {html.escape(updated)}</time></p><h1>{html.escape(clean_visible(title))}</h1><p class="article-dek">{html.escape(clean_visible(desc))}</p></header>'
    if not public:
        body+=f'<div class="warn"><strong>Status:</strong> {html.escape(str(fm.get("status","draft")))}. Evidence checks are still required before public recommendation.</div>'
    body+=md_to_html(md)+'</article>'
    noindex=not public
    public_path='/' + str(slug).strip('/') + '/'
    social_image_path=str(fm.get('social_image','')).strip() or '/assets/social/practical-ai-workflows-og.png'
    social_image_alt=str(fm.get('social_image_alt','')).strip() or 'Source map, claim check, retrieval practice, and repair workflow'
    write_page(DIST/str(slug), layout(str(title), body, noindex, desc=desc, path=public_path, page_type='article', social_image_path=social_image_path, social_image_alt=social_image_alt, date_modified=updated))
    posts.append({'slug':str(slug),'title':str(title),'category':str(fm.get('category','Workflow')),'order':int(fm.get('order',99)),'status':str(fm.get('status','draft')),'noindex':noindex,'public':public})
for p in sorted((CONTENT/'pages').glob('*.md')):
    fm,md=parse_fm(p.read_text(encoding='utf-8'))
    slug=reserve_slug(checked_slug(fm.get('slug',p.stem)), seen_slugs); title=fm.get('title',slug.replace('-',' ').title())
    page_heading='' if re.search(r'^#\s+',md,flags=re.M) else f'<h1>{html.escape(clean_visible(title))}</h1>'
    body=f'<article class="post page">{page_heading}{md_to_html(md)}</article>'
    desc=str(fm.get('description','')).strip() or 'Editorial notes, evidence, policies, and resources from Practical AI Workflows.'
    write_page(DIST/str(slug), layout(str(title), body, fm_bool(fm, 'noindex', False) is True, desc=desc, path='/' + str(slug).strip('/') + '/'))
visible_posts=public_posts if public_posts else posts
ordered_visible=sorted(visible_posts,key=lambda x:x['order'])
cards='\n'.join(f'<a class="dossier-link" href="{site_url("/" + x["slug"] + "/")}"><span>{i+1:02d}</span><strong>{html.escape(clean_visible(x["title"]))}</strong><em>{html.escape(clean_visible(x["category"]))}</em></a>' for i,x in enumerate(ordered_visible))
featured=next((x for x in ordered_visible if x['slug']=='hermes-agent-gpt-5-6-sol-max-ultra'),ordered_visible[0])
archive_items=[x for x in ordered_visible if x['slug']!=featured['slug']]
archive_cards='\n'.join(f'<a class="dossier-link" href="{site_url("/" + x["slug"] + "/")}"><span>{i+1:02d}</span><strong>{html.escape(clean_visible(x["title"]))}</strong><em>{html.escape(clean_visible(x["category"]))}</em></a>' for i,x in enumerate(archive_items[:5]))
featured_url=site_url('/' + featured['slug'] + '/')
home=f'''<section class="field-hero">
  <div class="hero-copy">
    <p class="overline">Independent agent field notes / July 2026</p>
    <h1>AI agents fail<br>in the gaps.</h1>
    <p class="hero-dek">Independent tests of model access, reasoning controls, orchestration, and the failures hidden between products.</p>
    <div class="hero-actions"><a class="primary" href="{featured_url}">Read the Max / Ultra investigation</a><a href="{site_url('/editorial-policy/')}">How claims are verified</a></div>
  </div>
  <figure class="hero-evidence">
    <img src="{site_url('/assets/evidence/hermes-max-ultra-control-gap.png')}" alt="Control-path audit showing GPT-5.6 Sol, the Hermes xhigh label, max wire support, and the separate Ultra orchestration mode" width="1568" height="948">
    <figcaption><span>Case 01</span> Hermes 0.18.2 / GPT-5.6 Sol / checked 2026-07-10</figcaption>
  </figure>
</section>
<section class="signal-bar" aria-label="Coverage">
  <span>Model access</span><span>Reasoning effort</span><span>Agent orchestration</span><span>Provider limits</span>
</section>
<section class="lead-case" aria-labelledby="lead-case-title">
  <div class="case-index"><span>01</span><p>Featured investigation</p></div>
  <div class="case-copy">
    <p class="case-kicker">GPT-5.6 Sol / Hermes Agent</p>
    <h2 id="lead-case-title">{html.escape(clean_visible(featured['title']))}</h2>
    <p>Hermes reaches the model, labels xhigh as Max, accepts a separate max value in its core, and still cannot recreate Ultra with one setting.</p>
    <a href="{featured_url}">Open the code-level investigation</a>
  </div>
  <dl class="case-verdict">
    <div><dt>Model</dt><dd>GPT-5.6 Sol reached</dd></div>
    <div><dt>UI</dt><dd>xhigh labeled Max</dd></div>
    <div><dt>Wire</dt><dd>max accepted</dd></div>
    <div><dt>Ultra</dt><dd>separate 4-agent mode</dd></div>
  </dl>
</section>
<section class="coverage-map" aria-labelledby="coverage-title">
  <header><p class="overline">What this publication covers</p><h2 id="coverage-title">The model is only one layer.</h2></header>
  <div class="coverage-grid">
    <article class="coverage-main"><span>01</span><h3>Access and entitlement</h3><p>Which model and mode your account can use, which provider route actually serves it, and where a third-party client drops the control.</p></article>
    <article><span>02</span><h3>Runtime behavior</h3><p>Reasoning values, tool loops, subagent inheritance, context handling, and silent fallbacks.</p></article>
    <article class="coverage-wide"><span>03</span><h3>Failure reports with receipts</h3><p>Source snapshots, sanitized logs, official documentation, reproducible checks, and fixes that survive outside a demo.</p></article>
  </div>
</section>
<section class="dossier-index archive-note">
  <div class="index-heading"><div><p class="overline">Earlier evidence series</p><h2>Document workflow archive</h2></div><p>The original source-audit articles stay live for readers who need them. They no longer define the homepage or the publication's direction.</p></div>
  <div class="dossier-list">{archive_cards}</div>
  <a class="archive-link" href="{site_url('/posts/')}">Browse every investigation and field note</a>
</section>
<section class="method-strip">
  <a href="{featured_url}">Start with the lead case</a>
  <a href="{site_url('/posts/')}">Browse the archive</a>
  <a href="{site_url('/editorial-policy/')}">Audit the method</a>
</section>'''
write_page(DIST, layout('AI Agent Tests, Model Access and Failure Analysis',home, noindex=False if public_posts else True, desc='Independent tests of AI agents, model access, reasoning modes, provider limits, and the fixes that work in real workflows.', path='/', social_image_path='/assets/social/agent-field-notes-og.png'))
posts_body='<section class="archive-head"><p class="overline">Public index</p><h1>Investigations and field notes</h1><p>Code-level agent failures, model-access checks, and the earlier source-audit archive.</p></section><div class="dossier-list">'+cards+'</div>'
write_page(DIST/'posts', layout('AI Agent Investigations and Field Notes',posts_body, noindex=False if public_posts else True, desc=f'{len(public_posts)} evidence-led investigations into AI agents, model access, runtime behavior, and workflow failures.', path='/posts/'))
if public_posts:
    robots='User-agent: *\nAllow: /\nSitemap: ' + absolute_url('/sitemap.xml') + '\n# Public build with only QA-approved URLs in sitemap.\n'
else:
    robots='User-agent: *\nDisallow: /\n# Evidence-needed staging build. Do not rely on robots.txt as noindex or security.\n'
(DIST/'robots.txt').write_text(robots,encoding='utf-8')
sitemap_paths=['/']
sitemap_paths += ['/' + p['slug'] + '/' for p in sorted(public_posts, key=lambda x:x['order'])]
sitemap_paths += ['/notebooklm-chatgpt-pdf-study-evidence/','/templates/']
seen_sitemap=[]
for sp in sitemap_paths:
    if sp not in seen_sitemap:
        seen_sitemap.append(sp)
sitemap_urls=''.join(f'<url><loc>{html.escape(absolute_url(sp))}</loc></url>' for sp in seen_sitemap)
(DIST/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap_urls}</urlset>\n',encoding='utf-8')
print(f'Built {len(posts)} posts into {DIST}')
