"""
Blog views.
"""
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Article, Category
from apps.seo.models import PageSEO


def article_list(request):
    """Blog listing with optional category filter."""
    categories = Category.objects.all()
    category_slug = request.GET.get('category')

    articles = Article.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).select_related('category')

    if category_slug:
        articles = articles.filter(
            Q(category__slug_fr=category_slug) |
            Q(category__slug_en=category_slug) |
            Q(category__slug_ar=category_slug)
        )

    try:
        page_seo = PageSEO.objects.get(page_identifier='blog')
    except PageSEO.DoesNotExist:
        page_seo = None

    return render(request, 'blog/article_list.html', {
        'articles': articles,
        'categories': categories,
        'active_category': category_slug,
        'page_seo': page_seo,
        'page_identifier': 'blog',
    })


def article_detail(request, slug):
    """Article detail view."""
    article = get_object_or_404(
        Article.objects.select_related('category'),
        Q(slug_fr=slug) | Q(slug_en=slug) | Q(slug_ar=slug),
        is_published=True,
        published_date__lte=timezone.now()
    )
    related_articles = Article.objects.filter(
        is_published=True,
        category=article.category
    ).exclude(pk=article.pk)[:3]

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'related_articles': related_articles,
        'page_identifier': 'blog_detail',
    })
