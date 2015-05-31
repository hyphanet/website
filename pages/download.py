# License: GFDL
import string
import markdown
from common import *

def content():
    return _("""
<div id="content">
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
          
      <h3>Important note for first time users</h3>
      <p>
    For best performance, Freenet will run continually. It should
    not interfere with your computer usage, as it requires around 
    200MB of RAM and 10% of one CPU core, plus some disk access. We 
    strongly recommend you shut down Freenet while playing computer 
    games etc. On Windows you can do this from the system tray icon, 
    on other systems use the links on the system menu or the desktop.
      </p>
      <p>
    Normally Freenet will connect automatically and should "just work",
    automatically connecting to other nodes (Strangers). However,
    if you know several people who are already using Freenet, you can
    enable high security mode and 
    <a rel="nofollow" href="http://127.0.0.1:8888/addfriend/">add them as Friends</a>, 
	so Freenet will only connect to them, making your usage of Freenet 
	almost undetectable, while still being able to access the rest of the
	network through their friends' friends etc. This will be slower unless 
	you add 10+ friends who are usually online when you are.
      </p>

      <div id="nojws">
	
	<h2>Installation Instructions</h2>
	
	<p><a href="http://freesocial.draketo.de/">Step by step guide</a> to setting up Freenet and 
	various Freenet apps. Please try this, especially if installing on Mac. We are not responsible for
	unofficial third party apps it recommends (including FMS), but many Freenet users and developers use
	them.</p> 
	
	<p>
	  Show instructions for:
	  <a href="javascript:showDiv('windows');hideDiv('macos');hideDiv('unix');">Windows
	    </a>, <a href="javascript:hideDiv('windows');showDiv('macos');hideDiv('unix');">Mac
	    OSX</a>, <a href="javascript:hideDiv('windows');hideDiv('macos');showDiv('unix');">Linux
	    etc</a><br>
	</p>
      </div>
      
      <div id="windows" style="display: none;">
	
	<h3>Windows</h3>
	
	<p>
	  - Download and
	  run <big><a href="https://freenetproject.org/jnlp/FreenetInstaller.exe">the
	      installer</a></big> (<a href="https://downloads.freenetproject.org/latest/FreenetInstaller.exe">try this if the first link is blocked</a>)<br> 
	  <br>
	  It will automatically install Freenet and other required
	  components for you. When done, your default browser will
	  automatically open up to Freenet's web-based user
	  interface. <br>
	  (Freenet contains <b style="text-decoration: underline;">NO spyware or adware</b> ,
	  it's Free Software! The source code is publicly available
	  for review) <br> 
	  <br>
	  Freenet requires Windows XP or later.<br>
	</p>
	
      </div>

      <div id="macos" style="display: none;">
	
	<h3>Mac OSX</h3>
	
	<p>
      <a href="/jnlp/freenet.jnlp">Install Freenet 0.7</a> using Java Web Start.<br>
      This requires that Java is installed and that Java Web Start is enabled.
      If it doesn't work, try <a rel="nofollow" href="http://www.java.com/">installing Java</a>,
      then downloading <a href="https://freenetproject.org/jnlp/freenet_installer.jar">the installer</a> and opening it.
      It might take a moment to launch.
    </p>

    <p>
<b>Note:</b> Mavericks does not ship with Java Web Start enabled. We would like
to make a <i>.dmg</i> for easier OS X installation but don't know how yet. If
you are a developer and would like to join us and help it would be much appreciated!
    </p>

      </div>
      
      <div id="unix" style="display: inline;">
	
	<h3>Linux and other Unix-like systems</h3>

	<p>
	  Try the <a href="/jnlp/freenet.jnlp">Java Web Start installer</a>.<br>
	  If it doesn't work:
	</p>
	<p>
	  You need to have a recent <b>Java Runtime Environment</b>
	  (JRE). We have experienced best results with Oracle's Java
	  Runtime Environment which can be obtained via
	  your <a rel="nofollow" href="https://en.wikipedia.org/wiki/Package_manager">package
	    manager</a> or
	  from <a rel="nofollow" href="http://www.java.com/">http://www.java.com/</a>.<br> 
	</p>
	<p>
      Java version 1.6 or higher is required, and 1.7 or higher is strongly
      recommended. You should keep Java up to date to avoid problems and for
      better performance.
    </p>

	<p>
	  Open a terminal and run:
	</p>
	
	<!-- please use "pre" as following (ie a newline after the
	openning pre, and no newline before the ending pre) -->

	<pre>	  wget '<a href="https://freenetproject.org/jnlp/freenet_installer.jar">https://freenetproject.org/jnlp/freenet_installer.jar</a>' -O new_installer_offline.jar
	  java -jar new_installer_offline.jar</pre>
	
	<p>
	  Alternatively,
	  downloading <a href="https://freenetproject.org/jnlp/freenet_installer.jar">the
	    installer</a>
	  (<a href="https://downloads.freenetproject.org/alpha/installer/new_installer_offline_1467.jar.sig">gpg
	    signature</a>) and then clicking on the file may work on
	  some systems, but if there are problems we recommend the
	  above command lines. If wget is not installed, it can be installed with a package manager, such as
	  sudo apt-get install wget on Debian or Ubuntu.
	</p>
	
	<p>If the link above is blocked, you could download it from our server <a href="https://downloads.freenetproject.org/latest/new_installer_offline.jar">here</a>.
	But please use the other link if you can.</p>

    <p>
<b>Note:</b> Many Linux distributions no longer ship with Java Web Start enabled.
We would like to make distribution packages for easier installation, and have
an in-development (and not maintained) <a href="https://github.com/freenet/debian">Debian package</a>, but haven't
gotten it stable or made official ones for other distributions. If
you are a developer and would like to join us and help it would be much appreciated!
    </p>


	<small>If this doesn't work on a headless server, try "java -jar new_installer_offline.jar -console", and 
	follow the prompts to tell it where to install Freenet etc.</small>
	
	<div id="mirrored">
	  
	  <h3>Mirrored installation</h3>
	  
	  <p>
	    If you have a working Freenet installation directory that you have mirrored 
	    from one Unix machine to another (e.g. via rsync or
	    unison), enabling the mirrored installation is not
	    difficult.  Nothing in a Freenet installation cares
	    about its host's IP address; it can't, or Freenet would
	    fail on machines that get IP addressss from a DHCP pool
	  </p>

	  <p>
	    All you actually need to do is tell the system you've
	    mirrored to that it should start the Freenet proxy
	    daemon for you on boot.  Do <tt>crontab -l</tt> on the
	    source machine, find the line that is tagged "FREENET
	    AUTOSTART" and add that to your crontab on the mirrored
	    machine.
	  </p>
	  
	  <p>
	    However: each installation has a unique identity key
	    generated at installation time. If you try to run two
	    instances with the same identity <em>at the same
	      time</em>, both proxy demons will become confused and
	    upset. Don't do this!
	  </p>
	  
	</div>
	
    <h3>HOWTO</h3>  
	      
      	     <p>You might find the <a href="http://freesocial.draketo.de/index.html">Freenet Social Networking Guide</a> useful.</p>

      </div>
      
      <script type="text/javascript">
					 // Try to detect if Sun Java 1.6.0 or higher is installed
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
      </script>
      
      <h3>Firewalls and routers</h3>
      
      <p>
	Freenet should work fine with most routers, but if you are having problems
	and you have a firewall or router, click <a href="faq.html#firewall"><b>here</b></a>
	for some info.
      </p>
      
      <h3>So it's running, what do I do?</h3>
      
      <p>
	When the installer closes, it should open a browser window pointing to
	the first-time wizard. Here you can configure basic settings, and then
	start using Freenet. You can access Freenet later on via the system tray
	menu (bottom right on the screen), or use the Browse Freenet shortcut on the 
	desktop and/or start menu. If it doesn't work, open 
	<a rel="nofollow" href="http://127.0.0.1:8888/">http://127.0.0.1:8888/</a> in your web browser.
      
      </p><p>
	For best security you should use a separate browser for Freenet, 
	preferably in privacy mode. On Windows, the system tray menu will 
	try to use Chrome in incognito mode if possible. Internet Explorer does
	not work well with Freenet, Firefox and Opera are widely
	used.
      </p>
      
      <p>
	If you know anyone running Freenet, you can improve your security and 
	help to build a robust network by connecting to their node. First, open the 
	<a rel="nofollow" href="http://127.0.0.1:8888/addfriend/">Add a friend page</a>. You and your
	friend should each download their "node reference". Send the file to
	the other person, and add his node reference using the form at the bottom
	of the page. When both are added, your friend's node should show up on the Friends 
	page, probably as "CONNECTED" or "BUSY". You can set a name for your node
	on the config page to make it easier to see who it is. Only add nodes run by people
	<b>you actually know</b>, whether online or offline, as adding total strangers
	harms performance and does not improve security much (they could be the bad guys!).
      </p>
      
      <h3>So I'm connected, what do I do?</h3>
      
      <p>
    Freenet itself includes anonymous websites ("freesites"), filesharing, searching, and 
    more, but you can also use third party 
	applications for chat, filesharing, to help you upload freesites, etc.
      </p>
    
    <p>The <a href="http://freesocial.draketo.de/">Freenet Social Networking Guide</a> explains how to set up
    the main third party tools, including email, forums and micro-blogging (Sone, a bit like twitter).</p>
      
      <h3>It doesn't work, now what?</h3>
      
      <p>
	If you have problems installing or running Freenet, please contact us on
	<a href="mailto:support@freenetproject.org">the support list</a> 
	(<a href="lists.html">subscribe here</a>), or join us on IRC on the
	#freenet channel on irc.freenode.net (try <a rel="nofollow" href="https://webchat.freenode.net/?randomnick=1&amp;channels=freenet">here</a>).
      </p>
      
      <h3>Hardware requirements</h3>
      <p>
    Generally a 1GHz processor and 1GB of RAM should be fine. Freenet will run on smaller
    systems, but it uses at least 128MB of RAM, so unless the system
    does nothing else it will struggle in less than 512MB. However, the 
    processor is less of a problem, people have been known to run it on 400MHz Pentium 2's or
    ATOM's, although downloads and browsing would be slow.</p>
    
      <p>
	Freenet will use a portion of your disk for storing data, 
	you can configure this to any size from 100MB upwards, but
	we recommend at least 1GB. Freenet also uses disk space for
	your downloads. Freenet's memory usage is approximately
	256MB plus 400kB for every 2GB of datastore.
      </p>
      
      <p>
      On 64-bit Windows, we will install a 32-bit Java Virtual Machine because 
      of limitations of the <a rel="nofollow" href="http://wrapper.tanukisoftware.org/doc/english/download.jsp">Java Service Wrapper</a>.
      </p>
      
      <h3>Upgrading</h3>
      
      <p>
	Freenet provides an update-over-freenet mechanism:
	It will keep itself up to date automatically from other
	Freenet nodes, and this will normally work even if it is
	unable to route to them due to them being too new. This is
	anonymous and secure, and we recommend people use it.
	However, if something is severely broken, you can update
	your node manually from our servers:</p>
      
      <ul>
	<li>Windows users can upgrade to the latest-stable Freenet
	  release from the system tray menu, or by running "update.cmd" in the Freenet
	  directory.</li>
	<li>Mac and Linux users may upgrade by running the
	  update.sh shell script in the Freenet directory.</li>
      </ul>
      
      <p>
	<small>
	  <b>Source Code:</b>
	  See <a href="developer.html">the developer page</a> 
	  for git access, or download the lastest stable
	  tarball <a href="https://github.com/freenet/fred/releases/download/build01467/freenet-build01467-source.tar.bz2">here</a> (<a href="https://downloads.freenetproject.org/alpha/freenet-build01467-source.tar.bz2.sig">signature</a>).
	</small>
      </p>
</div>""")

class DownloadPage(object):
    slug = "download"
    title = "Download"
    section = "download"
    section_link = False
    def generate(self, language, site_menu):
        h = text(content())
        return html(head("Freenet - Download"), body(menu(site_menu, self)+section("download","Download", h)))
