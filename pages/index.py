# Python code copyright Gerard Krol, license: MIT
# HTML copyright DesignBootstrap, Gerard Krol, license: MIT
import string
import markdown
import news
from common import *

site_brand = "Freenet"

class HomeSection(Section):
    def __init__(self):
        self.slug = "home"
        self.title = ""
    def generate(self): # override the generate function as this is not a normal section
        def slider_item(title, text, active=""):
            template = """
    <div class="item $active">
        <h3>
            $title
        </h3>
        <p>
            $text
        </p>
    </div>
    """
            return string.Template(template).substitute(title=title, text=text.strip().replace("\n","<br/>"), active=active) # FIXME: user markdown
        sliders = [
            # Slider items copyright Gerard Krol, licensed GFDL/CC-BY-SA 4.0/GPLv2+
            slider_item(_("Avoid Censorship"), _("""
                    Freenet allows you to freely share information
                    without any person, organization or country able
                    to block it. Freenet helps you to remain anonymous.
                    This allows you to communicate without fear.
                """), "active"),
            slider_item(_("Improve the World"), _("""
                    By using Freenet from the "free world" you
                    help people in oppressive regimes share information.
                    The more people use Freenet the easier it will
                    be to obtain. Using it will also be less suspicious.
                """)),
            slider_item(_("Save your (Childrens) Future"), _("""
                    Even if you live in a democratic country a dictator
                    needs only a few years to grab power.
                    Are you prepared?
                    Having experience with using Freenet might save lives!
                """)),
#            slider_item(_("Explore the Dark Web"), _("""
#                    What happens when people get total anonymity?
#                    Does evil surface? Or are most people inherently good?
#                    Freenet contains a varied amount of content,
#                    be careful what links you click though!
#                """)),
            slider_item(_("Meet New People"), _("""
                    People from all over the world use Freenet to
                    communicate. Granted, most of this could be done
                    fine over the open internet.
                    These pioneers however help us test the system.
                """)),
            slider_item(_("Experiment with Exciting New Technology"), _("""
                    Freenet is on the cutting edge of distributed
                    routing research. The data storage provided
                    by Freenet is a proving ground for a number
                    of new distributed systems.
                """)),
            slider_item(_("Host a Website"), _("""
                    Need a website nobody can take over?
                    That is hosted for free? That is
                    very resistant to attacks?
                    Just publish it on Freenet!
                """)),
            slider_item(_("Share Files"), _("""
                    Dropbox? No need, just upload
                    the file to Freenet and a few
                    minutes later anyone with the
                    secret URL can access it!
                """)),
        ]
        content = """
<!--HOME SECTION START-->
<div id="home" >
<div class="container">
<div class="row">
<div class="col-sm-8 col-sm-offset-2 col-md-8 col-md-offset-2 col-lg-8 col-lg-offset-2 ">
<div id="carousel-slider" data-ride="carousel" class="carousel slide  animate-in" data-anim-type="fade-in-up" data-interval="8000">

<div class="carousel-inner">
$sliders
</div>


</div>


</div>
</div>
<div class="row animate-in" data-anim-type="fade-in-up">
<div class="col-sm-6 col-sm-offset-3 col-md-6 col-md-offset-3 col-lg-8 col-lg-offset-2 scroll-me">


<p >
$tagline
</p>
<!-- FIXME: become social
<div class="social">
<a href="#" class="btn button-custom btn-custom-one" ><i class="fa fa-facebook "></i></a>
<a href="#" class="btn button-custom btn-custom-one" ><i class="fa fa-twitter"></i></a>
<a href="#" class="btn button-custom btn-custom-one" ><i class="fa fa-google-plus "></i></a>
<a href="#" class="btn button-custom btn-custom-one" ><i class="fa fa-linkedin "></i></a>
<a href="#" class="btn button-custom btn-custom-one" ><i class="fa fa-pinterest "></i></a>
<a href="#" class="btn button-custom btn-custom-one" ><i class="fa fa-github "></i></a>
</div>
-->
<a href="download.html" class=" btn button-custom btn-custom-two">$download_text</a>
</div>
</div>
</div>

</div>

<!--HOME SECTION END-->
"""
        tagline = _("Share, Chat, Browse. Anonymously. On the Free Network.")
        download_text = _("Get Freenet")
        return string.Template(content).substitute(sliders="".join(sliders),tagline=tagline,download_text=download_text)


