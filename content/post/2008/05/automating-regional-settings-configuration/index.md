---
title: "Automating regional settings configuration"
layout: "post"
date: 2008-05-30T12:43:00Z
slug: "automating-regional-settings-configuration"
aliases:
  - "/2008/05/automating-regional-settings-configuration/"
description: "For Windows XP, regional settings can be applied by using the following method: - Create an answer file that contains the [**RegionalSettings**] secti..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Deployment'
---
For Windows XP, regional settings can be applied by using the following method:

- Create an answer file that contains the [**RegionalSettings**] section items you want to modify, and then save it (for example, as c:\regopts.txt).
- Create a batch file by using the following command line to apply the answer file settings:rundll32.exe shell32,Control_RunDLL intl.cpl,,/f:"c:\regopts.txt"

The layout of the RegionalSettings file is as following:

```ini
[**RegionalSettings**]
Language = locale ID
LanguageGroup = language group ID, language group ID
SystemLocale = locale ID
UserLocale = locale ID
InputLocale = locale ID:keyboard layout ID, locale ID:keyboard layout ID
UserLocale_DefaultUser = locale ID
InputLocale_DefaultUser = locale ID:keyboard layout ID
```

More usefull information for those dealing with Global deployments can be found here:
[http://www.microsoft.com/globaldev/default.mspx](http://www.microsoft.com/globaldev/default.mspx)
NLS Information Page for Windows XP, Windows Vista and Server 2003
[http://www.microsoft.com/globaldev/nlsweb/default.mspx](http://www.microsoft.com/globaldev/nlsweb/default.mspx)

