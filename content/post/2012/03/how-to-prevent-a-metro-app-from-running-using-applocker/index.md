---
title: "How to prevent a Metro App from running using Applocker"
layout: "post"
date: 2012-03-01T22:12:22Z
slug: "how-to-prevent-a-metro-app-from-running-using-applocker"
aliases:
  - "/2012/03/how-to-prevent-a-metro-app-from-running-using-applocker/"
description: "In Windows 8 the Applocker feature has been extended to support management of metro style apps. Enterprise administrators can define a Packaged app Ru..."
author: "Alex Verboon"
image: "img/post-heroes/how-to-prevent-a-metro-app-from-running-using-applocker.png"
categories:
  - 'Windows'
tags:
  - 'Applocker'
  - 'Enterprise'
---
In Windows 8 the Applocker feature has been extended to support management of metro style apps. Enterprise administrators can define a Packaged app Rule to allow or deny the installation and/or use of a particular metro style app. When opening the Group Policy editor under Computer Configuration / Windows Settings / Security Settings / Application Control Settings / Applocker there is a new node called Packaged app Rules.

   [
![image](images/image_thumb1.png)
](images/image1.png)

  To create a new rule, right click on the Packaged app Rules and select Create New Rule…

  ![image](images/image_thumb2.png)

  Select “**Deny**” and then Next.

  ![image](images/image_thumb3.png)

  Select “**Use an installed packaged app as a reference**”. Note to prevent the installation of an app, you can select the packaged app installer as a reference too.

  ![image](images/image_thumb4.png)

  Select the application, then confirm with **OK**.

  ![image](images/image_thumb5.png)

  Then click “**Create**” to create the new Rule.

  ![image](images/image_thumb6.png)

  When a user attempts to launch this metro style application, the following message appears.



  ![image](images/image_thumb7.png)

  **Additional Resources:**

  [Packaged apps and Packaged app installer rules in AppLocker](http://technet.microsoft.com/en-us/library/hh831350.aspx)


