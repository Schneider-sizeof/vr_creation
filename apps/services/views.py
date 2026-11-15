"""
Services views.
"""
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.utils.translation import get_language

from .models import Service
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
