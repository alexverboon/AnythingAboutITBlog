---
title: PowerShell Script&ndash;Set App-V 4.6 Cache Size
layout: post
date: '2013-11-29T18:13:07Z'
slug: powershell-scriptset-app-v-4-6-cache-size
aliases:
- /2013/11/powershell-scriptset-app-v-4-6-cache-size/
description: 'Background: As part of our migration process from Configuration Manager
  2007 to Configuration Manager 2012 R2 we also adjust the App-V Cache Size that...'
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'App-V'
  - 'Appvcachesize-Exe'
---
Background: As part of our migration process from Configuration Manager 2007 to Configuration Manager 2012 R2 we also adjust the App-V Cache Size that is currently set to 6GB to 11GB because the ConfigMgr Agent Cache is set to 10GB, this by following the best practice described in Microsoft’s whitepaper [Virtual Application Management with Microsoft Application Virtualization 4.5/4.6 and System Center Configuration Manager 2007 R2](http://www.google.ch/url?sa=t&rct=j&q=&esrc=s&frm=1&source=web&cd=1&cad=rja&ved=0CCsQFjAA&url=http%3A%2F%2Fdownload.microsoft.com%2Fdownload%2Ff%2F7%2F8%2Ff784a197-73be-48ff-83da-4102c05a6d44%2FAPP-V%2FApp-V_and_ConfigMgr_Whitepaper_Final.docx&ei=ZdaYUrSUM_PzyAOOq4CwDQ&usg=AFQjCNG4EECrJQw6YqoBPTF3BYBCTh9Fnw&sig2=Za3zNXB5Gjb_YZg0Yw8zzw&bvm=bv.57155469,d.bGQ)**** where it says. 

 *“The App-V Client cache free disk space threshold parameter should be set to ensure that the available disk space on the client PC is at least 1 GB larger than the Configuration Manager Client cache size.”*

 The actual change of the App-V cache is not done through PowerShell itself but set using the [Microsoft appvcachesize.exe utility.](http://www.microsoft.com/en-us/download/details.aspx?id=5927) I used this utility based on the explanations provided in the blog post from Kirx [About the App-V Client Cache size not being (fully) controlled by the Registry Value FileSize](http://kirxblog.wordpress.com/2010/04/17/about-the-app-v-client-cache-size-not-being-fully-controlled-by-the-registry-value-filesize/)

 Because I am getting a lot from the community, I wanted to give something back and therefore created a standalone script of the code that changes the App-V Cache size that i have embedded in our larger ConfigMgr migration script which I might share at a later point in time. 

 The below script **Set'-AppVCacheSize.ps1** dos the following. 

  
- Copies the appvcachesize.exe to the targeted remote machine  
- Retrieves the current App'-V Cache file and size settings  
- Changes the App-V Cache size to the size specified  
- Displays the new App-V Cache file and size settings

 **Important**! You must store the [appvcachesize.exe](http://www.microsoft.com/en-us/download/details.aspx?id=5927) within the same folder where the PowerShell script is stored. 

 Also note that the script is using PowerShell remoting for all actions, so having WinRM enabled on the target machines is a must. 

 Examples of possible execution modes are documented within the Script. 

`powershell
<#
.Synopsis
   Configure the App-v 4.6X Cache Size
.DESCRIPTION
   Configure the App-V 4.6x Cache size on the specified computers using the AppvCachesize.exe
   Utility from Microsoft
.PARAMETER Computername
    Array of strings that represents the remote computeres to target
.PARAMETER Size
    The App-v Cache Size in MB
.PARAMETER Showonly
    Only Shows the Current App-V Cache Size but does not change anything
.EXAMPLE
    Set-AppVCacheSize -Computer TestClient01 -Size 11000
.EXMAPLE
    Set-AppvCacheSize -Computer TestClient01 -Showonly
.NOTES
    Version 1.0, Alex Verboon
#>

    [CmdletBinding()]
    Param (
        [Parameter(Mandatory=$True,
                    ValueFromPipeline=$true,
                    ValueFromPipelineByPropertyName=$true,
                    HelpMessage= 'One or more computer names')]
        [Alias('Host','ipaddress')]
        [String[]]$ComputerName,
        [Parameter(Mandatory=$False,
        ValueFromPipeline=$true,
                    ValueFromPipelineByPropertyName=$true,
                    HelpMessage= 'Specify the new App-V Cache size in MB')]
        [String]$Size,
        [switch]$Showonly
        
        )

Begin{
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition

if ($Showonly -eq $false -and [string]::IsNullOrEmpty($Size))
{
    write-output "You must specify the -Size parameter or -Showonly"
    Exit 0
}

Function Send-File {
##############################################################################
##
## Send-File
##
## From Windows PowerShell Cookbook (O'Reilly)
## by Lee Holmes (http://www.leeholmes.com/guide)
##
## http://www.powershellcookbook.com/recipe/ISfp/program-transfer-a-file-to-a-remote-computer
##############################################################################

<#

.SYNOPSIS

Sends a file to a remote session.

.EXAMPLE

PS >$session = New-PsSession leeholmes1c23
PS >Send-File c:\temp\test.exe c:\temp\test.exe $session

#>

param(
    ## The path on the local computer
    [Parameter(Mandatory = $true)]
    $Source,

    ## The target path on the remote computer
    [Parameter(Mandatory = $true)]
    $Destination,

    ## The session that represents the remote computer
    [Parameter(Mandatory = $true)]
    [System.Management.Automation.Runspaces.PSSession] $Session
)

Set-StrictMode -Version Latest

## Get the source file, and then get its content
$sourcePath = (Resolve-Path $source).Path
$sourceBytes = [IO.File]::ReadAllBytes($sourcePath)
$streamChunks = @()

## Now break it into chunks to stream
Write-Progress -Activity "Sending $Source" -Status "Preparing file"
$streamSize = 1MB
for($position = 0; $position -lt $sourceBytes.Length;
    $position += $streamSize)
{
    $remaining = $sourceBytes.Length - $position
    $remaining = [Math]::Min($remaining, $streamSize)

    $nextChunk = New-Object byte[] $remaining
    [Array]::Copy($sourcebytes, $position, $nextChunk, 0, $remaining)
    $streamChunks += ,$nextChunk
}

$remoteScript = {
    param($destination, $length)

    ## Convert the destination path to a full filesytem path (to support
    ## relative paths)
    $Destination = $executionContext.SessionState.`
        Path.GetUnresolvedProviderPathFromPSPath($Destination)

    ## Create a new array to hold the file content
    $destBytes = New-Object byte[] $length
    $position = 0

    ## Go through the input, and fill in the new array of file content
    foreach($chunk in $input)
    {
        Write-Progress -Activity "Writing $Destination" `
            -Status "Sending file" `
            -PercentComplete ($position / $length * 100)

        [GC]::Collect()
        [Array]::Copy($chunk, 0, $destBytes, $position, $chunk.Length)
        $position += $chunk.Length
    }

    ## Write the content to the new file
    [IO.File]::WriteAllBytes($destination, $destBytes)

    ## Show the result
    Get-Item $destination
    [GC]::Collect()
}

## Stream the chunks into the remote script
$streamChunks | Invoke-Command -Session $session $remoteScript `
    -ArgumentList $destination,$sourceBytes.Length

}
### End of Send-File function

Function Set-AppVSize($Size,$Showonly)
    {
        $AppVCache = Get-ItemProperty "HKLM:SOFTWARE\Wow6432Node\Microsoft\SoftGrid\4.5\Client\AppFS" 
        $AppvCacheFile = $AppVCache.FileName
        $AppVCacheFileSize = (Get-ItemProperty -Path "$AppvCacheFile").Length /1gb
        $AppvCacheSize = $AppVCache.FileSize

            $Prop = [ordered]@{ 
                    "AppvCachefile" = $AppvCacheFile
                    "AppVCacheFileSize" = $AppvCacheFileSize
                    "AppVCacheSize" = $AppvCacheSize
                    }
                    $Obj1=New-Object -TypeName PSObject -Property $Prop
                    $obj1 | Select-Object AppvCacheFile, AppVCacheFileSize, AppVCacheSize | format-list

        if ($Showonly -eq $False)
        {
            # set Eula acceptance in registry, required to run the Microsoft AppVCacheSize.exe
            # http://www.microsoft.com/en-us/download/details.aspx?id=5927
            New-Item -Path "Registry::HKCU\Software\Microsoft\AppVTools" -ErrorAction SilentlyContinue
            New-Item -Path "Registry::HKCU\Software\Microsoft\AppVTools\CacheSizeTool" -ErrorAction SilentlyContinue
            New-ItemProperty -Path "Registry::HKCU\Software\Microsoft\AppVTools\CacheSizeTool" -Name "EulaAccepted" -PropertyType "dword" -Value "1" -ErrorAction SilentlyContinue

            #Set the App-V Cache Size
            Write-output "Configuring App-V Cache Size to $Size"
            $cmd = "C:\WINDOWS\temp\AppVCacheSize.exe" 
            $arg = "/s:" + "$size"
            Start-Process -FilePath $cmd -ArgumentList $arg
            Start-Sleep -Seconds 5
        
           # Get updated App-V Cache size information
            $AppVCache = Get-ItemProperty "HKLM:SOFTWARE\Wow6432Node\Microsoft\SoftGrid\4.5\Client\AppFS" 
            $AppvCacheFile = $AppVCache.FileName
            $AppVCacheFileSize = (Get-ItemProperty -Path "$AppvCacheFile").Length /1gb
            $NewAppvCacheSize = $AppVCache.FileSize

            $Prop = [ordered]@{ 
                    "AppvCachefile" = $AppvCacheFile
                    "AppVCacheFileSize" = $AppvCacheFileSize
                    "AppVCacheSize" = $NewAppvCacheSize
                    }
                    $Obj1=New-Object -TypeName PSObject -Property $Prop
                    $obj1 | Select-Object AppvCacheFile, AppVCacheFileSize, AppVCacheSize | format-list

        }
    } # end set appv-size
} #end begin

# -------------------------------------------------------------------------------------------
# Process AppVCacheSize Cache setting
# -------------------------------------------------------------------------------------------
Process
{
    ForEach($c in $ComputerName)
    {
        $session = New-PSSession -ComputerName $c
        write-output "Processing: $c"
        If ($Showonly -ne $True)
            {
            Send-file "$scriptPath\appvcachesize.exe" "C:\Windows\temp\appvcachesize.exe" $session
            }
        Invoke-Command -Session $session -ScriptBlock ${function:Set-AppvSize} -ArgumentList $Size,$Showonly -Verbose
        Remove-PSSession $session
    }
}

End{

}

```
