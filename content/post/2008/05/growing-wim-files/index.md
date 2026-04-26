---
title: "Growing WIM files"
layout: "post"
date: 2008-05-10T09:36:00Z
slug: "growing-wim-files"
aliases:
  - "/2008/05/growing-wim-files/"
description: "You might have experienced that your WIM files seem to grow in size when editing the image. Of course it does, because you add content, but what if yo..."
author: "Alex Verboon"
tags:
  - virtual
  - wim
categories:
  - virtualization
---
You might have experienced that your WIM files seem to grow in size when editing the image. Of course it does, because you add content, but what if you replace files.. well it still grows, exactly by the size of the file(s) you replace. So when replacing larger content within your WIM images they might become bigger as you want.To get the WIM file resized simply perform an export by using imagex.exe.

