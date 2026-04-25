---
title: "Finding Group Policy Settings through Windows 7 Search Connector"
layout: "post"
date: 09/02/2010 20:44:18
slug: "finding-group-policy-settings-through-windows-7-search-connector"
aliases:
  - "/2010/09/finding-group-policy-settings-through-windows-7-search-connector/"
description: "Since the release of Windows 7 and Server 2008-R2 we have about 3000 Group Policy Settings available to centrally configure and manage Windows clients..."
author: "Alex Verboon"
image: "img/post-heroes/finding-group-policy-settings-through-windows-7-search-connector.png"
tags:
  - gpo
  - group-policy
  - group-policy-preferences
  - search
  - search-provider
categories:
  - gpo
  - group-policy
  - search-provider
  - tip
---
Since the release of Windows 7 and Server 2008-R2 we have about 3000 Group Policy Settings available to centrally configure and manage Windows clients and servers. Though some among us might have worked with GPO settings from the early days on, knowing about the existence of each and every available setting is nearly impossible. It still happens to me that while I am configuring a specific GPO setting, I do come across other GPOs I didn’t knew of yet. 

  [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2010/09/image2.png)

  Have we not all been in a situation once, where we wondered whether a certain system configuration item could be managed via a GPO setting? So what would you do? Open the Group Policy Management Console and browse through the settings until you find the setting you’ve been looking for? Yes, that is possible approach and sometimes the quickest if you know in which area the setting is most likely stored. Another approach is to download the [Group Policy Settings Reference for Windows and Windows Server](http://www.microsoft.com/downloads/details.aspx?FamilyID=18c90c80-8b0a-4906-a4f5-ff24cc2030fb&displaylang=en) spreadsheet and search through the Excel sheet. 

  Now here’s another nice solution that allows you to search for Group Policy settings without opening the GPMC or an Excel sheet. All you need is Windows 7 and Internet Access. 

  Open Internet Explorer and go to [http://gps.cloudapp.net/](http://gps.cloudapp.net/) (Group Policy Search) 

  In the Settings Menu select “**Add Search Connector**”.

  [
![2010-09-02 22h08_04](images/2010090222h08_04_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/09/2010090222h08_04.png) 

  Download the Search Connector configuration file.

  [
![2010-09-02 22h09_34](images/2010090222h09_34_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/09/2010090222h09_34.png)

  Select “**Add**” to install the Search Connector.  

  [
![2010-09-02 22h17_15](images/2010090222h17_15_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/09/2010090222h17_15.png) 

  Select Group Policy Search and type a word within the search bar. 

  [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2010/09/image1.png) 

  Happy GPO Setting searching!

