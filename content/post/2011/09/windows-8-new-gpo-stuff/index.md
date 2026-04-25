---
title: "Windows 8 &ndash; New GPO stuff"
layout: "post"
date: 09/15/2011 20:53:16
slug: "windows-8-new-gpo-stuff"
aliases:
  - "/2011/09/windows-8-new-gpo-stuff/"
description: "I have just compared the C:\Windows\PolicyDefinitions folder on the Widows 8 preview build with a Windows 7 Enterprise build. And unless I missed one,..."
author: "Alex Verboon"
tags:
  - appx
  - gpo
  - group-policy
  - new
  - profiles
  - store
  - windows-8
  - windows-to-go
categories:
  - gpo
  - group-policy
  - windows-8
---
I have just compared the C:\Windows\PolicyDefinitions folder on the Widows 8 preview build with a Windows 7 Enterprise build. And unless I missed one, the below ADMX/ADML files are new. 

  AppxPackageManager.admx   
dam.admx    
DeviceCompat.admx    
EAIME.admx    
EarlyLaunchAM.admx    
EdgeUI.admx    
ExternalBoot.admx    
msched.admx    
ProximityCommon.admx    
srm-fci.admx    
UserState.admx    
WindowsHistoryVault.admx    
WinStoreUI.admx    
wlansvc.admx    
WPN.admx    
WPN.Provider.admx    
wwansvc.admx

  When you open the related ADML files stored under C:\Windows\PolicyDefinitions\en-US you will find some interesting hints about what these new policies are supposed to do. You will find stuff about Windows to Go, the App Store, Profiles and more.

