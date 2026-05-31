---
title: Reducing size of WinPE
layout: post
date: '2009-01-17T13:23:35Z'
slug: reducing-size-of-winpe
aliases:
- /2009/01/reducing-size-of-winpe/
description: Today I have been looking into the new "Profiling" options for Windows
  PE 3.0. Using the profiling options allow you to reduce the content of Windows ...
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'Winpe'
  - 'Automation'
---
Today I have been looking into the new "Profiling" options for Windows PE 3.0. Using the profiling options allow you to reduce the content of Windows PE to an absolute minimum without removing any boot critical content.

I am not going to re-write a step by step process here, as it is all described within the Windows PE User Guide for Windows 7 but here are the basic things

	
- First build your PE boot.wim the way you have been doing it so far, but before unmounting it run the following command as well: dism /image:C:\PE\mount /Enable-profiling

	
- Then boot your PE and start doing all the things you will need in the future as well. Just a hint, if you intend to run the ipconfig command, you must run it now, otherwise it won't be there anymore when you apply the profile.
	
- Once you have launched all commands and done whatever you want to do, run the following command: wpeutil saveprofile e:\Optimize_Profile.txt "Image Optimization Profile"

*(drive e: is a connected USB stick so that you can copy away the profile file, you will need it later).*  
	
- Finally rebuild your PE boot.wim, with the command  dism /image:C:\PEHD\mount /Apply-Profiles:c:\optimize_profile.txt and then commit the changes.  Note that you do not need to run dism ...../Enable Profiling again here.

The results:

	
- The first boot.wim was 128 MB in size, a nearly standard boot.wim with some packages added.
	
- The optimized boot.wim was 62 MB in size.

Happy PE shrinking !

