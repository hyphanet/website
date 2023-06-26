import os
import os.path

AUTHOR = 'Freenet Project Inc.'
SITENAME = 'Freenet Project'
SITEURL = ''
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

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
PLUGINS = ["assets", "i18n_subsites", "optimize_images"]
JINJA_ENVIRONMENT = {
    'extensions' : ["jinja2.ext.i18n"],
}

ASSET_SOURCE_PATHS = ['static']

I18N_SUBSITES = {
        'fr': {},
        'ru': {},
}

I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_TEMPLATES_LANG = 'en'


MARKDOWN = {
    'extensions': ["markdown.extensions.def_list", "markdown.extensions.toc", "markdown.extensions.extra", ],
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
