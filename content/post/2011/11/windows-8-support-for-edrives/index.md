---
title: "Windows 8 Support for eDrives"
layout: "post"
date: 11/22/2011 21:39:49
slug: "windows-8-support-for-edrives"
aliases:
  - "/2011/11/windows-8-support-for-edrives/"
description: "I have just installed the Windows 8 Assessment and Deployment Kit and came across some information about Windows 8 support for eDrive also known as th..."
author: "Alex Verboon"
tags:
  - adk
  - edrive
  - unattendxml
  - windows-8
categories:
  - edrive
  - windows-8
---
I have just installed the Windows 8 Assessment and Deployment Kit and came across some information about Windows 8 support for eDrive also known as the Encrypted Hard Disk Drive.. 

  The Windows Setup Reference mentions a new setting called *Microsoft-Windows-EnhancedStorage-Adm* / *TCGSecurityActivationDisabled*. By default, when Windows is installed on an eDrive, Windows automatically encrypts the drive by using TCG and IEEE 1667 transport standards.

  More information:   
[eDrive Device Guide](http://msdn.microsoft.com/en-us/library/windows/hardware/br259095.aspx)    
[Almost All Future Drives Will Self Encrypt, Says Tom Coughlin, in Industry's First Forecast on SEDs](http://www.trustedcomputinggroup.org/community/category/data_protection/4)     
[Building hardware-accelerated encrypted devices (eDrives) in Windows 8](http://channel9.msdn.com/Events/Windows-Ecosystem-Summit/2011Taipei/SYS-007T)

