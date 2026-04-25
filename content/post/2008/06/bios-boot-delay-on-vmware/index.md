---
title: "BIOS Boot delay on VMWARE"
layout: "post"
date: 06/03/2008 09:56:00
slug: "bios-boot-delay-on-vmware"
aliases:
  - "/2008/06/bios-boot-delay-on-vmware/"
description: "Ever had that issue that you wanted to enter the VMWARE BIOS, but you simply don't made it because the VMWARE session boots too fast ? Add the followi..."
author: "Alex Verboon"
tags:
  - bios
  - virtualization
categories:
  - tip
  - virtualization
---
Ever had that issue that you wanted to enter the VMWARE BIOS, but you simply don't made it because the VMWARE session boots too fast ?

Add the following line to your *.vmx file. 

bios.bootDelay = "3000"

[http://communities.vmware.com/docs/DOC-1201](http://communities.vmware.com/docs/DOC-1201)¨

