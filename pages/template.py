# -*- coding: utf-8 -*-
# Copy this file to quickly add a new page
# License: GFDL
from common import *

class SomeSection(Section):
    def __init__(self):
        self.slug = "title-of-section"
        self.title = _("Title of the Section")
    def get_content(self):
        return text(md(_("""
Markdown text
""")))

class SomeLinkSection(Section):
    def __init__(self):
        self.title = _("Title")
        self.direct_link = "http://example.com"

class SomePage(Page):
    def __init__(self):
        self.slug = "page-title"
        self.title = _("Page Title")
        # self.first_section_in_menu = True
        self.sections = [
            SomeSection(),
            SomeLinkSection(),
            ]
