---
title: "Vista SP1 download using BITSADMIN"
layout: "post"
date: 11/23/2008 14:57:52
slug: "vista-sp1-download-using-bitsadmin"
aliases:
  - "/2008/11/vista-sp1-download-using-bitsadmin/"
description: "I wrote about [BITSADMIN ](https://www.verboon.info/?p=78)earlier, use the below command line to directly download Vista SP1. Note that you have to cr..."
author: "Alex Verboon"
tags:
  - service-pack-1
  - vista
  - windows-vista
categories:
  - automation
  - tip
  - vista
---
I wrote about [BITSADMIN ](https://www.verboon.info/?p=78)earlier, use the below command line to directly download Vista SP1. Note that you have to create the c;\download folder yourself or define an other path.

BITSADMIN /TRANSFER VSP1 [http://download.microsoft.com/download/3/a/9/3a9b72c2-527d-4694-8a49-84c056d4c34d/Windows6.0-KB936330-X86-wave0.exe](http://download.microsoft.com/download/3/a/9/3a9b72c2-527d-4694-8a49-84c056d4c34d/Windows6.0-KB936330-X86-wave0.exe) C:\DOWNLOAD\Windows6.0-KB936330-X86-wave0.exe

