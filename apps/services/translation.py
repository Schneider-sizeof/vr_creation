"""
Model translation for Services app.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import Service, ServiceImage, City


class ServiceTranslation(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'full_description', 'meta_title', 'meta_description')


class ServiceImageTranslation(TranslationOptions):
    fields = ('alt_text',)


class CityTranslation(TranslationOptions):
    fields = (
        'name', 'slug', 'region', 'hero_title', 'hero_description',
        'meta_title', 'meta_description', 'intro_text', 'market_description',
        'landmarks', 'typical_projects', 'services_tailored',
        'intervention_logistics', 'travel_time', 'faqs_data'
    )


translator.register(Service, ServiceTranslation)
translator.register(ServiceImage, ServiceImageTranslation)
translator.register(City, CityTranslation)