class ServiceSection(Section):
    def __init__(self):
        self.slug = "services"
        self.title = _("What is Freenet?")
    def get_content(self):
        def service(icon, title, text):
            content = """
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="$icon"></i>
        <h3>$title</h3>
        $text
    </div>
</div>
"""
            return string.Template(content).substitute(icon=icon,title=title,text=text)
        services = [
             # Services items copyright Gerard Krol, licensed GFDL/CC-BY-SA 4.0/GPLv2+
            service("ion-person", _("Secret Identity"),
                _("Create a secret identity so nobody knows who you are.")),
            service("ion-earth", _("Browse Webpages"),
                _("There are a lot of webpages hosted on Freenet.")),
            service("ion-chatboxes", _("Forums"),
                _("Ask questions and exchange ideas.")),
            service("ion-edit", _("Publish"),
                _("Publish information while remaining anonymous.")),
            service("ion-android-cloud-done", _("Share Files"),
                _("Easy upload & download.")),
            service("ion-hammer", _("Platform"),
                _("Write your own applications on the Freenet platform.")),
            service("ion-cube", _("Resistant"),
                _("Freenet has been designed to be resistant to attacks and censorship.")),
            service("ion-shuffle", _("Distributed"),
                _("No central points of fallure, efficient caching of popular content.")),
            service("ion-erlenmeyer-flask", _("Proven"),
                _("Based on solid research and in practical use for 15 years.")),
        ]
        content = """
<!-- service start -->
<div class="row animate-in" data-anim-type="fade-in-up">
$services
</div>
<!-- service end -->
"""
        return string.Template(content).substitute(services="".join(services))
    
class IntroductionSection(Section):
    def __init__(self):
        self.slug = "introduction"
        self.title = _("Introduction")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        content = _("""
> _"I worry about my child and the Internet all the time, even though she's too young to have logged on yet. Here's what I worry about. I worry that 10 or 15 years from now, she will come to me and say 'Daddy, where were you when they took freedom of the press away from the Internet?'"_   
> --Mike Godwin, [Electronic Frontier Foundation](https://www.eff.org/)

Freenet is free software which lets you anonymously share files, browse and publish "freesites" (web sites accessible only through Freenet) and chat on forums, without fear of censorship. Freenet is decentralised to make it less vulnerable to attack, and if used in "darknet" mode, where users only connect to their friends, is very difficult to detect.

Communications by Freenet nodes are encrypted and are routed through other nodes to make it extremely difficult to determine who is requesting the information and what its content is.

Users contribute to the network by giving bandwidth and a portion of their hard drive (called the "data store") for storing files. Files are automatically kept or deleted depending on how popular they are, with the least popular being discarded to make way for newer or more popular content. Files are encrypted, so generally the user cannot easily discover what is in his datastore, and hopefully can't be held accountable for it. Chat forums, websites, and search functionality, are all built on top of this distributed data store.

Freenet has been downloaded over 2 million times since the project started, and used for the distribution of censored information all over the world including countries such as China and the Middle East. Ideas and concepts pioneered in Freenet have had a significant impact in the academic world. Our 2000 paper "Freenet: A Distributed Anonymous Information Storage and Retrieval System" was the most cited computer science paper of 2000 according to Citeseer, and Freenet has also inspired papers in the worlds of law and philosophy. Ian Clarke, Freenet's creator and project coordinator, was selected as one of the top 100 innovators of 2003 by MIT's Technology Review magazine.

An important recent development, which very few other networks have, is the "darknet": By only connecting to people they trust, users can greatly reduce their vulnerability, and yet still connect to a global network through their friends' friends' friends and so on. This enables people to use Freenet even in places where Freenet may be illegal, makes it very difficult for governments to block it, and does not rely on tunneling to the "free world".

Sounds good? [Get Freenet](download.html)
""")
        return text(markdown.markdown(content))
    
class NewsSection(Section):
    def __init__(self):
        self.slug = "news"
        self.title = _("News")
    def get_content(self):
        # we show the most recent news items
        md_content = ""
        for item in news.news_items():
            md_content += "* " + item.markdown_link() + "\n"
        return text(md(md_content))

class IndexPage(Page):
    def __init__(self):
        self.slug = "index"
        self.title = _("Overview")
        self.sections = [
            HomeSection(),
            ServiceSection(),
            IntroductionSection(),
            NewsSection(),
            ContactSection()]
