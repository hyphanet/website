# -*- coding: utf-8 -*-
# License: GFDL
from common import *

class FaqSection(Section):
    # FIXME: this should probably be split up for easier maintenance and easier translation
    def __init__(self):
        self.slug = "faq"
        self.title = _("FAQ")
    def get_content(self):
        return text("""
  <h3> Additional information sources</h3>
  <ul><li><a href="/whatis.html">Read this first: What is Freenet?</a>
  </li><li><a href="https://wiki.freenetproject.org/FAQ">An other FAQ on our wiki server</a>
  </li><li><a href="https://wiki.freenetproject.org/Security_summary">A page dedicated to the security of freenet 0.7 on our wiki server</a>
  </li><li><a href="/image/rabbit/freenet-bunny.svg">High quality copy of the rabbit icon</a>
  </li></ul>
  
  <h3> General / Philosophical questions</h3>
  <ol><li><a href="#what">What is Freenet?</a>
  </li><li><a href="#tor">How is Freenet different to Tor? Can I access Google/Facebook/etc through Freenet?</a>
  </li><li><a href="#who">Who is behind Freenet?</a>
  </li><li><a href="#trust">If authors are anonymous how can you trust information?</a>
  </li><li><a href="#donate-bw">Do I have to donate disk space and bandwidth?</a>
  </li><li><a href="#leech">I don't have to donate anything when using filesharing application X and I get to leech more.</a>

  </li><li><a href="#donate-more-bw">All my friends donate very little space and bandwidth. Why should I donate more?</a>
  </li><li><a href="#donate-lot">If I donate a lot will my experience improve significantly?</a>
  </li><li><a href="#legal">Is Freenet legal?</a>
  </li><li><a href="#blocked">Is Freenet blocked by national firewalls?</a>
  </li><li><a href="#trouble">Can I get trouble if I run a node?</a>
  </li><li><a href="#copyright">What about copyright?</a>
  </li><li><a href="#childporn">What about child porn, offensive content or terrorism?</a>
  </li><li><a href="#offensive">I don't want my node to be used to harbor child porn, offensive content or terrorism. What can I do?</a>
  </li><li><a href="#export">How about encryption export restrictions?</a>

  </li><li><a href="#whatelse">I have nothing to hide and don't need anonymity. Is there anything else Freenet can offer?</a>
      </li></ol>
      <h3> Technical questions</h3>

      <ol><li><a href="#how">How do I use this software? I downloaded it, but when I run it there's no GUI.</a>
  </li><li><a href="#slow">Why is Freenet so slow?</a>
  </li><li><a href="#search">Is Freenet searchable?</a>
  </li><li><a href="#firewall">How do I get freenet working with a firewall/NAT?</a>
  </li><li><a href="#connection-perm">Do I need a permanent connection to run a node?</a>

  </li><li><a href="#connections">Why does Freenet only download 1 or 2 files at a time?</a>
  </li><li><a href="#store-perm">Why can't Freenet store data permanently?</a>
  </li><li><a href="#why-java">Why is Freenet implemented in Java?</a>

  </li><li><a href="#fproxy-lan">How do I allow connections to FProxy from other computers?</a>
  </li><li><a href="#openjdk">The installer breaks while downloading files and I'm using Ubuntu 8.04 and/or OpenJDK</a>

  </li><li><a href="#whatsnew">What's new? Is there a changelog?</a>
  </li><li><a href="#backtrace">Why are there so many messages in my logfile with a backtrace attached?</a>
  </li><li><a href="#stabchange">How can I change from stable to unstable?</a>
  </li><li><a href="#freenetinigone">Freenet doesn't start, says it can't find freenet.ini</a>
  </li><li><a href="#servicenotrespond">Freenet doesn't start, says "Service did not respond to signal"</a>
  </li><li><a href="#kaspersky">I have Kaspersky anti-virus and Freenet doesn't install, or consistently shows "Download/upload queue database corrupted!"</a>
  </li><li><a href="#forgotpass">I set a password and now I forgot it, what can I do?</a>
  </li><li><a href="#clockskew">Freenet keeps complaining about clock skew</a>
      </li></ol>
      <h3> Publisher questions</h3>

      <ol><li><a href="#find">If I publish something in Freenet, how will people find it? Don't they have to know the key I used?</a>
  </li><li><a href="#chk">How do I publish a Content Hash Key (CHK)?</a>
  </li><li><a href="#update">Can Freenet documents be updated / deleted?</a>

      </li></ol>
      <h3> Contribution questions</h3>

      <ol><li><a href="#idea">I have this great idea....</a>
  </li><li><a href="#contribute">Can I contribute to the Freenet Project?</a>
  </li><li><a href="#access">How can I access the code and website?</a>
  </li><li><a href="#devtools">What tools do I need to help develop?</a>
  </li><li><a href="#freenethelp">Is there a Help Site that goes deeper into the questions newbies may have about Freenet, and where people can contribute too?</a>
  </li><li><a href="#bugs">Where can I report bugs?</a>
  </li><li><a href="#theory">I'm a computer scientist/mathematician, how can I help?</a>

      </li></ol>
      <h3> Security questions</h3>

  <ol><li><a href="#browser">Can I browse Freenet with my regular browser?</a>
  </li><li><a href="#attack">Won't attack X break Freenet's anonymity?</a>
  </li><li><a href="#flooding">Is Freenet vulnerable to flooding attacks?</a>
  </li><li><a href="#hash">Why hash keys and encrypt data when a node operator could identify them (the data) anyway if he tried?</a>
  </li><li><a href="#cancer">What about hostile "cancer" nodes within the network?</a>
  </li><li><a href="#attackY">What about attack Y?</a>
  </li><li><a href="#privatedata">What private data does Freenet store? How do I get rid of it? How can I secure my computer so I am safe when running Freenet?</a>
  </li><li><a href="#smartscreen">Windows SmartScreen filter warns the Freenet installer might put my PC at risk. What's going on?</a>
  </li></ol>
      
  
      <h2> Philosophical answers
      </h2><p><b id="what">What is Freenet?</b><br>
  Freenet
  is free software designed to ensure true freedom of communication over
  the Internet. It allows anybody to publish and read information with
  complete anonymity. Nobody controls Freenet, not even its creators, meaning that the system is not vulnerable to manipulation or shutdown. Freenet

  is also very efficient in how it deals with information, adaptively
  replicating content in response to demand.  For more information,
  please read <a href="/whatis.html">What Is Freenet</a>.</p>
  
      <p><b id="tor">How is Freenet different to Tor? Can I access Google/Facebook/etc through Freenet?</b><br>
  </p><p>Freenet is a self-contained network, while Tor allows accessing the web anonymously, as well as using
  "hidden services" (anonymous web servers). Freenet is not a proxy: You cannot connect to services like 
  Google or Facebook using Freenet. However, Freenet has websites, filesharing, forums, chat, microblogging,
  email etc, all anonymous and hosted within Freenet.</p>
  
  <p>Freenet is a distributed datastore, so once content is uploaded to Freenet, it will remain on Freenet
  forever, as long as it remains popular, without fear of censorship or denial of service attacks, and without
  needing to run your own web server and keep it online constantly.</p>
  
  <p>The other big difference is that Freenet has the "darknet" or Friend to Friend mode, where your Freenet
  node (software on your computer) only connects to the Freenet nodes run by your friends, i.e. people you know
  (and maybe to their friends, to speed things up). This makes blocking Freenet, e.g. on a national firewall, 
  extremely difficult.</p>
  
  <p>However, most people currently use Freenet in "opennet" mode (that is, connecting automatically to
  whoever the network assigns, rather than connecting only to their friends). This is much less secure than
  using Freenet in "darknet" mode, and is relatively easy to block, as it does have some central servers ("seed nodes").</p>
  
  <p>Freenet has many unsolved problems, and is still experimental. Our objective for Freenet is to build a
  global friend-to-friend darknet, which would be extremely difficult to block, and would provide very strong
  anonymity and censorship resistance. This will require further work on Freenet, on usability, speed and 
  security, but above all it is a techno-social experiment: Will people know enough friends who are willing 
  to use Freenet to make such an anonymous friend-to-friend network possible? This is why Freenet supports 
  "opennet" mode: to let people try it out before they ask their friends to connect.</p>
  
  <p>Tor is a little less experimental, and arguably is an easier problem; it may provide better anonymity
  today, provided that it isn't blocked, and of course, Tor lets you access the internet as a whole, whereas
  on Freenet you can only access Freenet content. However if you can use a large enough darknet, Freenet 
  already provides an interesting level of censorship resistance, DoS resistance and anonymity.</p>
  
  <p>Using the internet "anonymously" is not necessarily easy: Connecting to Facebook through Tor doesn't
  prevent Facebook from knowing pretty much everything about you, and connecting to your (non-HTTPS)
  webmail account through Tor may mean the person running the proxy ("exit node") can steal your webmail 
  account password.</p>
  
  <p>Freenet is a separate network, which does things differently, because there are no central servers. This
  is why we don't support Javascript, server-side scripting etc on freesites: Everything must be rewritten to 
  work on a distributed network. But the advantage is there is no single server which can be compelled to hand
  over your private communications or which can be shut down.</p>
  
  <p>There are still risks, for example, talking about your home town or internet provider on an anonymous
  forum, or downloading files which Freenet can't make safe such as PDFs or word processor documents (Freenet 
  will warn you about this). Also, for web content in particular, it may be easier to upload it to Freenet than 
  set up a hidden server on Tor; you don't need to keep your node online for your content to be available,
  you don't need to figure out how to configure it safely, and most important, if you go away your site will
  still be available.</p>
  
  <h3>Summary:</h3>
  <p>Tor (or I2P):</p>
  <ul><li>Lets you access the Internet (but be careful!).</li>
  <li>Lets you access anonymous web servers and other services.</li>
  <li>Lets you host anonymous web servers, which need to be kept online, and can be DoS'ed, but can run any
  dynamic or server-side content you want.</li>
  <li>Provides reasonable anonymity</li>
  <li>Has been blocked by several countries, with varying success. Even its hidden bridges can be harvested 
  and blocked with moderate effort.</li>
  <li>Is somewhat centralised</li>
  <li>Is more mature and has more users and developers</li>
  </ul>
  <p>Freenet in general:</p>
  <ul><li>Only lets you access content uploaded to Freenet, including (static) websites, email, filesharing, 
  forums, microblogging, etc. All of which are anonymous (or pseudonymous i.e. you create an untraceable 
  identity).</li>
  <li>Hosts content in a distributed way: You don't know what your node is storing, any given content is 
  distributed across many nodes.</li>
  <li>Ensures that popular content will be available forever.</li>
  <li>Is older than Tor, but more experimental (arguably it's a harder task).</li>
  </ul>
  <p>Freenet in darknet mode: (friend to friend: connects only to your friends' nodes)</p>
  <ul><li>Is very hard to block, and this can be improved further with transport plugins.</li>
  <li>Provides good anonymity, and with a bit more work it could provide very strong anonymity (PISCES 
  tunnels).</li>
  <li>Is fully decentralised: No central servers at all.</li>
  </ul>
  <p>Freenet in opennet mode: (connect automatically even if you don't know anyone on Freenet)</p>
  <ul><li>Is relatively easy to block.</li>
  <li>Provides limited anonymity</li>
  <li>Is somewhat centralised</li>
  </ul>
  
  <p>Unfortunately most people use Freenet in opennet mode currently. The big question is can we 
  build a global friend-to-friend darknet? Join us and find out!</p>
  
  <p>PS for an example of how dependant Tor is on centralised hidden services, see 
  <a href="http://www.twitlonger.com/show/n_1rlo0uu">this</a> 
  <a href="http://arstechnica.com/tech-policy/2013/08/alleged-tor-hidden-service-operator-busted-for-child-porn-distribution/">bust</a>. 
  Half the hidden services on Tor were using a single hosting service, whose owner has now been 
  arrested. While we don't approve of these sites, it does illustrate the point: A centralised 
  network is a vulnerable network. Unfortunately, decentralised networks are hard, but in the long 
  run they are more secure.</p>

      <p><b id="who">Who is behind Freenet?</b><br>
  Freenet grew out of a design for an anonymous publication system created by Ian
  Clarke while a student at the University of Edinburgh, Scotland. Since
  then many other people have contributed towards making Ian's proposal a
  reality.</p>

      <p><b id="trust">If authors are anonymous how can you trust information?</b><br>
  Cryptographic signing of information allows people to prove
  authorship, this technique is frequently used to authenticate
  authorship of emails. Moreover, you can actually sign information
  while remaining anonymous, thus having an anonymous persona. You can
  prove that you wrote different pieces of information on Freenet, without revealing your identity. In this way you can build up an anonymous reputation for reliability.</p>

      <p><b id="donate-bw">Do I have to donate disk space and bandwidth?</b><br>
  You aren't really donating in the sense that you lose the disk
  space and the bandwidth; but you aren't really sharing either (at least
  not the same way as with filesharing programs). It is more like
  pitching in to the common Freenet resource pool.</p>

      <p><b id="leech">I don't have to donate anything when using filesharing application X and I get to leech more.</b><br>

  Do you get to do that anonymously? Freenet is designed with anonymity in mind, performance comes second.</p>

      <p><b id="donate-more-bw">All my friends donate very little space and bandwidth. Why should I donate more?</b><br>
  If you are happy with what you are getting then no. But if you want
  more you should consider donating more and running your node as close to 24x7 as possible, and
  you should ask your friends to do the same.</p>

      <p><b id="donate-lot">If I donate a lot will my experience improve significantly?</b><br>
  Your experience will definitely get better, but for a really great
  improvement we need more people to start thinking like you. Bandwidth
  counts more than diskspace.</p>

      <p><b id="legal">Is Freenet legal?</b><br>
  We don't currently know of any prosecutions for using merely using Freenet.
  Some people claim that the <a href="https://en.wikipedia.org/wiki/DADVSI">DADVSI</a>
  makes Freenet illegal in France; the German data retention law might have required
  logging, but <a href="http://en.wikipedia.org/wiki/Telecommunications_data_retention#Germany">was struck down</a>.
  Also, the German supreme court has found that 
  <a href="http://merlin.obs.coe.int/iris/2010/7/article13.en.html">not securing 
  your wifi properly</a> makes you responsible for other people's downloads over it; this 
  might or might not be extended to prohibiting anonymous peer to peer filesharing such as Freenet.
  <a href="http://en.wikipedia.org/wiki/ACTA">ACTA</a> might have
  wide-ranging effects, including on Freenet, should it pass, and similar laws
  such as IPRED2 have been tried in the past. There have also been attempts to
  force peer to peer systems to provide wiretapping capabilities in the USA, and
  there are <a href="http://www.bbc.co.uk/news/uk-politics-19968068">worrying 
  developments</a> in the UK that might result in it being blocked, but not being made
  illegal per se. As far as we know none of these things - apart from the first two - 
  have passed. Many of these are arguable either way (depending on how broadly the 
  legislation is applied) and will have to be decided in caselaw.
  The law can be an ass sometimes. You can read the EFF's (US-centric) advice to peer to peer developers 
  <a href="https://www.eff.org/wp/iaal-what-peer-peer-developers-need-know-about-copyright-law">here</a>. 
  If you need legal advice, talk to a lawyer. Also read the next section especially if you
  are in China; blocking the protocol may suggest the authorities don't like us!
      </p>

      <p><b id="blocked">Is Freenet blocked by national firewalls?</b><br>
  The Chinese national firewall (Golden Shield) has blocked our website for many years,
  and was observed in 2005 to block the 0.5 protocol as well. This suggests China doesn't 
  like us, so be careful if you run Freenet in China. Some other countries (e.g. France)
  are known to be hostile to peer to peer, and may eventually force ISPs to block peer to 
  peer networks (but right now Freenet works fine in France and we have many French users!).</p>
  
  <p>Technically, Freenet 0.7 has some minimal defences against blocking; the protocol is relatively hard 
  to identify (we are working on <a href="https://wiki.freenetproject.org/Transport_plugins">"transport plugins"</a>, 
  which would <a href="http://en.wikipedia.org/wiki/Steganography">make it much harder
  to detect Freenet</a>. Freenet supports a <a href="https://wiki.freenetproject.org/Darknet">darknet</a> mode 
  (i.e. only connecting to your friends) which makes automated harvesting and blocking 
  of nodes very difficult. Note that many mobile internet providers block all peer to peer networks
  along with other content, and many corporate or academic networks may block Freenet (but even
  if they don't, see <a href="#trouble">you shouldn't run Freenet at work</a> for non-work purposes!).</p>
  
  <p>There has been discussion in the US and UK of legislation to require backdoors and presumably 
  blocking of anything that can't be backdoored. This is unlikely to pass, especially in the 
  US, where similar laws have been proposed periodically and are probably unconstitutional. However, 
  even if the government came to us and demanded a back door, we would be legally unable to secretly
  distribute a trojan'ed build, because Freenet is open source, numerous people have contributed 
  code to it, so legally we have to give you the source code, including that for any government 
  mandated back doors - which wouldn't be secret for long! If this happened it is likely that
  <a href="/donate.html">Freenet Project Incorporated</a>, the non-profit organisation that runs 
  this website and handles donations, would shut down, but the Freenet network itself would live 
  on just fine, the only difference being not being able to pay full time developers as easily.</p>
  
  <p>See <a href="http://en.wikipedia.org/wiki/Network_neutrality">net neutrality</a> and <a href="https://www.eff.org/">the EFF</a>
  or equivalent organisations in your country for the politics of all this and how you can stop such
  laws.</p>
      
      <p><b id="trouble">Can I get trouble if I run a node?</b><br>
  This is related to <a href="#legal">"Is Freenet legal?"</a>. We have done everything
  we can to make it extremely difficult for any sane legal system to
  justify punishing someone for running a Freenet
  node, and there is little precedent for such action in today's developed
  countries. Many legal systems recognise the importance of freedom of
  speech, which is Freenet's
  core goal. Having said that, there is risk in doing anything that your
  government might not agree with; you should make an informed decision
  as to whether to take that risk. Furthermore, your ISP or hosting provider
  may have a problem with Freenet. At least one French hosting provider
  has been known to ban Freenet (along with Tor and others) from their
  servers; please read your terms and conditions to make sure you are 
  allowed to run Freenet. Note also that Freenet can use rather a lot of bandwidth,
  at least 20GB/month, and this may be a problem on a cheap or shared connection.
  And of course running it at work could get you into trouble too, unless it's for
  work purposes!</p>

      <p><b id="copyright">What about copyright?</b><br>
  There are some excellent thoughts on this subject on the <a href="/philosophy.html">Philosophy</a> page.
  Specific copyright-related laws may be a problem, please read <a href="#legal">Is Freenet legal?</a>
  and <a href="#blocked">Is Freenet blocked by national firewalls?</a>.</p>

      <p><b id="childporn">What about child porn, offensive content or terrorism?</b><br>
  While most people wish that child pornography and terrorism did not
  exist, humanity should not be deprived of their freedom to communicate
  just because of how a very small number of people might use that
  freedom.</p>


      <p><b id="offensive">I don't want my node to be used to harbor child porn, offensive content or terrorism. What can I do?</b><br>
  The true test of someone who claims to believe in Freedom of Speech
  is whether they tolerate speech which they disagree with, or even find
  disgusting. If this is not acceptable to you, you should not run a Freenet node.
  Also, content in Freenet is available only as long as it is popular, so it
  will go away if people lose interest. However, it should persist for some
  time, and if enough people are interested, it will persist forever.
  Note that other people's file are encrypted and split into pieces. They are not stored on your machine
  in their entirety. Your instance of Freenet will likely have a very small number
  of encrypted pieces from a given file. A file can only be assembled when all
  its pieces are combined with the decryption key.
  </p>

      <p><b id="export">How about encryption export restrictions?</b><br>
  The Freenet Project has notified the US authorities (since the files are hosted on SourceForge,
  which is on US soil) that it will be exporting crypto. As long as your
  country doesn't prohibit the use of encryption you are fine. Further, there
  is now an exception in the export laws for software doing exactly what Freenet
  does! However, Sun limits the encryption strength available on the JVM that runs
  Freenet; you should install the Unlimited Strength Policy Files for Java if possible
  to improve performance. Freenet will however work even without this, by using its built-in
  encryption code.</p>


      <p><b id="whatelse">I have nothing to hide and don't need anonymity. Is there anything else Freenet can offer?</b><br>
  Yes, in fact even without the anonymity feature Freenet
  is very useful because of its unique way it handles content distribution
  and information load. In simple terms that means you can publish a
  website without worrying about how big the site will be and without
  having to put someone elses ad banners on it. While it is unlikely that
  freenet sites will ever load faster than regular websites, it does adapt to
  sudden surges of visitors better (which often happen when relatively unknown sites 
  get linked to from a big site), and reasonable download speeds for big files
  are feasible too. Just don't expect very low latency.
      </p>
      
      <h2> Technical answers</h2>

      <p><b id="how">How do I use this software? I downloaded it, but when I run it there's no GUI.</b><br>
  Fred (the Freenet REference Daemon) runs as a daemon, or service, in the background. You normally talk to it through a Freenet client. One built-in client is fproxy, which lets you talk to Freenet with a web browser. 
  Freenet should have installed a Browse Freenet shortcut on the desktop and/or the start menu, or a system tray icon (rabbit) with a Launch Freenet menu item.
  Failing that, point your web browser to <a href="http://127.0.0.1:8888/" rel="nofollow">http://127.0.0.1:8888/</a> for the gateway page. Try clicking the various links in the "Freesite subscriptions" panel to reach some of the popular Freenet index sites.</p>

      <p>If you're looking for applications that run on top of Freenet and provide a different interface or functionality, please see the <a href="/tools.html">Tools</a> page.</p>

      <p><b id="slow">Why is Freenet so slow?</b><br>
  When you first install Freenet, it will be slow, and you may see Data Not Found 
  or Route Not Found errors for freesites. This is normal, and Freenet will speed
  up significantly over time. For best performance you should try to run Freenet
  as close to 24 hours a day as possible. This is why we install Freenet as a
  service.</p>

      <p>Please bear in mind that Freenet is inherently high latency: it can take a while 
  to (for example) load a page for the first time, even if it is capable of reasonable
  speeds (as anonymous systems go!) for large popular files. You can also improve performance
  for freesite browsing by using a separate browser and <a href="#connections">increasing 
  its connection limit</a>. You should also set the datastore size and bandwidth limit as
  high as possible. But protecting your anonymity does cost a certain amount of performance.
  You can configure how much to a degree by changing the security levels on the page under
  Configuration. </p>

      <p><b id="search">Is Freenet searchable?</b><br>
  Yes, there are a few different search mechanisms. To search the freenet web (freesites),
  you should be able to just use the search box on the homepage, or go to Search 
  Freenet on the Browse submenu. If it's not there, go to the Plugins page under 
  Configuration, and load the Library plugin. Alternatively, Frost and Thaw also 
  provide searching for messages and files. Note that searching on Freenet is a good 
  deal more difficult than on other networks because of Freenet's different 
  architecture and design goals.
      </p>

      <p><b id="firewall">How do I get freenet working with a Firewall/NAT?</b><br>
  Mostly, Freenet should just work with a NAT. However, you should forward the ports
  manually if you can. Click on the <a href="http://127.0.0.1:8888/connectivity/" rel="nofollow">Connectivity</a> page. At the top you will
  see a list of ports used by the node. You should forward (for UDP) the Darknet FNP 
  and Opennet FNP ports. You may need to look up your router's documentation to figure
  out how to do this. Freenet should have forwarded them itself through <a href="https://en.wikipedia.org/wiki/Universal_Plug_and_Play">Universal Plug and Play</a>,
  but this doesn't always work (and it never works if you don't have the UPnP plugin loaded, or have one router behind another).</p>

      <p>If you have a dyndns address or other domain name pointing to the computer you run 
  your Freenet node on, tell the node about it. Go to <a href="http://127.0.0.1:8888/config/node?mode=2">the core settings config page</a> (in advanced mode), 
  and find the option "IP address override". Put your domain name in that box, and apply the settings.</p>

      <p><b id="connection-perm">Do I need a permanent connection to run a node?</b><br>
  No, but it is preferred. You can run the software and test it from
  a "transient" connection (e.g. dial up/mobile modem), but for the network 
  as a whole to be most useful, we will need
  as many permanent nodes as possible (most cable modem or DSL setups are
  sufficiently "permanent" for this). A later version of Freenet may take better advantage of transient nodes.</p>

      <p><b id="connections">Why does Freenet only download 1 or 2 files at a time?</b><br>
  Many browsers limit the number of simultaneous connections to something far too low for efficiently browsing Freenet (since Freenet
  pages often have much higher latency than web pages). This can usually
  be reconfigured. For example, for Mozilla Firefox, type <span style="font-weight: bold;">about:config</span> in the address field
  of the browser and replace the value of the following settings to the one stated. Filter on <span style="font-weight: bold;">"connections"</span>

  to get only the relevant settings:</p>

      <code>
  network.http.max-connections 200<br>
  network.http.max-connections-per-server 200<br>
  network.http.max-persistent-connections-per-proxy 200<br>
  network.http.max-persistent-connections-per-server 200<br>
      </code>
      <p>Note that these settings will cause mozilla to use more
  connections for all your browsing, which may not be desirable from a
  network congestion point of view. But you should ideally be using a separate
  browser for Freenet anyway, for best security.</p>

      <p><b id="store-perm">Why can't Freenet store data permanently?</b><br>
  Because we can't find a way to do this without compromising Freenet's
  other goals. For example, people often suggest that someone's node could
  just never drop data they want to cache permanently. This, however,
  won't work because even if the data is still available on their node,
  there is no way to ensure that requests for that data will be routed to
  that node. We have considered many other ways that Freenet could store data 
  permanently, but they either won't work, or compromise Freenet's core goals 
  of anonymity, and scalability.</p>
  
    <p>Content which is popular should persist indefinitely, for example most
  freesites linked from the main indexes are still retrievable years later (at
  least their front pages are). If the content isn't very popular the best way
  to keep it available is to regularly re-insert (re-upload) it. An interesting
  option is the "Keepalive" plugin, which will do this for you - even if you 
  didn't upload the file/site in the first place. Improvements are planned, 
  such as a special kind of request that allows us to probe whether a file is
  available from a random point on the network.</p>

      <p><b id="why-java">Why is Freenet implemented in Java?</b><br>
  Opinions differ about the choice of java for the reference implementation of
  freenet (even among the core developers). <a href="/people.html">Ian Clarke</a> and several
  other developers are java proponents and the choice for java was made. Even if everybody could be convinced
  to switch to a different language reimplementing the current freenet protocol would be quite a big task, and
  take up a significant amount of time, while there is only a limited amount of developer-time available. Flame wars
  on the development list about the language choice aren't welcome, people willing to implement freenet
  in other languages however are very much encouraged to try. Don't underestimate the amount of work however.
      </p>
      
      <p><b id="fproxy-lan">How do I allow connections to FProxy from other computers?</b><br>
    If you want everyone to be able to use your node you have the following options:<br></p>
    <ul>
    <li>Go to the <a href="http://127.0.0.1:8888/config/fproxy">web interface configuration page</a> and enable advanced mode</li>
    <li>Stop your node and edit freenet.ini manually</li>
    </ul>
    <p>In both cases change the following parameters:</p>
    <p></p><code>
    fproxy.bindTo=0.0.0.0<br>
    fproxy.allowedHosts=*<br>
    </code><p>
    Of course, this leaves your node wide open, unless you control
    access with a firewall of some sort.  If you'd prefer to use access
    controls within Freenet, then you can use lines like this:</p>
    <code>
    fproxy.bindTo=0.0.0.0<br>
    fproxy.allowedHosts=127.0.0.1,192.168.1.0/24<br>
    </code>
    <p>Or even (find your IP address from ipconfig/ifconfig/winipcfg and substitute it for 192.168.1.1):</p>
  <code>
  fproxy.bindTo=127.0.0.1,192.168.1.1<br>
  fproxy.allowedHosts=127.0.0.1,192.168.1.0/24<br>
  </code>
  <p>And if you want to grant full access (i.e. change config settings, restart, etc) to the node (WARNING: Be very careful who you give full fproxy access to!):</p>
  <code>
  fproxy.allowedHostsFullAccess=127.0.0.1,192.168.1.0/24<br>
  </code>

    <p><b id="openjdk">Problems installing with OpenJDK</b><br>
  </p><p>Some versions of OpenJDK, particularly the one included with Ubuntu 8.04,
  have some problems with SSL which cause the installer to fail. Please install
  the Sun JRE, at least version 6. On Ubuntu or Debian, open a root terminal and type:</p>
  <pre>  apt-get install sun-java6-bin
  update-java-alternatives -s java-6-sun
  </pre>

    <p><b id="whatsnew">What's new? Is there a changelog?</b><br>
    On every new build, a brief summary of all the main changes is posted to the support and devl lists 
    and the eng.freenet board on Freetalk. This is usually relayed to FMS and Frost too. Alternatively,
    for a much more detailed view, check out the <a href="https://github.com/freenet/">git repositories</a>.
    Also, you should check the developer blogs (from the default bookmarks, or over the web, e.g. 
    <a href="http://amphibian.dyndns.org/flogmirror/">toad</a>), but be warned they are often not regularly 
    updated and frequently go off on rants on unrelated topics!</p>
    
      <p><b id="backtrace">Why are there so many messages in my logfile with a backtrace attached?</b><br>
  Fred (and freenet in general) are still very much in development, and if something goes wrong it's worthwhile
  to know exactly what went wrong.
      </p>
      
      <p><b id="stabchange">How can I change from the main network to the test network?</b><br>
  The test network is a separate network which allows the developers to see exactly
  what is going on. There is no anonymity on the test network. There is a separate installer
  (<a href="https://downloads.freenetproject.org/latest/testnet_installer_offline.jar">for Linux, OS/X</a>,
  <a href="https://downloads.freenetproject.org/latest/TestnetInstaller.exe">for Windows</a>).
  This can break quite often, so you should probably have some idea what you are doing or at least 
  be prepared to reinstall regularly!
      </p>
      
      <p><b id="freenetinigone">Freenet won't start and the launcher says it can't find freenet.ini</b><br>
    This is due to an unfortunate bug, fixed in 1249. You can fix it by renaming freenet.ini.tmp to freenet.ini.
      </p>
      
      <p><b id="servicenotrespond">Freenet won't start, it says "Service did not respond to signal"</b><br>
    This should be fixed now, let us know if you see it. If you have a very old install, you might be interested
    in the steps <a href="https://wiki.freenetproject.org/Installing/Windows#Service_did_not_respond_to_signal">here</a>.
      </p>
      
      <p><b id="kaspersky">I have Kaspersky anti-virus, and Freenet doesn't install, or shows "Download/upload queue database corrupted!"</b><br>
  Kaspersky can be a problem with Freenet. See <a href="https://wiki.freenetproject.org/Installing/Windows#.27Download.2Fupload_queue_database_corrupted.21.27_.28When_using_Kaspersky_on_Windows_7.29">here</a>.
  We recommend you turn off Kaspersky during install and during node startup, and exclude the directory you
  installed Freenet in (most likely C:\Program Files\Freenet or C:\Program Files (x86)\Freenet).</p>

      <p><b id="forgotpass">I set a password and now I forgot it, what can I do?</b><br>
  The password protects your downloads and uploads and the client-cache (cache of 
  what you've recently browsed on Freenet). It is stored in the file master.keys. There 
  is no way to recover the password, but if you forget it you can wipe your downloads and 
  uploads and the client cache by securely deleting the file master.keys. See <a href="#privatedata">the
  question on private data and local security</a> for more information.</p>
  
    <p><b id="clockskew">Freenet keeps complaining about clock skew</b><br>
  Freenet will have problems if your clock is constantly being rewound. Usually this 
  happens when something is resetting your clock regularly in big jumps. On linux, you 
  should run ntpd to make sure your clock isn't too far off (this isn't vital but it's
  helpful), but if you see clock skew errors, try adding the -x option to it to avoid 
  big backwards jumps. Also, running ntpdate on startup so there is one big jump before
  freenet starts is a good idea. This can also happen on Windows sometimes, let us know
  how you managed to fix it ... generally it's not all that serious though, especially if
  big jumps in the clock are only once a day.</p>

      <h2>Publisher answers</h2>
      <p>
  <b id="find">If I publish something in Freenet, how will people find it? Don't they have to know the key I used?</b><br>
  Yes, people will have to know what key you used to publish your
  information. This means you will have to announce your key in some way.</p>
      <p>The most common way to do this is to send a message, containing
  your key and brief description of your information, to the author of
  one of the existing Freenet sites. Most of the "portal" sites which are linked from the Freenet
  web interface (fproxy) read the Freetalk or FMS forums, and there are boards
  specifically for announcing sites (usually the boards are called "sites"!). You could also send your key to people by using
  the Freenet <a href="/lists.html">mailing lists</a>, in the
  IRC channel (irc.freenode.net #freenet), by private e-mail, or by advertising your Freenet
  site on your World Wide Web site. If you're feeling extravagant, you
  could even try skywriting it. (Graffiti is not recommended, for legal
  reasons.)</p>

      <p><b id="chk">How do I publish a Content Hash Key (CHK)?</b><br>
  A Content Hash Key is based on the actual content contained within
  it - and as such, the key will only be known after it has been inserted
  into Freenet.  To insert a CHK, simply insert it as "CHK@", Freenet will tell you what the actual CHK is once the insertion completes.

      </p><p><b id="update">Can Freenet documents be updated / deleted?</b><br>

  Currently, a document posted to Freenet
  with the same name as one already present may actually serve to
  propagate the existing document. There is also currently no means of
  deleting a document from Freenet. Documents that are never requested are eventually removed through disuse.</p>
      <p>However, you can use an <a href="https://wiki.freenetproject.org/USK">Updatable Subspace Key (USK)</a>
  to provide a form of updatable freesite: your node will automatically look for later editions of
  the site (after you visit it, or always if you bookmark it), and show you the latest version.
  You can force it to search for the latest version by changing the number at the end of the key to negative.</p>

      <h2> Contribution answers

      </h2><p><b id="idea">I have this great idea....</b><br>
  Good! First step: read the <a href="/lists.html">mailing list archives</a>.
  Odds are good that someone else had the same idea and discussed it with
  the group. Either a flaw was found in the idea, or perhaps it was
  decided to postpone implementing the idea until later. Some examples of
  ideas already discussed are storing information by content hash, key
  redirection, signed keys/data, use of UDP, server discovery, URLs,
  document versioning, and others. If you don't see the idea discussed in
  the archives, by all means bring it up in the appropriate <a href="/lists.html">mailing list</a>.</p>

      <p><b id="contribute">Can I contribute to the Freenet Project?</b><br>
  Absolutely. Even if you don't have the time or skills to become a co-developer of the project, you can contribute in other ways:</p>

      <ul><li> Help test Freenet by installing and configuring the server software on your machine.
  </li><li> Install the client software on your machine to test retrieving information and publishing your own.

  </li><li> Work on the Freenet web site (including the FAQ).
  </li><li> Contribute your ideas to the discussion lists.
  </li><li> <a href="https://wiki.freenetproject.org/Translation">Translate the user interface</a> into your local language (the website and the installers also need translation, you can ask us about this).
      </li></ul>
      
      <p>If you are a developer, you can help by working on Freenet itself, or by creating other applications
  to run on Freenet. External applications (such as FMS, the main forums system used on Freenet) use 
  <a href="https://wiki.freenetproject.org/FCPv2">the Freenet Client Protocol</a> to talk to Fred. Another 
  possibility is writing plugins - these are written in Java and run in Freenet's JVM, and can be bundled
  with Freenet when they are ready. A popular plugin is Sone, which is a microblogging/social app over 
  Freenet. You can see how to install FMS and Sone on e.g. the Freenet Social Networking Guide freesite.</p>
  
  <p>If you want to work on Freenet itself, see <a href="https://freenetproject.org/developer.html">here</a>
  to get the source code.</p>
  
  <p>Links to us are welcome, for example this <a href="http://www.webhostingsearch.com/">web hosting guide</a>.
  Improvements to this website, fixes for spelling/grammar mistakes, new ideas (see <a href="#idea">the previous answer</a>),
  are all welcome. You may find <a href="https://wiki.freenetproject.org/Main_Page">the wiki</a> helpful.</p>
  
  <p>If you want to contribute to Freenet in any way, please contact us, via 
  <a href="https://emu.freenetproject.org/cgi-bin/mailman/listinfo/devl/">the developers mailing list</a>,
  <a href="/irc.html">the chat channel</a>, anonymously via the freenet board on FMS, or email 
  <a href="mailto:ian@locut.us">Ian</a>.</p>
  
  <p>Last but not least you can <a href="/donate.html">donate</a> to support our paid developer(s) and cover
  server costs.</p>
      
      <p><b id="access">How can I access the code and website?</b><br>

  See the <a href="/developer.html">developer page</a> for details of our git repositories etc.
      </p>
      <p><b id="devtools">What tools do I need to help develop?</b><br>
  To build and deploy the Freenet server, you will need Java tools compatible with Sun's JDK 1.6 or later. You can download the source tarballs
  on the download page for a specific build, or use git to get an up to date copy of the source, see <a href="/developer.html">here</a> for details.
  Further instructions for building and deploying the server are included with the code itself.
  Generally speaking, joining our IRC channel is a good idea: <a href="irc://irc.freenode.net/freenet">#freenet on irc.freenode.net</a></p>

      <p><b id="freenethelp">Is there a Help Site that goes deeper into the questions newbies may have about Freenet, and where people can contribute too?</b><br>

  Have a look at <a href="https://wiki.freenetproject.org/">our wiki</a>.
  An older wiki, which is now read-only, but has a fair amount of content so is
  sometimes helpful is <a href="https://old-wiki.freenetproject.org/">here</a>. 
  There are also several implementations of wiki's over Freenet. The most recent
  one is called Jfniki. There is a link in the default bookmarks on the Browse 
  Freenet page after you install Freenet.
      </p>
      
      <p><b id="bugs">Where can I report bugs?</b><br>
  You can use our <a href="https://bugs.freenetproject.org/">bug tracking system</a> or send a mail to our <a href="/lists.html">support mailing list</a>.</p>
  
    <p><b id="theory">I'm a theoretical computer scientist/mathematician, how can I help? (research challenges)</b><br>
  See <a href="https://wiki.freenetproject.org/Research_challenges">here</a>.</p>

      <h2> Security answers</h2>
      <p><b id="browser">Can I use my regular browser to browse Freenet?</b><br>
  Freenet has a web interface: much of the content on Freenet is in the form of
  "freesites", and downloads, configuration and friend connections can be managed from 
  the web interface. However, because of weaknesses in current browsers, we 
  <b>strongly</b> recommend that you use a separate browser for Freenet. Specifically,
  browser history stealing, in all its forms, is a major threat if you share a 
  browser between Freenet and the WWW at large: malicious web pages will be able to
  probe which freesites you have visited, and report this information to their owners.
      </p>
      <p>With recent browsers, privacy/incognito mode may be sufficient, and the rabbit
    applet on the system tray on Windows will try to start a browser running in this 
    mode. However, this is not 100% reliable in our experience, so be careful.</p>
    
      <p><b id="attack">Won't attack X break Freenet's anonymity?</b></p>
      <p><b>Short answer:</b> Probably, on opennet. Maybe, on darknet.</p>
      <p><b>Long answer:</b></p>
      <p>Freenet has a different threat model to Tor and the Mixmaster remailers. 
  Freenet is designed to resist
  censorship: The network must therefore be robust, and content must be distributed
  without requiring a central server, whether anonymous or not. Anonymity is important
  for requesters and especially for those who upload content in the first place. The
  typical example is a corporate or government whistleblower. Generally to find the
  originator of some content, the attacker must be able to predict the data in advance,
  must be able to move across the network relatively quickly, and must be able to 
  perform the attack while the data is being inserted; after that, it is distributed 
  across the network and is much harder to trace, and the originator may have left the 
  network. However, if by chance or by overwhelming force the attacker is connected
  to the whistleblower (or e.g. seizes the computers of everyone on the network), he 
  may be able to identify this much more quickly. All of this is vastly more difficult 
  on a darknet, where everyone connects only to their friends, where it is very hard for
  an attacker to find nodes, and where to connect to a given node he must social engineer
  its operator! Freenet does support opennet mode (plug and play), but darknet is far more 
  secure, and far more difficult to block on a national firewall.</p>
      <p>Tor on the other hand is designed to anonymise real-time data streams, on the 
  assumption that the list of nodes can be public, that there is a free world where
  nodes can be operated safely, that the authors of controversial content will be able
  to either host (hidden) web servers themselves or upload it to other (hidden, but usually centralised) storage systems,
  and so on. And Tor has a concept of a "client", which is somebody who uses the 
  service without providing any value to it; on Freenet, every node relays data for
  its neighbours. Hence the attacks on Freenet are completely different to the attacks
  on Tor. Both compromise to some degree to enable more or less real-time performance.</p>

      <p>If you can use the darknet, trust your friends, don't reinsert files, always 
    use the "Insert a random, safe key" option, and change your anonymous identity after 
    some volume of inserts, you should be relatively safe using Freenet. However this has
    not yet been quantified. If 
  you can connect, build up some trust in your anonymous persona, insert your controversial 
  content, and then disappear, again, you are better off with Freenet, especially if the 
  content is a website (but if you are connecting on opennet, beware of seednode compromises). 
  In some other cases, Tor is better.</p>
    <p>We are still working on Freenet's security and there are major security enhancements
  which have not yet been implemented, most of which will go in before 1.0. Cryptographic
  tunnels similar to Tor's onion routing are one possibility, which would greatly reduce
  the impact of many of the below attacks, but there are several other enhancements 
  planned, both to anonymity and to network robustness/undetectability.</p>
  <b>Major known attacks:</b><br>
  In the interests of giving would-be users as much information as possible, and on
  the assumption that any serious attacker would do their homework, here are the major 
  classes of attack on Freenet we are presently aware of:<p></p>

      <ul><li><b>Harvesting</b>: Simply by running some powerful Freenet nodes, an 
    attacker can identify most of the opennet (Strangers network) relatively easily.
    These nodes can then be attacked one by one (subject to resources), their traffic
    analysed, or simply be blocked on a national firewall. Connecting only to friends (darknet)
    largely solves this problem. ISPs may be able to identify Freenet nodes with some
    effort, although we make this fairly difficult: Freenet's current protocol is designed
    to be hard to detect, and steganography will be introduced at some point. However, traffic flow 
    analysis, or brute-force blocking of all peer to peer traffic (e.g. traffic between 
    IP addresses marked as "consumer" rather than "business"), both of which would hit a lot
    of things other than Freenet, would likely be effective for quite some time.</li>

    <li><b>Bootstrapping attacks</b>: Unless a node only connects to friends, it will
    have to connect to the opennet "seednodes" to announce itself and get initial peers
    to connect to. At the moment there are relatively few seednodes and the list is 
    maintained manually. The seednodes could be blocked easily by a national firewall etc,
    but also, there is little to prevent attackers from setting up their own seednodes and
    submitting them, and then "capturing" any new Freenet users who connect to their 
    nodes, in order to observe their traffic etc. Freenet will try to announce to multiple
    seednodes, but see the below section on "correlation attacks", which generally are 
    feasible with only a single connection to the target. So this is a question of 
    resources - if the attacker has the resources to surveil all new Freenet nodes, he has
    a good chance of pulling it off. In future we may have more seednodes, and only
    reveal a small proportion of them to each node, as Tor does with its hidden bridges,
    but that will not prevent attackers from creating lots of malicious seednodes and 
    getting them into the official lists, and it will likely still be possible to block
    all the seednodes with some effort (something similar has already happened to Tor hidden
    bridges in China). Combined with harvesting and adaptive search attacks, this attack explains why opennet is 
    regarded by many core developers as hopelessly insecure. If you want good security
    you need to connect only to friends. Hit and run inserts are possible, and can be
    relatively safe in terms of many of the other attacks, but you are taking the risk 
    that the opennet seednode you connect to may be malicious.</li>

  <li><b>Datastore attacks</b>: This is largely solved as of build 1224, we don't
    cache our local requests or inserts, and neither do the nodes immediately connected
    to us, to a depth of at least 2 hops (3 on inserts). However, if your node is older
    than that, seizing the store might give a bad guy some interesting information.
    Also note that the client-cache caches local requests (but not inserts), so it should
    be encrypted and passworded by setting the physical security level to HIGH, or turned 
    off. You should also encrypt the swapfile in particular and the whole system if 
    possible to prevent information leaks from the web browser, media players etc. Note
    that some incriminating data (e.g. the list of bookmarks) is still stored in 
    plaintext; we're working on it, but did I mention you should 
    <a href="http://www.truecrypt.org">encrypt your whole system</a>?</li>

  <li><b>Correlation attacks</b>: If you are connected to a node, and can recognise
    the keys being requested (probably because it was posted publicly), you can show 
    statistically that the node in question probably requested it, based on the 
    proportion of the keys requested from that node, the locations of nearby nodes, the 
    HTL on the requests and so on. This will be largely eliminated by tunnels (but these
    will be quite expensive so may need to be turned off by default except for 
    predictable blocks), but in any case it requires a rather powerful attacker compared 
    to the next attack... Note also that if you only connect to your friends, a remote
    attacker will have to either co-opt your friends or social engineer you into giving
    them a connection; either way, connecting to the entire network this way is rather 
    expensive: If they already suspect you personally they'll probably bug your keyboard
    rather than trying to connect to your Freenet node!</li>

  <li><b>Adaptive search</b>: If you want to find the author of some content, and you can
    predict the exact keys which will be inserted, and you are able to connect to new 
    nodes at will, you may be able to listen out for the keys, guess where they must have
    come from, connect to nodes near there, and if your guess is correct, get more keys
    which gives you a more accurate fix on the originator, so the attack gets faster and
    faster and eventually converges on the originator. This attack is most powerful with
    inserts of big, predictable files, but the "Insert a random, safe key" option will
    make the keys unpredictable even if the content is guessable, by using random 
    encryption keys. The downside is it produces a different key each time for the same
    file, and you can never safely reinsert the same file to the same key. Given that
    Freenet's data persistence is currently relatively poor, this is a problem. Anyway,
    if you <i>can</i> use the random keys option, the attacker is unable to move towards
    you until after you announce the file: Most of his samples will come not from the 
    actual content inserts but from chat posts. There are far fewer of these, and 
    changing your pseudonymous identity periodically will help, provided the attacker 
    cannot easily connect the new identity to the old one. Using a dedicated identity for
    posting sensitive content, which doesn't chat too much, again will help. Another 
    thing which makes a huge difference is connecting only to your friends (i.e. using
    darknet): This makes it extremely difficult for an attacker to get new connections 
    closer to where he thinks you must be, just as it helps with correlation attacks.
    So the biggest problems with this attack are 1) Files which are not very popular fall
    off Freenet relatively quickly, so need to be reinserted, but it is not safe to 
    reinsert to the same key (this is why we have the "Insert a canonical key" option,
    for those who don't care about attacks), and 2) Chat can still be attacked. Tunnels
    will help to deal with both problems, and by default will only be used for 
    predictable keys so can be relatively slow without this causing problems in practice.
    Also there is work going on on various techniques to allow users to do reinserts 
    safely via for example preventing the attacker from seeing requests started before he
    connected. Another important point is this only works if the source is uploading new
    content, or chatting, regularly; creating and bootstrapping a new pseudonymous 
    identity over a short period, doing a single insert (of any size) with the safe 
    random key option, and announcing it, should be relatively safe from this attack, 
    even on opennet - but see the section above on bootstrapping attacks.</li>

  <li><b>Traffic analysis</b>: Freenet provides minimal protection against global
    traffic analysis (basic message padding etc); if the attacker also has nodes on the 
    network, the extra data will likely be helpful. We certainly do not guarantee that it
    is impossible to trace data transfers from one node to the next with detailed traffic
    data, however it is hoped that this will fall down on the busier nodes. One day we 
    will implement steganographic transports and/or constant bitrate links as an option
    for more paranoid users. Note that on Tor-style networks, global traffic analysis 
    will defeat the network completely: all that is needed is to observe both the entry 
    and exit points.</li>

  <li><b>Swapping attacks</b>: It is possible to attack the location swapping algorithm, and
    thereby disrupt routing on friend-to-friend networks. This has been demonstrated by 
    the authors of the Pitch Black paper. We are working on a solution, but sadly at the
    moment most users use opennet.</li>
  </ul>
      
      <p>More information on the current practical state of Freenet security is available
  <a href="https://wiki.freenetproject.org/Security_summary">here</a>.
      </p>
      
      <p><b id="flooding">Is Freenet vulnerable to flooding attacks?</b><br>

  Short answer: no.</p>

      <p>Long answer:<br>
  We don't think so. Aside from protecting freedom of speech, Freenet
  is also designed to be an efficient dynamic caching system. If
  information is requested a lot from a limited number of nodes, the
  nodes that the requests pass through will cache the information,
  lowering the load on the network. If information is inserted on a
  limited set of nodes and then subsequently requested a lot from a
  separate set of nodes, with repetition, the sets will close in on one
  another in the network topology until they are "neighbors" and only the
  originally targeted nodes are suffering from the attack.</p>
      <p>In other words, in order to harm Freenet
  with a flood you need to consistently change your point of entry into
  the network and continually insert and request new data, and you will
  still only increase the workload for the network that is linear to your
  own. Given an immense will and capacity greater than the total of the
  entire network, it is possible to cripple any public network (including
  the Internet itself) with floods, but it is our intention to always
  keep Freenet as resistant to this as theoretically possible.</p>
      <p>Curiously enough, the above analysis only applies to <a href="https://wiki.freenetproject.org/Opennet">Opennet</a>.
  On Darknet, you might have a little more success, although it would be much harder to change your entry point in any significant way.
  Nonetheless, you have a reasonably low bandwidth multiplier (the total number of nodes visited, around 20 on average), and you are severely limited by the number of nodes you can connect to, which will be low on a darknet.</p>
      
      <p><b id="hash">Why hash keys and encrypt data when a node operator could identify them (the data) anyway if he tried?</b><br>

  Hashing the key and encrypting the data is not meant a method to keep Freenet
  Node operators from being able to figure out what type of information is
  in their nodes if they really want to (after all, they can just find
  the key in the same way as someone who requests the information would)
  but rather to keep operators from having to know what information is in
  their nodes if they don't want to. This distinction is more a legal one
  than a technical one. It is not realistic to expect a node operator to
  try to continually collect and/ or guess possible keys and then check
  them against the information in his node (even if such an attack is
  viable from a security perspective), so a sane society is less likely
  to hold an operator liable for such information on the network.</p>

      <p><b id="cancer">What about hostile "cancer" nodes within the network?</b><br>
  The existence of malicious nodes within the network is the most
  difficult problem that a distributed network must face, and has been
  the bane of many previous ideas. Many systems (such as multiplayer
  gaming networks) try to avoid malicious nodes by keeping the protocol
  and code closed, but we have yet to see an example of that working in
  the long run. And anyway it is opposed to Freenet's philosophy.</p>
      <p>Freenet
  is based on a balance of positive and negative feedback loops that bring
  requests for information to a node when it is functioning well, and
  keep requests away from it when it is not. The key to avoiding
  "cancers" is (as in the body) to make sure these loops can correctly
  identify even the most carefully designed malicious node and not keep
  sending requests to it. This issue is not fully dealt with by the
  current test code, but you can rest assured that a number of possible
  solutions have been on the table and discussed for some time now.
  Several have been implemented (enforcing hashes or signatures on content, 
  per node failure tables, backing off from a node that causes timeouts ...)</p>

      <p><b id="attackY">What about attack Y?</b><br>
  Freenet
  is still in testing and there are bound to be attacks found that we have
  not dealt with yet. So if you do manage to figure out a truly new kind
  of attack, we are interested in hearing about it. Please keep in mind
  what Freenet
  is and what it is not, however. No single network can offer everybody
  everything, and there are security issues that Freenet,
  by it's nature, may not deal with to extent you might wish. If this
  upsets you, all of our code is freely available, so you are free to
  take as much of it as you like and write your own distributed network
  that suits your desires. </p>

    <p><b id="privatedata">What private data does Freenet store? How do I get rid of it? How can I secure my computer so I am safe when running Freenet?</b><br>
  First of all, we <b>strongly</b> suggest that you install Freenet inside an encrypted 
  drive using, for example, <a href="http://www.truecrypt.org/">Truecrypt</a>. It is not
  possible for Freenet to prevent all leaks of private data, especially if you download
  media files etc. Even if you only browse freesites and use the chat plugins, there will
  still be potentially incriminating data in your swapfile, which needs to be encrypted
  (on recent versions of Windows you could try the command "fsutil behavior set 
  encryptpagingfile 1", but really the solution is to encrypt your whole system including swap). It is also 
  essential that you use your web browser in privacy mode, or with cache and history 
  turned off; we try to do this if you launch Freenet via the rabbit icon, but there are 
  no guarantees as unfortunately this functionality seems buggy in current web browsers.
  Browser plugins could also be a problem, and you should use a separate browser for 
  Freenet if in any doubt.
  Be careful with the files you download from Freenet - not only
  could anyone seizing your computer see you have them (media files are likely to be 
  written to disk even if you open them directly in your web browser and never save them), 
  but also they could contain threats to anonymity themselves, such as calling back to
  a malicious website etc; this is possible in for instance PDFs and some video formats.
  Freenet tries to warn you about this when it can't filter out such malicious content:
  Currently it can only filter HTML pages, GIF/PNG/JPEG images and CSS, and MP3s, but we will
  add support for Ogg soon and other formats later. And of course there are many other threats - you
  should take standard security precautions, such as not running operating systems that
  are no longer updated, not running software not from a trustworthy source, using 
  appropriate security software etc (if you have a firewall make sure it allows the two 
  UDP ports Freenet needs through).</p>

  <p>Because not all users will have installed encrypted drives at the time when they 
  first install Freenet, Freenet itself attempts to encrypt all the potentially incriminating
  data that it stores on disk. Details are below but as explained, leaks are inevitable:
  you really should <a href="http://www.truecrypt.org/">encrypt your disks!</a></p>

  <p>The main datastore does not store data you request or insert (or
  that is requested or inserted by nearby nodes), because it can be probed by other nodes:
  This was introduced to fix <a href="http://www.theregister.co.uk/2005/05/13/freener_not_so_anonymous/">this attack</a> publicised by The Register.
  Freenet has a separate client-cache, which stores data which you have recently requested
  to avoid having to go back to the network every time (which would not only reduce speed
  but also security, by giving attackers more opportunities to see your requests). Also, Freenet stores the list of your downloads
  and uploads (which you can see on the Filesharing menu), their current progress, and 
  various other data, in the file node.db4o (or node.db4o.crypt). The actual data is kept
  in the persistent-temp-* directory. Unless you set the physical security level to LOW,
  this data is encrypted. At MAXIMUM, the encryption keys are never written to disk, so
  the data is effectively wiped on restarting the node; otherwise the encryption keys are
  stored in a file called master.keys (on HIGH this is passworded). You can wipe the data
  by either using the panic button on the downloads/uploads page or by securely deleting
  master.keys. Freenet also creates temporary files for other requests, which are also
  encrypted unless physical seclevel is LOW, which are in temp-*. Also, some plugins may
  create their own data files, which may contain for instance messages you have posted or
  downloaded from chat forums, and currently bookmarks and recently completed files are
  stored in plain text. It is our intention to move these into node.db4o or store them
  in separate encrypted databases, as soon as we have automatic backups for node.db4o.
  See <a href="https://wiki.freenetproject.org/Program_files">here</a> for details 
  on some of the files.</p>

<p><b id="smartscreen">Windows SmartScreen filter warns the Freenet installer might put my PC at risk. What's going on?</b><br>
<a href="http://windows.microsoft.com/en-us/windows7/smartscreen-filter-frequently-asked-questions-ie9">SmartScreen</a>
is sometimes incorrect in classifying a file as dangerous. We believe
our installer is not infected with malicious software, and if you are a developer
you can check the installer source code <a href="https://github.com/freenet/wininstaller-innosetup">here</a>.
</p>
""")

