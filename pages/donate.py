# -*- coding: utf-8 -*-
# Python code copyright Gerard Krol, license: MIT
from .common import *

class DonateSection(Section):
    def __init__(self):
        self.slug = "donate"
        self.title = _("Donate")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        donate_email = """<span class="e-mail" data-user="etanod" data-website="gro.tcejorpteneerf"></span>"""
        bitcoin_address = "1966U1pjj15tLxPXZ19U48c99EJDkdXeqb"
        return text(md(_("""
#### Financial Status

The project's current balance is **$MONEYBALANCE**. (updated twice a day)
This will pay for the project's one paid developer (we have many volunteers) and
the server for roughly another **MONEYMONTHS months** (MONEYDAYS days).
""") + "\n\n" + _("""
#### Why does The Freenet Project need donations?

Although countless people have given their time and skill to the project since
its inception, The Freenet Project relies on your donations both to support
those developers working full-time on this increasingly complex project, and to
cover hardware (this server) and administrative costs (i.e. domain
registrations and certificates). We would also like to start a legal defense
fund should the need arise.

Everyone involved is keenly interested in the future of The Freenet Project and
you can be assured donations have been and will continue to be used wisely. All
support is very much appreciated.
""") + "\n\n" + _("""
#### How can I donate?

You have several options:

* You can become a Freenet project "member" for a **recurring payment** of $5 or
more per month. The advantage of this is that it gives the project a more stable
and dependable income which makes it easier to make long term commitments to
potential developers - right now it is often difficult to say whether we will be
able to pay a developer the following month although so-far we have been
fortunate. You can become a member by clicking on this button (you will need a
[PayPal][url_paypal] account):
""") + "\n\n" + """
[url_paypal]: https://www.paypal.com/
""") + """
	  <center>
	    <table>
	      <tbody><tr>
		<td style="{padding:4px; border:1px solid silver}">
		  <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
		    <input type="hidden" name="cmd" value="_xclick-subscriptions">
		    <input type="hidden" name="business" value="ian@freenetproject.org">
		    <input type="hidden" name="item_name" value="Freenet Project Membership">
		    <input type="hidden" name="return" value="https://freenetproject.org/donatethanks.html">
		    <input type="hidden" name="cancel_return" value="https://freenetproject.org/donate.html">
		    <input type="hidden" name="no_shipping" value="1">
		    <input type="hidden" name="no_note" value="1">
		    <input type="hidden" name="currency_code" value="USD">
		    Amount:
		    <p>
		      $50 <input type="radio" name="a3" value="50.00"><span style="{border:1px solid black}">&nbsp;$20 <input type="radio" name="a3" value="20.00"></span>&nbsp; <span style="{border:1px solid black}">&nbsp;$10 <input type="radio" name="a3" checked="checked" value="10.00"></span>&nbsp; <span style="{border:1px solid black}">&nbsp;$5 <input type="radio" name="a3" value="5.00"></span>&nbsp;
		    </p>
		    <input type="image" src="https://www.paypal.com/images/x-click-but20.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
		    <input type="hidden" name="p3" value="1">
		    <input type="hidden" name="t3" value="M">
		    <input type="hidden" name="src" value="1">
		    <input type="hidden" name="sra" value="1">
		  </form>
		</td>
	      </tr>
	    </tbody></table>

		  <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
	  <p>Or set your own amount:
		    <input type="hidden" name="cmd" value="_xclick-subscriptions">
		    <input type="hidden" name="business" value="ian@freenetproject.org">
		    <input type="hidden" name="item_name" value="Freenet Project Membership">
		    <input type="hidden" name="return" value="https://freenetproject.org/donatethanks.html">
		    <input type="hidden" name="cancel_return" value="https://freenetproject.org/donate.html">
		    <input type="hidden" name="no_shipping" value="1">
		    <input type="hidden" name="no_note" value="1">
		    <input type="hidden" name="currency_code" value="USD">
		    <!-- We need javascript to disable the submission button until a value is set. For now just set a default. -->
		    <input type="text" name="a3" value="10.00" style="color:black">
		    <input type="image" src="https://www.paypal.com/images/x-click-but20.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
		    <input type="hidden" name="p3" value="1">
		    <input type="hidden" name="t3" value="M">
		    <input type="hidden" name="src" value="1">
		    <input type="hidden" name="sra" value="1">
		    </p>
		  </form>
	  </center>
    <hr width="90%">
	"""+md(_("* You can *donate once* via Paypal by clicking on this button:"))+"""<br>
	    <center>
	      <table cellpadding="5" cellspacing="0" width="1%">
		<tbody><tr>
		  <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
		    <input type="hidden" name="cmd" value="_xclick">
		    <input type="hidden" name="business" value="ian@freenetproject.org">
		    <input type="hidden" name="item_name" value="Freenet Donation">
		    <input type="hidden" name="no_shipping" value="1">
		    <input type="hidden" name="return" value="https://freenetproject.org/donatethanks.html">
		    <input type="hidden" name="cancel_return" value="https://freenetproject.org/donate.html">
		    <input type="hidden" name="currency_code" value="USD">
		    <td>
		      <select name="amount" style="background-color: gray;">
			<option value="500.00">$500.00</option>
			<option value="100.00">$100.00</option>
			<option value="50.00">$50.00</option>
			<option value="20.00">$20.00</option>
			<option selected="" value="10.00">$10.00</option>
			<option value="5.00">$5.00</option>
		      </select>
		    </td>
		    <td>
		      <input type="image" src="assets/img/paypal-submit.gif" border="0" name="submit">
		    </td>
		  </form>
		</tr>
		<tr>
		  <td>"""+md(_("Other amount:"))+""" $</td>
		  <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
		    <input type="hidden" name="cmd" value="_xclick">
		    <input type="hidden" name="business" value="ian@freenetproject.org">
		    <input type="hidden" name="item_name" value="Freenet Donation">
		    <input type="hidden" name="no_shipping" value="1">
		    <input type="hidden" name="return" value="https://freenetproject.org/donatethanks.html">
		    <input type="hidden" name="cancel_return" value="https://freenetproject.org/donate.html">
		    <input type="hidden" name="currency_code" value="USD">
		    <td>
		      <input type="text" name="amount" style="color:black">
		    </td>
		    <td>
		      <input type="image" src="assets/img/paypal-submit.gif" border="0" name="submit">
		    </td>
		  </form>
		</tr>
	      </tbody></table>
	    </center>
"""+md("* * *" + "\n\n" + _("""
![][logo_bitcoin] You can now donate to the Freenet Project using [bitcoin][url_bitcoin].  

Send your donations to the account: {bitcoin_address}
""").format(bitcoin_address=bitcoin_address) + "\n\n" + "* * *" + "\n\n" + _("""
Alternatively, please contact us: {donate_email} if you cannot use
any of these payment methods.

You can also donate to the project by purchasing items from the Freenet
[store][url_zazzle_store].
""").format(donate_email=donate_email) + "\n\n" + _("""
## How can I be sure that my donation will be used appropriately?

All donations go to The Freenet Project Inc, a non-profit 501c3 corporation with
the following mission statement:

> The specific purpose of this corporation is to assist in developing and
> disseminating technological solutions to further the open and democratic
> distribution of information over the Internet or its successor electronic
> communication networks or organizations. It is also the purpose of this
> organization to guarantee consenting individuals the free, unmediated,
> and unimpeded reception and impartation of all intellectual, scientific,
> literary, social, artistic, creative, human rights, and cultural
> expressions, opinions and ideas without interference or limitation by or
> service to state, private, or special interests. It is also the purpose of
> this organization to educate the world community and be an advocate of
> these purposes.

All funds received will only be utilized to advance our Mission Statement, and
are administered at the direction of the Freenet Project Board.
""") + "\n\n" + """
[url_bitcoin]: http://www.bitcoin.org/
[logo_bitcoin]: assets/img/BC_nBG_48px.png
[url_zazzle_store]: http://www.zazzle.com/freenetproject
"""))

