"""
Blog models — Articles and Categories.
"""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Blog article category."""
    name = models.CharField(_('Nom'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        verbose_name = _('Catégorie')
        verbose_name_plural = _('Catégories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    """Blog article / actualité."""
    title = models.CharField(_('Titre'), max_length=300)
    slug = models.SlugField(_('Slug'), max_length=300, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='articles', verbose_name=_('Catégorie')
    )
    author = models.CharField(_('Auteur'), max_length=200, default='VR Creation')
    excerpt = models.TextField(
        _('Extrait'), max_length=500,
        help_text=_('Résumé de l\'article (max 500 caractères)')
    )
    content = models.TextField(_('Contenu'))
    featured_image = models.ImageField(
        _('Image principale'), upload_to='blog/', blank=True, null=True
    )
    published_date = models.DateTimeField(_('Date de publication'))
    is_published = models.BooleanField(_('Publié'), default=False)
    reading_time = models.PositiveIntegerField(
        _('Temps de lecture (min)'), default=5
    )
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
