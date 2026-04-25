---
title: 'Microsoft User Experience Virtualization &ndash; Part 3: Creating and using
  Templates'
layout: post
date: '2012-07-04T20:32:52Z'
slug: microsoft-user-experience-virtualization-part-3-creating-and-using-templates
aliases:
- /2012/07/microsoft-user-experience-virtualization-part-3-creating-and-using-templates/
description: As explained in [Part 2 Setting up UE-V](https://www.verboon.info/index.php/2012/07/microsoft-user-experience-virtualization-part-2-setting-up-ue-v/)
  ...
author: Alex Verboon
tags:
- application
- catalog-path
- files
- generator
- registry
- template
- ue-v
- user-experience-virtualization
- walkthrough
- Windows
- Office
categories:
- ue-v
- Windows
- Office
---
As explained in [Part 2 Setting up UE-V](https://www.verboon.info/index.php/2012/07/microsoft-user-experience-virtualization-part-2-setting-up-ue-v/) out of the box UE-V has build-in support for various Windows Settings and the Office 2010 suite. But to take full advantage of UE-V you will most likely want to have you other applications roam their settings as well. For that you will have to create so called UE-V Templates. 

  Once you have created an application template you store it into the settings template catalogue, in the example I described in Part 2 this would be \\SRV010\DATA\UEVTEMPLATES that I have configured using the UE-V Group Policy Setting **Computer Configuration / Administrative Templates / Windows Components / User Experience Virtualization / Settings Template Catalog path**

  Clients that have the UE-V Agent installed by default will check for updates in the catalog path once a day and update and register the templates on the local client. If you do not want to wait another day, you can manually force the update by launching the ApplySettingsTemplateCatalog.exe stored under %program files%\Microsoft user Experience Virtualization \ Agent \ <SKU> as Administrator. 

  My original plan was to use this post to describe the process on how to create an application template using the UE-V Generator but I then realized that Helge Klein has already written an excellent post called [Walkthrough: Creating a UE-V Settings Location Template](http://helgeklein.com/blog/2012/04/walkthrough-creating-a-ue-v-settings-location-template/). So I suggest that once you have installed the UE-V Generator (ToolsSetup.exe is included in the UE-V installation sources and you must also install the Visual C++ 2010 redistributable) you continue reading Helge-s [post](http://helgeklein.com/blog/2012/04/walkthrough-creating-a-ue-v-settings-location-template/) on how to create an application template. 

  If you want to try out some existing templates then have a look at the UE-V Templates stored in the TechNet Gallery [here](http://gallery.technet.microsoft.com/site/search?f%5B0%5D.Type=RootCategory&f%5B0%5D.Value=UE-V)

