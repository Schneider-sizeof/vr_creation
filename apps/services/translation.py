"""
Model translation for Services app.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import Service, ServiceImage


class ServiceTranslation(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'full_description')


class ServiceImageTranslation(TranslationOptions):
    fields = ('alt_text',)


translator.register(Service, ServiceTranslation)
translator.register(ServiceImage, ServiceImageTranslation)