class MailingListSection(Section):
    def __init__(self):
        self.slug = "mailing-lists"
        self.title = _("Mailing lists")
    def get_content(self):
        return text(md(_("""
These are the mailing lists that can be used for support or general information about Freenet.

### Subscribing

To subscribe to one of the lists, click the list name and give your email address in the field below the <span style="font-weight: bold;">Subscribing to <mailinglist></span> header. To enter a password is optional, and if you do not enter one, one will be automatically generated for you. Then press the <span style="font-weight: bold;">Subscribe</span> button. You will recieve a confirmation email, and when that is answered, you will recieve mails from the list.

### Unsubscribing

To unsubscribe to one of the lists you are subscribed to, click the list name and give your subscription email address under the heading <span style="font-weight: bold;"><mailinglist> Subscribers</span> and press the button <span style="font-weight: bold;">Unsubscribe or edit options</span>.

_**Note**: We constantly get requests of people who want to become unsubscribed._ <span style="text-decoration:underline;">YOU</span> _have to do that yourself! Just click on the www link provided at the bottom of every mail, enter your e-mail address in the text field in section "Subscribers" and provide your password under the unsubscribe option. (You can get your password there as well, in case you forgot it.)_

### The lists

*   [Announcements](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/announce/) ([archive](https://emu.freenetproject.org/pipermail/announce/))  
     Please sign up here to be notified of major Freenet developments, such as announcements of new releases or important bugfixes. This list is moderated and is very low traffic (less than one message per month).
*   [Support](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/support/) ([archive](https://emu.freenetproject.org/pipermail/support/))  
     Asking for or giving advice relating to getting Freenet working, bug reports, and suggestions on improving the user experience. Requests for help are more likely to be heard here than in the other mailing lists. **Note:** Emails sent to this mailing list from those not subscribed to the list must be manually approved, and this can impose a delay of several days. To avoid this delay, please [subscribe](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/support/).
*   [Tech](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/tech/) ([archive](https://emu.freenetproject.org/pipermail/tech/))  
     This is for general technical discussion of Freenet. If you want to discuss longer-term technical ideas about Freenet, please use this list.
*   [Development](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/devl/) ([archive](https://emu.freenetproject.org/pipermail/devl/))  
     This list is for active developers to discuss bugs, and the implementation of near-term new features. Please only post to this list if you know what you are talking about, otherwise use the tech mailing list (see above).
*   [Darknet-Tools](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/darknet-tools/) ([archive](https://emu.freenetproject.org/pipermail/darknet-tools/))  
     A mailing list to discuss and develop ways of extending the darknet while keeping it a darknet: Instant messenger plugins, IRC plugins, email invitations, functionality in the node needed to support these, and any other means of extending the darknet while keeping it a darknet as much as possible.
*   [Chat](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/chat/) ([archive](https://emu.freenetproject.org/pipermail/chat/))  
     This list is for general discussion of Freenet, topics that are not suitable to other lists. Discussions of politics, law, philosophy, lawsuits, programming languages, related technology that should not be part of Freenet, and any thread that the developers and users don't deem appropriate to the main lists should be discussed here. Questions such as "How can I prevent my node from being used by terrorists?", or "Why don't you rewrite Freenet in C++?" should be addressed to this list.

_**Third party tools**: We are hosting some other mailing lists on our server here is the [full list](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/)._
""")))

