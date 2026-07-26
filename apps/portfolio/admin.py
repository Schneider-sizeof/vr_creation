"""
Admin configuration for Portfolio app.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Sector, Project, ProjectImage, CaseStudy


@admin.register(Sector)
class SectorAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}


class ProjectImageInline(TranslationTabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'alt_text', 'is_360', 'order')


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ('title', 'sector', 'client', 'is_featured', 'has_virtual_tour', 'date', 'image_preview')
    list_filter = ('sector', 'is_featured', 'has_virtual_tour')
    list_editable = ('is_featured',)
    search_fields = ('title', 'client', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    date_hierarchy = 'date'

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'sector', 'client', 'featured_image',
                       'is_featured', 'date')
        }),
        (_('Contenu'), {
            'fields': ('description', 'challenge', 'solution', 'result')
        }),
        (_('Visite virtuelle'), {
            'fields': ('has_virtual_tour', 'virtual_tour_url'),
            'classes': ('collapse',),
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


@admin.register(CaseStudy)
class CaseStudyAdmin(TranslationAdmin):
    list_display = ('title', 'sector', 'project', 'date', 'image_preview')
    list_filter = ('sector',)
    search_fields = ('title', 'problem', 'result')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'sector', 'project', 'featured_image', 'date')
        }),
        (_('Contenu'), {
            'fields': ('problem', 'service_importance', 'result', 'efficiency')
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
