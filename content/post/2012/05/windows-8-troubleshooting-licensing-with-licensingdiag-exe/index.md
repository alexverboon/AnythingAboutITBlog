---
title: "Windows 8 - Troubleshooting Licensing with licensingdiag.exe"
layout: "post"
date: 05/14/2012 19:32:05
slug: "windows-8-troubleshooting-licensing-with-licensingdiag-exe"
aliases:
  - "/2012/05/windows-8-troubleshooting-licensing-with-licensingdiag-exe/"
description: "Should you encounter problems with activating Windows 8 or Server 2012 then have a look at the new added command-line tool **licensingdiag.exe**. To r..."
author: "Alex Verboon"
tags:
  - command-line
  - licensing
  - licensingdiag-exe
  - server-2012
  - troubleshooting
  - windows-8
categories:
  - licensing
  - windows-8
---
Should you encounter problems with activating Windows 8 or Server 2012 then have a look at the new added command-line tool **licensingdiag.exe**.

  To run licensingdiag.exe open a command prompt and enter the following command:

  licensingdiag.exe -report c:\data\licensing\licenserep.xml -log c:\data\licensing\license.cab    

  This will create a log file and a CAB file. The log file is an XML type file that contains various information about the client, the OS and its licensing status. The CAB file contains a copy of the log file, a file called tokenstore.dat (I was unable to find any information about its purpose) and a Diagevents.evtx that contains a dump of License related events and can be opened using Eventviewer.

