---
title: "Group Policy Settings in Windows 10 Build 10.0.10074"
layout: "post"
date: 2015-05-16T13:29:30Z
slug: "group-policy-settings-in-windows-10-build-10-0-10074"
aliases:
  - "/2015/05/group-policy-settings-in-windows-10-build-10-0-10074/"
description: "Like with every new version of the Windows operating system we can expect new Group Policy settings. Today I took a look at Windows 10 build 10.0.1007..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Group Policy'
---
Like with every new version of the Windows operating system we can expect new Group Policy settings. Today I took a look at Windows 10 build 10.0.10074 and found the follownig settings.



     **Location**

  **Setting**

  **Description**

   Computer Configuration   Windows Components   DataCollectionAndPreviewBuilds

  Disable user control over preview builds

  This policy setting determines whether users can access the preview build controls in the Advanced Options for Windows Update. These controls are located under "Choose how preview builds are installed," and enable users to make their devices available for downloading and installing Windows preview software.  If you enable or do not configure this policy setting, users can download and install Windows preview software on their devices.  If you disable this policy setting, the item "Choose how preview builds are installed" will be unavailable.

   Computer Configuration   Windows Components    App Package Deployment

  Allow applications to share app data between users

  Enables or disables the ability for package families to share data with each other over multiple user instances.
If you enable this policy, applications that wish to share data between packages in their package family will be able to do so via a created SharedLocal folder that is specific to that package family and local machine. This folder is accessible through the Windows.Storage API.  If you disable this policy, applications will not be able to share data over multiple user instances. Pre-written shared data will persist, however. To clean, use DISM (/Get-ProvisionedAppxPackage to detect if there is any shared data, and /Remove-SharedAppxData to remove it)

   Computer Configuration   Windows Components    App Package Deployment  App Runtime

  Block launching Windows Store apps with Windows Runtime API access from hosted content

  This policy setting controls whether Windows Store apps with Windows Runtime API access directly from web content can be launched.  If you enable this policy setting, Windows Store apps with Windows Runtime API access directly from web content cannot be launched; Windows Store apps without Windows Runtime API access from web content are not affected.  If you disable or do not configure this policy setting, all Windows Store apps can be launched.

   Computer Configuration   System   Device Guard

  Turn On Virtualization Based Security

  Specifies whether Virtualization Based Security is enabled.  Virtualization Based Security uses the Windows Hypervisor to provide support for security services.  Virtualization Based Security requires Secure Boot, and can optionally be enabled with the use of DMA Protections.  DMA protections require hardware support and will only be enabled on correctly configured devices.  Virtualization Based Protection of Code Integrity  This setting enables virtualization based protection of Kernel Mode Code Integrity. When this is enabled kernel mode memory protections are enforced and the Code Integrity validation path is protected by the virtualization based security feature.  Warning: All drivers on the system must be compatible with this feature or the system may crash. Ensure that this policy setting is only deployed to computers which are known to be compatible.  LSA Credential Isolation  This setting lets you decide whether users can turn on Local Security Authority (LSA) Credential Isolation with virtualization-based security to help protect credentials.
Disabling these settings does not remove the feature from the computer.  Instead, you must also remove the security functionality from each computer, with a physically present user, in order to clear configuration persisted in Secure Boot.  Please refer to the documentation for a complete set of requirements to securely configure this feature.

   Computer Configuration   System  Device Guard

  Deploy Code Integrity Policy

  Deploy Code Integrity Policy  This policy setting lets you deploy a Code Integrity Policy to a machine to control what is allowed to run on that machine.  If you deploy a Code Integrity Policy, Windows will restrict what can run in both kernel mode and on the Windows Desktop based on the policy. To enable this policy the machine must be rebooted.  The file path must be either a UNC path (for example, \\ServerName\ShareName\SIPolicy.p7b), or a locally valid path (for example, C:\FolderName\SIPolicy.p7b).  The local machine account (LOCAL SYSTEM) must have access permission to the policy file.
If using a signed and protected policy then disabling this policy setting doesn't remove the feature from the computer. Instead, you must either:     1) first update the policy to a non-protected policy and then disable the setting, or
   2) disable the setting and then remove the policy from each computer, with a physically present user.

   User Configuration   Administrative Templates   Windows Components  File Explorer

  Turn off soft landing help tips

  Disabling soft landing messages

   Computer Configuration   Administrative Templates   System   Mitigation Options

  Untrusted Font Blocking

  This security feature provides a global setting to prevent programs from loading untrusted fonts. Untrusted fonts are any font installed outside of the %windir%\Fonts directory. This feature can be configured to be in 3 modes: On, Off, and Audit. By default, it is Off and no fonts are blocked. If you aren't quite ready to deploy this feature into your organization, you can run it in Audit mode to see if blocking untrusted fonts causes any usability or compatibility issues.

   Computer Configuration   Administrative Templates   Windows Components   Bitlocker Drive Encryption   Operating System Drives

  Configure pre-boot recovery message and URL

  This policy setting lets you configure the entire recovery message or replace the existing URL that are displayed on the pre-boot key recovery screen when the OS drive is locked.  If you select the "Use default recovery message and URL" option, the default BitLocker recovery message and URL will be displayed in the pre-boot key recovery screen. If you have previously configured a custom recovery message or URL and want to revert to the default message, you must keep the policy enabled and select the "Use default recovery message and URL" option.  If you select the "Use custom recovery message" option, the message you type in the "Custom recovery message option" text box will be displayed in the pre-boot key recovery screen. If a recovery URL is available, include it in the message.  If you select the "Use custom recovery URL" option, the URL you type in the "Custom recovery URL option" text box will replace the default URL in the default recovery message, which will be displayed in the pre-boot key recovery screen.  Note: Not all characters and languages are supported in pre-boot. It is strongly recommended that you test that the characters you use for the custom message or URL appear correctly on the pre-boot recovery screen.





 I found the references to these policy settings within the following administrative template files:

```text
C:\Windows\PolicyDefinitions\AllowBuildPreview.admx
C:\Windows\PolicyDefinitions\AppxPackageManager.admx
C:\Windows\PolicyDefinitions\AppXRuntime.admx
C:\Windows\PolicyDefinitions\DeviceGuard.admx
C:\Windows\PolicyDefinitions\Explorer.admx
C:\Windows\PolicyDefinitions\GroupPolicy.admx
C:\Windows\PolicyDefinitions\VolumeEncryption.admx
```

 The following template also contains a reference to Windows 10, but I was unable to find the related setting: `C:\Windows\PolicyDefinitions\PreviousVersions.admx`. However I noticed that within the file properties, the previous versions tab is back.


