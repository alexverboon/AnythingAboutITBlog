---
title: PowerShell Script - Get Group Policy events by CorrelationID
layout: post
date: '2014-07-17T15:00:44Z'
slug: powershell-script-get-group-policy-events-by-correlationid
aliases:
- /2014/07/powershell-script-get-group-policy-events-by-correlationid/
description: '**Update: 22. August 2014**: I have posted an updated version of the
  script [here](http://gallery.technet.microsoft.com/Get-GPEventByCorrelationID-979...'
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Correlationid'
  - 'Group Policy'
---
**Update: 22. August 2014**: I have posted an updated version of the script [here](http://gallery.technet.microsoft.com/Get-GPEventByCorrelationID-97944972). 

 During his [Group Policy: Notes from the Field - Tips, Tricks, and Troubleshooting](http://channel9.msdn.com/Events/TechEd/NorthAmerica/2014/WIN-B328#fbid=) session at TechEd Group Policy MVP Jeremy Moskowitz demonstrates how to filter the event log using the correlation ID. Now because I love using PowerShell I thought I create a function for that using Jeremy’s XMLquery.

 
```powershell
function Get-GPEventByCorrelationID
{
<#
.Synopsis
   Get Group Policy Eventlog entries by Correlation ID
.DESCRIPTION
   This function retrieves Group Policy event log entries filtered by Correlation ID
.EXAMPLE
   Get-GPEventByCorrelationID -CorrelationID A2A621EC-44B4-4C56-9BA3-169B88032EFD

   TimeCreated                     Id LevelDisplayName Message
   -----------                     -- ---------------- -------
   7/17/2014 3:00:27 PM          5117 Information      Group policy session completed successfully.

#>
    [CmdletBinding()]
    Param
    (
        # CorrelationID
        [Parameter(Mandatory=$true,
                   ValueFromPipelineByPropertyName=$true,
                   Position=0)]
        [string]$CorrelationID 
    )

    Begin
    {
        $Query = '*[System/Correlation/@ActivityID="{CorrelationID}"]'
        $FilterXML = $Query.Replace("CorrelationID",$CorrelationID)
    }
    Process
    {
        Get-WinEvent -FilterXml $FilterXML
    }
    End
    {
    }
}
```

 

Greetings form the sunny beaches at [Sardinia](http://en.wikipedia.org/wiki/Sardinia).
