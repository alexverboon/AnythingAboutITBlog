---
title: "vPro colors in BIOS"
layout: "post"
date: 2008-09-26T19:48:16Z
slug: "vpro-colors-in-bios"
aliases:
  - "/2008/09/vpro-colors-in-bios/"
description: "When remotely accessing the system BIOS of a HP Compaq dc7800 desktop machine using vPro, the BIOS appears in black and white"
author: "Alex Verboon"
image: "img/post-heroes/vpro-colors-in-bios.png"
tags:
  - bios
  - vpro
categories:
  - Tips
---
When remotely accessing the system BIOS of a HP Compaq dc7800 desktop machine using vPro, the BIOS appears in black and white as shown in the picture below:


![image](images/image-thumb2.png)

to get the native BIOS colors you must configure the terminal emulator mode to ANSI

![image](images/image-thumb3.png)

then, the BIOS will appear with colors as if you were sitting in front of the physical machine.

![image](images/image6.png)

Thanks to Claude Henchoz for the hint.

