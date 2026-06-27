---
title: "GPO Preferences require XMLLite"
layout: "post"
date: 2008-12-02T20:28:26Z
slug: "gpo-preferences-require-xmllite"
aliases:
  - "/2008/12/gpo-preferences-require-xmllite/"
description: "Reading the [Group Policy Preferences Overview](http://www.gpoguy.com/Portals/0/Group%20Policy%20Preferences%20Overview.pdf) Whitepaper from SDM softw..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Group Policy'
  - 'Tips-Tools'
---
Reading the [Group Policy Preferences Overview](http://www.gpoguy.com/Portals/0/Group%20Policy%20Preferences%20Overview.pdf) Whitepaper from SDM software, I just notice an interesting prerequisite for using GPO Preferences - [XMLLite](http://msdn.microsoft.com/en-us/library/ms752838.aspx).

XmlLite Runtime Files

The XmlLite runtime file, Xmllite.dll, is integrated into the following operating systems and products:


- Windows Server 2008

- Windows Vista

- Windows Server 2003 with Service Pack 2 or later.

- Microsoft Internet Explorer 7.0 and later.

The XmlLite runtime is also available as a download from the [XmlLite Update Page](http://support.microsoft.com/kb/915865) for the following operating systems:


- Windows Server 2003 (32-bit with Service Pack 1 or x64 Editions)

- Windows XP (32-bit with Service Pack 2 or x64 Editions)

So if you want to use GPO Preferences on a Windows XP SP2 client with Internet Explorer 6, you will need to install the [XMLLite runtime package for XP](http://www.microsoft.com/downloads/details.aspx?FamilyID=d7b5dc81-ad14-4de2-8ad5-8c4a9aab5992&displaylang=en&Hash=SCUXiGdaD3dKHqq0lu3YscnCAxwGIpyjAs29clXzqJ6gDj5%2f9EZ1NRpcK3%2fHd%2b5eokECskVy%2bbs99x2LgFxDJw%3d%3d).


