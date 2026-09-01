"""
Core views — Home, About, Legal pages, Error handlers.
"""
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page

from .models import TeamMember, Value, Strength, ProcessStep, HeroSlide, StrategicSuccess, Promotion
from apps.services.models import Service
from apps.portfolio.models import Project, CaseStudy
from apps.blog.models import Article
from apps.seo.models import PageSEO


def get_page_seo(page_identifier):
    """Retrieve SEO data for a static page."""
    try:
        return PageSEO.objects.get(page_identifier=page_identifier)
    except PageSEO.DoesNotExist:
        return None


def home(request):
    """Home page — hero, services, strengths, case studies, CTA."""
    services = Service.objects.filter(is_active=True)[:6]
    strengths = Strength.objects.all()[:8]
    projects = Project.objects.filter(is_featured=True)[:4]
    case_studies = CaseStudy.objects.all()[:3]
    values = Value.objects.all()[:4]
    process_steps = ProcessStep.objects.all()
    hero_slides = HeroSlide.objects.filter(active=True)
    strategic_successes = StrategicSuccess.objects.filter(is_active=True)
    
    # Featured promotion for display sections
    featured_promotion = Promotion.objects.filter(is_active=True, is_featured=True).first()

    context = {
        'services': services,
        'strengths': strengths,
        'featured_projects': projects,
        'case_studies': case_studies,
        'values': values,
        'process_steps': process_steps,
        'hero_slides': hero_slides,
        'strategic_successes': strategic_successes,
        'featured_promotion': featured_promotion,
        'page_seo': get_page_seo('home'),
        'page_identifier': 'home',
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page — history, team, values, methodology."""
    team_members = TeamMember.objects.all()
    values = Value.objects.all()
    process_steps = ProcessStep.objects.all()
    strengths = Strength.objects.all()
    
    # Featured promotion for display sections
    featured_promotion = Promotion.objects.filter(is_active=True, is_featured=True).first()

    context = {
        'team_members': team_members,
        'values': values,
        'process_steps': process_steps,
        'strengths': strengths,
        'featured_promotion': featured_promotion,
        'page_seo': get_page_seo('about'),
        'page_identifier': 'about',
    }
    return render(request, 'core/about.html', context)


def legal_notices(request):
    """Mentions légales page."""
    return render(request, 'core/legal_notices.html', {
        'page_seo': get_page_seo('legal'),
        'page_identifier': 'legal',
    })


def privacy_policy(request):
    """Politique de confidentialité page."""
    return render(request, 'core/privacy_policy.html', {
        'page_seo': get_page_seo('privacy'),
        'page_identifier': 'privacy',
    })


def cookie_policy(request):
    """Politique de cookies page."""
    return render(request, 'core/cookie_policy.html', {
        'page_seo': get_page_seo('cookies'),
        'page_identifier': 'cookies',
    })


def promotions(request):
    """Promotions list/grid page."""
    active_promotions = Promotion.objects.filter(is_active=True)
    return render(request, 'core/promotions_list.html', {
        'promotions': active_promotions,
        'page_seo': get_page_seo('promotions'),
        'page_identifier': 'promotions',
    })


def promotion_detail(request, slug):
    """Promotion detail landing page."""
    promotion = get_object_or_404(
        Promotion,
        slug=slug,
        is_active=True
    )
    included_services = promotion.included_services.filter(is_active=True)
    all_services = Service.objects.filter(is_active=True) if promotion.is_customizable else None
    return render(request, 'core/promotion_detail.html', {
        'promotion': promotion,
        'deliverables': promotion.deliverables.all(),
        'comparisons': promotion.comparisons.all(),
        'steps': promotion.steps.all(),
        'included_services': included_services,
        'all_services': all_services,
        'page_identifier': 'promotion_detail',
    })


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'core/404.html', status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, 'core/500.html', status=500)
