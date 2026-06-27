---
title: "Quick Access to installed QFEs"
layout: "post"
date: 2009-09-23T20:20:03Z
slug: "quick-access-to-installed-qfes"
aliases:
  - "/2009/09/quick-access-to-installed-qfes/"
description: "Instead of opening several windows, here’s an easy way to get a list of installed QFE’s. simply open a command prompt and type: **WMIC QFE ** or **WMI..."
author: "Alex Verboon"
image: "img/post-heroes/quick-access-to-installed-qfes.png"
categories:
  - 'Security'
tags:
  - 'Qfe'
  - 'Windows'
---
Instead of opening several windows, here’s an easy way to get a list of installed QFE’s. simply open a command prompt and type:

  **WMIC QFE **

  or

  **WMIC QFE get caption,hotfixid,installedon**

  ![image](images/image_thumb10.png)

  or if you are looking for a specific update, enter the following command:

  **WMIC QFE | find “958559”**

  where 958559 relates to the MS KB number. If the QFE is installed, it will be listed.

  ![image](images/image_thumb11.png)

  Related posts:

  [3 seconds to get system serial number](https://www.verboon.info/index.php/2008/09/3-seconds-to-get-system-serial-number/)