class SuggestionsSection(Section):
    def __init__(self):
        self.title = _("Suggestions")
        self.direct_link = "https://freenet.uservoice.com/"

class ChatSection(Section):
    def __init__(self):
        self.slug = "chat"
        self.title = _("Chat with us")
    def get_content(self):
        return text(md(_("""
Many of the developers and users of Freenet can often be found on an [IRC](https://en.wikipedia.org/wiki/IRC) channel, #freenet on chat.freenode.net. Almost everyone on the channel is a volunteer, and may be busy with other things, so you may not get an instant answer: **Ask your question/say what the problem is, then wait for a few minutes, and somebody may help you**.

[Chat with us](https://webchat.freenode.net/?randomnick=1&channels=freenet)

If you do not get an answer within the first few minutes, please keep the chat window open. We read our backlog, and if you stay, you will normally get an answer **within at most 4 hours** (when people with the relevant knowledge wake up).
""")))

class SetupSection(Section):
    def __init__(self):
        self.title = _("Setup")
        self.direct_link = "http://freesocial.draketo.de/"

class HelpPage(Page):
    def __init__(self):
        self.slug = "help"
        self.title = _("Help")
        self.first_section_in_menu = True
        self.sections = [
            FaqSection(),
            MailingListSection(),
            SuggestionsSection(),
            ChatSection(),
            SetupSection(),
            ]
