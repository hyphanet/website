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
- Figure out something for news updates
- Add a license
- Add submenu support?
- Get background image licensed (I'm in contact with the person who made it).
- Have the background image as background image, or add images to the slideshow

## FAQ ##

*What static site generator does this use?* None, it uses it's own 30 line Python script.
The entire template is also just Python code. If you know Python you don't have to
learn another templating language or theming framework to modify it.

*Why doesn't this use an existing static site generator like Pelican?*
Pelican was tried and it seemed like a lot of work to make a nice template for it.
Also, the support for translations was annoying. Overall it didn't feel like a good fit.

*Doesn't the dark background make Freenet look "dark" and "hacker" like?*
It might, but it also makes it look exciting and high-tech. Light websites
are more like "fun", "outside" and "old fashioned paper". If we want to
attract (technical) users and contributors the exiting and high-tech
look will probably suit them better.
