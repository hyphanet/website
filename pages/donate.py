# -*- coding: utf-8 -*-
# Copy this file to quickly add a new page
# License: GFDL
from common import *

class DonateSection(Section):
    def __init__(self):
        self.slug = "donate"
        self.title = _("Donate")
    def get_content(self):
        return text("""
      <h4>Why does The Freenet Project need donations?</h4>
      <p>
	Although countless people have given their time and skill to the project since its
	inception, The Freenet Project relies on your donations both to support those developers
	working full-time on this increasingly complex project, and to cover hardware (this server)
	and administrative costs (i.e. domain registrations). We would
	also like to start a legal defense fund should the need arise. </p><p> Everyone involved is keenly interested in the
	future of The Freenet Project and you can be assured donations have been and will continue
	to be used wisely. All support is very much appreciated.</p>
      
      <h4>How can I donate?</h4>
      You have several options:
      <ul>
	<li>You can become a Freenet project "member" for
	  a <b>recurring payment</b> of $5 or more per month.  The advantage of this is that 
	  it gives the
	  project a more stable and dependable income which makes it easier
	  to make long term committments to potential developers - right now
	  it is often difficult to say whether we will be able to pay a developer
	  the following month although so-far we have been fortunate.  You
	  can become a member by clicking on this button (you will need a
	  
	  <a rel="nofollow" href="https://www.paypal.com/">PayPal</a> account):
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
	  </center>
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
		    <input type="text" name="a3" value="10.00">
		    <input type="image" src="https://www.paypal.com/images/x-click-but20.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
		    <input type="hidden" name="p3" value="1">
		    <input type="hidden" name="t3" value="M">
		    <input type="hidden" name="src" value="1">
		    <input type="hidden" name="sra" value="1">
		    </p>
		  </form>
		  	  <hr width="90%">
	</li><li>You can <b>donate once</b> via Paypal by clicking on this button:<br>
	    <center>
	      <table cellpadding="5" cellspacing="0" width="1%">
		<tbody><tr>
		  <form action="https://www.paypal.com/cgi-bin/webscr" method="post"></form>
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
		  
		</tr>
		<tr>
		  <td>Other amount: $</td>
		  <form action="https://www.paypal.com/cgi-bin/webscr" method="post"></form>
		    <input type="hidden" name="cmd" value="_xclick">
		    <input type="hidden" name="business" value="ian@freenetproject.org">
		    <input type="hidden" name="item_name" value="Freenet Donation">
		    <input type="hidden" name="no_shipping" value="1">
		    <input type="hidden" name="return" value="https://freenetproject.org/donatethanks.html">
		    <input type="hidden" name="cancel_return" value="https://freenetproject.org/donate.html">
		    <input type="hidden" name="currency_code" value="USD">
		    <td>
		      <input type="text" name="amount">
		    </td>
		    <td>
		      <input type="image" src="assets/img/paypal-submit.gif" border="0" name="submit">
		    </td>
		  
		</tr>
	      </tbody></table>
	    </center>
	    <p>
	      </p><hr width="90%">
	    <p></p>
	    </li><li><img src="assets/img/BC_nBG_48px.png" width="126" height="48">
	    You can now donate to the Freenet Project using <a rel="nofollow" href="http://www.bitcoin.org/">bitcoin</a>.<br>
	    <div>Send your donations to the account: 1966U1pjj15tLxPXZ19U48c99EJDkdXeqb<br></div>
	    
	    <hr width="90%">
	    </li><li>Alternatively, please contact us: <span class="e-mail" data-user="etanod" data-website="gro.tcejorpteneerf"></span>
	      if you cannot use any of these payment methods.</li>
	    <li>You can also donate to the project by purchasing items from the 
	      Freenet <a rel="nofollow" href="http://www.zazzle.com/freenetproject">store</a>.</li>
	  </ul>
	  <h4>How can I be sure that my donation will be used appropriately?</h4>
	  <p>
	    All donations go to The  
	    Freenet Project Inc, a 
	    non-profit 501c3 corporation with the following 
	    mission  
	    statement:
	    </p><blockquote>
	      The specific purpose of this corporation is to assist in developing and 
	      disseminating technological solutions to further the open and democratic 
	      distribution of information over the Internet or its successor 
	      electronic communication networks or organizations. It is also the 
	      purpose of this organization to guarantee consenting individuals the 
	      free, unmediated, and unimpeded reception and impartation of all 
	      intellectual, scientific, literary, social, artistic, creative, human 
	      rights, and cultural expressions, opinions and ideas without 
	      interference or limitation by or service to state, private, or special 
	      interests. It is also the purpose of this organization to educate the 
	      world community and be an advocate of these purposes.
	    </blockquote>
	    All monies received will only be utilized to advance our 
	    Mission 
	    Statement, and are 
	    administered at the direction of the 
	    Freenet Project Board.
	  <p></p>
""")

