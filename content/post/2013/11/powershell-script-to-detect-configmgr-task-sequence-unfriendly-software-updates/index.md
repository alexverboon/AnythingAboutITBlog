---
title: PowerShell Script to detect ConfigMgr Task Sequence unfriendly Software Updates
layout: post
date: '2013-11-05T23:58:55Z'
slug: powershell-script-to-detect-configmgr-task-sequence-unfriendly-software-updates
aliases:
- /2013/11/powershell-script-to-detect-configmgr-task-sequence-unfriendly-software-updates/
description: '**Update**: 15 Une 2014 - Added [KB2965788](http://support.microsoft.com/kb/2965788)
  If you’re dealing with ConfigMgr and OS Deployment task sequences...'
author: Alex Verboon
categories:
  - 'ConfigMgr'
tags:
  - 'PowerShell'
  - 'Task-Sequence'
---
**Update**: 15 Une 2014 - Added [KB2965788](http://support.microsoft.com/kb/2965788)

 If you’re dealing with ConfigMgr and OS Deployment task sequences you’re probably aware of the KB article recently published by Microsoft called “[Task sequence fails in Configuration Manager if software updates require multiple restarts](http://support.microsoft.com/kb/2894518)”.

 Let’s hope the list of KBs causing this issue isn’t going to grow too much over time, in any case we’ve decided that we would continue to review the article whenever we add new patches to our infrastructure. To simplify the task of checking whether one of the affected KBs has slipped into a software update group, I created the below script.

 The script published below, contains all KB numbers stored in the $KB variable. I recommend that you update the variable within the script as the online article gets updated with additional KB numbers. If you prefer to just check for one particular KB number, you can run the script using the –KB parameter.

`powershell
<#
.Synopsis
   Lists Software Updates found within Software Update Groups that can cause ConfigMgr Task Sequences to fail
.DESCRIPTION
  As described witin KB2894518 http://support.microsoft.com/kb/2894518 some software updates that require
      multiple restarts can cuase ConfigMgr Task Sequences to fail
      If you run the script without any parameters, all KB numbers defined in variable $KB are checked. 
      update the $KB variable with additional KB numbers when added in the online KB article
.EXAMPLE
   Find-TSFailSWUpdates
.EXAMPLE 
 Find-TSFailSWUpdates -KB 2862330,2771431
.NOTES
    Written by Alex Verboon
    Version 1.0, 05.11.2013
#>

[CmdletBinding()]

 
param(
 
 
    # Software Update Group
    [Parameter(Mandatory = $false, ValueFromPipeline=$true)]
    [String[]] $KB
    )
 
 
$SiteCode = "SR1"

if ($KB.Length -eq 0) 
    {    
        $KB = "2862330","2771431","2871777","2821895","2545698","2529073",”2965788”
    }

Function Find-TSFailSWUpdates
{
 
# Check that youre not running X64
if ([Environment]::Is64BitProcess -eq $True) 
    {    Throw "Need to run at a X86 PowershellPrompt"
    }
 
# Load ConfigMgr module if it isn't loaded already
if (-not(Get-Module -name ConfigurationManager)) {
        Import-Module ($Env:SMS_ADMIN_UI_PATH.Substring(0,$Env:SMS_ADMIN_UI_PATH.Length-5) + '\ConfigurationManager.psd1')
   }
 
# Change to site
    Push-Location
    Set-Location ${SiteCode}:
 
 

$UpdateGroups = Get-CMSoftwareUpdateGroup | Select-Object LocalizedDisplayName

 
$info = @()
 
ForEach ($item in $UpdateGroups)
{
    Write-host "Processing Software Update Group" $($item.LocalizedDisplayName)
    forEach ($item1 in (Get-CMSoftwareUpdate -UpdateGroupName $($item.LocalizedDisplayName)))
    {
        forEach ($item2 in $KB)
        {
            if ($item1.ArticleID -eq $item2)
            {
            $object = New-Object -TypeName PSObject
            $object | Add-Member -MemberType NoteProperty -Name UpdateGroup -Value $item.LocalizedDisplayName
            $object | Add-Member -MemberType NoteProperty -Name ArticleID -Value $item1.ArticleID
            $object | Add-Member -MemberType NoteProperty -Name BulletinID -Value $item1.BulletinID
            $object | Add-Member -MemberType NoteProperty -Name Title -Value $item1.LocalizedDisplayName
            $info += $object
            }
        }
    }
}

$info | Format-Table
Pop-Location
}
 
# -----------------------------------------------------------------------------------------------------*
# Show the updates that cause ConfigMgr TS to fail and the software update group there'in
Find-TSFailSWUpdates

```
