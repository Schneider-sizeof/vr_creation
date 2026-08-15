"""
Core URL patterns.
"""
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path(_('a-propos/'), views.about, name='about'),
    path(_('mentions-legales/'), views.legal_notices, name='legal_notices'),
    path(_('confidentialite/'), views.privacy_policy, name='privacy_policy'),
    path(_('cookies/'), views.cookie_policy, name='cookie_policy'),
    path(_('promotions/'), views.promotions, name='promotions'),
    path(_('promotions/<slug:slug>/'), views.promotion_detail, name='promotion_detail'),
]
