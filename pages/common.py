# Copyright Designbootstrap (theme light-wave)
# Copyright Gerard Krol
# License: MIT
import string
import markdown
import re
import settings

# Wrapper for HTML intended to catch markdown-of-html bugs
# The HTML class taints all strings that are added to it to be HTML as well
class HTML(object):
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("HTML text must be of str, {f} found".format(f=text.__class__.__name__))
        self.text = text
    
    def __add__(self, other):
        if isinstance(other, HTML):
            return HTML(self.text + other.text)
        return HTML(self.text + other)
    
    def __radd__(self, other):
        if isinstance(other, HTML):
            return HTML(other.text + self.text)
        return HTML(other + self.text)
    
    def __repr__(self):
        return u"HTML: " + self.text
    
    def __unicode__(self):
        raise AssertionError("Implicitly converting HTML to unicode")
    
    def __str__(self):
        raise AssertionError("Implicitly converting HTML to str")

# Forces the given value to be represented as a unicode string
def force_unicode(val):
    if isinstance(val, str):
        return val
    if isinstance(val, HTML):
        return val.text
    return str(val)

# Forces the given value to be represented as an HTML object
def force_html(val):
    if isinstance(val, HTML):
        return val
    return HTML(force_unicode(val))

# Concatenates the given list of values into a HTML object
def concat_html(vals):
    if not isinstance(vals, list):
        raise TypeError
    return HTML(u"".join(map(force_unicode, vals)))

# Template substitution with HTML support. Substitutes the placeholders in the first argument
# string with the named values in the kwargs into a HTML object
def substitute_html(*args, **kwargs):
    if len(args) is not 1:
        raise TypeError("substitute_html() takes exactly one template argument ({n} given)".format(n=len(args)))
    template = args[0]
    kwargs = {k: force_unicode(v) for k, v in kwargs.items()}
    return HTML(string.Template(force_unicode(template)).substitute(**kwargs))

# Wrapper for markdowned text intended for catching double-markdown bugs
class Markdown(HTML):
    def __add__(self, other):
        if isinstance(other, Markdown):
            return Markdown(HTML(self) + HTML(other))
        return super(Markdown, self).__add__(other)
    
    def __radd__(self, other):
        if isinstance(other, Markdown):
            return Markdown(HTML(other) + HTML(self))
        return super(Markdown, self).__radd__(other)

# Shorter way to encode markdown, also strips leading and trailing whitespace
def md(text):
    if isinstance(text, Markdown):
        raise ValueError("Attempting to markdown already markdowned text")
    if isinstance(text, HTML):
        raise ValueError("Attempting to markdown HTML text")
    return Markdown(markdown.markdown(force_unicode(text)))
    
class Section(object):
    # slug, title, content
    direct_link = None # put a link in this variable to link directly to an external page
    def generate(self):
        return section(self.slug, self.title, self.get_content())

class Page(object):
    # slug, title
    hidden = False
    sections = []
    first_section_in_menu = False
    def generate(self, language, site_menu):
        section_content = concat_html([x.generate() for x in self.sections if not x.direct_link])
        return html(head("Freenet - " + self.title), body(menu(site_menu, self) + section_content))
    
def html(head, body):
    template = """
<!DOCTYPE html>
<html lang="en" class="no-js" >
$head
$body
</html>
"""
    return substitute_html(template, head=head, body=body)

def head(title):
    template = """
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<meta name="description" content="" />
<meta name="author" content="" />

<!-- Favicons start -->
<!-- generated by realfavicongenerator.net -->
<link rel="apple-touch-icon" sizes="57x57" href="assets/img/favicons/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="assets/img/favicons/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="assets/img/favicons/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="assets/img/favicons/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="assets/img/favicons/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="assets/img/favicons/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="assets/img/favicons/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="assets/img/favicons/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/img/favicons/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" href="assets/img/favicons/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="assets/img/favicons/favicon-194x194.png" sizes="194x194">
<link rel="icon" type="image/png" href="assets/img/favicons/favicon-96x96.png" sizes="96x96">
<link rel="icon" type="image/png" href="assets/img/favicons/android-chrome-192x192.png" sizes="192x192">
<link rel="icon" type="image/png" href="assets/img/favicons/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="assets/img/favicons/manifest.json">
<link rel="shortcut icon" href="assets/img/favicons/favicon.ico">
<meta name="msapplication-TileColor" content="#2b5797">
<meta name="msapplication-TileImage" content="assets/img/favicons/mstile-144x144.png">
<meta name="msapplication-config" content="assets/img/favicons/browserconfig.xml">
<meta name="theme-color" content="#ffffff">
<!-- favicons end -->

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
<!-- CUSTOM CSS -->
<link href="assets/css/style-freenet-4.css" rel="stylesheet" />
<!-- SLICK CAROUSEL -->
<!-- Kept in one directory instead of split to stay with upstream. -->
<link rel="stylesheet" type="text/css" href="assets/slick/slick.css"/>
<link rel="stylesheet" type="text/css" href="assets/slick/slick-theme.css"/>
<!-- HTML5 Shiv and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
<script src="assets/js/html5shiv.js"></script>
<script src="assets/js/respond.min.js"></script>
<![endif]-->

</head>
"""
    return substitute_html(template, title=title)
    
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
<script src="assets/js/jquery.easing.min.js"></script>
<!-- ISOTOPE SCRIPTS -->
<script src="assets/js/jquery.isotope.js"></script>
<!-- VIEWPORT ANIMATION SCRIPTS   -->
<script src="assets/js/appear.min.js"></script>
<!-- CUSTOM SCRIPTS -->
<script src="assets/js/custom.js"></script>
<!-- SLICK CAROUSEL -->
<script type="text/javascript" src="assets/slick/slick.min.js"></script>

