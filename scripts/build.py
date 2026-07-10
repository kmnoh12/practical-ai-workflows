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

def md_inline(s):
    s=html.escape(s)
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

def layout(title, body, noindex=False, desc='Tested AI workflows for source-based learning and creator automation.', path='/', page_type='website', social_image_path='/assets/social/practical-ai-workflows-og.png', social_image_alt='Source map, claim check, retrieval practice, and repair workflow'):
    robots='<meta name="robots" content="noindex,nofollow">' if noindex else '<meta name="robots" content="index,follow">'
    page_url=absolute_url(path)
    canonical=f'<link rel="canonical" href="{html.escape(page_url)}">'
    social_image=absolute_url(social_image_path)
    social_meta=(
        f'<meta property="og:type" content="{html.escape(page_type)}">'
        f'<meta property="og:site_name" content="{SITE_TITLE}">'
        f'<meta property="og:title" content="{html.escape(title)}">'
        f'<meta property="og:description" content="{html.escape(desc)}">'
        f'<meta property="og:url" content="{html.escape(page_url)}">'
        f'<meta property="og:image" content="{html.escape(social_image)}">'
        f'<meta property="og:image:width" content="1200">'
        f'<meta property="og:image:height" content="630">'
        f'<meta property="og:image:alt" content="{html.escape(social_image_alt)}">'
        f'<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{html.escape(title)}">'
        f'<meta name="twitter:description" content="{html.escape(desc)}">'
        f'<meta name="twitter:image" content="{html.escape(social_image)}">'
        f'<meta name="twitter:image:alt" content="{html.escape(social_image_alt)}">'
    )
    ga4_id=str(MANIFEST.get('ga4_measurement_id','')).strip()
    ga4=''
    if ga4_id:
        ga4=f'''<script async src="https://www.googletagmanager.com/gtag/js?id={html.escape(ga4_id)}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{html.escape(ga4_id)}');document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var href=a.getAttribute('href')||'';var eventName='link_click';if(href.includes('/downloads/'))eventName='template_download_click';else if(href.includes('/evidence/'))eventName='evidence_asset_click';else if(/^https?:/.test(href)&&!href.includes(location.hostname))eventName='outbound_official_tool_click';if(window.gtag)gtag('event',eventName,{{link_url:a.href,link_text:(a.innerText||'').slice(0,80)}});}});</script>'''
    gsc=str(MANIFEST.get('google_site_verification','')).strip()
    gsc_meta=f'<meta name="google-site-verification" content="{html.escape(gsc)}">' if gsc else ''
    adsense_pub=str(MANIFEST.get('adsense_publisher_id','')).strip()
    adsense=''
    if adsense_pub:
        adsense=f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={html.escape(adsense_pub)}" crossorigin="anonymous"></script>'
    nav=f'<div class="nav wrap"><a class="brand" href="{site_url("/")}">Practical AI Workflows</a><div class="links"><a href="{site_url("/posts/")}">Posts</a><a href="{site_url("/templates/")}">Templates</a><a href="{site_url("/notebooklm-chatgpt-pdf-study-evidence/")}">Evidence</a><a href="{site_url("/about/")}">About</a><a href="{site_url("/editorial-policy/")}">Method</a></div></div>'
    motion_js=f'''<script>document.documentElement.classList.add('js');if(!matchMedia('(prefers-reduced-motion: reduce)').matches){{document.addEventListener('DOMContentLoaded',function(){{var els=document.querySelectorAll('.evidence-spread,.spread-note,.dossier-index,.dossier-link,.workflow-rail,.workflow-step,.method-strip a,.evidence-ledger div');var io=new IntersectionObserver(function(entries){{entries.forEach(function(entry){{if(entry.isIntersecting){{entry.target.classList.add('is-visible');io.unobserve(entry.target);}}}});}},{{threshold:.14,rootMargin:'0px 0px -8% 0px'}});els.forEach(function(el,i){{el.style.setProperty('--stagger',Math.min(i,8));io.observe(el);}});}});}}</script>'''
    footer=f'''<footer class="footer wrap"><p>Practical AI Workflows publishes small, inspectable workflow tests.</p><nav aria-label="Footer"><a href="{site_url('/about/')}">About</a><a href="{site_url('/editorial-policy/')}">Editorial policy</a><a href="{site_url('/privacy-policy/')}">Privacy</a><a href="{site_url('/affiliate-disclosure/')}">Disclosure</a><a href="{site_url('/contact/')}">Contact</a></nav><p>© 2026 Practical AI Workflows.</p></footer>'''
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} - {SITE_TITLE}</title><meta name="description" content="{html.escape(desc)}">{robots}{canonical}{social_meta}{gsc_meta}{ga4}{adsense}<link rel="stylesheet" href="{site_url("/assets/style.css")}"></head><body>{nav}<main class="wrap">{body}</main>{footer}{motion_js}</body></html>'

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
    body=f'<article class="post"><p class="pill">{html.escape(str(fm.get("category","Workflow")))}</p><h1>{html.escape(str(title))}</h1>'
    if not public:
        body+=f'<div class="warn"><strong>Status:</strong> {html.escape(str(fm.get("status","draft")))}. Evidence checks are still required before public recommendation.</div>'
    body+=md_to_html(md)+'</article>'
    noindex=not public
    public_path='/' + str(slug).strip('/') + '/'
    desc=str(fm.get('description','')).strip() or 'A tested, source-grounded AI study workflow with copyable prompts, visible evidence, and clear limits.'
    social_image_path=str(fm.get('social_image','')).strip() or '/assets/social/practical-ai-workflows-og.png'
    social_image_alt=str(fm.get('social_image_alt','')).strip() or 'Source map, claim check, retrieval practice, and repair workflow'
    write_page(DIST/str(slug), layout(str(title), body, noindex, desc=desc, path=public_path, page_type='article', social_image_path=social_image_path, social_image_alt=social_image_alt))
    posts.append({'slug':str(slug),'title':str(title),'category':str(fm.get('category','Workflow')),'order':int(fm.get('order',99)),'status':str(fm.get('status','draft')),'noindex':noindex,'public':public})
