---
title: "SQL Server services user account"
layout: "post"
date: 2008-11-20T22:58:40Z
slug: "sql-server-services-user-account"
aliases:
  - "/2008/11/sql-server-services-user-account/"
description: "When you install SQL Server 2000 / 2005 / 2008 you can configure under what user account the services are running. In the past i've often seen people ..."
author: "Alex Verboon"
tags:
  - security
  - sql
categories:
  - security
  - sql
  - tip
---
When you install SQL Server 2000 / 2005 / 2008 you can configure under what user account the services are running. In the past i've often seen people selecting "local system", I also selected that....not thinking too much about security then and it was the easiest to do with no need to create an additional user account and as long as you don't need to access any other domain resources that worked fine.

Today from a security perspective though running the SQL services under the local sysem account is probably not a good idea, as the local system account is equivalent to a local administrator, so bad code that might get into your SQL server might hit the underlying system as well. From reading various sql forum postings and articles and Microsoft Technet articles it appears to be the best to simply create standard users accounts, during installation these accounts are being given the necessary permissions on the system they need.

If you don't need access to other domain resources, the creation of local user accounts on the system that hosts the SQL server is enough, if not create them in AD.

The article "[Picking Service Accounts](http://www.sqlservercentral.com/articles/Administering/pickingserviceaccounts/2351/)" describes it all in more detail. (note that you must register yourself to read articles on [SQLServerCentral.com](http://www.sqlservercentral.com/)

