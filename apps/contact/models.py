"""
Contact models.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactSubmission(models.Model):
    """Contact form submissions stored in database."""

    SECTOR_CHOICES = [
        ('immobilier', _('Immobilier')),
        ('retail', _('Retail / Commerce')),
        ('architecture', _('Architecture')),
        ('tourisme', _('Tourisme')),
        ('evenementiel', _('Événementiel')),
        ('autre', _('Autre')),
    ]

    name = models.CharField(_('Nom complet'), max_length=200)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=30, blank=True)
    subject = models.CharField(_('Sujet'), max_length=300)
    sector = models.CharField(
        _('Secteur d\'activité'), max_length=50,
        choices=SECTOR_CHOICES, blank=True
    )
    message = models.TextField(_('Message'))
    created_at = models.DateTimeField(_('Envoyé le'), auto_now_add=True)
    is_read = models.BooleanField(_('Lu'), default=False)

    class Meta:
        verbose_name = _('Message de contact')
        verbose_name_plural = _('Messages de contact')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject} ({self.created_at:%d/%m/%Y})"
