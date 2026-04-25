---
title: "Hyper-V Terminology"
layout: "post"
date: 2009-03-16T21:04:25Z
slug: "hyper-v-terminology"
aliases:
  - "/2009/03/hyper-v-terminology/"
description: "Talking to people about virtualization almost every day, I notice that many aren’t that familiar yet with all the terminologies. [Ben Armstrong](http:..."
author: "Alex Verboon"
tags:
  - hyper-v
  - terminology
  - virtualization
  - Windows
  - PowerShell
  - Office
categories:
  - hyper-v
  - virtualization
  - windows-server-2008
  - PowerShell
  - Office
---
Talking to people about virtualization almost every day, I notice that many aren’t that familiar yet with all the terminologies. [Ben Armstrong](http://blogs.msdn.com/Virtual_PC_Guy/) has written two good articles on his [blog](http://blogs.msdn.com/Virtual_PC_Guy/), describing all the terminologies used around Hyper-V. 

  [Hyper-V Terminology](http://blogs.msdn.com/virtual_pc_guy/archive/2008/02/25/hyper-v-terminology.aspx)

  [Hyper-V Terminology Update](http://blogs.msdn.com/virtual_pc_guy/archive/2009/03/04/hyper-v-terminology-update.aspx)

  One of the things that seems to confuse people a lot is understanding the difference between Hyper-V Server and Hyper-V on Server 2008. I take the freedom of copying Ben’s explanation (below). 

  ***Microsoft Hyper-V Server**      
When you see people talk about “Microsoft Hyper-V Server” they are talking about the stand alone version of Hyper-V.  The simple rule here is the “Microsoft” means that you are not talking about a full Windows installation.  From a Microsoft lexicon point of view software is either part of Windows – and gets the Windows naming (e.g. Windows Powershell) or is not part of Windows and gets the Microsoft naming (e.g. Microsoft Office). *

  ***Hyper-V on Windows Server 2008 / Windows Server 2008 with the Hyper-V role enabled**      
The part is a little clumsy.  While we have the “Windows Server 2008 without Hyper-V” SKU, its alternative is just “Windows Server 2008”.  But in order to avoid confusing people into thinking there is another SKU you will never see Microsoft say “Windows Server 2008 with Hyper-V” as that sounds to close to the aforementioned SKU name.  As a result you will see the above terms used to refer to a Windows Server 2008 system that has Hyper-V enabled (as compared to a Windows Server 2008 system that does not have Hyper-V enabled).*

