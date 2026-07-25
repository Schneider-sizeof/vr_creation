"""
Model translation for Blog app.
"""
from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Article


class CategoryTranslation(TranslationOptions):
    fields = ('name', 'slug', 'description')


class ArticleTranslation(TranslationOptions):
    fields = ('title', 'slug', 'author', 'excerpt', 'content')


translator.register(Category, CategoryTranslation)
translator.register(Article, ArticleTranslation)
