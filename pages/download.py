# Python code copyright Gerard Krol, license: MIT
import string
import markdown
from .common import *

def div(name, content):
    return """<div id="{}">{}</div>""".format(name, content)
    
def show_hide_script():
    # License: GFDL (from old freenetproject.org website)
    return """
    <script type="text/javascript">
        function getStyleByElementByID(whichDivId)
        {
            var elem;
            if( document.getElementById ) // this is the way the standards work
                elem = document.getElementById( whichDivId );
            else if( document.all ) // this is the way old msie versions work
                elem = document.all[whichDivId];
            else if( document.layers ) // this is the way nn4 works
                elem = document.layers[whichDivId];
            return elem.style;
        }

        function hideDiv( whichDivId )
        {
            getStyleByElementByID(whichDivId).display = 'none';
        }
        function showDiv( whichDivId )
        {
            getStyleByElementByID(whichDivId).display = 'inline';
        }
    </script>
"""

def run_show_hide_script():
    # License: GFDL (from old freenetproject.org website)
    return """
      <script type="text/javascript">
         // Try to detect if Java 1.6.0 or higher is installed
         //var Java = PluginDetect.isMinVersion('Java', '1,6,0');
         
         // Os detection
         var OSName="";
         if (navigator.appVersion.indexOf("Win")!=-1)
            OSName="windows";
         else if (navigator.appVersion.indexOf("Mac")!=-1)
            OSName="macos";
         else if (navigator.appVersion.indexOf("X11")!=-1)
            OSName="unix";
         else if (navigator.appVersion.indexOf("Linux")!=-1)
            OSName="unix";
         
         hideDiv("windows");
         hideDiv("macos");
         hideDiv("unix");
         if (OSName != "") {
           showDiv(OSName);
         } else {
           showDiv("windows");
           showDiv("macos");
           showDiv("unix");
         }
         
         // Below part Copyright Gerard Krol, licensed MIT
         function download(url) {
            document.write('<iframe width="1" height="1" frameborder="0" src="'+url+'"></iframe>');
         }
         
         var hash = window.location.hash.substring(1);
         if (hash == "autostart") {
            if (OSName == "windows") {
                download('assets/jnlp/FreenetInstaller.exe');
            }
            if (OSName == "unix") {
                download('assets/jnlp/freenet.jnlp');
            }
         }
      </script>
"""

