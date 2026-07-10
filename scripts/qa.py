#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
import sys, re, json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content'
DIST = ROOT / 'dist'
MANIFEST = json.loads((ROOT / 'site-manifest.json').read_text(encoding='utf-8')) if (ROOT / 'site-manifest.json').exists() else {}
BASE_PATH = str(MANIFEST.get('base_path', '')).rstrip('/')
PUBLIC_BASE_URL = str(MANIFEST.get('public_base_url', '')).rstrip('/')
issues = []
warnings = []

SLUG_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
GA4_RE = re.compile(r'^G-[A-Z0-9]+$')
BLOCKED_MARKERS = ['FACT CHECK', 'TODO', 'needs evidence', 'VERIFY']
PUBLIC_PLACEHOLDERS = [
    'Missing',
    'Not captured',
    'Results are not filled yet',
    'Do not pick a winner yet',
    'Placeholder result table',
    'Current status',
]
NOTEBOOKLM_POST_SLUG = 'notebooklm-vs-chatgpt-for-studying-pdfs'
NOTEBOOKLM_EVIDENCE_DIR = ROOT / 'automation-lab-archive' / 'docs' / 'day-13-notebooklm-evidence-pack-files'
NOTEBOOKLM_REQUIRED_PUBLIC_EVIDENCE = [
    'same-source-study-notes.md',
    'same-source-study-notes.pdf',
    'same-source-prompt.txt',
    'evaluation-rubric.md',
    'notebooklm-output.md',
    'chatgpt-output.md',
    'scoring-sheet.csv',
]
REQUIRED_DIST = [
    'index.html',
    'posts/index.html',
    'robots.txt',
    'sitemap.xml',
    'ads.txt',
    'assets/style.css',
    'assets/social/practical-ai-workflows-og.png',
    'assets/evidence/source-map-workflow-english.png',
    'editorial-policy/index.html',
    'affiliate-disclosure/index.html',
    'templates/index.html',
]
REQUIRED_POST_MARKERS_FOR_PUBLIC = [
    '## Tested with',
    '## What this is based on',
    '## Bottom line',
]


def parse_fm(text):
    data = {}
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    v = v.strip().strip('"')
                    if v.lower() == 'true':
                        v = True
                    elif v.lower() == 'false':
                        v = False
                    data[k.strip()] = v
            return data, parts[2].lstrip()
    return data, text


def fm_bool(fm, key, default=None, context='frontmatter'):
    if key not in fm:
        return default
    v = fm[key]
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        s = v.strip().lower()
        if s == 'true':
            return True
        if s == 'false':
            return False
    issues.append(f'{context}: invalid boolean frontmatter {key}={v!r}; only true/false are allowed')
    return default


def manifest_bool(key, default=False):
    return fm_bool(MANIFEST, key, default, 'site-manifest.json')


def is_public_candidate(fm, context='frontmatter'):
    return (
        str(fm.get('status', 'draft')) == 'published'
        and fm_bool(fm, 'indexable', False, context) is True
        and fm_bool(fm, 'qa_approved', False, context) is True
        and fm_bool(fm, 'noindex', True, context) is False
    )


def site_path(path='/'):
    path = '/' + str(path).lstrip('/')
    return (BASE_PATH + path) if BASE_PATH else path


def absolute_url(path='/'):
    path = '/' + str(path).lstrip('/')
    return PUBLIC_BASE_URL + path if PUBLIC_BASE_URL else site_path(path)


def canonical_href(html):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    return m.group(1) if m else ''


def sitemap_locs(xml_text):
    if not xml_text.strip():
        return set()
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        issues.append(f'sitemap.xml is invalid XML: {exc}')
        return set()
    locs = set()
    for elem in root.iter():
        if elem.tag.endswith('loc') and elem.text:
            locs.add(elem.text.strip())
    return locs


def href_attrs(html):
    links = []
    for m in re.finditer(r'<a\b([^>]*)>', html, flags=re.I):
        attrs = m.group(1)
        href_m = re.search(r'href=["\']([^"\']+)["\']', attrs, flags=re.I)
        if href_m:
            rel_m = re.search(r'rel=["\']([^"\']+)["\']', attrs, flags=re.I)
            links.append({'href': href_m.group(1), 'rel': rel_m.group(1) if rel_m else '', 'tag': m.group(0)})
    return links


def hrefs(html):
    return {x['href'] for x in href_attrs(html)}


def slug_is_valid(slug):
    return '/' not in slug and '\\' not in slug and '..' not in slug and SLUG_RE.fullmatch(slug)


for r in REQUIRED_DIST:
    if not (DIST / r).exists():
        issues.append(f'missing dist asset: {r}')

