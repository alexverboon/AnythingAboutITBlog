---
title: "PSExec launch script"
layout: "post"
date: 2011-05-11T15:10:32Z
slug: "psexec-launch-script"
aliases:
  - "/2011/05/psexec-launch-script/"
description: "Tired of typing the psexec command with all the command line options? Here’s a short PsExec launch script I wrote today. Using this allows you to just..."
author: "Alex Verboon"
tags:
  - process
  - psexec-2
  - pstools-2
  - remote
  - tip
  - tools
categories:
  - psexec
  - pstools
  - tip
  - tools
---
Tired of typing the psexec command with all the command line options? Here’s a short PsExec launch script I wrote today. Using this allows you to just type the remote computer’s computer name or IP address and then launches the command prompt. 

  @echo off     
Echo

  SET user= *ADD USERNAME HERE       
*SET pwd= *ADD PASSWORD HERE*

  :START     
SET /P Node=Computername or IP Address:       
IF "%node%"=="" GOTO :START

  Echo.     
Echo Starting PSEXEC on %node%      
Echo.      
psexec -u %user% -p %pwd% \\%node% cmd

  PSExec which is part of the Sysinternals PsTools suite can be downloaded from [here](http://technet.microsoft.com/en-us/sysinternals/bb896649)

