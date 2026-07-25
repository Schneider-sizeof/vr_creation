"""
Admin for SEO app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import PageSEO, SEOMeta


@admin.register(PageSEO)
class PageSEOAdmin(TranslationAdmin):
    list_display = ('page_identifier', 'meta_title', 'no_index')
    search_fields = ('page_identifier', 'meta_title')

    fieldsets = (
        (None, {
            'fields': ('page_identifier',)
        }),
        (_('Métadonnées'), {
            'fields': ('meta_title', 'meta_description', 'og_image', 'canonical_url', 'no_index')
        }),
    )


@admin.register(SEOMeta)
class SEOMetaAdmin(TranslationAdmin):
    list_display = ('content_type', 'object_id', 'meta_title', 'no_index')
    list_filter = ('content_type', 'no_index')
    search_fields = ('meta_title',)
