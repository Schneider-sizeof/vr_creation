"""
Services models.
"""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    """A service offered by VR Creation Company."""
    title = models.CharField(_('Titre'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    short_description = models.TextField(
        _('Description courte'), max_length=300,
        help_text=_('Résumé affiché dans les cartes (max 300 caractères)')
    )
    full_description = models.TextField(_('Description complète'))
    icon = models.CharField(
        _('Icône'), max_length=100, blank=True,
        help_text=_('Classe d\'icône ou emoji')
    )
    featured_image = models.ImageField(
        _('Image principale'), upload_to='services/', blank=True, null=True
    )
    meta_title = models.CharField(
        _('Titre SEO'), max_length=70, blank=True,
        help_text=_('Titre pour les moteurs de recherche (max 70 caractères). Laisser vide pour utiliser le titre du service.')
    )
    meta_description = models.CharField(
        _('Description SEO'), max_length=160, blank=True,
        help_text=_('Description pour les moteurs de recherche (max 160 caractères). Laisser vide pour utiliser la description courte.')
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    @property
    def get_font_awesome_icon(self):
        """Return a reliable FontAwesome class string for this service."""
        raw = (self.icon or '').strip()
        
        # If already a valid FA class (e.g. 'fas fa-cube', 'fa-solid fa-cube', 'fa-cube')
        if 'fa-' in raw:
            if not (raw.startswith('fas ') or raw.startswith('far ') or raw.startswith('fab ') or raw.startswith('fa-solid ') or raw.startswith('fa-regular ') or raw.startswith('fa-brands ')):
                return f'fas {raw}' if not raw.startswith('fa-') else f'fas {raw}'
            return raw

        # Slug-based mapping for VR Creation core services
        slug_map = {
            'modelisation-3d': 'fas fa-cube',
            'conception-modelisation-3d': 'fas fa-cube',
            'visites-virtuelles': 'fas fa-vr-cardboard',
            'visites-virtuelles-interactives': 'fas fa-vr-cardboard',
            'captures-360': 'fas fa-camera-retro',
            'captures-360-reelles': 'fas fa-camera-retro',
            'branding-visuel': 'fas fa-palette',
            'branding-communication-visuelle': 'fas fa-palette',
            'site-web-digital': 'fas fa-laptop-code',
            'site-web-experience-digitale': 'fas fa-laptop-code',
            'lead-generation': 'fas fa-bullseye',
            'lead-generation-suivi': 'fas fa-bullseye',
            'photographie': 'fas fa-camera',
            'photographie-professionnelle': 'fas fa-camera',
            'animation-motion-design': 'fas fa-film',
        }
        if self.slug in slug_map:
            return slug_map[self.slug]

        # Emoji mapping fallback
        emoji_map = {
            '🏗️': 'fas fa-cube',
            '🏗': 'fas fa-cube',
            '🥽': 'fas fa-vr-cardboard',
            '📸': 'fas fa-camera-retro',
            '📷': 'fas fa-camera',
            '🎨': 'fas fa-palette',
            '💻': 'fas fa-laptop-code',
            '🎯': 'fas fa-bullseye',
            '🎬': 'fas fa-film',
            '📊': 'fas fa-chart-line',
            '🚀': 'fas fa-rocket',
            '✨': 'fas fa-wand-magic-sparkles',
            '📐': 'fas fa-ruler-combined',
        }
        if raw in emoji_map:
            return emoji_map[raw]

        return 'fas fa-cube'

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})


class ServiceImage(models.Model):
    """Gallery images for a service."""
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='gallery_images',
        verbose_name=_('Service')
    )
    image = models.ImageField(_('Image'), upload_to='services/gallery/')
    alt_text = models.CharField(_('Texte alternatif'), max_length=300, blank=True)
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Image du service')
        verbose_name_plural = _('Images du service')
        ordering = ['order']

    def __str__(self):
        return f"{self.service.title} — Image {self.order}"


class City(models.Model):
    """City / Service Area landing page for Northern Morocco."""
    name = models.CharField(_('Nom de la ville'), max_length=150)
    slug = models.SlugField(_('Slug URL'), max_length=150, unique=True)
    region = models.CharField(_('Région / Province'), max_length=150, blank=True)
    hero_title = models.CharField(_('Titre Hero (H1)'), max_length=255, blank=True)
    hero_description = models.TextField(_('Sous-titre Hero'), blank=True)
    meta_title = models.CharField(_('Titre SEO (max 60 chars)'), max_length=70, blank=True)
    meta_description = models.TextField(_('Meta description SEO (140–160 chars)'), blank=True)
    intro_text = models.TextField(_('Introduction spécifique (120+ mots)'))
    market_description = models.TextField(_('Contexte économique & immobilier local'))
    landmarks = models.TextField(_('Quartiers & Repères locaux'), blank=True, help_text=_('Séparés par des virgules'))
    typical_projects = models.TextField(_('Scénarios de projets types'))
    services_tailored = models.TextField(_('Déclinaison des 7 services pour cette ville'))
    intervention_logistics = models.TextField(_('Logistique & Déplacements depuis Tanger'))
    faqs_data = models.JSONField(_('Questions fréquentes (FAQ)'), default=list, blank=True)
    nearby_cities = models.ManyToManyField('self', blank=True, symmetrical=True, verbose_name=_('Villes voisines à lier'))
    distance_from_tanger = models.CharField(_('Distance depuis Tanger'), max_length=100, blank=True)
    travel_time = models.CharField(_('Temps de trajet moyen'), max_length=100, blank=True)
    hero_image = models.ImageField(_('Image d\'en-tête'), upload_to='cities/', blank=True, null=True)
    order = models.PositiveIntegerField(_('Ordre d\'affichage'), default=0)
    is_published = models.BooleanField(_('Publié'), default=True)
    is_hub = models.BooleanField(_('Ville Hub (Tanger)'), default=False)
    created_at = models.DateTimeField(_('Date de création'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Dernière mise à jour'), auto_now=True)

    class Meta:
        verbose_name = _('Zone d\'intervention (Ville)')
        verbose_name_plural = _('Zones d\'intervention (Villes)')
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.region})"

    def get_absolute_url(self):
        return reverse('services:city_detail', kwargs={'slug': self.slug})

