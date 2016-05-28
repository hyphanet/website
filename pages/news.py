# Python code copyright Gerard Krol, license: MIT
import string
import markdown
from .common import *

class NewsItem(object):
    def __init__(self, section, title, content):
        self.section = section
        self.title = title
        self.content = md(content)
    def render(self):
        return section(self.section, self.title, text(self.content))
    def markdown_link(self):
        return "[{title}](news.html#{anchor})".format(anchor=self.section, title=self.title)

def news_items():
    donate_button = """<a class="btn button-custom btn-custom-two donate-button" href="donate.html">""" + _("Donate today.") + """</a>"""
    return [
        NewsItem("20160526-htl18attack", _("2016-05-26 - Police department's tracking efforts based on false statistics"),
_("""
Documents initially made public by the Missouri police department
describe their efforts on tracking Freenet usage.  Using a simple
scheme, they claim a near zero false positive rate for
tracking the originator of a download.  While we applaud all public
documentation on attacks, we have to point out that the claimed
effectiveness of their attacks is based solely on flawed mathematics.
In reality, the false positive rate of their method is at least 83%,
and close to 100% in real world scenarios.

The claimed effectiveness of their attack is based on a false
assumption about the distribution of the HTL of incoming requests.  HTL (Hops
to Live) is a number embedded in each request that is usually
decremented when the request is forwarded, starting at a value of 18
at the originator of the request, and serves to limit the number of
hops a request can survive on the network.  As a security precaution,
the HTL is decremented probabilistically on the first few hops.  In
their tracking efforts, the Missouri police department assumes that
when multiple requests for pieces of a file arrive from a single node,
and all these requests have HTL 18 with no requests at HTL 17 or 16,
this node must be the originator of the requests, with a false
positive probability decreasing with the number of requests received
from the node.  This would be true if whether the HTL is
decremented is decided per request, which has historically been the
case in the early days of Freenet.  The vulnerability they claim to
exploit was however addressed in 2008 (last touched in [this
commit][commithtl18]).  Whether the HTL is decremented is since
decided per connection, so any probability they claim using the
aforementioned method is false.

For every connection there is a 50% chance that all the HTL 18 requests
(not only a single one, as would be the case with per-request
probabilistic decrementing) did not originate from the node from which
we received them but were forwarded one step. So for 10 connections
(the lowest number of peers Freenet uses), there are on average 5
other nodes whose HTL 18 requests are forwarded with HTL 18, so the
probability that a given HTL 18 request originated at the node from
which we received it is only about 17% (1 in 6). If the node has more
connections (close to 30 is common), this probability is even lower. And
this probability does not get higher when gathering more requests of
chunks from a specific file or a specific kind of files, because they
can reasonably all be forwarded from a different node — the one which
really sent them.

The heterogenity of the network and routing with second-level
connections taken into account does not easily yield robust
statistical claims without knowing the peers of peers of the node
under investigation. Staying connected for a long time might allow for
distinguishing between the changing peers of the node and requests
originating at the node itself, but with significant cost.

If the node which is tracked has friend-to-friend peers
(which unlike automatically added peers do not change regularly), even waiting
will not allow finding out with the described method whether HTL 18 requests came from the
node itself or from the peers connected over
friend-to-friend connections.

For details, see [the code][codehtl18].

This does not make it impossible to track Freenet users who use only
Opennet mode (connecting to strangers), since a network where nodes
connect to strangers is inherently susceptible to Sybil attacks,
where nodes of typical users are outnumbered by malicious, colluding nodes.

The only way to defend against serious attacks is to *use Freenet in
Friend-to-Friend mode*, where the precondition to tracking a user is
social engineering to get the people to whom he/she is connected to
betray the user. The need to defend against this type of attacks is
the reason why the core of Freenet was rewritten in 2007 to add this
Friend-to-Friend mode (called Darknet mode).

However the method used by the Missouri police department is using
false statistics: despite its flaws, Freenet's Opennet is much harder to
track than they claim.

The Freenet developers do not condemn these attacks. Police departments
try to use every legal venue to catch criminals. This is their job and
vocation, but any attack they find could also be used by oppressive
governments to suppress dissenting opinions, so we will work to fix attacks
as they come to light.
We expect law enforcement to get their math right, especially when using
it in court. If they can get a warrant with an 83% false positive
rate, that's a problem for lawmakers. If they falsely claim a 0% false
positive rate, that's eroding the trust of citizens in the legal
system.

Additional information on this attack is available from the
[mailing list discussion][mlhtl18].

The mission of the Freenet Project is to safeguard freedom of the
press by providing censorship resistant communication. This requires
protecting people against being targeted for what they write or
read. To achieve this, Freenet enables users to publish anonymous
websites and offers chat, forums, and file-sharing, as well as
confidential communication among friends and methods to leverage the
capabilities of Freenet from other tools.

When the police spread misinformation about the security of Freenet, it
directly undermines our mission by driving users to networks which
cannot provide a comparable level of security for
whistle-blowers and those wishing to publish anonymously.
""") + """

[commithtl18]: https://github.com/freenet/fred/commit/4aaa08f11656af1dd857e45612763c9bd2d89fc2
[codehtl18]: https://github.com/freenet/fred/blob/next/src/freenet/node/PeerNode.java#L1603
[mlhtl18]: https://emu.freenetproject.org/pipermail/devl/2016-May/038923.html
"""),
        NewsItem("20160522-1473", _("2016-05-22 - Freenet build 1473 released"),
_("""
Freenet 0.7.5 build 1473 is now available. This is the first build to require
Java 7! It upgrades Bouncy Castle to version 1.54, and adds a Traditional
Chinese translation to the Windows installer.

Plugin updates:

* Add Sharesite - a fork of ShareWiki - as an official plugin. Thanks to
  ArneBab for getting it ready! It includes an earlier version of TextileJ to
  avoid license problems, and adds syntax help, external activelink support, and
  a template with div IDs for easier CSS.
* Update Freereader with the ability to configure the site title and subtitle,
  and fix the translation support.

User-facing core change highlights:

* Improve MP3 filtering.
* Add The Filtered Index to the default bookmark list.
* Fix handling of filenames with non-ASCII spaces.
* Alphabetize language configuration dropdown.
* Add Hungarian translation support. The translation was added previously but not
  actually available.
* Fix dropping low-traffic connections. This helps with simulations.
* Optimize FProxy CSS load order, and fix bugs which prevented caching static
  assets. This improves web interface responsiveness.
""")),
        NewsItem("20160503-ddg", _("2016-05-03 - DuckDuckGo donated $25,000"),
_("""
The Freenet Project is very excited to announce that [DuckDuckGo have donated][ddg_url] $25,000 to our project.
This new funding will be used to advance our goal of ensuring true freedom of communication on the Internet.

The project has always operated in a democratic manner, and we will use an open process to set priorities for how we allocate this funding, which will incorporate the views of Freenet’s users, developers, and supporters.
""") + """

[ddg_url]: https://duck.co/blog/post/303/2016-foss-donations-announcement
"""),
        NewsItem("20160410-1473-pre1", _("2016-04-10 - Freenet testing build 1473-pre1 released"),
_("""
Freenet unstable testing prerelease build 1473-pre1 is now available.
It's the first build to require Java 7.

Highlights:

* Add The Filtered Index to the default bookmark list
* Improve MP3 filter stability
* Fix binary blob download over FCP
* Fix handling of filenames with non-ASCII spaces

For more details and information on how to test this release see the [development mailing list thread][devl_thread].
""") + """

[devl_thread]: https://emu.freenetproject.org/pipermail/devl/2016-April/038888.html
"""),
        NewsItem("20160319-1472", _("2016-03-19 - Freenet 0.7.5 build 1472 released"),
_("""
This is the last build to support Java 6! The next build will require Java 7 or higher. Nodes running Java 7 or higher and using the official update key will now use a new update key. Nodes on Java 6 remain using the old update key and will not be updated to further builds. Thanks to yadevel for fixing the regression this release was blocking on!

This version was initially partially released as build 1471 - it was released on GitHub but not offered from the website or auto-update. Build 1472 fixes a bug which when using Java 6 prevented nodes from starting for the first time. It did not break existing installations.

Highlights:

- Fix uploads stalling when using MAXIMUM physical security.
- Fix lots of "setNativePriority(X) has failed!", which was caused by a serious thread priority problem. This might fix nodes unexpectedly losing peers.
- Order alerts within a category by time: if you have lots of messages from darknet peers they will remain nicely sorted.
- There is now a [caching layer][caching] which should significantly reduce I/O load.
- Update WebOfTrust from build 15 to build 18. [Its][wot16] [changelogs][wot17] [are][wot18] separate, but the changes reduce CPU load. Incremental score recomputation requires roughly 3 percent of the time of full recomputation, and queuing trust lists to disk lowers thread usage.

Translations:

- Add partial Greek translation.
- Update German, Bokmål, Brazilian Portuguese, Simplified Chinese, and  Traditional Chinese translations.
- Fix Bokmål localization loading.

Also:

- Remove Gantros Index from the default bookmark list because it stopped updating.
- Remove Linkageddon from the default bookmark list because it stopped updating.
- New version of UPnP to fix some instability and compatibility problems. Thanks to 007pig we have a [new UPnP plugin][upnp2] in development which supports UPnP2, but it is not yet included.
- New version of KeyUtils.

WebOfTrust now has an updatable testing version built and maintained by xor. To use it, unload WebOfTrust, then load "WebOfTrust Testing Versions" on the Plugins page. Versions built by xor will not work with Java 6.

Sites can set favicons with `<link rel="icon" type=... href=...>`. (`type` could be `"image/x-icon"`)

Extensive review and improvement of English source strings and French and Spanish translations. Tests for and fixes of value substitution in translations. Thanks Vaughan Woodzell!

The default theme is now sky-static instead of clean-dropdown. This looks less outdated, though not modern.

Fix default bookmarks missing the "software" category since build 1470. If you don't see this category please re-add the default bookmark set from the bookmark editing page.

IpToCountry database is updated. (This allows providing the country flags on the peers pages. It is local to each instance and does not contact an external service.)

Add partial CSS3 support, including viewport lengths. Thanks, Ben Green!
""") +
"""
[caching]: https://github.com/freenet/fred/pull/157
[wot18]: https://github.com/freenet/plugin-WebOfTrust/releases/tag/build0018
[wot17]: https://github.com/freenet/plugin-WebOfTrust/releases/tag/build0017
[wot16]: https://github.com/freenet/plugin-WebOfTrust/releases/tag/build0016
[upnp2]: https://github.com/freenet/plugin-UPnP2
"""),
        NewsItem("20160103-1471-pre3", _("2016-01-03 - Testing release build 1471-pre3"),
_("""
Freenet unstable testing prerelease 1471-pre3 is now available.

This is feature-complete and hopefully the last testing release before the stable release of build 1471.
Build 1471 will be the last to support Java 6.

Highlights:

- Fix uploads stalling when using MAXIMUM physical security.
- Fix lots of "setNativePriority(X) has failed!", which was caused by a serious thread priority problem. This might fix nodes unexpectedly losing peers.
- Order alerts within a category by time: if you have lots of messages from darknet peers they will remain nicely sorted.

For more information and how to help test see the [developer mailing list][devl_1471].
""") + """

[devl_1471]: https://emu.freenetproject.org/pipermail/devl/2016-January/038771.html
"""),
        NewsItem("20151220-hackathon-results", _("2015-12-20 - \"Weekend of Code\" hackathon results"),
_("""
During the hackathon we got some changes done:

- [Fix uploads stalling when using MAXIMUM physical security.][1]
- [Fix lots of "setNativePriority(X) has failed!"][2]
- [Fix Bokmål localization loading.][3]
- [Fix JVM version string parsing.][4]
- [Fix and add test for broken localization substitution token pairs.][5]
- [Remove Gantros Index][6] because it stopped updating.
- [Remove Linkageddon][6] because it stopped updating.
- [Remove deprecated negtype crypto.][7]
- [Order alerts by date.][8]
- [Progress toward Freemail "to" field autocomplete.][9]
- Progress toward changing the language setting in Winterface.
- Progress toward building and verifying dependencies for [Fred][10] and [Winterface][11] using [Gradle][12] and [gradle-witness][13].

If we're able to get final changes ready build 1471-pre3 will be released the weekend of January 2nd.
""") + """

[1]: https://github.com/freenet/fred/pull/438
[2]: https://github.com/freenet/fred/pull/435
[3]: https://github.com/freenet/fred/pull/426
[4]: https://github.com/freenet/fred/pull/437
[5]: https://github.com/freenet/fred/pull/421
[6]: https://github.com/freenet/fred/pull/433
[7]: https://github.com/freenet/fred/pull/439
[8]: https://github.com/freenet/fred/pull/418
[9]: https://github.com/Dr-Tensor/plugin-Freemail/tree/master
[10]: https://github.com/freenet/fred/tree/gradle
[11]: https://github.com/ademan/winterface/tree/gradle-witness-1
[12]: http://gradle.org/
[13]: https://github.com/WhisperSystems/gradle-witness
"""),
        NewsItem("20151212-mactray", _("2015-12-12 - New OS X installer and tray app"),
_("""
The [Freenet installer][downloads_url] for OS X is now a native application. It should fix several major installation problems OS X users have encountered in the past.

It also includes an updated [tray application][tray_url] with bugfixes and new features.

All Freenet users on OS X are encouraged to [download][tray_release_url] the new tray application.

![][tray_screenshot_url]
""") + """
[downloads_url]: download.html
[tray_screenshot_url]: assets/img/mactray/osx_installer_step2_transparent.png
[tray_release_url]: https://github.com/freenet/mactray/releases
[tray_url]: https://github.com/freenet/mactray#freenettray
"""),
        NewsItem("20151212-donation-appeal", _("2015-12-12 - Appeal for donations"),
_("""
Freenet is a platform for censorship-resistant communication and publishing. For the past 15 years the project has built tools to fight for freedom of speech and information.
Our software provides a decentralized peer-to-peer network designed to hide who publishes or accesses potentially controversial information - or even that it exists - especially useful for those living in oppressive political regimes.

While development is primarily driven by volunteers, the project has also employed paid developers to provide more-focused work.
Over the past 2 years, the project's paid developer has made [great progress][build18] improving “Web of Trust” functionality to combat spam, which is a central problem in any anonymous system.
Unfortunately, the Freenet Project no longer has enough money to retain his services, so he is now a volunteer.
This greatly reduces his capacity to continue this important work.

We are extremely excited for the future of Freenet and the [projects built on top of it][projects].
There is so much more work to do, and full-time developers greatly benefit the project.

Help us keep Internet freedom alive and expand human liberty. {donate_button}

Thank you,

Freenet Project volunteers
""").format(donate_button=donate_button) + """

[build18]: https://github.com/freenet/plugin-WebOfTrust/releases/tag/build0018
[projects]: https://wiki.freenetproject.org/Projects
"""),
        NewsItem("20151120-hackathon", _("2015-11-20 - \"Weekend of Code\" hackathon announcement"),
_("""
## Who?

We welcome developers of all skill levels, designers, translators, and users.

## What?

The Freenet Project is holding a "Weekend of Code" hackathon to improve user experience.

## When?

The weekend of December 19th and 20th.

## Where?

[chat.freenode.net #freenet][irc_url]

[FLIP][flip_url] #freenet

Local meetups are arranged separately.

## Details

See the [wiki Hackathon page][hackathon_url] for details.

Happy hacking!
""") + """

[irc_url]: help.html#irc
[flip_url]: https://wiki.freenetproject.org/FLIP
[hackathon_url]: https://wiki.freenetproject.org/Wiki/Hackathon
"""),
        NewsItem("20151025", _("2015-10-25 - Prerelease and Windows installer"),
_("""
The Windows installer has updated translations for French, Indonesian, and
Simplified Chinese, and is newly translated into Bulgarian, Croatian,
and Japanese.

In addition, Freenet unstable testing prerelease 1471-pre2 is now available.
For details on what it contains and how to test it see the
[release announcement][announcement].
""") + """
[announcement]: https://emu.freenetproject.org/pipermail/devl/2015-October/038449.html
"""),
        NewsItem("20151021-site-deploy", _("2015-10-21 - Website redesign is live"),
_("""
The redesigned website is now live!
Existing URLs [redirect](http://www.w3.org/Provider/Style/URI.html)
to their new equivalents. Thanks to everyone who contributed feedback,
development, and translations.

If we missed something, please tell us in our [support chat](help.html#irc)!
""")),
# Below news items are licensed GFDL (from old freenetproject.org website)
              NewsItem("20151011-redesign", _("2015-10-11 - Upcoming website redesign"),
_("""
In the next few weeks we will transition to a redesigned website. This will be
the first major change since 2009. In addition to looking more modern, this new
version is also more practical to modify, test, and translate.

If you'd like to get a look at the site in testing you can find it [here][url_testing] - as given in the prompt the username and password are "guest".
If you'd like to help with translation, please join us on the ["website" resource on Transifex][url_transifex].

If you have any feedback on the new website design please let us know on [chat][url_chat] or the [support list][url_supportlist]!
""" + "\n\n" + """
[url_testing]: https://testing.freenetproject.org/
[url_transifex]: https://www.transifex.com/otf/freenet/website/
[url_supportlist]: https://emu.freenetproject.org/cgi-bin/mailman/listinfo/support
[url_chat]: irc.html
""")),
              NewsItem("20150917-ecdsa-vulnerability", _("2015-09-17 - elliptic curves: using safe Bouncy Castle since November 2014"),
_("""
<p>
A recent article outlines
<a href="http://web-in-security.blogspot.ca/2015/09/practical-invalid-curve-attacks.html">
practical attacks against elliptic curves</a> to recover private keys
which worked against the Bouncy Castle crypto provider used by Freenet
until <a href="#build01466">Build 1466</a> (released 2014-11-09) and
against Java JCE
<a href="http://www.oracle.com/technetwork/topics/security/cpujul2015-2367936.html">
until July 2015</a>. If you use the current stable
<a href="#20150816-1470-release">build 1470</a> on an updated Java, your
node is not vulnerable to these attacks.
</p>

<p>
On darknet the attacks required knowing both node references, so in
darknet mode Freenet was only vulnerable to them if two friends
connected to the same malicious third party or shared their node
references in public. On opennet the target of these attacks would have
been the seednodes because other opennet connections are neither
persistent nor trusted.
</p>


""")),
        NewsItem("20150816-1470-release", _("2015-08-16 - Freenet 0.7.5 build 1470 released"),
                 _("""

<p>
This release fixes Freemail problems that prevented sending mail, and removes a
compromised opennet seed node. Freemail also gains a new message link on the
inbox page, links to senders' WoT profiles, and new translations:
</p>

<ul>
<li>Czech</li>
<li>Greek</li>
<li>Spanish</li>
<li>Finnish</li>
<li>Hungarian</li>
<li>Dutch</li>
<li>Polish</li>
<li>Portuguese (Portugal)</li>
<li>Serbian</li>
<li>Turkish</li>
</ul>

<p>
To clarify, the CHK metadata bug fixes in 1468 are added as a new compatibility
mode that is not yet the default. Compatibility with 1416 keys is available.
</p>

<p>
The Fred Spanish translation has comprehensive updates as well.
</p>

""")),
        NewsItem("20150807-1469-wininstaller", _("2015-08-07 - Windows translation update"),
                 _("""

<p>
The Windows installer and tray app have updated translations. The installer is
newly translated into Portuguese (Portugal) and Serbian. The tray app is newly
translated into Spanish, Persian, Portuguese (Portugal), and Serbian.
This also fixes a tray app problem where translations for Brazilian Portuguese
and Simplified Chinese were not used.
</p>

""")),
        NewsItem("20150719-1469-release", _("2015-07-19 - Freenet 0.7.5 build 1469 released"),
                 _("""

<p>
This release fixes two bugs introduced in build 1468. One caused very
slow operation and high CPU usage with large files and physical
security levels above None (i.e. Freenet-level disk encryption). The
other prevented interactive usage (e.g. freesite browsing) while
finishing large downloads or starting large uploads.
</p>

""")),
        NewsItem("20150713-1468-known-issues", _("2015-07-13 - Build 1468 known issues"),
                 _("""

<p>
Despite being in some form of prerelease for over 6 months, and two weeks of
being available as a release candidate, we didn't catch some bugs in time. There
are two main issues:
</p>

<ol>
<li>
Because the reimplementation of the client layer without db4o did not include
prioritization of FEC decoding / encoding, large bulk download or upload queues
can starve the realtime queues, making them unresponsive.
(See <a href="https://github.com/freenet/fred/pull/381">PR #381</a>.)
</li>
<li>
Due to our misunderstanding of when the cryptography library we use - Bouncy
Castle - included which fixes, we did not realize that version 1.51, used by
build 1468, has severe performance problems with the way we use it to implement
disk encryption. Build 1469 will upgrade to Bouncy Castle 1.52, which fixes this
problem. It is only an issue when the physical security level is set to "Low" or
higher. It does not happen when physical security is set to "None."
(See <a href="https://github.com/freenet/fred/pull/382">PR #382</a>.)
</li>
</ol>

<p>
Sadly, these problems can combine to make a node use 100% CPU to slowly process
bulk queues while the realtime queue does not respond. Matthew (toad_) has
already released a snapshot to fix these problems, which you can find
<a href="https://emu.freenetproject.org/pipermail/devl/2015-July/038123.html">on the mailing list</a>
or <a href="http://localhost:8080/forumviewthread.htm?messageuuid=E544C7BB-5E5E-4159-83F8-AFC46C089329@h2RzPS4fEzP0zU43GAfEgxqK2Y55kEUNR01cWvYApI#E544C7BB-5E5E-4159-83F8-AFC46C089329@h2RzPS4fEzP0zU43GAfEgxqK2Y55kEUNR01cWvYApI">on FMS</a>.
</p>

""")),
        NewsItem("20150711-1468-release", _("2015-07-11 - Freenet 0.7.5 build 1468 released"),
                 _("""

<p>
The Freenet team is very happy to announce the stable release of Freenet 0.7.5 build 1468.
</p>

<p>
<b>Important notes</b>: downgrading from build 1468 is not supported; if you want to go back to build 1467 without losing the upload and download queues, <b>before</b> upgrading, back-up the following files and directories: master.keys, persistent-temp-*/, and node.db4o (see https://wiki.freenetproject.org/Program_files ). Please note that running transfers will be restarted from scratch too. A reminder to those testing auto-update to 1468-pre4: please restore your auto-update key to the default. One way to do this is to stop Freenet, remove the "node.updater.URI" line from freenet.ini, and start Freenet again.
</p>

<p>
In this release, the way Freenet stores data locally has changed drastically by no longer using the now-deprecated db4o object storage. It is replaced with the product of toad's summer of work - a custom on-disk format that is much more robust against corruption and more efficient.
</p>

<ul>
<li>Existing unfinished downloads and uploads will be imported to a new format, which requires restarting them from the beginning.</li>
<li>Space for downloads is now all allocated at the start, so machines very low on disk space may run out, which causes downloads to temporarily fail until more space is available.</li>
<li>CHKs will change due to metadata bugfixes.</li>
<li>Some unofficial plugins will need to be updated because of API changes. Sone already works, as do all official plugins.</li>
<li>The queue format changes should make it extremely rare to lose the entire queue: the impact of corruption will almost always be localized.</li>
<li>Multi-container / site uploads can now be persistent, making it more practical to upload large sites.</li>
<li>Passworded physical security is now much stronger. (Full-disk encryption is still preferable.)</li>
</ul>

<ul>
<li>The Windows installer now defaults to starting Freenet on login.</li>
<li>There is a <a href="https://github.com/freenet/wintray">new Windows tray app</a> with some useful features that is included with new installations. If you are using the existing Windows tray app you can download the new one <a href="https://downloads.freenetproject.org/alpha/installer/FreenetTray.exe.build01468">here</a>. No need to put it in a specific directory - it will try the default installation location and prompt if it can't find it.</li>
</ul>

<ul>
<li>The list of download keys moved from downloads/listFetchKeys.txt to downloads/listKeys.txt.</li>
<li>A list of upload keys is now available at uploads/listKeys.txt</li>
</ul>

<ul>
<li>Gantros' index is now in the default bookmarks. It uses the same software as Enzo's index, which is no longer updated.</li>
</ul>

<ul>
<li>The obsolete and deprecated XMLLibrary and XMLSpider plugins are no longer officially supported. They will still load for those who have them added, but are no longer shown on the plugin page.</li>
<li>In the interests of releasing this build more quickly, the new version of FlogHelper does not support exporting and importing backups from the web UI. The old backup code did not work with the new Freenet version after removing db4o. People can instead back up "plugins.floghelper.FlogHelper" files in the plugin-data directory. These can be dropped into the directory after unloading FlogHelper to restore a backup.</li>
<li>ThawIndexBrowser works again. Thanks saces!</li>
</ul>

<ul>
<li>Fred translations are updated.</li>
</ul>

<ul>
<li>Add two seed nodes, one sponsored by meshnet.pl - the Polish radio/meshnet darknet users group, and another run by ArneBab. Thanks!</li>
<li>Update existing seed node references.</li>
</ul>

<p>
Thank you for using Freenet!
</p>

""")),
        NewsItem("20150627-1467-wininstaller", _("2015-06-27 - New Windows installer and tray app"),
                 _("""

<p>
The Windows installer is updated with Java 8u45, a <a href="https://github.com/freenet/wintray#freenet-tray-application">new tray application</a>, and is newly translated into:
</p>

<ul>
<li>Czech</li>
<li>German</li>
<li>Greek</li>
<li>Indonesian</li>
<li>Italian</li>
<li>Polish</li>
<li>Brazilian Portuguese</li>
<li>Simplified Chinese</li>
</ul>

""")),
        NewsItem("20150624-upcoming-1468-update", _("2015-06-24 - Upcoming installer and testing releases"),
                 _("""

<p>
This weekend we will release an updated Windows installer for build 1467 along
with a <a href="https://github.com/freenet/wintray/blob/master/README.md">new Windows tray application</a>.
We will also release 1468-pre4, which if all goes according to plan will be the
last prerelease before a stable release two weeks later.
</p>

<p>
If you'd like to help with translations before then please do so! The
Windows-related resources are:
</p>
<ul>
<li><a href="https://www.transifex.com/projects/p/freenet/resource/windows-installer/">Windows installer</a></li>
<li><a href="https://www.transifex.com/projects/p/freenet/resource/windows-tray-commands/">Windows tray commands</a></li>
<li><a href="https://www.transifex.com/projects/p/freenet/resource/windows-tray-common/">Windows tray common</a></li>
<li><a href="https://www.transifex.com/projects/p/freenet/resource/windows-tray-crash/">Windows tray crash</a></li>
<li><a href="https://www.transifex.com/projects/p/freenet/resource/windows-tray-preferences/">Windows tray preferences</a></li>
</ul>
<p>
Some of the Windows tray resources contain many strings tagged notranslate; to
hide these search for Tags: translate.
</p>
""")),
        NewsItem("20150522", _("2015-05-22 - UN Report: Encryption and Anonymity Deserve Strong Protection"),
                 _("""
The UN Special Rapporteur published [a report on encryption, anonymity,
and the human rights framework](http://www.ohchr.org/EN/Issues/FreedomOpinion/Pages/CallForSubmission.aspx)
([doc](http://www.ohchr.org/EN/HRBodies/HRC/RegularSessions/Session29/Documents/A.HRC.29.32_AEV.doc),
[companion pdf](http://www.ohchr.org/Documents/Issues/Opinion/Communications/States/Selected_References_SR_Report.pdf)).
From the summary:

> encryption and anonymity enable individuals to exercise their rights to
freedom of opinion and expression in the digital age.

The reports concludes that

> 63\. The use of encryption and anonymity tools and better digital literacy
should be encouraged. The Special Rapporteur, recognizing that the value
of encryption and anonymity tools depends on their widespread adoption,
encourages States, civil society organizations and corporations to engage
in a campaign to bring encryption by design and default to users around
the world and, where necessary, to ensure that users at risk be provided
the tools to exercise their right to freedom of opinion and expression securely.

We with the Freenet Project welcome the official recognition of our mission
as important part of securing human rights in the digital age and we invite
everyone - especially reporters and civil society organizations - to install
Freenet and its communication tools to provide a point of contact for users at risk.
""")),
        NewsItem("20150414", _("2015-04-14 - SUMA Award Acceptance Speech (video)"),
                 _("""
The video from the talk given when Freenet [received the SUMA Award 2015](#20150211)
for being the best project against surveillance and espionage on the Internet
is available on [the Award page][url_award] and [on YouTube][url_youtube]:

{embed_youtube}

The Freenet Project receives the SUMA award and Arne Babenhauserheide accepts
the prize as representative of the project. Arne then presents the current
capabilities of Freenet to regain confidential and pseudonymous speech
on the Internet, along with a vision of how whistleblowers could use Freenet
to contact journalists without spilling their identity.
""").format(embed_youtube="""
<iframe width="560" height="315" src="https://www.youtube.com/embed/dZpsBSPsHDI"
style="border: none;" allowfullscreen=""></iframe>
""") + "\n\n" + """
[url_award]: http://www.searchstudies.org/de/suma2015.html
[url_youtube]: https://youtu.be/dZpsBSPsHDI?t=5m56s
"""),
        NewsItem("20150329", _("2015-03-29 - New Linux/Unix/OS X installer"),
                 _("""
The installer for Linux, Unix, and Mac OS X is updated to better detect Java.
""")),
        NewsItem("20150315", _("2015-03-15 - Progress toward build 1468"),
                 _("""
Build 1468 continues to make progress toward release.

What is done:

*   Replace the unreliable db4o database. (Yay!)
*   Create more flexible Windows tray app.
*   Update Windows installer translations for Finnish and French.
*   Add Windows installer translations for Czech, German, Italian, Polish, Brazilian Portuguese, and Simplified Chinese.
*   Improve the reliability of starting Freenet under changing Java installations on Linux/OS X/POSIX.
*   Update WebOfTrust with bug fixes and a new API.

What remains to be done:

*   <del>Finish reviewing the synchronous plugin communication API. Review is split between [GitHub](https://github.com/freenet/fred/pull/319) and more recently the [development mailing list](https://emu.freenetproject.org/pipermail/devl/2015-February/037986.html).</del> -- Done 2015-03-28
*   Update all plugins (KeyUtils and WebOfTrust are already ready) for the API breakage in this version.
*   Add a .NET 3.5 install to the Windows installer, along with the new tray app. (This is necessary for it to always work for those not on Windows 7.)
*   Everything on [this list](https://bugs.freenetproject.org/roadmap_page.php?version_id=85).

Because this is such a large release new installers for build 1467 will be released shortly to test those changes. Once everything on this list is complete, there will be a release candidate, then finally the stable release.
""")),
        NewsItem("20150314", _("2015-03-14 - Freenet translation joins Localization Lab"),
                 _("""
The Freenet project has joined the [Localization Lab](http://www.localizationlab.org) organization on Transifex. This allows a larger team of translators, translating into more languages, and access to paid support.

If this transition has caused any problems please let us know!
""")),
        NewsItem("20150215", _("2015-02-15 - New Windows tray app for testing"),
                 _("""
The Windows tray application distributed as of build 1467 is written in the automation scripting language AutoHotKey. It has not been well-maintained and is also often falsely detected by antivirus by virtue of the language it uses. We are pleased to announce a new Windows tray application written in C# which has some additional features:

*   Allow choosing which browser to launch.
*   Allow starting Freenet without the tray on startup.
*   Allow opening the Downloads folder from the menu.
*   Give a more actionable response to crashes.
*   Can be hidden while keeping Freenet running.
*   Can be located other places than in the Freenet installation folder.

If all goes well we plan for this tray app to be distributed with build 1468. Testing is appreciated! If you'd like to try it for yourself you can find it [here](https://downloads.freenetproject.org/FreenetTray-testing-eaf31ea.exe). Please let us know how it goes and if you'd like to see any changes.
""")),
        NewsItem("20150211", _("2015-02-11 - Freenet received the SUMA Award 2014/15"),
                 _("""
<div style="float: right"><img src="assets/img/suma2015_badge_transparent_3.png" alt="SUMA Award 2014/15"/></div>

At this year's [congress](http://searchstudies.org/de/suma2015.html)
of [SUMA-EV](http://suma-ev.de/en/index.html), association for free access to knowledge,
the [SUMA award](http://suma-awards.de/en/index.html) was awarded in the venerable
Karl-H.-Ditze lecture hall of the Hamburg University of Applied Sciences.
The topic of the award, was the surveillance scandal, revealed by whistleblower
Edward Snowden: 'protection against total surveillance'. From submissions of about
50 projects for the SUMA award 2014/15 the panel of SUMA-EV selected the Freenet
Project as the winner. The prize money of 2500 euro will be used like regular [donations](donate.html)
to fund our one paid developer.

> ![](assets/img/news/suma_award_2015_handover.jpg)  
> Wolfgang Sander-Beuermann with Arne Babenhauserheide, long-term Freenet contributor, as representative of the award winner. Photo: Michael Christen in Hamburg, Lizenz: CC0.
""")),
        NewsItem("20150105", _("1st January 2015 - apt-get over Freenet"),
                 _("""
Developers of the privacy-focused Debian derivative Mempo report that it can download updates over Freenet! For details, see their page on [Apt over Freenet](http://deb.mempo.org/#install_apt_freenet).

Key Points:

*   use Freenet to distribute online updates
*   most secure hosting option

That means it is now possible to get reproducibly built kernels checked by anonymous (and therefore hard to pressure) contributors and update them over Freenet without disclosing that you use them. This applies to the packages provided by Mempo - other apt-get activity like installing GIMP is still public. It would be possible to host the entire Debian repository in Freenet, but this is not yet on the agenda for Mempo because this other activity does not disclose the potentially sensitive information that you want additional privacy.

> The practical cool result now, is that Mempo repository can not be censored, DDoSed or taken offline, despite having just 1 tiny server (or no server at all) - rfreeman (one of the mempo developers)
""")),
        NewsItem("build01467", _("2014-11-23 - Freenet 0.7.5 build 1467 released"),
                 _("""
This release fixes a bug introduced in build 1466 which can erase the list of plugins to load when Freenet starts if it crashes. If you are affected by this bug and can no longer connect, try adding the UPnP or JSTUN plugins again.

This release also has updated Finnish, French, Dutch, and Brazilian Portuguese translations thanks to [volunteers on Transifex][url_transifex].

The Windows installer is updated:

*   It now disables the Java installer's sponsor offers. Thanks artart78!
*   It gained a Finnish translation. Thanks oselotti!

Thank you for using Freenet!

- Steve Dougherty
""") + "\n\n" + """
[url_transifex]: https://www.transifex.com/projects/p/freenet/
"""),
        NewsItem("build01466", _("2014-11-09 - Freenet 0.7.5 build 1466 released"),
                 _("""
This release is planned to be the second-to-last version of Freenet to support Java 6\. The version after this one will refuse to upgrade unless running on Java 7 or later. Support for this behavior is part of a larger effort to allow separate official update channels - stable, testing, and unstable - as well as make it easier to publish unofficial update channels and further improve deployment security.

Highlights for this build:

*   Add Hungarian Windows installer translation. Thanks drezzium!*   Allow hiding the Java version End Of Life alert. (I'm sorry for the excessive annoyingness. Still - please upgrade Java!)
*   Upgrades to the next version (that is, when running this build's upgrade code) should no longer get [stuck in an upgrade loop][url_bug3208].
*   Increase opennet peer limit to 142 peers. This now has [more math behind it][url_peermath] and will change when network parameters are adjusted.
*   Add more opennet seed nodes. Thanks saces and juiceman!
*   This build will be mandatory starting 2014-11-16, because old nodes will reject new nodes with more than 110 peers. Updates only take a few hours to spread, so this should only cause short term disruption.

Additionally Matthew's (toad_'s) summer work on a custom on-disk format is done. This release lays the groundwork to include the results of that work [in the next release][url_toad]. This is designed for less disk activity and better behavior when corrupted.

This release coincides with the 25th anniversary of the demolition of the Berlin wall (Mauerfall), which marked the beginning of the end of a large censorship and surveillance regime. May censorship be demolished everywhere!

Thank you for using Freenet!

- Steve Dougherty and Arne Babenhauserheide

The link to http://127.0.0.1:8888 works for default Freenet nodes, but will not work for some setups. If you have a nonstandard setup, you should know the correct URL to use.
""") + "\n\n" + """
[url_bug3208]: https://bugs.freenetproject.org/view.php?id=3208
[url_peermath]: https://github.com/freenet/fred/pull/286
[url_toad]: http://127.0.0.1:8888/USK@pxtehd-TmfJwyNUAW2Clk4pwv7Nshyg21NNfXcqzFv4,LTjcTWqvsq3ju6pMGe9Cqb3scvQgECG81hRdgj5WO4s,AQACAAE/blog/23/Content-626611C.html
"""),
        # from here news items were selectively migrated as old release notes aren't that useful to keep around
        # TODO: Include all items again and select them in index.py instead.
        NewsItem("2013-tor-bust", _("2013-08-05 - Statement on the recent Freedom Hosting (Tor) bust"),
                 _("""
According to [the press](http://arstechnica.com/tech-policy/2013/08/alleged-tor-hidden-service-operator-busted-for-child-porn-distribution/), half of the hidden sites on Tor are now down, apparently connected to the arrest of a man allegedly behind Freedom Hosting, a hosting service for Tor hidden services. Some of these sites were said to offer illegal content and were apparently run by the FBI for two weeks, using a Javascript-based browser exploit to try to find their users.

This has had no effect on Freenet and could not happen on Freenet. Tor hidden services are centralised: A hidden service on Tor is run by a single server somewhere, and if this server is found, the whole site can be shut down, or compromised. In this case half the hidden sites on Tor were run on the same group of servers! See the [Tor blog](https://blog.torproject.org/blog/hidden-services-current-events-and-freedom-hosting) and [mailing list](https://lists.torproject.org/pipermail/tor-announce/2013-August/000089.html).

On Freenet, anything you upload is distributed across the network across thousands of separate nodes all over the world, and will remain available for as long as it remains sufficiently popular: Freenet is a distributed data storage network designed to prevent censorship, provide anonymity and be hard to block. To see more information on the difference between Freenet and Tor, see [our explanation in the FAQ](https://freenetproject.org/faq.html#tor).

Also, the Javascript exploit mentioned would not have worked on Freenet because Freenet removes Javascript by default. The Tor Browser Bundle has an option to block Javascript. We recommend that you enable this if you use Tor.

Furthermore, there was no attack against Tor itself: As far as we know, no users of the major "darknets" (Freenet, Tor and I2P) has been traced by attacking the networks, by law enforcement or anyone else. In this case, it appears to have been user error, not a problem with Tor itself. Similarly on Freenet, users need to be careful, and Freenet will often tell you when you are about to do something risky.

Having said that, Freenet's security is not perfect, and there are some known (but theoretical) weaknesses, so it might be possible for an attacker with relatively limited resources to trace individual Freenet contributors. Most of Freenet's weaknesses can be addressed by making long-lived connections with people that you trust, i.e. building a friend-to-friend "darknet". This functionality is already a part of the regular Freenet software, but we need more users who use Freenet in friend-to-friend mode to improve anonymity.

We have planned further improvements, which should greatly improve security (censorship resistance, anonymity and resistance to blocking), speed and usability. The expanding online surveillance from both governments (e.g. PRISM) and private corporations clearly show that tools such as Freenet, TOR and I2P are essential for a healthy democracy.

Please help us secure freedom of access to information by contributing to the Freenet-project with code, donations, translations, or just by running a node or creating content (anonymously)!

Volunteers - especially developers - are always very welcome. Feel free to contact us, through [IRC online chat](help.html#irc), [the mailing lists](help.html#mailing-lists), or on Freenet itself in the "freenet" board on FMS.

For press enquiries please contact [Ian Clarke](mailto:ian@freenetproject.org).
""")),
        NewsItem("2013-second-developer-xor", _("2013-06-26 - Freenet gets a second paid developer to fix the Web of Trust!"),
                 _("""
Long time coder xor (also known as p0s) has agreed to work, in a paid role, for us on fixing the Web of Trust plugin. This is a crucial component of many Freenet plugins:

*   **Sone**, an anonymous social network / microblogging tool.
*   **Freemail**, a private and untraceable email over Freenet system.
*   A filesharing system as yet unnamed which a student is working on.
*   Extensions to Infocalypse, being worked on by another student, a tool for managing source code which is vital to developing software over Freenet.

See the Freenet Social Networking Guide for how to load the first 2 plugins.

xor is well qualified for the role as he wrote most of the current code in the Web of Trust. The immediate priority will be to improve stability and performance by implementing a new more efficient FCP API. After that further optimisations are planned.

Freenet relies on unpaid volunteer developers as well as a few key paid developers. Toad (Matthew Toseland) is returning to full time work for Freenet after a study break, although he is off to university in October, and xor is just starting working for Freenet.

Improving the Web of Trust should substantially improve the performance of the key tools mentioned above and may be used by more in the future. Thanks to all our developers and donors!
""")),
        NewsItem("2012-traceback-attack", _("2012-09-11 - Response to the University of Hawaii's \"Experimental Study of Accountability in Existing Anonymous Networks\""),
                 _("""
Some academics [have published](http://www.ee.hawaii.edu/~dong/traceback/index.htm) a couple of attacks against Freenet, and they appear to be working on more as part of a project to unmask anonymous Freenet users. Build 1411, which was released on the 3rd of September, makes their main attack largely impractical. Nonetheless, we are working on improvements to both make this attack harder and to solve some of the [other known attacks](https://freenetproject.org/faq.html#attack). You can learn more about the attacks and our solution to them on our chief developer's [personal blog](http://amphibian.dyndns.org/flogmirror/#20120911-security).

We welcome all work to understand Freenet's security and expose any problems with it, although we would suggest that next time they might let us know before they make the paper public, as is common practice in the security community.

Finally, the long term solution is to build a darknet, a Freenet network where people only connect directly to people they trust. That means, get your friends using Freenet, and then add them as Friends on your node. When enough people use Freenet and form darknet connections, we won't need opennet, and this makes all attacks dramatically harder. We will work on making this easier and faster in the near future, as well as fixing the Pitch Black attack.
""")),
        NewsItem("freedom-house-april-2011", _("2011-04-13 - Freenet top anti-censorship tool in survey of Chinese users!"),
                 _("""
A [report](http://www.freedomhouse.org/sites/default/files/inline_images/Censorship.pdf) by [Freedom House](http://freedomhouse.org/) surveyed users in Azerbaijan, Burma, [China](http://www.freedomhouse.org/sites/default/files/LOtF_China.pdf) and Iran for their perceptions of and preferred tools for bypassing local government censorship. In China, Freenet was the only anti-censorship tool to achieve 5 stars, and the third most widely used overall.
""")),
    ]

class NewsPage(Page):
    def __init__(self):
        self.slug = "news"
        self.title = _("News")
        self.first_section_in_menu = False
        self.sections = [
            NewsSection(),
        ]

class NewsSection(Section):
    def __init__(self):
        self.slug = "news"
        self.title = ""

    def generate(self):
        return self.get_content()

    def get_content(self):
        return concat_html([x.render() for x in news_items()])

