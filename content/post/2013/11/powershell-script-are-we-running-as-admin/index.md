---
title: PowerShell Script - Are we running as Admin?
layout: post
date: '2013-11-08T20:19:16Z'
slug: powershell-script-are-we-running-as-admin
aliases:
- /2013/11/powershell-script-are-we-running-as-admin/
description: While exploring some of the new cmdlets that come with Windows 8.1 I
  came across [Test-NetConnection](http://technet.microsoft.com/en-us/library/dn372...
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'PowerShell'
  - 'Admin-Credentials'
---
While exploring some of the new cmdlets that come with Windows 8.1 I came across [Test-NetConnection](http://technet.microsoft.com/en-us/library/dn372891.aspx). and noticed that it has a property called IsAdmin. When running the cmdlet in an elevated PowerShell session the property returns True otherwise False. So I put together a very simple script to check whether we are running as admin or not.

```powershell
<#
.Synopsis
   Checks if we run as administrator
.DESCRIPTION
   This script uses the Test-NetConnection cmdlet that contains a IsAdmin Property to check if we ar running as admin
.EXAMPLE
   Check-Admin.ps1
#>
$AmIAdmin = Test-NetConnection localhost
 if ($AmIAdmin.IsAdmin -eq "True") {write-host "Running as Admin"} Else {write-host "NOT Running as Admin"}
```

Other (and probably more reliable) ways to determine whether we are running as admin are described [here](http://blogs.technet.com/b/heyscriptingguy/archive/2011/05/11/check-for-admin-credentials-in-a-powershell-script.aspx) by Ed Wilson and [here](http://blogs.msdn.com/b/virtual_pc_guy/archive/2010/09/23/a-self-elevating-powershell-script.aspx) by Ben Armstrong.

