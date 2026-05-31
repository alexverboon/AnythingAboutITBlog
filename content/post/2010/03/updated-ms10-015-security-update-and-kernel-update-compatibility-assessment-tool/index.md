---
title: "Updated MS10-015 Security Update and Kernel Update Compatibility Assessment Tool"
layout: "post"
date: 2010-03-02T22:49:20Z
slug: "updated-ms10-015-security-update-and-kernel-update-compatibility-assessment-tool"
aliases:
  - "/2010/03/updated-ms10-015-security-update-and-kernel-update-compatibility-assessment-tool/"
description: "During the past weeks we have seen quite some messages about the [MS10-015](http://www.microsoft.com/technet/security/Bulletin/MS10-015.mspx) security..."
author: "Alex Verboon"
categories:
  - 'Security'
tags:
  - 'Compatibility'
  - 'Kernel'
---
During the past weeks we have seen quite some messages about the [MS10-015](http://www.microsoft.com/technet/security/Bulletin/MS10-015.mspx) security update which can cause bluescreens after being installed. According to a recent [post](http://blogs.technet.com/msrc/archive/2010/03/02/update-ms10-015-security-update-re-released-with-new-detection-logic.aspx) on the Microsoft Security Response Center blog there is a revised installation package for MS10-015 that prevents the update from installing if abnormal conditions exist such as an infection of a computer virus as the Alureon rootkit. More details about the updated MS10-015 security update can be found [here](http://blogs.technet.com/msrc/archive/2010/03/02/update-ms10-015-security-update-re-released-with-new-detection-logic.aspx)

  In addition Microsoft today also released the [Kernel Update Compatibility Assessment Tool](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=b8cd1888-d3d3-45a0-b494-1f1f76824d70) that allows systems administrators who are concerned about deploying MS10-015 throughout their enterprise to perform an upfront assessment to identify clients that could have a compatibility issue with MS10-015. 

  Beside the Compatibility Tool mpsyschk.exe itself Microsoft has also added a sample batch file that could be added to a corporate logon or startup script. The script executes mpsyschk.exe and reports the status into a log file that can be stored on a central share. In a very large environment you also want to consider to write the status into a local log file and collect the results through a custom inventory on your Systems Management system.

