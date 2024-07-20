---
lang: en
author: Arne Babenhauserheide
layout: content
title:  Freenet/Hyphanet 1498 installer delayed
date:   2023-07-20
categories: release
---
Freenet / Hyphanet 0.7.5 build 1498 has been **released via auto-update**
on the network, but installers are still delayed due to security
testing of the signing infrastructure.

> **Install Freenet / Hyphanet** for **[Windows][windows-installer]**, for **[GNU/Linux, macOS and other *nixes][linux-installer]**, or for **[Android][android-package]**. See the [download page][download page] for more information and other platforms.

<div style="float: right; width: 30%; max-width: 300px;"><img src="./theme/images/logo-large.png" width="100%" style="filter: invert(30%)"  /></div>

Windows installers have to be signed to avoid triggering warning
messages. Due to the [forced renaming][] we have to establish a
[new signing workflow][] with a new signature provider.

The new signature provider has a higher standard of security. This is
something we cherish, because the signing pipeline we built for that
now always runs the script [verify-build][] on every release. That
script checks whether what is released as `jar` actually matches what
can be built from sources. That way developers cannot be pressured to
smuggle treacherous code into binary releases without automatically
raising red flag. Until now we had to rely only on anonymous users
running this script — that’s still the safest, so please keep doing
that — and now we have a second layer of protection.

This higher standard of security means, though, that they are getting
their github actions support checked by a thirdparty security tester,
and this takes time.
Therefore it will still take some time until we can provide a new
Windows installer. Until then, please install using the older
installers.

If you install from such an installer, your node will update
automatically to the most recent version once after it connected to
the network. [Build 1498][releasetag1498] has already been deployed
networkwide, so this is what you’ll get.

We will additionally provide the new release on this website once the
installers are ready.

<div style="clear: both"></div>


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

_What about the name Hyphanet? See [Freenet renamed to Hyphanet][freenet-hyphanet]._


That Hyphanet can keep moving forward and help people worldwide to
exercise their basic rights and freedoms is the work of amazing
volunteers, both contributors and people running Hyphanet nodes.

## Contribute

If you want to help us get better, please chat with us in <a href="https://web.libera.chat/?nick=Rabbit|?#freenet" id="chatlink" class="btn button-custom btn-custom-two">#freenet @ irc.libera.chat</a>. And give us time to answer, we’re all volunteers and might not be in your timezone.

To get into development right-away, have a look at one of the [Freenet / Hyphanet Projects](https://github.com/hyphanet/wiki/wiki/Projects) or just get [fred](https://github.com/hyphanet/fred) and fix something that annoys you.

And to take on something that makes a big difference, have a look at the [high-impact tasks](https://github.com/hyphanet/wiki/wiki/High-Impact-tasks).



Thank you for your contributions, and thank you for using Freenet / Hyphanet!

\-- AB

> **Install Freenet / Hyphanet** for **[Windows][windows-installer]**, for **[GNU/Linux, macOS and other *nixes][linux-installer]**, or for **[Android][android-package]**. See the [download page][download page] for more information and other platforms.


[high-impact-task]: https://github.com/hyphanet/wiki/wiki/High-Impact-tasks
[Roadmap]: https://github.com/hyphanet/wiki/wiki/Roadmap
[exe signing workflow]: https://github.com/hyphanet/sign-windows-installer
[verify-build script]: https://github.com/hyphanet/scripts/blob/master/verify-build
[debian-package]: https://www.draketo.de/dateien/freenet/build01498/hyphanet-fred-build01498.deb
[freenet-hyphanet]: https://www.hyphanet.org/freenet-renamed-to-hyphanet.html

[releasetag1498]: https://github.com/hyphanet/fred/releases/tag/build01498
[download page]: pages/download.html
[windows-installer]: https://www.draketo.de/dateien/freenet/build01497/FreenetInstaller-1497.exe
[linux-installer]: https://www.draketo.de/dateien/freenet/build01497/new_installer_offline_1497.jar
[android-package]: https://freenet-mobile.github.io/app/
[forced renaming]: /freenet-renamed-to-hyphanet.html
[verify-build]: https://github.com/hyphanet/scripts/blob/master/verify-build
[new signing workflow]: https://github.com/hyphanet/sign-windows-installer/blob/main/.github/workflows/ci.yml
