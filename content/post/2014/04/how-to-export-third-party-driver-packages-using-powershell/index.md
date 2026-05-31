---
title: How to export third-party driver packages using PowerShell
layout: post
date: '2014-04-04T19:43:09Z'
slug: how-to-export-third-party-driver-packages-using-powershell
aliases:
- /2014/04/how-to-export-third-party-driver-packages-using-powershell/
description: Windows 8.1 Update introduces a new cmdlet that allows you to export
  third-party drivers that are located within the driver store of a Windows client....
author: Alex Verboon
image: img/post-heroes/how-to-export-third-party-driver-packages-using-powershell.png
categories:
  - 'Windows'
tags:
  - 'PowerShell'
  - 'Windows-8-1-Update'
---
Windows 8.1 Update introduces a new cmdlet that allows you to export third-party drivers that are located within the driver store of a Windows client. 

`powershell
$ExpDrv = Export-WindowsDriver -Online -Destination c:\temp\3rdpartydrivers 

`powershell

The result, all drivers exported into the provided destination directory

![2014-04-04_21h36_47](images/2014-04-04_21h36_47_thumb.png)

Now we have a whole bunch of folders, but what drivers did we actually export?

`powershell

$ExpDrv | Select-Object ClassName, ProviderName, Date, Version | Sort-Object ClassName

```

![2014-04-04_21h40_00](images/2014-04-04_21h40_00_thumb.png)

For more information read the What’s new in DISM article [here](http://technet.microsoft.com/en-us/library/dn419776.aspx)