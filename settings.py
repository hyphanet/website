from pages.index import *
from pages.help import *
from pages.sectionlink import *

languages = ["en", "nl"]
title = "Freenet"
menu = [
    IndexPage(),
    SectionLink("index", "services", "What is Freenet?"),
    HelpPage(),
    ]
