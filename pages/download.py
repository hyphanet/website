import string
import markdown
from common import *

class DownloadPage(object):
    slug = "download"
    title = "Download"
    section = "download"
    section_link = False
    def generate(self, language, site_menu):
        content = _("""
This is a _underline_ test.
""")
        h = paragraph(markdown.markdown(content))
        return html(head("Freenet - Download"), body(menu(site_menu, self)+section("download","Download", h)))
