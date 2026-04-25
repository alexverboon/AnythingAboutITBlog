---
title: "Microsoft User Experience Virtualization &ndash; Part 1: The Road to UE-V"
layout: "post"
date: 2012-07-01T16:03:16Z
slug: "microsoft-user-experience-virtualization-part-1-the-road-to-ue-v"
aliases:
  - "/2012/07/microsoft-user-experience-virtualization-part-1-the-road-to-ue-v/"
description: "Many IT Administrators will agree that managing Windows user profiles can be somewhat of a challenge especially when using roaming user profiles where..."
author: "Alex Verboon"
tags:
  - folder-redirection
  - intellimirror
  - offline-files
  - roaming-profiles
  - ue-v
  - user-experience-virtualization
  - user-state-virtualization
  - usv
  - Windows
categories:
  - ue-v
  - Windows
---
Many IT Administrators will agree that managing Windows user profiles can be somewhat of a challenge especially when using roaming user profiles where data and settings can follow the user across multiple Windows Clients. The term roaming profiles was introduced in Windows NT 4.0 but my experience is that roaming profiles weren’t used much then because in these days most users just had their own dedicated desktop anyway and if roaming profiles were used then it was more for backup reasons. User data was typically stored on a home or group share and most applications were still using INI files instead of using the Windows registry. Some of you might remember the fun with [mapping INI files into the Registry](http://www.microsoft.com/resources/documentation/windowsnt/4/workstation/reskit/en-us/26_ini.mspx?mfr=true). Furthermore in these days many applications would not separate user data from application data hence the benefits of using a roaming profile were pretty limited.

  Then with Windows 2000, Microsoft introduced the [IntelliMirror](http://technet.microsoft.com/en-us/library/bb742423.aspx) management technologies, a set of features that enables users’ data, software and settings to follow them across multiple Windows Clients. IntelliMirror is not a product but a set of features built into the Windows operating system. The 3 pillars of IntelliMirror are:

     
- User Data Management    
- Software Installation and Maintenance    
- User Settings Management 

  At the same time of introducing IntelliMirror Microsoft also [announced](http://www.microsoft.com/en-us/news/press/1999/jul99/certificationpr.aspx) the Certified for Windows 2000 Program which includes guidelines for application developers to make their applications manageable through IntelliMirror e.g. separating user data and application data. 

  When companies started to deploy Windows 2000 and Active Directory it became kind of a must for IT Administrators to leverage as much as possible of the IntelliMirror features this included the use of roaming profiles. The use of roaming profiles on desktop computers that are always connected to the LAN in general works pretty smoothly; the challenges really start when using roaming profiles on laptop computers where users work offline or from a remote location.

  With the introduction of every new Windows operating system Microsoft has continued to extend and improve the features around IntelliMirror and how roaming profiles work nevertheless I have seen many companies stop using Roaming Profiles due to the various challenges in managing them especially because nowadays most users are using a laptop. 

  While in the early 2000s the term IntelliMirror was widely known across IT Administrators we don’t hear much of it these days, although still all its features continue to exist in current versions of Windows. 

  In 2010 Microsoft first introduced the term User State Virtualization (USV(. User State Virtualization is not a new product or feature but rather a terminology that describes how Roaming Profiles, Folder redirection and offline files can be used on the current Windows platform to address nowadays requirements. 

  In 2012 Microsoft is extending USV by a fourth technology called User Experience Virtualization aka UE-V. UE-V delivers a user’s personal Windows experience across many devices regardless if Windows or the applications are deployed physically or virtually. 

  With UE-V IT Administrators can make their users’ Windows and Application settings roam across different Windows devices without using roaming profiles. Just out of the box UE-V allows roaming the following Windows and Application settings:

     
- Desktop Settings    
- Ease of Access    
- Theme Settings    
- Microsoft Access 2010    
- Microsoft Excel 2010    
- Microsoft InfoPath 2010    
- Microsoft Lync 2010    
- Microsoft OneNote 2010    
- Microsoft Outlook 2010    
- Microsoft PowerPoint 2010    
- Microsoft Project 2010    
- Microsoft Publisher 2010    
- Microsoft SharePoint Workspace 2010    
- Microsoft Word 2010    
- Microsoft Visio 2010    
- Microsoft Internet Explorer 8    
- Microsoft Internet Explorer 9    
- Microsoft Internet Explorer 10    
- Microsoft Notepad    
- Microsoft WordPad    
- Microsoft Calculator 

    IT Administrators can use the UE-V Generator for creating additional application templates and then distribute those templates to their users making the settings of those applications roam as well. 

  In Part 2 I will describe how easy it is to get UE-V up and running.

