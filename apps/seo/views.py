"""
SEO views — robots.txt.
"""
from django.conf import settings
from django.shortcuts import render


def robots_txt(request):
    """Dynamic robots.txt with absolute sitemap URL."""
    return render(request, 'seo/robots.txt', {
        'site_domain': 'vrcreationcompany.com',
        'site_protocol': 'https',
        'site_url': 'https://vrcreationcompany.com',
    }, content_type='text/plain')
