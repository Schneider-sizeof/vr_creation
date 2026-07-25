"""
Model translation registration for Core app.
Must be defined before admin to work with modeltranslation.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import SiteSettings, TeamMember, Value, Strength, ProcessStep, HeroSlide


class SiteSettingsTranslation(TranslationOptions):
    fields = ('site_name', 'tagline', 'address', 'footer_text', 'copyright_text')


class TeamMemberTranslation(TranslationOptions):
    fields = ('name', 'role', 'bio')


class ValueTranslation(TranslationOptions):
    fields = ('title', 'description')


class StrengthTranslation(TranslationOptions):
    fields = ('title', 'description', 'stat_number', 'stat_label')


class ProcessStepTranslation(TranslationOptions):
    fields = ('title', 'description')


class HeroSlideTranslation(TranslationOptions):
    fields = ('title',)


translator.register(SiteSettings, SiteSettingsTranslation)
translator.register(TeamMember, TeamMemberTranslation)
translator.register(Value, ValueTranslation)
translator.register(Strength, StrengthTranslation)
translator.register(ProcessStep, ProcessStepTranslation)
translator.register(HeroSlide, HeroSlideTranslation)
