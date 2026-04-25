---
title: "Automating Regional settings configuration for Vista"
layout: "post"
date: 07/04/2008 19:24:34
slug: "automating-regional-settings-configuration-for-vista"
aliases:
  - "/2008/07/automating-regional-settings-configuration-for-vista/"
description: "In my earlier post \"[Automating Regional Settings configuration](https://www.verboon.info/?p=8)\" I described how to script the Regional Options settin..."
author: "Alex Verboon"
tags:
  - regional
  - vista
categories:
  - automation
  - deployment
  - tip
  - vista
---
In my earlier post "[Automating Regional Settings configuration](https://www.verboon.info/?p=8)" I described how to script the Regional Options settings for Windows XP using a rundll command. 

  For Windows Vista there is a similar trick using the following command:

  control intl.cpl,, /f:“filename.xml”

  Details on how to populate the filename.xml are documented on Microsoft Technet - [Guide to Windows Vista Multilingual User Interface](http://technet2.microsoft.com/WindowsVista/en/library/85e289ca-9fd8-4963-b06a-5ecc457006c71033.mspx?mfr=true).

