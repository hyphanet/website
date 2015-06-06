find -name "*.py" | xargs xgettext --from-code=UTF-8 -o - | ./clean_po.py > freenet_site.pot
