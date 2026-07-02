#!/usr/bin/env python3
from pathlib import Path
import sys,re
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
issues=[]
required=['index.html','posts/index.html','robots.txt','assets/style.css','editorial-policy/index.html','affiliate-disclosure/index.html','templates/index.html']
for r in required:
    if not (DIST/r).exists(): issues.append(f'missing {r}')
for slug in ['creator-automation-stack-for-beginners','make-vs-zapier-for-creators','beehiiv-vs-kit-convertkit-for-solo-creators','notebooklm-vs-chatgpt-for-studying-pdfs']:
    p=DIST/slug/'index.html'
    if not p.exists(): issues.append(f'missing post {slug}')
    else:
        text=p.read_text(encoding='utf-8',errors='ignore')
        if 'Evidence checks are still required' not in text: issues.append(f'missing evidence warning {slug}')
        if 'noindex' not in text: issues.append(f'missing noindex meta {slug}')
robots=(DIST/'robots.txt').read_text(encoding='utf-8',errors='ignore') if (DIST/'robots.txt').exists() else ''
if 'Disallow: /' not in robots: issues.append('robots not blocking staging site')
print('Static site QA')
if issues:
    for i in issues: print('-',i)
    sys.exit(1)
print('OK')
