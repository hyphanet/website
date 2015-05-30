import os
import shutil
import settings

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
    # copy assets
    os.makedirs(langpath(language))
    shutil.copytree('assets', langpath(language)+'/assets')
    # generate pages
    for page in settings.menu:
        if page.section_link: continue # no need to generate these, just a link
        f = open(html_filename(language, page.slug),'wt')
        f.write(page.generate(language, settings.menu))
        f.close
