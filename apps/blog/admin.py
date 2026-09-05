"""
Admin configuration for Blog app with AI Post Generator.
"""
import logging
from django.contrib import admin, messages
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _, gettext
from modeltranslation.admin import TranslationAdmin

from .models import Category, Article
from .forms import AIGeneratePostForm
from .services import (
    generate_blog_post_with_gemini,
    GeminiError,
    GeminiAPIKeyMissingError,
    GeminiTimeoutError,
    GeminiRateLimitError,
)

logger = logging.getLogger(__name__)


def _generate_unique_slug(base_text: str) -> str:
    """Generate a unique slug for Article."""
    base_slug = slugify(base_text)
    if not base_slug:
        base_slug = f"article-{int(timezone.now().timestamp())}"
    slug = base_slug[:280]
    counter = 1
    while Article.objects.filter(slug=slug).exists():
        slug = f"{base_slug[:270]}-{counter}"
        counter += 1
    return slug


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    change_list_template = 'admin/blog/article/change_list.html'

    list_display = (
        'title', 'category', 'author', 'status_badge', 'ai_badge',
        'published_date', 'reading_time', 'image_preview'
    )
    list_filter = ('status', 'is_published', 'ai_generated', 'category')
    list_editable = ()
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'category', 'author',
                'status', 'is_published', 'ai_generated',
                'published_date', 'reading_time'
            )
        }),
        (_('Contenu'), {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        (_('Dates système'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def status_badge(self, obj):
        """Displays status as a colored badge."""
        if obj.is_published or obj.status == 'published':
            return format_html(
                '<span style="background: #10b981; color: white; padding: 3px 9px; '
                'border-radius: 12px; font-size: 11px; font-weight: 700; text-transform: uppercase;">{}</span>',
                _('Publié')
            )
        return format_html(
            '<span style="background: #f59e0b; color: white; padding: 3px 9px; '
            'border-radius: 12px; font-size: 11px; font-weight: 700; text-transform: uppercase;">{}</span>',
            _('Brouillon')
        )
    status_badge.short_description = _('Statut')

    def ai_badge(self, obj):
        """Displays AI Generated indicator."""
        if obj.ai_generated:
            return format_html(
                '<span style="background: rgba(61,142,185,0.15); color: #1e4b6e; border: 1px solid #3d8eb9; '
                'padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700;">✨ IA</span>'
            )
        return '—'
    ai_badge.short_description = _('IA')

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:4px;">',
                obj.featured_image.url
            )
        return '—'
    image_preview.short_description = _('Aperçu')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'generate-ai-post/',
                self.admin_site.admin_view(self.generate_ai_post_view),
                name='blog_article_generate_ai',
            ),
        ]
        return custom_urls + urls

    def generate_ai_post_view(self, request):
        """Custom admin view to generate blog posts using Google Gemini AI."""
        if not self.has_add_permission(request):
            raise PermissionDenied

        if request.method == 'POST':
            form = AIGeneratePostForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['topic']
                tone = form.cleaned_data['tone']
                length = form.cleaned_data['length']
                language = form.cleaned_data['language']
                category = form.cleaned_data['category']
                author = form.cleaned_data['author'] or 'VR Creation'

                category_name = category.name if category else None

                try:
                    # Call Gemini AI Service
                    ai_result = generate_blog_post_with_gemini(
                        topic=topic,
                        tone=tone,
                        length=length,
                        language=language,
                        category_name=category_name,
                    )

                    title = ai_result['title']
                    excerpt = ai_result['excerpt']
                    content = ai_result['content']
                    unique_slug = _generate_unique_slug(title)

                    # Calculate reading time
                    word_count = len(content.split())
                    reading_time = max(1, round(word_count / 200))

                    # Create Article with status="draft" and ai_generated=True
                    article = Article(
                        title=title,
                        slug=unique_slug,
                        category=category,
                        author=author,
                        excerpt=excerpt,
                        content=content,
                        published_date=timezone.now(),
                        status='draft',
                        is_published=False,
                        ai_generated=True,
                        reading_time=reading_time,
                    )

                    # Populate modeltranslation fields for the generated language
                    if language == 'en':
                        article.title_en = title
                        article.slug_en = unique_slug
                        article.excerpt_en = excerpt
                        article.content_en = content
                        article.author_en = author
                        # Also populate default fallback fields
                        article.title_fr = title
                        article.slug_fr = unique_slug
                        article.excerpt_fr = excerpt
                        article.content_fr = content
                        article.author_fr = author
                    elif language == 'ar':
                        article.title_ar = title
                        article.slug_ar = unique_slug
                        article.excerpt_ar = excerpt
                        article.content_ar = content
                        article.author_ar = author
                        # Also populate default fallback fields
                        article.title_fr = title
                        article.slug_fr = unique_slug
                        article.excerpt_fr = excerpt
                        article.content_fr = content
                        article.author_fr = author
                    else:  # Default French
                        article.title_fr = title
                        article.slug_fr = unique_slug
                        article.excerpt_fr = excerpt
                        article.content_fr = content
                        article.author_fr = author

                    article.save()

                    # Log admin addition action in history
                    try:
                        LogEntry.objects.log_action(
                            user_id=request.user.pk,
                            content_type_id=ContentType.objects.get_for_model(Article).pk,
                            object_id=article.pk,
                            object_repr=str(article),
                            action_flag=ADDITION,
                            change_message=f"Généré automatiquement par IA Gemini ({topic[:80]}) — Statut Brouillon",
                        )
                    except Exception:
                        pass

                    logger.info("Admin %s generated AI article ID %d: '%s'", request.user.username, article.pk, article.title)

                    messages.success(
                        request,
                        format_html(
                            _("✨ L'article IA <strong>« %(title)s »</strong> a été généré avec succès en mode <strong>Brouillon</strong>. Vous pouvez maintenant le relire et l'éditer."),
                            title=article.title
                        )
                    )

                    return redirect(reverse('admin:blog_article_changelist'))

                except GeminiAPIKeyMissingError as exc:
                    messages.error(
                        request,
                        _("Configuration requise : %(msg)s") % {'msg': str(exc)}
                    )
                except GeminiTimeoutError as exc:
                    messages.error(
                        request,
                        _("Délai d'attente dépassé : %(msg)s") % {'msg': str(exc)}
                    )
                except GeminiRateLimitError as exc:
                    messages.warning(
                        request,
                        _("Limite de requêtes : %(msg)s") % {'msg': str(exc)}
                    )
                except GeminiError as exc:
                    messages.error(
                        request,
                        _("Erreur IA Gemini : %(msg)s") % {'msg': str(exc)}
                    )
                except Exception as exc:
                    logger.exception("Unexpected error during AI blog generation")
                    messages.error(
                        request,
                        _("Une erreur inattendue est survenue : %(msg)s") % {'msg': str(exc)}
                    )
        else:
            form = AIGeneratePostForm()

        context = {
            **self.admin_site.each_context(request),
            'form': form,
            'title': _("Générateur d'articles IA"),
            'opts': self.model._meta,
        }
        return render(request, 'admin/blog/article/generate_ai.html', context)
