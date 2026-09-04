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
