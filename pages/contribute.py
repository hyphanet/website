# -*- coding: utf-8 -*-
# Python code copyright Gerard Krol, license: MIT
from common import *

class DevelopersSection(Section):
    def __init__(self):
        self.slug = "developers"
        self.title = _("Developers")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
We are using [git](http://git-scm.com/) as our source code management system, hosted on [github](https://github.com/). We have many different git repositories for the website, freenet itself (fred), official plugins, the two installers, libraries and so on; for the list, see [our page on github](https://github.com/freenet/).

We strongly recommend that you use the official command-line git client, or the Windows port. If you want to use the Eclipse git integration, see the tutorial [here](http://wiki.eclipse.org/EGit/User_Guide).

You can obtain the latest source code from git using the following command line:

<pre>	git clone git://github.com/freenet/fred.git</pre>

Once you have cloned the repository, to get new changes you should do:

<pre>	git pull origin</pre>

More information on how to use git is further down this page.

Git is a distributed revision control system, this means amongst other things:

*   Everyone has a full copy of the repository, including all the history.
*   Branching and merging is easy.
*   Working offline (e.g. on a train) is easy.
*   We are much less vulnerable to compromise or failure of a central server.
*   Anonymous contribution over Freenet is much easier.
*   Generally a more secure workflow.

Initially we used git in a manner similar to SVN: Every developer has the right to push to the repository, and we gave out push rights fairly liberally. However, this is probably not the best model: Many other projects using Git use a more centralised (or decentralised, depending on how you look at it) model where you fork the repository (this is really easy on github), make your changes, push them to your repository, and then ask us to pull them; then a core developer reviews the changes and either pulls them into the main repository or asks for further changes. The advantage is there are fewer reverts in the history, better code in general, stuff can be put off more easily when we are trying to get a release out, and the security model is simpler. We are trying to mode to this model at the moment. You may find it is easier to fork -staging and then post a pull request (github makes both of these things easy), rather than asking for push rights to -staging.

Each part of Freenet currently has two repositories: -official and -staging (e.g. fred-official and fred-staging). This is left over from our using git similarly to SVN: The -official repository has been reviewed and released at least as a pre-build, and only core devs can push to it - they must review the code they are pushing before doing so, and will usually sign a tag for the build or pre-build after doing so. The -staging repository almost anyone can write to. New developers should fork on github and then post pull requests.

### Branches

The "master" branch tracks the latest release. The "next" branch includes code that should be in the next release, but may or may not be at the discretion of the release manager. Any significant feature should have its own branch. Release branches e.g. "stable-1411" are used by the release manager from time to time.

### Build Instructions

To build the source code you will need [Apache ANT](http://ant.apache.org/).

### Full Build

Building Fred (the Freenet reference daemon) with ant will pull in freenet-ext.jar for third party dependancies from the website. To build freenet-ext.jar yourself you need to get the contrib module, build it, and put it into lib/freenet-ext.jar before you build the main project. Note also that the contrib module contains a number of native libraries used to improve performance; you may also want to rebuild these.

Plugins, installers etc can generally be built with ant, but some libraries may be written in other languages and have their own building procedures.

### Basic git workflow

To pull all changes to the repository:

<pre>	git pull origin</pre>

Or if you want to review the changes before you merge them into your local repository:

<pre>	git fetch origin
	git log -p -M --ignore-space-change master..origin/master</pre>

If you are happy with the changes, then either merge your local changes into the remote changes:

<pre>	git rebase origin/master</pre>

Or merge the remote changes into your local repository:

<pre>	git merge origin/master</pre>

The latter will result in a non-linear history, so you should use rebase unless your local changes are very large.

To commit your local changes to your local repository:

<pre>	git commit -a</pre>

Or:

<pre>	git commit [ filenames you want to commit ]</pre>

To upload your changes:

<pre>	git push origin</pre>

To view recent changes:

<pre>	git log -p -M --ignore-space-change</pre>

To undo one or more local commits, assuming you have not pushed your changes, and have not merged remote changes (this will simply reset your local repository to a previous version, getting rid of everything since then):

<pre>	git reset [ last good revision ]</pre>

Or if you have committed your change, you will need to revert it:

<pre>	git revert [ revision to get rid of ]</pre>

More documentation for git can be found [here](http://git-scm.com/documentation) or [here](http://www.kernel.org/pub/software/scm/git/docs/).

### Review

If you don't like a commit, or think it could be improved, generally you should post to the devl [mailing list](help.html#mailing-lists). You should CC the author of the commit, but unless it is a trivial matter you should always mail devl.

### Development guidelines

Please keep us informed of what you are doing with Freenet! Create a github account, and then contact us either through the [development mailing list](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/devl) or on [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) in the [#freenet](irc://irc.freenode.net/%23freenet) channel at irc.freenode.net. Note that it is very useful to be able to contact contributors, so you should use a real (working) email address (we will provide an @freenetproject.org redirect if you need one), or see the section on contributing through Freenet below.

Project coding standards are documented [here](https://wiki.freenetproject.org/Coding_standards). Commits which do not follow these standards are likely to be rejected.

We strongly discourage "dropping a bomb", that is, sending in a huge patch with no history. This can be both harder to understand and risky legally (think SCO vs IBM). For large projects, you should post a git branch, on github or on Freenet, so we can merge and keep the history. Of course you can clean up the history before posting a pull request if you want. What is more important is to let us know early on so we can help you to get it right.

All releases are reviewed manually both to ensure security and to avoid bugs, and this is much easier if you follow some basic rules:

*   Keep cosmetic changes separate from functional changes. In particular, indenting and braces improvements, while these are generally acceptable, should **not** be mixed with functional changes.
*   Don't break the build: When you push, fred should build. Ideally each individual commit should build.
*   Small commits: "git commit" is a purely local operation, so there is no reason to combine a bunch of unrelated changes in a single commit. Obviously use your judgement.
*   Big or controversial stuff should go on a branch, rather than just getting pushed. We may be in the process of getting a new build out, and if big stuff is pushed it is likely to be shifted to a branch while the build is deployed.

### Development over Freenet

We accept patches submitted over Freenet via FMS. However, we will still need some sort of identity, e.g. a nick and a Freemail (v2) address. There are implementations of both Git and Mercurial (which can be bridged to git) over Freenet, although we don't currently maintain an official in-freenet tree.

### The website

To edit the website, fork the website repository, edit the files (in pages/en/), commit and push as above. Then post a pull request and remind administrators to deploy it if isn't done in reasonable time.

The website is php-based but is compiled at deploy time into static HTML. You can simulate this to see exactly what your changes will look like by running the make-pages.sh script (you will need php5-cgi). This outputs static HTML to output/.

We are trying to move most of the documentation to [the wiki](https://wiki.freenetproject.org), which should be easier to edit.
""")))

class TranslationSection(Section):
    def __init__(self):
        self.title = _("Translation")
        self.direct_link = "https://wiki.freenetproject.org/Translation"

class BugTrackerSection(Section):
    def __init__(self):
        self.title = _("Bug tracker")
        self.direct_link = "https://bugs.freenetproject.org/"

class ContributePage(Page):
    def __init__(self):
        self.slug = "contribute"
        self.title = _("Contribute")
        self.first_section_in_menu = True
        self.sections = [
            DevelopersSection(),
            TranslationSection(),
            BugTrackerSection(),
            ]
