---
title: "Putting drive letters first"
layout: "post"
date: 2008-07-01T09:42:01Z
slug: "putting-drive-letters-first"
aliases:
  - "/2008/07/putting-drive-letters-first/"
description: "Putting drive letters first"
author: "Alex Verboon"
image: "img/post-heroes/putting-drive-letters-first.png"
categories:
  - 'Windows'
tags:
  - 'Registry'
  - 'Tips-Tools'
---
When launching Windows Explorer, by default the driver letters are being displayed behind the volume / share name.

![explorer](images/explorer11.jpg)

Some people, like myself don't find this very convenient and want to see the drive letters in front of the volume / share description.  This can be customized by applying the following registry key:

```vb
Reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer /v ShowDriveLettersFirst /t REG_DWORD /d 0x4 /f
```

![Explorer](images/explorer2.jpg)


