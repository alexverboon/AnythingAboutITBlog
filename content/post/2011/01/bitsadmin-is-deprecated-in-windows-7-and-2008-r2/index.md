---
title: "BITSAdmin is deprecated in Windows 7 and 2008 R2"
layout: "post"
date: 01/19/2011 23:38:07
slug: "bitsadmin-is-deprecated-in-windows-7-and-2008-r2"
aliases:
  - "/2011/01/bitsadmin-is-deprecated-in-windows-7-and-2008-r2/"
description: "Just recently when I created a [script](https://www.verboon.info/index.php/2011/01/automated-microsoft-security-essentials-installation/) using BITSAd..."
author: "Alex Verboon"
tags:
  - bits
  - bitsadmin
  - download
  - powershell
categories:
  - bits
  - powershell
  - scripting
---
Just recently when I created a [script](https://www.verboon.info/index.php/2011/01/automated-microsoft-security-essentials-installation/) using BITSAdmin, I noticed the following text when running the BITSAdmin executable: **BITSADMIN is deprecated and is not guaranteed to be available in future versions of Windows. Administrative tools for the BITS service are now provided by BITS PowerShell cmdlets**.

  So BITS with PowerShell landed on my to-look-at list, but just today I came across Ashley McGlone’s Blog – [Big Downloads With Powershell](http://blogs.technet.com/b/ashleymcglone/archive/2010/11/18/big-downloads-with-powershell.aspx) which contains a sample script for BITS downloads using PowerShell. With all respect to PowerShell, I do hope Microsoft is not considering replacing all the handy command line tools with PowerShell cmdlets :-)

