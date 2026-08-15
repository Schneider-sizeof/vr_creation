"""
Model translation registration for Core app.
Must be defined before admin to work with modeltranslation.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import (
    SiteSettings, TeamMember, Value, Strength, ProcessStep, HeroSlide, StrategicSuccess,
    Promotion, PromotionDeliverable, PromotionComparison, PromotionStep
)


class SiteSettingsTranslation(TranslationOptions):
    fields = ('site_name', 'tagline', 'address', 'footer_text', 'copyright_text',
              'hero_headline', 'hero_subheadline', 'hero_cta1_label', 'hero_cta2_label')


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


class StrategicSuccessTranslation(TranslationOptions):
    fields = ('title', 'importance')


class PromotionTranslation(TranslationOptions):
    fields = ('title', 'badge_text', 'headline', 'sub_headline', 'short_description',
              'problem_title', 'problem_text', 'solution_title', 'solution_text',
              'solution_quote', 'cta_title', 'cta_text', 'offer_price')


class PromotionDeliverableTranslation(TranslationOptions):
    fields = ('title', 'description')


class PromotionComparisonTranslation(TranslationOptions):
    fields = ('feature', 'without_vr', 'with_vr')


class PromotionStepTranslation(TranslationOptions):
    fields = ('title', 'description')


translator.register(SiteSettings, SiteSettingsTranslation)
translator.register(TeamMember, TeamMemberTranslation)
translator.register(Value, ValueTranslation)
translator.register(Strength, StrengthTranslation)
translator.register(ProcessStep, ProcessStepTranslation)
translator.register(HeroSlide, HeroSlideTranslation)
translator.register(StrategicSuccess, StrategicSuccessTranslation)
translator.register(Promotion, PromotionTranslation)
translator.register(PromotionDeliverable, PromotionDeliverableTranslation)
translator.register(PromotionComparison, PromotionComparisonTranslation)
translator.register(PromotionStep, PromotionStepTranslation)
