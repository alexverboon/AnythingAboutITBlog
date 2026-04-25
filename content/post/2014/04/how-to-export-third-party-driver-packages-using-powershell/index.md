---
title: "How to export third-party driver packages using PowerShell"
layout: "post"
date: 04/04/2014 19:43:09
slug: "how-to-export-third-party-driver-packages-using-powershell"
aliases:
  - "/2014/04/how-to-export-third-party-driver-packages-using-powershell/"
description: "Windows 8.1 Update introduces a new cmdlet that allows you to export third-party drivers that are located within the driver store of a Windows client...."
author: "Alex Verboon"
image: "img/post-heroes/how-to-export-third-party-driver-packages-using-powershell.png"
tags:
  - dism
  - powershell
  - windows-8-1-update
categories:
  - powershell
---
Windows 8.1 Update introduces a new cmdlet that allows you to export third-party drivers that are located within the driver store of a Windows client. 

```
$ExpDrv = Export-WindowsDriver -Online -Destination c:\temp\3rdpartydrivers 

```

The result, all drivers exported into the provided destination directory

[
![2014-04-04_21h36_47](images/2014-04-04_21h36_47_thumb.png)
](https://www.verboon.info/wp-content/uploads/2014/04/2014-04-04_21h36_47.png)

Now we have a whole bunch of folders, but what drivers did we actually export?

```

$ExpDrv | Select-Object ClassName, ProviderName, Date, Version | Sort-Object ClassName

```

[
![2014-04-04_21h40_00](images/2014-04-04_21h40_00_thumb.png)
](https://www.verboon.info/wp-content/uploads/2014/04/2014-04-04_21h40_00.png)

For more information read the What’s new in DISM article [here](http://technet.microsoft.com/en-us/library/dn419776.aspx)

