---
title: "The Argument against Disabling IPv6"
layout: "post"
date: 2010-03-08T21:09:54Z
slug: "the-argument-against-disabling-ipv6"
aliases:
  - "/2010/03/the-argument-against-disabling-ipv6/"
description: "Last Friday I met with some friends I used to work with in the past and we had some talk about Windows 7 and IPv6. One had mentioned that they would e..."
author: "Alex Verboon"
tags:
  - dhcp
  - directaccess
  - homegroup
  - ipv6
  - tcpip
  - windows-7
categories:
  - directaccess
  - ipv6
  - knowledge
  - tcpip
  - vista
  - windows-7
---
Last Friday I met with some friends I used to work with in the past and we had some talk about Windows 7 and IPv6. One had mentioned that they would explicitly disable the IPv6 on the client systems, this because they would not use it and they wanted to avoid unnecessary network traffic on their LAN/WAN. 

  Back home I did some searches on the internet and found the below statement in the [Support for IPv6 in Windows Server 2008 R2 and Windows 7](http://207.46.16.252/en-us/magazine/2009.07.cableguy.aspx) Microsoft TechNet Magazine article. 

  *It is unfortunate that some organizations disable IPv6 on their computers running Windows Vista or Windows Server 2008, where it is installed and enabled by default. Many disable IPv6-based on the assumption that they are not running any applications or services that use it. Others might disable it because of a misperception that having both IPv4 and IPv6 enabled effectively doubles their DNS and Web traffic. This is not true.*

  *From Microsoft's perspective, IPv6 is a mandatory part of the Windows operating system and it is enabled and included in standard Windows service and application testing during the operating system development process. Because Windows was designed specifically with IPv6 present, Microsoft does not perform any testing to determine the effects of disabling IPv6. If IPv6 is disabled on Windows Vista, Windows Server 2008, or later versions, some components will not function. Moreover, applications that you might not think are using IPv6—such as Remote Assistance, HomeGroup, DirectAccess, and Windows Mail—could be.*

  *Therefore, Microsoft recommends that you leave IPv6 enabled, even if you do not have an IPv6-enabled network, either native or tunneled. By leaving IPv6 enabled, you do not disable IPv6-only applications and services (for example, HomeGroup in Windows 7 and DirectAccess in Windows 7 and Windows Server 2008 R2 are IPv6-only) and your hosts can take advantage of IPv6-enhanced connectivity.*

  I must admit that I haven’t looked at this in more detail myself, but for now I guess I would follow the advice above and leave IPv6 on, especially taking into account that some of our customers are considering using DirectAccess at some stage. 

  Another interesting article I recommend reading is [IPv6 Autoconfiguration in Windows Vista](http://technet.microsoft.com/en-us/magazine/2007.08.cableguy.aspx) which explains the IPv6 Autoconfiguration behavior in more detail.

