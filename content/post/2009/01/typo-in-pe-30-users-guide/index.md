---
title: Typo in PE 3.0 Users guide
layout: post
date: '2009-01-10T17:02:05Z'
slug: typo-in-pe-30-users-guide
aliases:
- /2009/01/typo-in-pe-30-users-guide/
description: I've just found a typo in the Windows PE 3.0 Users guide for DISM package
  path usage in WinPE.
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'Automation'
  - 'Dismexe'
---
I've just found a typo in the Windows PE 3.0 Users guide.

dism /image:C:\winpe_x86\mount /Add-Package /PackagePath:"C:\Program Files\Windows **OPK**\Tools\PETools\x86\WinPE_OCs\winpe-wmi.cab"

dism /image:C:\winpe_x86\mount /Add-Package /PackagePath:"C:\Program Files\Windows **AIK**\Tools\PETools\x86\WinPE_OCs\winpe-wmi.cab"

"OPK" should be replaced with "AIK" otherwise if you copy paste the sample commandline adding an optinonal component will not work.

