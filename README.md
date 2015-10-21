# Website #

## For Translators ##

*Note that by contributing a translation you agree to triple license it under the GFDL, CC-BY-SA 4.0 and GPLv2+ licenses.*

This website is being translated as the
[website resource](https://www.transifex.com/otf/freenet/website/) on Transifex.

To contribute without Transifex:

* Fork this repository and create a checkout
* Run update_po.sh from the root directory
* A freenet_site.pot file is generated in the root directory, you can import this in the existing translation or use it as a basis for a new translation. If you've started your translation before 6-6-2015 you may need to run your own .po file through clean_po.py to get a clean merge (and not lose any translations).
* When you done you can save your translation as locale/*language*/LC_MESSAGES/freenet_site.po
* If you want to test your translation make sure your language is in /settings.py and then run ./generate.py. The translated website is at /output/*language*/index.html
* You don't need to commit the .mo file, it will be generated automatically. It is also .gitignored for convenience.
* Please send a pull request on github.

Tips:

* All text is supposed to be [markdown](http://daringfireball.net/projects/markdown/syntax) formatted.
* If the old freenetproject.org website already has a translation you can just copy that one!
* If you encounter weird (HTML) stuff in one of the source texts (like HTML etc.) please open an issue on github.
* If you want you can fix the english text in the pages/*.py file and re-run the ./update_messages.sh script.
* Some of the source text may have weird whitespace at the start and the end, please ignore this.
* Note that newlines are important if they are inside a piece of text. They will end up on the site as line breaks.

## Requirements ##

* Markdown: https://pypi.python.org/pypi/Markdown
* Python 3: http://python.org

## Development ##

To generate a single language for local development:

    ./generate -l en

To generate a localized version suitable for a web server with multiview:

    ./generate

 TODO - describe multiview; cookie config

The basic design is:

- settings.py contains the supported languages and the menu definition
- pages/*.py contain the separate pages of the site
- assets contains css, javascript and images
- locale contains translations
- generate.py is the script that will turn this into a static site in output
- Translation is done using gettext; update_pot.sh will extract all the translatable strings into freenet_site.pot
- If you change English text in the site run update_translations.py so that all translations will get the new text. This may be a slightly
dangerous operation as it may cause a lot of fuzzy matches.

## License ##

### Content ###
*By contributing content you agree to triple license it under the GFDL, CC-BY-SA 4.0 and GPLv2+ licenses.*

Currently most of the content on the Freenet website seems to be licensed under the GNU Free Documentation License. It doesn't contain any copyright statements
so it is hard to verify this. There is a lot of commit history available though. I believe the site has always had a clear GFDL license banner at the bottom, so
contributors can be assumed to have licensed their contributions GFDL. I am not aware of any copyright assignment to the Freenet Project Inc.

There is a problem though. The GFDL is not compatible with the GPLv2 which Freenet itself is licensed under. We actually cannot take text of the website and include
it into Freenet itself. There is another problem. The GFDL states: *You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute.*
Inserting the website into Freenet itself may actually violate this term as the inserted data is only readable when you have the decryption key!

So, is there a way out of this mess? What would be a better license? Just using GPLv2+ would be easiest. CC-BY-SA 4.0 should become compatible with GPLv3 soon. For now we require all new content to be triple licensed.

Further reading:

* [General Resolution: Why the GNU Free Documentation License is not suitable for Debian main](https://www.debian.org/vote/2006/vote_001)

### Components ###
*By contributing code you agree to license it under the terms of the MIT license unless you specify otherwise.*

This website consists of a lot of parts. Files in the assets directory have their own licenses. If not mentioned these are MIT or BSD licensed.

The situation in pages is that everything except commons.py is GDFL licensed due to including content from freenetproject.org.
common.py contains parts of the theme light-wave provided by designbootstrap
(licensed MIT) and is fully MIT licensed itself.

the rabbit network image is copyright Gerard Krol, dual licensed CC-BY 4.0/GPLv2+
the freenetwork background image is copyright Gerard Krol, dual licensed CC-BY 4.0/GPLv2+

Finally there is the generate.py script which is MIT licensed (just so it is as compatible as possible). The MIT license can be found at http://opensource.org/licenses/MIT

assets/css/animations.min.css is copyright 2014, Joe Mottershaw but does not contain a license. See TODO

Some of the icons from ionicons may be licensed CC BY 4.0.

assets/js/jquery.isotope.js: GPLv3

This README.md is copyright Gerard Krol, licensed GFDL/CC-BY-SA 4.0/GPLv2+

So what would the license on the generated files be? The HTML pages are GFDL (stronger than MIT). All other files retain their own licenses.
It would however not be possible to create a unified whole of the software as the GPLv3 and the GFDL are not compatible.

## FAQ ##

*Doesn't the dark background make Freenet look "dark" and "hacker" like?*
It might, but it also makes it look exciting and high-tech. Light websites
are more like "fun", "outside" and "old fashioned paper". If we want to
attract (technical) users and contributors the exiting and high-tech
look will probably suit them better.

*Can I help?* Sure! Please take a look at the issues on Github to see what needs to be done.

*What static site generator does this use?* None, it uses it's own 30 line Python script.
The entire template is also just Python code. If you know Python you don't have to
learn another templating language or theming framework to modify it.

*Why doesn't this use an existing static site generator like Pelican?*
Pelican was tried and it seemed like a lot of work to make a nice template for it.
Also, the support for translations was annoying. Overall it didn't feel like a good fit.

*Why require triple licensing content added to the website?* That's just to be sure.
Probably we'd want to us a single license later, and it is nice to already have permission.
There is a lot of overlap between those licenses so you are not giving much extra away.

*What is the effect of licensing content under multiple licenses?* When someone want to use the content they can choose which of the licenses to use. This gives them a lot more freedom.
