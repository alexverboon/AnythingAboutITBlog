---
title: "Installing ESXi in VMWare Workstation 6.5"
layout: "post"
date: 2008-11-02T11:28:38Z
slug: "installing-esxi-in-vmware-workstation-65"
aliases:
  - "/2008/11/installing-esxi-in-vmware-workstation-65/"
description: "Installing ESXi"
author: "Alex Verboon"
categories:
  - 'Tips-Tools'
tags:
  - 'Vmware'
  - 'Virtualization'
---
Finally after several attempts, i've been able to install [VMWare ESXi ](http://www.vmware.com/products/esxi/)into VMware Workstation 6.5. The intend of doing this is purely to get familiar with the product. To get this done, i have been mainly following the [instructions ](http://knowledge.xtravirt.com/white-papers/esx-3x.html)provided by [xtravirt.com](http://knowledge.xtravirt.com/)

Once installed i had some challenges with [transfering files through the Virtual Infrastructure Client datastore browser](http://www.ntpro.nl/blog/archives/247-ESX-3i-Uploading-Files.html) where i received I/O errors. After some troubleshooting it appears to be related to the network , switch configuration which i haven't solved yet. The workaround i used for the time being is to configure the ESXi vmware network setting to "host" only instead of "Bridged".

Another interesting learning was that ESXi officially does not provide support for SSH, but this can be enabled thorugh an unsupported hack which is described [here](http://www.vm-help.com/esx/esx3i/ESXi_enable_SSH.php). Once ssh is enabled, you can also transfer files to the datastore using [WinSCP](http://winscp.net/eng/index.php).

