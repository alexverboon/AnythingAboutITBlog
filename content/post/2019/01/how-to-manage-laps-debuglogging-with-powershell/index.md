---
title: How to manage LAPS DebugLogging with PowerShell
layout: post
date: '2019-01-14T19:10:39Z'
slug: how-to-manage-laps-debuglogging-with-powershell
aliases:
- /2019/01/how-to-manage-laps-debuglogging-with-powershell/
description: If you need to troubleshoot the Local Administrator Password Solution
  (LAPS) you can configure how much information is written into the Windows Event
  log.
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'LAPS'
---
If you need to troubleshoot the Local Administrator Password Solution **LAPS **you can configure how much information is written into the Windows Event log.

Logging options are set through the following REG_DWORD values described below under:

HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GPExtensions\{D76B9641-3288-4f75-942D-087DE603E3EA}\ExtensionDebugLevel

**Value**
  **Meaning**

  **0**

  Silent mode; log errors only
  When no error occurs, no information is logged about CSE activity
  This is a default value

  **1**

  Log Errors and
  warnings

  **2**

  Verbose mode, log everything


Becasue navigating manually through the registry and modifying registry keys is a bit of a pain, I wrote two PowerShell cmdlets.

The **Get-LAPSLoggingMode** cmdlet retrieves the current LAPS logging configuration, **Set-LAPSLoggingmode** allows you to configure the LAPS logging configuration.

I used the PowerShell function template described here https://jdhitsolutions.com/blog/powershell/6348/building-more-powershell-functions/ and extended the concept to use custom parameters and added some additional logic to allow running the functions remotely and locally. Since not everyone has WinRM enabled, the functions can be used on the local machine without WinRM enabled.

**Get-LAPSLoggingMode**

**Set-LAPSLoggingMode**

Cheers and happy logging


