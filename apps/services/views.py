"""
Services views.
"""
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

from .models import Service
from apps.core.models import ProcessStep
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
    service = get_object_or_404(
        Service,
        Q(slug_fr=slug) | Q(slug_en=slug) | Q(slug_ar=slug),
        is_active=True
    )
    gallery = service.gallery_images.all()
    other_services = Service.objects.filter(is_active=True).exclude(pk=service.pk)
    process_steps = ProcessStep.objects.all()

    return render(request, 'services/service_detail.html', {
        'service': service,
        'gallery': gallery,
        'other_services': other_services,
        'process_steps': process_steps,
        'page_identifier': 'service_detail',
    })


def redirect_old_branding_slug(request):
    """301 redirect from old branding slugs to canonical branding-visuel."""
    return HttpResponsePermanentRedirect(
        reverse('services:detail', kwargs={'slug': 'branding-visuel'})
    )
