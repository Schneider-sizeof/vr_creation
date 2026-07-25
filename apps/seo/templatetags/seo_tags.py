"""
SEO template tags for meta tags, JSON-LD, hreflang, breadcrumbs.
"""
import json
from django import template
from django.conf import settings
from django.urls import reverse, resolve, translate_url
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

register = template.Library()


@register.simple_tag(takes_context=True)
def seo_meta_tags(context):
    """Render <title>, meta description, canonical, Open Graph, Twitter Cards."""
    request = context.get('request')
    page_seo = context.get('page_seo')
    site_settings = context.get('site_settings')

    # Determine values from page_seo or defaults
    title = ''
    description = ''
    og_image = ''
    no_index = False
    canonical = ''

    if page_seo:
        title = page_seo.meta_title or ''
        description = page_seo.meta_description or ''
        if page_seo.og_image:
            og_image = page_seo.og_image.url
        no_index = page_seo.no_index
        canonical = page_seo.canonical_url or ''

    # Fallbacks for dynamic content
    obj = context.get('service') or context.get('project') or context.get('article') or context.get('case_study')
    if obj and not title:
        title = getattr(obj, 'title', '')
    if obj and not description:
        description = getattr(obj, 'short_description', '') or getattr(obj, 'excerpt', '') or ''
        if not description:
            desc_field = getattr(obj, 'description', '') or getattr(obj, 'problem', '') or ''
            description = desc_field[:160] if desc_field else ''
    if obj and not og_image:
        img = getattr(obj, 'featured_image', None)
        if img:
            og_image = img.url

    # Fallback to default OG image from site settings
    if not og_image and site_settings and site_settings.default_og_image:
        og_image = site_settings.default_og_image.url

    site_name = site_settings.site_name if site_settings else 'VR Creation'
    if title and site_name not in title:
        full_title = f"{title} | {site_name}"
    elif not title:
        full_title = site_name
    else:
        full_title = title

    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"
    current_url = base_url + request.path if request else base_url
    if not canonical:
        canonical = current_url

    if og_image and not og_image.startswith('http'):
        og_image = base_url + og_image

    lang = get_language() or 'fr'
    locale_map = {'fr': 'fr_FR', 'en': 'en_US', 'ar': 'ar_SA'}
    og_locale = locale_map.get(lang, 'fr_FR')

    parts = []
    parts.append(f'<title>{full_title}</title>')
    if description:
        parts.append(f'<meta name="description" content="{description}">')
    parts.append(f'<link rel="canonical" href="{canonical}">')
    if no_index:
        parts.append('<meta name="robots" content="noindex, nofollow">')

    # Google Search Console verification
    if site_settings and site_settings.google_search_console_id:
        parts.append(f'<meta name="google-site-verification" content="{site_settings.google_search_console_id}">')

    # Open Graph
    parts.append(f'<meta property="og:title" content="{full_title}">')
    parts.append(f'<meta property="og:type" content="website">')
    parts.append(f'<meta property="og:url" content="{current_url}">')
    parts.append(f'<meta property="og:site_name" content="{site_name}">')
    parts.append(f'<meta property="og:locale" content="{og_locale}">')
    if description:
        parts.append(f'<meta property="og:description" content="{description}">')
    if og_image:
        parts.append(f'<meta property="og:image" content="{og_image}">')
        parts.append('<meta property="og:image:width" content="1200">')
        parts.append('<meta property="og:image:height" content="630">')

    # OG locale alternates
    for l_code, l_locale in locale_map.items():
        if l_code != lang:
            parts.append(f'<meta property="og:locale:alternate" content="{l_locale}">')

    # Twitter Card
    parts.append('<meta name="twitter:card" content="summary_large_image">')
    parts.append(f'<meta name="twitter:title" content="{full_title}">')
    if description:
        parts.append(f'<meta name="twitter:description" content="{description}">')
    if og_image:
        parts.append(f'<meta name="twitter:image" content="{og_image}">')

    return mark_safe('\n    '.join(parts))


