---
title: PowerShell Script to retrieve content from Internet Explorer ActiveX blocking
  log
layout: post
date: '2014-08-13T23:12:50Z'
slug: powershell-script-to-retrieve-content-from-internet-explorer-activex-blocking-log
aliases:
- /2014/08/powershell-script-to-retrieve-content-from-internet-explorer-activex-blocking-log/
description: In preparation of the Internet [Explorer out of date ActiveX control
  blocking](http://technet.microsoft.com/en-us/ie/dn798785.aspx) activities I wrote...
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Activex'
  - 'Internet-Explorer'
---
In preparation of the Internet [Explorer out of date ActiveX control blocking](http://technet.microsoft.com/en-us/ie/dn798785.aspx) activities I wrote the below script that retrieves the content of the log stored under LOCALAPPDATA%\Microsoft\Internet Explorer\AuditMode\VersionAuditLog.csv

You can download the script from [here](http://gallery.technet.microsoft.com/scriptcenter/Get-ActiveXControlLog-58d33184)

```
function Get-ActiveXControlLog
{
<#
.Synopsis
   Get-ActiveXControlLog
.DESCRIPTION
   Get-ActiveXControlLog retrieves the content of the Internet Explorer ActiveX control log stored locally. 
.EXAMPLE
   Get-ActiveXControlLog
    Shows all entries in the log file
.EXAMPLE
   Get-ActiveXControlLog -Show Allowed
   Shows only entries with status "Allowed"
.LINKS
    http://technet.microsoft.com/en-us/ie/dn798785.aspx
.NOTES
    version 1.0 by Alex Verboon
#>
    [CmdletBinding()]
    Param
    (
     [Parameter(Mandatory=$false,
     Position=0)]
     [ValidateSet("All","Allowed","Blocked")] 
     $Show="All"
    )

    Begin
    {
        # the default location of the log file
        $VersionAuditLog = [Environment]::GetFolderPath('LocalApplicationData') + "\Microsoft\Internet Explorer\AuditMode\VersionAuditLog.csv"
        # check if the log file is present
        If (Test-Path $VersionAuditLog)
        {
            Write-output "ActiveX out of date blocking control log found"
        }
        Else
        {
            Write-Verbose "ActiveX out of date blocking control log not found"
            # let's check if the logging policy is enabled at all
            $lm = (Get-ItemProperty -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\Policies\Ext" -Name "AuditModeEnabled" -ErrorAction SilentlyContinue).AuditModeEnabled 
            $cu = (Get-ItemProperty -Path "HKCU:Software\Microsoft\Windows\CurrentVersion\Policies\Ext" -Name "AuditModeEnabled" -ErrorAction SilentlyContinue).AuditModeEnabled
            
            If ($lm -le 0)
            {
                write-output "ActiveX control logging policy is not enabled at the computer level"
            }
            Else
            {
                Write-Output "Active control logging policy is enabled at the computer level, but there's no log: $VersionAuditLog"
            }

            If ($cu -le 0)
            {
                write-output "ActiveX control logging policy is not enabled at the User level"
            }
            Else
            {
                Write-Output "Active control logging policy is enabled at the user level, but there's no log: $VersionAuditLog"
            }
            Throw 
        }
    }
    Process
    {

    # Get the content of the log file
    $axlog = Import-csv -Delimiter "," -Path $VersionAuditLog -Header URL, Path, ProductVersion, FileVersion, Action, Reason, EPMCompat
    $axlogdata = @()
    ForEach ($entry in $axlog)
    {
     $object = New-Object -TypeName PSObject
     $object | Add-Member -MemberType NoteProperty -Name URL -Value $entry.URL
     $object | Add-Member -MemberType NoteProperty -Name Path -Value $entry.Path
     $object | Add-Member -MemberType NoteProperty -Name ProductVersion -Value $entry.ProductVersion
     $object | Add-Member -MemberType NoteProperty -Name FileVersion -Value $entry.FileVersion
     $object | Add-Member -MemberType NoteProperty -Name Result -Value $entry.Action
     $object | Add-Member -MemberType NoteProperty -Name Reason -Value $entry.Reason 
     $object | Add-Member -MemberType NoteProperty -Name EPMCompatible -Value $entry.EPMCompat
     $axlogdata += $object
    }
    }
    End
    {
        If ($Show -eq "All")
        {
            $axlogdata
        }
        Else
        {
            $axlogdata | Where-Object {$_.Result -eq "$Show"}
        }
    }
}
```

