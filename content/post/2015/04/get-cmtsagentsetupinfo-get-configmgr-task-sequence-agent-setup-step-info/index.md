---
title: "Get-CMTSAgentSetupInfo (Get ConfigMgr Task Sequence Agent Setup Step Info)"
layout: "post"
date: 2015-04-04T11:49:35Z
slug: "get-cmtsagentsetupinfo-get-configmgr-task-sequence-agent-setup-step-info"
aliases:
  - "/2015/04/get-cmtsagentsetupinfo-get-configmgr-task-sequence-agent-setup-step-info/"
description: "We recently performed an upgrade of our ConfigMgr 2012 R2 Infrastructure and due to way how we install the Agent and Agent patches, we had to update t..."
author: "Alex Verboon"
tags:
  - agent
  - configmgr
  - properties
  - task-sequence
  - Windows
  - PowerShell
categories:
  - configmgr
  - Windows
  - PowerShell
---
We recently performed an upgrade of our ConfigMgr 2012 R2 Infrastructure and due to way how we install the Agent and Agent patches, we had to update the “Setup Windows and ConfigMgr” step within a number of our Task Sequences. I therefore wrote the below Get-CMTSAgentSetupInfo.ps1 PowerShell script which dumps all the ConfigMgr Agent Setup step information from all or specified task sequences.

The script retrieves the following information:

	
- Task Sequence Name
	
- Agent Instalaltion propoerties
	
- PackageID of the ConfigMgr Agent Package
	
- Package Name of the ConfigMgr Agent Package
	
- Package Source Path of the ConfigMgr Agent Package

The script can be downloaded form the Microsoft Script Center [here](https://gallery.technet.microsoft.com/scriptcenter/Get-CMTSAgentSetupInfops1-04ed5981)

```
Function Get-CMTSAgentSetupInfo
<#
.Synopsis
   This function Retrieves the ConfigMgr Agent instalaltion properities information from Task Sequences
.DESCRIPTION
   This function retrieves the ConfigMgr Agent instalaltion propoerties information from all Task Sequences
   that contain the task sequence step SMS_TaskSequence_SetupWindowsAndSMSAction. 
   The following information is gathered:

   Task Sequence Name
   Agent Instalaltion propoerties
   PackageID of the ConfigMgr Agent Package
   Package Name of the ConfigMgr Agent Package
   Package Source Path of the ConfigMgr Agent Package

.PARAMETER SiteCode
    The Site code of the Configuration Manager infrastructure
.PARAMETER SiteServer
    The name of the Configuraiton Manager Site Server
.PARAMETER TaskSequence
    String within the Task Sequence name
.EXAMPLE
   Get-CMTSAgentSetupInfo -SiteCode DEV -SiteServer CM-DEV-001
   List all Agent Setup properties of all Task Sequences

.EXAMPLE
   Get-CMTSAgentSetupInfo -SiteCode DEV -SiteServer CM-DEV-001 -TaskSequence Windows7
   List the Agent Setup propoerties for all Task Sequences that have "Windows7" in their name. 

.EXMPLE
    Get-CMTSAgentSetupInfo -SiteCode DEV -SiteServer CM-DEV-001 | EXPORT-CSV -Path C:\TEMP\tsdump1.csv -NoTypeInformation
    Export all Agent Setup propoerites to a comma seprated file

.NOTES
  https://msdn.microsoft.com/en-us/library/cc142942.aspx
#>
{
    [CmdletBinding()]
    [OutputType([int])]
    Param
    (
    [Parameter(Mandatory=$true,
    ValueFromPipelineByPropertyName=$true,
    Position=0)]
    $SiteCode,

    [Parameter(Mandatory=$true,
    ValueFromPipelineByPropertyName=$true,
    Position=1)]
    $SiteServer,

    [Parameter(Mandatory=$false,
    ValueFromPipelineByPropertyName=$true,
    Position=2)]
    $TaskSequence
    )

Begin{
    if ($PSBoundParameters.ContainsKey("TaskSequence"))
    {
         $tsquery = Get-WmiObject -Namespace "root\SMS\site_$Sitecode" -ComputerName "$SiteServer" -Class "SMS_TaskSequencePackage" | Where-Object {$_.Name -like "*$taskSequence*"}
    }
    Else
    {
        $tsquery = Get-WmiObject -Namespace "root\SMS\site_$Sitecode" -ComputerName "$SiteServer" -Class "SMS_TaskSequencePackage" 
    }
}

Process{
    $TaskSequences = $tsquery
    $TSAgentsetupInfo = @()
    $si=0

    ForEach ($ts in $TaskSequences)
    {
        $ts.get()
        $seq_xml = [XML]$ts.Sequence
        $Agent = $seq_xml.GetElementsByTagName("*") |  select-object * | Where-Object {$_.type -like "SMS_TaskSequence_SetupWindowsAndSMSAction"}

        If ([string]::IsNullOrEmpty($Agent) -eq $false)
        {      
            $InstallProperties = $Agent.defaultVarList.variable[0]."#text"
            $PackageID = $Agent.defaultVarList.variable[1]."#text"
            $PackageName = Get-CimInstance -Namespace "root\SMS\site_$Sitecode" -ComputerName "$SiteServer" -Class "SMS_package" | Where-Object {$_.PackageID -eq "$PackageID"}

            $object = New-Object -TypeName PSObject
            $object | Add-Member -MemberType NoteProperty -Name "TaskSequenceName" -Value $ts.Name
            $object | Add-Member -MemberType NoteProperty -Name "AgentInstallProperties" -Value $InstallProperties
            $object | Add-Member -MemberType NoteProperty -Name "PackageID" -Value $Packagename.PackageID
            $object | Add-Member -MemberType NoteProperty -Name "PackageName" -Value $Packagename.Name
            $object | Add-Member -MemberType NoteProperty -Name "PackageSourcePath" -Value $Packagename.PkgSourcePath
            $TSAgentsetupInfo += $object
        }
        Write-Progress -Activity "Processing $($ts.name)" -Status "Processing $si of $($TaskSequences.Count)" -PercentComplete (($si / $TaskSequences.count) * 100)
        $si++
     }
}

End {
    $TSAgentsetupInfo 
    }
}
```

