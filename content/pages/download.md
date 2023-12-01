---
title: Download
lang: en
[url_lysator]: https://www.lysator.liu.se/index_en.html
[url_mirror_lysator]: https://ftp.lysator.liu.se/pub/freenet/
[url_mirror_lysator_tor]: http://lysator7eknrfl47rlyxvgeamrv7ucefgrrlhk7rouv3sna25asetwid.onion/pub/freenet/
[url_win_installer]: https://www.draketo.de/dateien/freenet/build01497/FreenetInstaller-1497.exe
[url_win_installer_sig]: https://www.draketo.de/dateien/freenet/build01497/FreenetInstaller-1497.exe.sig
[url_mac_installer]: https://github.com/freenet/mactray/releases/download/v2.1.0/FreenetTray_2.1.0.zip
[url_mac_installer_sig]: https://github.com/freenet/mactray/releases/download/v2.1.0/FreenetTray_2.1.0.zip.sig
[url_nix_installer]: https://www.draketo.de/dateien/freenet/build01497/new_installer_offline_1497.jar
[url_nix_installer_sig]: https://www.draketo.de/dateien/freenet/build01497/new_installer_offline_1497.jar.sig
[url_jnlp_installer]: {static}/assets/jnlp/freenet.jnlp?1497
[url_keyring]: #keyring
[github_release_url]: https://github.com/freenet/fred/releases/tag/build01497/

<!--
Steps:

* [Download and install Hyphanet][autostart]
* [Add friends (or connect to strangers)][add_friends]
* [Start using Hyphanet!][usage]

[autostart]: #autostart
[add_friends]: #note
[usage]: #usage
-->

Download and install Hyphanet:

