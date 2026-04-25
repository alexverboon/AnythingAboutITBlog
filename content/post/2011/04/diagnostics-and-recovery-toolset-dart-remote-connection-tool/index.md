---
title: "Diagnostics and Recovery Toolset (DART) Remote Connection Tool"
layout: "post"
date: 2011-04-28T20:07:58Z
slug: "diagnostics-and-recovery-toolset-dart-remote-connection-tool"
aliases:
  - "/2011/04/diagnostics-and-recovery-toolset-dart-remote-connection-tool/"
description: "Just a few weeks ago Microsoft released a public Beta version of the Diagnostics and Recovery Toolset (DART) 7. One of the new features of DART7 is th..."
author: "Alex Verboon"
image: "img/post-heroes/diagnostics-and-recovery-toolset-dart-remote-connection-tool.png"
tags:
  - dart
  - dart-7
  - diagnostics-and-recovery-toolset
  - mdop
  - pxe
  - remote-control
  - usb
  - windws-7
  - Windows
  - WinPE
categories:
  - dart
  - Windows
  - WinPE
---
Just a few weeks ago Microsoft released a public Beta version of the Diagnostics and Recovery Toolset (DART) 7. One of the new features of DART7 is the Remote Connection Tool. Okay, I agree this is not rocked science, actually I’ve written about this before [using a VNC client](https://www.verboon.info/index.php/2009/12/remote-management-of-amtvpro-machine-with-winpe-and-vnc/comment-page-1/#comment-249), but now that it is included within the tool suite, it’s just there and ready to use. 

  Let’s have a look how this works. On the client side we boot the client into DART, this can be either from a DVD, USB, from the [local disk](https://www.verboon.info/index.php/2010/11/adding-microsoft-diagnostics-and-recovery-toolset-dart-to-your-windows-7-boot-menu/) or PXE boot. Note that when creating the DART media you must include additional network drivers for the clients you use, unless already supported by the out-of-the-box drivers included within PE. 

              1[           

![2011-04-28 21h22_21](images/2011-04-28-21h22_21_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-28-21h22_21.png)        2[           

![2011-04-28 21h22_54](images/2011-04-28-21h22_54_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-28-21h22_54.png)                  3         
[
![2011-04-28 21h23_30](images/2011-04-28-21h23_30_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-28-21h23_30.png)        4         
[
![2011-04-28 21h24_56](images/2011-04-28-21h24_56_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-28-21h24_56.png)          Once the Remote Connection tool has started, the DART Remote Connection Viewer must be launched. After entering the Ticket Number, IP Address and Port number a remote connection can be established. 

              5         
[
![2011-04-28 21h26_15](images/2011-04-28-21h26_15_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-28-21h26_15.png)          
        6         
[
![2011-04-28 21h27_48](images/2011-04-28-21h27_48_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-28-21h27_48.png)          According to a [blog post](http://windowsteamblog.com/windows/b/business/archive/2011/04/04/management-and-security-enhancements-for-enterprise-customers-with-dart-and-mbam.aspx) on Windows for your Business DART7 is planned to be made available in Q3 2011.

