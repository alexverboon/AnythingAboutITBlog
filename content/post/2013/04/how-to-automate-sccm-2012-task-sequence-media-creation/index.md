---
title: How to automate SCCM 2012 Task Sequence Media Creation
layout: post
date: '2013-04-15T20:46:29Z'
slug: how-to-automate-sccm-2012-task-sequence-media-creation
aliases:
- /2013/04/how-to-automate-sccm-2012-task-sequence-media-creation/
description: Just recently I went through the CM12 Console Task Sequence media creation
  wizard several times a day, so at some point I thought, this is a good cand...
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Sccm-2012'
  - 'Task-Sequence'
---
Just recently I went through the CM12 Console Task Sequence media creation wizard several times a day, so at some point I thought, this is a good candidate for automation. 

  If you have [CU1](http://support.microsoft.com/kb/2817245/en-us) for SCCM 2012 SP1 already installed, you can take advantage of the new cmdlet **New-CMTaskSequenceMedia **Below an example. 

  CreateTaskMedia.ps1

  
```

import-module ($Env:SMS_ADMIN_UI_PATH.Substring(0,$Env:SMS_ADMIN_UI_PATH.Length-5) + '\ConfigurationManager.psd1')
cd NL1:

New-CMTaskSequenceMedia -BootableMediaOption -MediaInputType CDDVD -ProtectPassword $false -BootImageId NL100002 -DistributionPointServerName labsccm01.labhome.local -ManagementPointServerName labsccm01.labhome.local -MediaMode Dynamic -MediaPath C:\Sources\TSMedia\batchcreatedmedia1.iso -MediaSize SizeUnlimited -EnableUnknownSupport $false  -CreateMediaSelfCertificate $true -AllowUnattendedDeployment $false -UserDeviceAffinity DoNotAllow

```

If you haven’t installed CU1 yet, no worries. the command line tool CreateMedia.exe located in the SCCM Administrator Console’s bin directory does the same thing. 

CreateTaskmedia.cmd

```

@echo off 

"c:\Program Files (x86)\Microsoft Configuration Manager\AdminConsole\bin\i386\CreateMedia.exe" /K:boot /P:labsccm01.labhome.local /S:NL1 /D:LABSCCM01.LABHOME.LOCAL /L:Configuration Manager 2012 /U:True /J:False /Z:False /5:0 /X:SMSTSLocationMPs=http://labsccm01.labhome.local /B:NL100002 /T:CD /F:C:\Sources\TSMedia\batchcreatedmedia2.iso

```

  

A detailed description of the command line options available for CreateMedia.exe is documented [here](http://msdn.microsoft.com/en-us/library/jj155402.aspx). 

All Task Sequence Media creation task activities are logged here: 
  
"C:\Program Files (x86)\Microsoft Configuration Manager\AdminConsole\AdminUILog\CreateTsMedia.log"

