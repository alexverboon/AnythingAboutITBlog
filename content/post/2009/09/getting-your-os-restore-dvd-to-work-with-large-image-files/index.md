---
title: Getting your OS Restore DVD to work with large image files
layout: post
date: '2009-09-18T16:10:07Z'
slug: getting-your-os-restore-dvd-to-work-with-large-image-files
aliases:
- /2009/09/getting-your-os-restore-dvd-to-work-with-large-image-files/
description: This week, we completed the Windows 7 x64 build for our internal Tech
  Community. During the testing of the OS Restore DVD we ran into a problem when a...
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'Large-Image'
  - 'Dvd'
---
This week, we completed the Windows 7 x64 build for our internal Tech Community. During the testing of the OS Restore DVD we ran into a problem when attempting to restore the image from DVD. 

  Our custom Windows 7 64 bit image has a size of approx. 4.8 GB. This because the 64 bit version of Windows7 has a larger footprint than the 32 bit version and because we had included some applications like Office 2010 CTP and some drivers for a limited number of hardware. Since we did not want to split the content across multiple DVD’s, we had decided that we would create just one ISO with [OSCDIMG.EXE](http://technet.microsoft.com/en-us/library/cc749036(WS.10).aspx) life that people would need to burn on a [Dual Layer](http://en.wikipedia.org/wiki/DVD) DVD which provides enough capacity. 

  Oscdimg is a command-line tool for creating an image file (.iso) of a customized 32-bit or 64-bit version of Windows PE. You can then burn that .iso file to a CD-ROM or DVD-ROM. The OSCDIMG.EXE is provided with the Windows Automated Installation Toolkit (WAIK). 

  The problem we faced was that once WinPE was booted and the image restore process was started, Image.exe terminated with an error message. We had used the exact same process to produce restore DVD for the 64 bit OS as we used about thousand times before for the 32 bit version. Our first thought was that something had probably gone wrong when burning the DVD, but before wasting another DL-DVD that are quite expensive, we tested the ISO file within a virtual machine, and…. got the same error. 

  When we checked the image file (win7x64.wim) on the DVD we noticed that the displayed file size was listed as less than a megabyte, the image file we had added to the DVD had approx 4.8 GB. 

  After some searching we found out that the problem had to do with the large image file and the DVD that was created with the [Joliet File System](http://en.wikipedia.org/wiki/Joliet_(file_system)). 

  **Solution**

  To get our Restore DVD to work with a large image file, we used the **–u2** command line option with [OSCDIMG.EXE](http://technet.microsoft.com/en-us/library/cc749036(WS.10).aspx). Using the –u2 option instructs Oscdimg to use the [UDF file system](http://en.wikipedia.org/wiki/Universal_Disk_Format). 

  Thanks to Ted for finding this out. 

  The below relates to Windows XP and UDF, but might be useful to know as well. 

  [DVD-RW disks appear to be empty in Windows Explorer on a Windows XP Service Pack 2-based computer](http://support.microsoft.com/kb/899527)

  [CD-ROM Drive May Not Be Able to Read a UDF-Formatted Disc in Windows XP](http://support.microsoft.com/kb/321640)

