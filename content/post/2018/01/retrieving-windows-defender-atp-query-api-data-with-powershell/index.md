---
title: Retrieving Windows Defender ATP query API data with PowerShell
layout: post
date: '2018-01-09T20:45:15Z'
slug: retrieving-windows-defender-atp-query-api-data-with-powershell
aliases:
- /2018/01/retrieving-windows-defender-atp-query-api-data-with-powershell/
description: I am currently working on some automation around Windows Defender, so
  started to look at the Windows Defender Advanced Threat Protection query API. No...
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Windows'
  - 'API'
---
I am currently working on some automation around Windows Defender, so started to look at the Windows Defender Advanced Threat Protection query API.

Note that this API is still in preview. I wrote two functions for this.

**Connect-WindowsATP** is used to get an access token. Note that you will need to first register the API in Azure Directory so that you get an Application ID that you have to include at the top of the script.

**Get-WinATPData** uses the access token to retrieve the data from the API

You will also need the AzureAD PowerShell module installed. The script checks for it's presence.

```powershell
Function Connect-WindowsATP
{
<#
.Synopsis
   Connect-WindowsATP
.DESCRIPTION
   Connect-WindowsATP retrieves an access token to connect to the Defender ATP API
.PARAMETER Credential
   Specifies a user name for the credential, such as foo@corp.org
    If you omit this parameter, you are prompted for a user name and a password.
.EXAMPLE
   Connect-WindowsATP
   The above command prompts for user credentials and will then return the access token.
.EXMPLE
    $cr = Get-Credential
    Connect-WindowsATP -Credential $cr
    The above command uses the $cr variable as credential input and returns the Access Token.
.NOTES
    # Useful resources i found related to connecting to the Microsoft Graph API
    # https://www.michev.info/Blog/Post/1771/hacking-your-way-around-modern-authentication-and-the-powershell-modules-for-office-365
    # https://www.michev.info/Blog/Post/1771/hacking-your-way-around-modern-authentication-and-the-powershell-modules-for-office-365
    # http://www.powershell.no/azure,graph,api/2017/10/30/unattended-ms-graph-api-authentication.html
    # https://blog.kloud.com.au/2017/05/22/a-quick-start-guide-to-leveraging-the-azure-graph-api-with-powershell-and-oauth-2-0/
    # https://docs.microsoft.com/en-us/intune/intune-graph-apis
    # http://duffney.io/AddCredentialsToPowerShellFunctions
.VERSION
    1.0, 09.01.2018, alex verboon
#>
 [CmdletBinding()]
 Param(
        # Credentials to connect to Microsoft graph i.e. foo@corp.org
        [ValidateNotNull()]
        [System.Management.Automation.PSCredential]
        [System.Management.Automation.Credential()]
        $Credential = [System.Management.Automation.PSCredential]::Empty
 )
Begin{
    ## !!! ADD YOUR CLIENT ID HERE !!!! ##
    $client_id = "<CLIENT ID>" # The Azure AD Application ID for Defender ATP Preview
    # Check if AzureAD PowerShell Module is installed
    $AadModule = Get-Module -Name "AzureAD" -ListAvailable
    if ($AadModule -eq $null) {
        write-host
        write-host "AzureAD Powershell module not installed..." -f Red
        write-host "Install by running 'Install-Module AzureAD' from an elevated PowerShell prompt" -f Yellow
        write-host "Script can't continue..." -f Red
        write-host
        Throw
    }
    # Getting path to ActiveDirectory Assemblies
    # If the module count is greater than 1 find the latest version
    if ($AadModule.count -gt 1) {
        $Latest_Version = ($AadModule | select version | Sort-Object)[-1]
        $aadModule = $AadModule | ? { $_.version -eq $Latest_Version.version }
        $adal = Join-Path $AadModule.ModuleBase "Microsoft.IdentityModel.Clients.ActiveDirectory.dll"
        #$adalforms = Join-Path $AadModule.ModuleBase "Microsoft.IdentityModel.Clients.ActiveDirectory.Platform.dll"
    }
    else {
        $adal = Join-Path $AadModule.ModuleBase "Microsoft.IdentityModel.Clients.ActiveDirectory.dll"
        #$adalforms = Join-Path $AadModule.ModuleBase "Microsoft.IdentityModel.Clients.ActiveDirectory.Platform.dll"
    }
    # Load Microsoft.IdentityModel.Clients.ActiveDirectory DLL
    Add-Type -Path "$adal"
    # not needed here, but leave the code in anyway.
    # $cache = [Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache]::DefaultShared
    # $cache.ReadItems() | select DisplayableId, Authority, ClientId, Resource
    # $cacheToken = $cache.ReadItems() | Select-Object -ExpandProperty AccessToken
}
Process{
        $authContext = New-Object "Microsoft.IdentityModel.Clients.ActiveDirectory.AuthenticationContext" -ArgumentList 'https://login.microsoftonline.com/common/oauth2/token'
        if($Credential -ne [System.Management.Automation.PSCredential]::Empty)
        {
            Write-Verbose "Credentials already provided"
        }
        Else
        {
            Write-Verbose "No credentials, so prompt user"
            $Credential = Get-Credential
        }
        $AADcredential = New-Object "Microsoft.IdentityModel.Clients.ActiveDirectory.UserPasswordCredential" -ArgumentList $Credential.UserName,$Credential.Password
        $authResult = [Microsoft.IdentityModel.Clients.ActiveDirectory.AuthenticationContextIntegratedAuthExtensions]::AcquireTokenAsync($authContext,"https://graph.microsoft.com",$client_Id,$AADcredential)
        $AccessToken = $authResult.Result.AccessToken
}
End{
    If([string]::IsNullOrEmpty($AccessToken))
    {
        write-host "Unable to retrieve Access Token" -f Red
    }
    Else
    {
        $AccessToken
    }
}
}
```powershell
```powershell
Function Get-WinATPData
{
<#
.Synopsis
   Get-WinATPData
.DESCRIPTION
   Get-WinATPData retrieves data from the Windows Defender ATP query APIs.
    This is just an experimental function to become familiar with retrieving Windows Defender ATP data
    through the query API.
    Note! at present the API is in preview mode only: https://graph.microsoft.com/testwdatppreview
.EXAMPLE
    $AToken = Connect-WindowsATP
    Get-WinATPData -AccessToken $AToken -ATPSource Machine
    The command first retrrieves an access token and then queries Machine information from Defender ATP
.EXAMPLE
    $AToken = Connect-WindowsATP
    Get-WinATPData -AccessToken $AToken -ATPSource Alerts
    The command first retrrieves an access token and then queries Alert information from Defender ATP
.EXAMPLE
    $AToken = Connect-WindowsATP
    Get-WinATPData -AccessToken $AToken -ATPSource User -UserID Johndoe
    The command first retrrieves an access token and then queries user information from Defender ATP
.NOTES
    MS docs reference: https://docs.microsoft.com/en-us/windows/threat-protection/windows-defender-atp/supported-apis-windows-defender-advanced-threat-protection
    version 1.0, 09.01.2018, alex verboon
#>
[CmdletBinding()]
Param(
        # Access Token
        [Parameter(Mandatory=$true,
                   ValueFromPipelineByPropertyName=$true,
                   Position=0)]
        [ValidateNotNullOrEmpty()]
        [string]$AccessToken,
        # ATP Data Source
        [Parameter(Mandatory=$true,
                   ValueFromPipelineByPropertyName=$true,
                   Position=0)]
        [ValidateSet("Machine","User","Alerts")]
        [string]$ATPSource)
        # Dynamic Parameters
        DynamicParam{
        If ($ATPSource -eq "User")
        {
                $IDAttribute = New-Object System.Management.Automation.ParameterAttribute
                $IDAttribute.Mandatory = $true
                #create an attributecollection object for the attributes we just created.
                $attributeCollection = new-object System.Collections.ObjectModel.Collection[System.Attribute]
                $attributeCollection.Add($IDAttribute)
                #add our paramater specifying the attribute collection
                $IDParam = New-Object System.Management.Automation.RuntimeDefinedParameter('UserID', [string], $attributeCollection)
                #expose the name of our parameter
                $paramDictionary = New-Object System.Management.Automation.RuntimeDefinedParameterDictionary
                $paramDictionary.Add('UserID', $IDParam)
                return $paramDictionary
        }
}
Begin{
    If ($PSBoundParameters["AccessToken"])
    {
        Write-Verbose "Access Token was provided"
        $Authorization = [pscustomobject]@{
        access_token = "$accessToken"
        }
    }
    Else
    {
        # should not happen since require validate the parameter and to be not empty
        Throw
    }
      Switch ($ATPSource)
      {
        "Machine" {$atpuri = "https://graph.microsoft.com/testwdatppreview/machines"}
        "User" {$atpuri = ('https://graph.microsoft.com/testwdatppreview/users/USERID').Replace("USERID","$($IDParam.value)")}
        "Alerts" {$atpuri = "https://graph.microsoft.com/testwdatppreview/alerts"}
      }
}
Process{
    Write-Verbose "ATP DataSource: $ATPSource"
    Write-Verbose "ATP URI: $atpuri"
    # Retrieve the data
    Try{
        $ATPData = Invoke-RestMethod   -Headers @{Authorization =("Bearer "+ $Authorization.access_token)} -Uri $atpUri
    }
    Catch{
        Write-host "StatusCode:" $_.Exception.Response.StatusCode.value__
        Write-host "StatusDescription:" $_.Exception.Response.StatusDescription
    }
}
End{
      Switch ($ATPSource)
      {
        "Machine" {$result = $ATPData.value}
        "User" {$result = $ATPData}
        "Alerts" {$result = $ATPData.value}
      }
    $result
}
}
```

Have fun querying the Windows Defender ATP query API
