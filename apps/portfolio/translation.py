"""
Model translation for Portfolio app.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import Sector, Project, ProjectImage, CaseStudy


class SectorTranslation(TranslationOptions):
    fields = ('name', 'slug')


class ProjectTranslation(TranslationOptions):
    fields = ('title', 'slug', 'client', 'description', 'challenge', 'solution', 'result')


class ProjectImageTranslation(TranslationOptions):
    fields = ('alt_text',)


class CaseStudyTranslation(TranslationOptions):
    fields = ('title', 'slug', 'problem', 'service_importance', 'result', 'efficiency')


translator.register(Sector, SectorTranslation)
translator.register(Project, ProjectTranslation)
translator.register(ProjectImage, ProjectImageTranslation)
translator.register(CaseStudy, CaseStudyTranslation)
