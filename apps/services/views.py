"""
Services views.
"""
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.utils.translation import get_language

from .models import Service, City
from .service_catalog_data import get_service_enrichment
from apps.core.models import ProcessStep
from apps.portfolio.models import Project
from apps.seo.models import PageSEO


def service_list(request):
    """List all active services."""
    services = Service.objects.filter(is_active=True)
    try:
        page_seo = PageSEO.objects.get(page_identifier='services')
    except PageSEO.DoesNotExist:
        page_seo = None

    return render(request, 'services/service_list.html', {
        'services': services,
        'page_seo': page_seo,
        'page_identifier': 'services',
    })


def service_detail(request, slug):
    """Detail view for a single service with rich technical deliverables, FAQs, and workflow."""
    service = get_object_or_404(
        Service,
        Q(slug_fr=slug) | Q(slug_en=slug) | Q(slug_ar=slug),
        is_active=True
    )
    gallery = service.gallery_images.all()
    other_services = Service.objects.filter(is_active=True).exclude(pk=service.pk)

    lang = get_language() or 'fr'
    if lang not in ('fr', 'en', 'ar'):
        lang = 'fr'

    enrichment = get_service_enrichment(service.slug) or {}

    turnaround = enrichment.get('turnaround', {}).get(lang) or enrichment.get('turnaround', {}).get('fr', '')
    target_audience = enrichment.get('target_audience', {}).get(lang) or enrichment.get('target_audience', {}).get('fr', '')
    deliverables = enrichment.get('deliverables', {}).get(lang) or enrichment.get('deliverables', {}).get('fr', [])
    custom_process_steps = enrichment.get('process', {}).get(lang) or enrichment.get('process', {}).get('fr', [])
    faqs_data = enrichment.get('faqs', {}).get(lang) or enrichment.get('faqs', {}).get('fr', [])

    # Format FAQs for template and jsonld_faq
    formatted_faqs = []
    for item in faqs_data:
        formatted_faqs.append({
            'question': item.get('q'),
            'answer': item.get('a'),
        })

    # Related Services (2-3 services)
    related_slugs = enrichment.get('related_services', [])
    related_services = Service.objects.filter(slug__in=related_slugs, is_active=True)[:3]
    if not related_services.exists():
        related_services = other_services[:3]

    # Related Projects (1-2 projects)
    related_project_slugs = enrichment.get('related_projects', [])
    related_projects = Project.objects.filter(slug__in=related_project_slugs)[:2]
    if not related_projects.exists():
        related_projects = Project.objects.all()[:2]

    return render(request, 'services/service_detail.html', {
        'service': service,
        'gallery': gallery,
        'other_services': other_services,
        'turnaround': turnaround,
        'target_audience': target_audience,
        'deliverables': deliverables,
        'custom_process_steps': custom_process_steps,
        'faqs': formatted_faqs,
        'related_services': related_services,
        'related_projects': related_projects,
        'page_identifier': 'service_detail',
    })


def redirect_old_branding_slug(request):
    """301 redirect from old branding slugs to canonical branding-visuel."""
    return HttpResponsePermanentRedirect(
        reverse('services:detail', kwargs={'slug': 'branding-visuel'})
    )


def city_hub(request):
    """Hub page for Northern Morocco service areas."""
    cities = City.objects.filter(is_published=True).order_by('order', 'name')
    hub_city = cities.filter(is_hub=True).first() or cities.first()
    other_cities = cities.exclude(pk=hub_city.pk if hub_city else None)
    services = Service.objects.filter(is_active=True)

    lang = get_language() or 'fr'
    if lang == 'ar':
        page_title = "مناطق الخدمة — استوديو 3D والجولات الافتراضية شمال المغرب | VR Creation"
        page_desc = "استكشف مناطق تغطيتنا في طنجة، تطوان، أصيلة، العرائش، شفشاون، الحسيمة والمضيق للحلول البصرية، النمذجة 3D والدرون."
    elif lang == 'en':
        page_title = "Service Areas — 3D Studio & Virtual Tours Northern Morocco | VR Creation"
        page_desc = "Discover our service areas across Tangier, Tetouan, Asilah, Larache, Chefchaouen, Al Hoceima and M'diq for 3D modeling and 360 virtual tours."
    else:
        page_title = "Zones d'intervention — Studio 3D & Visites Virtuelles Nord Maroc | VR Creation"
        page_desc = "Découvrez nos zones d'intervention pour vos projets de modélisation 3D, visite virtuelle 360°, photographie et drone à Tanger, Tétouan et tout le Nord."

    return render(request, 'services/city_hub.html', {
        'cities': cities,
        'hub_city': hub_city,
        'other_cities': other_cities,
        'services': services,
        'page_title': page_title,
        'page_desc': page_desc,
        'page_identifier': 'city_hub',
    })


def city_detail(request, slug):
    """Dedicated city landing page with rich, non-duplicative local content, FAQs and schema."""
    city = get_object_or_404(
        City,
        Q(slug_fr=slug) | Q(slug_en=slug) | Q(slug_ar=slug),
        is_published=True
    )
    nearby_cities = city.nearby_cities.filter(is_published=True).exclude(pk=city.pk)
    services = Service.objects.filter(is_active=True)

    # Format city FAQs for template and jsonld_faq
    formatted_faqs = []
    if isinstance(city.faqs_data, list):
        for item in city.faqs_data:
            q = item.get('q') or item.get('question')
            a = item.get('a') or item.get('answer')
            if q and a:
                formatted_faqs.append({'question': q, 'answer': a})

    # Parse landmarks
    landmarks_list = [l.strip() for l in city.landmarks.split(',') if l.strip()]

    # Parse typical projects lines
    raw_projects = city.typical_projects or ''
    typical_projects_list = []
    for line in raw_projects.split('\n'):
        line = line.strip()
        if line.startswith('- ') or line.startswith('* '):
            typical_projects_list.append(line[2:].strip())
        elif line:
            typical_projects_list.append(line)

    # Parse tailored services lines
    raw_services = city.services_tailored or ''
    tailored_services_list = []
    for line in raw_services.split('\n'):
        line = line.strip()
        if line.startswith('- ') or line.startswith('* '):
            tailored_services_list.append(line[2:].strip())
        elif line:
            tailored_services_list.append(line)

    lang = get_language() or 'fr'
    if city.meta_title:
        page_title = city.meta_title
    else:
        if lang == 'ar':
            page_title = f"{city.name} : استوديو 3D، جولات افتراضية وتصوير درون | VR Creation"
        elif lang == 'en':
            page_title = f"{city.name}: 3D Studio, Virtual Tours & Drone Photography | VR Creation"
        else:
            page_title = f"{city.name} : Studio 3D, Visites Virtuelles & Drone | VR Creation"

    page_desc = city.meta_description or city.hero_description

    return render(request, 'services/city_detail.html', {
        'city': city,
        'nearby_cities': nearby_cities,
        'services': services,
        'faqs': formatted_faqs,
        'landmarks_list': landmarks_list,
        'typical_projects_list': typical_projects_list,
        'tailored_services_list': tailored_services_list,
        'page_title': page_title,
        'page_desc': page_desc,
        'page_identifier': 'city_detail',
    })