</body>
"""
    return substitute_html(template, content=content)

def menu(site_menu, current_page):
    menu_content = "";
    menu_template = """<li><a href="$filename#$section">$title</a></li>"""
    for page in site_menu:
        if page.hidden: continue
        filename = page.slug + ".html"
        if page.slug == current_page.slug:
            filename = ""
        section = ""
        if not page.first_section_in_menu:
            section = page.sections[0].slug
        menu_content += substitute_html(menu_template, filename=filename, section=section, title=page.title.upper())
    submenu_content = ""
    if current_page.first_section_in_menu:
        skip = 0
    else:
        skip = 1
    submenu_template = """<li><a href="$link">$title</a></li>"""
    submenu_content = concat_html([
        substitute_html(submenu_template, link=(section.direct_link or "#" + section.slug), title=section.title.upper())
        for section in current_page.sections[skip:]])
    language_template = """<li><a href="?language=$language">$title</a></li>"""
    languages = concat_html([
        substitute_html(language_template, language=language, title=language.upper())
        for language in settings.languages])
    template = """
<!--MENU SECTION START-->
<div class="navbar navbar-inverse navbar-fixed-top" id="menu-section" >
<div class="container">


<div class="navbar-header">
<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>

<div class="navbar-brand">
    <a href="index.html">
        <img src="assets/img/logo_65_49.png" style="height: 2em;" alt="$rabbit"/>
        $brand
    </a>
</div>
</div>

<!-- languages -->
<div class="navbar-collapse collapse navbar-language">
<ul class="nav navbar-nav navbar-nav-language navbar-right">

$languages

</ul>
</div>


<div class="navbar-collapse collapse">
    <ul class="nav navbar-nav navbar-nav-page navbar-right">
        $menu_content
    </ul>
</div>

<div class="navbar-collapse collapse">
<ul class="nav navbar-nav navbar-right">

$submenu_content

</ul>
</div>

</div>
</div>
<!--MENU SECTION END-->
"""
    return substitute_html(template,
        brand="FREENET", rabbit=_("Freenet rabbit logo"),
        menu_content=menu_content, submenu_content=submenu_content,
        languages=languages
    )

class ContactSection(Section):
    def __init__(self):
        self.slug = "contact"
        self.title = _("Contact")
    def get_content(self):
        template = """
<div class="row">

<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
<div class="contact-wrapper">
<h3>Contact</h3>
<h4><strong>$press </strong><span class="e-mail" data-user="sserp" data-website="gro.tcejorpteneerf"></span></h4>
<h4><strong>$support </strong> support@freenetproject.org </h4>
<h4><strong>$irc </strong> $irc_value</h4>
</div>

</div>
<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">
<div class="contact-wrapper">
<h3>$license_header</h3>
$license
<div class="footer-div" >
&copy; 2015 The Freenet Project Inc<br/>
<a href="http://www.designbootstrap.com/" target="_blank" >$design</a>
</div>
</div>

</div>
"""
        return substitute_html(template,
            press=_("Press:"),
            support=_("Support:"),
            irc=_("IRC:"),
            irc_value=_("{irc_channel} on {irc_server}").format(irc_channel="#freenet", irc_server="chat.freenode.net"),
            license_header=_("License"),
            license=_("Content on this website is licensed under the GNU Free Documentation License and may be available under other licenses."),
            design=_("Design by DesignBootstrap")
            )


def section(name, title, content):
    template = """
<!--section $name start-->
<section id="$name" >
<div class="container">
<div class="row text-center header">
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">

<h3>$title</h3>
<hr />
</div>
</div>

$content

</section>
<!-- section $name end -->
"""
    return substitute_html(template, name=name, title=title, content=content)

def text(content):
    template = """
<!-- text start -->
<div class="row">
<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
$content
</div>
</div>
<!-- text end -->
"""
    return substitute_html(template, content=content)
