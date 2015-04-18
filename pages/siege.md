title: siege study notes
date: 2015-04-18
tags: [siege, ops]


- Sieging the Site

One thing we’ve gotten better at as a result of You Rather’s traffic is testing our apps under heavy load. On any given day, we’ve experienced large traffic spikes due to social media, aggregators (see: the Slashdot effect), or App Store features. Two tools we use a lot to test load handling are

siege, and ab. For this setup, we mostly used siege.

Once we got Nginx serving our site up just right on our dev instance, it was time to hammer the box to see what it could handle. Using

siege, we could see what kind of a load a single instance could handle. One great advantage ofsiegeis its ability to hit an endpoint with concurrent connections, perfect for simulating a real-world use-case of You Rather. Starting the command:

siege -t 1M -c 20 http://nginx-test.yourather.com/

We simulated 20 concurrent users (

-c 20) hitting the site on that instance, non-stop for a minute (-t 1M).siegegives great analysis of the tests both during and afterwards. Things looked great from the get-go. The throughput was much lower than the old Apache AMI, and response times were generally lower. We kept tweaking thesiegetest, varying between 10 to 100 or more concurrent connections (protip: don’t go over 75 connections generally, things will break…), hitting different endpoints, like the user profile page, a specfic question’s page, and even the 404 page.

￼

We compared the results from

siege’ing the Nginx instance to a version of the current Apache site running on a control instance. In short, the Nginx instance performed 100% more transactions, with 50% less response time per transaction. Better yet, we watched thetopon the Nginx box while testing this out. It handled it like a boss, barely topping out the CPU while slamming it with connections. Nginx was clearly giving the site - the boost it needed.

Alternativa ao siege: wrk, wrk2
