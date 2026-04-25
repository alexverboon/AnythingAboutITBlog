---
title: "Automate BIOS configuration for HP clients"
layout: "post"
date: 2008-05-30T13:22:00Z
slug: "automate-bios-configuration-for-hp-clients"
aliases:
  - "/2008/05/automate-bios-configuration-for-hp-clients/"
description: "Today the following options exist to automate BIOS configuration for HP clients:The Client Management Interface allows you to use WSH to retrieve and ..."
author: "Alex Verboon"
tags:
  - bios
  - hp
categories:
  - automation
  - hp
  - tools
---
Today the following options exist to automate BIOS configuration for HP clients:The Client Management Interface allows you to use WSH to retrieve and set BIOS settings like in the example below which changes the Ownership Tag.
 
 

Const wbemFlagReturnImmediately = 16
Const wbemFlagForwardOnly = 32
lFlags = wbemFlagReturnImmediately + wbemFlagForwardOnly
strService = "winmgmts:{impersonationlevel=impersonate}//"
strComputer = "."
strNamespace = "/root/HP/InstrumentedBIOS"
strQuery = "select * from HP_BIOSSettingInterface"
Set objWMIService = GetObject(strService & _
strComputer & strNamespace)
Set colItems = objWMIService.ExecQuery(strQuery,,lFlags)
‘ "Enter Ownership Tag" is the name of the BIOS setting
‘ instance object that we want to update. The correct
‘ names of available settings are found by enumerating
‘ all instances of HP_BIOSSetting.
For each objItem in colItems
objItem.SetBiosSetting oReturn, _
"Enter Ownership Tag", _
"Some environment-specific inventory code", _
"1E302E020304"
Next
Dim strReturn
Select Case oReturn
Case 0 strReturn = "Success"
Case 1 strReturn = "Not Supported"
Case 2 strReturn = "Unspecified Error"
Case 3 strReturn = "Timeout"
Case 4 strReturn = "Failed"
18
Case 5 strReturn = "Invalid Parameter"
Case 6 strReturn = "Access Denied"
Case Else strReturn = "..."
End Select
WScript.Echo "SetBiosSetting()

More information about HP CMI can be found here:
[http://h20331.www2.hp.com/Hpsub/cache/284014-0-0-225-121.html?jumpid=reg_R1002_USEN](http://h20331.www2.hp.com/Hpsub/cache/284014-0-0-225-121.html?jumpid=reg_R1002_USEN)

The other option is to use the biosconfigutility.exe which comes with the HP System Software Manager. The example below changes the BIOS setting for WLAN switching:

BiosConfigUtility.exe /setconfig:wlan.txt

(wlan.txt content)
English
LAN/WLAN Switching 
Disable
*Enable

More Information about HP SSM can be found here:
[http://h20219.www2.hp.com/Hpsub/cache/284133-0-0-225-121.html](http://h20219.www2.hp.com/Hpsub/cache/284133-0-0-225-121.html)

