# Python code copyright Gerard Krol, license: MIT
# HTML copyright DesignBootstrap, Gerard Krol, license: MIT
import pages.news as news
from pages.common import *

class HomeSection(Section):

    def __init__(self):
        self.slug = "home"
        self.title = ""

    def generate(self):
        content = """
<!--HOME SECTION START-->
<section id="home">
    <div class="container">
        <div class="row text-center">
            <div class="col-sm-2 col-md-2 col-lg-2 hidden-xs">
                <div class="item active sidebar" id="suma_award_notice">
                    <p><a href="news.html#20150211"><img src="assets/img/suma2015_badge_transparent_3.png" alt="SUMA Award 2014/15" /></a></p>
                </div>
            </div>

            <div class="col-sm-8 col-md-8 col-lg-8">
                <div class="row">
                    <div id="home-logo">
                        <img src="assets/img/rabbit/freenet-bunny-with-name-flying.png" alt="Freenet Logo, leap over censorship"/><br />
                    </div>
                    <div id="home-slogan" class="h3">
                        $md__slogan
                    </div>
                    <div id="home-mission">
                        $md__mission
                    </div>
                    <div id="home-download" class="download">
                        <a href="download.html#autostart" class=" btn button-custom btn-custom-two">
                            <i class="icon ion-arrow-down-a"></i>
                            $str__download_text
                        </a>
                    </div>
                </div>
            </div>
        </div>
                        <div class="social">
                        <a href="https://twitter.com/freenetproject" class="btn button-custom btn-custom-one" ><i class="fa fa-twitter"></i></a>
                        <a href="https://github.com/freenet/fred" class="btn button-custom btn-custom-one" ><i class="fa fa-github "></i></a>
                        </div>

    </div>
</section>
<!--HOME SECTION END-->
"""
        slogan = md(_("""
Leap over censorship<br>
Escape total surveillance
"""))
        mission = md(_("""
Freenet is a peer-to-peer platform for censorship-resistant communication and publishing.
Browse websites, post on forums, and publish files within Freenet with strong privacy protections.
"""))
        download_text = _("Download Freenet")
        read_more = """<a href="{}" class="readmore">""" + _("""read more…""") + """</a>"""
        donate_text = md(_("Help keep Internet freedom alive and expand human liberty! Support another year of paid development. [Learn more about our fundraiser.][url_fundraiser]") + "\n\n" + "[url_fundraiser]: news.html#20151212-donation-appeal")
        donate_button_text = _("Donate!")
        donation_target = "27500"
        nonprofit = _("The Freenet Project Inc is a non-profit 501(c)(3) organization.")
        tax_deductable = _("""Donations are tax-deductible.""")
        return substitute_html(content,
            md__slogan=slogan,
            md__mission=mission,
            str__download_text=download_text,
            md__donate_text=donate_text,
            str__donate_button_text=donate_button_text,
            str__donation_target=donation_target,
            str__nonprofit=nonprofit,
            str__tax_deductable=tax_deductable,
            str__503_read_more=read_more.format("donate.html#fpi"),
        )


class ServiceSection(Section):
    def __init__(self):
        self.slug = "services"
        self.title = _("What is Freenet?")
    def get_content(self):
        def service(icon, title, text, link):
            content = """
<a href="$str__link">
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="$str__icon"></i>
        <h3>$str__title</h3>
        $str__text
    </div>
</div>
</a>
"""
            return substitute_html(content,
                str__icon=icon, str__title=title, str__text=text, str__link=link,
            )
        services = [
             # Services items copyright Gerard Krol, licensed GFDL/CC-BY-SA 4.0/GPLv2+
            service("ion-person", _("Secret Identity"),
                    _("Create a secret identity so nobody knows who you are."),
                    "https://wiki.freenetproject.org/Web_of_Trust"),
            service("ion-earth", _("Browse Websites"),
                    _("Freenet is home to sites ranging from programming to sustainable living."),
                    "https://wiki.freenetproject.org/Using_Freenet#Browsing_.26_Communicating_on_Freenet"),
            service("ion-chatboxes", _("Forums"),
                    _("Ask questions and exchange ideas."),
                    "https://wiki.freenetproject.org/Using_Freenet#Browsing_.26_Communicating_on_Freenet"),
            service("ion-edit", _("Publish"),
                    _("Publish anonymously without need for a server."),
                    "documentation.html#jsite"),
            service("ion-android-cloud-done", _("Share Files"),
                    _("Easy upload & download."),
                    "help.html#find"),
            service("ion-hammer", _("Platform"),
                    _("Write your own applications on the Freenet platform."),
                    "https://wiki.freenetproject.org/FCPv2"),
            service("ion-cube", _("Resistant"),
                    _("Freenet has been designed to be resistant to attacks and censorship."),
                    "documentation.html#content"),
            service("ion-shuffle", _("Distributed"),
                    _("No central points of failure, efficient caching of popular content."),
                    "documentation.html#understand"),
            service("ion-erlenmeyer-flask", _("Proven"),
                    _("Based on solid research and in practical use for 15 years."),
                    "about.html#papers"),
        ]
        content = """
<!-- service start -->
<div class="row">
    $html__services
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12" style="text-align: center">
        <div class="download">
        <p>$str__tagline</p>
        <a href="download.html#autostart" class=" btn button-custom btn-custom-two">
            <i class="icon ion-arrow-down-a"></i>
            $str__download_text
        </a>
        </div>
    </div>
</div>
<!-- service end -->
"""
        tagline = _("Share, Chat, Browse. Anonymously.")
        download_text = _("Download Freenet")
        return substitute_html(content,
            html__services=concat_html(services),
            str__tagline=tagline,
            str__download_text=download_text)

class NewsSection(Section):
    def __init__(self):
        self.slug = "news"
        self.title = _("Latest News")
    def get_content(self):
        # we show the most recent news items
        content = """
<div class="news-wrapper">
$md__items
</div>
"""
        md_content = ""
        news_items = news.news_items()
        for item in news_items[:min(5, len(news_items))]:
            md_content += item.markdown_link() + "\n\n"
        return substitute_html(content, md__items=md(md_content))

class IndexPage(Page):
    def __init__(self):
        self.slug = "index"
        self.title = _("Overview")
        self.sections = [
            HomeSection(),
            ServiceSection(),
            NewsSection(),
            ContactSection()]
