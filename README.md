Environment
===========

Install the required packages

    sudo apt-get install python-pip virtualenv gettext optipng libjpeg-turbo-progs

Using a python virtualenv is recommended.

Create a virtualenv

    virtualenv pelican_env

Use virtualenv

    source pelican_env/bin/activate

Install requirements

    pip install -r requirements.txt

Building
========

    make html

Testing 
=======

    firefox output/index.html
