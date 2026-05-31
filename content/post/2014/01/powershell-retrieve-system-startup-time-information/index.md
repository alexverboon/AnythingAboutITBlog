---
title: PowerShell - Retrieve System Startup Time Information
layout: post
date: '2014-01-06T20:02:18Z'
slug: powershell-retrieve-system-startup-time-information
aliases:
- /2014/01/powershell-retrieve-system-startup-time-information/
description: The below script gathers the following system startup time information
  from a local or remote client. - Computername - Last Wakeup time (from Sleep, H...
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Startup'
  - 'Boot-Time'
---
The below script gathers the following system startup time information from a local or remote client. 

  
- Computername  
- Last Wakeup time (from Sleep, Hibernate or Fast boot on Windows 8x clients)
The last wakeup date/time is converted from UTC into the client local time.  
- Last Boot time  
- The Time Zone of the client  
- The system wakeup / sleep message from the Windows event log

 Important: the script uses PowerShell remoting, it’s therefore required that the targeted clients have WinRM enabled. 

```
Function Get-SystemStartInfo()
 {
 <#
 .Synopsis
 Get System Boot / Wake-up Time 
 .DESCRIPTION
 This script retrieves system boot and wakeup times from the specified client(s). 
 On Windows 8x clients, the last Wake-up time is the last time the system performed a 
 fast boot. 
 .PARAMETER Computer
 The name of one or multiple clients
 .EXAMPLE
 Get-SystemStartInfo localhost, dev001 | Format-Table -AutoSize

 Computer LastWakeupTime LastBootTime TimeZone 
 -------- -------------- ------------ -------- 
 localhost 1/5/2014 11:55:41 PM 1/5/2014 2:35:44 PM (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm,...
 dev001 1/5/2014 11:55:41 PM 1/5/2014 2:35:44 PM (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm,...

.NOTES
 WinRM must be enabled on remote clients
 #>
 
[CmdletBinding()]
 Param(
    [Parameter(Mandatory=$true,
    ValueFromPipelineByPropertyName=$true,HelpMessage="Enter Computername(s)",
    Position=0)]
    [Alias("ipaddress","host")]
    [String[]]$Computer
    )

Begin
{
    Function Get-LocalTime($UTCTime,$Comp)
    {
        #Credits to Tao Yang for the Get-LocalTime function
        #http://blog.tyang.org/2012/01/11/powershell-script-convert-to-local-time-from-utc/
        #$strCurrentTimeZone = (Get-WmiObject win32_timezone).StandardName
        $strCurrentTimezone = Get-CimInstance -ComputerName $Comp -Namespace root/CIMV2 -ClassName win32_TimeZone | Select-Object -ExpandProperty StandardName -ErrorAction SilentlyContinue
        $TZ = [System.TimeZoneInfo]::FindSystemTimeZoneById($strCurrentTimeZone) 
        $LocalTime = [System.TimeZoneInfo]::ConvertTimeFromUtc($UTCTime, $TZ)
        Return $LocalTime, $TZ
    }
}
Process
{
    $SystemStartInfo=@()
    foreach ($c in $Computer)
    {
        Write-Output "Processing $c"
        if (Test-Connection -ComputerName $c -Quiet -Count 3 )
        {
            # The last boot date time
            $LBootLocal = Get-CimInstance -ComputerName $c -Namespace root/CIMV2 -ClassName Win32_OperatingSystem -ErrorAction SilentlyContinue | Select -ExpandProperty LastBootuptime -ErrorAction SilentlyContinue
            If([string]::IsNullOrEmpty($LBootLocal) -eq $true)
            {
                # No last boot time found
                $LBootLocal=""
            }
            
            $PowerEvent = Invoke-Command -ComputerName $c -ScriptBlock {
            $orgCulture = Get-Culture
            [System.Threading.Thread]::CurrentThread.CurrentCulture = New-Object "System.Globalization.CultureInfo" "en-US"
            $PowerEvent = Get-WinEvent -ProviderName "Microsoft-Windows-Power-Troubleshooter" -MaxEvents 1 -ErrorAction SilentlyContinue | Where-Object { $_.id -eq 1 } | Select-Object -ExpandProperty  Message -ErrorAction SilentlyContinue
            [System.Threading.Thread]::CurrentThread.CurrentCulture = $orgCulture
            return $PowerEvent
            } 
            
            If($PowerEvent.count -gt 0)
            {
                # Extract the Date / Time information when the system woke up
                $wake = ($PowerEvent.Replace("`n","@").split("@")[3]).replace("Wake Time: ","")
                [string]$utcyear = $wake.Substring(1,4)
                [string]$utcmonth = $wake.Substring(8,2)
                [string]$utcday = $wake.Substring(13,2)
                [string]$utchour = $wake.Substring(16,2)
                [string]$utcminute = $wake.Substring(19,2)
                [string]$utcseconds = $wake.Substring(22,2)
                $wakedt = $utcyear + $utcmonth + $utcday + $utchour + $utcminute + $utcseconds

                $Culture = [System.Globalization.CultureInfo]::InvariantCulture 

                #The datetime in UTC format
                $LWUTC = [datetime]::ParseExact($wakedt,"yyyyMMddHHmmss",$Culture)
                # The datetime in Local Time format
                $LWLocal = Get-LocalTime $LWUTC $c
            }
            Else
            {
                #No last wake up event found, so let's just get the TimeZone information
                $TZName = Get-CimInstance -ComputerName $c -Namespace root/CIMV2 -ClassName win32_TimeZone | Select-Object -ExpandProperty StandardName -ErrorAction SilentlyContinue
                $TZ = [System.TimeZoneInfo]::FindSystemTimeZoneById($TZName) 
                $LWLocal = "","$TZ"
                $PowerEvent = ""
            }

            $object = New-Object -TypeName PSObject
            $object | Add-Member -MemberType NoteProperty -Name "Computer" -Value $c
            $object | Add-Member -MemberType NoteProperty -Name "LastWakeupTime" -Value $LWLocal[0]
            $object | Add-Member -MemberType NoteProperty -Name "LastBootTime" -Value $LBootLocal
            $object | Add-Member -MemberType NoteProperty -Name "TimeZone" -Value $LWLocal[1]
            $object | Add-Member -MemberType NoteProperty -Name "Message" -Value $PowerEvent
            $SystemStartInfo += $object
        }
