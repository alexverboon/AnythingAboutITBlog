---
title: "Windows 7 - Driverstore size"
layout: "post"
date: 2009-02-01T11:38:51Z
slug: "windows-7-driverstore-size"
aliases:
  - "/2009/02/windows-7-driverstore-size/"
description: "When it comes to OS deployment the size of the image to some extend does matter. Windows by default comes with a large set of plug and play device dri..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Drivers'
  - 'Driver Store'
---
When it comes to OS deployment the size of the image to some extend does matter. Windows by default comes with a large set of plug and play device drivers that are included within the operating system installation sources.

Prestaged drivers in Windows Vista and Windows 7 are located under C:\Windows\system32\Driverstore.

If you run the following command against your mounted Windows 7 image file, you get a list of all [PnP](http://www.microsoft.com/whdc/system/pnppwr/pnp/default.mspx)drivers included within the Driverstore.

Dism /image:c:\mount /Get-Drivers /all

Now getting back to the image size. Looking at how we could eventually save image size space, I took a closer look at the Windows 7 Driverstore folder size, that on an installed system uses **624 MB**. So that looked like a potential candidate to reduce image size.

As mentioned above 624 MB is what the Driverstore uses on an installed system, but how much does it consume within an image, taking into account that there the content is compressed.

Running the following command creates a separate WIM (image) file with just Driverstore content included.

Imagex /capture c:\temp\driverstore\ c:\temp\win7drv.wim "win7driverstore"

The result is that 624 MB Driverstore content now just uses **219 MB**. If we add the /compress max option to the above Command brings the size even down to **197 MB**. 

Conclusion: Beside the fact that officially the default driver store cannot be modified anyway (if I am wrong here let me know), I think that carrying those +- 220 MB don't make much of a difference.

