# -*- coding: utf-8 -*-
# Python code copyright Gerard Krol, license: MIT
from .common import *

class MailingListSection(Section):
    def __init__(self):
        self.slug = "mailing-lists"
        self.title = _("Mailing lists")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
These are the mailing lists that can be used for support or general
information about Freenet.
""") + "\n\n" + _("""
### Subscribing

To subscribe to one of the lists, click the list name and give your email
address in the field below the **Subscribing to < mailinglist >** header. To
enter a password is optional, and if you do not enter one, one will be
automatically generated for you. Then press the **Subscribe** button. You
will receive a confirmation email, and when that is answered, you will
receive mails from the list.
""") + "\n\n" + _("""
### Unsubscribing

To unsubscribe to one of the lists you are subscribed to, click the list name
and give your subscription email address under the heading **< mailinglist >
Subscribers** and press the button **Unsubscribe or edit options**.

_**Note**: We constantly get requests of people who want to become
unsubscribed._ **YOU** _have to do that yourself! Just click on the www link
provided at the bottom of every mail, enter your e-mail address in the text
field in section "Subscribers" and provide your password under the
unsubscribe option. (You can get your password there as well, in case you
forgot it.)_
""") + "\n\n" + _("""
### The lists

* [Support](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/support/) ([archive](https://emu.freenetproject.org/pipermail/support/))<br/>
  Asking for or giving advice relating to getting Freenet working,
  bug reports, and suggestions on improving the user experience. Requests for
  help are more likely to be heard here than in the other mailing lists.
  **Note:** Emails sent to this mailing list from those not subscribed to the
  list must be manually approved, and this can impose a delay of several days.
  To avoid this delay, please [subscribe](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/support/).
* [Development](https://emu.freenetproject.org/cgi-bin/mailman/listinfo/devl/) ([archive](https://emu.freenetproject.org/pipermail/devl/))<br/>
  This list is for active developers to discuss bugs, and the implementation
  of near-term new features.

_**Third party tools**: We are hosting some other mailing lists on our server
here is the [full list][url_listinfo]._
""") + "\n\n" + """
[url_listinfo]: https://emu.freenetproject.org/cgi-bin/mailman/listinfo/
"""))

class SuggestionsSection(Section):
    def __init__(self):
        self.title = _("Suggestions")
        self.direct_link = "https://freenet.uservoice.com/"

class SupportSection(Section):
    def __init__(self):
        self.slug = "support"
        self.title = _("Get Support")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
If you need help installing Freenet for the first time, or have trouble using Freenet and can't find an answer to your problem in the [FAQ][faq_link] or in the [Knowledge Base][kb_link], please create a new discussion on our support forum.

When writing your support request, please make sure you include a full description of the problem, your current version of Java, your operating system and current Freenet version.
""") + "\n\n" + """
[faq_link]: https://wiki.freenetproject.org/FAQ
[kb_link]: https://freenetproject.tenderapp.com/kb
"""  + "\n\n" + """
<a href="https://freenetproject.tenderapp.com/discussion/new" id="supportlink" class="btn button-custom btn-custom-two">{}</a>
""".format(_("Create a support discussion"))))

class ChatSection(Section):
    def __init__(self):
        self.slug = "irc"
        self.title = _("Chat with us")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
Many of the developers and users of Freenet are on the [IRC](
https://en.wikipedia.org/wiki/IRC) channel #freenet on chat.freenode.net.
""") + "\n\n" + """
<a href="#chatlink" id="chatlink" class="btn button-custom btn-custom-two">{}</a>
""".format(_("Chat with us"))))

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
            SupportSection(),
            MailingListSection(),
            SuggestionsSection(),
            ChatSection(),
            SetupSection(),
            ]