class SponsorsSection(Section):
    def __init__(self):
        self.slug = "Sponsors"
        self.title = _("Sponsors")
    def get_content(self):
        return text(md(_("""
The following persons, organisations and companies have generously sponsored this project through donations or discounts on hardware and services:

*   [John Pozadzides](http://onemansblog.com/)  
     John is the founder of HTMLHelp.com and former Vice President of Sales for SAVVIS Communications. John has donated $10,000 to the Freenet Project to fund ongoing development of the Freenet software.
*   [Web Hosting Search](http://www.webhostingsearch.com/)  
     WebHostingSearch is a top rated guide to various world wide web hosting companies. Mr Chris Reynolds and the friendly team behind this company have become one of our proud promoters.
*   [John Gilmore](http://www.toad.com/gnu/)  
     John Gilmore is one of the founders of the Electronic Frontier Foundation, the Cypherpunks mailing list, and Cygnus Solutions. He created the alt.* hierarchy in Usenet and is a major contributor to the GNU project. He has donated $10,000.
*   [Bytemark Hosting](http://bytemark.co.uk/)  
     Bytemark provides discounted hosting facilities to Freenet and comes with our highest recommendation.
*   [zoozle Torrent Search](http://www.zoozle.org/)  
     zoozle is a search engine for BitTorrent and P2P networks. It is also available in [german](http://www.zoozle.net/ "deutsche Torrent Suchmaschine") and [french](http://www.zoozle.biz/ "le moteur
    							français de recherche pour BitTorrent"). They have donated $1,500.
*   [YourKit, LLC](http://www.yourkit.com/)  
     YourKit is kindly supporting Freenet by providing us a free of charge license of its full-featured Java Profiler. YourKit, LLC is the creator of innovative and intelligent tools for profiling Java applications. You can learn more about [YourKit Java Profiler](http://www.yourkit.com/java/profiler/index.jsp) following the link.
*   [Google](http://www.google.com/)  
     Google [open source](http://code.google.com/) have three times donated $18,000, as well as paying for students to work with us over summer since 2006 through the [Google Summer of Code](http://code.google.com/soc/) program.
*   [Finanzvergleich](http://www.finanzvergleich.de)  
     Finanzvergleich is a German financial services comparison site, who have contributed $1,500.
*   [TopDir](http://www.topdir.de "Top Directory")  
     TopDir is a human edited web directory with informations about interesting topics and websites in the German language.
*   [All Filters](http://www.allfilters.com/ "All Filters") - another generous sponsor.
*   [A German Site for Gardening and Plants](http://www.gartenheinz.de "A German Site for Gardening and Plants") - another generous sponsor.
*   [Simple Car Rentals](http://www.simple-carrentals.com/)  
     Simple Car Rentals has generously supported Freenet by helping us with some of our administrative expenses over the years.
*   [The Sports Den](http://www.sportsden.ie/)  
     The Sports Den has a wide variety of outdoor sports equipment, they are based in Ireland but can ship to the UK, Europe, and the United States.
*   ![](assets/img/logo_intellij_idea.png)  
    [JetBrains](https://www.jetbrains.com) has kindly provided a license for the Ultimate edition of [IntelliJ IDEA](https://www.jetbrains.com/idea).

Freenet Project Inc does not necessarily endorse the business activities of all of the companies listed on this page.

Donation inquiries please contact [Ian Clarke](mailto:donate@freenetproject.org)
""")))

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
