---
title: "Office 2007 Trusted location configuration"
layout: "post"
date: 2009-08-26T17:14:02Z
slug: "office-2007-trusted-location-configuration"
aliases:
  - "/2009/08/office-2007-trusted-location-configuration/"
description: "When opening an Excel file that contains macros, Microsoft Excel 2007 shows a security warning as shown in the picture below and disables the macros. ..."
author: "Alex Verboon"
image: "img/post-heroes/office-2007-trusted-location-configuration.png"
tags:
  - excel-2007
  - macros
  - office-2007
  - security
  - trusted-location
  - Office
categories:
  - excel-2007
  - office-2007
  - tip
---
When opening an Excel file that contains macros, Microsoft Excel 2007 shows a security warning as shown in the picture below and disables the macros. 

  [
![image](images/image-thumb5.png)
](https://www.verboon.info/wp-content/uploads/2009/08/image5.png) 

  To continue using the Excel sheet and its macros, you must first enable then by clicking on the "Options…” button and selecting the “Enable this content” option. This is quite annoying if you must use that same file on a regular basis. You could of course completely disable this security warning on your entire system, but then there is a risk of opening content once that could contain unwanted code. 

  But if you are sure about files that are located at a specific location can be considered as save, you can configure Trusted Locations in Excel 2007. Once that folder is configured as a trusted location, your Excel files will open without disabling the macros. 

  To configure Trusted Locations in Excel 2007, press the **Alt+F** key and then the **Alt+I** key to access the Excel Options, then select “Trust Center”, “Trust Center Settings”, “Trusted Locations”. 

   [
![image](images/image-thumb6.png)
](https://www.verboon.info/wp-content/uploads/2009/08/image6.png) 

   Then select “Add new location”. I used **C:\data\trust** for this example. 

   [
![image](images/image-thumb7.png)
](https://www.verboon.info/wp-content/uploads/2009/08/image7.png)

  Press the “OK” button to confirm your configuration.

