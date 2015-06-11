#!/usr/bin/env python
# Update all translation files so they contain the new source texts
# Copyright Gerard Krol
# License: MIT

import subprocess
import settings

# first update freenet.pot
subprocess.call(["./update_pot.sh"])

# then update all translations
for language in settings.languages:
    print(language)
    po_file = "locale/"+language+"/LC_MESSAGES/freenet_site.po"
    pot_file = "freenet_site.pot"
    subprocess.call(["msgmerge", "-U", po_file, pot_file])
