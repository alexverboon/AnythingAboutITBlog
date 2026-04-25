---
title: "IE8 Group Policy Settings and more"
layout: "post"
date: 01/27/2009 22:29:12
slug: "ie8-group-policy-settings-and-more"
aliases:
  - "/2009/01/ie8-group-policy-settings-and-more/"
description: "Yesterday Microsoft released the [Release Candidate](http://blogs.msdn.com/ie/archive/2009/01/26/internet-explorer-8-release-candidate-now-available.a..."
author: "Alex Verboon"
tags:
  - blocker
  - gpo
  - ie8
  - internet-explorer
categories:
  - deployment
  - group-policy
  - knowledge
  - packaging
  - scripting
  - vista
  - windows-xp
---
Yesterday Microsoft released the [Release Candidate](http://blogs.msdn.com/ie/archive/2009/01/26/internet-explorer-8-release-candidate-now-available.aspx) for Internet Explorer 8 that of course contains a lot of new features that I am not going to rewrite here again, as others did so already.

Reading the IE8 product group blog 100 additional group policy settings are being introduced to extend manageability of IE8 through Group Policy Management. The updated Group Policy Reference including the new IE8 settings can be downloaded [here](http://www.microsoft.com/downloads/details.aspx?FamilyID=ab4655f2-0a3c-42eb-974d-24b2790bf592&DisplayLang=en) and updated Group Policy Settings ADM files can be found [here](http://www.microsoft.com/downloads/details.aspx?FamilyID=39a9b0cf-0ade-44c5-976b-58ddde86533c&DisplayLang=en#filelist). Also worth reading is the [IE8 Deployment Guide](http://technet.microsoft.com/en-us/library/cc985339.aspx).

And finally for those that want to prevent IE8 being installed in an uncontrolled way throughout their infrastructure can consider using the [IE8 blocker toolkit](http://www.microsoft.com/downloads/details.aspx?FamilyID=21687628-5806-4ba6-9e4e-8e224ec6dd8c&displaylang=en). The IE8 blocker toolkit provides 2 methods to prevent IE8 being automatically installed on your client devices. Method 1 consists of a batch file and Method 2 is a group policy adm template  that allows you to configure IE8 installation blocking through GPO.

.

