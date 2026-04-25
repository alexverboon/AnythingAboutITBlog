---
title: "PowerShell Core logging configuration"
layout: "post"
date: 01/16/2018 22:41:16
slug: "powershell-core-logging-configuration"
aliases:
  - "/2018/01/powershell-core-logging-configuration/"
description: "After having browsed through the PowerShell code a bit, found some references as to how to configure PowerShell Core logging options through GPO or vi..."
author: "Alex Verboon"
tags:
  - group-policy
  - logging
  - powershellcore
categories:
  - powershell
---
After having browsed through the PowerShell code a bit, found some references as to how to configure PowerShell Core logging options through GPO or via a configuration file.

There are no GPO Templates available for PowerShell Core, but the same settings as are written for Windows PowerShell also apply for Core, they just live within another registry key.

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\**PowerShellCore**

So when you apply the folllowing registry settings , you can enable ScriptBlock logging and Transcripting for PowerShell Core.

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\PowerShellCore]

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\PowerShellCore\ScriptBlockLogging]
"EnableScriptBlockLogging"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\PowerShellCore\Transcription]
"EnableTranscripting"=dword:00000001
"OutputDirectory"="C:\\DEV\\CRAZYLOGS"

So until we get proper Group Policy templates, logging for PowerShell Core can be configured through Group Policy Preferences.

Reference to the source code section: "#region GroupPolicy Configs"

https://github.com/PowerShell/PowerShell/blob/d261e1f16692760db4469b44b1ca69155f6f3ada/src/System.Management.Automation/engine/PSConfiguration.cs

Another option to configure these settings , if you do are not enforcing stuff for your users, but don't want to fiddle with registry settings, is to use the confguration file.

"C:\Program Files\PowerShell\6.0.0\powershell.config.json"

that by default has the following content:

{"Microsoft.PowerShell:ExecutionPolicy":"RemoteSigned"}

Replacing it with the below configuration example will also enable PowerShell core logging options.

{
"Microsoft.PowerShell:ExecutionPolicy": "RemoteSigned",
  "PowerShellPolicies": {
    "ScriptExecution": {
      "ExecutionPolicy": "RemoteSigned",
      "EnableScripts": true
    },
    "ScriptBlockLogging": {
      "EnableScriptBlockInvocationLogging": true,
      "EnableScriptBlockLogging": true
    },
    "ModuleLogging": {
      "EnableModuleLogging": true,
      "ModuleNames": [
        "PSReadline",
        "PowerShellGet"
      ]
    },
    "ProtectedEventLogging": {
      "EnableProtectedEventLogging": false,
      "EncryptionCertificate": [
        "Joe"
      ]
    },
    "Transcription": {
      "EnableTranscripting": true,
      "EnableInvocationHeader": true,
      "OutputDirectory": "C:\\dev\\pscore6log"
    },
    "UpdatableHelp": {
      "DefaultSourcePath": "C:\\dev\\pscorehelp"
    },
    "ConsoleSessionConfiguration": {
      "EnableConsoleSessionConfiguration": false,
      "ConsoleSessionConfigurationName": "name"
    }
  },
  "LogLevel": "verbose"
}

