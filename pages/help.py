import string
import common

class HelpPage(object):
    slug = "help"
    def generate(language):
        return common.html(common.head("Freenet - Help"), common.body(common.menu()+common.section("","Help","Here you can find information on how to install and use Freenet.")))
