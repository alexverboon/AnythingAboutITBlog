---
title: "Skype Group Policy Settings"
layout: "post"
date: 2011-12-31T10:26:34Z
slug: "skype-group-policy-settings"
aliases:
  - "/2011/12/skype-group-policy-settings/"
description: "Just recently one of our customers requested the Skype ([Business version](http://www.skype.com/intl/en-us/business/download/)) Application to be pack..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Group Policy'
  - 'Settings'
---
Just recently one of our customers requested the Skype ([Business version](http://www.skype.com/intl/en-us/business/download/)) Application to be packaged for software distribution, so I wondered what the status is these days with regard to locking down Skype with Group Policy. Well the results are sobering. Despite the fact that Skype is [part of Microsoft](http://www.microsoft.com/en-us/skype/) since a while, there has not been much progress in making Skype more Group Policy aware.

  The settings that can be configured using Group Policy are documented within the Skype [IT Administrators Guide](http://download.skype.com/share/business/guides/skype-it-administrators-guide.pdf) but note that this document relates to Skype version 4.2 and there isn’t a newer version for Skype version 5.x. Also note that the number of settings is rather limited, in fact the only setting I consider as useful for Enterprise Administrators is to disable the *Check for Updates* setting that prevents Skype form automatically checking for new versions and updates.

  The latest [official version](http://community.skype.com/t5/Skype-Manager/ADM-Policy-Template-for-Version-5-5/m-p/56728#M42) of the Skype ADM template can be downloaded from [here](http://download.skype.com/share/security/Skype-v1.7.adm). If you are looking for ADMX files for Skype check out the links below.

  Sourceforge – CustomADMX project
[http://sourceforge.net/projects/customadmx/](http://sourceforge.net/projects/customadmx/)

  How to Control Skype in a Corporate Setting
[http://www.commodore.ca/windows/skype/skype-business.htm](http://www.commodore.ca/windows/skype/skype-business.htm)

  In case you have a requirement to further lock down Skype I suggest you look at [PolicyPak](http://policypak.com/).


