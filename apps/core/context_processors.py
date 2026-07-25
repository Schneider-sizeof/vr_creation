"""
Context processor to inject site settings into all templates.
"""
from django.utils.translation import get_language

from .models import SiteSettings


def site_settings(request):
    """Add site settings and language info to template context."""
    try:
        settings_obj = SiteSettings.load()
    except Exception:
        settings_obj = None

    current_language = get_language() or 'fr'
    is_rtl = current_language == 'ar'

    return {
        'site_settings': settings_obj,
        'current_language': current_language,
        'is_rtl': is_rtl,
        'text_dir': 'rtl' if is_rtl else 'ltr',
    }
