---
title: "How to detect if Windows Touch is enabled"
layout: "post"
date: 2012-12-20T19:15:54Z
slug: "how-to-detect-if-windows-touch-is-enabled"
aliases:
  - "/2012/12/how-to-detect-if-windows-touch-is-enabled/"
description: "How to detect whether Windows Touch is enabled using MDT tooling and a lightweight check."
author: "Alex Verboon"
image: "img/post-heroes/how-to-detect-if-windows-touch-is-enabled.png"
categories:
  - 'Windows'
tags:
  - 'Detect'
  - 'Istouchenabled-Exe'
---
While I was actually looking for something totally different, I stumbled on `IsTouchEnabled.exe`, which is stored in the MDT 2012 `\Tools\OSDResults` folder. The name says it all: it detects whether the device supports touch or not.

I copied the utility and ran it on a Samsung tablet with Windows 7, an HP workstation with Windows 7, an HP mobile workstation with Windows 8, and an HP ElitePad with Windows 8. On both tablet devices, the utility correctly detected touch support.

![image](images/image_thumb1.png)

If you run into a scenario where behavior should differ based on touch capability, `IsTouchEnabled.exe` can be useful.

Example batch script:

```bat
@echo off
for /f "delims=" %%a in ('IsTouchEnabled.exe') do set Touch=%%a
if "%Touch%"=="1" (
  echo Touch is enabled
  rem run your code here
) else (
  echo Touch is not enabled
  rem run your code here
)
pause
```