class DownloadSection(Section):
    def __init__(self):
        self.title = _("Download")
        self.slug = "download"
    def get_content(self):
        # License for all content in this section: GFDL (from old freenetproject.org website)
        return show_hide_script()+text("<a name=\"autostart\" class=\"anchor\"></a>"+md(_("""
[Step by step guide](http://freesocial.draketo.de/) to setting up Freenet and
various Freenet apps. Please try this, especially if installing on OS X. We
are not responsible for unofficial third party apps it recommends (including
FMS), but many Freenet users and developers use them.
"""))+
_("Show instructions for:")+"""
      <a href="javascript:showDiv('windows');hideDiv('macos');hideDiv('unix');">Windows
        </a>, <a href="javascript:hideDiv('windows');showDiv('macos');hideDiv('unix');">OS X
        </a>, <a href="javascript:hideDiv('windows');hideDiv('macos');showDiv('unix');">GNU/Linux & POSIX
        </a><br>
"""+div("windows",md(_("""
### Windows

Download and run [the installer](assets/jnlp/FreenetInstaller.exe)
([try this if the first link is blocked](https://downloads.freenetproject.org/latest/FreenetInstaller.exe))

It will automatically install Freenet and other required components for you.
When done, your default browser will automatically open up to Freenet's
web-based user interface. (Freenet contains **NO spyware or adware** ,
it's Free Software! The source code is publicly available for review)

Freenet requires Windows XP or later.
""")))+div("macos",md(_("""
### OS X

[Install Freenet 0.7](assets/jnlp/freenet.jnlp) using Java Web Start.  
This requires that Java is installed and that Java Web Start is enabled. If
it doesn't work, try [installing Java](http://www.java.com/),
then downloading [the installer](assets/jnlp/freenet_installer.jar) and
opening it. It might take a moment to launch.

**Note:** Mavericks does not ship with Java Web Start enabled. We would like
to make a _.dmg_ for easier OS X installation but don't know how yet. If you
are a developer and would like to join us and help it would be much
appreciated!
""")))+div("unix",md(_("""
### GNU/Linux & POSIX

Try the [Java Web Start installer](assets/jnlp/freenet.jnlp). If it doesn't
work:

You need to have a recent **Java Runtime Environment** (JRE). We have
experienced best results with Oracle's Java Runtime Environment which can be
obtained via your [package manager](
https://en.wikipedia.org/wiki/Package_manager) or from [
http://www.java.com/](http://www.java.com/).

Java version 1.6 or higher is required, and 1.7 or higher is strongly
recommended. You should keep Java up to date to avoid problems and for better
performance.

Open a terminal and run:
""") + "\n\n" + """
    wget 'https://freenetproject.org/assets/jnlp/freenet_installer.jar' -O new_installer_offline.jar
    java -jar new_installer_offline.jar
""" + "\n\n" + _("""
Alternatively, downloading [the installer](assets/jnlp/freenet_installer.jar)
([gpg signature](https://downloads.freenetproject.org/alpha/installer/new_installer_offline_1467.jar.sig))
and then clicking on the file may work on some systems, but if there are
problems we recommend the above command lines. If wget is not installed,
it can be installed with a package manager, such as sudo apt-get install wget
on Debian or Ubuntu.

If the link above is blocked, you could download it from our server
[here](https://downloads.freenetproject.org/latest/new_installer_offline.jar).
But please use the other link if you can.

**Note:** Many GNU/Linux distributions no longer ship with Java Web Start
enabled. We would like to make distribution packages for easier installation,
and have an in-development (and not maintained) [Debian package](
https://github.com/freenet/debian), but haven't gotten it stable or made
official ones for other distributions. If you are a developer and would like
to join us and help it would be much appreciated!

If this doesn't work on a headless server, try
"java -jar new_installer_offline.jar -console", and follow the prompts to
tell it where to install Freenet etc.
""") + "\n\n" + """
<a class="anchor" name="mirrored"></a>""" + "\n\n" + _("""
### Mirrored installation

If you have a working Freenet installation directory that you have mirrored
from one Unix machine to another (e.g. via rsync or unison), enabling the
mirrored installation is not difficult. Nothing in a Freenet installation
cares about its host's IP address; it can't, or Freenet would fail on
machines that get IP addresses from a DHCP pool.

All you actually need to do is tell the system you've mirrored to that it
should start the Freenet proxy daemon for you on boot. Do <tt>crontab -l</tt>
on the source machine, find the line that is tagged "FREENET AUTOSTART" and
add that to your crontab on the mirrored machine.

However: each installation has a unique identity key generated at
installation time. If you try to run two instances with the same identity _at
the same time_, both proxy demons will become confused and upset. Don't do
this!

### HOWTO

You might find the
[Freenet Social Networking Guide](http://freesocial.draketo.de/index.html)
useful.
""")))+run_show_hide_script()+md(_("""
### Firewalls and routers

Freenet should work fine with most routers, but if you are having problems
and you have a firewall or router, click [**here**](help.html#firewall) for
some info.
""") + "\n\n" + _("""
### So it's running, what do I do?

When the installer closes, it should open a browser window pointing to the
first-time wizard. Here you can configure basic settings, and then start
using Freenet. You can access Freenet later on via the system tray menu (
bottom right on the screen), or use the Browse Freenet shortcut on the
desktop and/or start menu. If it doesn't work, open
[http://127.0.0.1:8888/](http://127.0.0.1:8888/) in your web browser.

For best security you should use a separate browser for Freenet, preferably
in privacy mode. On Windows, the system tray menu will try to use Chrome in
incognito mode if possible. Internet Explorer does not work well with
Freenet, Firefox and Opera are widely used.

If you know anyone running Freenet, you can improve your security and help to
build a robust network by connecting to their node. First, open the [Add a
friend page](http://127.0.0.1:8888/addfriend/). You and your friend should
each download their "node reference". Send the file to the other person,
and add his node reference using the form at the bottom of the page. When
both are added, your friend's node should show up on the Friends page,
probably as "CONNECTED" or "BUSY". You can set a name for your node on the
config page to make it easier to see who it is. Only add nodes run by people
**you actually know**, whether online or offline, as adding total strangers
harms performance and does not improve security much (they could be the bad
guys!).
""") + "\n\n" + _("""
### So I'm connected, what do I do?

Freenet itself includes anonymous websites ("freesites"), filesharing,
searching, and more, but you can also use third party applications for chat,
filesharing, to help you upload freesites, etc.

The [Freenet Social Networking Guide](http://freesocial.draketo.de/) explains
how to set up the main third party tools, including email, forums and
micro-blogging (Sone, a bit like twitter).
""") + "\n\n" + _("""
### It doesn't work, now what?

If you have problems installing or running Freenet, please contact us on [the
support list](mailto:support@freenetproject.org) ([subscribe here](
help.html#mailing-lists)), or join us on IRC on the #freenet channel on
irc.freenode.net (try [here](
https://webchat.freenode.net/?randomnick=1&channels=freenet)).
""") + "\n\n" + _("""
### Hardware requirements

Generally a 1GHz processor and 1GB of RAM should be fine. Freenet will run on
smaller systems, but it uses at least 128MB of RAM, so unless the system does
nothing else it will struggle in less than 512MB. However, the processor is
less of a problem, people have been known to run it on 400MHz Pentium 2's or
ATOM's, although downloads and browsing would be slow.

Freenet will use a portion of your disk for storing data, you can configure
this to any size from 100MB upwards, but we recommend at least 1GB. Freenet
also uses disk space for your downloads. Freenet's memory usage is
approximately 256MB plus 400kB for every 2GB of datastore.

On 64-bit Windows, we will install a 32-bit Java Virtual Machine because of
limitations of the [Java Service Wrapper](
http://wrapper.tanukisoftware.org/doc/english/download.jsp).
""") + "\n\n" + _("""
### Upgrading

Freenet provides an update-over-freenet mechanism: It will keep itself up to
date automatically from other Freenet nodes, and this will normally work even
if it is unable to route to them due to them being too new. This is anonymous
and secure, and we recommend people use it. However, if something is severely
broken, you can update your node manually from our servers:

* Windows users can upgrade to the latest-stable Freenet release from the
  system tray menu, or by running "update.cmd" in the Freenet directory.
* OS X, GNU/Linux, or other POSIX users may upgrade by running the update.sh
  shell script in the Freenet directory.

**Source Code:** See [the GitHub repository](https://github.com/freenet/fred).
""")))

class NoteSection(Section):
    def __init__(self):
        self.slug = "note"
        self.title = _("Important note for first time users")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
For best performance, Freenet will run continually. It should
not interfere with your computer usage, as it requires around 
200MB of RAM and 10%% of one CPU core, plus some disk access. We 
strongly recommend you shut down Freenet while playing computer 
games etc. On Windows you can do this from the system tray icon, 
on other systems use the links on the system menu or the desktop.
""") + "\n\n" + _("""
Normally Freenet will connect automatically and should "just work",
automatically connecting to other nodes (Strangers). However,
if you know several people who are already using Freenet, you can
enable high security mode and 
[add them as Friends](http://127.0.0.1:8888/addfriend/").
so Freenet will only connect to them, making your usage of Freenet 
almost undetectable, while still being able to access the rest of the
network through their friends' friends etc. This will be slower unless 
you add 10+ friends who are usually online when you are.
""")))

class DownloadPage(Page):
    def __init__(self):
        self.slug = "download"
        self.title = _("Download")
        self.sections = [
            NoteSection(),
            DownloadSection(),
            ]
