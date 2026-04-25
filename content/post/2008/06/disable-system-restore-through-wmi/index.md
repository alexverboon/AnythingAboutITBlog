---
title: "Disable System Restore through WMI"
layout: "post"
date: 2008-06-30T14:16:05Z
slug: "disable-system-restore-through-wmi"
aliases:
  - "/2008/06/disable-system-restore-through-wmi/"
description: "If you are sure about what you are doing and you want to speed up the installation of multiple security patches or applications, you can use the follo..."
author: "Alex Verboon"
tags:
  - script
categories:
  - automation
  - tip
---
If you are sure about what you are doing and you want to speed up the installation of multiple security patches or applications, you can use the following WMI command to disable Windows XP system restore.

on error resume next
set sr=GetObject("winmgmts:\\.\root\default:SystemRestore")
e=sr.disable("")

To turn on System Restore again, use the following command:

on error resume next
set sr=GetObject("winmgmts:\\.\root\default:SystemRestore")
e=sr.enable("")

