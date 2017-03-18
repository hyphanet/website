#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import os.path

AUTHOR = u'Freenet Project Inc.'
SITENAME = u'Freenet Project'
SITEURL = os.environ['SITEURL']
BASE_URL = os.environ['SITEURL']
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = set()

# Social widget
SOCIAL = set()

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["i18n_subsites", "assets", "optimize_images"]
if os.environ['SHOULD_COMPRESS'] == 'True':
    PLUGINS += ["gzip_cache"]
    GZIP_CACHE_OVERWRITE = os.environ['SHOULD_COMPRESS']
JINJA_ENVIRONMENT = {
    'extensions' : ["jinja2.ext.i18n"],
}


I18N_SUBSITES = {}

def subsite(language):
    I18N_SUBSITES[language] = {
        'MARKDOWN' : {
            'extensions': ["markdown.extensions.def_list", "markdown.extensions.toc", "markdown_i18n", ],
            'extension_configs': {
                'markdown_i18n': {
                    'i18n_dir': 'locales',
                    'i18n_lang': language,
                },
            },
        },
    }

for language in os.listdir("locales"):
    if os.path.exists(os.path.join("locales", language, "LC_MESSAGES", "messages.mo")):
        subsite(language)

I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_TEMPLATES_LANG = 'en'

MARKDOWN = {
    'extensions': ["markdown.extensions.def_list", "markdown.extensions.toc", "markdown_i18n", ],
    'extension_configs': {
        'markdown_i18n': {
            'i18n_dir': 'locales',
        },
    },
}

STATIC_PATHS = [
    'assets',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
