#!/usr/bin/env python
import os
import shutil
import settings
import gettext

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
    print language
    if language != "en":
        lang = gettext.translation('freenet_site', localedir='locale', languages=[language])
        lang.install()
    else:
        gettext.install('freenet_site')
    # copy assets
    os.makedirs(langpath(language))
    shutil.copytree('assets', langpath(language)+'/assets')
    # generate pages
    menu = settings.create_menu()
    for page in menu:
        if page.section_link: continue # no need to generate these, just a link
        f = open(html_filename(language, page.slug),'wt')
        f.write(page.generate(language, menu))
        f.close
