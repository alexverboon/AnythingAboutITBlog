---
title: "How to setup KMS on Server 2012 for activating Office 2013 Preview"
layout: "post"
date: 2012-07-24T21:17:59Z
slug: "how-to-setup-kms-on-server-2012-for-activating-office-2013-preview"
aliases:
  - "/2012/07/how-to-setup-kms-on-server-2012-for-activating-office-2013-preview/"
description: "Hey there, it’s been a while since I wrote the last blog post, but that is because I spend 2 excellent weeks at an Italian beach with my family and en..."
author: "Alex Verboon"
tags:
  - activation
  - deployment
  - kms
  - volume-activation-services
  - Windows
  - Office
categories:
  - kms
  - licensing
  - Windows
  - Office
---
Hey there, it’s been a while since I wrote the last blog post, but that is because I spend 2 excellent weeks at an Italian beach with my family and enjoyed “[dolce far niente](http://en.wiktionary.org/wiki/dolce_far_niente)”. Now and then I did read some tweets so of course got notice of the Office 2013 Preview Microsoft released earlier last week. So now that I’m back I have started reading through the various documentations and so I came across the Microsoft [Office 2013 Preview Volume License Pack](http://www.microsoft.com/en-us/download/details.aspx?id=30342) that Microsoft released to activate Office 2013 Preview using KMS or Active Directory based activation.

  What is cool about this is that even if you’re not interested in activating Office 2013, with the information provided, you can go through the entire process of setting up KMS or Active Directory based volume activation on Server 2012 because Microsoft has provided test VLK keys.

  Below you’ll find a step by step description of how I have setup KMS for Office 2013 Preview in my test lab. Before starting with setting up the Volume Activation Role, I downloaded the 64 Bit version of the Office 2013 Preview Volume license Pack from [here](http://www.microsoft.com/en-us/download/details.aspx?id=30342).

  I then enabled the Volume Activation Services Role as shown in the following screenshots.

  ![1clip_image002_thumb](https://www.verboon.info/wp-content/uploads/2012/10/1clip_image002_thumb.jpg)

  ![2clip_image004_thumb](https://www.verboon.info/wp-content/uploads/2012/10/2clip_image004_thumb.jpg)

  ![3clip_image006_thumb](https://www.verboon.info/wp-content/uploads/2012/10/3clip_image006_thumb.jpg)

  ![4clip_image008_thumb1](https://www.verboon.info/wp-content/uploads/2012/10/4clip_image008_thumb1.jpg)

  ![5clip_image010_thumb1](https://www.verboon.info/wp-content/uploads/2012/10/5clip_image010_thumb1.jpg)

  ![6clip_image010_thumb1](https://www.verboon.info/wp-content/uploads/2012/10/6clip_image010_thumb1.jpg)

  ![7clip_image012_thumb](https://www.verboon.info/wp-content/uploads/2012/10/7clip_image012_thumb.jpg)

  ![8clip_image014_thumb](https://www.verboon.info/wp-content/uploads/2012/10/8clip_image014_thumb.jpg)

  Once the Volume Activation Role is enabled, launch the Microsoft Office 2013 Preview Volume License Pack installation.

  ![9clip_image016_thumb](https://www.verboon.info/wp-content/uploads/2012/10/9clip_image016_thumb.jpg)

  When completed the Volume Activation Tools are launched, or in case you closed it launch it manually.

  ![10clip_image018_thumb](https://www.verboon.info/wp-content/uploads/2012/10/10clip_image018_thumb.png)

  ![11clip_image020_thumb](https://www.verboon.info/wp-content/uploads/2012/10/11clip_image020_thumb.jpg)

  Here you can decide whether you want to use KMS or Active Directory based activation. Note that Active Directory based activation will only work for Windows 8 and Server 2012 systems. Because we are most likely going to have both Windows 7 / Office 2010 in our environment I choose KMS.

  ![12clip_image022_thumb](https://www.verboon.info/wp-content/uploads/2012/10/12clip_image022_thumb.jpg)

  Next I’ve entered the Test VLK key Microsoft provides [here](http://www.microsoft.com/en-us/download/details.aspx?id=30342)

  ![13clip_image024_thumb](https://www.verboon.info/wp-content/uploads/2012/10/13clip_image024_thumb.jpg)

  ![14clip_image026_thumb](https://www.verboon.info/wp-content/uploads/2012/10/14clip_image026_thumb.jpg)

  ![15clip_image028_thumb](https://www.verboon.info/wp-content/uploads/2012/10/15clip_image028_thumb.jpg)

  ![16clip_image030_thumb](https://www.verboon.info/wp-content/uploads/2012/10/16clip_image030_thumb.jpg)

  ![17clip_image032_thumb](https://www.verboon.info/wp-content/uploads/2012/10/17clip_image032_thumb.jpg)

  ![18clip_image034_thumb](https://www.verboon.info/wp-content/uploads/2012/10/18clip_image034_thumb.jpg)

  I then enabled the Firewall options and decided to publish the KMS server into my DNS. I strongly recommend that you do NOT select this option if you are setting up your test KMS server in a production environment where you have other production KMS servers running.

  ![19clip_image036_thumb](https://www.verboon.info/wp-content/uploads/2012/10/19clip_image036_thumb.jpg)

  ![20clip_image038_thumb](https://www.verboon.info/wp-content/uploads/2012/10/20clip_image038_thumb.jpg)

  ![21clip_image040_thumb](https://www.verboon.info/wp-content/uploads/2012/10/21clip_image040_thumb.jpg)

  Then a little check if our Windows 8 client sees the KMS server and we’re “almost” done.

  ![22clip_image042_thumb](https://www.verboon.info/wp-content/uploads/2012/10/22clip_image042_thumb.jpg)

  Finally I launched Office 2013 Preview and…..ups, not activated, well that’s because like with Office 2010, KMS requires at least 5 clients before activation takes place.

  ![23clip_image044_thumb](https://www.verboon.info/wp-content/uploads/2012/10/23clip_image044_thumb.jpg)

  As with the previous version of Office, Office 2013 also has the ospp.vbs script included providing various command line options around product activation.

  ![25clip_image048_thumb](https://www.verboon.info/wp-content/uploads/2012/10/25clip_image048_thumb.jpg)