class SponsorsSection(Section):
    def __init__(self):
        self.slug = "Sponsors"
        self.title = _("Sponsors")
    def get_content(self):
        donate_email = """<span class="e-mail" data-user="etanod" data-website="gro.tcejorpteneerf"></span>"""
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
The following persons, organisations and companies have generously sponsored
this project through donations or discounts on hardware and services:
""") + "\n\n" + _("""
*   [John Pozadzides][url_john_pozadzides]  
John is the founder of HTMLHelp.com and former Vice President of Sales for SAVVIS Communications.
John has donated $10,000 to the Freenet Project to fund ongoing development of the Freenet software.
""") + "\n" + _("""
*   [Web Hosting Search][url_web_hosting_search]  
WebHostingSearch is a top rated guide to various world wide web hosting companies.
Mr Chris Reynolds and the friendly team behind this company have become one of our proud promoters.
""") + "\n" + _("""
*   [John Gilmore][url_john_gilmore]  
John Gilmore is one of the founders of the Electronic Frontier Foundation, the Cypherpunks mailing list, and Cygnus Solutions.
He created the alt.* hierarchy in Usenet and is a major contributor to the GNU project.
He has donated $10,000.
""") + "\n" + _("""
*   [Bytemark Hosting][url_bytemark_hosting]  
Bytemark provides discounted hosting facilities to Freenet and comes with our highest recommendation.
""") + "\n" + _("""
*   [zoozle Torrent Search][url_zoozle]  
zoozle is a search engine for BitTorrent and P2P networks.
It is also available in [german][url_zoozle_german] and [french][url_zoozle_french].
They have donated $1,500.
""") + "\n" + _("""
*   [YourKit, LLC][url_yourkit]  
YourKit is kindly supporting Freenet by providing us a free of charge license of its full-featured Java Profiler.
YourKit, LLC is the creator of innovative and intelligent tools for profiling Java applications.
You can learn more about [YourKit Java Profiler][url_yourkit_profiler] following the link.
""") + "\n" + _("""
*   [Google][url_google]  
Google [open source][url_google_opensource] have three times donated $18,000, as well as paying for students to work with us over summer since 2006 through the [Google Summer of Code][url_google_soc] program.
""") + "\n" + _("""
*   [Finanzvergleich][url_finanzvergleich]  
Finanzvergleich is a German financial services comparison site, who have contributed $1,500.
""") + "\n" + _("""
*   [TopDir][url_topdir]  
TopDir is a human edited web directory with informations about interesting topics and websites in the German language.
""") + "\n" + _("""
*   [All Filters][url_allfilters] - another generous sponsor.
""") + "\n" + _("""
*   [A German Site for Gardening and Plants][url_gartenheinz] - another generous sponsor.
""") + "\n" + _("""
*   [Simple Car Rentals][url_simple_carrentals]  
Simple Car Rentals has generously supported Freenet by helping us with some of our administrative expenses over the years.
""") + "\n" + _("""
*   [The Sports Den][url_sportsden]  
The Sports Den has a wide variety of outdoor sports equipment, they are based in Ireland but can ship to the UK, Europe, and the United States.
""") + "\n" + _("""
*   ![][logo_intellij_idea]  
[JetBrains][url_jetbrains] has kindly provided a license for the Ultimate edition of [IntelliJ IDEA][url_intellij_idea].
""") + "\n\n" + _("""
Freenet Project Inc does not necessarily endorse the business activities of all of the companies listed on this page.

