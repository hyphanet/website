Environment
===========

Install uv (see https://docs.astral.sh/uv/getting-started/installation/)

    curl -LsSf https://astral.sh/uv/install.sh | sh

Enable Pelican plugins

    git submodule init
    git submodule update

Testing 
=======

    uv run make devserver

Deploying
=========

    uv run make github


Build for upload in Freenet
---------------------------

    PYTHONPATH=$PYTHONPATH:pelican-plugins{$(ls pelican-plugins/| sed 's/ /,/g')}
    SITEURL=/USK@0iU87PXyodL2nm6kCpmYntsteViIbMwlJE~wlqIVvZ0,nenxGvjXDElX5RIZxMvwSnOtRzUKJYjoXEDgkhY6Ljw,AQACAAE/freenetproject-mirror/490
    DEBUG=1
    uv run make html && freesitemgr update freenetproject-mirror
