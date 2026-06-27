---
title: Enabling PowerShell logging for PowerShell Core 6 (Workaround)
layout: post
date: '2018-01-13T02:02:41Z'
slug: enabling-powershell-logging-for-powershell-core-6-workaround
aliases:
- /2018/01/enabling-powershell-logging-for-powershell-core-6-workaround/
description: By default, PowerShell Core does not log events to the Windows Event
  logs. From a security perspective this isn’t ideal, but that’s something I’ll tak...
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Powershell-Core'
  - 'Eventlog'
---
By default, PowerShell Core does not log events to the Windows Event logs. From a security perspective this is not ideal, but that is something I will take a closer look at later.

To enable PowerShell logging, you need to run `RegisterManifest.ps1`, which is located in `C:\Program Files\PowerShell\6.0.0`. Unfortunately, running that command did not work for me.

This is the beauty of PowerShell being open source: the code, and the comments from developers, are publicly available. After a short search in the GitHub repository for PowerShell Core, I found references to the issue.

The issue was acknowledged and fixed. If you want to enable logging for PowerShell Core on Windows, download `RegisterManifest.ps1` from GitHub and store the file locally:

[https://github.com/PowerShell/PowerShell/blob/master/src/PowerShell.Core.Instrumentation/RegisterManifest.ps1](https://github.com/PowerShell/PowerShell/blob/master/src/PowerShell.Core.Instrumentation/RegisterManifest.ps1)

```powershell
C:\dev\fix\RegisterManifest.ps1 -Path 'C:\Program Files\PowerShell\6.0.0\' -Verbose
```

![image](https://ftp.verboon.info/wp-content/uploads/dfd7be28cc63_2623/image.png)

When opening Windows Event Viewer, you will see a new folder called "PowerShellCore".

![image](https://ftp.verboon.info/wp-content/uploads/dfd7be28cc63_2623/image_3.png)

Based on the output from the following commands, it appears that PowerShell Core on Windows uses the same Event IDs as Windows PowerShell. You can still distinguish between Windows PowerShell and PowerShell Core based on the Event Source information.

```powershell
(Get-WinEvent -ListProvider "PowerShellCore").Events | Select-Object ID, Description
(Get-WinEvent -ListProvider "Microsoft-Windows-PowerShell").Events | Select-Object ID, Description
```

I have Windows PowerShell module and transcript logging enabled on this client, but so far I tend to believe that PowerShell Core is not writing any transcript logs. I still need to take a closer look at that.

More details about PowerShell Core logging can be found here:

[https://github.com/dantraMSFT/PowerShell-Docs/blob/staging/reference/6/Microsoft.PowerShell.Core/About/about_Logging.md](https://github.com/dantraMSFT/PowerShell-Docs/blob/staging/reference/6/Microsoft.PowerShell.Core/About/about_Logging.md)

