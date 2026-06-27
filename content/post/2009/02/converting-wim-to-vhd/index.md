---
title: "Converting WIM to VHD"
layout: "post"
date: 2009-02-15T14:35:12Z
slug: "converting-wim-to-vhd"
aliases:
  - "/2009/02/converting-wim-to-vhd/"
description: "Today I've tested the WIM2VHD script provided by [Mike Kolitz](http://blogs.msdn.com/mikekol/default.aspx) a Software Design Engineer from the Hyper-V..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Convert'
  - 'Vhd'
---
Today I've tested the WIM2VHD script provided by [Mike Kolitz](http://blogs.msdn.com/mikekol/default.aspx) a Software Design Engineer from the Hyper-V Team at Microsoft.

In short, the script allows you to create a bootable VHD file directly from Windows 7 installation media, so you don't need to go through the whole Windows Installation process. Once the VHD is completed, you can move it directly into your Hyper-V System and boot the operating system.

Detailed information about the script can found on the MSDN Code Gallery - [Windows(R) Image to Virtual Hard Disk (WIM2VHD) Converter](http://code.msdn.microsoft.com/wim2vhd).
Note that you must have the [Windows 7 AIK](http://www.microsoft.com/downloadS/info.aspx?na=40&p=1&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=f1bae135-4190-4d7c-b193-19123141edaa&u=http%3a%2f%2fdownload.microsoft.com%2fdownload%2fD%2f1%2f4%2fD14C40CA-CAED-4B49-B9CF-8B07D8BA344F%2fKB3AIK_EN.iso) installed to run this script. The script provides a lot of optional command line options, the shortest with using all default settings is as following:

cscript wim2vhd.wsf /wim:d:\sources\install.wim /sku:ULTIMATE

If you don't feel like trying it out yourself but want to see how things are working, watch the video below.