Else
        {
        Write-Verbose "Unable to connect to $c"
        }
    }
}
End
{
    return $SystemStartInfo 
}
}

```

Example:

```
Get-Systemstartupinfo client1,client2,client3,client4,client5, client6 | format-list

```

Computer       : client1
LastWakeupTime : 
LastBootTime   : 24.12.2013 12:28:41
TimeZone       : (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna
Message        : 

Computer       : client2
LastWakeupTime : 06.01.2014 08:33:04
LastBootTime   : 06.01.2014 08:29:08
TimeZone       : (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna
Message        : The system has resumed from sleep.
                 
                 Sleep Time: ?2014?-?01?-?06T07:32:42.550130000Z
                 Wake Time: ?2014?-?01?-?06T07:33:04.780800500Z
                 
                 Wake Source: Device -Intel(R) 82579LM Gigabit Network Connection

Computer       : client3
LastWakeupTime : 29.12.2013 19:17:22
LastBootTime   : 06.01.2014 00:55:57
TimeZone       : (UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi
Message        : The system has resumed from sleep.
                 
                 Sleep Time: ?2013?-?12?-?29T11:05:17.427355600Z
                 Wake Time: ?2013?-?12?-?29T11:17:22.762004000Z
                 
                 Wake Source: Power Button

Computer       : client4
LastWakeupTime : 06.01.2014 10:03:57
LastBootTime   : 06.01.2014 09:55:36
TimeZone       : (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna
Message        : The system has resumed from sleep.
                 
                 Sleep Time: ?2014?-?01?-?06T09:01:05.727399400Z
                 Wake Time: ?2014?-?01?-?06T09:03:57.248801300Z
                 
                 Wake Source: Power Button

Computer       : client5
LastWakeupTime : 13.12.2013 13:27:33
LastBootTime   : 06.01.2014 09:28:39
TimeZone       : (UTC) Dublin, Edinburgh, Lisbon, London
Message        : The system has resumed from sleep.
                 
                 Sleep Time: ?2013?-?12?-?13T12:32:42.342018800Z
                 Wake Time: ?2013?-?12?-?13T13:27:33.513115200Z
                 
                 Wake Source: Device -USB Root Hub

Computer       : client6
LastWakeupTime : 
LastBootTime   : 06.01.2014 01:23:48
TimeZone       : (UTC+10:00) Canberra, Melbourne, Sydney
Message        :

