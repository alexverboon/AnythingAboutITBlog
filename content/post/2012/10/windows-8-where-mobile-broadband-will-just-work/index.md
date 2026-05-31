---
title: "Windows 8 - Where Mobile Broadband will just work"
layout: "post"
date: 2012-10-23T21:41:04Z
slug: "windows-8-where-mobile-broadband-will-just-work"
aliases:
  - "/2012/10/windows-8-where-mobile-broadband-will-just-work/"
description: "Windows 8 comes with a number of enhancement for mobile broadband functionality. If you're interested in the details I recommend you read the content ..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Broadband'
  - 'Mobile'
---
Windows 8 comes with a number of enhancement for mobile broadband functionality. If you're interested in the details I recommend you read the content I have referenced at the end of this blog post. But in short if your mobile broadband device meets the Mobile Broadband Interface (MBIM( specification then Windows 8 will load the inbox class driver (MBCD) so there is no need to install 3rd party drivers. If then the operator in a given country has submitted their connection information to Microsoft you can just establish a connection to the internet without the need of installing additional software or entering connection details. 

  The default installation of Windows 8 includes the APN Database (mobile broadband connectivity directory) which is basically just an XML file stored under C:\Windows\System32\apndatabase.xml that holds all the connection information for the various operators that have submitted their connection details (According to the documentation, this database is automatically updated via Windows Update). 

  The current APN Database dated 12.09.2012 contains connection details for 135 countries world wide and there are about 230 different operators (providers) that have submitted their connection data for inclusion. 

  The below table shows my top 10 country list and the providers that are included within the APN database. (I selected the countries based on the top 10 countries where my blog readers come from). 

                       **Country**

                        **Provider**

                                  **United States**

                        AT&T 

                                  ** **

                        Cincinnati Bell Wireless 

                                  ** **

                        Plateau Wireless 

                                  ** **

                        Rural Cellular Corporation 

                                  ** **

                        SunCom 

                                  ** **

                        T-Mobile USA 

                                  ** **

                        T-Mobile USA: ASpider 

                                  ** **

                        T-Mobile USA: IDT 

                                  ** **

                        T-Mobile USA: Roam Mobility 

                                  ** **

                        T-Mobile USA: Simple Mobile 

                                  ** **

                        T-Mobile USA: Solavei 

                                  ** **

                        T-Mobile USA: Tracfone 

                                  ** **

                        T-Mobile USA: Walmart 

                                  ** **

                        T-Mobile USA: Wyless 

                                  ** **

                        Verizon 

                                  **United Kingdom**

                        3 

                                  ** **

                        Cable & Wireless Guernsey Ltd 

                                  ** **

                        O2 

                                  ** **

                        Orange 

                                  ** **

                        T-Mobile 

                                  ** **

                        Vodafone UK 

                                  **Germany**

                        E-Plus 

                                  ** **

                        O2 

                                  ** **

                        T-Mobile 

                                  ** **

                        Vodafone.de 

                                  **Canada**

                        Bell 

                                  ** **

                        Rogers 

                                  ** **

                        Telus 

                                  **France**

                        Bouygues 

                                  ** **

                        Free Mobile 

                                  ** **

                        Orange 

                                  ** **

                        Orange Caraïbe 

                                  ** **

                        Orange La Réunion 

                                  ** **

                        SFR 

                                  **India**

                        Aircel 

                                  ** **

                        Airtel 

                                  ** **

                        Bharat Sanchar Nigam Limited 

                                  ** **

                        Idea 

                                  ** **

                        MTNL 

                                  ** **

                        Reliance Communication 

                                  ** **

                        Tata Docomo 

                                  ** **

                        Vodafone India 

                                  **Netherlands**

                        KPN/Hi 

                                  ** **

                        Tele2 

                                  ** **

                        Telfort 

                                  ** **

                        T-Mobile 

                                  ** **

                        Vodafone NL 

                                  **Australia**

                        Hutchison - 3 

                                  ** **

                        Optus 

                                  ** **

                        Telstra 

                                  ** **

                        Vodafone Australia 

                                  **Russian Federation**

                        Chelyabinsk Cellular Communications LLC 

                                  ** **

                        DonTeleCom 

                                  ** **

                        Ermak RMS 

                                  ** **

                        MegaFon 

                                  ** **

                        MTS 

                                  ** **

                        NCC 

                                  ** **

                        OJSC Sibirtelecom 

                                  ** **

                        OJSC VimpelCom 

                                  ** **

                        PrimTel 

                                  ** **

                        Uraltel 

                                  ** **

                        Yeniseytelecom 

                                  **Italy**

                        3 

                                  ** **

                        TIM 

                                  ** **

                        vodafone IT 

                                  ** **

                        Wind 

                                  **Sweden**

                        3 

                                  ** **

                        Halebop 

                                  ** **

                        TDC Sweden 

                                  ** **

                        Telenor 

                                  ** **

                        Telia 

                                  **Switzerland**

                        Orange 

                                  ** **

                        Sunrise 

                                  ** **

                        Swisscom 

                                  ** **

                        Tele2 

                 If you want to know what provider is included in your country just open the apndatabase.xml with an XML reader, notepad or import the XML into Excel and then search for the country name. 

  ****

  **Additional Information**

  [Overview of Mobile Broadband in Windows 8](http://msdn.microsoft.com/en-us/library/windows/hardware/hh770525.aspx)    
[Engineering Windows 8 for mobile networks](http://blogs.msdn.com/b/b8/archive/2012/01/20/engineering-windows-8-for-mobility.aspx)    
[Understanding mobile broadband and connection management in Windows 8](http://channel9.msdn.com/events/BUILD/BUILD2011/HW-331T)    
[Connecting Windows 8 to mobile broadband and Wi-Fi networks](http://channel9.msdn.com/events/BUILD/BUILD2011/HW-732T)    
[MBIM-Based Mobile Broadband Requirements for Windows](http://msdn.microsoft.com/en-us/library/windows/hardware/hh918600.aspx)

