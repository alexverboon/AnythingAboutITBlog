---
title: "Group Policy Settings for Silverlight 4 &ndash; FIXED"
layout: "post"
date: 2011-06-06T13:29:23Z
slug: "group-policy-settings-for-silverlight-4fixed"
aliases:
  - "/2011/06/group-policy-settings-for-silverlight-4fixed/"
description: "On the Microsoft Silverlight website you will find a page that describes the [available Group Policy Settings for Silverlight](http://www.microsoft.co..."
author: "Alex Verboon"
image: "img/post-heroes/group-policy-settings-for-silverlight-4fixed.png"
categories:
  - 'Windows'
tags:
  - 'Group Policy'
  - 'Silverlight'
---
On the Microsoft Silverlight website you will find a page that describes the [available Group Policy Settings for Silverlight](http://www.microsoft.com/getsilverlight/resources/documentation/grouppolicysettings.aspx#isolated-storage) as well as the content for the ADMX and ADML file. But… it doesn’t work because the code on the web contains a bug and a section is missing. 

  Within the silverlight.admx there is an unnecessary space and within the silverlight.amdl the section for SET_ALLOW_MAXIMUM_ISOLATED_STORAGE and ALLOW_MAXIMUM_ISOLATED_STORAGE_HELP is completely missing.  

  [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/06/image.png)

  To get the Silverlight GPO working remove the space from ALLOW_MAXIMUM_ISOLATED_STORAGE_HELP and add the following section to the silverlight.adml file. 

  [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2011/06/image1.png)

  Then copy the files to your central store (\\Lab.net\sysvol\LAB.NET\Policies\PolicyDefinitions) or into your local Policy Definitions folder (C:\Windows\PolicyDefinitions) and open the Group Policy Management Console, you should now find the Silverlight settings under Administrative Templates. 

  [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2011/06/image2.png)

  [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2011/06/image3.png)

