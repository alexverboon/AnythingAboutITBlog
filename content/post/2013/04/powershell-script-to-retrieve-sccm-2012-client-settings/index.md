---
title: 'PowerShell: Script to Retrieve SCCM 2012 Client Settings'
layout: post
date: '2013-04-30T22:16:54Z'
slug: powershell-script-to-retrieve-sccm-2012-client-settings
aliases:
- /2013/04/powershell-script-to-retrieve-sccm-2012-client-settings/
description: '**4/3/2017 - Update: here''s a better version:** https://www.verboon.info/2017/03/configmgr-client-policy-settings-get-cmclientpolicysettings/
  To make ...'
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Client-Settings'
  - 'Sccm-2012'
---
**4/3/2017 - Update:  here's a better version:** https://www.verboon.info/2017/03/configmgr-client-policy-settings-get-cmclientpolicysettings/



To make documenting the configured SCCM Client configuration settings a bit easier I wrote a small script that retrieves all the configured settings for the Default and custom  configuration settings.

To run this script the Configuration Manager powershell module must be loaded and connected to the site.

```powershell
# Get the different Client settings Names
$a = Get-CMClientSetting | select Name
foreach ($a in $a )
{
	# Get all possible values for the Get-CMClientSetting -Setting parameter
	$xsettings = [Enum]::GetNames( [Microsoft.ConfigurationManagement.Cmdlets.ClientSettings.Commands.SettingType])
	# dump the detailed configuration settings
	foreach ($xsettings in $xsettings ) {
        	#write-host $a.Name
	        Get-CMClientSetting -Setting $xsettings -Name $a.Name | format-table
    }
}
```

