---
title: A quick look at the Windows PowerShell Module for Intel vPro
layout: post
date: '2010-09-04T18:41:44Z'
slug: a-quick-look-at-the-windows-powershell-module-for-intel-vpro
aliases:
- /2010/09/a-quick-look-at-the-windows-powershell-module-for-intel-vpro/
description: In a previous post [Using Intel AMT Power Management @ Home](https://www.verboon.info/index.php/2009/07/using-intel-amt-power-management-home/)
  I wrot...
author: Alex Verboon
tags:
- amt
- intel
- power-management
- vpro
- Windows
- PowerShell
categories:
- amt
- intel
- tip
- vpro
- Windows
- PowerShell
---
In a previous post [Using Intel AMT Power Management @ Home](https://www.verboon.info/index.php/2009/07/using-intel-amt-power-management-home/) I wrote about how to use Intel AMT Power Management at home or let’s say in an environment where you don’t have systems managed by an infrastructure that provides integrated support for Intel AMT.

  Now Intel has released a PowerShell Module for Intel vPro. You find all the details in the following blog posts. 

  [Intel Core vPro Processor PowerShell Module - Release & Introduction](http://communities.intel.com/community/openportit/vproexpert/blog/2010/07/19/intel-core-vpro-processor-powershell-module--release-introduction)

  [Using the Intel Core vPro Processor PowerShell Module - Part 1](http://communities.intel.com/community/openportit/vproexpert/blog/2010/07/19/using-the-intel-core-vpro-processor-powershell-module--part-1)

  [Using the Intel Core vPro Processor PowerShell Module - Part 2](http://communities.intel.com/community/openportit/vproexpert/blog/2010/07/19/using-the-intel-core-vpro-processor-powershell-module--part-2)

  So now that we have a PowerShell Module available there is no need anymore to use external command line tools from the Intel [SDK](http://software.intel.com/en-us/articles/download-the-latest-intel-amt-software-development-kit-sdk/). Can’t wait to see it in action? OK here we go. 

  1. Download the Intel vPro PowerShell Module from [here](http://software.intel.com/file/29241) and install it on a machine that has PowerShell installed (Note: Windows 7 includes PowerShell by default). 

  2. You have a second vPro enabled client that is configured in SMB mode. 

  3. Create a script with the following content and save it as vpro_on.ps1

  import-module intelvpro      
Invoke-AMTPowerManagement 192.168.1.248 16992 PowerOn -Username:admin -Password:vProAdmin123*

  4. Launch the script in PowerShell, if all goes right, the PC should power on. To turn it off again, simply change ***PowerOn*** to ***PowerOff***

  That’s it.