* [For Windows](#windows)
* [For macOS, GNU/Linux & POSIX](#gnulinux-posix)

<!--* [For macOS](#macos)-->

*Hyphanet is free and open source software available under GPLv2+. The source code is on [GitHub](https://github.com/freenet/fred).*

## Windows

Download and run [the installer][url_win_installer] ([gpg signature][url_win_installer_sig]; [keyring][url_keyring])

[Download Hyphanet for Windows][url_win_installer]{: .download-button}

It will automatically install Hyphanet and other required components for you.
When done, your default browser will automatically open up to Hyphanet's
web-based user interface.

![]({static}/assets/img/install/1-langselect-windows.png)

Hyphanet requires Windows 8.1 or later.

Free code signing provided by
[SignPath.io](https://about.signpath.io/), certificate by SignPath
Foundation.

**Note**: Once a Windows version reaches end of life, we do not guarantee
any longer support, or the fact that Hyphanet will install and/or work in
such environments. However, it is not mandatory that Hyphanet will not work
on an older Windows OS. We always strongly recommend you to take security
very seriously, and run up to date software that receives security updates,
to be on the safe side.

<!--
## macOS

Download and run [the installer][url_mac_installer] ([gpg signature][url_mac_installer_sig]; [keyring][url_keyring]).

**The installer currently has some problems. If it fails, use the GNU/Linux installer below.**

[Download Hyphanet for macOS][url_mac_installer]{: .download-button}

It will automatically install Hyphanet and other required components for you.
When done, your default browser will automatically open up to Hyphanet's web-based user interface.

![]({static}/assets/img/mactray/osx_installer_step2_transparent.png)

Hyphanet requires macOS 10.8 or later.

-->

## GNU/Linux & POSIX

Get the [Java-based installer][url_nix_installer] ([gpg signature][url_nix_installer_sig]; [keyring][url_keyring]).

[Download Hyphanet for GNU/Linux & POSIX][url_nix_installer]{: .download-button}

Run the file with Java, then follow the installer:

![]({static}/assets/img/install/1-langselect.png)

You need to have a recent **Java Runtime Environment** (JRE), for
example **OpenJDK** which can be obtained via your
[package manager](https://en.wikipedia.org/wiki/Package_manager) or from
[https://adoptopenjdk.net](https://adoptopenjdk.net).

Java version 9 or higher is required.

If there are problems, use the command line. This requires
wget which can be installed with a package manager, such as
`sudo apt-get install wget` on Debian or Ubuntu.

    wget 'https://www.draketo.de/dateien/freenet/build01497/new_installer_offline_1497.jar' -O new_installer_offline.jar;
    java -jar new_installer_offline.jar;

To install on a headless system, or if you get fontconfig problems, use the `-console` option and follow the prompts:

    java -jar new_installer_offline.jar -console;


**Note**: We would love to have packages for most distributions. There
is a [package for Gentoo](https://packages.gentoo.org/packages/net-p2p/freenet), and a
[Debian package](https://github.com/freenet/fred/pull/774). The debian
Package also works on WSL2 (but not WSL1). If you would like to help,
it would be much appreciated!

**Note**: On some systems (including FreeBSD and OpenBSD) the wrapper does
not work, unless you install additional software packages and configure it.
You can start Hyphanet manually there, but you then don’t have
auto-updates. After installation you find the relevant classpath
arguments in wrapper.conf. Then call java directly with a command like `java -Xmx1500m -Xss512k -Dnetworkaddress.cache.ttl=0 -Dnetworkaddress.cache.negative.ttl=0 --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED  -cp bcprov-jdk15on-1.59.jar:freenet-ext.jar:freenet.jar:jna-4.5.2.jar:jna-platform-4.5.2.jar:pebble-3.1.5.jar:unbescape-1.1.6.RELEASE.jar:slf4j-api-1.7.25.jar freenet.node.NodeStarter`

## Release Mirror

Our releases are provided via Lysator. You can try the
[http mirror][url_mirror_lysator] or the [tor mirror][url_mirror_lysator_tor] 
provided by [Lysator][url_lysator].

Alternatively you can use the [github release][github_release_url].

## Mirrored installation

If you have a working Hyphanet installation directory that you have mirrored
from one Unix machine to another (e.g. via rsync or unison), enabling the
mirrored installation is not difficult. Nothing in a Hyphanet installation
cares about its host's IP address; it can't, or Hyphanet would fail on
machines that get IP addresses from a DHCP pool.

All you actually need to do is tell the system you've mirrored to that it
should start the Hyphanet proxy daemon for you on boot. Do `crontab -l`
on the source machine, find the line that is tagged "FREENET AUTOSTART" and
add that to your crontab on the mirrored machine.

However: each installation has a unique identity key generated at
installation time. If you try to run two instances with the same identity _at
the same time_, both proxy demons will become confused and upset. Don't do
this!

## Using Hyphanet

Please try the [step by step guide][url_freesocial] to setting up Hyphanet and various Hyphanet apps,
especially if installing on macOS.
We are not responsible for unofficial third party apps it recommends (including FMS),
but many Hyphanet users and developers use them.

### Firewalls and routers

Hyphanet should work fine with most routers, but if you are having problems
and you have a firewall or router, click [**here**](help.html#firewall) for
some info.

### So it's running, what do I do?

When the installer closes, it should open a browser window pointing to the
first-time wizard. Here you can configure basic settings, and then start
using Hyphanet. You can access Hyphanet later on via the system tray menu (
bottom right on the screen), or use the Browse Hyphanet shortcut on the
desktop and/or start menu. If it doesn't work, open
[http://127.0.0.1:8888/](http://127.0.0.1:8888/) in your web browser.

For best security you should use a separate browser for Hyphanet, preferably
in privacy mode. On Windows, the system tray menu will try to use Chrome in
incognito mode if possible. Internet Explorer does not work well with
Hyphanet, Firefox and Opera are widely used.

If you know anyone running Hyphanet, you can improve your security and help to
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

### So I'm connected, what do I do?

Hyphanet itself includes anonymous websites ("freesites"), filesharing,
searching, and more, but you can also use third party applications for chat,
filesharing, to help you upload freesites, etc.

The [Hyphanet Social Networking Guide](http://freesocial.draketo.de/) explains
how to set up the main third party tools, including email, forums and
micro-blogging (Sone, a bit like twitter).

### It doesn't work, now what?

If you have problems installing or running Hyphanet, please see the [knowledge base][kb_url], [FAQ][faq_url], [chat][chat_url], or [mailing list][ml_url].

[kb_url]: https://support.freenetproject.org/kb
[faq_url]: help.html#faq
[chat_url]: help.html#irc
[ml_url]: help.html#mailing-lists

### Hardware requirements

Generally a 1GHz processor and 1GB of RAM should be fine. Hyphanet will run on
smaller systems, but it uses at least 128MB of RAM, so unless the system does
nothing else it will struggle in less than 512MB. However, the processor is
less of a problem, people have been known to run it on 400MHz Pentium 2's or
ATOM's, although downloads and browsing would be slow.

Hyphanet will use a portion of your disk for storing data, you can configure
this to any size from 100MB upwards, but we recommend at least 1GB. Hyphanet
also uses disk space for your downloads. Hyphanet's memory usage is
approximately 256MB plus 400kB for every 2GB of datastore.

On 64-bit Windows, we will install a 32-bit Java Virtual Machine because of
limitations of the [Java Service Wrapper](
http://wrapper.tanukisoftware.org/doc/english/download.jsp).

### Upgrading

Hyphanet provides an upgrade-over-Hyphanet mechanism: It will keep itself up to
date automatically from other Hyphanet nodes, and this will normally work even
if it is unable to route to them due to them being too new. This is anonymous
and secure, and we recommend people use it. However, if something is severely
broken, you can upgrade your node manually from our servers:

* Windows users can upgrade to the latest-stable Hyphanet release
  by running `update.cmd` in the Hyphanet directory.
* macOS, GNU/Linux, or other POSIX users may upgrade by running the `update.sh`
  shell script in the Hyphanet directory.

[url_freesocial]: http://freesocial.draketo.de/

## Add friends (or connect to strangers)

If you know other people who also use Hyphanet, you can [add them as Friends][url_addfriend].
This will make you safer against attacks on Hyphanet Project infrastructure
(the [seednodes][url_seednode_info]).

Once you are connected to 5 or more friends, you can enable **high security mode**.
In high security mode Hyphanet will only connect to your friends.
This makes your usage of Hyphanet almost undetectable,
but you are still able to access the rest of the network through your friends' friends friends ....

You don't have to add friends right now.
If you use a "low" or "normal" security level Hyphanet will automatically connect to strangers and will work just fine.
However, your (or someone else's) government may be able to find out who you are with enough effort. Be careful!

[url_addfriend]: http://127.0.0.1:8888/addfriend/
[url_seednode_info]: https://wiki.freenetproject.org/Seed_nodes#Seed_node

## Verifying Signatures

Download the [Hyphanet Project signing keys][url_keyring] and import them into your keyring:

        pub   2048R/0xEAC5EBF07AA9C2A3 2013-04-29
              Key fingerprint = DBB7 7338 3BC3 49C9 5203  ED91 EAC5 EBF0 7AA9 C2A3

        pub   4096R/0x00100D897EDBA5E0 2013-09-21 [expired: 2016-09-08]
              Key fingerprint = 0046 195B 2DCA B176 D394  09CD 0010 0D89 7EDB A5E0
        uid                  Steve Dougherty (operhiem1 Release Signing Key) <steve@asksteved.com>
        sub   4096R/0x7BF0F7B36AC8B380 2013-09-21 [expired: 2016-09-15]

        pub   4096R/0xFF24CA421946AA94 2013-09-24 [expires: 2018-09-23]
              Key fingerprint = B76D 4AA7 96D8 403E ED78  C9F9 FF24 CA42 1946 AA94
        uid                  Matthew Toseland (2013-2018 key, higher key length) <matthew@toselandcs.co.uk>
        uid                  Matthew Toseland (2013-2018 key, higher key length) <toad@amphibian.dyndns.org>
        sub   4096R/0xF877E62895C42009 2013-09-24 [expires: 2018-09-23]

        pub   4096R/0xB67C19E817A8D846 2016-01-02 [expires: 2018-01-03]
              Key fingerprint = 5D77 D9A4 2E28 0F5A FF8F  2EBF B67C 19E8 17A8 D846
        uid                  Stephen Oliver <steve@infincia.com>
        sub   4096R/0x9BCDD1614041F59E 2016-01-02 [expires: 2018-01-03]
        sub   4096R/0x1652EBA5AC1BB386 2016-01-02 [expires: 2018-01-03]
        sub   4096R/0x38A62E479684F2F2 2016-01-02 [expires: 2018-01-03]

        pub   4096R/0xB41A6047FD6C57F9 2017-02-23
              Key fingerprint = B30C 3D91 069F 81EC FEFE  D0B1 B41A 6047 FD6C 57F9
        uid                  Arne Babenhauserheide (freenet releases) <arne_bab@web.de>
        uid                  Arne Babenhauserheide (ArneBab) <arne_bab@web.de>

[url_keyring]: {static}/assets/keyring.gpg
