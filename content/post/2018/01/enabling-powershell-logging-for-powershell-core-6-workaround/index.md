---
title: "Enabling PowerShell logging for PowerShell Core 6 (Workaround)"
layout: "post"
date: 2018-01-13T02:02:41Z
slug: "enabling-powershell-logging-for-powershell-core-6-workaround"
aliases:
  - "/2018/01/enabling-powershell-logging-for-powershell-core-6-workaround/"
description: "By default, PowerShell Core does not log events to the Windows Event logs. From a security perspective this isn’t ideal, but that’s something I’ll tak..."
author: "Alex Verboon"
tags:
  - eventlog
  - powershell-core
categories:
  - powershell
---
By default, PowerShell Core does not log events to the Windows Event logs. From a security perspective this isn’t ideal, but that’s something I’ll take a closer look at later. To enable PowerShell logging you have to run `RegisterManifest.ps1 which is located in the "C:\Program Files\PowerShell\6.0.0" folder. But unfortunately running that command would not work for me. Now this is the beauty of PowerShell being open sourced, the code as well as the comments from developers is publicly available. So after a short search within the GitHub repo of PowerShell Core I found references about the issue. `

`The issue was acknowledged and fixed. If you want to enable logging for PowerShell Core on Windows, download the RegisterManifest.ps1 from Gitbub [https://github.com/PowerShell/PowerShell/blob/master/src/PowerShell.Core.Instrumentation/RegisterManifest.ps1](https://github.com/PowerShell/PowerShell/blob/master/src/PowerShell.Core.Instrumentation/RegisterManifest.ps1) and store the file somewhere locally. `

C:\dev\fix\RegisterManifest.ps1 -Path 'C:\Program Files\PowerShell\6.0.0\' -Verbose

![image](https://ftp.verboon.info/wp-content/uploads/dfd7be28cc63_2623/image.png)

When opening Windows Event Viewer, you’ll see a new Folder called “PowerShellCore"

![image](https://ftp.verboon.info/wp-content/uploads/dfd7be28cc63_2623/image_3.png)

`Based on the output from the following command, it appears that PowerShell Core on Widows uses the exact same Event IDs as Windows PowerShell. But you can distinguish between Windows PowerShell and Core based on the Event Source information. `

(Get-WinEvent -ListProvider "PowerShellCore").Events | Select-Object ID, Description

(Get-WinEvent -ListProvider "Microsoft-Windows-PowerShell").Events | Select-Object ID, Description

`I have Windows PowerShell module and transcript logging enabled on this client, but so far I tend to believe that PowerShell Core is not writing any transcript logs, but will need to take a closer look at that. `

`More details about PowerShell Core logging can be found here:`

[https://github.com/dantraMSFT/PowerShell-Docs/blob/staging/reference/6/Microsoft.PowerShell.Core/About/about_Logging.md](https://github.com/dantraMSFT/PowerShell-Docs/blob/staging/reference/6/Microsoft.PowerShell.Core/About/about_Logging.md)

