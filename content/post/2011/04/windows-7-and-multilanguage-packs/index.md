---
title: Windows 7 and Multilanguage Packs
layout: post
date: '2011-04-26T13:34:43Z'
slug: windows-7-and-multilanguage-packs
aliases:
- /2011/04/windows-7-and-multilanguage-packs/
description: Most of you actively dealing with Windows 7 deployments probably know
  about the Multilanguage Packs for Windows 7 , but since I do still get questions...
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'Language-Pack'
  - 'Editions'
---
Most of you actively dealing with Windows 7 deployments probably know about the Multilanguage Packs for Windows 7 , but since I do still get questions about this every now and then, I thought it’s worth to do a brief recap on this subject. 

  For the sake of simplicity I’ve created a Q&A based summary. 

  **Q:  What is the default language of Windows 7     
**A:  The Windows 7 (as Vista) core operating system is language agnostic. In terms of licensing and language support Microsoft has the following definitions: 

  
>    a) Single Language Editions (Windows 7 Starter, Home Basic, Home Premium, Professional)

    b) Multilingual Editions (Windows 7 Enterprise, Windows 7 Ultimate)

 

  A single language edition can only support one language when used by the end-user. The multilingual editions allow installing one or multiple language packs where the user can at any time configure and use their preferred language. 

  So if you buy a Windows 7 Home Premium license in the Netherlands you basically get the Windows 7 Home Premium installation media  with the Dutch language pack pre-installed. You will also notice that when buying a new computer users often are asked to select a language, in this case the hardware vendor has preloaded several language packs, but only one language pack is allowed to remain active after installation. 

  Windows 7 Enterprise installation media by default is provided with the English language pack enabled, additional language pack support can be provided by either pre-installing one or more language packs within the corporate image or deploying them via software distribution mechanisms such as Microsoft SCCM. 

  **Q: What is a language pack?     
**A: A language pack contains all resources (files) needed to provide a localized User Interface for all components included within the Operating system, but not for applications that you install on top of that. Note that some products such as Microsoft Office 2010 requires separate language packs to be installed to localize the application. One good example is Internet Explorer. Windows 7 by default has Internet Explorer 8 included, when installing the operating system Multilanguage pack, IE8 is localized as well, but as soon as you upgrade IE8 to IE9 you will also need to install [IE9 language packs](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=5a1870ba-96ad-4e47-bb9e-1671b6a64495) separately.  

  **Q: What languages are supported?**    
A: For Windows 7 35 language packs are available. The below table lists all supported languages. 

              **Available Multilanguage Packs for Windows 7**                  Arabic        Estonian        Korean        Serbian Latin                  Bulgarian        Finnish        Latvian        Slovak                  Chinese (Simplified)        French        Lithuanian        Slovenian                  Chinese (Traditional)        German        Norwegian (Bokmål)        Spanish                  Croatian        Greek        Polish        Swedish                  Czech        Hebrew        Portuguese (Brazil)        Thai                  Danish        Hungarian        Portuguese (Portugal)        Turkish                  Dutch        Italian        Romanian        Ukrainian                  English        Japanese        Russian                   **Q: What if my language is not listed?     
**A: Beside the Language Packs which provides 100% UI localization coverage  Microsoft also provides so-called LIP packages (partial language packs). More details about the differences between LP and LIPS can be found [here](http://technet.microsoft.com/en-us/library/dd744336(WS.10).aspx#LangPackTypes)

  **Q: I just recently upgraded to Windows 7 “Service Pack 1” anything to consider with regard to Language Packs?     
**A: Yes, you must update your existing Windows 7 RTM Language pack sources with the new ones released for Windows 7 Service Pack 1. 

   

  I might create a follow up article on this one, but for now that’s it, hope it was useful for some of you. If you have more questions , drop a comment and I can extend the Q&A list. 

   

  **Additional Information**

  [Windows 7 Features – Language Packs](http://windows.microsoft.com/en-US/windows7/products/features/language-packs)    
[Understanding Multilingual Deployments](http://technet.microsoft.com/en-us/library/dd744336(WS.10).aspx)    
[Multilanguage Packs Explained – Video](https://www.verboon.info/index.php/2009/02/windows-multilanguage-packs-explained/)    
[Windows Team Blog on LIPs](http://windowsteamblog.com/windows/b/springboard/archive/2010/08/01/windows-7-language-packs.aspx)

