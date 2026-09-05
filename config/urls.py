"""
Root URL configuration for VR Creation Company.
Multilingual URL patterns with i18n_patterns.
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.views.static import serve

from apps.seo.sitemaps import VR_SITEMAPS
from apps.seo.views import robots_txt

# Non-i18n URLs
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico', permanent=True)),
    path('vrcreation_dashboard/', RedirectView.as_view(url='/fr/vrcreation_dashboard/', permanent=False)),
    path('vrcreation_dashboard', RedirectView.as_view(url='/fr/vrcreation_dashboard/', permanent=False)),
    path('sitemap.xml', sitemap, {'sitemaps': VR_SITEMAPS},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('i18n/', include('django.conf.urls.i18n')),
]

# i18n URL patterns (prefixed by /fr/, /en/, /ar/)
urlpatterns += i18n_patterns(
    path('vrcreation_dashboard/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('', include('apps.services.urls')),
    path('', include('apps.portfolio.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.contact.urls')),
    prefix_default_language=True,
)

# Always serve media files (user uploads) — uses django.views.static.serve directly
# because Django's static() helper silently returns [] when DEBUG=False
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler404 = 'apps.core.views.custom_404'
handler500 = 'apps.core.views.custom_500'

# Admin site customization
admin.site.site_header = 'VR Creation — Administration'
admin.site.site_title = 'VR Creation Admin'
admin.site.index_title = 'Tableau de bord'
