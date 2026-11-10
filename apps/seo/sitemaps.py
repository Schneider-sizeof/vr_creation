"""
Django Sitemaps for VR Creation Company.
Includes all content types with full multilingual support (French, English, Arabic)
and hreflang alternate links for Google Search Console.
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.services.models import Service
from apps.portfolio.models import Project, CaseStudy
from apps.blog.models import Article
from apps.core.models import Promotion


class BaseVRSitemap(Sitemap):
    """Base sitemap with HTTPS and multilingual hreflang enabled."""
    protocol = 'https'
    i18n = True
    alternates = True


class StaticViewSitemap(BaseVRSitemap):
    """Main static pages sitemap."""
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home',
            'core:about',
            'services:list',
            'portfolio:project_list',
            'portfolio:casestudy_list',
            'portfolio:virtual_tours',
            'blog:list',
            'contact:contact',
            'core:promotions',
        ]

    def location(self, item):
        return reverse(item)


class LegalViewSitemap(BaseVRSitemap):
    """Legal & compliance pages sitemap."""
    priority = 0.3
    changefreq = 'yearly'

    def items(self):
        return [
            'core:legal_notices',
            'core:privacy_policy',
            'core:cookie_policy',
        ]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(BaseVRSitemap):
    """Services sitemap."""
    changefreq = 'weekly'
    priority = 0.85

    def items(self):
        return Service.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProjectSitemap(BaseVRSitemap):
    """Portfolio projects sitemap."""
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class CaseStudySitemap(BaseVRSitemap):
    """Case studies sitemap."""
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return CaseStudy.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class ArticleSitemap(BaseVRSitemap):
    """Blog articles sitemap."""
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        from django.utils import timezone
        return Article.objects.filter(
            is_published=True,
            published_date__lte=timezone.now()
        )

    def lastmod(self, obj):
        return obj.updated_at


class PromotionSitemap(BaseVRSitemap):
    """Promotion/pack pages sitemap."""
    changefreq = 'weekly'
    priority = 0.85

    def items(self):
        return Promotion.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


VR_SITEMAPS = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
    'projects': ProjectSitemap,
    'case_studies': CaseStudySitemap,
    'articles': ArticleSitemap,
    'promotions': PromotionSitemap,
    'legal': LegalViewSitemap,
}
