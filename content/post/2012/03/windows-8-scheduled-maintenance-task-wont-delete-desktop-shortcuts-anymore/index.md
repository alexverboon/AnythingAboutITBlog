---
title: "Windows 8 &ndash; Scheduled Maintenance Task won&rsquo;t delete Desktop Shortcuts anymore"
layout: "post"
date: 2012-03-10T20:28:04Z
slug: "windows-8-scheduled-maintenance-task-wont-delete-desktop-shortcuts-anymore"
aliases:
  - "/2012/03/windows-8-scheduled-maintenance-task-wont-delete-desktop-shortcuts-anymore/"
description: "On Windows 7 many users suffer from disappearing shortcuts on their desktop. I wrote about this in [Control Windows 7 Scheduled Maintenance Behavior T..."
author: "Alex Verboon"
tags:
  - broken-shortcuts
  - scheduled-task
  - system-maintenance
  - troubleshooting
  - Windows
categories:
  - Windows
---
On Windows 7 many users suffer from disappearing shortcuts on their desktop. I wrote about this in [Control Windows 7 Scheduled Maintenance Behavior Through Group Policy](https://www.verboon.info/index.php/2010/11/control-windows-7-scheduled-maintenance-behavior-through-group-policy/). On Windows 8 this shouldn’t happen anymore, since Microsoft has removed the related scripts and Tasks from the Diagnosis troubleshooting pack (DiagPackage.diagpkg)

  The following files have been removed from the C:\Windows\diagnostics\scheduled\Maintenance folder:

     
- RS_RemoveShortcuts.ps1    
- RS_RemoveUnusedDesktopIcons.ps1    
- TS_BrokenShortcuts.ps1    
- TS_UnusedDesktopIcons.ps1

