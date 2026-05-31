---
title: "App-V Management Server Setup and SQL Server Configuration"
layout: "post"
date: 2010-03-14T00:01:02Z
slug: "app-v-management-server-setup-and-sql-server-configuration"
aliases:
  - "/2010/03/app-v-management-server-setup-and-sql-server-configuration/"
description: "During the Installation of the App-V Management Server on a Windows Server 2008 with SQL Server 2008 Express installed I ran into an problem specifyin..."
author: "Alex Verboon"
image: "img/post-heroes/app-v-management-server-setup-and-sql-server-configuration.png"
categories:
  - 'Tips-Tools'
tags:
  - 'App-V'
  - 'Setup'
---
During the Installation of the App-V Management Server on a Windows Server 2008 with SQL Server 2008 Express installed I ran into an problem specifying the database server and got an error as shown in the picture below. [
![image](images/image_thumb7.png)
](https://www.verboon.info/wp-content/uploads/2010/03/image7.png)

*The installation program could not connect to the configuration data store. Please see the installation log file for more information.*

I solved the problem by opening the SQL Server Configuration Manager and enabled TCP/IP in the SQL Server Network Configuration options.

[
![image](images/image_thumb8.png)
](https://www.verboon.info/wp-content/uploads/2010/03/image8.png) Within the Properties specify Port 1433 as shown in the picture below.

[
![image](images/image_thumb9.png)
](https://www.verboon.info/wp-content/uploads/2010/03/image9.png)Finally restart the SQL Server Service. Once the SQL Service has restarted the App-V Management Server installation Wizard should find the SQL Server Instance.

[
![image](images/image_thumb10.png)
](https://www.verboon.info/wp-content/uploads/2010/03/image10.png)

Update: May, 2010, although I managed to get this running with SQL 2008, i recommend using SQL 2005 as that to my knowledge is the official supported SQL Database. Any inputs welcome.

