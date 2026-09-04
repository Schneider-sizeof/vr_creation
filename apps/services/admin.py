"""
Admin configuration for Services app.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Service, ServiceImage


class ServiceImageInline(TranslationTabularInline):
    model = ServiceImage
    extra = 0
    fields = ('image', 'alt_text', 'order')


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'is_active', 'order', 'image_preview')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceImageInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'icon', 'is_active', 'order')
        }),
        (_('Contenu'), {
            'fields': ('short_description', 'full_description', 'featured_image')
        }),
        (_('Optimisation SEO'), {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )

    def image_preview(self, obj):
        if obj.featured_image:
            try:
                return format_html(
                    '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:4px;">',
                    obj.featured_image.url
                )
            except Exception:
                return '—'
        return '—'
    image_preview.short_description = _('Aperçu')
