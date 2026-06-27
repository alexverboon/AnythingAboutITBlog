---
title: "New Group Policy Settings in Windows 8 Consumer Preview"
layout: "post"
date: 2012-02-29T23:45:24Z
slug: "new-group-policy-settings-in-windows-8-consumer-preview"
aliases:
  - "/2012/02/new-group-policy-settings-in-windows-8-consumer-preview/"
description: "Today, oh that was yesterday already, Microsoft released the Windows 8 Consumer Preview, so I did what I always do when there is a new Windows Operati..."
author: "Alex Verboon"
image: "img/post-heroes/new-group-policy-settings-in-windows-8-consumer-preview.png"
categories:
  - 'Windows'
tags:
  - 'Group Policy'
  - 'New-Settings'
---
Today, oh that was yesterday already, Microsoft released the Windows 8 Consumer Preview, so I did what I always do when there is a new Windows Operating system and that is looking for any new Group Policy settings. I do that by simply opening the group policy editor (gpedit.msc) select the Administrative Templates node and then go to All Settings, sort them alphabetically by Setting name and just go down the list and look for any policies where the requirement is defined to “At least Windows 8”. And this is what I have been doing for the last 3 hours. The task might look boring but I can tell you this is a good way to learn about new things.

  ![image](images/image_thumb.png)

  Below you find a list of new settings I have found, well possible that I missed one or the other setting, but in any case there are quite some interesting new things to explore.

  **Computer Configuration**

  Control Panel/Personalization

  ·         Prevent changing start menu background

  Network/Background Intelligent Transfer Service (BITS)

  ·         Set default download behavior for BITS jobs on costed networks

  Network/BranchCache

  ·         Configure Hosted Cache Servers

  ·         Enable Automatic Hosted Cache Discovery by Service Connection Point

  ·         Set age for segments in the data cache

  ·         Specify the age in days for which segments in the data cache are valid

  Network/DNS Client

  ·         Allow NetBT queries for fully qualified domain names IDN mapping

  ·         Prefer link local responses over DNS when received over a network with higher precedence

  ·         Turn off IDN encoding

  ·         Turn off smart multi-homed name resolution

  ·         Turn off smart protocol reordering

  Network/Lanman Server

  ·         Hash Version support for BranchCache

  Network/Network Connectivity Status Indicator

  ·         Specify passive polling

  Network/Network Isolation

  ·         Private network ranges for Metro style apps

  ·         Proxy definitions are authoritative

  ·         Subnet definitions are authoritative

  Network/Offline Files

  ·         Enable file synchronization on costed networks

  ·         Remove "Work offline" command

  Network/Windows Connection Manager

  ·         Disable power management in connected standby mode

  ·         Minimize the number of simultaneous connections to the Internet or a Windows Domain

  ·         Prohibit connection to roaming Mobile Broadband networks

  Network/WLAN Service/WLAN Media Cost

  ·         Set Cost

  Network/WWAN Service/WWAN Media Cost

  ·         Set 4G Cost

  Printers

  ·         Always rasterize content to be printed using a software rasterizer

  ·         Change Microsoft XPS Document Writer (MXDW) default output format to the legacy Microsoft XPS format (*.xps)

  ·         Do not allow v4 printer drivers to show printer extensions

  ·         Isolate print drivers from applications

  System/Access Denied Remediation

  ·         Access Denied Remediation configuration for Access Denied errors

  ·         Access Denied Remediation configuration for File Not Found errors Enabled Local Group Policy

  System/Early Launch Antimalware

  ·         Boot-Start Driver Initialization Policy

  System/File Classification Infrastructure

  ·         File Classification Infrastructure: Display Classification tab in Windows Explorer

  ·         File Classification Infrastructure: Specify Classification Properties List

  System/Folder Redirection

  ·         Redirect folders on primary computers only

  System/Group Policy

  ·         Turn off Group Policy Client Service AOAC optimization

  System/Internet Communication Management/Internet Communication settings

  ·         Turn off access to the Store

  System/KDC

  ·         Support Dynamic Access Control and Kerberos armoring

  System/Kerberos

  ·         Disable revocation checking for the SSL certificate of KDC proxy servers

  ·         Fail authentication requests when Kerberos armoring is not available

  ·         Set maximum Kerberos SSPI context token buffer size

  ·         Specify KDC proxy servers for Kerberos clients

  ·         Support authorization with client device information

  System/Logon

  ·         Do not enumerate connected users on domain-joined computers

  ·         Enumerate local users on domain-joined computers Enabled Local Group Policy

  ·         Turn off app notifications on the lock screen

  ·         Turn off PIN logon and picture password logon

  System/Net Logon/DC Locator DNS Records

  ·         Do not use NetBIOS-based discovery for domain controller location when DNS-based discovery fails

  System/Shutdown

  ·         Require use of hybrid boot

  System/Troubleshooting and Diagnostics/Application Compatibility Diagnostics

  ·         Detect compatibility issues for applications and drivers

  System/User Profiles

  ·         Download roaming profiles on primary computers only

  ·         User management of sharing user name, account picture, and domain information with metro-styled apps

  System/Windows Proximity Service

  ·         Turn off the Windows Proximity Service

  Windows Components/App Package Deployment

  ·         Allow all trusted apps to install

  ·         Allow deployment operations in special profiles

  Windows Components/BitLocker Drive Encryption/Fixed Data Drives

  ·         Configure use of hardware-based encryption for fixed data drives

  Windows Components/BitLocker Drive Encryption/Operating System Drives

  ·         Allow network unlock at startup

  ·         Allow Secured Boot for integrity validation

  ·         Configure TPM platform validation profile for BIOS-based firmware configurations

  ·         Configure TPM platform validation profile for native UEFI firmware configurations

  ·         Configure use of hardware-based encryption for operating system drives

  ·         Configure use of passwords for operating system drives

  ·         Enable use of BitLocker authentication requiring preboot keyboard input on slates

  ·         Reset platform validation data after BitLocker recovery

  Windows Components/BitLocker Drive Encryption/Removable Data Drives

  ·         Configure use of hardware-based encryption for removable data drives

  ·         Enforce drive encryption type on removable data drives

  Windows Components/Credential User Interface

  ·         Do not display the password reveal button

  Windows Components/Desktop Window Manager

  ·         Use solid color for Start background

  Windows Components/Device and Driver Compatibility

  ·         Device compatibility settings

  ·         Driver compatibility settings

  Windows Components/File History

  ·         Turn off File History

  Windows Components/Location and Sensors/Windows Location Provider

  ·         Turn off Windows Location Provider

  Windows Components/Maintenance Scheduler

  ·         Automatic Maintenance Random Delay

  ·         Automatic Maintenance WakeUp Policy

  Windows Components/Portable Operating System

  ·         Allow hibernate (S4) when starting from a Windows To Go workspace

  ·         Allow standby sleep states (S1-S3) when starting from a Windows to Go workspace

  ·         Windows To Go Default Startup Options

  Windows Components/Remote Desktop Services/Remote Desktop Connection Client

  ·         Turn Off UDP On Client

  Windows Components/Remote Desktop Services/Remote Desktop Session Host/Connections

  ·         Turn Off Network Detection On Server

  ·         Turn Off UDP On Server

  Windows Components/Search

  ·         Always use automatic language detection when indexing content and properties

  Windows Components/Setting Synch

  ·         Do not synchronize user application settings

  ·         Do not synchronize user credentials

  ·         Do not synchronize user desktop themes

  ·         Do not synchronize user personalization settings

  ·         Do not synchronize user settings

  ·         Do not synchronize user web browser settings

  ·         Do not synchronize user Windows settings

  Windows Components/Store

  ·         Turn off Automatic Download of updates

  ·         Turn off the Store application

  Windows Components/Windows Explorer

  ·         Allow the use of remote paths in file shortcut icons

  ·         Configure Windows SmartScreen

  ·         Pick one of the following settings

  ·         Do not show the 'new application installed' notification

  ·         Location where all default Library definition files for users/machines reside.

  ·         Default Libraries definition location

  ·         Show hibernate in the power options menu

  ·         Show lock in the user tile menu

  ·         Show sleep in the power options menu

  ·         Start Windows Explorer with ribbon minimized

  ·         Pick one of the following settings

   Windows Components/Windows Installer

  ·         Prevent embedded UI

  ·         Turn off shared components

  Windows Components/Windows Update

  ·         Let the service shut down when it is idle



  **User Configuration**

  Network/Offline Files

  ·         Remove "Work offline" command

  Start Menu and Taskbar

  ·         Clear history of tile notifications on exit

  ·         Do not show the Start Menu when the user logs in

  ·         Prevent users from uninstalling applications from Start

  ·         Show "Run as different user" command on Start

  Start Menu and Taskbar/Notifications

  ·         Turn off all notifications

  ·         Turn off toast notifications

  ·         Turn off toast notifications on the lock screen

  Start Menu and Taskbar/Push Notifications

  ·         Turn off notification cloud usage

  System/Folder Redirection

  ·         Do not automatically make specific redirected folders available offline

  ·         Enable optimized move of contents in Offline Files cache on Folder Redirection server path change

  ·         Redirect folders on primary computers only

  System/Internet Communication Management/Internet Communication settings

  ·         Turn off access to the Store

  Windows Components/Credential User Interface

  ·         Do not display the password reveal button

  Windows Components/Edge UI

  ·         Turn off Backstack

  ·         Turn off tracking of app usage

  Windows Components/IME

  ·         Do not include Non-Publishing Standard Glyph in the candidate list

  ·         Restrict character code range of conversion

  ·         Turn off custom dictionary

  ·         Turn off history-based predictive input

  ·         Turn off Internet search integration

  ·         Turn off Open Extended Dictionary

  ·         Turn off saving auto-tuning data to file

  ·         Turn on misconversion logging for misconversion report

  Windows Components/Search

  ·         Turn off storage and display of search history

  Windows Components/Store

  ·         Turn off the Store application

  Windows Components/Windows Explorer

  ·         Start Windows Explorer with ribbon minimized


