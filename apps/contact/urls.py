"""
Contact URL patterns.
"""
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'contact'

urlpatterns = [
    path(_('contact/'), views.contact_view, name='contact'),
    path(_('contact/merci/'), views.contact_confirmation, name='confirmation'),
]
