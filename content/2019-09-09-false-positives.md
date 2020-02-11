---
layout: content
title:  Statistical results without false positives check are most likely wrong
date:   2019-09-09
categories: release
---
Like every other privacy network, Freenet is a target of
statistical attacks to trace the activity of its users.

Studies that investigated tracing Freenet users were built on
unrealistic idealized setups or simplistic routing, so that their
results don’t apply to the real network.

Despite these shortcomings in the studies, there have been cases of
seized equipment. To prevent future cases from targeting innocents based on
these misleading statistics, we want to provide an example of a clean
calculation of the probability that some observation is a false
positive.

A short definition: False positives are results which look like a hit,
e.g. finding the originator of a request, but which are wrong,
e.g. pointing to the wrong persion.

Second definition: A Freenet node is Freenet running on a computer.

When observing Freenet, false positives most likely happen because of
misunderstanding how Freenet routing works, how file transfer works,
or how connections in Freenet are structured in real operation.

In the article
[tracking efforts based on false statistics][false-statistics],
we already showed how false results occur due to specific
misunderstandings about the concepts used in Freenet routing.
The current article shows how false positives happen due to using a
false idea about the actual structure of the Freenet network.


[false-statistics]: /police-departments-tracking-efforts-based-on-false-statistics.html

Firstoff: In an idealized structure, each node has 6 connections, all
nodes provide the same bandwidth, and all connections are usable all
the time. Such an idealized lattice of nodes looks like the following:


       6     6
    6     6     6
       6     6
    6     6     6
       6     6


In the real network at the time of writing, the number of connections
varies between 5 and 65, depending on the bandwidth available at the
nodes. A snapshot of the connection-count distribution can be seen on
the [Freenet statistics site][freenet-stats]. Between 10% and 80% of
the connections are inactive due to overload (backoff). This increased
when grouds of users started to patch their nodes to request data at a
higher rate than the rest.

[freenet-stats]: https://d6.gnutella2.info/freenet/USK@WMa1Z40iYdZZ51yctQ3toFl9zuuFEnNdsm3NejJU5KE,jCBcaNBeKD5~sSQeSkyKz737Bh5ibBGqdzfD8mgfdMY,AQACAAE/statistics/560/

A more realistic structure therefore looks like this:



           80  6   6
        70            6
      65                6
     60                  6
    55                   13
    50         24        13
    42                   13
     39                 15
      36               18
        33           21
           30 28  24




            6   
        70      13  
                    
      55    7     20
                    
         40   30    
                    
                    


The difference to the idealized structure which is most important to
this article is that almost every node has at least one connection to
another node with 8 connections or less. Also several of these
connections are in backoff, so they are not actually used, which
easily reduces the effective connection count to 4. From now on I will
call such nodes “small nodes”.

If the connection count of a node is just 4, the requests a
neighboring node forwards from a single download look very similar to
requests from the neighboring node if it has 4 downloads running.

Therefore whenever you see requests which could originate from a given
node, you must check how likely it is that they were actually sent
from such a small node. 

The first step is to check whether we can exclude a small node as
likely originator. Freenet assigns the number of connections based on
the assigned bandwidth. A node with 4x the bandwidth has 2x the
connections. Therefore, if its user did not actively change its code,
a small node has low bandwidth.

As a simple test, I downloaded a file with roughly 20 MiB on a node
with 8 connections as maximum, 6 active connections on average. It
downloaded 2 MiB per minute. Scaling up, a node with 16 connections
should download about 8 MiB per minute. If you observe a download of
400 MiB that takes 2 hours or more, it is possible that it comes from
a small node with around 11 peers (8-9 working at any time). 

If you see 400MiB take only 1 hour or you see 1 GiB downloaded in 2
hours, it is more likely that the originator has 16 connections or
more. With some tricks that can be increased, so as a rule of thumb to
exclude a small node you would have to observe a download of 400 MiB
taking only half an hour. Due to asymmetric connections a small node
is typically one with slow upload, not with slow download.

With these basics in place, we’ll show the rest with a scenario.

