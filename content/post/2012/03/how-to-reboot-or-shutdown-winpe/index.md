---
title: How to Reboot or Shutdown WinPE
layout: post
date: '2012-03-28T20:03:11Z'
slug: how-to-reboot-or-shutdown-winpe
aliases:
- /2012/03/how-to-reboot-or-shutdown-winpe/
description: Windows XP, Windows Vista, Windows 7 and Windows 8 include the shutdown.exe
  command-line tool that can be used for shutting down or rebooting a system...
author: Alex Verboon
categories:
  - 'Tips-Tools'
tags:
  - 'Reboot'
  - 'Shutdown'
---
Windows XP, Windows Vista, Windows 7 and Windows 8 include the shutdown.exe command-line tool that can be used for shutting down or rebooting a system within a script or just from the command prompt. WinPE however is only a minimal operating system primarily designed to act as a preinstallation or recovery environment.

  To keep the footprint of WinPE as small as possible many services or tools usually found within a full Windows installation are not available within WinPE. The same applies for the shutdown.exe command. 

  So how to shutdown or reboot WinPE from the command prompt? WinPE does have a number of command-line tools included and one of them is Wpeutil providing various commands. 

  To shutdown a WinPE session run:

  wpeutil shutdown

  To Reboot a WinPE session run:

  wpeutil reboot

  More details on the WinPE command-line tools can be found [here](http://technet.microsoft.com/en-us/library/dd799280(v=ws.10).aspx)

