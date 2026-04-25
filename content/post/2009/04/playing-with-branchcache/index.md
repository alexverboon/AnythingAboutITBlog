---
title: "Playing with BranchCache"
layout: "post"
date: 04/20/2009 00:23:13
slug: "playing-with-branchcache"
aliases:
  - "/2009/04/playing-with-branchcache/"
description: "During the past 2 days I have been looking at the Windows 7 BranchCache feature. After hearing, reading and talking about this for months, it was abou..."
author: "Alex Verboon"
tags:
  - branchcache
  - windows-7
  - windows-server-2008r2
categories:
  - branchcache
  - windows-7
  - windows-server-2008
---
During the past 2 days I have been looking at the Windows 7 BranchCache feature. After hearing, reading and talking about this for months, it was about time to do some hands-on stuff. 

  I used the [BranchCache Early Adopter's Guide](http://www.microsoft.com/downloads/details.aspx?FamilyID=A9A1ED8A-71AB-468E-A7E0-470FD46E46B3&displaylang=en) from Microsoft. If you would have a perfect test environment, the implementation would probably be done in 2-3 hours. For me it took a little bit longer……. but once again, I’ve learned a lot more. 

  I tested the “Distributed” mode, this is where the BranchCache gets replicated on the clients local disk. 

  My test environment looked like this: 

  **PC1** – Running VMWare Workstation with a domain controller and 2 Windows7 guests. While the domain controller runs in bridged network mode, i had the two Windows7 clients running in NAT mode, this to make sure they don’t appear in the same subnet as the File Server that has BranchCache enabled. (otherwise nothing will happen)

  **PC2** – Running VMWare Workstation with a Windows 2008R2 server configured with BranchCache. This server was running with bridged network mode. 

  The configuration is quite straight forward and can all be done via Group Policies or using the netsh command. 

  There is no GUI for BranchCache, but using the netsh branchcache commands and perfmon helps you to see if things work. 

  For more information about BranchCache check the Microsoft TechNet BranchCache site: [http://technet.microsoft.com/en-us/network/dd425028.aspx](http://technet.microsoft.com/en-us/network/dd425028.aspx)

