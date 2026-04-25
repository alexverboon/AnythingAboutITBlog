---
title: "Windows Services, what changed from Vista to Windows7 Part1"
layout: "post"
date: 04/21/2009 23:34:52
slug: "windows-services-what-changed-from-vista-to-windows7-part1"
aliases:
  - "/2009/04/windows-services-what-changed-from-vista-to-windows7-part1/"
description: "Today I took a closer look at the Windows Services running on Windows7. A lot of the performance improvements with Windows7 are related to the way how..."
author: "Alex Verboon"
tags:
  - services
  - startmode
  - windows-vista
categories:
  - hyper-v
  - knowledge
  - vista
  - windows-7
---
Today I took a closer look at the Windows Services running on Windows7. A lot of the performance improvements with Windows7 are related to the way how and when services are being loaded so i thought it’s worth to see what’s happening there. 

  I first installed a Windows 7 build 7077 and a Windows Vista SP1 client on my Hyper-V server. Because I am primarily interested in what’s happening in an enterprise environment, both clients were joined to a domain. 

  To obtain the services data from each system, i executed the following PowerShell command: 

  gwmi win32_service | select Displayname, Started, StartMode, State  | format-table | out-file c:\data\services.txt

  I then imported the data in excel and then the painful work actually started… :-), comparing…. I compared the services that were installed including the start mode and current state. I will talk more about the start mode in [Part2](https://www.verboon.info/index.php/2009/04/windows-services-what-changed-from-vista-to-windows7-part2/).

  **New Services / New Default Services**

     
- Application Identity     
- ActiveX Installer (AxInstSV)     
- BitLocker Drive Encryption...     
- Bluetooth Support Service     
- Disk Defragmenter     
- Encrypting File System (EFS)     
- Windows Media Center Recei...     
- Windows Media Center Sched...     
- Fax     
- HomeGroup Provider     
- Media Center Extender Service     
- BranchCache     
- Power     
- RPC Endpoint Mapper     
- Adaptive Brightness     
- Software Protection     
- SPP Notification Service     
- Storage Service     
- Credential Manager     
- Windows Biometric Service     
- Parental Controls     
- WWAN AutoConfig  

  Some of the above services are available in Vista as well, but aren’t installed by default. 

  **Renamed**

  It looks like all “Terminal Service…” type Services  are now called Remote Desktop…..”

  **Removed***

  The below Services exist on Vista, but I haven’t seen them on Windows7.

     
- removed     
- DFS Replication     
- ReadyBoost     
- Software Licensing     
- SL UI Notification Service     
- Microsoft Software Shadow ...  

  * well possible that some of the above “removed” services have been renamed or integrated within the above “new” services. 

  Read [Part 2](https://www.verboon.info/index.php/2009/04/windows-services-what-changed-from-vista-to-windows7-part2/)

