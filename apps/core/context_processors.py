"""
Context processor to inject site settings into all templates.
"""
from django.utils.translation import get_language

from .models import SiteSettings, Promotion


def site_settings(request):
    """Add site settings, language info, and featured promotion to template context."""
    try:
        settings_obj = SiteSettings.load()
    except Exception:
        settings_obj = None

    # Featured promotion — available globally for banners on any page
    try:
        featured_promo = Promotion.objects.filter(is_active=True, is_featured=True).first()
    except Exception:
        featured_promo = None

    current_language = get_language() or 'fr'
    is_rtl = current_language == 'ar'

    return {
        'site_settings': settings_obj,
        'featured_promotion': featured_promo,
        'current_language': current_language,
        'is_rtl': is_rtl,
        'text_dir': 'rtl' if is_rtl else 'ltr',
    }
