Environment
===========

Install the required packages

    sudo apt-get install python-pip python-virtualenv gettext optipng libjpeg-turbo-progs

Using a python virtualenv is recommended.

Create a virtualenv

    virtualenv pelican_env

Use virtualenv

    source pelican_env/bin/activate

Install Python modules

    pip install -r requirements.txt

Enable Pelican plugins

    git submodule init
    git submodule update

Building
========

    make html

Testing 
=======

    firefox output/index.html
