# -*- coding: utf-8 -*-
# Python code copyright Gerard Krol, license: MIT
from .common import *

class DevelopersSection(Section):
    def __init__(self):
        self.slug = "developers"
        self.title = _("Developers")
    def get_content(self):
        # License: GFDL
        return text(md(_("""
If you already have a contribution in mind you can find the project repositories
[on GitHub](https://github.com/freenet/). For a separate list of projects see
[here](https://wiki.freenetproject.org/Projects).

We're happy to accept either pull requests on GitHub or patches sent under a
pseudonym through Freenet forums such as FMS.

Feel free to join us on IRC: [#freenet on chat.freenode.net](help.html#irc)
""")))

class TranslationSection(Section):
    def __init__(self):
        self.title = _("Translation")
        self.direct_link = "https://wiki.freenetproject.org/Translation"

class BugTrackerSection(Section):
    def __init__(self):
        self.title = _("Bug tracker")
        self.direct_link = "https://bugs.freenetproject.org/"

class ContributePage(Page):
    def __init__(self):
        self.slug = "contribute"
        self.title = _("Contribute")
        self.first_section_in_menu = True
        self.sections = [
            DevelopersSection(),
            TranslationSection(),
            BugTrackerSection(),
            ]
