#!/bin/sh
find -name "*.py" | xargs xgettext --add-comments=Translators: --from-code=UTF-8 -o - | ./clean_po.py > freenet_site.pot
# now msgmerge with itself to keep changes in the translated files to a minimum later
msgmerge -U freenet_site.pot freenet_site.pot
