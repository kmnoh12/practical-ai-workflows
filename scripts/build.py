#!/usr/bin/env python3
from pathlib import Path
import re, html, shutil
ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'content'
DIST=ROOT/'dist'
SITE_TITLE='Practical AI Workflows'

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

def md_inline(s):
    s=html.escape(s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
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

def layout(title, body, noindex=False, desc='Tested AI workflows for source-based learning and creator automation.'):
    robots='<meta name="robots" content="noindex,nofollow">' if noindex else ''
    nav='<div class="nav wrap"><a class="brand" href="/">Practical AI Workflows</a><div class="links"><a href="/posts/">Posts</a><a href="/templates/">Templates</a><a href="/editorial-policy/">Methodology</a><a href="/affiliate-disclosure/">Disclosure</a></div></div>'
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} - {SITE_TITLE}</title><meta name="description" content="{html.escape(desc)}">{robots}<link rel="stylesheet" href="/assets/style.css"></head><body>{nav}<main class="wrap">{body}</main><footer class="footer wrap">© 2026 Practical AI Workflows. Some links may be paid links. Evidence-backed workflow testing, not generic tool lists.</footer></body></html>'

def write_page(path, html_text):
    path.mkdir(parents=True,exist_ok=True)
    (path/'index.html').write_text(html_text,encoding='utf-8')

if DIST.exists(): shutil.rmtree(DIST)
DIST.mkdir(parents=True)
shutil.copytree(ROOT/'public', DIST, dirs_exist_ok=True)
posts=[]
for p in sorted((CONTENT/'posts').glob('*.md')):
    fm,md=parse_fm(p.read_text(encoding='utf-8'))
    slug=fm.get('slug',p.stem); title=fm.get('title',slug.replace('-',' ').title())
    body=f'<article class="post"><p class="pill">{html.escape(str(fm.get("category","Workflow")))}</p><h1>{html.escape(str(title))}</h1>'
    if fm.get('status')!='published':
        body+=f'<div class="warn"><strong>Status:</strong> {html.escape(str(fm.get("status","draft")))}. Evidence checks are still required before public recommendation.</div>'
    body+=md_to_html(md)+'</article>'
    write_page(DIST/str(slug), layout(str(title), body, bool(fm.get('noindex',False))))
    posts.append({'slug':str(slug),'title':str(title),'category':str(fm.get('category','Workflow')),'order':int(fm.get('order',99)),'status':str(fm.get('status','draft'))})
for p in sorted((CONTENT/'pages').glob('*.md')):
    fm,md=parse_fm(p.read_text(encoding='utf-8'))
    slug=fm.get('slug',p.stem); title=fm.get('title',slug.replace('-',' ').title())
    body=f'<article class="post"><h1>{html.escape(str(title))}</h1>{md_to_html(md)}</article>'
    write_page(DIST/str(slug), layout(str(title), body, bool(fm.get('noindex',False))))
cards='\n'.join(f'<div class="card"><p class="pill">{html.escape(x["category"])}</p><h3><a href="/{x["slug"]}/">{html.escape(x["title"])}</a></h3><p class="muted">Status: <span class="status">{html.escape(x["status"])}</span></p></div>' for x in sorted(posts,key=lambda x:x['order']))
home=f'<section class="hero"><p class="pill">Evidence-backed workflow lab</p><h1>Tested AI workflows for source-based learning and creator automation.</h1><p>Practical AI Workflows turns PDFs, notes, newsletters, checkout tools, and creator automations into repeatable systems with evidence plans, templates, and decision tables.</p></section><section><h2>Launch cluster</h2><div class="grid">{cards}</div></section><section><h2>Start with templates</h2><div class="grid"><div class="card"><h3>Creator Automation Stack Checklist</h3><p>Map landing page, email, checkout, automation, and content workflow before buying more tools.</p></div><div class="card"><h3>PDF-to-Study-Guide Workflow Checklist</h3><p>Use source-grounded notes and AI explanations without losing verification.</p></div><div class="card"><h3>AI Content Brief Template</h3><p>Define intent, evidence, screenshots, links, and publish gates before drafting.</p></div></div></section>'
write_page(DIST, layout('Home',home))
write_page(DIST/'posts', layout('Posts','<h1>Posts</h1><div class="grid">'+cards+'</div>'))
(DIST/'robots.txt').write_text('User-agent: *\nDisallow: /\n# Evidence-needed staging build. Remove Disallow after FACT CHECK cleanup.\n',encoding='utf-8')
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>\n',encoding='utf-8')
print(f'Built {len(posts)} posts into {DIST}')
