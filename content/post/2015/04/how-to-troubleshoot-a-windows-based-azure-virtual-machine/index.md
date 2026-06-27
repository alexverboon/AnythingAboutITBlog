---
title: "How to troubleshoot a Windows-based Azure Virtual Machine"
layout: "post"
date: 2015-04-05T22:52:41Z
slug: "how-to-troubleshoot-a-windows-based-azure-virtual-machine"
aliases:
  - "/2015/04/how-to-troubleshoot-a-windows-based-azure-virtual-machine/"
description: "When a physical device running Windows has problems, you have all sorts of possibilities to fix it, when virtual machine hosted within your on-premise..."
author: "Alex Verboon"
image: "img/post-heroes/how-to-troubleshoot-a-windows-based-azure-virtual-machine.png"
categories:
  - 'Azure'
tags:
  - 'Virtual-Machine'
  - 'Windows'
---
When a physical device running Windows has problems, you have all sorts of possibilities to fix it, when virtual machine hosted within your on-premise virtualization infrastructure runs into issues, you still have all options to fix it. But the first time when a virtual machine hosted in Azure gets into trouble you might feel a little bit lost. But there’s hope. When I ran into an issue myself recently I found the following article “[Troubleshoot Remote Desktop connections to a Windows-based Azure Virtual Machine](http://azure.microsoft.com/en-us/documentation/articles/virtual-machines-troubleshoot-remote-desktop-connections/)”

  The article mentions the Azure IaaS Remote Diagnostics Package. Here’s how it works.

  First go to [https://home.diagnostics.support.microsoft.com/SelfHelp/](https://home.diagnostics.support.microsoft.com/SelfHelp/) and then search for “IaaS”, you then should find the IaaS Azure Diagnostics Package.

  ![image](images/image_thumb.png)

  Next Enter a Tracking ID (optional), then select “**Create**”

  ![image](images/image_thumb1.png)

  Next select “**Download**”

  ![image](images/image_thumb2.png)

  Save the file and then select “**Run**”

  ![image](images/image_thumb3.png)

  Select “**Run now on this PC**”

  ![image](images/image_thumb4.png)

  Select “**Accept**”

  ![image](images/image_thumb5.png)

  Select “**Start**” and confirm the UAC prompt

  ![image](images/image_thumb6.png)

    A folder c:\WindowsAzure is created on the local client.

  Select “**Next**”

  ![image](images/image_thumb7.png)

  Next sign-in with your Azure Account.

  ![image](images/image_thumb8.png)

  Select the Azure Subscription (in case you have multiple)

  ![image](images/image_thumb9.png)

  Next Accept to collect diagnostic data from Azure VMs.

  ![image](images/image_thumb10.png)

  Select the Azure Storage Account (in case you have multiple)

  ![image](images/image_thumb11.png)

  Next select the issue you are experiencing.

  ![image](images/image_thumb12.png)

  Next select the VM that experiences an issue.

  ![image](images/image_thumb13.png)

  When the test / diagnosis is completed, you have the option to view the log files.

  ![image](images/image_thumb14.png)

    Optionally the log files can be saved locally.

  ![image](images/image_thumb15.png)

  ![image](images/image_thumb16.png)

  In addition to the saved CAB file, the tool also saves an additional file locally. In my case the file name was:

  "C:\WindowsAzure\Logs\AzureVMLogCollector_VM06.zip"

  The ZIP file contains various information such as Windows Event log data, Windows Setup, Networking and other information that might of use when troubleshooting a virtual machine.

  Let’s hope your Azure virtual machines, just run smoothly, but in case, now you know there’s tools around for troubleshooting.


