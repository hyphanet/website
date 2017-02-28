
Requirements
============

* pelican
* pelican-plugins
  * i18n_subsites
* markdown_i18n


Environment
===========

Using a python virtualenv is recommended.

Create a virtualenv

    virtualenv pelican_env

Use virtualenv

    source pelican_env/bin/activate

Install pelican

    pip install pelican

Get pelican plugins. Place in the same parent directory as this repository.

    $ pwd
    /home/droberts/Projects/freenet-website
    $ cd ../
    $ git clone https://github.com/getpelican/pelican-plugins

Building
========

    find locales -name 'freenet_site.po' -exec msgfmt {} -o messages.mo \;
    pelican -t theme content

Coming soon: Makefile handling of translation processing

Testing 
=======

Use virtualenv

    source pelican_env/bin/activate

Change to output directory

    cd /home/droberts/Projects/freenet-website/output

Serve contents

    python -m pelican.server