if BASE_PATH and manifest_bool('robots_at_host_root', False) is not True:
    warnings.append('base_path build: dist/robots.txt may not live at host root; do not rely on robots.txt for indexing control')

content_items = []
for kind, folder in [('post', CONTENT / 'posts'), ('page', CONTENT / 'pages')]:
    for source in sorted(folder.glob('*.md')):
        raw = source.read_text(encoding='utf-8')
        fm, body = parse_fm(raw)
        slug = str(fm.get('slug', source.stem)).strip()
        content_items.append({'kind': kind, 'source': source, 'raw': raw, 'fm': fm, 'body': body, 'slug': slug})

seen_slugs = {}
for item in content_items:
    slug = item['slug']
    label = f'{item["kind"]}:{item["source"].name}'
    if not slug_is_valid(slug):
        issues.append(f'{label}: invalid slug {slug!r}; use lowercase words separated by single hyphens')
    elif slug in seen_slugs:
        issues.append(f'{label}: duplicate slug {slug!r} also used by {seen_slugs[slug]}')
    else:
        seen_slugs[slug] = label

post_infos = []
public_posts = []
for item in [x for x in content_items if x['kind'] == 'post']:
    fm = item['fm']
    body = item['body']
    raw = item['raw']
    slug = item['slug']
    source = item['source']
    status = str(fm.get('status', 'draft'))
    title = str(fm.get('title', '')).strip()
    public = is_public_candidate(fm, f'{slug or source.name}')
    html_path = DIST / slug / 'index.html' if slug_is_valid(slug) else None
    html = html_path.read_text(encoding='utf-8', errors='ignore') if html_path and html_path.exists() else ''
    info = {'slug': slug, 'source': source, 'fm': fm, 'html': html, 'body': body, 'public': public}
    post_infos.append(info)

    if not title:
        issues.append(f'{slug}: missing title frontmatter')
    if html_path and not html_path.exists():
        issues.append(f'{slug}: missing built html')
        continue

    unresolved_markers = [marker for marker in BLOCKED_MARKERS if marker in raw]

    if '<link rel="canonical"' not in html:
        issues.append(f'{slug}: missing canonical link')
    if '<meta name="description"' not in html:
        issues.append(f'{slug}: missing meta description')

    if status == 'published' and not public:
        issues.append(f'{slug}: status published is not public unless indexable:true, qa_approved:true, and noindex:false are all explicit')
        if fm_bool(fm, 'indexable', False, slug) is not True:
            issues.append(f'{slug}: published post requires indexable: true')
        if fm_bool(fm, 'qa_approved', False, slug) is not True:
            issues.append(f'{slug}: published post requires qa_approved: true')
        if fm_bool(fm, 'noindex', True, slug) is not False:
            issues.append(f'{slug}: published post requires noindex: false')

    if public:
        public_posts.append(info)
        href = canonical_href(html)
        expected = absolute_url('/' + slug + '/')
        if not PUBLIC_BASE_URL.startswith('https://'):
            issues.append(f'{slug}: public candidate requires https public_base_url in site-manifest.json')
        if not href.startswith('https://'):
            issues.append(f'{slug}: public candidate canonical must be absolute https URL, got: {href}')
        if href != expected:
            issues.append(f'{slug}: canonical expected URL mismatch: canonical={href}, expected={expected}')
        for marker in unresolved_markers:
            issues.append(f'{slug}: public candidate has unresolved marker: {marker}')
        for phrase in PUBLIC_PLACEHOLDERS:
            if phrase in body:
                issues.append(f'{slug}: public candidate still contains placeholder phrase: {phrase}')
        if 'content="index,follow"' not in html:
            issues.append(f'{slug}: public candidate missing index,follow robots meta')
        for marker in REQUIRED_POST_MARKERS_FOR_PUBLIC:
            if marker not in body:
                issues.append(f'{slug}: public candidate missing required marker: {marker}')
        if not re.search(r'^## Copy ', body, flags=re.M):
            issues.append(f'{slug}: public candidate missing a direct copy/download section')
        if not re.search(r'^## (Limits|What this test does not prove)$', body, flags=re.M):
            issues.append(f'{slug}: public candidate missing a plainly labeled limits section')
        if not re.search(r'\]\([^\)\n]*(?:evidence|downloads)[^\)\n]*\)', body, flags=re.I):
            issues.append(f'{slug}: public candidate missing a linked evidence or download artifact')
        evidence_hits = sum(token in body for token in ['Sources:', 'official', 'NotebookLM', 'OpenAI', 'Make', 'Zapier'])
        if evidence_hits < 1:
            issues.append(f'{slug}: public candidate has insufficient source/evidence mentions')
        if slug == NOTEBOOKLM_POST_SLUG:
            for rel in NOTEBOOKLM_REQUIRED_PUBLIC_EVIDENCE:
                if not (NOTEBOOKLM_EVIDENCE_DIR / rel).exists():
                    issues.append(f'{slug}: missing required evidence file: docs/day-13-notebooklm-evidence-pack-files/{rel}')
    else:
        for marker in unresolved_markers:
            warnings.append(f'{slug}: non-public source still contains marker: {marker}')
        if 'content="noindex,nofollow"' not in html:
            issues.append(f'{slug}: non-public post missing noindex,nofollow robots meta')
        if 'Evidence checks are still required' not in html:
            issues.append(f'{slug}: non-public post missing evidence warning')

