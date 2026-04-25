---
title: "Windows To Go Startup Options"
layout: "post"
date: 2012-10-28T16:26:35Z
slug: "windows-to-go-startup-options"
aliases:
  - "/2012/10/windows-to-go-startup-options/"
description: "Windows To Go is another new feature introduced with Windows 8 but only available to users that run Windows 8 Enterprise. With Windows To Go users can..."
author: "Alex Verboon"
image: "img/post-heroes/windows-to-go-startup-options.png"
tags:
  - bootloader
  - bootnxt
  - boottgt
  - startup-options
  - usb
  - windows-8
  - windows-8-to-go
  - workspace
categories:
  - windows-8
---
Windows To Go is another new feature introduced with Windows 8 but only available to users that run Windows 8 Enterprise. With Windows To Go users can create a Windows 8 workspace that can be booted from a USB drive. So simply said with Windows To Go, there’s no need to carry around a laptop if you’re going somewhere. If you have your Windows To Go workspace stored on a compatible USB drive, you can just boot your Windows 8 from any device that meets the Windows 7/8 hardware requirements. 

  The configuration steps required to boot from USB depends on what operating system is installed on the physical system. If the system is running an earlier version of the Windows operating system such as Windows 7, the boot order in the BIOS must be configured so that USB devices are set before the local disk. 

  On computers running Windows 8 there is no need for going into the BIOS because the configuration can be set using the Windows To Go Startup Options. 

  The startup options can be accessed by just entering the word “startup” on the Windows Start Menu

  [
![clip_image002](images/clip_image002_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0021.jpg)

  Or for those who intend to create a desktop shortcut use   
 C:\Windows\system32\rundll32.exe pwlauncher.dll,ShowPortableWorkspaceLauncherConfigurationUX

  [
![clip_image004](images/clip_image004_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0041.jpg)

  And of course there’s also a command-line version pwlauncher.exe

  With pwlauncher.exe we can check and configure the startup options. 

  [
![clip_image006](images/clip_image006_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0061.jpg)

  On a default Windows 8 client, startup options are not configured. 

  [
![clip_image008](images/clip_image008_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0081.jpg)

  To configure the startup option run pwlauncher.exe /enable

  [
![clip_image010](images/clip_image010_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0101.jpg)

  I wanted to understand how and where Windows actually stores the configuration so configured [Sysinternal’s Process Monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx) and configured it to watch pwlauncher.exe. 

  [
![clip_image012](images/clip_image012_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0121.jpg)

  When executing pwlauncher /enable process monitor captures a lot of registry and file system actions. The registry actions however are just limited to query actions e.g. reading information, but no write actions. The file system actions however showed some file writing actions. 

  [
![clip_image014](images/clip_image014_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0141.jpg)

  [
![clip_image016](images/clip_image016_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image0161.jpg)

  [
![clip_image018](images/clip_image018_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/10/clip_image018.jpg)

  When enabling the startup options, Windows updates the file BOOTNXT and creates a new file BOOTTGT. 

  When disabling the startup options, Windows again updates the file BOOTNXT and deletes the file BOOTTGT

  Additional Information

  [Windows To Go step by step](http://social.technet.microsoft.com/wiki/contents/articles/6991.windows-to-go-step-by-step-en-us.aspx?PageIndex=3)    
[Get up and go! Windows To Go, that is….](http://blogs.technet.com/b/canitpro/archive/2012/10/26/get-up-and-go-windows-to-go-that-is.aspx)    
[Windows To Go Frequently Asked Questions](http://technet.microsoft.com/en-us/library/jj592680.aspx#wtg_faq_whatis)

