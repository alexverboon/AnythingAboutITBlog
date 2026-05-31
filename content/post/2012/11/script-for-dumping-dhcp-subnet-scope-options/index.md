---
title: "Script for dumping DHCP subnet scope options"
layout: "post"
date: 2012-11-16T15:12:41Z
slug: "script-for-dumping-dhcp-subnet-scope-options"
aliases:
  - "/2012/11/script-for-dumping-dhcp-subnet-scope-options/"
description: "Here’s simple script I’ve put together as I was in need of one that dumps the DHCP subnet scope options into a text file. The script first queries the..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Scope-Options'
  - 'Dhcp'
---
Here’s simple script I’ve put together as I was in need of one that dumps the DHCP subnet scope options into a text file. 

  The script first queries the DHCP servers it can find and then dumps the scope options of each subnet it finds on each DHCP server. 

  Copy the below code and save it as dhcpsubnetscopeoptions.cmd

  @echo off

  echo %date% %time% >%~dp0\dhcpsubnetscopeoptions.txt

  echo ----------------------------------------------------------------- >>%~dp0\dhcpscopeoptions.txt

  Echo Dumping DHCP Subnet Scope options

  for /f "skip=2 tokens=4 delims=[] " %%G in ('netsh.exe dhcp show server') DO (call :sub1 %%G)

  :sub1

  set srv=%1

  for /f "skip=4 tokens=1 delims= " %%a in ('netsh.exe dhcp server %srv% show scope') DO (

  IF "%%a" == "Total" (echo.

  ) ELSE IF "%%a" == "Command" (echo.

  ) ELSE (netsh dhcp server %srv% scope %%a show optionvalue >>%~dp0\dhcpsubnetscopeoptions.txt

  )

  )

  Note that you must have appropriate rights such as DHCP Users, DHCP Administrators or Domain admin to retrieve the information. The output is saved into a file called dhcpsubnetoptions.txt

  The script has been tested on Windows 7 against a Windows 2008 DHCP Server.

