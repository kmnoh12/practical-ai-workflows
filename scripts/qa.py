#!/usr/bin/env python3
from pathlib import Path
import sys, re, json
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
MANIFEST=json.loads((ROOT/'site-manifest.json').read_text(encoding='utf-8')) if (ROOT/'site-manifest.json').exists() else {}
BASE_PATH=str(MANIFEST.get('base_path','')).rstrip('/')
issues=[]
required=['index.html','posts/index.html','robots.txt','assets/style.css','editorial-policy/index.html','affiliate-disclosure/index.html','templates/index.html']
for r in required:
    if not (DIST/r).exists(): issues.append(f'missing {r}')
for slug in ['creator-automation-stack-for-beginners','make-vs-zapier-for-creators','beehiiv-vs-kit-convertkit-for-solo-creators','notebooklm-vs-chatgpt-for-studying-pdfs']:
    p=DIST/slug/'index.html'
    if not p.exists():
        issues.append(f'missing post {slug}')
        continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    if 'Evidence checks are still required' not in text: issues.append(f'missing evidence warning {slug}')
    if 'day-12-evidence-gated' not in text: issues.append(f'missing day-12 status {slug}')
    if 'noindex' not in text: issues.append(f'missing noindex meta {slug}')
    if 'Official source touchpoints' not in text: issues.append(f'missing source touchpoints section {slug}')
robots=(DIST/'robots.txt').read_text(encoding='utf-8',errors='ignore') if (DIST/'robots.txt').exists() else ''
if 'Disallow: /' not in robots: issues.append('robots not blocking staging site')
index=(DIST/'index.html').read_text(encoding='utf-8',errors='ignore') if (DIST/'index.html').exists() else ''
expected_css=(BASE_PATH + '/assets/style.css') if BASE_PATH else '/assets/style.css'
if expected_css not in index: issues.append(f'homepage missing expected css link {expected_css}')
if BASE_PATH and 'href="/assets/style.css"' in index: issues.append('homepage still uses root asset path')
if BASE_PATH and f'href="{BASE_PATH}/posts/"' not in index: issues.append('homepage missing base-path posts nav')
print('Static site QA')
if issues:
    for i in issues: print('-',i)
    sys.exit(1)
print('OK')
