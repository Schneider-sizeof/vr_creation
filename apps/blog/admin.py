"""
Admin configuration for Blog app.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'author', 'published_date', 'is_published',
                    'reading_time', 'image_preview')
    list_filter = ('is_published', 'category')
    list_editable = ('is_published',)
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'author', 'is_published',
                       'published_date', 'reading_time')
        }),
        (_('Contenu'), {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
    )

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:4px;">',
                obj.featured_image.url
            )
        return '—'
    image_preview.short_description = _('Aperçu')
