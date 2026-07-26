"""
Admin configuration for Core app.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import SiteSettings, TeamMember, Value, Strength, ProcessStep, HeroSlide


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    """Singleton site settings — only one instance."""

    fieldsets = (
        (_('Identité du site'), {
            'fields': ('site_name', 'tagline', 'logo', 'favicon', 'default_og_image')
        }),
        (_('Coordonnées'), {
            'fields': ('email', 'phone', 'address', 'google_maps_embed_url')
        }),
        (_('Images & Vidéo principales'), {
            'fields': ('hero_image', 'hero_video', 'hero_video_poster', 'about_image'),
            'description': 'La vidéo hero sera affichée en arrière-plan des bannières de toutes les pages (accueil, services, portfolio, blog, contact, etc.).',
        }),
        (_('Réseaux sociaux'), {
            'fields': ('social_facebook', 'social_instagram', 'social_linkedin',
                       'social_youtube', 'social_twitter', 'social_tiktok',
                       'social_behance', 'social_whatsapp'),
        }),
        (_('Google / Analytics / SEO'), {
            'fields': ('google_analytics_id', 'google_search_console_id'),
            'description': 'Configuration des outils Google. L\'ID Analytics est chargé uniquement après consentement cookies.',
        }),
        (_('Pied de page'), {
            'fields': ('footer_text', 'copyright_text'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('name', 'role', 'photo_preview', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role')

    def photo_preview(self, obj):
        if obj.photo:
            try:
                return format_html(
                    '<img src="{}" style="width:40px;height:40px;object-fit:cover;border-radius:50%;">',
                    obj.photo.url
                )
            except Exception:
                return '—'
        return '—'
    photo_preview.short_description = _('Photo')


@admin.register(Value)
class ValueAdmin(TranslationAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)


@admin.register(Strength)
class StrengthAdmin(TranslationAdmin):
    list_display = ('title', 'stat_number', 'stat_label', 'order')
    list_editable = ('order',)


@admin.register(ProcessStep)
class ProcessStepAdmin(TranslationAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(HeroSlide)
class HeroSlideAdmin(TranslationAdmin):
    list_display = ('title', 'image_preview', 'order', 'active')
    list_editable = ('order', 'active')
    search_fields = ('title',)

    def image_preview(self, obj):
        if obj.image:
            try:
                return format_html(
                    '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:4px;">',
                    obj.image.url
                )
            except Exception:
                return '—'
        return '—'
    image_preview.short_description = _('Aperçu')
