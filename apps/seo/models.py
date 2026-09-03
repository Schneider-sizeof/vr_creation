"""
SEO models — Per-page meta management and generic SEO overrides.
"""
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _


class PageSEO(models.Model):
    """SEO metadata for static pages (home, about, contact, etc.)."""
    page_identifier = models.SlugField(
        _('Identifiant de page'), max_length=100, unique=True,
        help_text=_('Identifiant unique : home, about, services, portfolio, contact, blog, etc.')
    )
    meta_title = models.CharField(_('Titre SEO'), max_length=70, blank=True)
    meta_description = models.CharField(_('Description SEO'), max_length=160, blank=True)
    og_image = models.ImageField(
        _('Image Open Graph'), upload_to='seo/', blank=True, null=True,
        help_text=_('Image 1200x630px recommandée')
    )
    canonical_url = models.URLField(_('URL canonique'), blank=True)
    no_index = models.BooleanField(
        _('Ne pas indexer'), default=False,
        help_text=_('Ajouter noindex à cette page')
    )
    keywords = models.TextField(
        _('Mots-clés'), blank=True,
        help_text=_('Mots-clés séparés par des virgules pour cette page (ex: modélisation 3D Tanger, visite virtuelle Maroc)')
    )

    class Meta:
        verbose_name = _('SEO — Page statique')
        verbose_name_plural = _('SEO — Pages statiques')

    def __str__(self):
        return f"SEO: {self.page_identifier}"


class SEOMeta(models.Model):
    """Generic SEO metadata attachable to any model instance via GenericForeignKey."""
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name=_('Type de contenu')
    )
    object_id = models.PositiveIntegerField(_('ID objet'))
    content_object = GenericForeignKey('content_type', 'object_id')

    meta_title = models.CharField(_('Titre SEO'), max_length=70, blank=True)
    meta_description = models.CharField(_('Description SEO'), max_length=160, blank=True)
    og_image = models.ImageField(
        _('Image Open Graph'), upload_to='seo/', blank=True, null=True
    )
    canonical_url = models.URLField(_('URL canonique'), blank=True)
    no_index = models.BooleanField(_('Ne pas indexer'), default=False)

    class Meta:
        verbose_name = _('SEO — Métadonnées objet')
        verbose_name_plural = _('SEO — Métadonnées objets')
        unique_together = ('content_type', 'object_id')

    def __str__(self):
        return f"SEO: {self.content_type} #{self.object_id}"
