import string
from common import *

site_brand = "Freenet"

def home():
    def slider_item(title, text):
        template = """
<div class="carousel-inner">
<div class="item active">
    <h3>
        $title
    </h3>
    <p>
        $text
    </p>
</div>
"""
        return string.Template(template).substitute(title=title, text=text)
    return """
<!--HOME SECTION START-->
<div id="home" >
<div class="container">
<div class="row">
<div class="col-sm-8 col-sm-offset-2 col-md-8 col-md-offset-2 col-lg-8 col-lg-offset-2 ">
<div id="carousel-slider" data-ride="carousel" class="carousel slide  animate-in" data-anim-type="fade-in-up" data-interval="8000">

<div class="carousel-inner">
<div class="item active">
    <h3>
        Avoid Censorship
    </h3>
    <p>
        Freenet allows you to freely share information<br/>
        without any person, organization or country able<br/>
        to block it. Freenet helps you to remain anonymous.<br/>
        This allows you to communicate without fear.<br/>
    </p>
</div>
<div class="item">
    <h3>
        Improve the World
    </h3>
    <p>
        By using Freenet from the "free world" you<br/>
        help people in oppressive regimes share information.<br/>
        The more people use Freenet the easier it will<br/>
        be to obtain. Using it will also be less suspicious.<br/>
    </p>
</div>
<div class="item">
    <h3>
        Save your (Childrens) Future
    </h3>
    <p>
        Even if you live in a democratic country a dictator<br/>
        needs only a few years to grab power.<br/>
        Are you prepared?<br/>
        Having experience with using Freenet might save lives!
    </p>
</div>
<div class="item">
    <h3>
        Explore the Dark Web
    </h3>
    <p>
        What happens when people get total anonymity?<br/>
        Does evil surface? Or are most people inherently good?<br/>
        Freenet contains a varied amount of content,<br/>
        be careful what links you click though!
    </p>
</div>
<div class="item">
    <h3>
        Meet New People
    </h3>
    <p>
        People from all over the world use Freenet to<br/>
        communicate. Granted, most of this could be done<br/>
        fine over the open internet.<br/>
        These pioneers however help us test the system.
    </p>
</div>
<div class="item">
    <h3>
        Experiment with Exciting New Technology
    </h3>
    <p>
        Freenet is on the cutting edge of distributed<br/>
        routing research. The data storage provided<br/>
        by Freenet is a proving ground for a number<br/>
        of new distributed systems.
    </p>
</div>
<div class="item">
    <h3>
        Host a Website
    </h3>
    <p>
        Need a website nobody can take over? That<br/>
        is hosted for free? That is very resistant<br/>
        to attacks?<br/>
        Just publish it on Freenet!
    </p>
</div>
<div class="item">
    <h3>
        Share Files
    </h3>
    <p>
        Dropbox?<br/>
        No need, just upload the file to Freenet and<br/>
        a few minutes later anyone with the secret URL<br/>
        can access it!
    </p>
</div>

</div>


</div>


</div>
</div>
<div class="row animate-in" data-anim-type="fade-in-up">
<div class="col-sm-6 col-sm-offset-3 col-md-6 col-md-offset-3 col-lg-8 col-lg-offset-2 scroll-me">


<p >
Share, Chat, Browse. Anonymously. On the Free Network.
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
<a href="#services" class=" btn button-custom btn-custom-two">Get Freenet</a>
</div>
</div>
</div>

</div>

<!--HOME SECTION END-->
"""

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
    return section("services", "What is Freenet?", content)

class IndexPage(object):
    slug = "index"
    def generate(language):
        return html(head("Freenet"), body(menu()+home()+service()+contact()))
