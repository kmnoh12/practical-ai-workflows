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

def layout(title, body, noindex=False, desc='Tested AI workflows for source-based learning and creator automation.', path='/'):
    robots='<meta name="robots" content="noindex,nofollow">' if noindex else '<meta name="robots" content="index,follow">'
    canonical=f'<link rel="canonical" href="{html.escape(absolute_url(path))}">'
    ga4_id=str(MANIFEST.get('ga4_measurement_id','')).strip()
    ga4=''
    if ga4_id:
        ga4=f'''<script async src="https://www.googletagmanager.com/gtag/js?id={html.escape(ga4_id)}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{html.escape(ga4_id)}');document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var href=a.getAttribute('href')||'';var eventName='link_click';if(href.includes('/downloads/'))eventName='template_download_click';else if(href.includes('/evidence/'))eventName='evidence_asset_click';else if(/^https?:/.test(href)&&!href.includes(location.hostname))eventName='outbound_official_tool_click';if(window.gtag)gtag('event',eventName,{{link_url:a.href,link_text:(a.innerText||'').slice(0,80)}});}});</script>'''
    gsc=str(MANIFEST.get('google_site_verification','')).strip()
    gsc_meta=f'<meta name="google-site-verification" content="{html.escape(gsc)}">' if gsc else ''
    nav=f'<div class="nav wrap"><a class="brand" href="{site_url("/")}">Practical AI Workflows</a><div class="links"><a href="{site_url("/posts/")}">Posts</a><a href="{site_url("/templates/")}">Templates</a><a href="{site_url("/editorial-policy/")}">Methodology</a><a href="{site_url("/affiliate-disclosure/")}">Disclosure</a></div></div>'
    motion_js=f'''<script>document.documentElement.classList.add('js');if(!matchMedia('(prefers-reduced-motion: reduce)').matches){{document.addEventListener('DOMContentLoaded',function(){{var els=document.querySelectorAll('.evidence-spread,.spread-note,.dossier-index,.dossier-link,.method-strip a,.evidence-ledger div');var io=new IntersectionObserver(function(entries){{entries.forEach(function(entry){{if(entry.isIntersecting){{entry.target.classList.add('is-visible');io.unobserve(entry.target);}}}});}},{{threshold:.14,rootMargin:'0px 0px -8% 0px'}});els.forEach(function(el,i){{el.style.setProperty('--stagger',Math.min(i,8));io.observe(el);}});}});}}</script>'''
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} - {SITE_TITLE}</title><meta name="description" content="{html.escape(desc)}">{robots}{canonical}{gsc_meta}{ga4}<link rel="stylesheet" href="{site_url("/assets/style.css")}"></head><body>{nav}<main class="wrap">{body}</main><footer class="footer wrap">© 2026 Practical AI Workflows. Source-grounded workflow testing with screenshots, templates, and failure notes. Affiliate links, if used, are disclosed.</footer>{motion_js}</body></html>'

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
    write_page(DIST/str(slug), layout(str(title), body, noindex, path=public_path))
    posts.append({'slug':str(slug),'title':str(title),'category':str(fm.get('category','Workflow')),'order':int(fm.get('order',99)),'status':str(fm.get('status','draft')),'noindex':noindex,'public':public})
for p in sorted((CONTENT/'pages').glob('*.md')):
    fm,md=parse_fm(p.read_text(encoding='utf-8'))
    slug=reserve_slug(checked_slug(fm.get('slug',p.stem)), seen_slugs); title=fm.get('title',slug.replace('-',' ').title())
    body=f'<article class="post"><h1>{html.escape(str(title))}</h1>{md_to_html(md)}</article>'
    write_page(DIST/str(slug), layout(str(title), body, fm_bool(fm, 'noindex', False) is True, path='/' + str(slug).strip('/') + '/'))
visible_posts=public_posts if public_posts else posts
cards='\n'.join(f'<a class="dossier-link" href="{site_url("/" + x["slug"] + "/")}"><span>0{i+1}</span><strong>{html.escape(x["title"])}</strong><em>Open workflow</em></a>' for i,x in enumerate(sorted(visible_posts,key=lambda x:x['order'])))
home=f'''<section class="dossier-hero">
  <div class="dossier-copy">
    <p class="lab-label">Practical AI Workflows</p>
    <h1>PDF study workflows with receipts.</h1>
    <p class="dossier-sub">NotebookLM for source trails. ChatGPT for retrieval practice. Every public claim links back to prompts, screenshots, outputs, and failure logs.</p>
  </div>
  <aside class="evidence-ledger" aria-label="Evidence ledger">
    <div><span>Scope</span><strong>3 public workflows</strong></div>
    <div><span>Evidence</span><strong>screenshots, outputs, scoring</strong></div>
    <div><span>Excluded</span><strong>generic AI tool lists</strong></div>
    <div class="ledger-actions"><a href="{site_url('/notebooklm-vs-chatgpt-for-studying-pdfs/')}">Read test</a><a href="{site_url('/notebooklm-chatgpt-pdf-study-evidence/')}">Evidence pack</a></div>
  </aside>
</section>
<section class="evidence-spread">
  <figure>
    <img src="{site_url('/assets/evidence/03_notebooklm_answer_visible.png')}" alt="NotebookLM source-grounded answer from the PDF study workflow test">
  </figure>
  <div class="spread-note"><h2>Not another AI tools roundup.</h2><p>The site now ships as a small research file: one source, one prompt, two tools, visible artifacts. Weak launch-cluster pages stay out of the sitemap until tested.</p></div>
</section>
<section class="dossier-index">
  <div class="index-heading"><h2>Public dossier</h2><p>Start with the comparison, then use the source-map and active-recall workflows.</p></div>
  <div class="dossier-list">{cards}</div>
</section>
<section class="method-strip">
  <a href="{site_url('/templates/')}">Copy the templates</a>
  <a href="{site_url('/notebooklm-chatgpt-pdf-study-evidence/')}">Inspect raw files</a>
  <a href="{site_url('/editorial-policy/')}">Read methodology</a>
</section>'''
write_page(DIST, layout('Home',home, noindex=False if public_posts else True, path='/'))
write_page(DIST/'posts', layout('Posts','<h1>Posts</h1><div class="dossier-list">'+cards+'</div>', noindex=False if public_posts else True, path='/posts/'))
if public_posts:
    robots='User-agent: *\nAllow: /\nSitemap: ' + absolute_url('/sitemap.xml') + '\n# Public build with only QA-approved URLs in sitemap.\n'
else:
    robots='User-agent: *\nDisallow: /\n# Evidence-needed staging build. Do not rely on robots.txt as noindex or security.\n'
(DIST/'robots.txt').write_text(robots,encoding='utf-8')
sitemap_urls=''.join(f'<url><loc>{html.escape(absolute_url("/" + p["slug"] + "/"))}</loc></url>' for p in public_posts)
(DIST/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap_urls}</urlset>\n',encoding='utf-8')
print(f'Built {len(posts)} posts into {DIST}')
