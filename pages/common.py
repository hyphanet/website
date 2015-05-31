# Contains parts of the Designbootstrap theme light-wave
# License: MIT
import string
import markdown
import re

def md(text):
    return markdown.markdown(text.strip())
    
def html(head, body):
    template = """
<!DOCTYPE html>
<html lang="en" class="no-js" >
$head
$body
</html>
"""
    return string.Template(template).substitute(head=head, body=body)

def head(title):
    template = """
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<meta name="description" content="" />
<meta name="author" content="" />
<!--[if IE]>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<![endif]-->
<title>$title</title>
<!-- BOOTSTRAP CORE CSS -->
<link href="assets/css/bootstrap.css" rel="stylesheet" />
<!-- ION ICONS STYLES -->
<link href="assets/css/ionicons.css" rel="stylesheet" />
<!-- FONT AWESOME ICONS STYLES -->
<link href="assets/css/font-awesome.css" rel="stylesheet" />
<!-- FANCYBOX POPUP STYLES -->
<link href="assets/js/source/jquery.fancybox.css" rel="stylesheet" />
<!-- STYLES FOR VIEWPORT ANIMATION -->
<link href="assets/css/animations.min.css" rel="stylesheet" />
<!-- CUSTOM CSS -->
<link href="assets/css/style-freenet.css" rel="stylesheet" />
<!-- HTML5 Shiv and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
<script src="assets/js/html5shiv.js"></script>
<script src="assets/js/respond.min.js"></script>
<![endif]-->
</head>
"""
    return string.Template(template).substitute(title=title)
    
def body(content):
    template = """    
<body data-spy="scroll" data-target="#menu-section">
$content

<!-- JAVASCRIPT FILES PLACED AT THE BOTTOM TO REDUCE THE LOADING TIME -->
<!-- CORE JQUERY -->
<script src="assets/js/jquery-1.11.1.js"></script>
<!-- BOOTSTRAP SCRIPTS -->
<script src="assets/js/bootstrap.js"></script>
<!-- EASING SCROLL SCRIPTS PLUGIN -->
<script src="assets/js/vegas/jquery.vegas.min.js"></script>
<!-- VEGAS SLIDESHOW SCRIPTS -->
<script src="assets/js/jquery.easing.min.js"></script>
<!-- FANCYBOX PLUGIN -->
<script src="assets/js/source/jquery.fancybox.js"></script>
<!-- ISOTOPE SCRIPTS -->
<script src="assets/js/jquery.isotope.js"></script>
<!-- VIEWPORT ANIMATION SCRIPTS   -->
<script src="assets/js/appear.min.js"></script>
<script src="assets/js/animations.min.js"></script>
<!-- CUSTOM SCRIPTS -->
<script src="assets/js/custom.js"></script>

</body>
"""
    return string.Template(template).substitute(content=content)

def menu(site_menu, current_page):
    menu_content = "";
    for page in site_menu:
        filename = page.slug + ".html"
        if page.slug == current_page.slug:
            filename = ""
        menu_content += string.Template("""<li><a href="$filename#$section">$title</a></li>""").substitute(filename=filename,section=page.section,title=page.title.upper())
    
    template = """
<!--MENU SECTION START-->
<div class="navbar navbar-inverse navbar-fixed-top scroll-me" id="menu-section" >
<div class="container">
<div class="navbar-header">
<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="#">

$brand

</a>
</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav navbar-right">

$menu_content

</ul>
</div>

</div>
</div>
<!--MENU SECTION END-->
"""
    return string.Template(template).substitute(brand="FREENET", menu_content=menu_content)

def contact():
    return """
<!--CONTACT SECTION START-->
<section id="contact" >
<div class="container">
<div class="row text-center header animate-in" data-anim-type="fade-in-up">
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">

<h3>Contact Details </h3>
<hr />

</div>
</div>

<div class="row animate-in" data-anim-type="fade-in-up">

<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
<div class="contact-wrapper">
<h3>Quick Contact</h3>
<h4><strong>Press : </strong> press%freenetproject.org </h4>
<h4><strong>Site : </strong> support%freenetproject.org </h4>
<h4><strong>IRC : </strong> #freenet at freenode.org </h4>
</div>

</div>
<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
<div class="contact-wrapper">
<h3>Website</h3>
This website is licensed under the GNU Free Documentation License
<div class="footer-div" >
&copy; 2015 Freenet <br/>
<a href="http://www.designbootstrap.com/" target="_blank" >Design by DesignBootstrap</a>
</div>
</div>

</div>

</div>


</div>
</section>
<!--CONTACT SECTION END-->
"""

def section(name, title, content):
    template = """
<!--section $name start-->
<section id="$name" >
<div class="container">
<div class="row text-center header animate-in" data-anim-type="fade-in-up">
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">

<h3>$title</h3>
<hr />
</div>
</div>

$content

</section>
<!-- section $name end -->
"""
    return string.Template(template).substitute(name=name, title=title,content=content)

def text(content):
    template = """
<!-- text start -->
<div class="row animate-in" data-anim-type="fade-in-up">
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
$content
</div>
</div>
<!-- text end -->
"""
    return string.Template(template).substitute(content=content)