Assume that there is a monitorying node that observed requests coming
from a node with 50 peers. The file in question is 400 MiB big and the
download lasted slightly more than two hours. Assume that you observed
requests for 4% of the file from the 50 peer node.

In an idealized uniform network without friend-of-a-friend (FOAF)
routing, you would now assume that you are connected to the
originator. But due diligence requires that you correct for FOAF
routing and the real non-uniform structure, and check for false
positives.

How likely is it that the requests were started by one of the roughly
8 small nodes connected to a typical 50-peer-node?

A typical false positive would be that within those two hours, a node
you were connected to tried to retrieve the file. Let’s only use
information we actually received (without naming names). We’ll clearly
mark where we have to take assumptions, and where this is due to
lacking required information.

Let’s start with the information:

> between 3:50 PM UTC and 6:08 PM UTC the Freenet node requested 383
> unique blocks. The Freenet node reported an average of 51.3
> peers. To reconstruct the file requires a minimum of 12,723 blocks
> of a total possible of 24,874.

- minimum required blocks: 12,723
- the node had 50 peers
- the observer saw 383 block-requests sent via the connection with you


The node had 50 peers.

At that time about 25% of nodes had less than 10 peers (peek at 7
peers), 15% of nodes had only 10 to 15 peers, with the rest evenly
spread between 16 and 70. Only about 20% of nodes have 50 peers or
more. See the [^peercount] footnote at the end for the origin of this
data.


Assumptions: the node was connected to a node with 7 peers, and that
node requested the file. From the peers of that node, you were the
only with 50 peers or more. Then there was a node with 30 peers. Then
two nodes with 15 peers each, and three nodes with 7 peers each.


- assumption: actual originator had 7 peers
- assumption: the peer-count distribution was typical


This is still a typical situation (not a rare one).

Originator-connections:

- node: 50 peers.
- A: 30 peers.
- B: 15 peers.
- C: 15 peers.
- D: 7 peers.
- E: 7 peers.
- F: 7 peers.

We do not know the number of peers of the observer node, so let’s assume
that it has many connections to see a larger share of the traffic. Let’s
assume 70, because that’s what I would do.


- assumption: observer had 70 peers. (information lacking)


First step: The originator requests only the minimum required blocks of
the file, because all requests succeed. In absolute numbers: 12,723
requests.

These are distributed over the peers. In a typical situation, about one
in three peers is backed off. Let’s assume the routable hosts during the
request to be the node, A, C, D and E. B and F are backed off.

Routable:

- node: 50 peers.
- A: 30 peers.
- C: 15 peers.
- D: 7 peers.
- E: 7 peers.

Now those requests are distributed via FOAF-Routing not evenly but by
peer-count. There are in total 119 second degree peers, so the node
will receive on average 50/119 * 12723 requests, which would be 5345
requests.

Now we get to the node. Let’s assume a typical distribution
again. Since it has many peers, it will stick closer to the
statistical node-count due to stronger sampling. It will have 10 nodes
with 50 or more peers, one of which is the observer node. As usual, 30%
will be backed off.

The routable connections (not backed off):

- 1 Observer: 70 peers.
- 6 with 60 peers.
- 13 with 30 peers.
- 5 with 15 peers.
- 10 with 7 peers.

The backed off connections:

- (3 with 60 but backed off).
- (7 with 30 but backed off).
- (2 with 15 but backed off).
- (3 with 7 but backed off).

This gives a total number of 965 second-level peers via routable
connections, of which the observer watches 70. So you’d expect that the
observer will see 5345 * 70 / 965 requests: Total requests you received
multiplied by the peers of the observer and divided by the total count
of routable second-level peers.


5345 * 70 / 965 = 387.720207253886.


This number of requests is therefore confirmed as a likely false
positive. It occurs in a typical scenario where the node is not
the requester.


The short of it: The argumentation does NOT show that the node is
likely the requester of the file. Not even in a typical situation. The
most likely situation is that a node this node was connected to
requested the file without the nodes knowledge. If we’d use atypical
but often occurring situations, this would be even clearer.


Sidenote: A calculation like this is not sufficient to show that someone
is guilty. It only shows that the information provided CANNOT show
guilt, because it is very likely to be a false positive.


