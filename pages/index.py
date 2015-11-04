# Python code copyright Gerard Krol, license: MIT
# HTML copyright DesignBootstrap, Gerard Krol, license: MIT
import pages.news as news
from pages.common import *

class HomeSection(Section):

    def __init__(self):
        self.slug = "home"
        self.title = ""

    def generate(self):
        def slider_item(title, text, active=""):
            template = """
    <div class="item $str__active">
        <h3>$str__title</h3>
        $md__text
    </div>
    """
            return substitute_html(template,
                str__title=title,
                md__text=md(text),
                str__active=active)

        sliders = [
            # Slider items copyright Gerard Krol, licensed GFDL/CC-BY-SA 4.0/GPLv2+
            slider_item(_("Avoid Censorship"), _("""
Freenet is a platform for censorship-resistant communication and publishing.
It helps you to remain anonymous, and communicate without fear.
"""), "active"),
            slider_item(_("Host a Website"), _("""
Need a website nobody can take over? That is hosted for free? That is very
resistant to attacks? Publish it on Freenet!
""")),
            slider_item(_("Share Files"), _("""
Upload a file to Freenet and anyone with the secret URL can access it.
""")),
            slider_item(_("Meet New People"), _("""
People from all over the world use Freenet to communicate. Some of them do so
anonymously. You might never hear their voices in the open.
""")),
            slider_item(_("Experiment with Exciting New Technology"), _("""
Freenet is on the cutting edge of distributed routing research. The data
storage provided by Freenet is a proving ground for a number of new
distributed systems.
""")),
            slider_item(_("Improve the World"), _("""
By using Freenet from the "free world" you help people in oppressive regimes
share information. The more people use Freenet the easier it will be to
obtain. Using it will also be less suspicious.
""")),
        ]
        content = """
<!--HOME SECTION START-->
<section id="home">
    <div class="container">
        <div class="row">
            <!--DONATE SUBSECTION -->
            <div class="col-sm-12 col-md-12 col-lg-12">
                <div class="item active donate" id="donate_button">
                     $md__donate_text
                     <div class="meter blue" id="donate_bar_small">
                         <div class="quantity" style="left: 15px;">$$MONEYBALANCE</div>
                         <div class="quantity" style="right: 15px;">$$$str__donation_target</div>
                         <span style="width: calc(MONEYBALANCE / $str__donation_target * 100%)">
                         </span>
                     </div>
                     <script type="text/javascript">
                         fund_percentage = (MONEYBALANCE / $str__donation_target);
                         if(fund_percentage <= 1/3) {
                             donate_bar = document.getElementById("donate_bar_small");
                             donate_bar.className = "meter red";
                         }
                     </script>
                     <a class="btn button-custom btn-custom-two donate-button" href="donate.html">$str__donate_button_text</a>
                </div>
            </div>
            <!-- DONATE SUBSECTION END -->
        </div>
        <div class="row text-center">
            <div class="col-sm-2 col-md-2 col-lg-2">
                <div class="item active sidebar" id="suma_award_notice">
                    <p><a href="news.html#20150211"><img src="assets/img/suma2015_badge_transparent_3.png" alt="SUMA Award 2014/15" /></a></p>
                </div>
            </div>

            <div class="col-sm-8 col-md-8 col-lg-8">
                <div class="row">
                    <div id="carousel-slider">
                        <div class="carousel-inner">
                            $html__sliders
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="download">
                        <p>$str__tagline</p>
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
                            $str__download_text
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!--HOME SECTION END-->
"""
        tagline = _("Share, Chat, Browse. Anonymously.")
        download_text = _("Download Freenet")
        donate_text = md(_("""
We are raising funds so we can continue paying our developer for another year.
        """))
        donate_button_text = _("Donate!")
        donation_target = "27500"
        return substitute_html(content,
            html__sliders=concat_html(sliders),
            str__tagline=tagline,
            str__download_text=download_text,
            md__donate_text=donate_text,
            str__donate_button_text=donate_button_text,
            str__donation_target=donation_target)

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
    <div class="col-sm-12 col-md-12 col-lg-12" style="text-align: center">
        <div class="download">
        <p>$str__tagline</p>
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
