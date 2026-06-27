---
title: "Microsoft Silverlight 3 Silent Installation"
layout: "post"
date: 2009-09-04T13:17:43Z
slug: "microsoft-silverlight-3-silent-installation"
aliases:
  - "/2009/09/microsoft-silverlight-3-silent-installation/"
description: "This morning I integrated Microsoft Silverlight 3 into our Windows 7 build. Since we use an automated image build process, i prepared the Silverlight ..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Silverlight'
  - 'Silent-Installs'
---
This morning I integrated Microsoft Silverlight 3 into our Windows 7 build. Since we use an automated image build process, i prepared the Silverlight package for a silent install.

Here’s what you need to do to run a silent Silverlight 3 installation:

1. Download the latest Silverlight installation package from the [Silverlight website](http://silverlight.net/).

2. You will get a silverlight.exe. Run silverlight.exe /x to extract the content

3. Now extract the silverlight.msp from the silverlight.7z file (you can use the free [7-Zip](http://www.7-zip.org/) tool to do that).

4.  Then create a batch script that has the following command:
msiexec /i silverlight.msi /update silverlight.msp /qn

**Update April 2010
**This works as well.

Silverlight.exe /q /ignorewarnings /noupdate


