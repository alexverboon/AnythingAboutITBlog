---
title: "GP Preferences"
layout: "post"
date: 2008-08-15T15:58:36Z
slug: "gp-preferences"
aliases:
  - "/2008/08/gp-preferences/"
description: "In 2006 Microsoft acquired the company DesktopStandard"
author: "Alex Verboon"
tags:
  - group-policy
  - vista
  - Windows
categories:
  - GroupPolicy
---
In 2006 Microsoft acquired the company DesktopStandard known for its extending Group Policy products GPVault and PolicyMaker.

While GPVault has become part of Microsofts MDOP suite that is available only for Enterprise customers that have a Software Assurance contract, the Policy Maker features have been available to everyone.

The PolicyMaker GPO extensions are now called GP Preferences.

GPO Preferences can be managed directly from a Windows 2008 system that has the latest GPMC installed or through a Windows Vista client with RSAT installed.
With GP Preferences you can now manage Windows 2008 server, Windows Vista, Server 2003 SP1 and Windows XP SP2.

What can I do with these GP Preferences ? Well, GPO preferences go beyond what we used to do with Group Policy settings today, furthermore while GPO policies are being enforced, with GP Preferences a user might still have the possibility to change things.

With GP Preferences, you can now customize all those things that you would typically do through a logon script, software packaging or by putting the settings into an image.

The big advantage is that now you can do this all from the same management console where you manage your Group Policy settings.

To give you an idea of what GP Preferences can do:

- Configure Power Settings
- Drive Mappings
- Map local / network printer
- Create / Change Folders, Files and Registry settings
- Configure Applications through extensions.

Furthermore , and I found this an extremely useful feature, you can target the GP preferences. As an example, you can first define power settings or power schemes and then add a query so that the GP preference is only being applied if the query matches that device or user, let's say, only apply the power settings if the system is a notebook.

Give it a try, if you already have a test environment available all you need to do is the following:

1. Install a Windows 2008 server or RSAT on Windows Vista SP1
2. Open the Group Policy Management Console and create a new GPO Object.
3. Within the GPO object create a new Preference, for example an environment variable that is set at system level
4. Link the Group Policy object you just created to the OU where you have your test machine computer objects stored
5. On the client machine run gpupdate /force to pull down the new GPO settings.

If you are using a Windows XP client, you will first need to install the client side extensions that can be downloaded from Microsoft.

Resources:

- [A Guide to Group Policy Preferences for Users of PolicyMaker Standard Edition](http://www.microsoft.com/downloads/details.aspx?FamilyID=8D5F2917-7B6D-460D-83C1-497B721D666C&displaylang=en)
- [Group Policy Preferences Overview](http://www.microsoft.com/downloads/details.aspx?familyid=42E30E3F-6F01-4610-9D6E-F6E0FB7A0790&displaylang=en)
- [Group Policies on TechNet](http://technet.microsoft.com/en-us/windowsserver/grouppolicy/default.aspx)
- [Group Policy Preference Client Side Extensions for Windows XP (KB943729)](http://www.microsoft.com/downloads/details.aspx?FamilyID=e60b5c8f-d7dc-4b27-a261-247ce3f6c4f8&DisplayLang=en)

