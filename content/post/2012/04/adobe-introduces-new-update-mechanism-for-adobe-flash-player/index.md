---
title: "Adobe introduces new Update Mechanism for Adobe Flash Player"
layout: "post"
date: 2012-04-02T22:54:32Z
slug: "adobe-introduces-new-update-mechanism-for-adobe-flash-player"
aliases:
  - "/2012/04/adobe-introduces-new-update-mechanism-for-adobe-flash-player/"
description: "A few days ago Adobe released a [security update](http://www.adobe.com/support/security/bulletins/apsb12-07.html) for Adobe Flash player and with that..."
author: "Alex Verboon"
categories:
  - 'Security'
tags:
  - 'Flash-Player'
  - 'Update'
---
A few days ago Adobe released a [security update](http://www.adobe.com/support/security/bulletins/apsb12-07.html) for Adobe Flash player and with that update Adobe also introduced a new mechanism for Flash Player updates. When deploying Adobe Flash player within a controlled corporate environment you most likely want to prevent the player from automatically updating itself or show notifications about a new version being available.

  When installing Adobe Flash Player 11.2 you will find the following:


- A new Scheduled Task called Adobe Flash Player Updater
- A new Service called Adobe Flash Player Update Service
- The mms.cfg file located in C:\Windows\System32\Macromed\Flash on 32-Bit systems or C:\Windows\SysWOW64\Macromed\Flash on 64-Bit systems.

  The mms.cfg isn’t a new thing, as it was actually already a common practice for Enterprise Administrators to deploy this file to prevent automatic updates, but it wasn’t installed by default, which is the case now.

  Now I don’t have to rewrite in detail what others have already written, so to learn more about the new Adobe Flash Player Background Updater for Windows [read this article](http://www.adobe.com/devnet/flashplayer/articles/background-updater-windows.html).

  Note that the mms.cfg file cannot only be used for configuring update behavior but also allows configuring other flash player settings. For more detail read the Adobe Flash Player [Administrator Guide](http://www.adobe.com/devnet/flashplayer/articles/flash_player_admin_guide.html) Page 21 - Summary of mms.cfg options.


