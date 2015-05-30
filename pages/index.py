import string
from common import *

site_brand = "Freenet"

def home():
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
        slider_item(_("Explore the Dark Web"), _("""
                What happens when people get total anonymity?
                Does evil surface? Or are most people inherently good?
                Freenet contains a varied amount of content,
                be careful what links you click though!
            """)),
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
<a href="#services" class=" btn button-custom btn-custom-two">$download_text</a>
</div>
</div>
</div>

</div>

<!--HOME SECTION END-->
"""
    tagline = _("Share, Chat, Browse. Anonymously. On the Free Network.")
    download_text = _("Get Freenet")
    return string.Template(content).substitute(sliders="".join(sliders),tagline=tagline,download_text=download_text)


def service():
    content = """
<!-- service start -->
<div class="row animate-in" data-anim-type="fade-in-up">

<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-person"></i>
        <h3>Secret Identity</h3>
        Create a secret identity so nobody knows who you are.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-earth"></i>
        <h3>Browse Webpages</h3>
        There are a lot of webpages hosted on Freenet.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-chatboxes"></i>
        <h3>Forums</h3>
        Ask questions and exchange ideas.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-edit"></i>
        <h3>Publish</h3>
        Publish information while remaining anonymous.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-android-cloud-done"></i>
        <h3>Share Files</h3>
        Easy upload & download.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-cube"></i>
        <h3>Resistant</h3>
        Freenet has been designed to be resistant to attacks.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-shuffle"></i>
        <h3>Distributed</h3>
        No central points of fallure.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-wifi"></i>
        <h3>Meshable</h3>
        You can use Freenet as a meshnet.
    </div>
</div>
<div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
    <div class="services-wrapper">
        <i class="ion-hammer"></i>
        <h3>Platform</h3>
        Write your own applications on the Freenet platform.
    </div>
</div>


</div>
<!-- service end -->
"""
    return section("services", _("What is Freenet?"), content)

class IndexPage(object):
    slug = "index"
    section = "home"
    title = "Freenet"
    section_link = False
    def generate(self, language, site_menu):
        return html(head(self.title), body(menu(site_menu, self)+home()+service()+contact()))
