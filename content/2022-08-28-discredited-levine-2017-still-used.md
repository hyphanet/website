---
layout: content
title:  The discredited Levine 2017 approach is still used
date:   2022-08-28
categories: news
---
In april 2020 the approach [by Levine et al.](http://ceur-ws.org/Vol-1873/IWPE17_paper_12.pdf) to track downloaders was
thoroughly debunked and proven to be wrong:
*Their false positives rate is wrong, their math is wrong, and their model is wrong.
Therefore results you get when using their method are false.* Yet this
approach is still used two years later to get warrants against Freenet users.

The Levine group themselves even changed their method in response
(they posted this to conference proceedings, not peer-reviewed, and
unlikely to pass peer-review because it contains claims that are
obviously false), but they still use the 2017 method for arguments in
court.

Therefore we are now providing the arguments that disprove it directly
on the Freenet Project website to ensure that they are found when
innocents are caught in that dragnet.

# Wrong false positives rate

The core pillar of the detection they name is their claim of a 2.3%
**false positives rate**. But this claim is **wrong**, because they only
reach it through many **false assumptions**:

-   They **ignore** that friend-of-a-friend routing breaks their metric when
    
    -   an intermediary node, or
    -   the observing node **has many connections**.
    
    which is not the rare case but **the normal case**.

-   They assume that they only get a false positive, if a request for a
    given file reached them with both HTL 18/17 and HTL 16. But the
    routing algorithm within Freenet causes them to **almost always**
    receive requests from a given node **over the same route**. So they
    get the same HTL, regardless of the actual number of hops from the
    source. Therefore Their 2.3% false positives rate contains a mixture
    of
    
    -   the probability of **two people** requesting the file in the same
        interval and
    
    -   the rate of **routing-changes** within Freenet (for example because a
        node on the path went offline). If a request from a given peer is
        received both from HTL 17 and from HTL 16 then routing changed,
        otherwise this should not happen.
    
    Their **false positives rate** when measuring with only one node is
    therefore **meaningless**.


# Wrong math

In addition **their math is wrong**:

> We construct a model by assuming that each request the
> downloader makes is sent to exactly one of its peers, and that
> the selection of that peer is made **uniformly at random**.

This does not take friend of a friend routing into account. Therefore
their math is wrong: It does not match the actual selection of peers,
so the results are meaningless for the actual Freenet.

They expect even share peer selection, but Freenet does not use even share.

# Wrong model

And their **model** of how measurement works **is wrong**:

> a simple expected fraction of 1/degree for the adjacent and
> (1/degree)² for the two-hop case.

This does not take the degree of the measuring node into account,
therefore it is not a model of routing in Freenet.


# Summary (TLDR)

Their false positives rate is wrong, their math is wrong, and their model is wrong. Therefore results you get when using their method are false.


# Remarks

To somewhat save the grace for the Levine-team: They at least tried to
actually measure the false positives rate. They did it wrong and drew
false conclusions, and that they tried doesn’t make it right and it
doesn’t excuse persecuting people based on their flawed reasoning, but
at least they tried.

That the Levine-team **did not contact Freenet developers** prior to
publication is **inexcusable**, though. It’s like publishing a paper based
on evaluations of particle beams from CERN without ever talking to
someone from CERN. Can it be so hard to write an email to press -at-
freenetproject.org saying 
*“Hi, we found a method to track Freenet downloaders and drafted a paper based on that. Could you have a look to see whether we missed something?”*

# Final words

If you want to know the actual requirements for calculating a false
positives rate in Freenet, read the article [Statistical results without false positives check are most likely wrong](https://freenetproject.org/statistical-results-without-false-positives-check-are-most-likely-wrong.html).

While the Levine group has a false positives check, their check is
wrong. They measured the wrong metric. We have explained patiently
where the Levine group made mistakes. It is hard to understand when
assuming scientific integrity that they still claim in court that
their 2017 method is robust even after they changed their approach
themselves.
