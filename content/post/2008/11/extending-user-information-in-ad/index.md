---
title: "Extending User Information in AD"
layout: "post"
date: 2008-11-17T19:44:51Z
slug: "extending-user-information-in-ad"
aliases:
  - "/2008/11/extending-user-information-in-ad/"
description: "The Windows 2003 Resource Kit contains a nice extension for the Active Directory Users and Computers console."
author: "Alex Verboon"
image: "img/post-heroes/extending-user-information-in-ad.png"
categories:
  - 'Windows'
tags:
  - 'Active Directory'
  - 'User-Account-Information'
---
The Windows 2003 Resource Kit contains a nice extension for the Active Directory Users and Computers console showing additional User Account information.

The additional user account information can be enabled by registering the acctinfo.dll as described below.

![ADConsole](images/image3-230x300.png)

Follow the steps below to enable the additional user account information.

  1. [Download](http://www.microsoft.com/downloads/details.aspx?familyid=9d467a69-57ff-4ae7-96ee-b18c4790cffd&displaylang=en) the Windows 2003 Resource kit tools.
  2. Unpack / Install the Windows 2003 Resource Kit
  3. Copy the acctinfo.dll to c:\windows\system32
  4. Register the DLL by running the following command:

      ```bash
      regsvr32 C:\windows\system32\acctinfo.dll
      ```	
  5. Launch the Active Directory Users and Computers management console, then select a user object and select the Additional Account Info tab.

