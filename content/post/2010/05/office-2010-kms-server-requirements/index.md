---
title: Office 2010 KMS Server Requirements
layout: post
date: '2010-05-12T21:54:12Z'
slug: office-2010-kms-server-requirements
aliases:
- /2010/05/office-2010-kms-server-requirements/
description: Although I have been working with Office 2010 for a while, I wasn’t aware
  of the KMS Server specific requirements until today when we were asked to lo...
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'Office'
  - 'Kms'
---
Although I have been working with Office 2010 for a while, I wasn’t aware of the KMS Server specific requirements until today when we were asked to load the Office 2010 KMS key into one of our customers KMS servers.

  *A dedicated server is not needed to run KMS for Office 2010. A KMS host is a lightweight service, and you can co-host an Office 2010 and Windows KMS host. However, only **Windows Server 2003**, volume editions of **Windows 7**, and **Windows Server 2008 R2** are supported as Office 2010 KMS hosts*

  …..hmmm, must be a typo, they probably forgot to list Windows Server 2008……but no, this isn’t a typo it’s real, Windows Server 2008 is not a supported platform to host the KMS Server for Office 2010 activations and yes Windows Server 2003 is supported. Did they just forgot that in between Server 2003 and Server 2008 R2 they had shipped Server 2008? No they didn’t, see the comment below posted on the Office 2010 activation forum by Ted Way who works on the Office Team.

  *In short, WS 2008 and WS 2008 R2 have different code bases.  It would take a substantial amount of work and require a service pack, not a patch.  A few common questions:*

  *- Why is WS 2003 supported but not WS 2008?  WS 2003 did not have the KMS service, so it was easier to add the KMS service.*

  *- Why can WS 2008 R2 and W7 be activated just by patching WS 2008?  All this patch contains are license files that recognize the new KMS host key to activate WS 2008 R2 and W7.  No change to the KMS service was required.  The KMS service that shipped in WS 2008 does not meet the requirements that Office has.*

  *- What are the alternatives?  Use a WS 2003, WS 2008 R2, or W7 box as your Office KMS host.  They can also be on DNS, and Office will try all the KMS hosts it finds on DNS until one succeeds.  If you must use WS 2008, then you can run a WS 2003, WS 2008 R2, or W7 VM on the WS 2008 machine.*

  *You're frustrated, and rightly so.  I'm on the Office team, and believe me, if there was an easy way to get WS 2008 to work as an Office KMS host, I would be jumping on it.  It does not make sense for us from a business perspective to have any hindrance in Office deployment, so we would not arbitrarily impose this burden on you, however arbitrary it seems.*

  *Office and Windows did work very closely together during the O14 cycle, and that's why W7 and WS 2008 R2 support Office.  However, WS 2008 had already shipped, which meant any changes would have to be done post-RTM.*

  *Obviously this is not the answer you want to hear, and my goal is not to make you happy in this response, but I hope you at least have a better understanding of why things are the way they are.*

  **More about Office 2010 Volume Activation:**

  [Office 2010 Volume Activation](http://blogs.technet.com/office2010/archive/2009/08/24/volume-activation.aspx)
[Volume Activation for Office 2010](http://technet.microsoft.com/en-us/office/ee691939.aspx)
[Frequently asked questions: Volume activation of Office 2010](http://technet.microsoft.com/en-us/library/ff678211(office.14).aspx)
[Volume activation quick start guide for Office 2010](http://technet.microsoft.com/en-us/library/ee624359(office.14).aspx)


