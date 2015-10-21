# -*- coding: utf-8 -*-
# Python code copyright Gerard Krol, license: MIT
import string
import markdown
from .common import *

class DocumentationIntroSection(Section):
    def __init__(self):
        self.slug = "documentation-intro"
        self.title = _("Documentation")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
The documentation on Freenet is forever changing, since this is a project in
development. However, here under the Documentation menu, you may find usage
documents on how to setup Freenet and use the most popular Freenet tools as
well as a user driven Wiki and an extensive Frequently Asked Questions
department.

*   [**Install**](#install)
     Contains detailed instructions on how to install Freenet using the new
     installer.
*   [**Connect**](#connect)
     How to connect to Freenet.
*   [**Content**](#content)
     Freenet as a Content Distribution System.
*   [**Understand**](#understand)
     Explains the workings of Freenet, and a glossary with the most frequently
     used terms.
*   [**Freemail**](#freemail)
     How to setup Freenets own anonymous email service.
*   [**Frost**](#frost)
     Frost is the oldest and most used messaging and file sharing tool in the
     Freenet suite. This describes how to set it up and use it for the first
     time.
*   [**jSite**](#jsite)
     jSite is a Freenet website (a.k.a. Freesite) insertion tool.
*   [**Wiki**](https://wiki.freenetproject.org/)
     The Freenet Wiki is a user driven space where new features may be described
     before finding its way into the website. It is a good source of information
     about all sorts of Freenet related issues.
""")))

class InstallSection(Section):
    def __init__(self):
        self.slug = "install"
        self.title = _("Install")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
To install Freenet might not be as difficult as you might have heard. There are
two ways to install Freenet:

*   Graphical install
*   Headless install
*   Enabling a mirror copy of a Freenet installation

If you want to install the Freenet software on a computer which lacks a GUI,
see the [Headless install](download.html#unix) instructions. If you have
mirrored a working Freenet installation to a machine without explicitly
installing it, see [Mirrored install](download.html#mirrored). Otherwise,
continue reading.
""") + "\n\n" + _("""
#### Graphical install

**The below is outdated for Windows systems**, for Windows you should use
[the Windows installer](assets/jnlp/FreenetInstaller.exe) as described on
[the download page](download.html). You can also get the Windows installer
from [here](https://downloads.freenetproject.org/latest/FreenetInstaller.exe).

For a graphical installation you have to have:

*   A working Java Runtime Environment,
*   a downloaded copy of [new_installer_offline.jar](assets/jnlp/freenet_installer.jar)
    (if this does not work try [here](https://downloads.freenetproject.org/latest/new_installer_offline.jar))
*   a working graphical user interface (GUI)

You should save the new_installer.jar file somewhere were you can find it
again. Your home-directory should be a good place. The next step requires you
to know where you stored the file (the path to it), so it is quite important
that you do that step thoroughly.
""") + "\n\n" + _("""
To start the installation, open a command line interface/terminal/shell
window. Exchange the **/path/to** to the real path (for example:
/home/username/download/new_installer.jar) to the new_installer.jar-file and
type:

<pre>	$ java -jar /path/to/new_installer_offline.jar</pre>

The first window you should see is the one below, which allows you to select
your preferred language for the installation program.

<img height="160" src="assets/img/install/1-langselect.png" />

Next is shown an about-box, some information about the version of Freenet and
authors. Just click **Next** to proceed.

<img height="457" src="assets/img/install/2-about.png" />

The next step is to choose the directory in which to install Freenet. The
default location on GNU/Linux & POSIX operating systems is
**/home/username/Freenet** as shown below. Change it to something appropriate or
leave "as is". Click **Next** when you are finished.

<img height="458" src="assets/img/install/4-Install_directory.png" />

Select the packages that you want to install with your Freenet software.
Since it takes up virtually no extra disk-space, it is recommended that you
leave all packages selected and press **Next**.

<img height="458" src="assets/img/install/5-select_packages.png" />

In the next stage, the packages are installed, and a progress meter runs
across the window. When it is finished, press **Next** to continue to the
next step.

<img height="457" src="assets/img/install/6-Install_packages.png" />

After that, the Freenet software is installed and/or upgraded, plugins are
enabled and the environment is started. When completed, press **Next** to
proceed.

<img height="454" src="assets/img/install/7-install_progress.png" />

For some graphical environments, shortcuts in the menu-structure can be
created. This is not the case for all of the platforms that Freenet run on.
However, there should be created shortcuts on the desktop in all supported
environments. Change the application group according to your needs and press
**Next** when finished.

<img height="458" src="assets/img/install/8-create_shortcuts.png" />

After that, the installation is finished. Click **Done** to close the window.

<img height="457" src="assets/img/install/9-Install_finished.png" />

If all has gone well, a browser window should have opened in the background.
This will ask you a bunch of questions to configure Freenet, and then you
should be able to use it.
""") + "\n\n" + _("""
It will ask about network security level - "protection from strangers
attacking you over the internet". If you choose LOW or NORMAL, Freenet should
"just work", connecting in a few minutes. If you choose HIGH or MAXIMUM,
Freenet will need you to add Friends before you can use it. These must be
people you personally know. Adding people you don't know will not improve
security.
""")))

class ConnectSection(Section):
    def __init__(self):
        self.slug = "connect"
        self.title = _("Connect")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
There are two ways to connect to Freenet:

* You can enable insecure mode (the installation wizard will ask you) and
  Freenet will automatically find nodes to connect to - Strangers.
* You can connect to nodes run by people you know - Friends. Note that these
  should be people you actually know on some level, in order to maintain good
  network topology and maximum security.

In practice, you should probably use both of these options, unless you are
really paranoid, in which case you should of course only connect to people
you trust. Insecure mode should work automatically once enabled, so the rest
of this page is about connecting to Friends.

To connect to your friends' nodes, you have to exchange Node references with
them. The references must be added on **both sides** to be established. That
is, you need to add his/hers, and he/she needs to add yours.
""") + "\n\n" + _("""
*When you have a freshly connected node, you have no data cached in your
datastore, and very few connections even if insecure mode is enabled.
Requests are sent out in a random fashion. **This makes some (or all)
requests time out before retrieving anything.** It takes a couple of days for
your Freenet-node to get up to speed, so please don't get discouraged by this.*

You should have at least three nodes that are connected to you at all times,
ideally at least five to seven. Since some nodes may be unreachable at times,
you need to connect to some more nodes to get the expected number. The nodes
that are connected directly to you are the only nodes on freenet that might
see what kind of traffic that passes through to your Freenet node. But if
insecure mode is enabled, any node can find yours; this is the big advantage
of **not** enabling insecure mode: you are effectively invisible except to
your Friends. In practice most people start off with insecure mode and
gradually add Friends, and hopefully turn off insecure mode once they have at
least 10 Friends.
""") + "\n\n" + _("""
<img height="587" src="assets/img/Freenet-architecture-small.png" />

*Figure 1: Visible Freenet connections*

**Node A** in the figure also has a number of nodes connected to it, but they
are all (except from your own node) invisible to you. The traffic routing
algorithm is therefore only able to direct traffic to one of the few nodes
that you know of that it thinks is most able to find what you are looking for.

The traffic is encrypted, so it is quite difficult for the nodes that you
connect to to see what your Freenet-traffic consists of, but it is far from
impossible. It is therefore important that you connect only to people you
know. If that is not possible, then at least people you've talked to.

There are a number of ways to add peer node references.
""") + "\n\n" + _("""
### Fproxy

Connecting peer nodes with FProxy can be done in several ways. Common for all
these are that they are all done under the **Darknet** menu item or using the
[http://127.0.0.1:8888/friends/](http://127.0.0.1:8888/friends/) link. Below
is the thing that makes it all happen:

<img height="295" src="assets/img/add_peers.png" />

As you can see, there are three ways of getting a node reference from someone
else:

*   Pasting it "as is", in the top field,
*   a URL pointing at the reference, or
*   a file, containing the reference.

[http://dark-code.bulix.org/](http://dark-code.bulix.org/) is a so called
**paste-bin**, where you can add your node reference, make sure that the
**private** box is checked, and press **Paste**.

The paste-bin then returns an URL (e.g.
http://dark-code.bulix.org/yuf01h-34676?raw), which can be shared with
others. Make sure that you add **?raw** to the link. This makes the link
point only to the actual pasted data, with no extra design elements.

Your own Freenet reference can be found on the [
http://127.0.0.1:8888/friends/](http://127.0.0.1:8888/friends/) page,
under the caption **My reference**. It might look something like this (cut
for screen purposes):
""") + """

<pre>	lastGoodVersion=Fred,0.7,1.0,1010
	sig=7c7edc8c5250e42ac4cb161b216b70de7019221f1b331f0f92bd67439[...]609660f0d4
	identity=5tBtS3R59nfOTvc1be~V0sSfkWir8EW38YeocP0gsYM
	myName=FreenetTestInstall
	location=0.02970997399122577
	testnet=false
	version=Fred,0.7,1.0,1016
	physical.udp=83.255.75.223:13762
	ark.pubURI=SSK@M1wjFha2tujYo50QQF~5Fqz5anVEiIzI9VrA8IrhAsQ,5M[...],AQACAAE/ark
	ark.number=0
	dsaPubKey.y=JhlWYVx8rA0y0x1Fb3y9TfqXDYiIsnkEka8PLsePerpCELTIn[...]laHe2bkl0O7Dg
	dsaGroup.p=AIYIrE9VNhM38qPjirGGT-PJjWZBHY0q-JxSYyDFQfZQeOhrx4[...]ofeLdX7xhehuk
	dsaGroup.g=UaRatnDByf0QvTlaaAXTMzn1Z15LDTXe-J~gOqXCv0zpz83CVn[...]Fuqt8yZe1PDVg
	dsaGroup.q=ALFDNoq81R9Y1kQNVBc5kzmk0VvvCWosXY5t9E9S1tN5
	End</pre>

""" + _("""
Remember that both you and the node you are connecting to must add references
to make the connection work. This means that if you add a persons node
reference on your side, but that person does not add your reference on
his/her side, the connection **does not work**.
""") + "\n\n" + _("""
### Darknet peers

When you have a number of connections, you can visit the Darknet-page. It
should look something like this:

<img height="520" src="assets/img/Freenet-darknet_peers.png" />

There are a number of status messages that can be seen here:

* CONNECTED - the node is connected and ready to take your request
* BACKED OFF - the node is choked with traffic and unable to respond
* DISCONNECTED - the node is not connected to your node, and probably turned off
* NEVER CONNECTED - the connection between the nodes has not been established.
  This can be because of firewall problems/restrictions, one side not adding
  the other sides node reference or that the nodes has not been online at the
  same time yet in order to confirm the connection. If the problem persists over
  a long time and both sides have added each other, try to redo the connection.

In the Idle-column, you can see how much time has passed since the last status
message.
""")))

class ContentSection(Section):
    def __init__(self):
        self.slug = "content"
        self.title = _("Content")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
In addition to its anonymity features, as a content distribution network
Freenet has the following strengths:

*   **Totally decentralized**  
     Information can be inserted into Freenet for download without any reliance
     on a centralized server. All the inserter needs to do is give the content's
     "key" to someone else and they will be able to download it.
*   **Adaptive caching**  
     Many CDN architectures only allow peers which have already downloaded a
     file to share it with other peers. Freenet will adaptively cache
     information on peers as necessary to meet demand regardless of what that
     peer has downloaded. This allows Freenet to "scale-up" much more quickly
     than most solutions for popular files, and improves load-balancing.
*   **Strong Security**  
     Freenet has long-supported the concept of "Content Hash Keys" which
     guarantee the integrity of retrieved data. This approach has since been
     adopted by other architectures. Freenet also supports
     "Signed Subspace Keys" which allow content to be digitally signed. This
     also allows content integrity to be guaranteed, but is more flexible than
     CHKs.
*   **Forward Error Correction**  
     In-common with some other CDN architectures, Freenet employs "Forward Error
     Correction", which allows files to be reconstructed even if some of the
     parts of that file can't be retrieved. Uniquely, Freenet also supports
     "healing", which involves the reconstruction and reinsertion of missing
     file components.

This page contains links to freely available content on Freenet. If you would
like to add a new link please email it to [us](
https://emu.freenetproject.org/cgi-bin/mailman/listinfo/support) - remember
that we will only link to content that can be legally distributed in the
United States of America.
""")))

class UnderstandSection(Section):
    def __init__(self):
        self.slug = "understand"
        self.title = _("Understand")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
Freenet can be thought of as a large storage device. When you store a file in
it, you receive a key which can be used to retrieve the file. When you supply
Freenet with a key, it returns the appropriate file (if it is located). The
storage space is distributed among all connected nodes on Freenet.

Freenet is a Peer-to-peer network, which is both decentralized and
anonymized. The nodes that you connect to only knows its nearest neighbours
and has no idea about how the network as a whole is structured.
""") + "\n\n" + _("""
### Small world network

Freenet is built on the principle of small world networks. By connecting to
nodes of people you already know, and the people you know in turn connect to
people they know, one should be able to reach all nodes in a Freenet network.
""") + "\n\n" + _("""
### The datastore

All Freenet nodes contribute with a part of their harddrive space to store
files. The files are stored encrypted in the **store**-directory in the
Freenet installation directory.
""") + "\n\n" + _("""
Unlike other peer-to-peer networks, you as a user have little or no control
over what is stored in your datastore. Instead, files are kept or deleted
depending on how popular they are. This is to ensure that Freenet is
censorship resistant. The only possible way to remove something from Freenet
is to not search for it, and hope that everybody else does the same.
""") + "\n\n" + _("""
It is hard, but not impossible, to determine which files that are stored in
your local Freenet Datastore. This is to enable plausible deniability as to
what kind of material that lies on your harddrive in the datastore.
""") + "\n\n" + _("""
The initial diskspace allocated for the datastore is 5%% of available disk
space if it is over 20GB, 10%% if it is over 10GB, 512MB if under 10GB,
and 256MB if under 5GB. You can change the store size at any time, the more
the better, both for your personal browsing and for Freenet as a whole.
""") + "\n\n" + _("""
### Freenet Routing

Initially, each node has no information about the performance of the other
nodes it knows about. This means that routing of requests is essentially
random. But since different nodes have different randomness, they will
disagree about where to send a request, given a key. So the data in a
newly-started Freenet will be distributed somewhat randomly.
""") + "\n\n" + _("""
As more documents are inserted by the same node, they will begin to cluster
with data items whose keys (see below) are similar, because the same routing
rules are used for all of them. More importantly, as data items and requests
from different nodes "cross paths", they will begin to share clustering
information as well.
""") + "\n\n" + _("""
The result is that the network will self-organize into a distributed,
clustered structure where nodes tend to hold data items that are close
together in key space. There will probably be multiple such clusters
throughout the network, any given document being replicated numerous times,
depending on how much it is used.
""") + "\n\n" + _("""
### Freenet keys

Each file that exists on Freenet has a key associated with it. Freenet 0.7
has various types of keys. Keys are used for everything on freenet, and are a
kind of [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) (
e.g. freenet:=KSK@sample.txt).
""") + "\n\n" + _("""
Most keys are hashes: there is no notion of semantic closeness when speaking
of key closeness. Therefore there will be no correlation between key
closeness and similar popularity of data as there might be if keys did
exhibit some semantic meaning, thus avoiding bottlenecks caused by popular
subjects.
""") + "\n\n" + _("""
### Accessing data

To access a particular piece of data on Freenet, you can use FProxy. You need
to know the key to the data, and enter it like this (or click a link
containing the key):

<pre>	http://localhost:8888/[Freenet Key]</pre>

There are four types of keys in Freenet:

*   **CHK** - Content Hash Keys
*   **SSK** - Signed Subspace Keys
*   **USK** - Updateable Subspace Keys
*   **KSK** - Keyword Signed Keys
""") + "\n\n" + _("""
CHKs are the most fundamental. All files over 1kB are ultimately divided into
one or more 32kB CHKs. CHKs' filenames are determined only by their contents.
SSKs are the other basic type. These combine a public key with a
human-readable filename and therefore allow for freesites. KSKs are a variant
of SSKs where everything is determined by a simple human readable filename (
e.g. =KSK@sample.txt). These are spammable but convenient in some cases. And
USKs are a form of updatable keys especially useful for freesites and
**Address Resolution Keys**.
""") + "\n\n" + _("""
An Address Resolution Key (ARK) is an Updateable Subspace Key (USK) inserted
by the node whenever its IP address changes. It contains the reference for
the node - its cryptographic details, and in particular its IP address(es).
ARKs are a way to help people connect to Freenet if they have problems caused
by firewalls, routers or changing IP addresses. If someone cannot accept
incoming traffic it can make it difficult to connect.

ARKs are an implementation detail and you don't need to know anything about
them to use Freenet.
""") + "\n\n" + _("""
### Content Hash Keys

Content Hash Keys are for files with static content, like an .mp3 or a
PDF-document. These keys are hashes of the content of the file. A hash is a
reproducible method of turning a specific piece of data into a relatively
small number that serve as a sort of *fingerprint* for the data. If the file
content changes, even ever so little, the hash of the file changes radically.
This makes the data hard to tamper with without anyone noticing. A CHK
uniquely identifies a file, it should not be possible for two files with
different content to have the same CHK. The CHK consists of three parts:

1.  the hash for the file
2.  the decryption key that unlocks the file, and
3.  the cryptographic settings used
""") + "\n\n" + _("""
A typical CHK key looks like this:

    CHK@file hash,decryption key,crypto settings

or for example:

    CHK@SVbD9~HM5nzf3AX4yFCBc-A4dhNUF5DPJZLL5NX5Brs,bA7qLNJR7IXRKn6uS5PAySjIM6azPFvK~18kSi6bbNQ,AAEA--8

The decryption key is stored encrypted within the file, so it is not possible
to decrypt the file without the CHK key.

To access the file, the whole key must be pasted behind the FProxy address
(cut to fit screen):

    http://localhost:8888/CHK@SVbD9~[..]X5Brs,bA7qLN[..]Si6bbNQ,AAEA--8
""") + "\n\n" + _("""
### Signed Subspace Keys

Signed Subspace Keys are usually for sites that are going to change over
time. For example, a website that may need news to be updated or information
to be corrected, added or deleted. They work in such a way that someone else
can't put up a newer version of your site and pretend it was you who did it.

It works by using public-key cryptography so you can sign your site. Only the
person with the secret key can add updated versions of your site to Freenet.
""") + "\n\n" + _("""
Also the SSK consists of five parts:

* **public key hash** - This part is all that is required to uniquely identify
  the file (but not decrypt it), so nodes need only store this bit. The actual
  public key is stored (unencrypted) with the (encrypted) data.
* **document decryption key** - This is only known to clients and not to the
  nodes storing the data, so nodes cannot decrypt the data they store without
  the full address.
* **crypto settings** - Cryptographic algorithm used, etc.
* **user selected name** - a word or sentence chosen by the site author.
* **version** - the current version of the site.

The version number is increased each time a new version of the site is
created and inserted into Freenet. This approach is used since it is not
currently possible to update already inserted data in Freenet. Updateable
Subspace Keys makes this more transparent to the user, see below.

A typical SSK key looks like this:

    SSK@public key hash,decryption key,crypto settings/user selected name-version

For example (cut for screen purposes):

    SSK@GB3wuHmt[..]o-eHK35w,c63EzO7u[..]3YDduXDs,AQABAAE/mysite-4
""") + "\n\n" + _("""
### How Signed Subspace Keys work

* The author generates a cryptographic keypair: a **private key** for signing
  files and a **public key** for verifying the signature.
* The author also generates a single **symmetric key** (one that is used for
  both encrypting and decrypting).
* When a file is inserted into Freenet, it is encrypted with the **symmetric
  key** and signed with the **private key**. The signature is stored with the
  file. Nodes don't store the **symmetric key**, only the **public key** part of
  the SSK, as an index to the data. This is so they can plausibly deny knowledge
  of the data on their node.

The SSK is made up of a hash of the public key, and the symmetric key. The
hash of the public key acts as the index to the data for searching purposes.
Also, the actual public key is stored with the data. This is so that Freenet
nodes can verify the signature when the SSK file comes into their node,
and also so that clients can verify the signature when retrieving the file.
The symmetric key is so that clients can decrypt the file.

Signed Subspace Key sites have largely been superseded by Updatable Subspace
Key (USK) sites, which are based on SSKs but allow for links that try to
always retrieve the most up-to-date version of the site.
""") + "\n\n" + _("""
### Updateable Subspace Keys

Updateable Subspace Keys are useful for linking to the latest version of a
Signed Subspace Key (SSK) site. Note that USKs are really just a
user-friendly wrapper around SSKs, which hide the process of searching for
more recent versions of a site.

A typical USK key looks like this:

    USK@public key hash,decryption key,crypto settings/user selected name/number/

It is almost identical to the Signed Subspace Key, with the exception of the
version-number. There are two types of USK addresses:

*   an USK with a positive number at the end, or
*   an USK with a negative number at the end.
""") + "\n\n" + _("""
The USK with a **positive** number at the end works like this: the Freenet
node on your computer keeps a list of versions of USKs that it knows about,
without necessarily storing the data as well. This list is built up from
previous visits, and also background requests from previous visits to these
kind of links. When you visit an USK like the one below, it consults this
list for versions of the mysite site of number 5 or greater. If it finds any,
it return the latest one. Then, in the background, it searches for **newer**
versions that it doesn't yet know about to add to your USK registry for the
next time you visit the address.

Example (cut for screen purposes):

    USK@GB3wuHmt[..]o-eHK35w,c63EzO7u[..]3YDduXDs,AQABAAE/mysite/5/
""") + "\n\n" + _("""
When you visit a link with a **negative** number at the end, Freenet searches
for the version you requested (e.g. **-7**) plus four more (i.e. 7,8,9,10,
11) at the node on your computer and on other nodes. If it finds only version
7, it will return that. If it finds one of the others, it searches for
another batch of five versions: 12,13,14,15,16\. It repeats this until there
are four consecutive versions it can't find. Then it will return the latest
version it has found so far.

Example (cut for screen purposes):

    USK@GB3wuHmt[..]o-eHK35w,c63EzO7u[..]3YDduXDs,AQABAAE/mysite/-7/

The real treat with USKs comes when data is to be inserted into Freenet. But
more on that elsewhere.
""") + "\n\n" + _("""
### Keyword Signed Keys

Keyword-Signed Keys (KSKs) allow you to save named pages in Freenet. They are
not secure against spamming or name hijacking. Several people could each
insert a different file to Freenet, all with the same address. However,
there is a collision detection, which tries to prevent overwriting of a
once-inserted page. A KSK address looks like this:

    KSK@myfile.txt

The drawback to KSKs is that anyone can insert a file with the same name as
yours and divert traffic from your file to their own. The advantage is human
readable links that can be easily remembered.

The KSK description should not contain slashes, just as with other keys (
slashes are used to denote Manifests or Containers).

A KSK address can contain a redirection to a CHK address, or it can contain
the file itself.
""") + "\n\n" + _("""
### Containers

A container, in general Freenet terms, is a file that contains several other
files. In freenet 0.7, a freesite, or other collection of files, may be
bundled together in a ZIP file, which is limited in size to 2MB. Containers
have the advantage that when you load one page you load all the files on the
freesite, so either it loads in its entirety or it doesn't load at all,
and greatly reduce the number of keys required to insert a given freesite.
Containers are currently created transparently when inserting a freesite
using e.g. jSite.
""") + "\n\n" + _("""
### Manifests

A manifest contains metadata over the list of blocks a CHK is divided into
and some information about the content-type(MIME), the filenames and other
useful information. The main information is whether the CHK-key is a
splitfile or not, and whether the manifest is chained or not. You don't need
to know much about manifests in order to use Freenet, since it is a part that
is handled internally.
""")))

class FreemailSection(Section):
    def __init__(self):
        self.slug = "freemail"
        self.title = _("Freemail")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
Freemail is an email system for Freenet. It allows you to send anonymous
emails to other Freenet users using your standard email client. It is
currently not bundled in the Freenet installer, and has to be downloaded
separately. You can also try the Freemail plugin by selecting it from the
list on the plugins page of your Freenet node. Beware, though, that the
plugin is still in an early stage of development, and users should be active
about looking in log files and reporting problems if they find them.

You can download the latest pre-compiled version from
[https://downloads.freenetproject.org/alpha/plugins/Freemail/](https://downloads.freenetproject.org/alpha/plugins/Freemail/)
""") + "\n\n" + _("""
### Easy account setup

The easy way to set up a Freemail account is to visit the Freemail plugin,
after you have downloaded it, through your **Plugins** web page. The web
interface will prompt you for an IMAP name, an IMAP password, and a Freemail
shortname to associate with the account. When the account is created, it will
email you the secure name that it generated for you.

The chosen short Freemail-address must be unique and will give you an address
looking like:

*   <anything>@<short-Freemail-address>.freemail

The <anything> before the @ will be ignored. It is only there because mail
user and transport agents want to see an @ in addresses. Yes, we _do_ know
this is an ugly kludge.

Once you have installed the freemail plugin for your Freenet proxy daemon,
starting or restarting the daemon will start the freemail service for you
automatically.

If for some reason you cannot make the web interface work, we have included
hand-configuration instructions down this page.
""") + "\n\n" + _("""
### Mail client setup

Now you have the Freemail proxy running, which means that you can send and
receive emails through Freenet. For this we recommend that you set up your
favorite email client to use the special Freenet private ports:

*   **Incoming emails** - Protocol: **IMAP**, Server: **localhost**, Port: **3143**
*   **Outgoing emails** - Protocol: **SMTP**, Server: **localhost**, Port: **3025**

Your Freemail plugin must be running while you are reading and sending
freemails. Leaving your node running, with the Freemail pugin enabled,
will ensure this. For debugging purposes, it is also possible to send and
receive Freemail mail with only the Freenet jar running.
""") + "\n\n" + _("""
### Fetching Freemail mail with fetchmail

You can easily make [fetchmail](http://fetchmail.berlios.de/) poll your
freenet mail with an entry like this:

<pre>	poll freenet via localhost with proto imap port 3143
	user LOCALNAME here is IMAPNAME there with password PASSWORD</pre>

This will cause Freemail mail to be automatically fetched and merged into
your normal incoming mail stream, so any of your email clients will see it.
Of course, you will need to change IMAPNAME and PASSWORD to match the
authetication pair you gave when you created the Freemail account,
and LOCALNAME to the local login you want to receive the mail.

A variant of this recipe will still work if you have your freenet node.
running on another machine. Just change "localhost" to the DNS address of the
node host.
""") + "\n\n" + _("""
### Thunderbird

If you use Thunderbird as your email client:

1. From the Edit menu, select Account Settings.
2. Click the Add Account... button.
3. Select Email Account and click Next.
4. Type in the name and either the long Freemail address you were given, or
   your short address if you created one. Check this carefully as an incorrect
   address here will not only mean people won't be able to reply to you,
   but your messages will appear as 'Spoofed'. Once you've done this,
   click Next.
5. Set the type of incoming server to IMAP and the incoming server name to
   localhost. Then click Next.
6. For the Incoming User Name, use the account name you chose earlier ('john' in
   this example), which may not be the same as your email address. Click Next.
7. Enter an arbitrary Account Name and click Next and then Finish.
8. Now we have to change the IMAP port number from the default: On the left
   panel click on Server Settings under the new account. Change the Port to
   3143 from the default of 143.

Now you should be able to read incoming freemails. To send out emails:

1. From the Edit menu, select Account Settings.
2. In the left-hand panel, scroll down and click on the Outgoing Server (SMTP)
   option.
3. You probably already have at least one SMTP server set up already for your
   normal emails. So click on the Add... button to create one specially for
   freemails.
4. Under Description put anything you want - Freemail might be a good choice.
   Set Server Name to localhost and change Port to 3025\. Make sure 'Use name
   and password' is checked and put your original account name as the User
   Name ('john' in our example). 'Use secure connection' should be set to No
   (don't worry, it's only the local connection that is unencrypted). Click OK.
5. The final thing is to set your new Freemail account to use this outgoing
   server instead of the default one. So in the left panel find and click on
   the top line of the new incoming mail account you added. In our example
   this would be something like me@jsmith.freemail. There should be a
   drop-down box called Outgoing Server (SMTP). Set this to the new setup we
   just added: something like Freemail - localhost. And click OK.

Congratulations - you're now set up to send and receive email over Freenet!
""") + "\n\n" + _("""
### Hand configuration

To set up an account for Freemail by hand, execute the following commands:

<pre>	java -jar Freemail.jar --newaccount <username>
	java -jar Freemail.jar --passwd <username> <password>
	java -jar Freemail.jar --shortaddress <username> <short-Freemail-address>
	java -jar Freemail.jar</pre>

Exchange the values within <brackets> with the appropriate values.

After running the last command you now have a running Freemail proxy,
listening on localhost at IMAP port 3143 for incoming mails, and SMTP port
3025 for outgoing mails. Connect to it using your favourite email client
software.
""") + "\n\n" + _("""
If you didn't follow, here's a longer and more detailed recipe:

### Account Setup

Change to the directory containing the Freemail.jar file. At the command
line, type:

<pre>	java -jar Freemail.jar</pre>
""") + "\n\n" + _("""
If you are running Freemail for the first time, it will prompt you to create
an account:

<pre>	Starting Freemail for the first time.
	You will probably want to add an account by running Freemail with arguments --newaccount <username></pre>

So do what it says. The username you create here is used to authenticate to
the Freemail-service and will only be seen by you, it isn't part of your
freemail address:

<pre>	java -jar Freemail.jar --newaccount john</pre>

It now generates your Freemail address which is a long random string like
**anything@DS3FG3R...SF6FHJ8YUK.freemail**. Generating the cryptographic
keypair is a computation-intensive process and may take a few minutes on a
slow machine.

<pre>	Generating mailsite keys...
	Mailsite keys generated.
	Your Freemail address is: anything@DS3FG3R...SF6FHJ8YUK.freemail
	Generating cryptographic keypair (this could take a few minutes)...
	Account creation completed.
	Account created for john. You may now set a password with --passwd <password></pre>
""") + "\n\n" + _("""
The next step is to create a password for your account. The syntax to create
a password is shown below:

<pre>	java -jar Freemail.jar --passwd <username> <password></pre>

To create the password **secretpass** for the user **john**, type:

<pre>	java -jar Freemail.jar --passwd john secretpass</pre>

Now we have an account, a password for that account and a rather lengthy
Freemail-address. The problem is that not many people in the world will be
able to remember that Freemail-address. The solution to this problem is to
create a short address that points to the long one:

To do this, run the main command again:

<pre>	java -jar Freemail.jar</pre>

and the software will prompt you to create a short Freemail address:

<pre>	Secure Freemail address: anything@DS3FG3R...SF6FHJ8YUK.freemail
	You don't have a short Freemail address. You could get one by running Freemail
	with the --shortaddress option, followed by your account name and the name
	you'd like. For example, 'java -jar freemail.jar --shortaddress bob bob' will give
	you the address 'anything@bob.freemail'. Try to pick something unique!
	trying slotinsert to freenet:SSK@sdfgsdfg...ertretert/mailsite-1/mailpage</pre>
""") + "\n\n" + _("""
The syntax to create a short freemail address is:

<pre>	java -jar Freemail.jar --shortaddress <username> <short address></pre>

To create an alias known as **jsmith** for user **john**, write:

<pre>	java -jar Freemail.jar --shortaddress john jsmith</pre>

If that short alias is free, it will tell you your Freemail address:

<pre>	Secure Freemail address: anything@DS3FG3R...SF6FHJ8YUK.freemail
	Short Freemail address (*probably* secure): anything@jsmith.freemail</pre>

Now you have created a Freemail account, a long and a short address and set
up a password for the account. Now, all you need to do is to start the
Freemail proxy, to listen for incoming IMAP and SMTP connections. The
Freemail proxy must run while you use Freemail, or else no mails you send
will get delivered. To start the server, run the command:

<pre>	java -jar Freemail.jar</pre>
""") + "\n\n" + _("""
### Troubleshooting tips

If you try to run the Freemail jar and get messages that look like the following:

<pre>	24/12/2008 11:20:52 ERROR(freemail.smtp.SMTPListener): Error in SMTP server - Address already in use
	24/12/2008 11:20:52 ERROR(freemail.imap.IMAPListener): Error in IMAP server - Address already in use</pre>

...it probably means you downloaded the Freemail plugin through the Web
interface and your node is already running it. On a GNU/Linux machine you can
check to see if the private SMTP and IMAP ports are actually in use with
`netstat -tln`; the port numbers you're looking for in the listing are 3143 (
Freenet IMAP) and 3025 (Freenet SMTP).

If you get these messages and these ports are _not_ in use, try shutting down
and restarting the node. If the problem persists after that, you have found a
bug and should file it with the Freenet developers.

If the ports are indeed in use, check the **List of Plugins** on your
**Plugins**. If Freemail is in that list, then you can eaither unload it and
go through the manual procedure (running java -jar Freemail.jar) or configure
your Freemail account through the web interface.
""")))

class FrostSection(Section):
    def __init__(self):
        self.slug = "frost"
        self.title = _("Frost")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
Frost is an application for Freenet that provides usenet-like message boards
and file uploading/downloading/sharing functionalities. It should get
installed with Freenet 0.7 automatically if you used the standard Freenet
installers.

To run Frost on GNU/Linux or POSIX from the command line, change to your
Freenet install directory, then change to the frost subdirectory. Then make
the frost.sh file executable, and run it:

<pre>	cd /home/username/
	cd frost/
	chmod +x ./frost.sh
	./frost.sh</pre>
""") + "\n\n" + _("""
The first time you start Frost, you will get a number of dialogs. The first
ask you if you would like to import old Frost data. If this is the first time
you use Freenet at all, you can safely answer **Clean startup** here.

![](assets/img/frost/clean-start.png)

Since Freenet is able to run on both Freenet 0.5 and the current Freenet 0.7,
you will need to specify which version you want to run with. If you have
followed the previous install instructions, you will probably want **Freenet
0.7 (Darknet)**.

![](assets/img/frost/select-version.png)

Next step is to choose which identidy you want to be known by when using
Frost. As it says, it does not have to be unique, but it certainly helps.

![](assets/img/frost/choose-identity.png)

You will then get the main Frost window, where one can participate in the
message boards and up/download files. The windows will probably take a while
to populate on the first startup.

![](assets/img/frost/main-window.png)
""") + "\n\n" + _("""
### Sharing files

Sharing files can be done by clicking the **Shared files** -tab and then
clicking on the Folder-icon top left in the appearing tab.
""") + "\n\n" + _("""
### Further information

Additional information about Frost can be found in the mailing-list or on the
official website: [Frost Homepage](http://jtcfrost.sourceforge.net/)
""")))

class JSiteSection(Section):
    def __init__(self):
        self.slug = "jsite"
        self.title = _("jSite")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
jSite is a graphical application that you can use to create, insert and
manage your own Freenet sites. It was written in Java by Bombe.

You can [download jSite here](https://downloads.freenetproject.org/alpha/jSite/jSite.jar)
""") + "\n\n" + _("""
### Starting jSite

To start jSite, type the following in a terminal:

<pre>	java -jar jSite.jar</pre>

The first window you see is this:

![](assets/img/jsite/select-project.png)

In the pane to the left, already created projects can be selected for
updating, deleting or cloning. Since this is the first start, no such
projects exist.
""") + "\n\n" + _("""
### Creating a Freesite

To create a new Freesite, you click the **Add project**-button. You then need
to fill in the details of the project. Under the Project information-section:

* **Name** - this is just a name for you to know the project, so anything will
  do. It may contain spaces.
* **Description** - again, just a slightly longer description of the project for
  your own convenience.
* **Local Path** - This is a directory where you will store all the pages of the
  freesite you are creating. Put in the full path. You can click the Browse
  button to select a directory graphically or just type it in.
""") + "\n\n" + _("""
Under the Address-section, there are some automatically generated entries,
and the human readable name for the site, as seen in the address-field of the
browser:

* **Request URI** - this is filled in automatically and should be a long string
  of seemingly random characters
* **Insert URI** - this is also filled in automatically and will look similar to
  the Request URI..
* **Path** - You need to enter a single word here without spaces. This will
  appear at the end of the address of your site. You can't leave this blank.

Below is an example of how it might look:

![](assets/img/jsite/project-details.png)

When everything is filled in correctly, you may press **Next**.
""") + "\n\n" + _("""
The next step is to add files to your Freenet site (or Freesite). This is
done in the dialog called **Project Files**. Since we have no files in the
current directory, yet, the dialog is pretty much empty.

![](assets/img/jsite/project-files.png)

To add files, we put some files in the local directory we specified earlier,
**/home/test**, and press **Re-scan**. Then, presto, the files appear.

![](assets/img/jsite/default-file.png)

We then highlight one of these files that will be the default page (e.g.
index.html might be a good choice) and check the **Default file** checkbox.
It should recognise the MIME type as text/html, so leave everything else as
they are and click the **Insert now** button.
""") + "\n\n" + _("""
If all goes well, a window like the one below should appear. It may take
quite a while to insert the Freesite, several minutes in fact.

![](assets/img/jsite/project-insert.png)

When all is finished, you will get a message pop-up that tells you that the
site has been inserted successfully. You can copy the URI to the clip-board
by clicking the **Copy URI to Clipboard** -button.
""") + "\n\n" + _("""
Then you can use FProxy to surf to your newly created Freesite. Just paste
the URI after the

[http://localhost:8888/](http://localhost:8888/)

in the browser address bar, like this (cut for screen purposes):

<pre>	http://localhost:8888/freenet:USK@cJNO6G0[..]joM,AQACAAE/watergate2/1/</pre>

If it works, congratulations, you have just created your first Freesite!
""")))

class WikiSection(Section):
    def __init__(self):
        self.slug = "wiki"
        self.title = _("Wiki")
        self.direct_link = "https://wiki.freenetproject.org/"

class DocumentationPage(Page):
    def __init__(self):
        self.slug = "documentation"
        self.title = _("Documentation")
        self.sections = [
            DocumentationIntroSection(),
            InstallSection(),
            ConnectSection(),
            ContentSection(),
            UnderstandSection(),
            FreemailSection(),
            FrostSection(),
            JSiteSection(),
            WikiSection()
            ]
