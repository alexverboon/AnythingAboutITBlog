---
title: Grow vmware size
layout: post
date: '2008-05-10T09:38:00Z'
slug: grow-vmware-size
aliases:
- /2008/05/grow-vmware-size/
description: Today i ran out of diskspace on one of my systems that runs within a
  vmware session. The system disk only had 10 GB and I needed to add another 10 GB....
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'Vmware'
  - 'Virtualization'
---
Today i ran out of diskspace on one of my systems that runs within a vmware session. The system disk only had 10 GB and I needed to add another 10 GB.

This is what i did:
	
- Extend the disk in offline mode by running the following command: C:\Program Files\VMware\VMware Workstation>vmware-vdiskmanager -x 20GB "C:\Users\Alex\Documents\Virtual Machines\Server 2003 - sysmanage\Windows Server 2003 Standard Edition-cl1.vmdk"
It then takes a while until the disk is expanded.
	
- Boot the system from WinPE 2.0
	
- I then ran the following commands: diskpart

```bash	
list disk
list volume
select volume=1 (in my case volume 1 is the volume that i had extended)
extend
```

Reboot the system and done.
