---
title: "Adding Games on Windows 7 Enterprise"
layout: "post"
date: 2009-08-09T18:35:35Z
slug: "adding-games-on-windows-7-enterprise"
aliases:
  - "/2009/08/adding-games-on-windows-7-enterprise/"
description: "When you run a default Windows 7 Enterprise installation, you will notice that by default no games are being installed. System administrators using th..."
author: "Alex Verboon"
tags:
  - configuration
  - dism
  - features
  - games
  - windows-7
categories:
  - deployment
  - tip
  - tools
  - windows-7
  - windows7
---
When you run a default Windows 7 Enterprise installation, you will notice that by default no games are being installed. System administrators using the Windows Automated Installation Toolkit can use the image manager to enable games within their customized Windows 7 Enterprise installation, but here’s another trick how you can get the games enabled. 

  Open a command prompt with elevated Administrative privileges and execute the following command:

  dism /online /enable-feature /featurename:InboxGames

  when completed, you should see all the default games appear within the Start Menu. To disable the games, simply run the following command:

  dism /online /disable-feature /featurename:InboxGames

  This was just an example with games. Run DISM /Online /get-features | more to find other features you can enable or disable.