Donation inquiries please contact Ian Clarke: {donate_email}
""").format(donate_email=donate_email) + "\n\n" + """
[url_john_pozadzides]: http://onemansblog.com/
[url_web_hosting_search]: http://www.webhostingsearch.com/
[url_john_gilmore]: http://www.toad.com/gnu/
[url_bytemark_hosting]: http://bytemark.co.uk/
[url_zoozle]: http://www.zoozle.org/
[url_zoozle_german]: http://www.zoozle.net/ "deutsche Torrent Suchmaschine"
[url_zoozle_french]: http://www.zoozle.biz/ "le moteur français de recherche pour BitTorrent"
[url_yourkit]: http://www.yourkit.com/
[url_yourkit_profiler]: http://www.yourkit.com/java/profiler/index.jsp
[url_google]: http://www.google.com/
[url_google_opensource]: http://code.google.com/
[url_google_soc]: http://code.google.com/soc/
[url_finanzvergleich]: http://www.finanzvergleich.de
[url_topdir]: http://www.topdir.de "Top Directory"
[url_allfilters]: http://www.allfilters.com/
[url_gartenheinz]: http://www.gartenheinz.de
[url_simple_carrentals]: http://www.simple-carrentals.com/
[url_sportsden]: http://www.sportsden.ie/
[logo_intellij_idea]: assets/img/logo_intellij_idea.png
[url_jetbrains]: https://www.jetbrains.com
[url_intellij_idea]: https://www.jetbrains.com/idea
"""))

class StoreSection(Section):
    def __init__(self):
        self.title = _("Store")
        self.direct_link = "http://www.zazzle.com/freenetproject"

class DonatePage(Page):
    def __init__(self):
        self.slug = "donate"
        self.title = _("Donate")
        self.sections = [
            DonateSection(),
            SponsorsSection(),
            StoreSection(),
            ]

class DonateThanksSection(Section):
    def __init__(self):
        self.slug = "thanks"
        self.title = _("Thanks for your donation!")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        donate_email = """<span class="e-mail" data-user="etanod" data-website="gro.tcejorpteneerf"></span>"""
        return text(md(_("""
We have received your generous donation. It will be used at the direction of
the Freenet Board to advance the interests of the Freenet Project. If you
have any questions about how your donation will be used please contact Ian
Clarke: {donate_email}.
""").format(donate_email=donate_email)))
            
class DonateThanksPage(Page):
    def __init__(self):
        self.slug = "donatethanks"
        self.title = _("Thanks")
        self.hidden = True
        self.sections = [
            DonateThanksSection(),
            ]
