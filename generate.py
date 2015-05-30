import os
import shutil
import settings

output_path = 'output'

def langpath(language):
    return output_path+"/"+language
def html_filename(language, slug):
    return langpath(language)+'/'+slug+'.html'
    
shutil.rmtree('output')

for language in settings.languages:
    os.makedirs(langpath(language))
    shutil.copytree('assets', langpath(language)+'/assets')
    for page in settings.menu:
        f = open(html_filename(language, page.slug),'wt')
        f.write(page.generate())
        f.close
