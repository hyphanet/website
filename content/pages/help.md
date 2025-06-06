---
title: Help
lang: en
---

## Philosophical

### What is Hyphanet?

Hyphanet is a platform for censorship-resistant communication and
publishing. It is designed to ensure true freedom of communication over
the Internet. It allows anybody to publish and read information with
complete anonymity. Nobody controls Hyphanet, not even its creators, meaning
that the system is not vulnerable to manipulation or shutdown. Hyphanet
is also very efficient in how it deals with information, adaptively
replicating content in response to demand.  For more information,
see [What is Hyphanet?](about.html#what-is-freenet)

### How is Hyphanet different to Tor? Can I access Google/Facebook/etc through Hyphanet?

Hyphanet is a self-contained network, while Tor allows accessing the web
anonymously, as well as using "hidden services" (anonymous web servers).
Hyphanet is not a proxy: You cannot connect to services like Google or
Facebook using Hyphanet. However, Hyphanet has websites, filesharing, forums,
chat, microblogging, email etc, all anonymous and hosted within Hyphanet.

Hyphanet is a distributed datastore, so once content is uploaded to Hyphanet,
it will remain on Hyphanet forever, as long as it remains popular, without
fear of censorship or denial of service attacks, and without needing to run
your own web server and keep it online constantly.

The other big difference is that Hyphanet has the "darknet" or Friend to
Friend mode, where your Hyphanet node (software on your computer) only
connects to the Hyphanet nodes run by your friends, i.e. people you know (and
maybe to their friends, to speed things up). This makes blocking Hyphanet,
e.g. on a national firewall, extremely difficult.

However, most people currently use Hyphanet in "opennet" mode (that is,
connecting automatically to whoever the network assigns, rather than
connecting only to their friends). This is much less secure than using
Hyphanet in "darknet" mode, and is relatively easy to block, as it does have
some central servers ("seed nodes").

Hyphanet has many unsolved problems, and is still experimental. Our objective
for Hyphanet is to build a global friend-to-friend darknet, which would be
extremely difficult to block, and would provide very strong anonymity and
censorship resistance. This will require further work on Hyphanet,
on usability, speed and security, but above all it is a techno-social
experiment: Will people know enough friends who are willing to use Hyphanet to
make such an anonymous friend-to-friend network possible? This is why Hyphanet
supports "opennet" mode: to let people try it out before they ask their
friends to connect.

Tor is a little less experimental, and arguably is an easier problem; it may
provide better anonymity today, provided that it isn't blocked, and of
course, Tor lets you access the internet as a whole, whereas on Hyphanet you
can only access Hyphanet content. However if you can use a large enough
darknet, Hyphanet already provides an interesting level of censorship
resistance, DoS resistance and anonymity.

Using the internet "anonymously" is not necessarily easy: Connecting to
Facebook through Tor doesn't prevent Facebook from knowing pretty much
everything about you, and connecting to your (non-HTTPS) webmail account
through Tor may mean the person running the proxy ("exit node") can steal
your webmail account password.

Hyphanet is a separate network, which does things differently, because there
are no central servers. This is why we don't support Javascript, server-side
scripting etc on freesites: Everything must be rewritten to work on a
distributed network. But the advantage is there is no single server which can
be compelled to hand over your private communications or which can be shut
down.

There are still risks, for example, talking about your home town or internet
provider on an anonymous forum, or downloading files which Hyphanet can't make
safe such as PDFs or word processor documents (Hyphanet will warn you about
this). Also, for web content in particular, it may be easier to upload it to
Hyphanet than set up a hidden server on Tor; you don't need to keep your node
online for your content to be available, you don't need to figure out how to
configure it safely, and most important, if you go away your site will still
be available.

### Summary:

Tor (or I2P):

* Lets you access the Internet (but be careful!).
* Lets you access anonymous web servers and other services.
* Lets you host anonymous web servers, which need to be kept online, and can be
  DoS'ed, but can run any dynamic or server-side content you want.
* Provides reasonable anonymity
* Has been blocked by several countries, with varying success. Even its hidden
  bridges can be harvested and blocked with moderate effort.
* Is somewhat centralised
* Is more mature and has more users and developers

Hyphanet in general:

* Only lets you access content uploaded to Hyphanet, including (static) websites,
  email, filesharing, forums, microblogging, etc. All of which are anonymous
  (or pseudonymous i.e. you create an untraceable identity).
* Hosts content in a distributed way: You don't know what your node is storing,
  any given content is distributed across many nodes.
* Ensures that popular content will be available forever.
* Is older than Tor, but more experimental (arguably it's a harder task).

Hyphanet in darknet mode: (friend to friend: connects only to your friends' nodes)

* Is very hard to block, and this can be improved further with transport plugins.
* Provides good anonymity, and with a bit more work it could provide very strong
  anonymity (PISCES tunnels).
* Is fully decentralised: No central servers at all.

Hyphanet in opennet mode: (connect automatically even if you don't know anyone
on Hyphanet)

* Is relatively easy to block.
* Provides limited anonymity
* Is somewhat centralised

Unfortunately most people use Hyphanet in opennet mode currently. The big
question is can we build a global friend-to-friend darknet? Join us and find
out!

PS for an example of how dependant Tor is on centralised hidden services,
see [this](http://www.twitlonger.com/show/n_1rlo0uu)
[bust](http://arstechnica.com/tech-policy/2013/08/alleged-tor-hidden-service-operator-busted-for-child-porn-distribution/).
Half the hidden services on Tor were using a single hosting service,
whose owner has now been arrested. While we don't approve of these sites,
it does illustrate the point: A centralised network is a vulnerable network.
Unfortunately, decentralised networks are hard, but in the long run they are
more secure.

### Who is behind Hyphanet?

Hyphanet grew out of a design for an anonymous publication system created by
Ian Clarke while a student at the University of Edinburgh, Scotland. Since
then many other people have contributed towards making Ian's proposal a
reality.

### If authors are anonymous how can you trust information?

Cryptographic signing of information allows people to prove authorship,
this technique is frequently used to authenticate authorship of emails.
Moreover, you can actually sign information while remaining anonymous,
thus having an anonymous persona. You can prove that you wrote different
pieces of information on Hyphanet, without revealing your identity. In this
way you can build up an anonymous reputation for reliability.

### Do I have to donate disk space and bandwidth?

You aren't really donating in the sense that you lose the disk space and the
bandwidth; but you aren't really sharing either (at least not the same way as
with filesharing programs). It is more like pitching in to the common Hyphanet
resource pool.

### I don't have to donate anything when using filesharing application X and I get to leech more.

Do you get to do that anonymously? Hyphanet is designed with anonymity in
mind, performance comes second.

### All my friends donate very little space and bandwidth. Should I donate more?

If you are happy with what you are getting then no. But if you want more you
should consider donating more and running your node as close to 24x7 as
possible, and you should ask your friends to do the same.

### If I donate a lot will my experience improve significantly?

Your experience will definitely get better, but for a really great
improvement we need more people to start thinking like you. Bandwidth counts
more than diskspace.

### Is Hyphanet legal?

We don't currently know of any prosecutions for merely using Hyphanet.
Some people claim that the [DADVSI](https://en.wikipedia.org/wiki/DADVSI)
makes Hyphanet illegal in France; the German data retention law might have
required logging, but [was struck down](http://en.wikipedia.org/wiki/Telecommunications_data_retention#Germany).
Also, the German supreme court has found that [not securing your wifi properly](http://merlin.obs.coe.int/iris/2010/7/article13.en.html)
makes you responsible for other people's downloads over it; this might or
might not be extended to prohibiting anonymous peer to peer filesharing such
as Hyphanet. [ACTA](http://en.wikipedia.org/wiki/ACTA) might have
wide-ranging effects, including on Hyphanet, should it pass, and similar laws
such as IPRED2 have been tried in the past. There have also been attempts to
force peer to peer systems to provide wiretapping capabilities in the USA,
and there are [worrying developments](http://www.bbc.co.uk/news/uk-politics-19968068)
in the UK that might result in it being blocked, but not being made illegal
per se. As far as we know none of these things - apart from the first two -
have passed. Many of these are arguable either way (depending on how broadly
the legislation is applied) and will have to be decided in caselaw. The law
can be an ass sometimes. You can read the EFF's (US-centric) advice to peer
to peer developers [here]( https://www.eff.org/wp/iaal-what-peer-peer-developers-need-know-about-copyright-law).
If you need legal advice, talk to a lawyer. Also read the next section
especially if you are in China; blocking the protocol may suggest the
authorities don't like us!

### Is Hyphanet blocked by national firewalls?

The Chinese national firewall (Golden Shield) has blocked our website for
many years, and was observed in 2005 to block the 0.5 protocol as well. This
suggests China doesn't like us, so be careful if you run Hyphanet in China.
Some other countries (e.g. France) are known to be hostile to peer to peer,
and may eventually force ISPs to block peer to peer networks (but right now
Hyphanet works fine in France and we have many French users!).

Technically, Hyphanet 0.7 has some minimal defences against blocking; the
protocol is relatively hard to identify (we are working on ["transport
plugins"](https://wiki.freenetproject.org/Transport_plugins), which would
[make it much harder to detect Hyphanet](http://en.wikipedia.org/wiki/Steganography).
Hyphanet supports a [darknet](https://wiki.freenetproject.org/Darknet) mode (i.e.
only connecting to your friends) which makes automated harvesting and
blocking of nodes very difficult. Note that many mobile internet providers
block all peer to peer networks along with other content, and many corporate
or academic networks may block Hyphanet (but even if they don't, see
[you shouldn't run Hyphanet at work](#can-i-get-in-trouble-if-i-run-a-node) for non-work purposes!).

There has been discussion in the US and UK of legislation to require
backdoors and presumably blocking of anything that can't be backdoored. This
is unlikely to pass, especially in the US, where similar laws have been
proposed periodically and are probably unconstitutional. However, even if the
government came to us and demanded a back door, we would be legally unable to
secretly distribute a trojan'ed build, because Hyphanet is open source,
numerous people have contributed code to it, so legally we have to give you
the source code, including that for any government mandated back doors -
which wouldn't be secret for long! If this happened it is likely that [
Hyphanet Project Incorporated](donate.html), the non-profit organisation that
runs this website and handles donations, would shut down, but the Hyphanet
network itself would live on just fine, the only difference being not being
able to pay full time developers as easily.

See [net neutrality](http://en.wikipedia.org/wiki/Network_neutrality) and
[the EFF](https://www.eff.org/) or equivalent organisations in your country for
the politics of all this and how you can stop such laws.

### Can I get trouble if I run a node?

This is related to ["Is Hyphanet legal?"](#legal). We have done everything we
can to make it extremely difficult for any sane legal system to justify
punishing someone for running a Hyphanet node, and there is little precedent
for such action in today's developed countries. Many legal systems recognize
the importance of freedom of speech, which is Hyphanet's core goal. Having
said that, there is risk in doing anything that your government might not
agree with; you should make an informed decision as to whether to take that
risk. Furthermore, your ISP or hosting provider may have a problem with
Hyphanet. At least one French hosting provider has been known to ban Hyphanet (
along with Tor and others) from their servers; please read your terms and
conditions to make sure you are allowed to run Hyphanet. Note also that
Hyphanet can use rather a lot of bandwidth, at least 20GB/month, and this may
be a problem on a cheap or shared connection. And of course running it at
work could get you into trouble too, unless it's for work purposes!

### What about copyright?

There are some excellent thoughts on this subject on the [Philosophy](
about.html#philosophy) page. Specific copyright-related laws may be a
problem, please read [Is Hyphanet legal?](#is-freenet-legal) and [Is Hyphanet blocked by
national firewalls?](#is-freenet-blocked-by-national-firewalls).

### What about child porn, offensive content or terrorism?

While most people wish that child pornography and terrorism did not exist,
humanity should not be deprived of their freedom to communicate just because
of how a very small number of people might use that freedom.

### I don't want my node to be used to harbor child porn, offensive content, or terrorism. What can I do?

This is a problem that sadly any censorship-resistance tool faces.
If the capacity to remove content existed, it might only be used to remove things one finds offensive, but it could be used to remove anything.
From a technological point of view one cannot have censorship-resistance with exceptions.
Hyphanet is merely a tool that by itself doesn't do anything to promote offensive content.
How people choose to use the tool is their sole responsibility.
As a communication medium, Hyphanet cannot be considered responsible for what people use it for — just like Internet Service Providers, telecoms, or postal services cannot be held responsible for their users either.

Note that files are encrypted and split into pieces.
They are not stored on your machine in their entirety.
Your instance of Hyphanet will likely have very few encrypted pieces of a given file, if any.
These pieces cannot be used as parts of the file they were made from without additional information.
Reassembling a file requires knowing both what pieces to use and the key to decrypt them, neither of which is included with each piece.

### How about encryption export restrictions?

The Hyphanet Project has notified the US authorities that it will be exporting
crypto. As long as your country doesn't prohibit the use of encryption you
are fine. Further, there is now an exception in the export laws for software
doing exactly what Hyphanet does! However, Oracle limits the encryption strength
available on the JVM that runs Hyphanet; you should install the Unlimited
Strength Policy Files for Java if possible to improve performance. Hyphanet
will however work even without this, by using its built-in encryption code.

### I have nothing to hide and don't need anonymity. Is there anything else Hyphanet can offer?

Yes, in fact even without the anonymity feature Hyphanet is very useful
because of the unique way it handles content distribution and information
load. In simple terms that means you can publish a website without worrying
about how big the site will be and without having to put someone else's ad
banners on it. While it is unlikely that freesites will ever load faster
than regular websites, they do adapt to sudden surges of visitors better (
which often happen when relatively unknown sites get linked to from a big
site), and reasonable download speeds for big files are feasible too. Just
don't expect very low latency.

## Technical

### How do I use this software? I downloaded it, but when I run it there's no GUI.

Fred (the Hyphanet REference Daemon) runs as a daemon, or service, in the
background. You normally talk to it through a Hyphanet client. One built-in
client is fproxy, which lets you talk to Hyphanet with a web browser. Hyphanet
should have installed a Browse Hyphanet shortcut on the desktop and/or the
start menu, or a system tray icon (rabbit) with an Open Hyphanet menu item.
Failing that, point your web browser to [http://127.0.0.1:8888/](
http://127.0.0.1:8888/) for the gateway page. Try clicking the various links
in the bookmark list to reach an initial set of sites.

### Why is Hyphanet so slow?

When you first install Hyphanet, it will be slow, and you may see Data Not
Found or Route Not Found errors for freesites. This is normal, and Hyphanet
will speed up significantly over time. For best performance you should try to
run Hyphanet as close to 24 hours a day as possible. This is why we install
Hyphanet as a service.

Please bear in mind that Hyphanet is inherently high latency: it can take a
while to (for example) load a page for the first time, even if it is capable
of reasonable speeds (as anonymous systems go!) for large popular files. You
can also improve performance for freesite browsing by using a separate
browser and [increasing its connection limit](#connections). You should also
set the datastore size and bandwidth limit as high as possible. But
protecting your anonymity does cost a certain amount of performance. You can
configure how much to a degree by changing the security levels on the page
under Configuration.

### Is Hyphanet searchable?

Yes, there are a few different search mechanisms. To search the Hyphanet web
(freesites), you should be able to just use the search box on the homepage,
or go to Search Hyphanet on the Browse submenu. If it's not there, go to the
Plugins page under Configuration, and load the Library plugin. Alternatively,
Frost and Thaw also provide searching for messages and files. Note that
searching on Hyphanet is a good deal more difficult than on other networks
because of Hyphanet's different architecture and design goals.

### How do I get Hyphanet working with a Firewall/NAT?

Mostly, Hyphanet should just work with a NAT. However, you should forward the
ports manually if you can. Click on the [Connectivity](
http://127.0.0.1:8888/connectivity/) page. At the top you will see a list of
ports used by the node. You should forward (for UDP) the Darknet FNP and
Opennet FNP ports. You may need to look up your router's documentation to
figure out how to do this. Hyphanet should have forwarded them itself through
[Universal Plug and Play](
https://en.wikipedia.org/wiki/Universal_Plug_and_Play), but this doesn't
always work (and it never works if you don't have the UPnP plugin loaded,
or have one router behind another).

If you have a dyndns address or other domain name pointing to the computer
you run your Hyphanet node on, tell the node about it. Go to [the core
settings config page](http://127.0.0.1:8888/config/node?mode=2) (in advanced
mode), and find the option "IP address override". Put your domain name in
that box, and apply the settings.

### Do I need a permanent Internet connection to run a node?

No, but it is preferred. You can run the software and test it from a
"transient" connection (e.g. dial up/mobile modem), but for the network as a
whole to be most useful, we will need as many permanent nodes as possible (
most cable modem or DSL setups are sufficiently "permanent" for this). A
later version of Hyphanet may take better advantage of transient nodes.

### Why does Hyphanet only download 1 or 2 files at a time?

Many browsers limit the number of simultaneous connections to something far
too low for efficiently browsing Hyphanet (since Hyphanet pages often have much
higher latency than web pages). This can usually be reconfigured. For
example, for Mozilla Firefox, type **about:config** in the address field of
the browser and replace the value of the following settings to the one
stated. Filter on **"connections"** to get only the relevant settings:

    network.http.max-connections 200  
    network.http.max-connections-per-server 200  
    network.http.max-persistent-connections-per-proxy 200  
    network.http.max-persistent-connections-per-server 200  

Note that these settings will cause mozilla to use more connections for all
your browsing, which may not be desirable from a network congestion point of
view. But you should ideally be using a separate browser for Hyphanet anyway,
for best security.

### Why can't Hyphanet store data permanently?

Because we can't find a way to do this without compromising Hyphanet's other
goals. For example, people often suggest that someone's node could just never
drop data they want to cache permanently. This, however, won't work because
even if the data is still available on their node, there is no way to ensure
that requests for that data will be routed to that node. We have considered
many other ways that Hyphanet could store data permanently, but they either
won't work, or compromise Hyphanet's core goals of anonymity, and scalability.

Content which is popular should persist indefinitely, for example most
freesites linked from the main indexes are still retrievable years later (at
least their front pages are). If the content isn't very popular the best way
to keep it available is to regularly re-insert (re-upload) it. An interesting
option is the "Keepalive" plugin, which will do this for you - even if you
didn't upload the file/site in the first place. Improvements are planned,
such as a special kind of request that allows us to probe whether a file is
available from a random point on the network.

### Why is Hyphanet implemented in Java?

Opinions differ about the choice of Java for the reference implementation of
Hyphanet (even among the core developers). [Ian Clarke](https://wiki.freenetproject.org/People#ian-clarke) and
several other developers are Java proponents and the choice for Java was
made. Even if everybody could be convinced to switch to a different language
reimplementing the current Hyphanet protocol would be quite a big task,
and take up a significant amount of time, while there is only a limited
amount of developer-time available. Flame wars on the development list about
the language choice aren't welcome, people willing to implement Hyphanet in
other languages however are very much encouraged to try. Don't underestimate
the amount of work however.

### How do I allow connections to FProxy from other computers?

If you want everyone to be able to use your node you have the following options:  

*   Go to the [web interface configuration page](http://127.0.0.1:8888/config/fproxy) and enable advanced mode
*   Stop your node and edit freenet.ini manually

In both cases change the following parameters:

    fproxy.bindTo=0.0.0.0  
    fproxy.allowedHosts=*  


Of course, this leaves your node wide open, unless you control access with a
firewall of some sort. If you'd prefer to use access controls within Hyphanet,
then you can use lines like this:

    fproxy.bindTo=0.0.0.0  
    fproxy.allowedHosts=127.0.0.1,192.168.1.0/24  

Or even (find your IP address from ipconfig/ifconfig/winipcfg and substitute
it for 192.168.1.1):

    fproxy.bindTo=127.0.0.1,192.168.1.1  
    fproxy.allowedHosts=127.0.0.1,192.168.1.0/24  

And if you want to grant full access (i.e. change config settings, restart,
etc) to the node (WARNING: Be very careful who you give full fproxy access
to!):

    fproxy.allowedHostsFullAccess=127.0.0.1,192.168.1.0/24  

### What's new? Is there a changelog?

On every new build, a brief summary of all the main changes is posted to the
support and devl lists and the eng.freenet board on Freetalk. This is usually
relayed to FMS and Frost too. Alternatively, for a much more detailed view,
check out the [git repositories](https://github.com/hyphanet/). Also,
you should check the developer blogs (from the default bookmarks, or over the
web, e.g. [toad](http://amphibian.dyndns.org/flogmirror/)), but be warned
they are often not regularly updated and frequently go off on rants on
unrelated topics!

### Why are there so many messages in my logfile with a backtrace attached?

Hyphanet logs messages excessively during normal operation. It's something we're
aware of and are working on.

### I have Kaspersky anti-virus, and Hyphanet doesn't install, or shows "Download/upload queue database corrupted!"

Kaspersky can be a problem with Hyphanet. See [here][url_kaspersky].
We recommend you turn off Kaspersky during install and during node startup, and exclude the directory you installed Hyphanet in (most likely C:\Program Files\Hyphanet or C:\Program Files (x86)\Hyphanet).

[url_kaspersky]: https://wiki.freenetproject.org/Installing/Windows#.27Download.2Fupload_queue_database_corrupted.21.27_.28When_using_Kaspersky_on_Windows_7.29

### I set a password and now I forgot it, what can I do?

The password protects your downloads and uploads and the client-cache (cache
of what you've recently browsed on Hyphanet). It is stored in the file
master.keys. There is no way to recover the password, but if you forget it
you can wipe your downloads and uploads and the client cache by securely
deleting the file master.keys. See [the question on private data and local
security](#privatedata) for more information.

### Hyphanet keeps complaining about clock skew

Hyphanet will have problems if your clock is constantly being rewound. Usually
this happens when something is resetting your clock regularly in big jumps.
On Linux, you should run ntpd to make sure your clock isn't too far off (this
isn't vital but it's helpful), but if you see clock skew errors, try adding
the -x option to it to avoid big backwards jumps. Also, running ntpdate on
startup so there is one big jump before Hyphanet starts is a good idea. This
can also happen on Windows sometimes, let us know how you managed to fix it
... generally it's not all that serious though, especially if big jumps in
the clock are only once a day.

## Publishing

### If I publish something in Hyphanet, how will people find it? Don't they have to know the key I used?

Yes, people will have to know what key you used to publish your information.
This means you will have to announce your key in some way.

The most common way to do this is to send a message, containing your key and
brief description of your information, to the author of one of the existing
Hyphanet sites. Most of the "portal" sites which are linked from the Hyphanet
web interface (fproxy) read the Freetalk or FMS forums, and there are boards
specifically for announcing sites (usually the boards are called "sites"!).
You could also send your key to people by using the Hyphanet [mailing lists](
help.html#mailing-lists), in the IRC channel (libera.chat #freenet),
by private e-mail, or by advertising your Hyphanet site on your World Wide Web
site. If you're feeling extravagant, you could even try skywriting it.
(Graffiti is not recommended, for legal reasons.)

### How do I publish a Content Hash Key (CHK)?

A Content Hash Key is based on the actual content contained within it - and
as such, the key will only be known after it has been inserted into Hyphanet.
To insert a CHK, simply insert it as "CHK@", Hyphanet will tell you what the
actual CHK is once the insertion completes.

### Can Hyphanet documents be updated / deleted?

Currently, a document posted to freenet with the same name as one already
present may actually serve to propagate the existing document. there is also
currently no means of deleting a document from freenet. documents that are
never requested are eventually removed through disuse.

however, you can use an [updatable subspace key (usk)](
https://wiki.freenetproject.org/usk) to provide a form of updatable freesite:
your node will automatically look for later editions of the site (after you
visit it, or always if you bookmark it), and show you the latest version. you
can force it to search for the latest version by changing the number at the
end of the key to negative.

## Contributing

### I have this great idea...

Good! First step: read the [mailing list archives](help.html#mailing-lists).
Odds are good that someone else had the same idea and discussed it with the
group. Either a flaw was found in the idea, or perhaps it was decided to
postpone implementing the idea until later. Some examples of ideas already
discussed are storing information by content hash, key redirection, signed
keys/data, use of UDP, server discovery, URLs, document versioning,
and others. If you don't see the idea discussed in the archives, by all means
bring it up in the appropriate [mailing list](help.html#mailing-lists).

### Can I contribute to the Hyphanet Project?

Absolutely. Even if you don't have the time or skills to become a
co-developer of the project, you can contribute in other ways:

* Help test Hyphanet by installing and configuring the server software on your
  machine.
* Install the client software on your machine to test retrieving information and
  publishing your own.
* Work on the Hyphanet web site (including the FAQ).
* Contribute your ideas to the discussion lists.
* [Translate the user interface](https://wiki.freenetproject.org/Translation)
  into another language.

If you are a developer, you can help by working on Hyphanet itself,
or by creating other applications to run on Hyphanet. External applications
(such as FMS, the main forums system used on Hyphanet) use [the Hyphanet Client
Protocol](https://wiki.freenetproject.org/FCPv2) to talk to Fred. Another
possibility is writing plugins - these are written in Java and run in
Hyphanet's JVM, and can be bundled with Hyphanet when they are ready. A popular
plugin is Sone, which is a microblogging/social app over Hyphanet. You can see
how to install FMS and Sone on e.g. the Hyphanet Social Networking Guide
freesite.

If you want to work on Hyphanet itself, see:

* [Source code](https://github.com/hyphanet/fred)
* [Roadmap](https://wiki.freenetproject.org/Roadmap)
* [Development page](https://wiki.freenetproject.org/Development)

Improvements to this website, fixes for
spelling/grammar mistakes, new ideas (see [the previous answer](#idea)),
are all welcome. You may find [the wiki](
https://wiki.freenetproject.org/Main_Page) helpful.

If you have any questions about contributing, please contact us, via [the developers mailing list][url_devlist], [the chat channel][url_chat], [the support mailing list][url_supportlist] or anonymously via the freenet board on FMS.

Last but not least you can [donate][url_donate] to support our paid
developer(s) and cover server costs.

[url_devlist]: #mailing-lists
[url_supportlist]: #mailing-lists
[url_chat]: #irc
[url_donate]: donate.html

### How can I access the code and website?

See our [GitHub repository](https://github.com/hyphanet/).

### What tools do I need to help develop?

Building Hyphanet requires JDK 1.8 or later.  You can download the source tarballs on the
download page for a specific build, or use git to get an up to date copy of
the source, see [here](https://wiki.freenetproject.org/Development) for details. Further
instructions for building and deploying the server are included with the code
itself. Generally speaking, joining our IRC channel is a good idea: [#freenet
on libera.chat](ircs://irc.libera.chat:6697/freenet)

### Is there a Help Site that goes deeper into the questions newbies may have about Hyphanet, and where people can contribute too?

Have a look at [our wiki](https://wiki.freenetproject.org/). An older wiki,
which is now read-only, but has a fair amount of content so is sometimes
helpful is [here](https://old-wiki.freenetproject.org/). There are also
several implementations of wiki's over Hyphanet. The most recent one is called
Jfniki. There is a link in the default bookmarks on the Browse Hyphanet page
after you install Hyphanet.

### Where can I report bugs?

You can use our [bug tracking system](https://freenet.mantishub.io/) hosted by MantisHub or
send a mail to our [support mailing list](help.html#mailing-lists).

### I'm a theoretical computer scientist/mathematician, how can I help?

See [here](https://wiki.freenetproject.org/Research_challenges).

## Security

### Can I use my regular browser to browse Hyphanet?

Hyphanet has a web interface: much of the content on Hyphanet is in the form of
"freesites", and downloads, configuration and friend connections can be
managed from the web interface. However, because of weaknesses in current
browsers, we **strongly** recommend that you use a separate browser for
Hyphanet. Specifically, browser history stealing, in all its forms, is a major
threat if you share a browser between Hyphanet and the WWW at large: malicious
web pages will be able to probe which freesites you have visited, and report
this information to their owners.

Privacy/incognito mode may be sufficient, and Windows tray app will start a
browser running in this mode.

### Won't attack X break Hyphanet's anonymity?

**Short answer**: Probably, on opennet. Maybe, on darknet.

**Long answer**:

Hyphanet has a different threat model to Tor and the Mixmaster remailers.
Hyphanet is designed to resist censorship: The network must therefore be
robust, and content must be distributed without requiring a central server,
whether anonymous or not. Anonymity is important for requesters and
especially for those who upload content in the first place. The typical
example is a corporate or government whistleblower. Generally to find the
originator of some content, the attacker must be able to predict the data in
advance, must be able to move across the network relatively quickly, and must
be able to perform the attack while the data is being inserted; after that,
it is distributed across the network and is much harder to trace, and the
originator may have left the network. However, if by chance or by
overwhelming force the attacker is connected to the whistleblower (or e.g.
seizes the computers of everyone on the network), they may be able to identify
this much more quickly. All of this is vastly more difficult on a darknet,
where everyone connects only to their friends, where it is very hard for an
attacker to find nodes, and where to connect to a given node they must social
engineer its operator! Hyphanet does support opennet mode (plug and play),
but darknet is far more secure, and far more difficult to block on a national
firewall.

Tor on the other hand is designed to anonymise real-time data streams,
on the assumption that the list of nodes can be public, that there is a free
world where nodes can be operated safely, that the authors of controversial
content will be able to either host (hidden) web servers themselves or upload
it to other (hidden, but usually centralised) storage systems, and so on. And
Tor has a concept of a "client", which is somebody who uses the service
without providing any value to it; on Hyphanet, every node relays data for its
neighbours. Hence the attacks on Hyphanet are completely different to the
attacks on Tor. Both compromise to some degree to enable more or less
real-time performance.

If you can use the darknet, trust your friends, don't reinsert files, always
use the "Insert a random, safe key" option, and change your anonymous
identity after some volume of inserts, you should be relatively safe using
Hyphanet. However this has not yet been quantified. If you can connect,
build up some trust in your anonymous persona, insert your controversial
content, and then disappear, again, you are better off with Hyphanet,
especially if the content is a website (but if you are connecting on opennet,
beware of seednode compromises). In some other cases, Tor is better.

We are still working on Hyphanet's security and there are major security
enhancements which have not yet been implemented, most of which will go in
before 1.0\. Cryptographic tunnels similar to Tor's onion routing are one
possibility, which would greatly reduce the impact of many of the below
attacks, but there are several other enhancements planned, both to anonymity
and to network robustness/undetectability.

**Major known attacks**:

In the interests of giving would-be users as much information as possible,
and on the assumption that any serious attacker would do their homework,
here are the major classes of attack on Hyphanet we are presently aware of:

* **Harvesting**: Simply by running some powerful Hyphanet nodes, an attacker can
  identify most of the opennet (Strangers network) relatively easily. These
  nodes can then be attacked one by one (subject to resources), their traffic
  analysed, or simply be blocked on a national firewall. Connecting only to
  friends (darknet) largely solves this problem. ISPs may be able to identify
  Hyphanet nodes with some effort, although we make this fairly difficult:
  Hyphanet's current protocol is designed to be hard to detect, and steganography
  will be introduced at some point. However, traffic flow analysis, or
  brute-force blocking of all peer to peer traffic (e.g. traffic between IP
  addresses marked as "consumer" rather than "business"), both of which would
  hit a lot of things other than Hyphanet, would likely be effective for quite
  some time.

* **Bootstrapping attacks**: Unless a node only connects to friends, it will
  have to connect to the opennet "seednodes" to announce itself and get
  initial peers to connect to. At the moment there are relatively few
  seednodes and the list is maintained manually. The seednodes could be blocked
  easily by a national firewall etc, but also, there is little to prevent
  attackers from setting up their own seednodes and submitting them, and then
  "capturing" any new Hyphanet users who connect to their nodes, in order to
  observe their traffic etc. Hyphanet will try to announce to multiple seednodes,
  but see the below section on "correlation attacks", which generally are
  feasible with only a single connection to the target. So this is a question of
  resources - if the attacker has the resources to surveil all new Hyphanet
  nodes, they have a good chance of pulling it off. In future we may have more
  seednodes, and only reveal a small proportion of them to each node, as Tor
  does with its hidden bridges, but that will not prevent attackers from
  creating lots of malicious seednodes and getting them into the official lists,
  and it will likely still be possible to block all the seednodes with some
  effort (something similar has already happened to Tor hidden bridges in
  China). Combined with harvesting and adaptive search attacks, this attack
  explains why opennet is regarded by many core developers as hopelessly
  insecure. If you want good security you need to connect only to friends. Hit
  and run inserts are possible, and can be relatively safe in terms of many of
  the other attacks, but you are taking the risk that the opennet seednode you
  connect to may be malicious.

* **Correlation attacks**: If you are connected to a node, and can recognise the
  keys being requested (probably because it was posted publicly), you can show
  statistically that the node in question probably requested it, based on the
  proportion of the keys requested from that node, the locations of nearby
  nodes, the HTL on the requests and so on. This will be largely eliminated
  by tunnels (but these will be quite expensive so may need to be turned off
  by default except for predictable blocks), but in any case it requires a
  rather powerful attacker compared to the next attack... Note also that if you
  only connect to your friends, a remote attacker will have to either co-opt
  your friends or social engineer you into giving them a connection; either way,
  connecting to the entire network this way is rather expensive: If they already
  suspect you personally they'll probably bug your keyboard rather than trying
  to connect to your Hyphanet node!

* **Adaptive search**: If you want to find the author of some content, and you
  can predict the exact keys which will be inserted, and you are able to
  connect to new nodes at will, you may be able to listen out for the keys,
  guess where they must have come from, connect to nodes near there, and if your
  guess is correct, get more keys which gives you a more accurate fix on the
  originator, so the attack gets faster and faster and eventually converges on
  the originator. This attack is most powerful with inserts of big, predictable
  files, but the "Insert a random, safe key" option will make the keys
  unpredictable even if the content is guessable, by using random encryption
  keys. The downside is it produces a different key each time for the same file,
  and you can never safely reinsert the same file to the same key. Given that
  Hyphanet's data persistence is currently relatively poor, this is a problem.
  Anyway, if you _can_ use the random keys option, the attacker is unable to
  move towards you until after you announce the file: Most of his samples will
  come not from the actual content inserts but from chat posts. There are far
  fewer of these, and changing your pseudonymous identity periodically will
  help, provided the attacker cannot easily connect the new identity to the old
  one. Using a dedicated identity for posting sensitive content, which doesn't
  chat too much, again will help. Another thing which makes a huge difference is
  connecting only to your friends (i.e. using darknet): This makes it extremely
  difficult for an attacker to get new connections closer to where they think you
  must be, just as it helps with correlation attacks. So the biggest problems
  with this attack are 1) Files which are not very popular fall off Hyphanet
  relatively quickly, so need to be reinserted, but it is not safe to reinsert
  to the same key (this is why we have the "Insert a canonical key" option, for
  those who don't care about attacks), and 2) Chat can still be attacked.
  Tunnels will help to deal with both problems, and by default will only be used
  for predictable keys so can be relatively slow without this causing problems
  in practice. Also there is work going on on various techniques to allow users
  to do reinserts safely via for example preventing the attacker from seeing
  requests started before they connected. Another important point is this only
  works if the source is uploading new content, or chatting, regularly; creating
  and bootstrapping a new pseudonymous identity over a short period, doing a
  single insert (of any size) with the safe random key option, and announcing
  it, should be relatively safe from this attack, even on opennet - but see the
  section above on bootstrapping attacks.

* **Traffic analysis**: Hyphanet provides minimal protection against global
  traffic analysis (basic message padding etc); if the attacker also has
  nodes on the network, the extra data will likely be helpful. We certainly do
  not guarantee that it is impossible to trace data transfers from one node to
  the next with detailed traffic data, however it is hoped that this will fall
  down on the busier nodes. One day we will implement steganographic transports
  and/or constant bitrate links as an option for more paranoid users. Note that
  on Tor-style networks, global traffic analysis will defeat the network
  completely: all that is needed is to observe both the entry and exit points.

* **Swapping attacks**: It is possible to attack the location swapping
  algorithm, and thereby disrupt routing on friend-to-friend networks. This has
  been demonstrated by the authors of the Pitch Black paper. We are working on a
  solution, but sadly at the moment most users use opennet.

More information on the current practical state of Hyphanet security is available
[here](https://wiki.freenetproject.org/Security_summary).

### Is Hyphanet vulnerable to flooding attacks?

Short answer: no.

Long answer:

We don't think so. Aside from protecting freedom of speech, Hyphanet is also
designed to be an efficient dynamic caching system. If information is
requested a lot from a limited number of nodes, the nodes that the requests
pass through will cache the information, lowering the load on the network. If
information is inserted on a limited set of nodes and then subsequently
requested a lot from a separate set of nodes, with repetition, the sets will
close in on one another in the network topology until they are "neighbors"
and only the originally targeted nodes are suffering from the attack.

In other words, in order to harm Hyphanet with a flood you need to
consistently change your point of entry into the network and continually
insert and request new data, and you will still only increase the workload
for the network that is linear to your own. Given an immense will and
capacity greater than the total of the entire network, it is possible to
cripple any public network (including the Internet itself) with floods,
but it is our intention to always keep Hyphanet as resistant to this as
theoretically possible.

Curiously enough, the above analysis only applies to [Opennet](
https://wiki.freenetproject.org/Opennet). On Darknet, you might have a little
more success, although it would be much harder to change your entry point in
any significant way. Nonetheless, you have a reasonably low bandwidth
multiplier (the total number of nodes visited, around 20 on average), and you
are severely limited by the number of nodes you can connect to, which will be
low on a darknet.

### Why hash keys and encrypt data when a node operator could identify them (the data) anyway if they tried?

Hashing the key and encrypting the data is not meant a method to keep Hyphanet
Node operators from being able to figure out what type of information is in
their nodes if they really want to (after all, they can just find the key in
the same way as someone who requests the information would) but rather to
keep operators from having to know what information is in their nodes if they
don't want to. This distinction is more a legal one than a technical one. It
is not realistic to expect a node operator to try to continually collect and/
or guess possible keys and then check them against the information in his
node (even if such an attack is viable from a security perspective),
so a sane society is less likely to hold an operator liable for such
information on the network.

### What about hostile "cancer" nodes within the network?

The existence of malicious nodes within the network is the most difficult
problem that a distributed network must face, and has been the bane of many
previous ideas. Many systems (such as multiplayer gaming networks) try to
avoid malicious nodes by keeping the protocol and code closed, but we have
yet to see an example of that working in the long run. And anyway it is
opposed to Hyphanet's philosophy.

Hyphanet is based on a balance of positive and negative feedback loops that
bring requests for information to a node when it is functioning well,
and keep requests away from it when it is not. The key to avoiding "cancers"
is (as in the body) to make sure these loops can correctly identify even the
most carefully designed malicious node and not keep sending requests to it.
This issue is not fully dealt with by the current test code, but you can rest
assured that a number of possible solutions have been on the table and
discussed for some time now. Several have been implemented (enforcing hashes
or signatures on content, per node failure tables, backing off from a node
that causes timeouts ...)

### What about attack Y?

Complex software free from security vulnerabilities is essentially impossible, and there are bound to be attacks that we
are unaware of or have not yet been able to prevent. If you believe you have discovered a new kind
of attack, we are interested in hearing about it. Please keep in mind what
Hyphanet is and what it is not, however. No single network can offer everybody
everything, and there are security issues that Hyphanet, by its nature,
may not deal with to extent you might wish. If this upsets you, all of our
code is freely available, so you are free to take as much of it as you like
and write your own distributed network that suits your desires.

### What private data does Hyphanet store? How do I get rid of it? How can I secure my computer so I am safe when running Hyphanet?

First of all, we **strongly** suggest that you install Hyphanet inside an
encrypted drive using, for example, [Veracrypt](https://veracrypt.fr/).
It is not possible for Hyphanet to prevent all leaks of private data,
especially if you download media files etc. Even if you only browse freesites
and use the chat plugins, there will still be potentially incriminating data
in your swapfile, which needs to be encrypted (on recent versions of Windows
you could try the command "fsutil behavior set encryptpagingfile 1",
but really the solution is to encrypt your whole system including swap). It
is also essential that you use your web browser in privacy mode, or with
cache and history turned off; we try to do this if you launch Hyphanet via the
rabbit icon, but there are no guarantees as unfortunately this functionality
seems buggy in current web browsers. Browser plugins could also be a problem,
and you should use a separate browser for Hyphanet if in any doubt. Be careful
with the files you download from Hyphanet - not only could anyone seizing your
computer see you have them (media files are likely to be written to disk even
if you open them directly in your web browser and never save them), but also
they could contain threats to anonymity themselves, such as calling back to a
malicious website etc; this is possible in for instance PDFs and some video
formats. Hyphanet tries to warn you about this when it can't filter out such
malicious content: Currently it can only filter HTML pages, GIF/PNG/JPEG
images and CSS, and MP3s, but we will add support for Ogg soon and other
formats later. And of course there are many other threats - you should take
standard security precautions, such as not running operating systems that are
no longer updated, not running software not from a trustworthy source,
using appropriate security software etc (if you have a firewall make sure it
allows the two UDP ports Hyphanet needs through).

Because not all users will have installed encrypted drives at the time when
they first install Hyphanet, Hyphanet itself attempts to encrypt all the
potentially incriminating data that it stores on disk. Details are below but
as explained, leaks are inevitable: you really should [encrypt your disks!](
https://veracrypt.fr/)

The main datastore does not store data you request or insert (or that is
requested or inserted by nearby nodes), because it can be probed by other
nodes: This was introduced to fix [this attack](
http://www.theregister.co.uk/2005/05/13/freener_not_so_anonymous/) publicised
by The Register. Hyphanet has a separate client-cache, which stores data which
you have recently requested to avoid having to go back to the network every
time (which would not only reduce speed but also security, by giving
attackers more opportunities to see your requests). Also, Hyphanet stores the
list of your downloads and uploads (which you can see on the Filesharing
menu), their current progress, and various other data, in the file node.db4o
(or node.db4o.crypt). The actual data is kept in the persistent-temp-*
directory. Unless you set the physical security level to LOW, this data is
encrypted. At MAXIMUM, the encryption keys are never written to disk, so the
data is effectively wiped on restarting the node; otherwise the encryption
keys are stored in a file called master.keys (on HIGH this is passworded).
You can wipe the data by either using the panic button on the
downloads/uploads page or by securely deleting master.keys. Hyphanet also
creates temporary files for other requests, which are also encrypted unless
physical seclevel is LOW, which are in temp-*. Also, some plugins may create
their own data files, which may contain for instance messages you have posted
or downloaded from chat forums, and currently bookmarks and recently
completed files are stored in plain text. It is our intention to move these
into node.db4o or store them in separate encrypted databases, as soon as we
have automatic backups for node.db4o. See [here](
https://wiki.freenetproject.org/Program_files) for details on some of the
files.

### Windows SmartScreen filter warns the Hyphanet installer might put my PC at risk. What's going on?

[SmartScreen][url_smartscreen] is sometimes incorrect in classifying a file as dangerous.
We believe our installer is not infected with malicious software, and if you are a developer you can check the installer source code [here][url_installer].

[url_smartscreen]: http://windows.microsoft.com/en-us/windows7/smartscreen-filter-frequently-asked-questions-ie9
[url_installer]: https://github.com/hyphanet/wininstaller-innosetup

### Has anyone ever faced legal trouble for their anonymous activities conducted on Hyphanet?

Yes. We do know of some such instances.

United States law enforcement can identify anonymous users of [Hyphanet][f] and [Tor][t].
We have [some information about the techniques used][le_technique], and we suspect it primarily affects people using the network security level "normal" or lower.
It is reasonable to assume that other governments have access to the same technology, which is provided by private contractors.
If you are concerned about governments, you should use Hyphanet's capacity to connect only to users you trust, ("high" network security level or higher) and bear in mind that no anonymity technology provides perfect protection.

While we applaud law enforcement's apparent success in apprehending suspects allegedly sharing child abuse images, any security flaws they may have used are not limited to such noble usage.
Many governments persecute and prosecute political dissidents for legitimate speech published online.
Therefore we hope to discover and fix these flaws to protect those who fight for human rights, against corruption, for a peaceful future, and for other legitimate goals.

[f]: http://www.thedickinsonpress.com/news/north-dakota/3885239-predators-police-online-struggle
[t]: http://motherboard.vice.com/read/court-docs-show-a-university-helped-fbi-bust-silk-road-2-child-porn-suspects
[le_technique]: the-discredited-levine-2017-approach-is-still-used.html

### Additional information sources

*   [Wiki FAQ page][url_wiki]
*   [Security summary][url_security]
*   [High quality copy of the rabbit icon][url_rabbit_icon]

[url_wiki]: https://wiki.freenetproject.org/FAQ
[url_security]: https://wiki.freenetproject.org/Security_summary
[url_rabbit_icon]: assets/img/rabbit/freenet-bunny.svg

## Mailing lists
<a name="mailing-lists"></a>

These are the mailing lists that can be used for support or general
information about Hyphanet.

* [Support](https://ml.freenetproject.org/v1/) ([archive](https://www.mail-archive.com/support@freenetproject.org/))<br/>
  Asking for or giving advice relating to getting Hyphanet working,
  bug reports, and suggestions on improving the user experience. Requests for
  help are more likely to be heard here than in the other mailing lists.
* [Development](https://ml.freenetproject.org/v1/) ([archive](https://www.mail-archive.com/devl@freenetproject.org/))<br/>
  This list is for active developers to discuss bugs, and the implementation
  of near-term new features.

## Get Support
You can find information about installing Hyphanet in the [Wiki][wiki_link]
especially in the [Installing Hyphanet][install_link] and [FAQ][faq_link].

When Hyphanet is already installed you may get support in [FMS][fms_link] forum.

When writing your support request, please make sure you include a full description of the problem, your current version of Java, your operating system and current Hyphanet version.

[wiki_link]: https://wiki.freenetproject.org/Main_Page
[install_link]: https://wiki.freenetproject.org/Installing-Hyphanet
[faq_link]: https://wiki.freenetproject.org/FAQ
[fms_link]: https://wiki.freenetproject.org/FMS

## Chat with us

Many of the developers and users of Hyphanet are on the [IRC](
https://en.wikipedia.org/wiki/IRC) channel #freenet on irc.libera.chat.

<a href="https://web.libera.chat/?nick=FollowRabbit|?#freenet" id="chatlink" class="btn button-custom btn-custom-two">Chat with us</a>

## [Setup](http://freesocial.draketo.de/)

