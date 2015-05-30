import string
from common import *

class HelpPage(object):
    slug = "help"
    def generate(language):
        return html(head("Freenet - Help"), body(menu()+section("","Help","Here you can find information on how to install and use Freenet.")))
