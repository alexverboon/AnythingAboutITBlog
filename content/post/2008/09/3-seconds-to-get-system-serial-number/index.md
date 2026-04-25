---
title: "3 seconds to get system serial number"
layout: "post"
date: 09/10/2008 15:30:21
slug: "3-seconds-to-get-system-serial-number"
aliases:
  - "/2008/09/3-seconds-to-get-system-serial-number/"
description: "Okay, depends on how fast you can type. Start a command prompt and enter the following command: wmic csproduct get identifyingnumber,vendor,name In si..."
author: "Alex Verboon"
tags:
  - wmi
categories:
  - tip
---
Okay, depends on how fast you can type. Start a command prompt and enter the following command:

wmic csproduct get identifyingnumber,vendor,name

In simple words, wmic is a WMI commandline tool. It's around since XP if i am right, but there hasn't been much documentation for it:

Some references here:

[http://technet.microsoft.com/en-us/library/bb742610.aspx](http://technet.microsoft.com/en-us/library/bb742610.aspx)
[http://msdn.microsoft.com/en-us/library/aa394531.aspx](http://msdn.microsoft.com/en-us/library/aa394531.aspx)

