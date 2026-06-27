---
title: Use Microsoft Endpoint Configuration Manager to Configure the Windows Print
  Spooler Service
layout: post
date: '2021-07-10T15:07:17Z'
slug: use-microsoft-endpoint-configuration-manager-to-configure-the-windows-print-spooler-service
aliases:
- /2021/07/use-microsoft-endpoint-configuration-manager-to-configure-the-windows-print-spooler-service/
description: How to use Microsoft Endpoint Configuration Manager and configuration
  baselines to ensure the Windows Print Spooler service remains stopped and disabled.
author: Alex Verboon
image: img/post-heroes/use-microsoft-endpoint-configuration-manager-to-configure-the-windows-print-spooler-service.png
categories:
  - 'Security'
tags:
  - 'Windows'
  - 'ConfigMgr'
---
Hello there,

In [my earlier post](https://www.verboon.info/2021/07/use-microsoft-endpoint-configuration-manager-to-stop-the-windows-print-spooler-service/) [Use Microsoft Endpoint Configuration Manager to stop the Windows Print Spooler Service – Anything about IT (verboon.info)](https://www.verboon.info/2021/07/use-microsoft-endpoint-configuration-manager-to-stop-the-windows-print-spooler-service/) I explained how to stop the Print Spooler service using Microsoft Endpoint Configuration Manager leveraging CMPivot to identify servers where the Print Spooler is running and the Run Script function to stop and disable the service. This method was intended as a first response action, however as new servers get deployed, we want to make sure the print spooler remains disabled, so we need a more permanent solution.

In this blog post I will explain how we can use Microsoft Endpoint Configuration Manager and a Configuration Baseline to ensure the Print Spooler is stopped and disabled. And yes, this blog post is intended for those who for whatever reason cannot or do not want to use AD Group Policy.

First download the scripts from my GitHub repo [https://github.com/alexverboon/PowerShellCode/tree/main/PrintSpooler/MEMCMBaseLine](https://github.com/alexverboon/PowerShellCode/tree/main/PrintSpooler/MEMCMBaseLine) and save them locally as shown in the example below.

![](071021_1503_UseMicrosof1.png)

Next open the Microsoft Endpoint Configuration Manager and then launch PowerShell ISE from the console.

![](images/071021_1503_UseMicrosof2.png)

Next load the function that is included in `New-CMCIPrintSpoolerService.ps1` and then run the function that creates the Configuration Item in Microsoft Endpoint Configuration Manager.

```powershell
. .\New-CMCIPrintSpoolerService.ps1
New-CMCIPrintSpoolerService -SiteCode P01 -SiteServer cm01.corp.net -Verbose
```

![](images/071021_1503_UseMicrosof3.png)

When all goes well, you now have a new Configuration Item.

![](images/071021_1503_UseMicrosof4.png)

The CI has both the discovery script and remediation script embedded.

![](images/071021_1503_UseMicrosof5.png)

Next create a configuration baseline and include the newly created configuration item.

![](images/071021_1503_UseMicrosof6.png)

And finally deploy the configuration baseline to a device collection that includes all servers where the print spooler must be disabled. As soon as the device picks up the configuration baseline, you can verify the status on the device.

![](images/071021_1503_UseMicrosof7.png)

Test the configuration baseline by setting the print spooler to automatic and/or start it, and then run the evaluation again.

![](images/071021_1503_UseMicrosof8.png)

If all works as expected, the service is stopped and set to disabled.

![](images/071021_1503_UseMicrosof9.png)

You can find the scripts mentioned in this blog post here on GitHub: [https://github.com/alexverboon/PowerShellCode/tree/main/PrintSpooler/MEMCMBaseLine](https://github.com/alexverboon/PowerShellCode/tree/main/PrintSpooler/MEMCMBaseLine)

I would also like to refer to another [blog post from Thijs Lecomte](https://thecollective.eu/blog/implement-workarounds-for-pinter-nightmare-with-mem/), where he describes how to use MEM to deploy Print Spooler patches and configuration through Microsoft Intune.

Have a great day

Alex


