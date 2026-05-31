---
title: List ConfigMgr Software Update Group members with PowerShell
layout: post
date: '2013-09-22T20:47:18Z'
slug: list-configmgr-software-update-group-members-with-powershell
aliases:
- /2013/09/list-configmgr-software-update-group-members-with-powershell/
description: The below script allows you to select a Configuration Manager software
  update group and then lists the software updates that are assigned to it. ``` <...
author: Alex Verboon
categories:
  - 'ConfigMgr'
tags:
  - 'PowerShell'
  - 'Software-Update-Group'
---
The below script allows you to select a Configuration Manager software update group and then lists the software updates that are assigned to it. 

`powershell

<#
.Synopsis
   Lists assigned software updates in a configuration manager 2012 software update group
.DESCRIPTION
   Lists all assigned software updates in a configuration manager 2012 software update group that is selected 
   from the list of available update groups or provided as a command line option
.EXAMPLE
   Get-UpdateGroupcontent.ps1
.EXAMPLE
   Get-UpdateGroupcontent.ps1 -UpdateGroup "Win7x64_12_11_15"

#>

[CmdletBinding()]

param(

    # Software Update Group
    [Parameter(Mandatory = $false, ValueFromPipeline=$true)]
    [String] $UpdateGroup
    )

$SiteCode = "POC"

Function Get-UpdateGroupcontent
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

#Set-CMQueryResultMaximum -Maximum 5000

if ($UpdateGroup.Length -eq 0) {
    $UpdateGroup = Get-CMSoftwareUpdateGroup | Select-Object LocalizedDisplayName | Out-GridView -Title "Select the Software Update Group " -PassThru 
    }
Else
    {
    $UpdateGroup = Get-CMSoftwareUpdateGroup | Where-Object {$_.LocalizedDisplayName -like "$($UpdateGroup)"} |  Select-Object LocalizedDisplayName 
}

$info = @()

ForEach ($item in $UpdateGroup)
{
   Write-host "Processing Software Update Group" $($item.LocalizedDisplayName)
   forEach ($item1 in (Get-CMSoftwareUpdate -UpdateGroupName $($item.LocalizedDisplayName)))
   {
    $object = New-Object -TypeName PSObject
    #$object | Add-Member -MemberType NoteProperty -Name UpdateGroup -Value $item.LocalizedDisplayName
    $object | Add-Member -MemberType NoteProperty -Name ArticleID -Value $item1.ArticleID
    $object | Add-Member -MemberType NoteProperty -Name BulletinID -Value $item1.BulletinID
    $object | Add-Member -MemberType NoteProperty -Name Title -Value $item1.LocalizedDisplayName
    $info += $object
    }
}

$Title = "Total assigned software updates in " + $item.LocalizedDisplayName + " = " + $info.count
$info | Out-GridView -Title "$Title"
}

# -----------------------------------------------------------------------------------------------------*
# Get the list of software updates in the selected update group
Get-UpdateGroupcontent

```
