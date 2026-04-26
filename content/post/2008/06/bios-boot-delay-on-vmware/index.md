---
title: "BIOS Boot delay on VMWARE"
layout: "post"
date: 2008-06-03T09:56:00Z
slug: "bios-boot-delay-on-vmware"
aliases:
  - "/2008/06/bios-boot-delay-on-vmware/"
description: "Ever had that issue that you wanted to enter the VMWARE BIOS, but you simply don't made it because the VMWARE session boots too fast ? Add the followi..."
author: "Alex Verboon"
tags:
  - bios
  - virtualization
categories:
  - Tips
---
Ever had that issue that you wanted to enter the VMWARE BIOS, but you simply don't made it because the VMWARE session boots too fast ?

Add the following line to your *.vmx file. 

```ini
bios.bootDelay = "3000"
```

[http://communities.vmware.com/docs/DOC-1201](http://communities.vmware.com/docs/DOC-1201)¨

