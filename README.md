# New Freenet Website #

This is a new version of the Freenet website. Its main goal is to improve the popularity of Freenet and
to attract new contributors. The theme is [Light Wave]( http://www.designbootstrap.com/light-wave-template-bootstrap-transparent-theme/), by DesignBootstrap
This repository contains a python application that will generate the website for all supported languages.

See it in action on http://realitysink.com/freenet/en/
We're working towards the 1.0 release (when it will replace the official Freenet website). Take a look
at the issues on github to see what still needs to be done. Pull requests are very welcome!

Goals:
- Improve the popularity of Freenet
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

## For Translators ##

We might switch to Transifex soon, for now these are the steps:
* Fork this repository and create a checkout
* Run update_po.sh from the root directory
* A messages.po file is generated in the root directory, you can import this in the existing translation or use it as a basis for a new translation.
* Happy translating! Note that if the old freenetproject.org website already has a translation you can just copy that one.
* If you encounter weird (HTML) stuff in one of the source texts (like HTML etc.) please open an issue on github. Everything is supposed to be markdown. If you want you can fix the english text in the pages/*.py file and re-run the ./update_messages.sh script.
* When you done you can save your translation as locale/<language>/LC_MESSAGES/freenet_site.po
* If you want to test your translation make sure your language is in /settings.py and then run ./generate.py. The translated website is at /output/<language>/index.html
* You don't need to commit the .mo file, it will be generated automatically. It is also .gitignored for convenience.
* Please send a pull request on github.

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

*How can I help?* Take a look at the issues on github.

## License ##

This website consists of a lot of parts. Files in the assets directory
have their own licenses. If not mentioned these are MIT or BSD licensed.

The situation in pages is that everything except commons.py is GDFL licensed
due to including content from freenetproject.org.
common.py contains parts of the theme light-wave provided by designbootstrap
(licensed MIT) and is fully MIT licensed itself.

Finally there is the generate.py script which is MIT licensed (just so it is as compatible as possible).
Anything other written by gerard- and committed to this repository can also be considered MIT licensed.

assets/img/freenetwork.png is copyright Gerard Krol, licensed CC-BY.

assets/css/animations.min.css is copyright 2014, Joe Mottershaw but does not contain a license. See TODO

Some of the icons from ionicons may be licensed CC BY 4.0.

assets/js/jquery.isotope.js : GPLv3

So what would the license on the generated files be? It looks like GPLv3 (from isotope) is the "strongest" license
and it is also compatible with the rest. The entire website itself is thus GPLv3.

## Migration ##
Migration is complete:
* download.html -> download.py
* whatis.html -> index.html#introduction
* index.html (no unique content)
* news.html -> news.py
* philosophy.html -> about.html#philosophy
* people.html -> about.html#people
* papers.html -> about.html#papers
* documentation.html and subpages -> documentation.py
* link to wiki
* faq.html -> help.html#faq
* lists.html -> help.html#mailing-lists
* link to uservoice
* irc.html -> help.html#irc
* link to "The newcomer's guide to anonymous communication on Freenet"
* donate.html -> donate.html
* sponsors.html -> donate.html#sponsors
* link to store http://www.zazzle.com/freenetproject
* developer.html -> contribute.html#developers
* link to https://wiki.freenetproject.org/Translation
* link to bugtracker https://bugs.freenetproject.org/my_view_page.php
