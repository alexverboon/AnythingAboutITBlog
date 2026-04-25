---
title: "User Profile Hive Cleanup Service Installation (UPHClean)"
layout: "post"
date: 2008-10-23T20:11:34Z
slug: "user-profile-hive-cleanup-service-installation-uphclean"
aliases:
  - "/2008/10/user-profile-hive-cleanup-service-installation-uphclean/"
description: "Today's challenge was to get UPHClean.msi installing correctly. You would think that installing an MSI package is an easy thing to do, so thought I. B..."
author: "Alex Verboon"
tags:
  - profiles
  - Windows
categories:
  - automation
  - deployment
  - tip
---
Today's challenge was to get UPHClean.msi installing correctly. You would think that installing an MSI package is an easy thing to do, so thought I. But unfortunately MSI is not always MSI. Looking at all the posts on the web, it seems I was not the only one who had a bit of a challenge getting this installed in an automated way.

When launching the UPHClean.msi manually all works fine, software installs, service gets registered and the package is being listed in the Add/Remove programs list.

I had created a batch file that would automatically remotely install this MSI on a client, apparently that would not work. Software gets installed but not properly registered.

By default most system management tools install software under the Windows SYSTEM account unless specified differently. So did I with UPHClean-setup.msi.

**SOLUTION !**

Once i had defined the UPHClean-setup.msi to be installed under the "Administrators" context, it all got installed as expected.

Update: 27. October 2008: I was partually wrong, although it seemed to install correctly, it still doesn't seem to be perfect. But my colleague told me that with "%ProgramFiles%\uphclean\uphclean.exe" -install it seems to work.

Robin Caron, who has developped UPHClean at Microsoft has a [blog site](http://blogs.technet.com/uphclean/), i think i will drop him a note on this, since many people have kind of a challenge to get this right.

Download UPHClean-Setup.msi from Microsoft [here](http://www.microsoft.com/downloads/details.aspx?FamilyId=1B286E6D-8912-4E18-B570-42470E2F3582&displaylang=en)

