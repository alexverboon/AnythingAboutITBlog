---
title: "SCVMM 2008 - After 48 hours"
layout: "post"
date: 2008-12-23T02:15:49Z
slug: "scvmm-2008-after-48-hours"
aliases:
  - "/2008/12/scvmm-2008-after-48-hours/"
description: "It's about 48 hours ago , that i started with setting up a System Center Virtual Machine Manager environment, No worries, i have been doinng otherthin..."
author: "Alex Verboon"
tags:
  - hyper-v
  - virtualization
categories:
  - hyper-v
  - virtualization
---
It's about 48 hours ago , that i started with setting up a System Center Virtual Machine Manager environment, No worries, i have been doinng otherthings in between, although today , uhm yesterday I spend most of the time with it. Also the hardware I have available , isn't realy that powerfull, so it all takes a bit time, but that's okay, while waiting I've just continued reading.

So for all those that plan to give SCVMM a try as well but don't have big powerfull servers available let me encourage you, my setup is as following:

	
- Windows 2008 x64 with Hyper-V runs on a HP 8710p notebook with a 150 GB disk and 2 GB RAM
	
- System Center Virtual Machine Manager runs on Windows 2008 x64 that runs in a WMWare Workstation session that runs on a HP dc7800 desktop with 2 GB RAM, the session has 1024 GB RAM assigned
	
- The System Center Virtual Machine Manager Console is installed on Windows Vista SP1 that runs in a VMWare Workstation Session that runs on another desktop with 3 GB RAM.
	
- An Active Directory is required, not for the guest systems you run in SCVMM but for SCVMM itself. I run the AD on a Windows 2003 Server within VMWare as well, as i was slowly running out of RAM on my physical machine, i just gave it a 256 MB RAM, works well so far.

In general i do strongly recommend that before you start installing the various component, you make sure you are working with a most resent installation, e.g. Vista must be SP1 and for Windows Server 2008, there are a couple of important updates to be applied, espeically to update the Hyper-V Server. Read [Warning on Hyper-V hosts under SCVMM ](http://blogs.msdn.com/virtual_pc_guy/archive/2008/11/20/warning-on-hyper-v-hosts-under-scvmm.aspx)for more details.

The first page to start is the [Microsoft System Center Virtual Machine Manager](http://www.microsoft.com/systemcenter/virtualmachinemanager/en/us/default.aspx) site. More VM related links can be found on the [Virtual PC Guy](http://blogs.msdn.com/virtual_pc_guy/default.aspx) blog.

To be continued....

