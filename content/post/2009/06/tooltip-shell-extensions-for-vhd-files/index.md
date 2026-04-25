---
title: "ToolTip &ndash; Shell extensions for VHD files"
layout: "post"
date: 2009-06-21T12:16:23Z
slug: "tooltip-shell-extensions-for-vhd-files"
aliases:
  - "/2009/06/tooltip-shell-extensions-for-vhd-files/"
description: "If you are running a Hyper-V server, this is something you want to look at. The [VHDShellExt.VBS](http://code.msdn.microsoft.com/VHDShellExt) extends ..."
author: "Alex Verboon"
tags:
  - shell-extension
  - tool
  - vhd
  - Windows
categories:
  - hyper-v
  - virtualization
  - windows-server-2008
---
If you are running a Hyper-V server, this is something you want to look at. The [VHDShellExt.VBS](http://code.msdn.microsoft.com/VHDShellExt) extends the explorer context menu for VHD files with the following functions. 

  ![VHD Shell Extensions context menu](http://www.ravichaganti.com/blog/wp-content/uploads/2009/06/Menu.jpg)

  Download the script from MSDN Code Gallery and run cscript.exe VHDShellExt.vbs /action:setup for installation. More [documentation](http://www.ravichaganti.com/blog/?p=592#more-592) can be found on Ravikanth’s site.

