"""
Django base settings for VR Creation Company.
"""
import os
from pathlib import Path
from copy import copy

# Python 3.14 / Django 5.1 context copy bug monkeypatch
try:
    from django.template.context import Context, BaseContext
    def _clean_copy(self):
        duplicate = self.__class__.__new__(self.__class__)
        duplicate.__dict__ = copy(self.__dict__)
        duplicate.dicts = self.dicts[:]
        if hasattr(self, 'render_context'):
            duplicate.render_context = copy(self.render_context)
        return duplicate
    Context.__copy__ = _clean_copy
    BaseContext.__copy__ = _clean_copy
except ImportError:
    pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-vrc-dev-key-change-in-production-!@#$%'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'vrcreation.com')
SITE_PROTOCOL = os.environ.get('SITE_PROTOCOL', 'https')

# Application definition
INSTALLED_APPS = [
    # Modeltranslation must be before django.contrib.admin
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',

    # Third-party

    # Project apps
    'apps.core',
    'apps.services',
    'apps.portfolio',
    'apps.blog',
    'apps.contact',
    'apps.seo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'apps.core.context_processors.site_settings',
                'apps.seo.context_processors.seo_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database — SQLite in data/ directory
DATABASE_PATH = os.environ.get(
    'DATABASE_PATH',
    str(BASE_DIR / 'data' / 'db.sqlite3')
)

# Ensure the data directory exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
        'OPTIONS': {
            'timeout': 20,
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =============================================================================
# Internationalization / Multilingual
# =============================================================================
LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
    ('ar', 'العربية'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'fr'
MODELTRANSLATION_LANGUAGES = ('fr', 'en', 'ar')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('fr', 'en')

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =============================================================================
# Static files (CSS, JavaScript, Images)
# =============================================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# =============================================================================
# Media files (user uploads)
# =============================================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =============================================================================
# Email
# =============================================================================
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() in ('true', '1')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'contact@vrcreation.com')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'contact@vrcreation.com')

# =============================================================================
# Cache (file-based, good for SQLite deployments)
# =============================================================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# =============================================================================
# Security defaults (overridden in prod.py)
# =============================================================================
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# Contact form rate limiting
# =============================================================================
CONTACT_RATE_LIMIT_SECONDS = int(os.environ.get('CONTACT_RATE_LIMIT_SECONDS', '60'))
CONTACT_RATE_LIMIT_MAX = int(os.environ.get('CONTACT_RATE_LIMIT_MAX', '5'))

# =============================================================================
# Image optimization
# =============================================================================
MAX_IMAGE_SIZE = (1920, 1080)
THUMBNAIL_SIZE = (600, 400)
OG_IMAGE_SIZE = (1200, 630)
