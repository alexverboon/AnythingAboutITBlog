---
title: "ToolTip: HDX Monitor for XenDesktop"
layout: "post"
date: 2011-05-19T23:00:07Z
slug: "tooltip-hdx-monitor-for-xendesktop"
aliases:
  - "/2011/05/tooltip-hdx-monitor-for-xendesktop/"
description: "If you experience poor performance using a XenDesktop session, video and audio is not playing nicely, the Windows Event log is showing messages as sho..."
author: "Alex Verboon"
image: "img/post-heroes/tooltip-hdx-monitor-for-xendesktop.png"
tags:
  - citrix
  - flash
  - hdx
  - latency
  - mediastream
  - network
  - performance
  - xendesktop
  - Windows
categories:
  - citrix
  - hdx
  - network
  - performance
---
If you experience poor performance using a XenDesktop session, video and audio is not playing nicely, the Windows Event log is showing messages as shown below, it’s time to take a closer look at what’s going on. 

  *Network latency is above the level supported by HDX MediaStream for Flash.  Server-side Flash rendering will be used if available.*

  *Measured latency (milliseconds): 86*

  [
![2011-05-20 00h40_32](images/2011-05-20-00h40_32_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/05/2011-05-20-00h40_32.png)

  Citrix has a FREE tool available to validate the operation of HDX. The Tool is called HDX Monitor for XenDesktop and can be downloaded from [here](http://hdx.citrix.com/hdx-monitor)

              [
![2011-05-20 00h55_34](images/2011-05-20-00h55_34_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/05/2011-05-20-00h55_34.png)        [
![2011-05-20 00h54_58](images/2011-05-20-00h54_58_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/05/2011-05-20-00h54_58.png)        [
![2011-05-20 00h57_18](images/2011-05-20-00h57_18_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/05/2011-05-20-00h57_18.png)          *The HDX Monitor is a tool to validate the operation of XenDesktop's HDX stack including the latest HDX MediaStream for Flash and HDX RealTime features. Install this tool on your virtual desktop to obtain helpful technical details about your HDX experience. The tool is organized into sections that cover the various HDX technologies. Use it to view bandwidth usage, session settings and performance metrics.*

