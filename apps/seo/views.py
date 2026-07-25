"""
SEO views — robots.txt.
"""
from django.conf import settings
from django.shortcuts import render


def robots_txt(request):
    """Dynamic robots.txt."""
    return render(request, 'seo/robots.txt', {
        'site_domain': settings.SITE_DOMAIN,
        'site_protocol': settings.SITE_PROTOCOL,
    }, content_type='text/plain')
