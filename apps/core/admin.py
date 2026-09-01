"""
Admin configuration for Core app.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline

from .models import (
    SiteSettings, TeamMember, Value, Strength, ProcessStep, HeroSlide, StrategicSuccess,
    Promotion, PromotionDeliverable, PromotionComparison, PromotionStep
)


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
        (_('Hero page d’accueil'), {
            'fields': ('hero_video', 'hero_video_poster', 'hero_headline',
                       'hero_subheadline', 'hero_cta1_label', 'hero_cta1_link',
                       'hero_cta2_label', 'hero_cta2_link'),
            'description': 'Contenu du hero de la page d’accueil : vidéo de fond, titre, sous-titre et boutons d’action.',
        }),
        (_('Images principales'), {
            'fields': ('hero_image', 'about_image'),
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


@admin.register(StrategicSuccess)
class StrategicSuccessAdmin(TranslationAdmin):
    list_display = ('title', 'importance', 'image_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'importance')

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


class PromotionDeliverableInline(TranslationStackedInline):
    model = PromotionDeliverable
    extra = 1
    classes = ('collapse',)
    fields = ('title', 'description', 'icon', 'image', 'order')


class PromotionComparisonInline(TranslationTabularInline):
    model = PromotionComparison
    extra = 1
    classes = ('collapse',)


class PromotionStepInline(TranslationTabularInline):
    model = PromotionStep
    extra = 1
    classes = ('collapse',)


@admin.register(Promotion)
class PromotionAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'badge_text', 'offer_price', 'is_featured', 'is_customizable', 'is_active', 'order')
    list_editable = ('is_featured', 'is_customizable', 'is_active', 'order')
    list_filter = ('is_active', 'is_featured', 'is_customizable')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'headline', 'sub_headline')
    filter_horizontal = ('included_services',)
    inlines = [PromotionDeliverableInline, PromotionComparisonInline, PromotionStepInline]

    fieldsets = (
        (_('Identité de l\'offre'), {
            'fields': ('title', 'slug', 'badge_text', 'featured_image', 'short_description')
        }),
        (_('Section Accroche / Hero'), {
            'fields': ('headline', 'sub_headline')
        }),
        (_('Section Problème'), {
            'fields': ('problem_title', 'problem_text')
        }),
        (_('Section Solution'), {
            'fields': ('solution_title', 'solution_text', 'solution_quote')
        }),
        (_('Section Appel à l\'action (CTA)'), {
            'fields': ('cta_title', 'cta_text', 'offer_price', 'commission_rate')
        }),
        (_('Services inclus dans le pack'), {
            'fields': ('included_services',),
            'description': 'Sélectionnez les services inclus dans ce pack. Pour les packs personnalisables, le client pourra ajuster cette sélection.',
        }),
        (_('Paramètres du Pack'), {
            'fields': ('is_featured', 'is_customizable', 'is_active', 'order'),
            'description': '• Mise en avant : affiche ce pack en section vedette sur la page d\'accueil.\n'
                           '• Personnalisable : le client peut modifier les services inclus.\n'
                           '• Décocher "Personnalisable" pour les offres sur commission.',
        }),
    )


