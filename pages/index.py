# Python code copyright Gerard Krol, license: MIT
# HTML copyright DesignBootstrap, Gerard Krol, license: MIT
import pages.news as news
from pages.common import *

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
                    Even if you live in a democratic country a
                    dictator only needs a few years to grab power.
                    Are you prepared?
                    Freenet might save lives!
                """)),
#            slider_item(_("Explore the Dark Web"), _("""
#                    What happens when people get total anonymity?
#                    Does evil surface? Or are most people inherently good?
#                    Freenet contains a varied amount of content,
#                    be careful what links you click though!
#                """)),
            slider_item(_("Meet New People"), _("""
                    People from all over the world
                    use Freenet to communicate.
                    Some of these do so anonymously.
                    You would never hear their voices in the open.
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
                    Dropbox? No need. Just upload
                    the file to Freenet and a few
                    minutes later anyone with the
                    secret URL can access it.
                """)),
        ]
        content = """
<!--HOME SECTION START-->
<section id="home">
<div class="container">
<div class="row text-center">
<div class="col-sm-2 col-md-2 col-lg-2">
        <div class="item active">
             <h4>&nbsp; &nbsp;</h4>
             <p>&nbsp; &nbsp;</p>
             <p>&nbsp; &nbsp;</p>
             <p>&nbsp; &nbsp;</p>
             <p><a href="news.html#20150211"><img src="assets/img/suma2015_badge_transparent.png" alt="SUMA Award 2014/15" /></a></p>
        </div>
</div>
<div class="col-sm-8 col-md-8 col-lg-8">
<div class="row">
<div class="col-sm-12 col-md-12 col-lg-12">
<div id="carousel-slider" data-ride="carousel" class="carousel slide  animate-in" data-anim-type="fade-in-up" data-interval="8000">

<div class="carousel-inner">
$sliders
</div>


</div>


</div>
</div>
<div class="row animate-in" data-anim-type="fade-in-up">
<div class="col-sm-12 col-md-12 col-lg-12 scroll-me">
<div class="download">

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
<a href="download.html#autostart" class=" btn button-custom btn-custom-two">
    <i class="icon ion-arrow-down-a"></i>
    $download_text
</a>
</div>
</div>
</div>
</div>
<!--DONATE SUBSECTION -->
<div class="col-sm-2 col-md-2 col-lg-2">
        <div class="item active donate" id="donate_button">
             <h4>$donate_title</h4>
             <p>$donate_text</p>
             <div class="meter blue">
                 <span style="width: calc(MONEYMONTHS / 12 *100%)">MONEYMONTHS / 12 months</span>
             </div>
             <a class="btn button-custom btn-custom-two donate-button" href="donate.html">$donate_button_text</a>
        </div>
</div>
<!-- DONATE SUBSECTION END -->
</div>
</div>
</div>

</section>

<!--HOME SECTION END-->
"""
        tagline = _("Share, Chat, Browse. Anonymously.")
        download_text = _("Download Freenet")
        donate_title = _("Please Donate")
        donate_text = _("""Your donations pay our servers and developer. Our current funds will&nbsp;last""")
        donate_button_text = _("Donate!")
        return string.Template(content).substitute(sliders="".join(sliders),
                                                   tagline=tagline,
                                                   download_text=download_text,
                                                   donate_text=donate_text,
                                                   donate_title=donate_title,
                                                   donate_button_text=donate_button_text)


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
                _("Freenet is home to webpages with topics ranging from programming to sustainable living.")),
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
                _("No central points of failure, efficient caching of popular content.")),
            service("ion-erlenmeyer-flask", _("Proven"),
                _("Based on solid research and in practical use for 15 years.")),
        ]
        content = """
<!-- service start -->
<div class="row animate-in" data-anim-type="fade-in-up">
$services
<div class="col-sm-12 col-md-12 col-lg-12 scroll-me" style="text-align: center">
<div class="download">

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
<a href="download.html#autostart" class=" btn button-custom btn-custom-two">$download_text</a>
</div>
</div>
</div>
<!-- service end -->
"""
        tagline = _("Share, Chat, Browse. Anonymously.")
        download_text = _("Get Freenet")
        return string.Template(content).substitute(services="".join(services),
                                                   tagline=tagline,
                                                   download_text=download_text)
    
class NewsSection(Section):
    def __init__(self):
        self.slug = "news"
        self.title = _("News")
    def get_content(self):
        # we show the most recent news items
        md_content = ""
        news_items = news.news_items()
        for item in news_items[:min(5, len(news_items))]:
            md_content += item.markdown_link() + "\n\n"
        return text(md(md_content))

class IndexPage(Page):
    def __init__(self):
        self.slug = "index"
        self.title = _("Overview")
        self.sections = [
            HomeSection(),
            ServiceSection(),
            NewsSection(),
            ContactSection()]
