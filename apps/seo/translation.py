"""
Model translation for SEO app.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import PageSEO, SEOMeta


class PageSEOTranslation(TranslationOptions):
    fields = ('meta_title', 'meta_description', 'keywords')


class SEOMetaTranslation(TranslationOptions):
    fields = ('meta_title', 'meta_description')


translator.register(PageSEO, PageSEOTranslation)
translator.register(SEOMeta, SEOMetaTranslation)
