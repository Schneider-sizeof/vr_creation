"""
Admin configuration for Services app.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from .models import Service, ServiceImage, City


class ServiceImageInline(TranslationTabularInline):
    model = ServiceImage
    extra = 0
    fields = ('image', 'alt_text', 'order')


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
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


@admin.register(City)
class CityAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'slug', 'region', 'is_hub', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    list_filter = ('is_published', 'is_hub', 'region')
    search_fields = ('name', 'region', 'intro_text')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('nearby_cities',)

    fieldsets = (
        (_('Identité & En-tête'), {
            'fields': ('name', 'slug', 'region', 'hero_title', 'hero_description', 'hero_image', 'is_hub', 'is_published', 'order')
        }),
        (_('Contenu spécifique'), {
            'fields': ('intro_text', 'market_description', 'landmarks', 'typical_projects', 'services_tailored', 'intervention_logistics', 'distance_from_tanger', 'travel_time', 'nearby_cities')
        }),
        (_('Foire aux questions (FAQ)'), {
            'fields': ('faqs_data',),
            'description': 'Liste au format JSON d\'objets {"q": "Question", "a": "Réponse"}',
        }),
        (_('Optimisation SEO'), {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )

