---
title: About
lang: fr
---

## What is Hyphanet?

> Je m’inquiète en permanence pour ma fille et Internet, bien qu’elle soit trop
> jeune pour s’être déjà connectée. Voici ce qui m’inquiète. Je m’inquiète que dans
> 10 ou 15 ans, elle viendrait me voir et me dirait «Papa, t’étais où quand ils
> ont supprimé la liberté de la presse sur Internet?»

--Mike Godwin, [Fondation Frontière électronique](https://www.eff.org/)

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zu9gM3_gIfM"
	frameborder="0" allowfullscreen></iframe>
</div>

Hyphanet is free software which lets you anonymously share files, browse and
publish "freesites" (web sites accessible only through Hyphanet) and chat on
forums, without fear of censorship. Hyphanet is decentralised to make it less
vulnerable to attack, and if used in “darknet” mode, where users only connect to
their friends, is very difficult to detect.

Communications by Hyphanet nodes are encrypted and routed through other
nodes to make it extremely difficult to determine who is requesting the
information and what its content is.

Users contribute to the network by giving bandwidth and a portion of their
hard drive (called the "data store") for storing encrypted chunks of data. 
Information is kept or deleted depending on the last time they were downloaded. 
Least accessed information is discarded to make way for other content.
This forms a privacy-preserving encrypted caching proxy. Chat, blogs, forums,
websites, radio streaming, are all built on top of this distributed
data store.

Hyphanet has been downloaded many millionss of times since the project started,
and used for the distribution of censored information all over the world
including countries such as China and in the Middle East. Ideas and concepts
pioneered in Hyphanet have had a significant impact in the academic world. 
We maintain a selection of [papers about Hyphanet](#papers).

Hyphanet has named its friend-to-friend mode "darknet" long before
this became a widespread term. By only connecting to people they
trust, users can greatly reduce their vulnerability, and yet still
connect to a global network through their friends' friends' friends.

### Current Contributors


Matthew Toseland

: Matthew has been working on Hyphanet since before the 0.5 release. His work
and that of others has resulted in dramatic improvements to the performance
and stability of the network.

Oskar Sandberg

: Oskar was also one of the earliest contributors to the Hyphanet Project,
and has made some important theoretical breakthroughs that lead to the
beginning of Hyphanet 0.7, see the papers page.

Florent Daignière

: Since 2003, Florent has improved various aspects of the software and
performed the project's system administration. In his day job, he is the
Technical Director of [Matta Consulting](https://www.trustmatta.com),
a boutique security consultancy firm and currently works on
 [safepass.me](https://safepass.me), an Active Directory password filter.

Michael Rogers

: Michael has mostly contributed detailed simulations as part of the Google
Summer of Code. He has been helpful in designing the [new transport layer](
https://old-wiki.freenetproject.org/NewTransportLayer).

Steve Dougherty

: The current release manager. He joined in GSoC 2013 and has been a
driving force behind tackling long standing issues in Hyphanet.


xor

: The Developer of the Web of Trust and Freetalk. He worked on the Web
of Trust in part-time for one year and is now working as volunteer
again.


David (Bombe) Roden

: The developer of the site insertion tool jSite and of Sone, the Social
Network over Hyphanet.


Ximin Luo

: A debian developer who currently works on packaging Hyphanet.


Bert Massop

: Works on the Hyphanet core and wherever there is need.


TheSeeker

: A long term contributor who, among other things, helps keep the
contact between the core developers and users in active subgroups.


Tommy[D]

: A Gentoo packager who untangled all the dependencies of Hyphanet and
packaged it cleanly in Gentoo.


Arne Babenhauserheide

: The current maintainer of pyHyphanet and infocalypse. He also writes
articles and tutorials for Hyphanet.


#### The translators

A dilligent team of people from various backgrounds who make it
possible to ship Hyphanet and this website in many different languages.


#### Many more great hackers

This list is missing many freesite authors, plugin writers, and a host
of other people who contributed in various ways.


### Anonymous Contributors


Eleriseth

: Works on Hyphanet core and communicates via FMS.


Somedude

: The developer of the Hyphanet-based Forum system FMS, of FreenetHG and
of FLIP, chat over Hyphanet.


The folks from Frost

: A group of users and programmers who use an old spammable
Hyphanet-based forum system which has been abandoned by most of the
core developers. They are active, however, and though it takes time
for their contributions to reach to core development, they take part
in Hyphanet development.



### Previous Contributors

Thomas Markus

: A dutch developer and statistic-enthusiast. He now works at Topicus.Education.

Ian Clarke

: Hyphanet is based on Ian's paper "A Distributed Decentralised Information
Storage and Retrieval System". Ian started the Hyphanet Project around July of
1999.

Scott Miller

: Scott is responsible for the implementation of much of the cryptography
elements within Hyphanet.

Steven Starr

: Steven helps with administration of Hyphanet Project Inc, and is an advisor to
the project on business and publicity matters.

Dave Baker

: Dave's main contribution has been [Freemail](documentation.html#freemail),
his Summer of Code project to build a working email-over-Hyphanet system,
as well as some debugging and core work in various places.

Robert Hailey

: Robert has helped improve the speed and security of Hyphanet by finding two
**major** bugs, and has recently contributed some code.

David Sowder

: David (Zothar) has helped the Hyphanet Project as time permits and interest
directs, including configuration, statistics and peer management via FCP,
the FProxy stats page and Node 2 Node Messages (N2NM/N2NTMs).

And **hundreds of others**, who either haven't asked to be added here, who
prefer to remain nameless, or who we just haven't got around to thanking. Not to
mention thousands of users, testers, and [donors](donate.html#sponsors)!

### Papers

![][icon_pdf] [Measuring Freenet in the Wild: Censorship-resilience under Observation]({static}/assets/papers/roos-pets2014.pdf) (PDF)
Observations and measurements on the live Hyphanet network. Includes suggestions
for improvement. This was submitted to PETS 2014.

![][icon_pdf] [The Dark Freenet]({static}/assets/papers/freenet-0.7.5-paper.pdf) (PDF)
Detailed paper about the Hyphanet 0.7.5 network, as opposed to its routing
algorithm, which is detailed in the below papers. Includes some new
simulations. This has been submitted to PET 2010.

![][icon_video] [Video of Small World talk, Berlin, December 2005](http://player.vimeo.com/video/22488244?title=0&byline=0&portrait=0)  
This is a video of a talk given by Ian Clarke and Oskar Sandberg at the Chaos
Computer Congress in Berlin, December 2005, describing the (then) new
architecture for Hyphanet 0.7\. You can also download the [slideshow](
/assets/papers/ccc-slideshow.pdf.bz2), and the source for the Java [demo](
/assets/papers/ccc-freenet-demo.tar.bz2) (requires Java 1.5).

![][icon_pdf] [Searching in a Small World]({static}/assets/papers/lic.pdf) (PDF)
Oskar Sandberg's licentiate thesis describing a simple decentralized
mechanism for constructing small world networks that is inspired by Hyphanet's
original design. Part II of the thesis describes the basis for the new
Darknet architecture.

![][icon_pdf] [Distributed routing in Small World Networks]({static}/assets/papers/swroute.pdf) (PDF)
A paper by Oskar Sandberg describing the theoretical basis for the new
"Darknet" routing mechanism employed by Hyphanet 0.7.

![][icon_pdf] Chaos Computer Congress Talk (slideshow)  
This is a [slideshow]({static}/assets/papers/ccc-slideshow.pdf.bz2) for a talk given
at the Chaos Computer Congress on 30th Dec 2005 in Berlin, Germany by Ian
Clarke and Oskar Sandberg. It described the new "darknet" approach to be
employed in Hyphanet 0.7\. A Java demonstration to accompany the talk is [
also]({static}/assets/papers/ccc-freenet-demo.tar.bz2) available.

![][icon_pdf] [Switching for a small world]({static}/assets/papers/vilhelm_thesis.pdf) (PDF)
A thesis by Vilhelm Verendel exploring ways to optimise the swapping algorithm.

![][icon_pdf] [Protecting Freedom of Information Online with Freenet]({static}/assets/papers/freenet-ieee.pdf) (PDF)
An IEEE Internet Computing article describing the Hyphanet architecture circa
2002 - probably the best introduction to the theory behind Hyphanet.

![][icon_pdf] [FreeNet White Paper]({static}/assets/papers/ddisrs.pdf) (PDF)
Original white paper by Ian Clarke, Division of Informatics, University of
Edinburgh 1999.

* * *

![][icon_pdf] [Attack Resistant Network Embeddings for Darknets](https://web.archive.org/web/20171210222609/https://www.ukp.tu-darmstadt.de/fileadmin/user_upload/Group_P2P/share/publications/Attack_Resistant_Network_Embeddings_for_Darknets.pdf) (PDF)  
A proposal for changing the darknet swapping algorithm which we are still
considering (we have some doubts about long-term performance).

![][icon_pdf] [A Contribution to Analyzing and Enhancing Darknet Routing](http://www.p2p.tu-darmstadt.de/publications/details/?no_cache=1&tx_bibtex_pi1%5Bpub_id%5D=TUD-CS-2013-0036) ([PDF](http://www.p2p.tu-darmstadt.de/fileadmin/user_upload/Group_P2P/share/INFOCOM.pdf))  
A proposal for changing the routing algorithm which we are still considering
(the worst case performance i.e. when a block has been lost may be
unacceptable).

![][icon_pdf] [Presentation: Towards "Dark" Social Networking Services (Strufe et al.)](https://www.icsi.berkeley.edu/icsi/sites/default/files/events/events_1303_strufe.pdf) (PDF)
An interesting presentation by the group responsible for the two above papers.

![][icon_pdf] [Pisces: Anonymous Communication Using Social Networks](http://arxiv.org/abs/1208.6326)  
An algorithm for setting up onion-like tunnels on darknets. 

![][icon_pdf] [Routing in the Dark: Pitch Black](http://grothoff.org/christian/pitchblack.pdf) ([citeseer](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.117.1543)) (PDF)  
A paper describing some attacks on Hyphanet 0.7's location swapping algorithm.
We have solutions for this but they are still being tested.

* * *

The most up to date reference is of course [the source code](
https://github.com/hyphanet/fred), but there is also some useful documentation on
[the wiki](https://wiki.freenetproject.org/) (you may have to search a bit),
and most implemented ideas have been discussed in detail on [the mailing
lists](help.html#mailing-lists) at some point, more recently often in-Hyphanet
forums such as FMS, or [the bug tracker](https://freenet.mantishub.io/) hosted by MantisHub.

[icon_pdf]: /assets/img/small-n-flat/file-pdf.png
[icon_video]: /assets/img/small-n-flat/file-video.png