@register.simple_tag(takes_context=True)
def hreflang_tags(context):
    """Generate hreflang alternate links for all languages."""
    request = context.get('request')
    if not request:
        return ''

    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"
    current_path = request.path

    parts = []
    for lang_code, lang_name in settings.LANGUAGES:
        translated = translate_url(current_path, lang_code)
        if translated:
            full_url = base_url + translated
            parts.append(f'<link rel="alternate" hreflang="{lang_code}" href="{full_url}">')

    # x-default points to French (default language)
    default_url = base_url + translate_url(current_path, 'fr')
    parts.append(f'<link rel="alternate" hreflang="x-default" href="{default_url}">')

    return mark_safe('\n    '.join(parts))


@register.simple_tag(takes_context=True)
def jsonld_organization(context):
    """JSON-LD Organization schema."""
    site_settings = context.get('site_settings')
    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"

    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": site_settings.site_name if site_settings else "VR Creation Company",
        "url": base_url,
        "description": site_settings.tagline if site_settings else "L'innovation en action",
        "email": site_settings.email if site_settings else "",
        "telephone": site_settings.phone if site_settings else "",
    }

    if site_settings and site_settings.logo:
        data["logo"] = base_url + site_settings.logo.url

    social = []
    if site_settings:
        for field in ['social_facebook', 'social_instagram', 'social_linkedin',
                       'social_youtube', 'social_twitter']:
            url = getattr(site_settings, field, '')
            if url:
                social.append(url)
    if social:
        data["sameAs"] = social

    if site_settings and site_settings.address:
        data["address"] = {
            "@type": "PostalAddress",
            "streetAddress": site_settings.address,
        }

    return mark_safe(f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>')


@register.simple_tag(takes_context=True)
def jsonld_breadcrumb(context, *breadcrumbs):
    """
    JSON-LD BreadcrumbList.
    Usage: {% jsonld_breadcrumb "Services" "/fr/services/" "Modélisation 3D" "" %}
    Pairs of (name, url). Empty url = current page.
    """
    request = context.get('request')
    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"

    items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": base_url + "/fr/"}]

    pos = 2
    for i in range(0, len(breadcrumbs), 2):
        name = breadcrumbs[i]
        url = breadcrumbs[i + 1] if i + 1 < len(breadcrumbs) else ''
        item = {"@type": "ListItem", "position": pos, "name": str(name)}
        if url:
            item["item"] = base_url + str(url) if not str(url).startswith('http') else str(url)
        pos += 1
        items.append(item)

    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }
    return mark_safe(f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>')


@register.simple_tag(takes_context=True)
def jsonld_service(context):
    """JSON-LD Service schema for service detail pages."""
    service = context.get('service')
    if not service:
        return ''

    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"
    site_settings = context.get('site_settings')

    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service.title,
        "description": service.short_description or service.full_description[:200],
        "url": base_url + service.get_absolute_url(),
        "provider": {
            "@type": "Organization",
            "name": site_settings.site_name if site_settings else "VR Creation Company",
        }
    }

    if service.featured_image:
        data["image"] = base_url + service.featured_image.url

    return mark_safe(f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>')


@register.simple_tag(takes_context=True)
def jsonld_article(context):
    """JSON-LD Article schema for blog posts."""
    article = context.get('article')
    if not article:
        return ''

    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"

    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article.title,
        "description": article.excerpt,
        "author": {"@type": "Person", "name": article.author},
        "datePublished": article.published_date.isoformat(),
        "dateModified": article.updated_at.isoformat(),
        "url": base_url + article.get_absolute_url(),
    }

    if article.featured_image:
        data["image"] = base_url + article.featured_image.url

    return mark_safe(f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>')


@register.simple_tag(takes_context=True)
def jsonld_local_business(context):
    """JSON-LD LocalBusiness for contact page."""
    site_settings = context.get('site_settings')
    base_url = f"{settings.SITE_PROTOCOL}://{settings.SITE_DOMAIN}"

    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": site_settings.site_name if site_settings else "VR Creation Company",
        "url": base_url,
        "email": site_settings.email if site_settings else "",
        "telephone": site_settings.phone if site_settings else "",
    }

    if site_settings and site_settings.address:
        data["address"] = {
            "@type": "PostalAddress",
            "streetAddress": site_settings.address,
        }

    if site_settings and site_settings.logo:
        data["image"] = base_url + site_settings.logo.url

    return mark_safe(f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>')
