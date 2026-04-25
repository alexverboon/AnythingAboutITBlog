---
title: "ToolTip: Boxcutter &ndash; A Command line screenshot utility"
layout: "post"
date: 2011-11-08T22:57:10Z
slug: "tooltip-boxcutter-a-command-line-screenshot-utility"
aliases:
  - "/2011/11/tooltip-boxcutter-a-command-line-screenshot-utility/"
description: "Boxcutter is a simple command line-driven screenshot program for Microsoft Windows. Below you find a short script I wrote that will take a screenshot ..."
author: "Alex Verboon"
tags:
  - bmp
  - boxcutter
  - command-line
  - png
  - screen-capture
  - screenshot
  - script
categories:
  - screencapture
  - tip
  - tools
---
Boxcutter is a simple command line-driven screenshot program for Microsoft Windows. Below you find a short script I wrote that will take a screenshot of the full screen every 20 seconds until 100 screenshots are saved. 

  One usage scenario (I plan to use) is where you are running an OS installation within a Virtual Machine and want to take screenshots of the various stages of the installation without having to manually take a screenshot. You would just let the script run, it will probably produce more screenshots as needed, but these then can be deleted manually afterwards. 

  @echo off     
:: ----------------------------------------------     
:: seconds to wait until taking next screenshot      
set waitsecs=20      
:: maximum # of screenshots that will be taken      
set maxcapture=100      
:: ---------------------------------------------

  set start=0     
:CAPTURE

  :: first prepare the filename using date and time string, cut off fractional seconds and replace      
:: colons with dashes     
set t=%time:~0,8%      
set t=%t::=-%      
set FileName=capture-%date%-%t%

  :: Capture fullscreen     
boxcutter.exe -f %FileName%.png      
timeout %waitsecs%      
set /A count=start+1      
set start=%count%      
if %count% gtr %maxcapture% GOTO :END      
GOTO :CAPTURE

  :END     
Echo Screen Capture batch process completed.      
pause

  Boxcutter is **FREE** and can be downloaded from Matthew D. Rasmussen’s website [here](http://keepnote.org/boxcutter/)

