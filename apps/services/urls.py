"""
Services URL patterns.
"""
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'services'

urlpatterns = [
    path(_('services/'), views.service_list, name='list'),
    path(_('services/') + '<slug:slug>/', views.service_detail, name='detail'),
]
