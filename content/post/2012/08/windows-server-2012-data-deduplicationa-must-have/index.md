---
title: "Windows Server 2012 Data Deduplication&ndash;A must have"
layout: "post"
date: 2012-08-20T21:15:24Z
slug: "windows-server-2012-data-deduplicationa-must-have"
aliases:
  - "/2012/08/windows-server-2012-data-deduplicationa-must-have/"
description: "During my summer vacation I’ve watched several TechEd video’s and there were plenty of interesting things I have seen, but the Data Deduplication feat..."
author: "Alex Verboon"
tags:
  - data-deduplication
  - file-services
  - space
  - storage
categories:
  - windows-server-2012
---
During my summer vacation I’ve watched several TechEd video’s and there were plenty of interesting things I have seen, but the Data Deduplication feature in Server 2012 definitely belongs to one of my favorite ones. There are plenty of use cases were the Data Deduplication feature can help you save storage space. To try out this feature I created a folder on my test server and created 4 folders. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/10/image4.png)

  The folders Source1 and Source2 contained a copy of the Windows 8 Enterprise ISO file and in folder Source3 and Source4 I copied the install.wim from the Windows 8 Enterprise client installation source. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/10/image13.png)

  After having copied these files, about 12 GB of my 40 GB disk was used. But once I had Data Reduplication enabled the used space went down to just 2.82 GB.

  ![image](https://www.verboon.info/wp-content/uploads/2012/10/image18.png)

  To learn more about the Windows Server 2012 Data Deduplication feature check out the below resources. 

  [Introduction to Data Deduplication in Windows Server 2012](http://blogs.technet.com/b/filecab/archive/2012/05/21/introduction-to-data-deduplication-in-windows-server-2012.aspx)     
[Data Deduplication overview](http://technet.microsoft.com/en-us/library/hh831602)     
[Windows Server 2012 Data Deduplication Video on TechNet](http://technet.microsoft.com/en-us/video/windows-server-2012-data-deduplication.aspx)

