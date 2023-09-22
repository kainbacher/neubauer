# -*- coding: utf-8 -*-
import os
from os import path
# import re
# import pprint
from django.utils.translation import ugettext_lazy as _


BASE_DIR = path.dirname(path.abspath(__file__))

SITE_NAME = 'neubauer'
SITE_ID = 1

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
gettext = lambda s: s

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i:s'
FIXTURE_DIRS = 'fixtures'

ADMINS = (
    ('Roland Kainbacher', 'roland@kainbacher.io'),
)

MANAGERS = ADMINS

SEND_BROKEN_LINK_EMAILS = False

THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_QUALITY = 95
# THUMBNAIL_EXTENSION = 'png'
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    # 'main.processors.blur_processor',
)
THUMBNAIL_ALIASES = {
    '': {
        'image_name': {
            'size': (600, 0),
            'crop': 'True',
            'upscale': 'True',
        },
    },
}

TIME_ZONE = 'Europe/Vienna'
LANGUAGE_CODE = 'de'
WEEK_START_DAY = 1
LANGUAGES = (
    ('de', gettext('DE')),
    # ('en', gettext('EN')),
    # ('fr', gettext('FR')),
)
USE_I18N = True
USE_L10N = True
# USE_TZ = True


MEDIA_ROOT = BASE_DIR + '/../public/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR + '/../public/static/'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
    'djangobower.finders.BowerFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'neubauer.urls'

IP_PATH = SITE_ROOT + '/data/'

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_extensions',
    'compressor',
    'compat',

    'djangocms_text_ckeditor',
    'mptt',
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'djangobower',
    'common',
    'column',
    'spacer',
    'djangocms_link',
    'djangocms_picture',

    'hero',
    'card',
    'contact',
    'badge',
    'mailform',

    # 'djangocms_googlemap',
    # 'djangocms_inherit',
    # 'djangocms_column',
    # 'djangocms_snippet',

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# common non-application specific translations for Caruso project.
LOCALE_PATHS = (
    PROJECT_DIR + '/locale',
)

# CMS
CMS_TEMPLATES = (
    ('standard.html', 'Template Standard'),
)

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': gettext("Content"),
    },
    'footer_column_1': {
        'name': gettext("Footer Column 1"),
    },
    'footer_column_2': {
        'name': gettext("Footer Column 2"),
    },
    'footer_column_3': {
        'name': gettext("Footer Column 3"),
    },
    'footer_column_4': {
        'name': gettext("Footer Column 4"),
    },
    'footer_column_5': {
        'name': gettext("Footer Column 5"),
    },
    'footer_line': {
        'name': gettext("Footer Line"),
    },
}

# CMS_PERMISSION = True

CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': gettext('Deutsch'),
            # 'fallbacks': ['en',],
            'public': True,
        },
        # {
        #     'code': 'en',
        #     'name': gettext('English'),
        #     # 'fallbacks': ['en'],
        #     'public': True,
        #     # 'hide_untranslated': True,
        #     # 'redirect_on_fallback':False,
        # },
    ],
    'default': {
        # 'fallbacks': ['en'],
        # 'redirect_on_fallback': True,
        'public': False,
        'hide_untranslated': True,
    }
}


CKEDITOR_SETTINGS = {
    'contentsCss': "%scss/rte.min.css" % (STATIC_URL),
    'language': '{{ language }}',
    'height': '500',
    'toolbar_CMS': [
        [
            'Bold',
            'Italic',
            'Underline',
            '-',
            'Subscript',
            'Superscript',
            '-',
            'RemoveFormat'
        ],
        [
            'JustifyLeft',
            'JustifyCenter',
            'JustifyRight'
        ],
        [
            'NumberedList',
            'BulletedList',
        ],
        [
            'Format',
            'Styles'
        ],
        [
            'cmsplugins',
            '-',
            'ShowBlocks'
        ],
        ['Undo', 'Redo'],
        ['PasteFromWord'],
        # ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        # ['Maximize', ''],
        ['Source']
    ],
    'toolbar_HTMLField': [
        [
            'Bold',
            'Italic',
            'Underline',
            '-',
            'Subscript',
            'Superscript',
            '-',
            'RemoveFormat'
        ],
        [
            'JustifyLeft',
            'JustifyCenter',
            'JustifyRight'
        ],
        [
            'NumberedList',
            'BulletedList',
        ],
        [
            'Format',
            'Styles'
        ],
        [
            'Link',
            'Unlink'
        ],
        [
            'ShowBlocks'
        ],
        ['Undo', 'Redo'],
        ['PasteFromWord'],
        # ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        # ['Maximize', ''],
        ['Source']
    ],
    'skin': 'moono-lisa',
    'stylesSet': [
        {
            'name': 'Text groß',
            'element': 'span',
            'attributes': {
                'class': 'lead'
            }
        },
        {
            'name': 'Text klein',
            'element': 'span',
            'attributes': {
                'class': 'small'
            }
        },
        {
            'name': 'Pre Header',
            'element': 'span',
            'attributes': {
                'class': 'prehaeder'
            }
        },
    ],
    'format_tags': 'h1;h2;h3;h4;h5;p'
    # 'allowedContent': 'h1;h2;h3;h4;p;span;ul;li;ol;a;strong;em;sup;sub;br'
}

BOWER_COMPONENTS_ROOT = STATIC_ROOT
BOWER_INSTALLED_APPS = (
    'bootstrap#5.0.1',
    'jquery#3.6.0',
    'matchHeight#0.7.2',
    'css-hamburgers',
    # 'slick-carousel#1.8.1',  # http://kenwheeler.github.io/slick/
    # 'font-awesome',
)

# wieder aktivieren
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

WSGI_APPLICATION = 'neubauer.wsgi.application'

FORCE_SCRIPT_NAME = ''

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

from .settings_local import *
