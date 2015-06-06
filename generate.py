#!/usr/bin/env python3
# Generates static pages from python scripts
# Copyright Gerard Krol
# License: MIT
import os
import shutil
import settings
import gettext
import codecs
import subprocess
try:
    import __builtin__ as builtins
except:
    import builtins
import re

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
    
def nop(x):
    return x;

# We strip all text that is to be translated and also remove all newlines at the start
# of a line. That way the text looks much cleaner for the translators.
def install_clean_gettext(gt):
    def c(text):
        return gt(re.sub(r"^[ \t]+", "", text.strip(), flags=re.MULTILINE))
    builtins._ = c

for language in settings.languages:
    print(language)
    if language != "en":
        # generate .mo files (so we don't have to check them into source control)
        base = "locale/"+language+"/LC_MESSAGES/freenet_site"
        subprocess.call(["msgfmt", "-o", base+".mo", base+".po"])
        lang = gettext.translation('freenet_site', localedir='locale', languages=[language], codeset="utf-8")
        install_clean_gettext(lang.gettext)
    else:
        install_clean_gettext(nop)
    # copy assets
    os.makedirs(langpath(language))
    shutil.copytree('assets', langpath(language)+'/assets')
    # generate pages
    menu = settings.create_menu()
    for page in menu:
        f = codecs.open(html_filename(language, page.slug),"w","utf-8")
        f.write(page.generate(language, menu))
        f.close