robots = (DIST / 'robots.txt').read_text(encoding='utf-8', errors='ignore') if (DIST / 'robots.txt').exists() else ''
sitemap = (DIST / 'sitemap.xml').read_text(encoding='utf-8', errors='ignore') if (DIST / 'sitemap.xml').exists() else ''
ads_txt = (DIST / 'ads.txt').read_text(encoding='utf-8', errors='ignore').strip() if (DIST / 'ads.txt').exists() else ''
expected_ads_txt = 'google.com, pub-4624913344767889, DIRECT, f08c47fec0942fa0'
index = (DIST / 'index.html').read_text(encoding='utf-8', errors='ignore') if (DIST / 'index.html').exists() else ''
posts_index = (DIST / 'posts' / 'index.html').read_text(encoding='utf-8', errors='ignore') if (DIST / 'posts' / 'index.html').exists() else ''
expected_css = site_path('/assets/style.css')
if ads_txt != expected_ads_txt:
    issues.append('ads.txt missing or does not match the configured Google AdSense publisher record')
if expected_css not in index:
    issues.append(f'homepage missing expected css link {expected_css}')
for marker in [
    '<meta property="og:title"',
    '<meta property="og:description"',
    '<meta property="og:image"',
    '<meta name="twitter:card" content="summary_large_image">',
    absolute_url('/assets/social/practical-ai-workflows-og.png'),
]:
    if marker not in index:
        issues.append(f'homepage missing social preview marker: {marker}')
if 'assets/evidence/source-map-workflow-english.png' not in index:
    issues.append('homepage missing English workflow reconstruction asset')
if 'width="1568" height="948"' not in index:
    issues.append('homepage evidence image must reserve intrinsic dimensions to avoid layout shift')
if BASE_PATH and 'href="/assets/style.css"' in index:
    issues.append('homepage still uses root asset path')
if BASE_PATH and f'href="{BASE_PATH}/posts/"' not in index:
    issues.append('homepage missing base-path posts nav')

locs = sitemap_locs(sitemap)
expected_public_urls = {absolute_url('/' + post['slug'] + '/') for post in public_posts}
public_build = bool(public_posts)

if public_build:
    # Keep the public set deliberately small and evidence-led. The original
    # three pillars may expand into a tightly related source-audit column
    # series, but weak launch-cluster drafts must remain noindex.
    if len(public_posts) < 3:
        issues.append(f'public evidence gate expects at least three indexable posts, found {len(public_posts)}')
    if len(public_posts) > 8:
        issues.append(f'public evidence gate expects no more than eight indexable posts, found {len(public_posts)}')
    if not PUBLIC_BASE_URL.startswith('https://'):
        issues.append('public build requires https public_base_url in site-manifest.json')
    if manifest_bool('robots_at_host_root', False) is not True:
        issues.append('public build requires robots_at_host_root: true before relying on robots.txt')
    if 'Disallow: /' in robots:
        issues.append('robots blocks all despite public indexable posts')
    if 'Allow: /' not in robots:
        issues.append('public robots.txt must contain Allow: /')
    expected_sitemap_line = 'Sitemap: ' + absolute_url('/sitemap.xml')
    if expected_sitemap_line not in robots:
        issues.append(f'public robots.txt missing absolute sitemap line: {expected_sitemap_line}')
    expected_sitemap_urls = set(expected_public_urls)
    expected_sitemap_urls.add(absolute_url('/'))
    expected_sitemap_urls.add(absolute_url('/notebooklm-chatgpt-pdf-study-evidence/'))
    expected_sitemap_urls.add(absolute_url('/templates/'))
    if locs != expected_sitemap_urls:
        issues.append(f'sitemap URL set mismatch: expected {sorted(expected_sitemap_urls)}, got {sorted(locs)}')
    for loc in locs:
        if not loc.startswith('https://'):
            issues.append(f'public sitemap loc must be absolute https URL: {loc}')
    for post in post_infos:
        if not post['public']:
            non_public_url = absolute_url('/' + post['slug'] + '/')
            if non_public_url in locs:
                issues.append(f'sitemap includes non-public post URL: {non_public_url}')
            non_public_href = site_path('/' + post['slug'] + '/')
            if non_public_href in hrefs(index):
                issues.append(f'homepage links non-public post during public build: {post["slug"]}')
            if non_public_href in hrefs(posts_index):
                issues.append(f'/posts/ links non-public post during public build: {post["slug"]}')
