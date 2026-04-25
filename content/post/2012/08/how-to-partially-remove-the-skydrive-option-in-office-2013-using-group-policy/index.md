---
title: "How to partially remove the SkyDrive option in Office 2013 using Group Policy"
layout: "post"
date: 2012-08-02T19:05:46Z
slug: "how-to-partially-remove-the-skydrive-option-in-office-2013-using-group-policy"
aliases:
  - "/2012/08/how-to-partially-remove-the-skydrive-option-in-office-2013-using-group-policy/"
description: "If you have tried out the Office 2013 Preview you probably noticed the SkyDrive integration within the File Open and Save dialogs in Word, Excel and o..."
author: "Alex Verboon"
tags:
  - gpo
  - group-policy
  - office-2013
  - skydrive
categories:
  - group-policy
  - office-2013
  - skydrive
---
If you have tried out the Office 2013 Preview you probably noticed the SkyDrive integration within the File Open and Save dialogs in Word, Excel and other Office Applications. Personally have started using SkyDrive all the time, but I can imagine that some companies rather do not want to see their users storing sensitive data on SkyDrive. So I wondered if this option could be disabled.

  ![1image_thumb](https://www.verboon.info/wp-content/uploads/2012/10/1image_thumb.png)

   

   

  Well apparently there is a Group Policy setting for this called “Show SkyDrive Sign in” located under User Configuration / Policies / Administrative Templates / Microsoft Office 2013 / Miscellaneous

  ![2image_thumb1](https://www.verboon.info/wp-content/uploads/2012/10/2image_thumb1.png)

  When setting this to Disabled, the result is as following.

  ![3image_thumb2](https://www.verboon.info/wp-content/uploads/2012/10/3image_thumb2.png)

  But…if we select Add a place, we still get the SkyDrive option and I ‘m allowed to sign up and store my document.

  ![4image_thumb3](https://www.verboon.info/wp-content/uploads/2012/10/4image_thumb3.png)

  So it looks like the option can only be partially disabled, at least within the Microsoft Office 2013 Preview version.

