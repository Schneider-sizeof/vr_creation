"""
SEO template tags for meta tags, JSON-LD, hreflang, breadcrumbs.
Strictly canonicalized to https://vrcreationcompany.com.
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
    """Render <title>, meta description, keywords, canonical, Open Graph, Twitter Cards."""
    request = context.get('request')
    page_seo = context.get('page_seo')
    site_settings = context.get('site_settings')

    # Determine values from page_seo or defaults
    title = ''
    description = ''
    og_image = ''
    no_index = False
    canonical = ''
    keywords = ''

    if page_seo:
        title = page_seo.meta_title or ''
        description = page_seo.meta_description or ''
        keywords = getattr(page_seo, 'keywords', '') or ''
        if page_seo.og_image:
            og_image = page_seo.og_image.url
        no_index = page_seo.no_index
        canonical = page_seo.canonical_url or ''

    # Fallbacks for dynamic content
    obj = context.get('service') or context.get('project') or context.get('article') or context.get('case_study') or context.get('promotion')
    if obj:
        if not title:
            title = getattr(obj, 'meta_title', None) or getattr(obj, 'title', '')
        if not description:
            description = getattr(obj, 'meta_description', None) or getattr(obj, 'short_description', '') or getattr(obj, 'excerpt', '') or ''
            if not description:
                desc_field = getattr(obj, 'description', '') or getattr(obj, 'problem', '') or ''
                description = desc_field if desc_field else ''
        if not keywords:
            keywords = getattr(obj, 'keywords', '') or ''
        if not og_image:
            img = getattr(obj, 'featured_image', None)
            if img:
                og_image = img.url

    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')

    # Fallback to default OG image from site settings or branded fallback banner
    if not og_image and site_settings and site_settings.default_og_image:
        og_image = site_settings.default_og_image.url
    if not og_image:
        og_image = "/static/img/strategic/projet-immobilier.jpg"

    # Strict description trimming at word boundary (≤ 155 chars)
    if description:
        description = description.strip().replace('\r', ' ').replace('\n', ' ')
        if len(description) > 155:
            trimmed = description[:152].rsplit(' ', 1)[0]
            description = f"{trimmed}..."

    # Strict title enforcement: <= 60 characters
    site_name = site_settings.site_name if site_settings else 'VR Creation Tanger'
    brand_suffix = ' | VR Creation'
    if title:
        title = title.strip()
        if 'VR Creation' in title:
            full_title = title
        elif len(title) + len(brand_suffix) <= 60:
            full_title = f"{title}{brand_suffix}"
        else:
            full_title = title
        if len(full_title) > 60:
            full_title = full_title[:57].rsplit(' ', 1)[0] + '...'
    else:
        full_title = 'VR Creation | Studio 3D Tanger'

    current_url = base_url + request.path if request else base_url
    if not canonical:
        canonical = current_url
    elif not canonical.startswith('http'):
        canonical = base_url + canonical

    if og_image and not og_image.startswith('http'):
        og_image = base_url + og_image

    lang = get_language() or 'fr'
    locale_map = {'fr': 'fr_MA', 'en': 'en_US', 'ar': 'ar_MA'}
    og_locale = locale_map.get(lang, 'fr_FR')

    parts = []
    parts.append(f'<title>{full_title}</title>')
    if description:
        parts.append(f'<meta name="description" content="{description}">')
    parts.append(f'<link rel="canonical" href="{canonical}">')
    if no_index:
        parts.append('<meta name="robots" content="noindex, follow">')

    # Google Search Console verification
    gsc_id = ''
    if site_settings and site_settings.google_search_console_id:
        gsc_id = site_settings.google_search_console_id
    if not gsc_id:
        gsc_id = getattr(settings, 'GOOGLE_SEARCH_CONSOLE_ID', '')
    if gsc_id:
        parts.append(f'<meta name="google-site-verification" content="{gsc_id}">')

    # Open Graph
    parts.append(f'<meta property="og:title" content="{full_title}">')
    parts.append('<meta property="og:type" content="website">')
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
    """
    Generate hreflang alternate links:
    fr-MA, en, ar-MA, and x-default pointing to French translation.
    """
    request = context.get('request')
    if not request:
        return ''

    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')
    current_path = request.path

    hreflang_map = {
        'fr': 'fr-MA',
        'en': 'en',
        'ar': 'ar-MA',
    }

    parts = []
    for lang_code, _lang_name in settings.LANGUAGES:
        translated = translate_url(current_path, lang_code)
        if translated:
            full_url = base_url + translated
            hl_code = hreflang_map.get(lang_code, lang_code)
            parts.append(f'<link rel="alternate" hreflang="{hl_code}" href="{full_url}">')

    # x-default points to French (default language)
    default_url = base_url + translate_url(current_path, 'fr')
    parts.append(f'<link rel="alternate" hreflang="x-default" href="{default_url}">')

    return mark_safe('\n    '.join(parts))


@register.simple_tag(takes_context=True)
def get_translated_url(context, lang_code):
    """Return the current page URL translated into the given language code."""
    request = context.get('request')
    if not request:
        return f"/{lang_code}/"
    path = request.get_full_path()
    translated = translate_url(path, lang_code)
    return translated or f"/{lang_code}/"


@register.simple_tag(takes_context=True)
def jsonld_organization(context):
    """JSON-LD Organization schema with Tanger/Morocco locality."""
    site_settings = context.get('site_settings')
    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')

    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": site_settings.site_name if site_settings else "VR Creation Company",
        "url": base_url,
        "description": site_settings.tagline if site_settings else "L'innovation en action",
        "email": site_settings.email if site_settings else "contact@vrcreationcompany.com",
        "telephone": site_settings.phone if site_settings else "+212625071498",
    }

    if site_settings and site_settings.logo:
        data["logo"] = base_url + site_settings.logo.url

    social = []
    if site_settings:
        for field in ['social_facebook', 'social_instagram', 'social_linkedin',
                       'social_youtube', 'social_twitter', 'social_tiktok', 'social_behance']:
            url = getattr(site_settings, field, '')
            if url:
                social.append(url)
    if social:
        data["sameAs"] = social

    if site_settings and site_settings.address:
        data["address"] = {
            "@type": "PostalAddress",
            "streetAddress": site_settings.address,
            "addressLocality": "Tanger",
            "addressRegion": "Tanger-Tétouan-Al Hoceïma",
            "postalCode": "90000",
            "addressCountry": "MA",
        }

    data["areaServed"] = {
        "@type": "City",
        "name": "Tanger",
        "containedInPlace": {
            "@type": "Country",
            "name": "Morocco",
        }
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
    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')

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

    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')
    site_settings = context.get('site_settings')

    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service.title,
        "description": service.short_description or (service.full_description[:200] if service.full_description else ""),
        "url": base_url + service.get_absolute_url(),
        "provider": {
            "@type": "Organization",
            "name": site_settings.site_name if site_settings else "VR Creation Company",
            "url": base_url,
        },
        "areaServed": [
            {"@type": "City", "name": "Tanger"},
            {"@type": "City", "name": "Tétouan"},
            {"@type": "AdministrativeArea", "name": "Northern Morocco"}
        ]
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

    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')

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
def jsonld_project(context):
    """JSON-LD CreativeWork schema for portfolio project detail pages."""
    project = context.get('project')
    if not project:
        return ''

    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')
    site_settings = context.get('site_settings')

    data = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": project.title,
        "description": (project.description[:160] if project.description else ""),
        "url": base_url + project.get_absolute_url(),
        "creator": {
            "@type": "Organization",
            "name": site_settings.site_name if site_settings else "VR Creation Company",
            "url": base_url
        }
    }

    if project.featured_image:
        data["image"] = base_url + project.featured_image.url

    return mark_safe(f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>')


@register.simple_tag(takes_context=True)
def jsonld_faq(context, faqs=None):
    """Generate JSON-LD FAQPage structured data from a list of (question, answer) dicts or tuples."""
    if not faqs:
        return ''

    main_entities = []
    for item in faqs:
        if isinstance(item, dict):
            q = item.get('question') or item.get('q')
            a = item.get('answer') or item.get('a')
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            q, a = item[0], item[1]
        else:
            continue

        if q and a:
            main_entities.append({
                "@type": "Question",
                "name": str(q),
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": str(a)
                }
            })

    if not main_entities:
        return ''

    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entities
    }
    return mark_safe(f'<script type="application/ld+json">\n{json.dumps(data, ensure_ascii=False, indent=2)}\n</script>')


@register.simple_tag(takes_context=True)
def jsonld_local_business(context):
    """JSON-LD Organization + ProfessionalService / LocalBusiness structured data."""
    site_settings = context.get('site_settings')
    base_url = getattr(settings, 'SITE_URL', 'https://vrcreationcompany.com')

    logo_url = (base_url + site_settings.logo.url) if (site_settings and site_settings.logo) else f"{base_url}/media/site/logo.png"

    social = []
    if site_settings:
        for field in ['social_instagram', 'social_linkedin', 'social_tiktok', 'social_facebook', 'social_youtube']:
            url = getattr(site_settings, field, '')
            if url and url not in social:
                social.append(url)
    if not social:
        social = [
            "https://instagram.com/vrcreation",
            "https://linkedin.com/company/vrcreation",
            "https://tiktok.com/@vrcreation"
        ]

    data = {
        "@context": "https://schema.org",
        "@type": ["Organization", "ProfessionalService"],
        "name": "VR Creation Company",
        "image": logo_url,
        "@id": f"{base_url}/#organization",
        "url": f"{base_url}/",
        "telephone": site_settings.phone if (site_settings and site_settings.phone) else "+212625071498",
        "email": (site_settings.email if site_settings else "contact@vrcreationcompany.com"),
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Ibn Batouta bureaux, Av. Youssef Ibn Tachfine",
            "addressLocality": "Tanger",
            "addressRegion": "Tanger-Tétouan-Al Hoceïma",
            "postalCode": "90000",
            "addressCountry": "MA"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 35.7772,
            "longitude": -5.8047
        },
        "areaServed": [
            {"@type": "City", "name": "Tanger"},
            {"@type": "City", "name": "Tétouan"},
            {"@type": "City", "name": "Chefchaouen"},
            {"@type": "AdministrativeArea", "name": "Nord du Maroc"}
        ],
        "sameAs": social + ["https://share.google/CEh7vvvHw6o1atT6d"]
    }

    return mark_safe(f'<script type="application/ld+json">\n{json.dumps(data, ensure_ascii=False, indent=2)}\n</script>')
