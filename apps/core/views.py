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
    strategic_successes = list(StrategicSuccess.objects.filter(is_active=True))
    if not strategic_successes:
        from django.utils.translation import get_language
        lang = (get_language() or 'fr')[:2]
        strategic_successes = [
            {
                'title': {'fr': 'Entreprise & startup', 'en': 'Business & startup', 'ar': 'شركة ومشروع ناشئ'}.get(lang, 'Entreprise & startup'),
                'importance': {'fr': "Construire une image de marque forte pour se lancer avec impact.", 'en': 'Build a strong brand image to launch with impact.', 'ar': 'بناء صورة علامة تجارية قوية للانطلاق بتأثير.'}.get(lang, "Construire une image de marque forte pour se lancer avec impact."),
                'get_font_awesome_icon': 'fas fa-briefcase',
                'get_image_url': '/static/img/strategic/entreprise-startup.jpg',
            },
            {
                'title': {'fr': 'Restaurant & commerce', 'en': 'Restaurant & retail', 'ar': 'مطعم وتجارة'}.get(lang, 'Restaurant & commerce'),
                'importance': {'fr': "Attirer les clients avec un visuel professionnel et engageant.", 'en': 'Attract customers with professional and engaging visuals.', 'ar': 'جذب العملاء بمرئيات احترافية وجذابة.'}.get(lang, "Attirer les clients avec un visuel professionnel et engageant."),
                'get_font_awesome_icon': 'fas fa-store',
                'get_image_url': '/static/img/strategic/restaurant-commerce.jpg',
            },
            {
                'title': {'fr': 'Professionnel & freelance', 'en': 'Professional & freelancer', 'ar': 'مهني ومستقل'}.get(lang, 'Professionnel & freelance'),
                'importance': {'fr': 'Se démarquer avec un portfolio et une présence digitale unique.', 'en': 'Stand out with a unique portfolio and digital presence.', 'ar': 'التميز بملف أعمال وحضور رقمي فريد.'}.get(lang, 'Se démarquer avec un portfolio et une présence digitale unique.'),
                'get_font_awesome_icon': 'fas fa-user-tie',
                'get_image_url': '/static/img/strategic/professionnel-freelance.jpg',
            },
            {
                'title': {'fr': 'Événementiel & salons', 'en': 'Events & exhibitions', 'ar': 'فعاليات ومعارض'}.get(lang, 'Événementiel & salons'),
                'importance': {'fr': 'Captiver votre audience avec des visuels et vidéos percutants.', 'en': 'Captivate your audience with striking visuals and videos.', 'ar': 'إبهار الجمهور بمرئيات وفيديوهات مؤثرة.'}.get(lang, 'Captiver votre audience avec des visuels et vidéos percutants.'),
                'get_font_awesome_icon': 'fas fa-calendar-star',
                'get_image_url': '/static/img/strategic/evenementiel.jpg',
            },
        ]
    
    promotions = list(Promotion.objects.filter(is_active=True).order_by('order'))

    context = {
        'services': services,
        'strengths': strengths,
        'featured_projects': projects,
        'case_studies': case_studies,
        'values': values,
        'process_steps': process_steps,
        'hero_slides': hero_slides,
        'strategic_successes': strategic_successes,
        'promotions': promotions,
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
    
    context = {
        'team_members': team_members,
        'values': values,
        'process_steps': process_steps,
        'strengths': strengths,
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
    active_promotions = Promotion.objects.filter(is_active=True).order_by('order')
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
