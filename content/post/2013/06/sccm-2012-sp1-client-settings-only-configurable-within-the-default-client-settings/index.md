---
title: "SCCM 2012 SP1 Client Settings only configurable within the Default Client Settings"
layout: "post"
date: 2013-06-04T20:14:48Z
slug: "sccm-2012-sp1-client-settings-only-configurable-within-the-default-client-settings"
aliases:
  - "/2013/06/sccm-2012-sp1-client-settings-only-configurable-within-the-default-client-settings/"
description: "While preparing and documenting the System Center Configuration Manager 2012 SP1 Client settings for our clients and servers I noticed that there are ..."
author: "Alex Verboon"
categories:
  - 'ConfigMgr'
tags:
  - 'Default-Client-Settings'
  - 'Sccm-2012'
---
While preparing and documenting the System Center Configuration Manager 2012 SP1 Client settings for our clients and servers I noticed that there are a few settings that cannot be configured within custom client settings meaning they can only be configured within the Default Settings.

  The following table lists the settings I identified as only configurable within the Default Client Settings.

              **Agent**        **Setting**                  Compliance Settings        Schedule compliance evaluation                  Hardware Inventory        Maximum custom MIF File Size in KB                           Collect MIF Files                  Software Inventory        Configure the display names for manufacturer or product          Related content: [About Client Settings in Configuration Manager](http://technet.microsoft.com/en-us/library/gg682067.aspx#BKMK_Compliance)


