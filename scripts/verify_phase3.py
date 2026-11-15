import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
import django
django.setup()

from django.test import Client
from apps.services.models import City

client = Client()
cities = list(City.objects.filter(is_published=True).order_by('order'))
langs = ['fr', 'en', 'ar']

print(f"Loaded {len(cities)} cities to verify across {langs}.\n")

total_tests = 0
passed_tests = 0

# 1. Test City Hub in 3 languages
print("=== 1. Testing City Hub ===")
for lang in langs:
    total_tests += 1
    url = f"/{lang}/zones-intervention/"
    resp = client.get(url, HTTP_HOST='vrcreationcompany.com')
    if resp.status_code == 200:
        content = resp.content.decode('utf-8')
        assert 'Zones d\'intervention' in content or 'Service Areas' in content or 'مناطق الخدمة' in content, f"Missing title in hub {lang}"
        assert 'schema.org' in content, f"Missing schema in hub {lang}"
        print(f"  ✓ [{resp.status_code}] {url} (OK, HTML size: {len(content)} bytes)")
        passed_tests += 1
    else:
        print(f"  ✗ [{resp.status_code}] {url} FAILED!")

# 2. Test each City Detail in 3 languages
print("\n=== 2. Testing City Detail Pages ===")
for city in cities:
    for lang in langs:
        total_tests += 1
        url = f"/{lang}/zones-intervention/{city.slug}/"
        resp = client.get(url, HTTP_HOST='vrcreationcompany.com')
        if resp.status_code == 200:
            content = resp.content.decode('utf-8')
            # Extract plain text rough word count
            import re
            plain_text = re.sub(r'<[^>]+>', ' ', content)
            words = plain_text.split()
            word_count = len(words)
            has_prof_service = '"@type": "ProfessionalService"' in content
            has_faq_page = '"@type": "FAQPage"' in content
            has_breadcrumb = '"@type": "BreadcrumbList"' in content
            print(f"  ✓ [{resp.status_code}] {url} ({city.name} - {lang}) Words: ~{word_count} | Schema: ProfService={has_prof_service}, FAQ={has_faq_page}, Breadcrumb={has_breadcrumb}")
            passed_tests += 1
        else:
            print(f"  ✗ [{resp.status_code}] {url} FAILED!")

# 3. Test Sitemap for Cities
print("\n=== 3. Testing Sitemap ===")
total_tests += 1
resp = client.get('/sitemap.xml', HTTP_HOST='vrcreationcompany.com')
if resp.status_code == 200:
    sitemap_xml = resp.content.decode('utf-8')
    assert '/zones-intervention/' in sitemap_xml, "zones-intervention missing from sitemap!"
    assert '/zones-intervention/tanger/' in sitemap_xml, "Tanger missing from sitemap!"
    assert '/zones-intervention/tetouan/' in sitemap_xml, "Tetouan missing from sitemap!"
    print(f"  ✓ [{resp.status_code}] /sitemap.xml includes hub and city entries!")
    passed_tests += 1
else:
    print(f"  ✗ [{resp.status_code}] /sitemap.xml FAILED!")

# 4. Test HTML Sitemap
print("\n=== 4. Testing HTML Sitemap ===")
total_tests += 1
resp = client.get('/fr/plan-du-site/', HTTP_HOST='vrcreationcompany.com')
if resp.status_code == 200:
    content = resp.content.decode('utf-8')
    assert 'Zones d\'intervention' in content, "Zones d'intervention missing from HTML sitemap!"
    assert 'tetouan' in content, "Tetouan link missing from HTML sitemap!"
    print(f"  ✓ [{resp.status_code}] /fr/plan-du-site/ includes Zones d'intervention section!")
    passed_tests += 1
else:
    print(f"  ✗ [{resp.status_code}] /fr/plan-du-site/ FAILED!")

print(f"\n==========================================")
print(f"Results: {passed_tests}/{total_tests} tests passed successfully!")
print(f"==========================================")
