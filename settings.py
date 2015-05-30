#License: GFDL
from pages.index import *
from pages.help import *
from pages.sectionlink import *
from pages.download import *

languages = ["en", "nl"]
title = "Freenet"
def create_menu():
    return [
        IndexPage(),
        SectionLink("index", "services", _("What is Freenet?")),
        DownloadPage(),
        HelpPage(),
        ]
