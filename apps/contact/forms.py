"""
Contact form with honeypot and time-based anti-spam protection.
"""
import time
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """
    Contact form protected by:
    1. Honeypot field (website_url) — hidden from human users via CSS
    2. Submission timestamp (form_time) — rejects automated bots submitting in < 3s
    """

    # Honeypot field — invisible to users, bots fill it in
    website_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'tabindex': '-1',
            'autocomplete': 'off',
            'aria-hidden': 'true',
            'style': 'opacity: 0; position: absolute; top: 0; left: 0; height: 0; width: 0; z-index: -1;',
        }),
        label='',
    )

    # Submission timestamp — minimum elapsed time validation
    form_time = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'sector', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': _('Votre nom complet'),
                'id': 'contact-name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': _('votre@email.com'),
                'id': 'contact-email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': _('Votre numéro de téléphone'),
                'id': 'contact-phone',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': _('Sujet de votre message'),
                'id': 'contact-subject',
            }),
            'sector': forms.Select(attrs={
                'class': 'form-input',
                'id': 'contact-sector',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': _('Décrivez votre projet...'),
                'rows': 6,
                'id': 'contact-message',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.is_bound:
            self.initial['form_time'] = int(time.time())

    def clean_website_url(self):
        """Honeypot validation — if filled, it's a bot."""
        value = self.cleaned_data.get('website_url')
        if value:
            raise forms.ValidationError(_('Spam detected.'))
        return value

    def clean_form_time(self):
        """Validate submission duration: minimum 3 seconds for human entry."""
        raw_val = self.cleaned_data.get('form_time')
        if raw_val:
            try:
                elapsed = time.time() - int(raw_val)
                if elapsed < 3.0:
                    raise forms.ValidationError(
                        _('Formulaire soumis trop rapidement. Veuillez patienter un instant.')
                    )
            except (ValueError, TypeError):
                pass
        return raw_val
