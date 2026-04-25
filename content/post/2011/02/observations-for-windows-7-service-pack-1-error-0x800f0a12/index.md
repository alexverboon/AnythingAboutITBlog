---
title: "Observations for Windows 7 Service Pack 1 Error 0x800f0a12"
layout: "post"
date: 02/24/2011 19:02:38
slug: "observations-for-windows-7-service-pack-1-error-0x800f0a12"
aliases:
  - "/2011/02/observations-for-windows-7-service-pack-1-error-0x800f0a12/"
description: "During the past days I have been manually updating a few Windows 7 clients and on two of them I received the error **0x800fa12**. [ ![2011-02-24 11h26..."
author: "Alex Verboon"
image: "img/post-heroes/observations-for-windows-7-service-pack-1-error-0x800f0a12.png"
tags:
  - 0x800f0a12
  - error
  - service-pack-1
  - windws-7
categories:
  - servicepack
  - windows7
---
During the past days I have been manually updating a few Windows 7 clients and on two of them I received the error **0x800fa12**. 

  [
![2011-02-24 11h26_01](images/2011-02-24-11h26_01_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-24-11h26_01.png)

  When clicking on the Go online [link](http://windows.microsoft.com/en-US/windows7/windows-7-windows-server-2008-r2-service-pack-1-sp1-installation-error-0x800F0A12) Microsoft mentions the several reasons that could lead to this error. 

     
-      The system partition isn’t automatically mounted, or made accessible to Windows, during startup. 

       
-      A hard disk containing the system partition was removed prior to beginning SP1 installation.

       
-      Windows is running on a storage area network (SAN), and access to the system partition has been disabled. 

       
-      A disk management tool from another software manufacturer was used to copy (or clone) the disk or partition on which you’re trying to install SP1

    

  Knowing my systems I could immediately exclude cause 2,3 and 4, so took a closer look at cause 1. Running the command MOUNTVOL /L showed the following result: 

  [
![2011-02-24 11h26_19](images/2011-02-24-11h26_19_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-24-11h26_19.png)

  I than ran DISKPART and got the following result. In fact the 100MB sized System Partition was Offline. 

  [
![2011-02-24 11h26_10](images/2011-02-24-11h26_10_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-24-11h26_10.png)

  as per Microsoft’s recommendation I then executed MOUNTVOL /E which re-enables automatic mounting of new volumes and then rebooted the system. Once rebooted I executed MOUNTVOL again and got the following result. 

  [
![2011-02-24 11h31_31](images/2011-02-24-11h31_31_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-24-11h31_31.png)

  When executing DISKPART the results were as following: 

  [
![2011-02-24 11h32_06](images/2011-02-24-11h32_06_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-24-11h32_06.png)

  When Launching the Service Pack 1 installer again no issues were detected and installation could continue. 

  [
![2011-02-24 11h33_53](images/2011-02-24-11h33_53_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-24-11h33_53.png)

  Why this actually happened I don’t know. Windows 7 by default has the automount feature enabled. The current status of automount can be checked by looking at the following registry key. 

  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MountMgr\NoAutoMount

  If the value is set to 1: This indicates that Automatic mounting of new volumes is Disabled. If the value is set to 0: This indicates that Automatic mounting of new volumes is Enabled.

  Additional information on this issue can be found [here](http://blogs.technet.com/b/joscon/archive/2011/02/17/windows-7-2008-r2-service-pack-1-fails-with-0x800f0a12.aspx).

