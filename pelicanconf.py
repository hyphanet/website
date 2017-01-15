#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Freenet Project Inc.'
SITENAME = u'Freenet Project'
SITEURL = ''

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

PLUGINS = ["i18n_subsites"]
JINJA_EXTENSIONS = ["jinja2.ext.i18n"]
JINJA_ENVIRONMENT = {
        'extensions' : ["jinja2.ext.i18n"],
}

I18N_SUBSITES = {
    'de': {
        'MARKDOWN' : {
            'extension_configs': {
                'markdown_i18n': {
                    'i18n_dir': 'locales',
                    'i18n_lang': 'de',
                },
            },
        },
    },
}

I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'

MARKDOWN = {
    'extensions': ["markdown_i18n"],
    'extension_configs': {
        'markdown_i18n': {
            'i18n_dir': 'locales',
        },
    },
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
