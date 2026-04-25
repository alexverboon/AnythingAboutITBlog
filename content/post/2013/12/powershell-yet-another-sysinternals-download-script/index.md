---
title: "PowerShell - Yet another Sysinternals download script"
layout: "post"
date: 2013-12-01T22:10:33Z
slug: "powershell-yet-another-sysinternals-download-script"
aliases:
  - "/2013/12/powershell-yet-another-sysinternals-download-script/"
description: "Today I completed the Microsoft Virtual Academy [Advanced Tools & Scripting with PowerShell 3.0 Jump Start](http://www.microsoftvirtualacademy.com/tra..."
author: "Alex Verboon"
tags:
  - whatif-verbose
  - download
  - invoke-webrequest
  - powershell
  - sysinternals
categories:
  - powershell
---
Today I completed the Microsoft Virtual Academy [Advanced Tools & Scripting with PowerShell 3.0 Jump Start](http://www.microsoftvirtualacademy.com/training-courses/advanced-tools-scripting-with-powershell-3-0-jump-start) course. If you haven’t looked at it yet, I realy recommend you do so, lots of good stuff there. So for the purpose of applying some of the stuff I’ve learned there regarding the use of -Whatif and -verbose messages i wrote the below script which downloads the sysinternals tools. 

  

```
<#
.Synopsis
   Download Sysinternals Tools
.DESCRIPTION
   Download the Sysinternals tools from live.sysinternals.com to the local machine
.NOTES
    version 1.0
.EXAMPLE
   Get-Sysinternals -Path C:\Data|sysinternals
.EXAMPLE
   Get-Sysinternals.ps1 -Path C:\Data\Sysinternals -Whatif -verbose
#>

[CmdletBinding(SupportsShouldProcess=$true)]
Param(
[Parameter(Mandatory=$true,ValueFromPipelineByPropertyName=$true,ParameterSetName="Directory",
           HelpMessage= 'The local download folder')]
[String]$Directory
)

Begin
    {
    Write-Verbose "Starting Sysinternals Tool download"
    $url="http://live.sysinternals.com/tools/"

    if ((Test-path -path $Directory) -eq $False)
         {
        Write-Verbose "Creating Directory $Directory"
        if ($PScmdlet.ShouldProcess("Creating folder $Directory","",""))
        {New-Item -ItemType Directory -Path $Directory}
        } 

    $siuri = Invoke-WebRequest -Uri $url -EA SilentlyContinue
    if ($siuri.BaseResponse.StatusCode -eq "OK")
        {
            $sfiles = $siuri.Links | Where-Object {$_.href -ne '/'} | Select-Object -ExpandProperty innerText
        }
    Else
        {
        Write-Verbose "Unable to reach $url"
        Exit 1
        }   
    }

Process
    {
    ForEach ($st in  $sfiles)
        {
        $downloadfile = $url+$st
        #Write-Verbose -Message "Downloading $downloadfile to $Directory\$st"
        if ($PScmdlet.ShouldProcess("Downloading now $downloadfile to $Directory\$st","",""))
            {Start-BitsTransfer -Description "SysinternalsDownload - $st" -Source $downloadfile -Destination "$Directory\$st"}
        }
    }

End
    {
        Write-Verbose "Download complete"
    }

```

