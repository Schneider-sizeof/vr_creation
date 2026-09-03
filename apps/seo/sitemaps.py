"""
Django Sitemaps for VR Creation Company.
Includes all content types with multilingual support.
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.services.models import Service
from apps.portfolio.models import Project, CaseStudy
from apps.blog.models import Article
from apps.core.models import Promotion


class StaticViewSitemap(Sitemap):
    """Static pages sitemap."""
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['core:home', 'core:about', 'services:list',
                'portfolio:project_list', 'portfolio:casestudy_list',
                'portfolio:virtual_tours', 'blog:list', 'contact:contact',
                'core:promotions']

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    """Services sitemap."""
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Service.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProjectSitemap(Sitemap):
    """Portfolio projects sitemap."""
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class CaseStudySitemap(Sitemap):
    """Case studies sitemap."""
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return CaseStudy.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class ArticleSitemap(Sitemap):
    """Blog articles sitemap."""
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        from django.utils import timezone
        return Article.objects.filter(
            is_published=True,
            published_date__lte=timezone.now()
        )

    def lastmod(self, obj):
        return obj.updated_at


class PromotionSitemap(Sitemap):
    """Promotion/pack pages sitemap."""
    changefreq = 'weekly'
    priority = 0.8

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
}

