---
title: "How to identify ConfigMgr collections that take long to refresh"
layout: "post"
date: 2014-08-30T09:54:14Z
slug: "how-to-identify-configmgr-collections-that-take-long-to-refresh"
aliases:
  - "/2014/08/how-to-identify-configmgr-collections-that-take-long-to-refresh/"
description: "I’ve put together the below PowerShell script this week to identify collections in ConfigMgr that require the longest time to refresh. If you ever exp..."
author: "Alex Verboon"
tags:
  - collections
  - duration
  - performance
  - refresh
categories:
  - configmgr
  - powershell
---
I’ve put together the below PowerShell script this week to identify collections in ConfigMgr that require the longest time to refresh. If you ever experience a decrease in ConfigMgr collection update performance, you might want to run this script to find potential collections that have a long refresh duration. 

  

```
Function Get-CMCollectionRefreshDuration
{
<#
.Synopsis
   Get-CMCollectionRefreshDuration displays the duration of Configuration Manager refresh cycles
.DESCRIPTION
   Inefficient queries can cause long collection refresh cycles. Use the Get-CMCollectionRefreshDuration
   cmdlet to identify collections with long refresh cycles. 
.EXAMPLE
   Get-CMCollectionRefreshDuration -DataSource sqlsrv01\instance1 -Database CM_DB1

    Collection                   EvaluationStartTime          LastRefreshTime              Duration
    ----------                   -------------------          ---------------              --------
    Collection1                  30.08.2014 09:20:11          30.08.2014 09:22:45          00:02:33
    Collection2                  30.08.2014 09:27:31          30.08.2014 09:30:05          00:02:33
    Collection3                  30.08.2014 07:01:23          30.08.2014 07:03:56          00:02:33
    Collection4                  30.08.2014 07:20:38          30.08.2014 07:23:11          00:02:33
    Collection5                  30.08.2014 07:05:00          30.08.2014 07:07:33          00:02:33 

.EXAMPLE
   Get-CMCollectionRefreshDuration -DataSource sqlsrv01\instance1 -Database CM_DB1 -ShowTopCollections 100

   Lists the top 100 collections
.PARAMETER DataSource
   The name of the SQL Server that hosts the configuration manager database

   <servername\instance>

.PARAMETER Database
   The database name of the configuration manager database

.PARAMETER ShowTopCollections
   The number of collections to show that have the longers collection refresh cycle duration

#>
    [CmdletBinding()]
    Param
    (
     [Parameter(Mandatory=$false,
     Position=0,
     HelpMessage="Enter the SQL Server datasource name <server\instance>")]
     [string]$DataSource="server01\instance1",
     [Parameter(Mandatory=$false,
     Position=1,
     HelpMessage="The database name of the ConfigMgr database")]
     [string]$Database="CMDB1",
     [Parameter(Mandatory=$false,
     Position=2,
     HelpMessage="The number of top collectons to show")]
     [ValidateRange(1,10000)]
     [int]$ShowTopCollections="5" 
    )

Begin{
    # connecting to SQL server
    Try{
    $Connection = New-Object System.Data.SqlClient.SqlConnection
    $Connection.ConnectionString = "Data Source=$DataSource;Integrated Security=True"
    $Connection.Open()
    }
    Catch [Exception]
    {
        write-output "Unable to connect to $DataSource"
        Write-Output $_.Exception
        Throw
    }
    $query = "
    SELECT TOP $ShowTopCollections
        [CollectionName],
        [EvaluationStartTime],
        [LastRefreshTime],
        CAST([LastRefreshTime] - [EvaluationStartTime] as datetime) as Duration
    FROM [$Database].[dbo].[Collections]
    ORDER BY CAST([LastRefreshTime] - [EvaluationStartTime] as datetime) DESC"

    $command = $connection.CreateCommand()
    $command.CommandText = $query
    $result = $command.ExecuteReader()

    $table = new-object “System.Data.DataTable”
    $table.Load($result)
    $Connection.Close()
}

Process{
    $colupdateduration = @()
    ForEach($cud in $table)
    {
        $object = New-Object -TypeName PSObject
        $object | Add-Member -MemberType NoteProperty -Name "Collection" -Value $cud.Collectionname
        $object | Add-Member -MemberType NoteProperty -Name "EvaluationStartTime" -Value $cud.EvaluationStartTime
        $object | Add-Member -MemberType NoteProperty -Name "LastRefreshTime" -Value $cud.LastRefreshTime
        $object | Add-Member -MemberType NoteProperty -Name "Duration" -Value ($dur = Get-date $cud.Duration -Format "HH:mm:ss")
        $colupdateduration += $object
    }
}

End{
    $colupdateduration
    }
}
```

Thanks to Roger Zander and Claude Henchoz for the SQL query to find these collections.

