---
title: "No Battery Alarm Sound on Vista - it's by design"
layout: "post"
date: 2008-12-13T21:48:25Z
slug: "no-battery-alarm-sound-on-vista-its-by-design"
aliases:
  - "/2008/12/no-battery-alarm-sound-on-vista-its-by-design/"
description: "Early this year I bought a new laptop for my wife with Windows Vista Home Premium pre-installed, before she used a notebook with Windows XP. Since she..."
author: "Alex Verboon"
image: "img/post-heroes/no-battery-alarm-sound-on-vista-its-by-design.png"
categories:
  - 'Tips-Tools'
tags:
  - 'Battery'
  - 'Batterymeter'
---
Early this year I bought a new laptop for my wife with Windows Vista Home Premium pre-installed, before she used a notebook with Windows XP. Since she is using that new notebook, she is regularly complaining about Windows Vista just shutting down. Of course we could argue that people should read the messages they get such as the one below:

![](images/image-thumb7.png)

If Windows Vista would play a sound, people would probably pay more attention to it, but according to a Microsoft Knowledge base article [KB950161](http://support.microsoft.com/kb/950161/en-us). low and critical battery alarms do not sound on Windows Vista.

*This behavior is by design.

The "Low Battery Alarm" and "Critical Battery Alarm" options in "Sounds" are not used by the battery meter in Windows Vista.  These options exist for third-party battery meter applications.*

Okay, nice, here Microsoft has been kind enough to leave some market space for 3rd party software developers. I found a nice piece of software called [BatteryBar](http://vb.nitescifi.com/batterybar.html#), the name is self explaining, it adds an additional Toolbar component to the Windows Taskbar.

Note that BatteryBar does not use the Battery settings configured within the Windows Power Settings, but uses its own settings, that are stored in BatteryBar.Settings.xml. read the applications readme.txt for more information.

![](images/image-thumb8.png)


