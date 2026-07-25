"""
Blog URL patterns.
"""
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'blog'

urlpatterns = [
    path(_('blog/'), views.article_list, name='list'),
    path(_('blog/') + '<slug:slug>/', views.article_detail, name='detail'),
]
