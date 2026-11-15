"""
Services URL patterns.
"""
from django.urls import path, re_path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'services'

urlpatterns = [
    path(_('services/'), views.service_list, name='list'),
    path(_('services/') + 'branding-immobilier/', views.redirect_old_branding_slug, name='branding_redirect'),
    path(_('services/') + 'branding-communication-visuelle/', views.redirect_old_branding_slug, name='branding_comm_redirect'),
    path(_('services/') + '<slug:slug>/', views.service_detail, name='detail'),

    # Canonical city hub & detail (uniform ASCII slug across all languages)
    path('zones-intervention/', views.city_hub, name='city_hub'),
    path('zones-intervention/<slug:slug>/', views.city_detail, name='city_detail'),

    # English aliases (service-areas)
    path('service-areas/', views.city_hub),
    path('service-areas/<slug:slug>/', views.city_detail),

    # Arabic aliases (both raw UTF-8 and percent-encoded)
    re_path(r'^(?:مناطق-الخدمة|%D9%85%D9%86%D8%A7%D8%B7%D9%82-%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A9)/?$', views.city_hub),
    re_path(r'^(?:مناطق-الخدمة|%D9%85%D9%86%D8%A7%D8%B7%D9%82-%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A9)/(?P<slug>[-\w]+)/?$', views.city_detail),
]
