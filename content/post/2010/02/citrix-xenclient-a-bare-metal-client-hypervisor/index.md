---
title: "Citrix XenClient a bare metal client hypervisor"
layout: "post"
date: 2010-02-07T21:26:42Z
slug: "citrix-xenclient-a-bare-metal-client-hypervisor"
aliases:
  - "/2010/02/citrix-xenclient-a-bare-metal-client-hypervisor/"
description: "Today Hypervisors are classified into two types. Type 1 is the so-called native bare metal hypervisor and type 2 the hosted hypervisor. Within the ser..."
author: "Alex Verboon"
tags:
  - hypervisor
  - xenclient
  - Windows
categories:
  - citrix
  - hypervisor
  - virtualization
---
Today Hypervisors are classified into two types. Type 1 is the so-called native bare metal hypervisor and type 2 the hosted hypervisor. Within the server based computing world there are various products available based on Type 1 (VMWare ESX Server, Citrix XEN Server) or Type 2 (Microsoft Hyper-V, VMWare Server). 

  Within the Desktop computing space most of us have rather been using Type2 based solutions such as VMWare Workstation or Microsoft VirtualPC. 

  With Citrix XenClient we will soon get a Type1 Hypervisor for client systems. So what is this good for? Well let’s assume you have a need to run two different versions of Windows on your laptop. You can either install both OS on the system and use a dual boot scenario, or what most of us do in these days, install one OS on the physical hardware and virtualize the second one on top of the primary OS using a desktop virtualization solution such as VMWare Workstation, Windows Virtual PC or Sun’s VirtualBox. 

  The downside of these approaches are that you can either only run one operating system at a time (Dual Boot option) or that running the Virtualized OS requires that you first boot the primary OS that hosts the Virtualization Software. 

  With the XenClient you can actually run both (or more) operating systems in parallel right on top of a Type1 Hypervisor. Once you have the Operating systems installed you can easily switch between desktops with a single keyboard shortcut, but you can also share applications between the two operating system sessions. 

  So who is going to use this ? Well I can think of various use cases. Imagine the Application developer who has one or more operating system installed with all his development tools and most likely prefers to delete these periodically depending on what he is working on. But then he also requires access to his company’s business applications that are managed and brought to his client by the companies IT department. With XenClient, the developer can have full control over his own managed operating systems but also benefit from having a corporate managed standard desktop environment. 

  At the end of last year I had the pleasure to get my hands on the XenClient Beta and although I could not spend as much time with it as I  wanted to, I can say, that it all looks very promising. Unfortunately I have no information about when Citrix is going to release the XenClient but assume it will be sometimes in 2010. 

  **Additional Resources:**    
[Citrix XenClient Overview](http://www.citrix.com/tv/#videos/1430)    
[XenClient Central](http://community.citrix.com/citrixready/xenclient)    
[Local Virtual Machine-based Desktops](http://www.citrix.com/English/ps2/products/feature.asp?contentID=1685500)    
[Patrick Gelsinger - Synergy Keynote Day 2 Part 1](http://www.citrix.com/tv/#videos/423) (XenClient starts at 28 minutes)    
[Microsoft hates Type 1 client hypervisors](http://www.brianmadden.com/blogs/appdetective/archive/2009/12/17/microsoft-hates-type-1-client-hypervisors.aspx)