This is for a file where all blocks succeeded. For a file that’s on the
brink of dropping out, you’d expect two times as many requests. If the
actual requester had more peers, you’d expect fewer requests. If the
requester had only nodes with few peers, you’d expect more
requests. And this is without actually looking for evidence. This is
just disproving the claim using the much too limited information from
the affidavit by showing that this is most likely a false positive.



Besides: Argumentation like the following argumentation is false to a
seriously annoying degree:

> minimum of 12,723 blocks of a total possible of 24,874. These 383 blocks
> represent 155% of the even, or expected, share of the minimum block
> (12,723) required to download the file and 79% of the even or expected

Those 3% of the file the observer saw are 155% of what you’d expect if
all the nodes peers had the same number of peers. But that is a false
assumption, as you can already see from the example distribution given
for the originator. The number of blocks requested scale with the
peercount of each peer. So if the observer node had 60 peers while a
typical node had 20 peers, the observer would automatically receive 3x
as many requests as with even share.


[^peercount]: The peercount is taken from the statistics in june and october, versions 334 and 355 as found via the datehints for that site, counted by eye: SSK@WMa1Z40iYdZZ51yctQ3toFl9zuuFEnNdsm3NejJU5KE,jCBcaNBeKD5~sSQeSkyKz737Bh5ibBGqdzfD8mgfdMY,AQACAAE/statistics-DATEHINT-2018-9?type=text/plain SSK@WMa1Z40iYdZZ51yctQ3toFl9zuuFEnNdsm3NejJU5KE,jCBcaNBeKD5~sSQeSkyKz737Bh5ibBGqdzfD8mgfdMY,AQACAAE/statistics-DATEHINT-2018-10?type=text/plain SSK@WMa1Z40iYdZZ51yctQ3toFl9zuuFEnNdsm3NejJU5KE,jCBcaNBeKD5~sSQeSkyKz737Bh5ibBGqdzfD8mgfdMY,AQACAAE/statistics-334/plot_peer_count.png SSK@WMa1Z40iYdZZ51yctQ3toFl9zuuFEnNdsm3NejJU5KE,jCBcaNBeKD5~sSQeSkyKz737Bh5ibBGqdzfD8mgfdMY,AQACAAE/statistics-355/plot_peer_count.png



As a note: The peer-count can change from release to release when parameters are
optimized. The argumentation here stays the same, but the numbers change
a bit. People will have to look at the peer count distribution
during the time of the measurement.



Final note: The minimal information required for statistical claims
about observations of node upload or download activity in Freenet:

- The exact time and HTL of each watched chunk that was seen from the node
    - per chunk: node-location of the observer at the time
    - per chunk: node-location of the observed at the time
    - per chunk: node-locations of all peers of the observer at the time
    - per chunk: node-locations of all peers of the observed at the time
    - per-chunk: the manifest it belongs to
                 (only size + index in some list + number of chunks in the
                  manifest)
    - per chunk: routing part of the key of the chunk
      (no decryption possible from this info => data not accessible)

- The exact formula of the probability that the observed is a valid
  target
- The exact formula of the probability that the observed is not a false
  positive
- The results of applying those formula to the data along with the data,
  so they can be checked independently.

- all chunks received at HTL <= 16 which would be a match if at HTL > 16
- The peercounts they observed on that day in all nodes they connected to
  (a plain list of numbers)
- Keys for chunks should be truncated by cutting or blacking at least
  4 letters, so they cannot easily be used to download the associated
  data, though the full keys must be provided on request to an
  independent trusted party (i.e. the defense lawyer) to verify that
  they contain what is claimed. Otherwise they could just make up
  claims from thin air.


definition: watched chunks are those which are recorded if received from
            the observed or sent to the observed, as well as those which
            would be recorded if received by the observer or sent by the
            observer.


If observers cannot provide this minimal information, they cannot get
a robust statistical result. If they do not want to provide this to
a court, they prevent the court from checking their claims.


Yes, it is hard to correctly trace activity in Freenet to a
specific user. Without this property, Freenet could not protect
Freedom of speech and of the press, both of which are under attack
in many countries around the world.
