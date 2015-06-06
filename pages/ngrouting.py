# -*- coding: utf-8 -*-
# Python code copyright Gerard Krol, license: MIT
from .common import *

class NGRoutingSection(Section):
    def __init__(self):
        self.slug = "ngrouting"
        self.title = _("Freenet's Next Generation Routing Protocol")
    def get_content(self):
        # License: GFDL (from old freenetproject.org website)
        return text(md(_("""
**by [Ian Clarke](mailto:ian@locut.us), Freenet Project Coordinator, 20th July 2003**

While Freenet has come a long way since my 1999 paper, the fundamental ideas behind how Freenet finds information have changed very little. Now that Freenet is maturing it is time to re-examine the core Freenet architecture to see where it can be improved. This new design is known as "Next Generation Routing".

### Freenet's current routing mechanism

Firstly, let me recap on how Freenet works right now. Every node in the Freenet network is required to provide a simple service to other nodes in the system. When a node receives a request for a particular key, it should do its best to retrieve the data corresponding to that key as quickly as possible and send it back to the node that requested it. Provided that every node in the Freenet network performs this service reasonably well - Freenet will work.

In the simplest case, the recipients of the request will already have the data cached locally, and can immediately send it to the requester. In most cases, however, the node will need to request the data from another node in the network which it thinks will be better able to retrieve the data. The way Freenet makes this decision forms the core of the Freenet algorithm.

At present, the algorithm used to select which node should be consulted for a given key is relatively simple. In short, when a node forwards a request for a particular key to another node in the network, and that node is successful in retrieving the data, the address of an upstream node (possibly the one where the data originated) is included in the reply, this is called the "DataSource". The requester makes a note of the requested key, and the DataSource node passed back with that reply. It is assumed that the upstream node is a good place to route future requests for keys closest to the previously requested key. It is analogous to deciding that since your friend George successfully answered a question about France, he might also be a good person to answer a question about Belgium.

Despite its simplicity, this approach has proved surprisingly effective, both in simulation and in practice. One of the expected side effects of this approach was that nodes would tend to specialize in the retrieval of some keys to the exclusion of others. This can be seen is somewhat analogous to the way that people specialize in particular areas of expertise. This effect has been observed in actual Freenet nodes deployed in the Freenet network, the following image represents the keys stored by an actual Freenet node. The X axis represents the "keyspace", at the left is key 0, across to the right which is key 2<sup>160</sup>. Dark areas indicate where the node has better knowledge. The dark strips indicate areas in which the node has detailed knowledge about where requests for those keys should be routed:

<center>* image rthist.png missing, let us know if you find it! *</center>

Note that when the node was first initialized keys would have been evenly distributed across the keyspace. This is a good indication that Freenet's current routing algorithm is performing correctly. Nodes specialize like this due to an emergent feedback effect, when a node successfully responds to a request for a given key - it increases the likelihood that other nodes will route requests for similar keys in the future. Over time this effect causes the specialization that can be seen very clearly in the diagram above. You can see an animation of a node's datastore specializing over time [here](assets/img/histanim.mpeg).

### Next generation routing mechanism

The fact that it works, of course, does not mean that it cannot be improved upon. At the simplest level, note that the current algorithm does not distinguish between a slow Freenet node sitting at the end of a slow modem line in the remote Australian outback, and a powerful node connected to a T3 in downtown Los Angeles. Also note that while the current algorithm works, the only real way to test improvements to the algorithm is to see how they affect a large scale network, either in simulation, or in the real world - this leads to a slow and cumbersome development cycle. By making more effective use of the information available to a Freenet node, we can dramatically improve a node's ability to route requests in a manner likely to result in the fastest response for that request. By avoiding guesswork, and striving for a firm basis in statistical reality - we can even accelerate our development effort by allowing ourselves to determine the effectiveness of a modification based on its effect on a single node, before we deploy it. These goals are achieved by Next Generation Routing.

The core idea behind the Next Generation Routing design is to make Freenet nodes much smarter about deciding where to route information. For each node reference in its routing table, a node will collect extensive statistical information including response times for requesting particular keys, the proportion of requests which succeed in finding information, and the time required to establish a connection in the first place. When a new request is received, this information is used to estimate which node is likely to be able to retrieve the data in the least amount of time, and that is the node to which the request is forwarded.

### DataReply estimation

The most important metric is finding a way to estimate, given a given key being requested from a given node, how long it will take to get the data. To achieve this an algorithm was required that would meet the following criteria:

*   Must be able to make reasonable guesses about keys that it has not seen before

*   Must be progressive – if a node's performance changes over time, this should be represented, but should not be oversensitive to recent fluctuations which may vary significantly from the average.

*   Must be “scale free”  
    Consider a naive implementation of this that works by splitting the keyspace into a number of sections and maintaining an average for each. Now consider a node where most of its incoming requests lie within a very small section of the keyspace. Our naïve implementation would be unable to represent variations in response time within that small area and would therefore limit that node's ability to accurately estimate routing times.

*   Must be efficiently serializable

We developed a simple algorithm which meets these criteria. It works by maintaining N “reference” points (where N is configurable – 10 being a typical value) which are initially evenly distributed across the keyspace. When we have a new routing time sample for a particular key – we move the two points closest to our new sample toward it. The amount they are moved can be adjusted to change how “forgetful” the estimator is.

<center>![](assets/img/rte_diag.gif)  

</center>

In this diagram it can be seen that two of the reference points (blue) are being moved toward our new data sample (red).

When we wish to create an estimate for a new key, we see where the line between the reference points at either side of that key intersects (green) and this gives us our estimated response time.

### Handling different data lengths

Also consider the fact that there isn't just one timing measurement that must be taken into account when we receive a DataReply, there are two. The first is the time required to get the beginning of the response, the second is the time required to transfer the data. This raises the question of how we can combine these two timings into a single value which can be reported to the estimator algorithm described above.

The answer we have settled upon is to use these two numbers to estimate what the total time between the request being sent and the transfer being _completed_ would have been had the data been the average length of data in Freenet (which we in turn estimate by taking the average length of data in the local datastore). This is a single value which can be compared directly with other timing measurements even when they were made with requests where the data was differing sizes.

### Handling DataNotFound messages

When a request has visited the number of nodes specified in its "hops to live" field (similar to "time to live" in other protocols), a "DataNotFound" or DNF message is returned to the requester. This indicates that the data could not be found within the time limit specified by the requester. There are two reasons that a DNF can be returned for some data, either the data exists but wasn't found, or the data didn't exist at all. In the former case, a DNF would indicate a shortcoming in the routing ability of whichever node the request was routed to. In the latter case, it would not - but the difficulty is that for a given DNF - there is no easy way to tell what type of DNF it is, whether it is "legitimate" or not.

Let, us, for a moment, assume that there was a way to identify illegitimate DNFs. In this case, the cost in terms of the time required for such a DNF would be the time required to receive the DNF plus the time required to request the same data from somewhere else. We can estimate the former by looking at how long previous DNFs took for requests sent to this node (taking into account that this time will be proportional to the HTL of the request <sup>ie.</sup> a request with a HTL of 10 will visit twice as many nodes as a request with HTL 5 and will therefore take about twice as long to return a DNF). We can estimate the latter by looking at the average amount of time it takes to successfully retrieve some data.

Now, imagine a Freenet node with perfect routing, the only DNFs it returns would be "legitimate" - since if the data was in the network, it would find it. The proportion of DNFs this perfect node returned would be the same as the proportion of DNFs for which the data simply didn't exist in the network. Now - such a node (we assume) could not exist, however we can approximate it by looking at the proportion of DNFs for the node with the lowest proportion of DNFs in our routing table.

So now, we can determine the time cost of DNFs, and we can also approximate what proportion of a node's DNFs are legitimate - and therefore should not incur a time cost. We can therefore add an estimated routing time cost for each node to account for DNFs.

### Handing failed connections

With nodes which are heavily overloaded - it is also possible that when we attempt to establish a connection to them - we will be unable to do-so, we can account for this possibility by recalling the average proportion of failed connections for each node, and how long each took - and adding this on to our estimated routing time for that node.

### Inherited Knowledge

One of the problems observed in the current Freenet is the time required for a Freenet node to establish sufficient knowledge about the Freenet network to route efficiently. This is particularly damaging to Freenet's usability as people's first impressions of software is critical, and the first impressions of Freenet are generally the worst impressions of Freenet as they are formed before the Freenet node can route requests effectively.

The solution is to employ some qualified trust between Freenet nodes, allowing them to share the information the have collected about each other, albeit in a rather untrusting way. There are two ways that a Freenet node finds out about new Freenet nodes. The first is when they first start up - they load a "seednodes.ref" file which contains the routing expertise of another experienced node. With N.G routing this information will be enriched with actual statistical data so that even with a node first starts up, it will already have the knowledge of an experienced node. It will then go on to refine this knowledge according to its own experience.

The other way nodes learn about new nodes is in the "DataSource" field of successful replies to requests for data. The DataSource field will contain one of the upstream nodes in the request chain. The simple approach would be to allow this DataSource node to attach statistical information concerning its own performance to the reply - but clearly this would be open to abuse. A refinement would be to say that any node passing back a reply which has collected its own statistical information about the node in the DataSource will replace the statistical data in the reply with its own. This will mean that even if a node does put misleading statistical information in the reply - it will probably be replaced as it is passed back to the requester.

### Benefits of Next-Generation Routing

*   **Adapts to network topology**  
     In the old Freenet routing algorithm, a Freenet node running on a slow modem in the middle of the Australian outback is viewed pretty much the same way as a fast node running on a T3 in downtown San Jose. In essence, the underlying Internet topology is ignored by Freenet, all nodes are treated equally. In contrast, N.G routing bases its decisions on actual routing times, this means that a node will tend to prefer routing messages to faster nodes, on better Internet connections that are geographically closer - unless those nodes become overloaded, which will decrease the incentive to use them and have a load balancing effect.
*   **Performance can be evaluated locally**  
     With the old approach to Freenet's routing, the only concrete way to evaluate its performance was by trying it. With N.G Routing we have a simple metric of how effectively it is performing - namely the difference between estimated routing times, and actual routing times. If a modification to the algorithm results in closer estimates, then we know it is better. If not, we know that it isn't. This will dramatically accelerate the development cycle of future improvements.
*   **Approaching optimality**  
     If one accepts that in an environment where only one's own node may be trusted, it is reasonable to say that all decisions should be based upon one's own observations. Given this, it could be said that if we make optimal use of prior observations while making routing decisions, then our routing algorithm is optimal. Now clearly there will always be room for refinement in the manner in which the new algorithm estimates routing times

### Current Status

Next Generation routing was deployed in Freenet from 2003-2005, however in Freenet 0.7, started in 2005, we reverted back to a much simpler approach. A 2007 paper by Oskar Sandberg [Decentralized Search with Random Costs](http://arxiv.org/abs/0804.0577) determined that the concepts underlying this paper "were fundamentally sound".

### Interested in helping?

In addition to joining our development effort, you can really help us to make this all a reality by donating whatever you can spare to the project on our [Donations](donate.html) page.
""")))

class NGRoutingPage(Page):
    def __init__(self):
        self.slug = "ngrouting"
        self.title = _("Freenet's Next Generation Routing Protocol")
        # self.first_section_in_menu = True
        self.hidden = True
        self.sections = [
            NGRoutingSection(),
            ]
