# New Freenet Website #

Goals:
- Should look nice
- Static (so it does not need a webserver and can also be hosted on Freenet)
- Should work without Javascript and through FProxy
- The website should be easy to translate & maintain

The basic design is:
- settings.py contains the supported languages and the menu definition
- pages/*.py contain the separate pages of the site
- assets contains css, javascript and images
- locale contains translations
- generate.py is the script that will turn this into a static site in output
- Translation is done using gettext; update_messages.sh will extract all the translatable strings into messages.po

Status:
- General layout and design are done
- A single page (Download) has been moved over

Todo:
- Make the list of possibilities of Freenet translatable
- Move over all existing content
