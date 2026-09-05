"""
Forms for Blog app including AI Article Generation Form.
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Category


class AIGeneratePostForm(forms.Form):
    """Form used in Django Admin to generate blog articles with Gemini AI."""

    TONE_CHOICES = [
        ('professionnel', _('Professionnel & Expert')),
        ('engageant', _('Dynamique & Engageant')),
        ('informatif', _('Pédagogique & Informatif')),
        ('technique', _('Technique & Spécialisé 3D/VR')),
        ('persuasif', _('Persuasif & Commercial')),
        ('storytelling', _('Storytelling & Inspirant')),
    ]

    LENGTH_CHOICES = [
        ('court', _('Court (~400 à 600 mots)')),
        ('moyen', _('Standard (~600 à 800 mots)')),
        ('long', _('Approfondi (~800 à 1200 mots)')),
    ]

    LANGUAGE_CHOICES = [
        ('fr', _('Français')),
        ('en', _('English')),
        ('ar', _('العربية')),
    ]

    topic = forms.CharField(
        label=_('Sujet principal / Mots-clés'),
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'vLargeTextField',
            'placeholder': _("Ex: Les avantages de la modélisation 3D et des rendus photoréalistes pour l'architecture et l'immobilier haut de gamme..."),
            'required': True,
        }),
        help_text=_("Indiquez le sujet principal, les axes clés ou les mots-clés que l'article doit aborder.")
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label=_('Catégorie'),
        empty_label=_('— Aucune catégorie (Général) —'),
        widget=forms.Select(attrs={'class': 'vSelect'}),
    )

    tone = forms.ChoiceField(
        label=_('Ton de rédaction'),
        choices=TONE_CHOICES,
        initial='professionnel',
        widget=forms.Select(attrs={'class': 'vSelect'}),
    )

    length = forms.ChoiceField(
        label=_('Longueur cible'),
        choices=LENGTH_CHOICES,
        initial='moyen',
        widget=forms.Select(attrs={'class': 'vSelect'}),
    )

    language = forms.ChoiceField(
        label=_("Langue de l'article"),
        choices=LANGUAGE_CHOICES,
        initial='fr',
        widget=forms.Select(attrs={'class': 'vSelect'}),
    )

    author = forms.CharField(
        label=_('Nom de l\'auteur'),
        max_length=200,
        initial='VR Creation',
        required=False,
        widget=forms.TextInput(attrs={'class': 'vTextField'}),
    )
