#!/usr/bin/env python
# Generates static pages from python scripts
# License: MIT
import os
import shutil
import settings
import gettext
import codecs
import subprocess

output_path = 'output'

def langpath(language):
    return output_path+"/"+language
def html_filename(language, slug):
    return langpath(language)+'/'+slug+'.html'

# cleanup
try:
    shutil.rmtree('output')
except:
    pass

for language in settings.languages:
    print(language)
    if language != "en":
        # generate .mo files (so we don't have to check them into source control)
        base = "locale/"+language+"/LC_MESSAGES/freenet_site"
        subprocess.call(["msgfmt", "-o", base+".mo", base+".po"])
        lang = gettext.translation('freenet_site', localedir='locale', languages=[language], codeset="utf-8")
        lang.install()
    else:
        gettext.install('freenet_site', codeset="utf-8")
    # copy assets
    os.makedirs(langpath(language))
    shutil.copytree('assets', langpath(language)+'/assets')
    # generate pages
    menu = settings.create_menu()
    for page in menu:
        f = codecs.open(html_filename(language, page.slug),"wt","utf-8")
        f.write(page.generate(language, menu))
        f.close
