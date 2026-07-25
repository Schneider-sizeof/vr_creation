"""
SEO context processor — injects base SEO data into all templates.
"""
from django.conf import settings


def seo_context(request):
    """Add base SEO data to all templates."""
    return {
        'site_domain': settings.SITE_DOMAIN,
        'site_protocol': settings.SITE_PROTOCOL,
        'base_url': f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}",
    }
