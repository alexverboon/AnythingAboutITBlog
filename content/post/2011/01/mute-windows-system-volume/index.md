---
title: "Mute Windows System Volume"
layout: "post"
date: 2011-01-15T17:46:36Z
slug: "mute-windows-system-volume"
aliases:
  - "/2011/01/mute-windows-system-volume/"
description: "I came across a forum post where someone asked how to programmatically mute the Windows System volume. So this is what I have found: [ ![image](images..."
author: "Alex Verboon"
image: "img/post-heroes/mute-windows-system-volume.png"
tags:
  - mute
  - script
  - unmute
  - volume
  - Windows
categories:
  - scripting
  - tip
  - tools
  - volume
---
I came across a forum post where someone asked how to programmatically mute the Windows System volume. So this is what I have found: 

  [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2011/01/image1.png)

  **NirCmd**

  [NirCmd](http://www.nirsoft.net/utils/nircmd.html) from NirSoft is a small command-line utility that contains many smart functions like muting and unmuting the system volume. 

  To mute the system volume, simply run the following command

  nircmd.exe mutesysvolume 1 

  and to unmute you run 

  nircmd.exe mutesysvolume 0 

  **With VBScript**

  Another option is to use a VBscript, the following code I found [here](http://www.nilpo.com/2008/11/windows-xp/mute-sound-volume-in-wsh/) will mute or unmute the system volume

  Set WshShell = CreateObject("WScript.Shell")   
WshShell.SendKeys(chr(&hAD))

  **SndVolPlus**

  Although it doesn’t allow to automate muting the volume, SndVolPlus is a nice replacement utility for the default volume control in Windows.  SndVolPlus can do everything the standard volume control does, but also allows you to mute / unmute the volume by just double clicking on the volume icon. SndVolPlus can be downloaded from [here](http://factormystic.net/projects/apps/sndvolplus)

