---
title: "Backup Office 365 sign-in data with Azure Log Analytics and Logic App"
layout: "post"
date: 2018-03-16T19:59:59Z
slug: "backup-office-365-sign-in-data-with-azure-log-analytics-and-logic-app"
aliases:
  - "/2018/03/backup-office-365-sign-in-data-with-azure-log-analytics-and-logic-app/"
description: "The Office 365 solution in Operations Management Suite (OMS) allows you to monitor your Office 365 environment in Log Analytics. Like with any solutio..."
author: "Alex Verboon"
image: "img/post-heroes/backup-office-365-sign-in-data-with-azure-log-analytics-and-logic-app.png"
tags:
  - archive
  - azure-log-analytics
  - azure-logic-app
  - backup
  - office-365-2
  - sign-in-data
  - Office
categories:
  - azure
  - azure-logic-app
  - log-analytics
  - Office
---
The Office 365 solution in Operations Management Suite (OMS) allows you to monitor your Office 365 environment in Log Analytics. Like with any solution that you setup in OMS you have to think of the data retention time.

At present the maximum retention time can be set to two years, but this of course will affect your Azure billing. In today's blog post I walk you through a possible solution how to backup just a subset of data into a custom log. The idea is that you can keep the retention period for the large amount of data low and only keep the data that is important for you for a longer period. The solution uses [Azure Log Analytics](https://docs.microsoft.com/en-us/azure/log-analytics/) and [Azure Logic App Services](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-overview).

The Logic App will do the following:

 	
- Start the workflow every day at 00:10 AM
 	
- Run a query in log analytics using the office 365 log data , collect Username, IP Address and Event time from the previous day.
 	
- Parses the query result into JSON
 	
- Sends the data to a custom log in Log Analytics.

![](images/031618_1957_BackupOffic1.png)

First setup an OMS Workspace and then add and configure the Office 365 solution. Detailed instructions can be found here: [https://docs.microsoft.com/en-us/azure/operations-management-suite/oms-solution-office-365](https://docs.microsoft.com/en-us/azure/operations-management-suite/oms-solution-office-365)

![](images/031618_1957_BackupOffic2.png)

Note that it can take up to a day until you will see data coming in.

Next create an Azure Logic App and wait for the deployment to complete.

![](images/031618_1957_BackupOffic3.png)

Select "**Logic App Designer**" and select "**Blank Logic App**"

![](images/031618_1957_BackupOffic4.png)

The first step of the workflow is the Schedule.

![](images/031618_1957_BackupOffic5.png)

I have defined the Schedule as shown below.

![](images/031618_1957_BackupOffic6.png)

Then add the next step and select "**Add an action**"

![](images/031618_1957_BackupOffic7.png)

We will now define the send step of the workflow which consists of running a query in log analytics.

![](images/031618_1957_BackupOffic8.png)

![](images/031618_1957_BackupOffic9.png)

Sign-in to log analytics to create a connection.

![](images/031618_1957_BackupOffic10.png)

Once connected, select the Subscription, Resource Group and workspace name and finally enter the query.

![](images/031618_1957_BackupOffic11.png)

Now press **Save** and then **Run** the workflow. If all goes well, you get the following result.

![](images/031618_1957_BackupOffic12.png)

Expand the Run Query and list results and then select "**Show raw outputs**"

![](images/031618_1957_BackupOffic13.png)

Mark all the "Body" content of the raw content and copy it into a notepad file, we'll use it later.

![](images/031618_1957_BackupOffic14.png)

Go back to "**Design**" mode to continue editing the workflow.

Then add the next step and select "**Add an action**"

![](images/031618_1957_BackupOffic15.png)

Add "**Data Operations – Parse JSON**"

![](images/031618_1957_BackupOffic16.png)

Within the "Content" field add "**value**", which is the output from the run query step.

![](images/031618_1957_BackupOffic17.png)

Next select "**use sample payload to generate schema**" and now copy past the raw output that you have saved previously.

![](images/031618_1957_BackupOffic18.png)

![](images/031618_1957_BackupOffic19.png)

**Save** the logic App again and **Run** it. If all went well you'll get the following result.

![](images/031618_1957_BackupOffic20.png)

Go back into edit mode and add the final step of the workflow.

![](images/031618_1957_BackupOffic21.png)

Select "**Azure log analytics data collector – send data**"

![](images/031618_1957_BackupOffic22.png)

Enter a connection name, the Workspace ID and Workspace key. If you want to use different retention periods for the Office 365 solution and the custom log, use a separate Log Analytics workspace.

![](images/031618_1957_BackupOffic23.png)

Select "**Body**" which is the output from the previous Parse Jason step.

![](images/031618_1957_BackupOffic24.png)

Next enter the Custom Log name and enter "**time**" in the time-generated field.

![](images/031618_1957_BackupOffic25.png)

**Save** the workflow and **Run** it.

![](images/031618_1957_BackupOffic26.png)

Now let's head over to the Azure Log Analytics portal and see if our data is coming in. Be patient, this can take a few minutes.

**Tip**: Consider opening a new browser session "after" you ran the workflow, I've noticed some issues with query tab completion.

And there we go, the data arrived in my custom log "MyCustomLog2_CL".

![](images/031618_1957_BackupOffic27.png)

Hope you enjoyed this blog post, as always feedback is welcome.

Cheers

Alex

