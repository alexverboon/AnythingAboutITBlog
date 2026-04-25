---
title: "Group Policy Settings for Microsoft Edge Browser in Windows 10 Build 10.0.10240"
layout: "post"
date: 07/17/2015 09:00:34
slug: "group-policy-settings-for-microsoft-edge-browser-in-windows-10-build-10-0-10240"
aliases:
  - "/2015/07/group-policy-settings-for-microsoft-edge-browser-in-windows-10-build-10-0-10240/"
description: "Continuing exploring the Windows 10 preview builds for new Group Policy settings, I come across some new settings for the [Microsoft Edge browser](htt..."
author: "Alex Verboon"
tags:
  - group-policy
  - microsoft-edge
  - spartan
categories:
  - windows-10
---
Continuing exploring the Windows 10 preview builds for new Group Policy settings, I come across some new settings for the [Microsoft Edge browser](https://msdn.microsoft.com/en-us/library/hh772401(v=vs.85).aspx).

  

    **Location** **Setting** **Description**  Computer Configuration / Administrative Templates / Windows Components / Microsoft Edge Allows you to run scripts like Javascript  This setting lets you decide whether to let people run scripts, like JavaScript. This setting is enabled by default.

 If you enable this setting, scripting is turned on for all your computers. 

 If you disable this setting, scripts can’t run.

    Allows you to let people use autofill on websites  This setting lets you decide whether people can use autofill on websites. This setting is enabled by default.

 If you enable this setting, people can use autofill on websites, caching the info locally.

 If you disable this setting, people can’t use autofill.

    Allows you to let people send Do not track headers  This setting lets you decide whether to let people send Do Not Track headers. This setting is disabled by default.

 If you enable this setting, people can send Do Not Track headers from any computer in your organization.

 If you disable this setting, people can’t send Do Not Track headers.

    Allows you to configure password manager  This setting lets you decide whether people can save passwords locally on their computers. This setting is enabled by default.

 If you enable this setting, Password Manager is turned on and people can save passwords locally on their computers.

 If you disable this setting, Password Manager is turned off and people can’t save passwords locally.

    Allows you to run pop-ups  This setting lets you decide whether to allow pop-ups. This setting is disabled by default.

 If you enable this setting, pop-ups can run on all your organization’s computers.

 If you disable this setting, pop-ups can’t run.

    Stop address bar from showing search suggestions  This setting lets you decide whether the address bar should show search suggestions. This setting is enabled by default.

 If you enable this setting, people can see search suggestions in the address bar.

 If you disable this setting, search results don’t appear in the address bar.

    Allows you to configure smartscreen  This setting lets you decide whether to turn on SmartScreen. This setting is enabled by default.

 If you enable this setting, SmartScreen is turned on for all your computers. 

 If you disable this setting, SmartScreen is turned off.

    Configure how Microsoft Edge treates cookies  This settings lets you decide how Microsoft Edge should treat cookies.

 If you enable this setting, you have 3 additional options:
  • Don’t block. Cookies can download from all websites. This is the default value.
  • Block only third-party cookies. Stops third-party cookies from downloading.
  • Block all cookies. Stops all cookies from downloading.

    Allows you to configure the the Enterprise Site list  This setting lets you decide whether to set up and use the Enterprise Site List for compatibility.

 If you enable this setting, you have 2 additional options:
  • Not configured. You can’t use the Enterprise Site List.
  • UseEnterpriseModeSiteList. Lets you use the Enterprise Site List. If you use this option, you must also include the location to your XML site list in the {URI} box. This is the default value.

    Sends all intranet traffic over to internet explorer  This setting lets you decide whether to send all intranet traffic to Internet Explorer. This setting is disabled by default

 If you enable this setting, your intranet websites automatically open in Internet Explorer.

 If you disable this setting, your intranet websites will automatically open in Microsoft Edge.

  

 The same settings can also be found under User  Configuration / Administrative Templates / Windows Components / Microsoft Edge.

