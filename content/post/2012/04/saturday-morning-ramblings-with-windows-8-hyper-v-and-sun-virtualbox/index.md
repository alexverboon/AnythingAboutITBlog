---
title: "Saturday morning ramblings with Windows 8 Hyper-V and Sun VirtualBox"
layout: "post"
date: 04/28/2012 08:43:56
slug: "saturday-morning-ramblings-with-windows-8-hyper-v-and-sun-virtualbox"
aliases:
  - "/2012/04/saturday-morning-ramblings-with-windows-8-hyper-v-and-sun-virtualbox/"
description: "Yesterday I prepared a new system with Windows 8 CP that has the latest Intel I7 processor and 8GB of RAM. My initial plan was to use Hyper-V which is..."
author: "Alex Verboon"
tags:
  - 64-bit
  - guest
  - hyper-v
  - virtualbox-2
  - windows-8
categories:
  - virtualbox
  - windows-8
---
Yesterday I prepared a new system with Windows 8 CP that has the latest Intel I7 processor and 8GB of RAM. My initial plan was to use Hyper-V which is now also included as a feature on the Client.

  So on this beautiful Saturday morning I continued with the setup of this HP 8760w Elitebook.  But because I ran into several network related issues, others have also reported about on the Microsoft forums, I decided to switch back to Sun VirtualBox for now as that has worked fine on Windows 8 so far. 

  But then to my surprise I noticed that when creating a new VM in VirtualBox I could not select any 64 Bit guest anymore……..I had previously setup 64 bit OS guests in Hyper-V so was pretty sure the hardware supports it, just to go for sure, I went back into the BIOS and checked all the settings related to Virtualization, all set correctly. 

  I then ran the [SecurAble](http://www.grc.com/securable.htm) tool that also provides the ability to show the whether a system provides Hardware Virtualization support and to my surprise it indicated it would not. 

  Well finally I removed the Hyper-V feature from Windows 8 CP and guess what……VirtualBox now allows me to select and install 64 Bit guests. 

  Conclusion: You never stop learning. Wish you all a great and relaxing week-end.

