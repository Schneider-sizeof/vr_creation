"""
Services views.
"""
from django.shortcuts import render, get_object_or_404

from .models import Service
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
    """Detail view for a single service."""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    gallery = service.gallery_images.all()
    other_services = Service.objects.filter(is_active=True).exclude(pk=service.pk)[:4]

    return render(request, 'services/service_detail.html', {
        'service': service,
        'gallery': gallery,
        'other_services': other_services,
        'page_identifier': 'service_detail',
    })
