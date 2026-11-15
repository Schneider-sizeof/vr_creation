import os
import sys
import re
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
import django
django.setup()

from django.test import Client
from apps.services.models import Service, City
from apps.blog.models import Article
from apps.portfolio.models import Project, CaseStudy
from apps.core.models import Promotion

client = Client()

langs = ['fr', 'en', 'ar']

# Collect all dynamic objects
services = list(Service.objects.filter(is_active=True))
cities = list(City.objects.filter(is_published=True).order_by('order'))
articles = list(Article.objects.filter(is_published=True))
projects = list(Project.objects.all())
case_studies = list(CaseStudy.objects.all())
promotions = list(Promotion.objects.filter(is_active=True))

urls_to_crawl = []

# 1. Root and redirects
urls_to_crawl.append(('/', 'Root redirect'))
urls_to_crawl.append(('/about/', 'Old root about redirect'))
urls_to_crawl.append(('/services/', 'Old root services redirect'))
urls_to_crawl.append(('/portfolio/', 'Old root portfolio redirect'))
urls_to_crawl.append(('/zones-intervention', 'Old root zones-intervention redirect'))
urls_to_crawl.append(('/fr/services/branding-immobilier/', 'Old branding redirect'))
urls_to_crawl.append(('/robots.txt', 'Robots.txt'))
urls_to_crawl.append(('/sitemap.xml', 'XML Sitemap'))

# 2. Main static & list pages across 3 languages
static_paths = [
    '',
    'a-propos/',
    'services/',
    'realisations/',
    'etudes-de-cas/',
    'visites-virtuelles/',
    'blog/',
    'promotions/',
    'contact/',
    'plan-du-site/',
    'mentions-legales/',
    'confidentialite/',
    'cookies/',
    'zones-intervention/',
]

for lang in langs:
    for sp in static_paths:
        urls_to_crawl.append((f'/{lang}/{sp}', f'Static: {sp or "home"} ({lang})'))

# 3. Service details
for s in services:
    for lang in langs:
        urls_to_crawl.append((f'/{lang}/services/{s.slug}/', f'Service: {s.slug} ({lang})'))

# 4. City details
for c in cities:
    for lang in langs:
        urls_to_crawl.append((f'/{lang}/zones-intervention/{c.slug}/', f'City: {c.slug} ({lang})'))

# 5. Articles
for a in articles:
    for lang in langs:
        urls_to_crawl.append((f'/{lang}/blog/{a.slug}/', f'Article: {a.slug} ({lang})'))

# 6. Case Studies
for cs in case_studies:
    for lang in langs:
        urls_to_crawl.append((f'/{lang}/etudes-de-cas/{cs.slug}/', f'Case Study: {cs.slug} ({lang})'))

# 7. Portfolio projects
for p in projects:
    for lang in langs:
        urls_to_crawl.append((f'/{lang}/realisations/{p.slug}/', f'Project: {p.slug} ({lang})'))

# 8. Promotions
for pr in promotions:
    for lang in langs:
        urls_to_crawl.append((f'/{lang}/promotions/{pr.slug}/', f'Promotion: {pr.slug} ({lang})'))

print(f"Total URLs to crawl: {len(urls_to_crawl)}\n")

results = []
issues = []

for url, label in urls_to_crawl:
    resp = client.get(url, HTTP_HOST='vrcreationcompany.com')
    status = resp.status_code

    # Check redirects
    if status in (301, 302):
        location = resp.get('Location', '')
        results.append({
            'url': url,
            'label': label,
            'status': status,
            'redirect': location,
            'title_len': '-',
            'desc_len': '-',
            'h1_count': '-',
            'canonical': '-',
            'hreflang_count': '-',
            'schemas': '-',
            'word_count': '-'
        })
        continue

    # Non-HTML files (robots, sitemap)
    if url in ('/robots.txt', '/sitemap.xml'):
        content = resp.content.decode('utf-8', errors='ignore')
        results.append({
            'url': url,
            'label': label,
            'status': status,
            'redirect': '',
            'title_len': '-',
            'desc_len': '-',
            'h1_count': '-',
            'canonical': '-',
            'hreflang_count': '-',
            'schemas': 'XML/Text',
            'word_count': len(content.split())
        })
        continue

    if status != 200:
        issues.append(f"HTTP {status} on {url} ({label})")
        results.append({
            'url': url,
            'label': label,
            'status': status,
            'redirect': '',
            'title_len': 0,
            'desc_len': 0,
            'h1_count': 0,
            'canonical': 'MISSING',
            'hreflang_count': 0,
            'schemas': 'NONE',
            'word_count': 0
        })
        continue

    html = resp.content.decode('utf-8', errors='ignore')

    # Title
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else ''
    title_len = len(title)

    # Description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
    desc = desc_match.group(1).strip() if desc_match else ''
    desc_len = len(desc)

    # H1 count
    h1s = re.findall(r'<h1\b[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    h1_count = len(h1s)

    # Canonical
    canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html, re.IGNORECASE)
    canonical = canon_match.group(1).strip() if canon_match else ''

    # Hreflang alternates
    hreflangs = re.findall(r'<link\s+rel=["\']alternate["\']\s+hreflang=["\'](.*?)["\']\s+href=["\'](.*?)["\']', html, re.IGNORECASE)
    hreflang_count = len(hreflangs)

    # Schemas
    schema_types = re.findall(r'"@type":\s*["\']([a-zA-Z0-9_]+)["\']', html)
    unique_schemas = sorted(list(set(schema_types)))

    # Words
    plain = re.sub(r'<[^>]+>', ' ', html)
    words = len(plain.split())

    # Check for issues
    if title_len == 0 or title_len > 65:
        # Note: 60-65 is acceptable limit in SERPs
        issues.append(f"Title length {title_len} chars on {url}: '{title}'")
    if desc_len == 0:
        issues.append(f"Missing meta description on {url}")
    if h1_count != 1:
        issues.append(f"H1 count is {h1_count} on {url}")
    if not canonical:
        issues.append(f"Missing canonical tag on {url}")
    if hreflang_count < 3 and not url.startswith('/robots'):
        issues.append(f"Only {hreflang_count} hreflang tags on {url}")

    results.append({
        'url': url,
        'label': label,
        'status': status,
        'title': title,
        'title_len': title_len,
        'desc_len': desc_len,
        'h1_count': h1_count,
        'canonical': canonical,
        'hreflang_count': hreflang_count,
        'schemas': ", ".join(unique_schemas),
        'word_count': words
    })

print(f"Crawled {len(results)} URLs.")
print(f"Issues found: {len(issues)}")
for iss in issues[:20]:
    print(f"  - {iss}")

# Save results as json for table generation in report
with open('scripts/crawl_results.json', 'w', encoding='utf-8') as f:
    json.dump({'results': results, 'issues': issues}, f, ensure_ascii=False, indent=2)
print("\nSaved crawl results to scripts/crawl_results.json")
