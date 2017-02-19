#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Freenet Project Inc.'
SITENAME = u'Freenet Project'
SITEURL = 'https://ademan-laptop.github.io/freenet-website-redesign-pelican/'
BASE_URL = 'https://ademan-laptop.github.io/freenet-website-redesign-pelican/'

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

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ["i18n_subsites"]
JINJA_EXTENSIONS = ["jinja2.ext.i18n"]
JINJA_ENVIRONMENT = {
    'extensions' : ["jinja2.ext.i18n"],
}


I18N_SUBSITES = {}

def subsite(language):
    I18N_SUBSITES[language] = {
        'MARKDOWN' : {
            'extension_configs': {
                'markdown_i18n': {
                    'i18n_dir': 'locales',
                    'i18n_lang': language,
                },
            },
        },
    }

subsite('de')
subsite('fr')

I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_TEMPLATES_LANG = 'en'

MARKDOWN = {
    'extensions': ["markdown_i18n", "markdown.extensions.def_list",],
    'extension_configs': {
        'markdown_i18n': {
            'i18n_dir': 'locales',
        },
    },
}

STATIC_PATHS = [
        'assets',
        ]
