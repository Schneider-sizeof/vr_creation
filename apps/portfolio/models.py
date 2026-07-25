"""
Portfolio models — Projects, Case Studies, Sectors, Virtual Tours.
"""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Sector(models.Model):
    """Industry sector for filtering projects."""
    name = models.CharField(_('Nom'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    icon = models.CharField(_('Icône'), max_length=100, blank=True)
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Secteur')
        verbose_name_plural = _('Secteurs')
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio project / réalisation."""
    title = models.CharField(_('Titre'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    sector = models.ForeignKey(
        Sector, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='projects', verbose_name=_('Secteur')
    )
    client = models.CharField(_('Client'), max_length=200, blank=True)
    description = models.TextField(_('Description'))
    challenge = models.TextField(_('Défi / Problématique'), blank=True)
    solution = models.TextField(_('Solution apportée'), blank=True)
    result = models.TextField(_('Résultat obtenu'), blank=True)
    featured_image = models.ImageField(
        _('Image principale'), upload_to='portfolio/'
    )
    has_virtual_tour = models.BooleanField(_('Visite virtuelle'), default=False)
    virtual_tour_url = models.URLField(
        _('URL visite virtuelle'), blank=True,
        help_text=_('URL iframe de la visite virtuelle 360° (Pannellum, Matterport, etc.)')
    )
    date = models.DateField(_('Date de réalisation'), blank=True, null=True)
    is_featured = models.BooleanField(_('Mis en avant'), default=False)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        verbose_name = _('Projet')
        verbose_name_plural = _('Projets')
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})


class ProjectImage(models.Model):
    """Gallery images for a project."""
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='gallery_images',
        verbose_name=_('Projet')
    )
    image = models.ImageField(_('Image'), upload_to='portfolio/gallery/')
    alt_text = models.CharField(_('Texte alternatif'), max_length=300, blank=True)
    is_360 = models.BooleanField(_('Image 360°'), default=False)
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Image du projet')
        verbose_name_plural = _('Images du projet')
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — Image {self.order}"


class CaseStudy(models.Model):
    """Étude de cas — Problem / Importance / Result / Efficiency format."""
    title = models.CharField(_('Titre'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    sector = models.ForeignKey(
        Sector, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='case_studies', verbose_name=_('Secteur')
    )
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='case_studies', verbose_name=_('Projet lié')
    )
    problem = models.TextField(_('Problème / Contexte'))
    service_importance = models.TextField(_('Importance du service'))
    result = models.TextField(_('Résultat'))
    efficiency = models.TextField(_('Efficacité / Impact'))
    featured_image = models.ImageField(
        _('Image principale'), upload_to='case_studies/', blank=True, null=True
    )
    date = models.DateField(_('Date'), blank=True, null=True)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        verbose_name = _('Étude de cas')
        verbose_name_plural = _('Études de cas')
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:casestudy_detail', kwargs={'slug': self.slug})
