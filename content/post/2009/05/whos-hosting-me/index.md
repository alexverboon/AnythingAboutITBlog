---
title: "Who&rsquo;s hosting me ?"
layout: "post"
date: 05/22/2009 11:35:40
slug: "whos-hosting-me"
aliases:
  - "/2009/05/whos-hosting-me/"
description: "This morning i had an issue with a fileserver that is running as a guest on a Hyper-V server, far away from my location, in fact I did not even know w..."
author: "Alex Verboon"
image: "img/post-heroes/whos-hosting-me.png"
tags:
  - guest
  - hyper-v
categories:
  - hyper-v
  - virtualization
---
This morning i had an issue with a fileserver that is running as a guest on a Hyper-V server, far away from my location, in fact I did not even know what Hyper-V system is hosting that Fileserver. I wanted to see within Hyper-V manager how the system is doing, but without knowing the Hyper-V server host name, you can’t connect (kind of logic) :-)

  So what’s the name of the underlying server that is hosting my virtual server ? A friend within my team found the answer. 

  To my surprise this information is stored within the guest windows registry under HKLM\Software\Microsoft\Virtual Machine\Guest\Parameters as shown in the picture below. 

  [
![vhost](images/vhost-thumb.png)
](https://www.verboon.info/wp-content/uploads/2009/05/vhost.png)

