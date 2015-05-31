# License: GFDL
import string
from common import *

class HelpPage(Page):
    slug = "help"
    title = "Help"
    section = "help"
    def generate(self, language, site_menu):
        help_text = text(_("Here you can find information on how to install and use Freenet."))
        return html(head("Freenet - Help"), body(menu(site_menu, self)+section("help","Help", help_text)))
