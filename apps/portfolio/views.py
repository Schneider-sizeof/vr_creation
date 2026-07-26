"""
Portfolio views — Projects, Case Studies, Virtual Tours.
"""
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Sector, Project, CaseStudy
from apps.seo.models import PageSEO


def project_list(request):
    """Filterable portfolio grid."""
    sectors = Sector.objects.all()
    sector_slug = request.GET.get('sector')

    projects = Project.objects.select_related('sector').all()
    if sector_slug:
        projects = projects.filter(
            Q(sector__slug_fr=sector_slug) |
            Q(sector__slug_en=sector_slug) |
            Q(sector__slug_ar=sector_slug)
        )

    try:
        page_seo = PageSEO.objects.get(page_identifier='portfolio')
    except PageSEO.DoesNotExist:
        page_seo = None

    return render(request, 'portfolio/project_list.html', {
        'projects': projects,
        'sectors': sectors,
        'active_sector': sector_slug,
        'page_seo': page_seo,
        'page_identifier': 'portfolio',
    })


def project_detail(request, slug):
    """Project detail with gallery and virtual tour."""
    project = get_object_or_404(
        Project.objects.select_related('sector'),
        Q(slug_fr=slug) | Q(slug_en=slug) | Q(slug_ar=slug)
    )
    gallery = project.gallery_images.all()
    related_projects = Project.objects.filter(
        sector=project.sector
    ).exclude(pk=project.pk)[:3]

    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'gallery': gallery,
        'related_projects': related_projects,
        'page_identifier': 'project_detail',
    })


def casestudy_list(request):
    """Case studies listing."""
    case_studies = CaseStudy.objects.select_related('sector', 'project').all()

    try:
        page_seo = PageSEO.objects.get(page_identifier='case_studies')
    except PageSEO.DoesNotExist:
        page_seo = None

    return render(request, 'portfolio/casestudy_list.html', {
        'case_studies': case_studies,
        'page_seo': page_seo,
        'page_identifier': 'case_studies',
    })


def casestudy_detail(request, slug):
    """Case study detail — Problem / Importance / Result / Efficiency."""
    case_study = get_object_or_404(
        CaseStudy.objects.select_related('sector', 'project'),
        Q(slug_fr=slug) | Q(slug_en=slug) | Q(slug_ar=slug)
    )
    other_studies = CaseStudy.objects.exclude(pk=case_study.pk)[:3]

    return render(request, 'portfolio/casestudy_detail.html', {
        'case_study': case_study,
        'other_studies': other_studies,
        'page_identifier': 'casestudy_detail',
    })


def virtual_tours(request):
    """Virtual tours page — list projects with 360° tours."""
    projects = Project.objects.filter(has_virtual_tour=True).select_related('sector')

    try:
        page_seo = PageSEO.objects.get(page_identifier='virtual_tours')
    except PageSEO.DoesNotExist:
        page_seo = None

    return render(request, 'portfolio/virtual_tours.html', {
        'projects': projects,
        'page_seo': page_seo,
        'page_identifier': 'virtual_tours',
    })
