"""
Contact form with honeypot and math captcha anti-spam.
"""
import random
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """Contact form with honeypot + math captcha for spam protection."""

    # Honeypot field — hidden, should remain empty
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={'tabindex': '-1', 'autocomplete': 'off'}),
        label='',
    )

    # Math captcha
    captcha_answer = forms.IntegerField(
        label=_('Question de sécurité'),
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': _('Votre réponse'),
            'id': 'contact-captcha',
            'autocomplete': 'off',
        }),
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
        self.captcha_num1 = kwargs.pop('captcha_num1', random.randint(1, 9))
        self.captcha_num2 = kwargs.pop('captcha_num2', random.randint(1, 9))
        super().__init__(*args, **kwargs)
        self.fields['captcha_answer'].label = _('Combien font %(num1)d + %(num2)d ?') % {
            'num1': self.captcha_num1, 'num2': self.captcha_num2
        }

    def clean_website(self):
        """Honeypot validation — if filled, it's a bot."""
        value = self.cleaned_data.get('website')
        if value:
            raise forms.ValidationError(_('Spam detected.'))
        return value

    def clean_captcha_answer(self):
        """Validate math captcha answer."""
        answer = self.cleaned_data.get('captcha_answer')
        expected = self.captcha_num1 + self.captcha_num2
        if answer != expected:
            raise forms.ValidationError(_('Réponse incorrecte. Veuillez réessayer.'))
        return answer
