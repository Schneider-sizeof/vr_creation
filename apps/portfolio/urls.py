"""
Portfolio URL patterns.
"""
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'portfolio'

urlpatterns = [
    path(_('realisations/'), views.project_list, name='project_list'),
    path(_('realisations/') + '<slug:slug>/', views.project_detail, name='project_detail'),
    path(_('etudes-de-cas/'), views.casestudy_list, name='casestudy_list'),
    path(_('etudes-de-cas/') + '<slug:slug>/', views.casestudy_detail, name='casestudy_detail'),
    path(_('visites-virtuelles/'), views.virtual_tours, name='virtual_tours'),
]
