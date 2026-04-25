---
title: "Select-MyAzureRmSubscription"
layout: "post"
date: 2017-02-07T15:08:07Z
slug: "select-myazurermsubscription"
aliases:
  - "/2017/02/select-myazurermsubscription/"
description: "I have multiple Azure subscriptions linked to my account, so anytime I connect to Azure in PowerShell I have to make sure i am working in the right co..."
author: "Alex Verboon"
tags:
  - azure
  - powershell
categories:
  - azure
  - powerpoint-viewer-2010
---
I have multiple Azure subscriptions linked to my account, so anytime I connect to Azure in PowerShell I have to make sure i am working in the right context. To simplify this I wrote a little helper function called Select-MyAzureRmSubscription.

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/Select-MyAzureSubscription_DD91/image.png)

After entering the -SubscriptionName parameter the script enumerates alll the subscriptions I have access to and generates a dynamic parameter option.

```

```

Script location on GitHub: [https://github.com/alexverboon/posh/blob/master/Azure/Utilities/select-MyAzureRmSubscription.ps1](https://github.com/alexverboon/posh/blob/master/Azure/Utilities/select-MyAzureRmSubscription.ps1)

