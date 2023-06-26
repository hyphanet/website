import os
import os.path

AUTHOR = 'Hyphanet Contributors'
SITENAME = 'Hyphanet'
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
PLUGINS = ['i18n_subsites', 'webassets']
JINJA_ENVIRONMENT = {
    'extensions' : ["jinja2.ext.i18n"],
}

WEBASSETS_SOURCE_PATHS = ['static']

MARKDOWN = {
    'extensions': ["markdown.extensions.def_list", "markdown.extensions.toc", "markdown.extensions.extra", ],
}

I18N_SUBSITES = {}
I18N_GETTEXT_LOCALEDIR = 'locales'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_TEMPLATES_LANG = 'en'

for language in os.listdir(I18N_GETTEXT_LOCALEDIR):
    if os.path.exists(os.path.join(I18N_GETTEXT_LOCALEDIR, language, "LC_MESSAGES", I18N_GETTEXT_DOMAIN + ".mo")):
        I18N_SUBSITES[language] = {'MARKDOWN': MARKDOWN}

STATIC_PATHS = [
    'assets',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