for p in sorted((CONTENT/'pages').glob('*.md')):
    fm,md=parse_fm(p.read_text(encoding='utf-8'))
    slug=reserve_slug(checked_slug(fm.get('slug',p.stem)), seen_slugs); title=fm.get('title',slug.replace('-',' ').title())
    body=f'<article class="post"><h1>{html.escape(str(title))}</h1>{md_to_html(md)}</article>'
    desc=str(fm.get('description','')).strip() or 'Practical templates, evidence, and editorial notes for source-grounded AI study workflows.'
    write_page(DIST/str(slug), layout(str(title), body, fm_bool(fm, 'noindex', False) is True, desc=desc, path='/' + str(slug).strip('/') + '/'))
visible_posts=public_posts if public_posts else posts
cards='\n'.join(f'<a class="dossier-link" href="{site_url("/" + x["slug"] + "/")}"><span>0{i+1}</span><strong>{html.escape(x["title"])}</strong><em>Open workflow</em></a>' for i,x in enumerate(sorted(visible_posts,key=lambda x:x['order'])))
home=f'''<section class="dossier-hero">
  <div class="dossier-copy">
    <p class="lab-label">Practical AI Workflows</p>
    <h1>Stop summarizing PDFs first.</h1>
    <p class="dossier-sub">Map the source in NotebookLM. Turn verified notes into retrieval practice with ChatGPT.</p>
    <div class="hero-actions"><a href="{site_url('/notebooklm-vs-chatgpt-for-studying-pdfs/')}">Read the field test</a><a href="{site_url('/templates/')}">Copy the workflow</a></div>
  </div>
  <aside class="evidence-ledger" aria-label="Evidence ledger">
    <div><span>Scope</span><strong>1 source / 2 tools</strong></div>
    <div><span>Receipts</span><strong>raw outputs + screenshots</strong></div>
    <div><span>Known flaw</span><strong>citation-label artifacts</strong></div>
    <div class="ledger-actions"><a href="{site_url('/notebooklm-chatgpt-pdf-study-evidence/')}">Inspect evidence</a><a href="{site_url('/editorial-policy/')}">Read method</a></div>
  </aside>
</section>
<section class="evidence-spread">
  <figure>
    <img src="{site_url('/assets/evidence/source-map-workflow-english.png')}" alt="English reconstruction of the source map, claim check, retrieval practice, and repair workflow" width="1568" height="948">
    <figcaption>English reconstruction of the recorded workflow. The original Korean UI capture remains in the public evidence pack.</figcaption>
  </figure>
  <div class="spread-note"><h2>The messy capture stays public.</h2><p>The NotebookLM run exposed Korean citation labels and duplicated headings in the exported text. I kept those artifacts instead of polishing the evidence into a cleaner story.</p><a href="{site_url('/notebooklm-chatgpt-pdf-study-evidence/')}">See the raw run</a></div>
</section>
<section class="workflow-rail" aria-labelledby="workflow-heading">
  <div class="workflow-intro"><h2 id="workflow-heading">A workflow you can run today.</h2><p>Four passes. Each one has a job, an output, and a failure check.</p></div>
  <div class="workflow-steps">
    <div class="workflow-step"><span>01</span><h3>Map</h3><p>List sections, concepts, and source cues before asking for prose.</p></div>
    <div class="workflow-step"><span>02</span><h3>Verify</h3><p>Separate source facts from explanations, examples, and open questions.</p></div>
    <div class="workflow-step"><span>03</span><h3>Practice</h3><p>Generate closed-book questions only from the notes you checked.</p></div>
    <div class="workflow-step"><span>04</span><h3>Repair</h3><p>Turn missed questions into a short retest plan instead of another summary.</p></div>
  </div>
</section>
<section class="dossier-index">
  <div class="index-heading"><h2>Public dossier</h2><p>Start with the comparison. Continue with the source map, study-guide audit, and answer-key columns when you need the exact checking workflow.</p></div>
  <div class="dossier-list">{cards}</div>
</section>
<section class="method-strip">
  <a href="{site_url('/templates/')}">Copy the templates</a>
  <a href="{site_url('/notebooklm-chatgpt-pdf-study-evidence/')}">Inspect raw files</a>
  <a href="{site_url('/editorial-policy/')}">Read the method</a>
</section>'''
write_page(DIST, layout('Source-Grounded PDF Study Workflows',home, noindex=False if public_posts else True, desc='A tested NotebookLM and ChatGPT workflow for source maps, claim checks, retrieval practice, and missed-question repair.', path='/'))
write_page(DIST/'posts', layout('Tested PDF Study Workflows','<h1>Tested PDF study workflows</h1><div class="dossier-list">'+cards+'</div>', noindex=False if public_posts else True, desc=f'{len(public_posts)} source-grounded PDF study workflows and columns with prompts, evidence, limits, and free templates.', path='/posts/'))
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
