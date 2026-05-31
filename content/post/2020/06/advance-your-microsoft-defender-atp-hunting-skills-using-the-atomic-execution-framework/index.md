---
title: Advance your Microsoft Defender ATP hunting skills using the Atomic execution
  framework
layout: post
date: '2020-06-05T12:38:56Z'
slug: advance-your-microsoft-defender-atp-hunting-skills-using-the-atomic-execution-framework
aliases:
- /2020/06/advance-your-microsoft-defender-atp-hunting-skills-using-the-atomic-execution-framework/
description: Advance my hunting skills using MITRE ATT&CK and Microsoft Defender Advanced
  Threat Protection.
author: Alex Verboon
image: img/post-heroes/advance-your-microsoft-defender-atp-hunting-skills-using-the-atomic-execution-framework.png
tags:
- mitreattack
- PowerShell
categories:
- Microsoft Defender XDR
- Security
- PowerShell
---
Hello everyone, during the past months I took a closer look at [MITRE ATT&CK ](#) to advance my hunting skills using [Microsoft Defender Advanced Threat Protection](#). For those not familiar with MITRE ATT&CK, in short, it is a knowledge base knowledge base of adversary tactics and techniques based on real-world observations.

To familiarize myself with MITRE ATT&CK, I first started reading through all the tactics and techniques, to be honest while reading, I often couldn't resists to get my hands on the keyboard and try things out, but I kept discipline and completed studying all the content first.

Below is an example of Credential dumping, when you look at the MITRE ATT&CK matrix, you see that the are organized in techniques and tactics. Note that some tactics can exist in multiple technique categories, like BITS jobs, which is listed under  Defense Evasion and Persistence.

![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour1.png)

Now if you want to advance your Microsoft Defender ATP hunting skills, you need *data* to hunt for. By data I mean that we have to feed MDATP with data. A while ago I found the [Atomic Red Team](#) Git repository. This repository contains tests that allows you to execute several techniques used by adversaries and…. They are mapped to MITRE ATT&CK.

Okay enough about the theory, let's get back to the keyboard. To run the tests on Windows we first need to  install the Atomic test execution framework that's hosted here on GitHub [https://github.com/redcanaryco/invoke-atomicredteam](#) and the documentation for it can be found here: [https://github.com/redcanaryco/invoke-atomicredteam/wiki](#)

Note: I suggest that you perform the following tasks on a test client and not on your own device. Although these are just simulations and the tests do include cleanup tasks, things might be left behind that you would then have to cleanup manually. (*Like notepad and calculator that continue to startup on one of my test devices upon every user logon* )

To install the Atomic Test framework, run the following command in an elevated PowerShell prompt:
IEX (IWR 'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1');
Install-AtomicRedTeam -getAtomics -Force![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour2.png)

Run the following command to get a list of all available tests:
Invoke-AtomicTest All -ShowDetailsBrief
And you see, we have several tests for the techniques available.

![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour3.png)![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour4.png)

If you want to get more information about the individual tests, just run the following command
Invoke-AtomicTest -AtomicTechnique T1197 -ShowDetails![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour5.png)

Okay, now let's run the test, T1003 , Credential Dumping: [https://attack.mitre.org/techniques/T1003/](#)Invoke-AtomicTest -AtomicTechnique T1003![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour6.png)![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour7.png)

Now let's turn over to Microsoft Defender ATP and see what's happening there, looks like our tests created some noise.

![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour8.png)![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour9.png)

Now let me clarify a common misunderstanding, here we see that MDATP actually raised an alert for the observed activity, however that's not the case for every action, let's take [BITS Jobs](#) as an example, Bits jobs are quite common for various benign activities such as the download of the outlook address book as shown in the example below or when using ConfigMgr to deploy software.

![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour10.png)

Bottom line, if you want to detect BITS jobs related to malicious activities, you will need to 'hunt' for them. So we first run the BITS Job tests.

![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour11.png)

And then continue hunting for them through the Microsoft Defender Advanced hunting interface.
// T1197 - BITS Jobs

// Reference: https://attack.mitre.org/techniques/T1197/

DeviceProcessEvents

| where Timestamp >= ago(7d)

| where FolderPath == "C:\\Windows\\System32\\bitsadmin.exe" and ProcessCommandLine contains "http"

| project Timestamp, DeviceName, FolderPath, ProcessCommandLine, AccountDomain, AccountName, InitiatingProcessFolderPath, ProcessCreationTime, DeviceId, ReportId

| sort by Timestamp desc![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour12.png)    // Reference: https://attack.mitre.org/techniques/T1197/

let timeframe = 7d;

DeviceProcessEvents

| where Timestamp >= ago(timeframe)

| where InitiatingProcessFileName in ("powershell.exe", "POWERSHELL.EXE", "powershell_ise.exe", "POWERSHELL_ISE.EXE","pwsh.exe")

| where ProcessCommandLine has "Start-BitsTransfer" and ProcessCommandLine contains "http"

| project Timestamp, DeviceName, InitiatingProcessFileName, FileName, ProcessCommandLine, AccountDomain, AccountName, DeviceId, ReportId

| sort by Timestamp desc![](https://www.verboon.info/wp-content/uploads/2020/06/060520_1235_Advanceyour13.png)

If you want to improve your advanced hunting skills in Microsoft Defender ATP, I recommend that you execute the individual tests and then start looking at the information that Defender ATP captures and then start building your hunting queries.

Below you find some references to various collections of hunting queries:

[https://github.com/DebugPrivilege/KQL-Queries/tree/master/MDAPT](#)[https://github.com/microsoft/Microsoft-threat-protection-Hunting-Queries](#)[https://github.com/CGCFAD/WDATP-Advanced-Hunting](#)[https://github.com/richlilly2004/Microsoft-Defender-ATP](#)[https://github.com/microsoft/Microsoft-threat-protection-Hunting-Queries](#)[https://github.com/eshlomo1/WindowsDefenderATP_Advanced_Hunting_Samples_Queries](#)

If you happen to have a Pluralsight subscription, I recommend the course [Kusto Query Language (KQL) from Scratch](#)

I also recommend you follow [@DebugPrivilege](#) he's frequently tweeting new hunting queries

As always , feedback, comments are always welcome

Alex

