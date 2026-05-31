---
title: Generating Advanced hunting queries with PowerShell
layout: post
date: '2020-07-10T23:21:46Z'
slug: generating-advanced-hunting-queries-with-powershell
aliases:
- /2020/07/generating-advanced-hunting-queries-with-powershell/
description: Writing advanced hunting queries for Microsoft Defender ATP to search
  for execution of specific PowerShell commands.
author: Alex Verboon
image: img/post-heroes/generating-advanced-hunting-queries-with-powershell.png
categories:
  - 'PowerShell'
tags:
  - 'Microsoft Defender Xdr'
  - 'KQL'
---
I was recently writing some advanced hunting queries for Microsoft Defender ATP to search for the execution of specific PowerShell commands. If you are just looking for one specific command, you can run query as sown below

```
`// Find all machines running a given Powersehll cmdlet. 
let powershellCommandName = "Invoke-RickAscii"; 
DeviceEvents 
| where ActionType == "PowerShellCommand" 
| where AdditionalFields contains powershellCommandName`
```
But if you are looking for several functions, then there is going to be a lot of manual editing, and so the idea was born to use PowerShell to help me generate an advanced hunting query. The below function can do the following:

- Generate a kql query to search for all functions included in the specified PowerShell Module, use this when you have the module already installed.

Or

- Generate a kql query to search for all functions included in the specified PowerShell module manifest file, use this when you have a module that you do not want to necessary load on your device

Below are a few examples how to use the script **New-KQPSModuleFunctions** (sorry I could not come up with a better name for the function )

![](https://www.verboon.info/wp-content/uploads/2020/07/071020_2310_GeneratingA1.png)And there we have our advanced hunting queries, automatically generated with PowerShell including all the functions included in the **NetSecurity** PowerShell module

![](https://www.verboon.info/wp-content/uploads/2020/07/071020_2310_GeneratingA2.png)And here the advanced hunting query with all the functions included in the **Powersploit** module

![](https://www.verboon.info/wp-content/uploads/2020/07/071020_2310_GeneratingA3.png)The code can be found here: [https://gist.github.com/alexverboon/9ccf8af7569103397da2b8ba4079529d](#)

That's it, have a great day

Alex

