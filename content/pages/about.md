---
title: About
---

## What is Freenet?

> I worry about my child and the Internet all the time, even though she's too
> young to have logged on yet. Here's what I worry about. I worry that 10 or
> 15 years from now, she will come to me and say 'Daddy, where were you when
> they took freedom of the press away from the Internet?

--Mike Godwin, [Electronic Frontier Foundation](https://www.eff.org/)

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zu9gM3_gIfM"
	frameborder="0" allowfullscreen></iframe>
</div>

Freenet is free software which lets you anonymously share files, browse and
publish "freesites" (web sites accessible only through Freenet) and chat on
forums, without fear of censorship. Freenet is decentralised to make it less
vulnerable to attack, and if used in "darknet" mode, where users only connect to
their friends, is very difficult to detect.

Communications by Freenet nodes are encrypted and are routed through other
nodes to make it extremely difficult to determine who is requesting the
information and what its content is.

Users contribute to the network by giving bandwidth and a portion of their
hard drive (called the "data store") for storing files. Files are
automatically kept or deleted depending on how popular they are, with the
least popular being discarded to make way for newer or more popular content.
Files are encrypted, so generally the user cannot easily discover what is in
his datastore, and hopefully can't be held accountable for it. Chat forums,
websites, and search functionality, are all built on top of this distributed
data store.

Freenet has been downloaded over 2 million times since the project started,
and used for the distribution of censored information all over the world
including countries such as China and in the Middle East. Ideas and concepts
pioneered in Freenet have had a significant impact in the academic world. Our
2000 paper "Freenet: A Distributed Anonymous Information Storage and
Retrieval System" was the most cited computer science paper of 2000 according
to Citeseer, and Freenet has also inspired papers in the worlds of law and
philosophy. Ian Clarke, Freenet's creator and project coordinator,
was selected as one of the top 100 innovators of 2003 by MIT's Technology
Review magazine.

An important recent development, which very few other networks have, is the
"darknet": By only connecting to people they trust, users can greatly reduce
their vulnerability, and yet still connect to a global network through their
friends' friends' friends and so on. This enables people to use Freenet even
in places where Freenet may be illegal, makes it very difficult for
governments to block it, and does not rely on tunneling to the "free world".

*Written by Ian Clarke*

1.  [A Disclaimer](#a-disclaimer)
2.  [Suggested prior reading](#suggested-prior-reading)
3.  [The importance of the Free flow of information](#the-importance-of-the-free-flow-of-information)
4.  [Censorship and freedom](#censorship-and-freedom)
5.  [The solution](#the-solution)
6.  [Isn't censorship sometimes necessary?](#isnt-censorship-sometimes-necessary)
7.  [But why is anonymity necessary?](#but-why-is-anonymity-necessary)
8.  [And what of copyright?](#and-what-of-copyright)
9.  [But how will artists be rewarded for their work without copyright?](#but-how-will-artists-be-rewarded-for-their-work-without-copyright)
10.  [Alternatives to Copyright](#alternatives-to-copyright)

## The Philosophy Behind Freenet

1. ### A Disclaimer

    There are many reasons why people get involved in the Freenet Project. Some
    share the views outlined in this document; some share variations of these views,
    which are also served by what we are trying to achieve; and some just enjoy the
    technical challenge. These are the ideas which motivated me to architect the
    system in the first place, but not necessarily the views that everyone involved
    in the Freenet Project holds.

2. ### Suggested prior reading

    For this document to make sense, you should probably know what Freenet is. You
    can get a good overview from [What is Freenet?](about.html#introduction).

3. ### The importance of the Free flow of information

    Freedom of speech, in most western cultures, is generally considered to be one
    of the most important rights any individual might have. Why is the freedom to
    share ideas and opinions so important? There are several ways to answer this
    question.

    1. ### Communication is what makes us human

        One of the most obvious differences between mankind and the rest of the animal
        kingdom is our ability to communicate sophisticated and abstract concepts. While
        we constantly discover that animal's communication ability is more sophisticated
        than previously assumed, it is unlikely that any other animal approaches our own
        level of ability in this area.

    2. ### Knowledge is good

        Most people, given the option of knowing something and not knowing something,
        will choose to have more information rather than less. Wars have been won and
        lost over who was better-informed. This is because being better-informed allows
        us to make better decisions, and generally improve our ability to survive and be
        successful.

    3. ### Democracy assumes a well informed population

        Many people today live under democratic governments, and those who don't,
        probably want to. Democracy is an answer to the question of how to create
        leaders, while preventing them from abusing that power. It achieves this by
        giving the population the power to regulate their government through voting,
        yet the ability to vote does not necessarily mean that you live in a
        democratic country. For a population to regulate their government effectively
        it must know what their government is doing, they must be well informed. It
        is a feedback loop, but this loop can be broken if the government has the
        power to control the information the population has access to.

4. ### Censorship and freedom

    Everyone values their freedom, in fact, many consider it so important that
    they will die for it. People like to think that they are free to form and
    hold whatever opinions they like, particularly in western countries. Consider
    now that someone had the ability to control the information you have access
    to. This would give them the ability to manipulate your opinions by hiding
    some facts from you, by presenting you with lies and censoring anything that
    contradicted those lies. This is not some Orwellian fiction, it is standard
    practice for most western governments to lie to their populations, so much
    so, that people now take it for granted, despite the fact that this
    undermines the very democratic principles which justify the government's
    existence in the first place.

5. ### The solution

    The only way to ensure that a democracy will remain effective is to ensure
    that the government cannot control its population's ability to share
    information, to communicate. So long as everything we see and hear is
    filtered, we are not truly free. Freenet's aim is to allow two or more people
    who wish to share information, to do so.

6. ### Isn't censorship sometimes necessary?

    Of course no issue is black and white, and there are many who feel that
    censorship is a good thing in some circumstances. For example, in some
    European countries propagating information deemed to be racist is illegal.
    Governments seek to prevent people from advocating ideas which are deemed
    damaging to society. There are two answers to this however. The first is that
    you can't allow those in power to impose "good" censorship, without also
    enabling them to impose "bad" censorship. To impose any form of censorship a
    government must have the ability to monitor and thus restrict communication.
    There are already criticisms that the anti-racism censorship in many European
    countries is hampering legitimate historical analysis of events such as the
    second world war.

    The second argument is that this "good" censorship is counter-productive even
    when it does not leak into other areas. For example, it is generally more
    effective when trying to persuade someone of something to present them with
    the arguments against it, and then answer those arguments. Unfortunately,
    preventing people from being aware of the often sophisticated arguments used
    by racists, makes them vulnerable to those arguments when they do eventually
    encounter them.

    Of course the first argument is the stronger one, and would still hold-true
    even if you didn't accept the second. Basically, you either have censorship,
    or you don't. There is no middle-ground.

7. ### But why is anonymity necessary?

    You cannot have freedom of speech without the option to remain anonymous.
    Most censorship is retrospective, it is generally much easier to curtail free
    speech by punishing those who exercise it afterward, rather than preventing
    them from doing it in the first place. The only way to prevent this is to
    remain anonymous. It is a common misconception that you cannot trust
    anonymous information. This is not necessarily true, using digital signatures
    people can create a secure anonymous pseudonym which, in time, people can
    learn to trust. Freenet incorporates a mechanism called "subspaces" to
    facilitate this.

8. ### And what of copyright?

    Of course much of Freenet's publicity has centered around the issue of
    copyright, and thus I will speak to it briefly. The core problem with
    copyright is that enforcement of it requires monitoring of communications,
    and you cannot be guaranteed free speech if someone is monitoring everything
    you say. This is important, most people fail to see or address this point
    when debating the issue of copyright, so let me make it clear:

    > *You cannot guarantee freedom of speech and enforce copyright law*

    It is for this reason that Freenet, a system designed to protect Freedom of
    Speech, must prevent enforcement of copyright.

9. ### But how will artists be rewarded for their work without copyright?

    Firstly, even if copyright were the only way that artists could be rewarded
    for their work, then I would contend that freedom is more important than
    having professional artists (those who claim that we would have no art do not
    understand creativity: people will always create, it is a compulsion,
    the only question is whether they can do it for a living).

    Secondly, it could be questioned whether copyright is effective even now. The
    music industry is one of the most vocally opposed to enhancements in
    communication technology, yet according to many of the artists who should be
    rewarded by copyright, it is failing to do so. Rather it has allowed
    middle-men to gain control over the mechanisms of distribution, to the
    detriment of both artists and the public.

10. ### Alternatives to Copyright

    Fortunately it won't come to this. There are many alternative ways to reward
    artists. The simplest is voluntary payment. This is an extension of the
    patronage system which was frequently used to reward artists prior to
    copyright, where a wealthy person would fund an artist to allow them to
    create full-time. The Internet permits an interesting extension of this idea,
    where rather than having just one wealthy patron, you could have hundreds of
    thousands, contributing small amounts of money over the Internet.

    We actually practice what we preach in this regard too, on the 15th of March
    2001 the Freenet Project started taking donations, and within a week we had
    collected over $1000.

### Current Contributors


Ian Clarke

: Freenet is based on Ian's paper "A Distributed Decentralised Information
Storage and Retrieval System". Ian started the Freenet Project around July of
1999, and continues to coordinate the project.
Learn more about Ian on his [personal website](http://blog.locut.us/).

Matthew Toseland

: Matthew has been working on Freenet since before the 0.5 release. His work
and that of others has resulted in dramatic improvements to the performance
and stability of the network.

Oskar Sandberg

: Oskar was also one of the earliest contributors to the Freenet Project,
and has made some important theoretical breakthroughs that lead to the
beginning of Freenet 0.7, see the papers page.

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
driving force behind tackling long standing issues in Freenet.


xor

: The Developer of the Web of Trust and Freetalk. He worked on the Web
of Trust in part-time for one year and is now working as volunteer
again.


David (Bombe) Roden

: The developer of the site insertion tool jSite and of Sone, the Social
Network over Freenet.


Ximin Luo

: A debian developer who currently works on packaging Freenet.


Bert Massop

: Works on the Freenet core and wherever there is need.


TheSeeker

: A long term contributor who, among other things, helps keep the
contact between the core developers and users in active subgroups.


Tommy[D]

: A Gentoo packager who untangled all the dependencies of Freenet and
packaged it cleanly in Gentoo.


Arne Babenhauserheide

: The current maintainer of pyFreenet and infocalypse. He also writes
articles and tutorials for Freenet.


#### The translators

A dilligent team of people from various backgrounds who make it
possible to ship Freenet and this website in many different languages.


#### Many more great hackers

This list is missing many freesite authors, plugin writers, and a host
of other people who contributed in various ways.


### Anonymous Contributors


Eleriseth

: Works on Freenet core and communicates via FMS.


Somedude

: The developer of the Freenet-based Forum system FMS, of FreenetHG and
of FLIP, chat over Freenet.


The folks from Frost

: A group of users and programmers who use an old spammable
Freenet-based forum system which has been abandoned by most of the
core developers. They are active, however, and though it takes time
for their contributions to reach to core development, they take part
in Freenet development.



### Previous Contributors

Thomas Markus

: A dutch developer and statistic-enthusiast. He now works at Topicus.Education.

Scott Miller

: Scott is responsible for the implementation of much of the cryptography
elements within Freenet.

Steven Starr

: Steven helps with administration of Freenet Project Inc, and is an advisor to
the project on business and publicity matters.

Dave Baker

: Dave's main contribution has been [Freemail](documentation.html#freemail),
his Summer of Code project to build a working email-over-Freenet system,
as well as some debugging and core work in various places.

Robert Hailey

: Robert has helped improve the speed and security of Freenet by finding two
**major** bugs, and has recently contributed some code.

David Sowder

: David (Zothar) has helped the Freenet Project as time permits and interest
directs, including configuration, statistics and peer management via FCP,
the FProxy stats page and Node 2 Node Messages (N2NM/N2NTMs).

And **hundreds of others**, who either haven't asked to be added here, who
prefer to remain nameless, or who we just haven't got around to thanking. Not to
mention thousands of users, testers, and [donors](donate.html#sponsors)!

### Papers

![][icon_pdf] [Measuring Freenet in the Wild: Censorship-resilience under Observation]({filename}/assets/papers/roos-pets2014.pdf) (PDF)
Observations and measurements on the live Freenet network. Includes suggestions
for improvement. This was submitted to PETS 2014.

![][icon_pdf] [The Dark Freenet]({filename}/assets/papers/freenet-0.7.5-paper.pdf) (PDF)
Detailed paper about the Freenet 0.7.5 network, as opposed to its routing
algorithm, which is detailed in the below papers. Includes some new
simulations. This has been submitted to PET 2010.

![][icon_video] [Video of Small World talk, Berlin, December 2005](http://player.vimeo.com/video/22488244?title=0&byline=0&portrait=0)  
This is a video of a talk given by Ian Clarke and Oskar Sandberg at the Chaos
Computer Congress in Berlin, December 2005, describing the (then) new
architecture for Freenet 0.7\. You can also download the [slideshow](
/assets/papers/ccc-slideshow.pdf.bz2), and the source for the Java [demo](
/assets/papers/ccc-freenet-demo.tar.bz2) (requires Java 1.5).

![][icon_pdf] [Searching in a Small World]({filename}/assets/papers/lic.pdf) (PDF)
Oskar Sandberg's licentiate thesis describing a simple decentralized
mechanism for constructing small world networks that is inspired by Freenet's
original design. Part II of the thesis describes the basis for the new
Darknet architecture.

![][icon_pdf] [Distributed routing in Small World Networks]({filename}/assets/papers/swroute.pdf) (PDF)
A paper by Oskar Sandberg describing the theoretical basis for the new
"Darknet" routing mechanism employed by Freenet 0.7.

![][icon_pdf] Chaos Computer Congress Talk (slideshow)  
This is a [slideshow]({filename}/assets/papers/ccc-slideshow.pdf.bz2) for a talk given
at the Chaos Computer Congress on 30th Dec 2005 in Berlin, Germany by Ian
Clarke and Oskar Sandberg. It described the new "darknet" approach to be
employed in Freenet 0.7\. A Java demonstration to accompany the talk is [
also]({filename}/assets/papers/ccc-freenet-demo.tar.bz2) available.

![][icon_pdf] [Switching for a small world]({filename}/assets/papers/vilhelm_thesis.pdf) (PDF)
A thesis by Vilhelm Verendel exploring ways to optimise the swapping algorithm.

![][icon_pdf] [Protecting Freedom of Information Online with Freenet]({filename}/assets/papers/freenet-ieee.pdf) (PDF)
An IEEE Internet Computing article describing the Freenet architecture circa
2002 - probably the best introduction to the theory behind Freenet.

![][icon_pdf] [FreeNet White Paper]({filename}/assets/papers/ddisrs.pdf) (PDF)
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
A paper describing some attacks on Freenet 0.7's location swapping algorithm.
We have solutions for this but they are still being tested.

* * *

The most up to date reference is of course [the source code](
https://github.com/freenet/fred), but there is also some useful documentation on
[the wiki](https://wiki.freenetproject.org/) (you may have to search a bit),
and most implemented ideas have been discussed in detail on [the mailing
lists](help.html#mailing-lists) at some point, more recently often in-Freenet
forums such as FMS, or [the bug tracker](https://freenet.mantishub.io/) hosted by MantisHub.

[icon_pdf]: /assets/img/small-n-flat/file-pdf.png
[icon_video]: /assets/img/small-n-flat/file-video.png
