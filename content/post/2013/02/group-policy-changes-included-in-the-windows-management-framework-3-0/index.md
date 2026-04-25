---
title: "Group Policy changes included in the Windows Management Framework 3.0"
layout: "post"
date: 2013-02-26T06:48:22Z
slug: "group-policy-changes-included-in-the-windows-management-framework-3-0"
aliases:
  - "/2013/02/group-policy-changes-included-in-the-windows-management-framework-3-0/"
description: "While creating a new Group Policy object to enable WinRM (Windows Remote Management) on clients, I noticed some Group Policy changes that are introduc..."
author: "Alex Verboon"
tags:
  - group-policy
  - powershell
  - windows-remote-management
  - winrm
categories:
  - group-policy
  - winrm
---
While creating a new Group Policy object to enable WinRM (Windows Remote Management) on clients, I noticed some Group Policy changes that are introduced with the Windows Management Framework 3.0. The Windows Management Framework 3.0 contains the following updates:

     
- Windows PowerShell 3.0    
- Windows Management Instrumentation (WMI) 3.0    
- Windows Remote Management (WinRM)    
- Management OData IIS Extension    
- Server Manager CIM Provider 

  I became aware of the changes as I was referring to a blog post I had written a while back about [how to enable Windows Remote Management via Group Policy.](https://www.verboon.info/index.php/2011/11/enable-windows-remote-management-through-group-policy/)I noticed that the name of the Group Policy setting located under Computer Configuration \ Windows Components \ Windows Remote Management (WinRM) \ WinRM Service \ **Allow automatic configuration of listeners** was changed to **Allow Remote Server management through WinRM**

  Looking at the Group Policy template files stored under C:\Windows\PolicyDefinitions I noticed that the following template updates. 

     
- PowerShellExecutionPolicy.adml    
- PowerShellExecutionPolicy.admx    
- WindowsRemoteManagement.adml    
- WindowsRemoteManagement.admx    
- WindowsRemoteShell.adml     
    
- WindowsRemoteShell.admx was not changed.  

  The changes aren’t huge, but for those interested in the detail, here’s an overview of what I found out while comparing the content of the above listed files. 

  For PowerShell two new settings are introduced. They can be found under Computer Configuration \ Administrative Templates \ Windows Components \ Windows Powershell. 

     
- Turn on Module logging    
- Set default source path for update-help 

  For Windows Remote Shell no new settings were introduced, the template changes only relate to changes in wording of the policy descriptions. 

  For Windows Remote Management located under Computer Configuration \ Windows Components \ Windows Remote Management (WinRM) the following policies were added/ changed. 

     
- WinRM Service \ Allow Remote Server management through WinRM     
 (only a name change, previously known as: Allow automatic configuration of listeners)    
- WinRM Service \ Disallow WinRM from storing RunAS credentials     
(New Setting) 

  All English template language files (adml) received a wording overhaul. Descriptions now all start with “This policy setting….” and single digit numbers are spelled out. Also wording changed from “will be..” to “are”

