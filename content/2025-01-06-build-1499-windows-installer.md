---
author: Arne Babenhauserheide
layout: content
title:  1499 installer re-released
date:   2025-01-06
categories: release
---
The Windows Installer for Freenet / Hyphanet 0.7.5 build 1499 has been re-released

> **Install Freenet / Hyphanet** for **[Windows][windows-installer]**, for **[GNU/Linux, macOS and other *nixes][linux-installer]**, or for **[Android][android-package]**. See the [download page][download page] for more information and other platforms (Apple Silicon needs library updates to work).

<div style="float: right; width: 30%; max-width: 300px;"><img src="./theme/images/logo-large.png" width="100%" style="filter: invert(30%)"  /></div>

The Windows installer for 1499 had a regression that caused it to lack
dependencies. The reason was a mistake in updating the Gradle build
file of the installer so the dependencies were not properly read from
the main project.

This only affects new installs: auto-update should cause no problems.
Installing on GNU/Linux/macOS/*nix is unaffected.

The Windows installer has been re-released and the downloads are
fixed.

There is a remaining regression in 1499 that can cause high CPU load
on pure friend-to-friend nodes. It will soon be fixed in an emergency
build 1500 release.

We’re sorry for inconvenience this causes.

<div style="clear: both"></div>

## Contribute

_Join our core._

If you want to help us get better, please chat with us in <a href="https://web.libera.chat/?nick=Rabbit|?#freenet" id="chatlink" class="btn button-custom btn-custom-two">#freenet @ irc.libera.chat</a>. And give us time to answer, we’re all volunteers and might not be in your timezone. It already helps a lot if you try out our test releases on a platform you use.

To get into development right-away, have a look at one of the [Freenet / Hyphanet Projects](https://github.com/hyphanet/wiki/wiki/Projects) or just get [fred](https://github.com/hyphanet/fred) and fix something that annoys you.

And to take on something that makes a big difference, have a look at the [high-impact tasks](https://github.com/hyphanet/wiki/wiki/High-Impact-tasks).

In addition to coding, spreading Hyphanet, joining the community, writing a decentralized website, and other ways to contribute within Hyphanet, you can join the awesome team of translators [at transifex][transifex-project]. They are the reason why we’re able to support several different languages, the often unseen heroes who make our work accessible to those who need it the most.


## What is Freenet / Hyphanet?

Hyphanet is the original Freenet,  
a peer-to-peer platform for  
censorship-resistant and privacy-respecting  
publishing and communication.

> I worry about my child and the Internet all the time, even though
> she's too young to have logged on yet. Here's what I worry about. I
> worry that 10 or 15 years from now, she will come to me and say
> 'Daddy, where were you when they took freedom of the press away from
> the Internet? --Mike Godwin, Electronic Frontier Foundation

_What about the name „Hyphanet“? See [Freenet renamed to Hyphanet][freenet-hyphanet]._


That Hyphanet can keep moving forward and help people worldwide to
exercise their basic rights and freedoms is the work of amazing
volunteers, both contributors and people running Hyphanet nodes.

Thank you for your contributions, and thank you for using Freenet / Hyphanet!

\-- AB

> **Install Freenet / Hyphanet** for **[Windows][windows-installer]**, for **[GNU/Linux, macOS and other *nixes][linux-installer]**, or for **[Android][android-package]**. See the [download page][download page] for more information and other platforms.


[high-impact-task]: https://github.com/hyphanet/wiki/wiki/High-Impact-tasks
[Roadmap]: https://github.com/hyphanet/wiki/wiki/Roadmap
[exe signing workflow]: https://github.com/hyphanet/sign-windows-installer
[verify-build script]: https://github.com/hyphanet/scripts/blob/master/verify-build
[debian-package]: https://www.draketo.de/dateien/freenet/build01499/hyphanet-fred-build01499.deb
[gentoo-package]: https://gitweb.gentoo.org/repo/gentoo.git/tree/net-p2p/freenet/
[arch-package]: https://aur.archlinux.org/packages/freenet
[guix-package]: https://git.sr.ht/~pranavats/freenet-guix/tree/master/item/freenet.scm
[transifex-project]: https://explore.transifex.com/otf/freenet/
[freenet-hyphanet]: https://www.hyphanet.org/freenet-renamed-to-hyphanet.html
[pyFreenet]: https://github.com/hyphanet/pyFreenet

[releasetag1499]: https://github.com/hyphanet/fred/releases/tag/build01499
[download page]: pages/download.html
[windows-installer]: https://www.draketo.de/dateien/freenet/build01499/FreenetInstaller-1499.exe
[linux-installer]: https://www.draketo.de/dateien/freenet/build01499/new_installer_offline_1499.jar
[android-package]: https://freenet-mobile.github.io/app/
