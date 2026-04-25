---
title: "End of Support for Windows XP SP2 &ndash; Deploy XP SP3"
layout: "post"
date: 04/13/2010 19:27:24
slug: "end-of-support-for-windows-xp-sp2"
aliases:
  - "/2010/04/end-of-support-for-windows-xp-sp2/"
description: "On July 12, 2010 Microsoft Windows XP Service Pack will reach end of support, for most companies this shouldn’t come as a surprise as this has been wi..."
author: "Alex Verboon"
tags:
  - compatibility
  - deployment
  - product-lifecycle
  - product-support
  - service-pack-2
  - windows-xp-service-pack-3
categories:
  - compatibility
  - deployment
  - product-lifecycle
  - tip
  - windows-xp
---
On July 12, 2010 Microsoft Windows XP Service Pack will reach end of support, for most companies this shouldn’t come as a surprise as this has been widely [communicated](http://blogs.technet.com/lifecycle/archive/2008/04/25/what-s-happening-to-windows-xp-on-june-30th.aspx) when Microsoft released Windows XP Service Pack 3. however it appears that some companies didn’t took these message too serious then, but now suddenly realize that July 12, 2010 is just a few months ahead of them. 

  Many people have still in memory the challenges they faced with Windows XP Service Pack 2, this because this in fact was more than what people knew as being a Service Pack. Windows XP Service Pack 2 was not just a rollup of security and product fixes, but also contained various technology updates (Network protection, Memory Protection, Web Browsing security and Computer Maintenance). In these days the famous word was *Trustworthy Computing* and this was what Windows XP Service Pack 2 was about. From a technical and security perspective Windows XP Service Pack 2 was definitely a big step forward, but many companies faced quite some challenges in deploying it especially with regard to [application compatibility](http://www.microsoft.com/downloads/details.aspx?FamilyId=9300BECF-2DEE-4772-ADD9-AD0EAF89C4A7&displaylang=en). 

  So now when it comes to the deployment of Windows XP Service Pack 3, many people automatically think of Service Pack 2. But as mentioned previously, Service Pack 2 was a kind of special Service Pack, this isn’t the case for Service Pack 3 which is basically a [rollup of security and product fixes](http://support.microsoft.com/kb/946480/) and contains just a few [new technologies or enhancements](http://www.microsoft.com/downloads/details.aspx?FamilyID=68c48dad-bc34-40be-8d85-6bb4f56f5110&displaylang=en#filelist) that won’t have a big impact on the existing environment. 

  Here’s a short checklist for planning and deploying Windows XP Service Pack 3

  1. Include Windows XP Service Pack 3 in your Software Distribution or Patch Deployment System

  2. Identify Test users (Application owners, Developers, standard users) and deploy Windows XP SP3

  3. Monitor the Pilot clients and track any issues

  4. If all is green, start deploying Windows XP Service Pack 3 throughout the Enterprise

  5. In parallel you want to update your current Windows XP Service Pack 2 based images with Service Pack 3 as well, this to prevent very long new PC installation times. 

  **Things to consider**

  Microsoft did not release separate Multilanguage Packs for XP SP3, companies can continue to use the previous released MUI Pack, but there is a [MUI Pack update](http://www.microsoft.com/downloads/details.aspx?FamilyID=d3f8f6ab-84f1-4095-8709-df509b1bee22&DisplayLang=en) available that provides MUI support for some of the new or updated components that come with SP3. 

  If you were using a single image for standard desktop/laptops **and TabletPC’s** then be aware of the fact that with Windows XP Service Pack 3 Microsoft has removed the possibility of using a Single Image for Windows XP Professional and TabletPC Edition.  So if a company uses TabletPC devices, they will end up creating separate images for these. 

  **Additional Information     
**[Lifecycle Supported Service Packs](http://support.microsoft.com/gp/lifesupsps)    
[Microsoft Support Lifecycle Blog](http://blogs.technet.com/lifecycle/)    
[End of Support for Windows XP SP2 and Windows Vista (with no service packs installed)](http://blogs.technet.com/lifecycle/archive/2010/02/24/end-of-support-for-windows-xp-sp2-and-windows-vista-with-no-service-packs-installed.aspx)    
[What’s up with Service Pack support?](http://blogs.technet.com/lifecycle/archive/2008/03/21/what-s-up-with-service-pack-support.aspx)    
[Windows XP Service Pack 3 Overview](http://www.microsoft.com/downloads/details.aspx?FamilyID=68c48dad-bc34-40be-8d85-6bb4f56f5110&displaylang=en)    
[Release Notes for Windows XP Service Pack 3](http://www.microsoft.com/downloads/details.aspx?FamilyId=60807C3A-8969-4DDF-BEB2-8BFAC9ED416B&displaylang=en)

