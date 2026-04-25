---
title: "No Automatic reboot please"
layout: "post"
date: 2008-08-24T13:59:22Z
slug: "no-automatic-reboot-please"
aliases:
  - "/2008/08/no-automatic-reboot-please/"
description: "Saturday morning, before going out with my family on a shopping tour I started a large FTP download and assumed it would have completed upon my return..."
author: "Alex Verboon"
image: "img/post-heroes/no-automatic-reboot-please.png"
tags:
  - automatic-updates
  - registry
  - Windows
categories:
  - tip
  - vista
---
Saturday morning, before going out with my family on a shopping tour I started a large FTP download and assumed it would have completed upon my return.... a few hours later, I found my system at the logon prompt, as it had rebooted itself automatically and of course the FTP download was not completed.

What happened ? Very simple, Windows Update had automatically rebooted the system, probably after having displayed a message as shown in the screen shot below.

![image](images/image7.png)

Was it really Windows Update ? Yes, i compared the time the FTP transfer had stopped with the Event log entries and the time period seemed to match.

[
![image](images/image-thumb7.png)
](https://www.verboon.info/wp-content/uploads/2008/08/image7.png)

To prevent Windows Update from automatically rebooting in the future, I applied the following Windows registry keys::

[
![image](images/image-thumb8.png)
](https://www.verboon.info/wp-content/uploads/2008/08/image8.png)