else:
    if 'Disallow: /' not in robots:
        issues.append('staging build without public posts must keep robots Disallow: /')
    if locs:
        issues.append(f'sitemap contains URLs while no public posts exist: {sorted(locs)}')
    for html_file in sorted(DIST.glob('**/*.html')):
        html = html_file.read_text(encoding='utf-8', errors='ignore')
        if 'content="noindex,nofollow"' not in html:
            issues.append(f'{html_file.relative_to(DIST)}: staging build page missing noindex,nofollow robots meta')

ga4_id = str(MANIFEST.get('ga4_measurement_id', '')).strip()
if public_build and not GA4_RE.fullmatch(ga4_id):
    issues.append('public build requires valid GA4 measurement ID matching ^G-[A-Z0-9]+$')
if ga4_id:
    for html_file in sorted(DIST.glob('**/*.html')):
        html = html_file.read_text(encoding='utf-8', errors='ignore')
        if html.count('googletagmanager.com/gtag/js?id=') != 1:
            issues.append(f'{html_file.relative_to(DIST)}: GA4 loader count must be exactly 1')
        if len(re.findall(r"gtag\('config'\s*,\s*['\"]" + re.escape(ga4_id) + r"['\"]\)", html)) != 1:
            issues.append(f'{html_file.relative_to(DIST)}: GA4 config count must be exactly 1')

gsc = str(MANIFEST.get('google_site_verification', '')).strip()
if public_build and not gsc:
    issues.append('public build requires google_site_verification before indexing')
if gsc and index.count('google-site-verification') != 1:
    issues.append('homepage must contain exactly one google-site-verification meta tag when configured')

adsense_pub = str(MANIFEST.get('adsense_publisher_id', '')).strip()
if public_build and not re.fullmatch(r'ca-pub-[0-9]+', adsense_pub):
    issues.append('public build requires adsense_publisher_id matching ca-pub-[0-9]+')
if adsense_pub:
    expected_adsense_src = f'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={adsense_pub}'
    for html_file in sorted(DIST.glob('**/*.html')):
        html = html_file.read_text(encoding='utf-8', errors='ignore')
        if html.count(expected_adsense_src) != 1:
            issues.append(f'{html_file.relative_to(DIST)}: AdSense loader count must be exactly 1 for {adsense_pub}')
        if 'crossorigin="anonymous"' not in html:
            issues.append(f'{html_file.relative_to(DIST)}: AdSense loader missing crossorigin="anonymous"')

affiliate_domains = MANIFEST.get('affiliate_domains', [])
if not isinstance(affiliate_domains, list):
    issues.append('site-manifest.json: affiliate_domains must be a list when present')
    affiliate_domains = []
affiliate_domains = {str(x).lower().lstrip('.').strip() for x in affiliate_domains if str(x).strip()}

for post in public_posts:
    for link in href_attrs(post['html']):
        href = link['href'].strip()
        lowered = href.lower()
        if lowered.startswith('javascript:') or lowered.startswith('data:'):
            issues.append(f'{post["slug"]}: public page contains unsafe href: {href}')
        if affiliate_domains:
            host = (urlparse(href).hostname or '').lower().lstrip('.')
            if host and any(host == d or host.endswith('.' + d) for d in affiliate_domains):
                rel_tokens = set(link['rel'].lower().split())
                if not {'sponsored', 'nofollow'}.issubset(rel_tokens):
                    issues.append(f'{post["slug"]}: affiliate link to {host} requires rel="sponsored nofollow"')
                disclosure = (DIST / 'affiliate-disclosure' / 'index.html').read_text(encoding='utf-8', errors='ignore') if (DIST / 'affiliate-disclosure' / 'index.html').exists() else ''
                if 'content="index,follow"' not in disclosure:
                    issues.append(f'{post["slug"]}: affiliate links require an indexable affiliate disclosure page')

print('Static site QA')
if warnings:
    for w in warnings:
        print('warning:', w)
if issues:
    for i in issues:
        print('-', i)
    sys.exit(1)
print('OK')
