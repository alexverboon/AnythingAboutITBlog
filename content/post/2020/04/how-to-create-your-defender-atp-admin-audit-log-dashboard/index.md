---
title: "How to create your Defender ATP Admin Audit Log Dashboard"
layout: "post"
date: 2020-04-11T20:11:07Z
slug: "how-to-create-your-defender-atp-admin-audit-log-dashboard"
aliases:
  - "/2020/04/how-to-create-your-defender-atp-admin-audit-log-dashboard/"
description: "Walk you through the process of creating an admin audit log dashboard for Defender Advanced Threat Protection."
author: "Alex Verboon"
image: "img/post-heroes/how-to-create-your-defender-atp-admin-audit-log-dashboard.png"
tags:
  - api
  - audit
  - azure-logic-app
  - defender-atp
  - log-analytics
categories:
  - azure-logic-app
  - defender-atp
  - log-analytics
---
Hello everyone,

In today's blogpost I will walk you through the process of creating an admin audit log dashboard for Defender Advanced Threat Protection. During my past customer engagements, I was often asked if there is a way to show device actions taken by Defender ATP admins. The answer is yes, this is possible. First the information is available through the Defender ATP API, second the information is also stored within the Windows event log of the device itself.

# Defender ATP API

Microsoft Defender ATP exposes much of its data and actions through a set of programmatic APIs. Through this API we can also retrieve a list of [**Machineactions**](#). Within the Microsoft Defender Security Center we can access the API through the API explorer.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate1.png)
# Windows Device Event log

On a Defender ATP managed device, we can also find machine action logs within the **Microsoft-Windows-SENSE** event log.
**Event ID****Description**59Starting command:60Failed to run command:71Succeeded to run command:
I have written about this in an earlier blog post, [Microsoft Defender Advanced Threat Protection – Respond Actions Events](#).

# API, Event logs? Management wants a dashboard!

While accessing an API or event log data should be an easy task for the average engineer, you probably don't want to run that task every time when someone needs that information, and with someone I refer to your colleagues in the organization that aren't familiar with accessing an API. What we need is a dashboard that is easily accessible and provides us with the information we want instantly.

# The MDATP Admin Audit Log Dashboard

Use the following step-by-step instructions to create your MDATP Admin Audit Log dashboard.

## Prerequisites

To create the MDATP Admin Audit Log we use the following:

- Microsoft Defender ATP API
- Azure Logic App
- Azure Log Analytics

## Preparing the Azure Log Analytics Workspace

We are going to store our Defender ATP machine action logs into an Azure Log Analytics workspace, so let's create one.
**#****Description****1**Logon to the **Azure Portal** and go to **Log Analytics workspaces**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate2.png)**2**Select **Add **for creating a new Log Analytics workspace

- Select the Subscription, then create new Resource Group **rg_MDATPAdminAuditLog** (or use an existing one)
- Enter a name for the log analytics workspace, in this example I called it **laMDATPAdminAuditLog**
- Select the region where you want to deploy the resources, in this example **West US**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate3.png)

Click on **Next: Pricing Tier
****3**Select your preferred **Pricing Tier** for Azure Log Analytics

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate4.png)

Unless you want to set tags on your resource, click on **Review + Create
****4**If all goes well, validation should pass and you can continue creating the Azure Log Analytics workspace

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate5.png)

Click on **Create**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate6.png)**5**Wait until the deployment is complete.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate7.png)

Click on **Go to resource****6**Take a note of the following information, we will need this later

- **Subscription ID
**
- **Workspace Name
**
- **Workspace ID
**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate8.png)**7**Select **Advanced Settings**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate9.png)

Note down the following information:

- **Workspace ID
**
- **Primary Key
**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate10.png)
## Preparing the Logic App workflow

We will use an Azure Logic App workflow to retrieve the Machineactions data from Microsoft Defender ATP and store the data into our Azure Log Analytics workspace.
![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate11.png)

**#****Description****1**Logon to the **Azure Portal** and go to **Logic Apps**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate12.png)**2**Select **Add **for creating a new Logic App

- Select the Subscription, then select the Resource Group **rg_MDATPAdminAuditLog** we created previously
- Enter a name for the Logic App, in this example I called it **MDATPAdminAuditLog**
- Select the region where you want to deploy the resources, in this example **West US**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate13.png)

Click **Review + Create
**

Click **Create**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate14.png)**3**Wait until the deployment is complete.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate15.png)

Click on **Go to resource****4**Click on **Edit**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate16.png)**5**Select **Blank Logic App**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate17.png)**6**We want to run this workflow 3 times per day, therefore our **trigger** is a **schedule**.

Search for **Schedule**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate18.png)

Select **Recurrence**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate19.png)

Enter the **interval**: 8, select the **frequency**: Hour

Then select the **Time zone** and enter the **start time**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate20.png)

Now is a good time to save our work before we continue

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate21.png)**7**Select **Next Step**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate22.png)**8**We want data from Microsoft Defender ATP, search for **Defender **, when found select **Microsoft Defender ATP**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate23.png)**9**From the list of **Actions**, select **Actions – Get list of machine actions**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate24.png)**10**We now need to sign into Defender ATP, click on the **Sign in** button

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate25.png)

Select the account to sign-in, or select use another account

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate26.png)**11**We leave the Filter results and parameters empty. Select **Next Step**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate27.png)**12**Search for **Control, **then select **For each**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate28.png)

Select an output, click into the '**Select an output from previous steps'** field

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate29.png)

Select **Machine Actions**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate30.png)

The Machine actions output is added. When you hover over the Machine Actions you should see the following formula:

@body('Actions_-_Get_list_of_machine_actions')?['value']

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate31.png)

Select **Add an Action****13**Search for **Log Analytics data collector**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate32.png)**14**From the list of **Actions**, select **Send Data** (preview)

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate33.png)**15**Remember that when we created the Azure Log Analytics workspace, we noted down some information

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate34.png)

Provide a name for the connection, **MDATPAdminAuditLog**

Enter the **Workspace ID** and **Workspace Key **of the Log Analytics workspace

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate35.png)

Click **Create****16**Click into the JSON Request body field, then select **Current Item**

Enter the name of the Custom log, **MDATPAdminAuditLog**

Note: This is the name of the custom log that will be created in our Log Analytics workspace

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate36.png)**17**Select Add parameter and tick the checkbox for **Time-generated field**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate37.png)

Select **utcNow() **,then click **OK**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate38.png)![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate39.png)**18**Our workflow is now complete, now is a good time to save our work again.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate40.png)**19**Next we are going to run our workflow for the very first time, we manually trigger this by clicking on the Run button.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate41.png)

Keep fingers crossed and wait for the process to complete, if all goes well we have a **green**OK indicator displayed for each action.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate42.png)**20**Our logic app indicates that all actions processed successfully, so let's head over to our Azure Log Analytics workspace and see the results.

Under the Custom Logs node we should see our newly created custom table **MDATPAdminAuditLogs_CL**. Note that _CL is automatically added by Log Analytics when ingesting custom data.

Let's take a look at the schema by running the following query:
MDATPAdminAuditLog_CL

| getschema

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate43.png)**21**Next, let's take a look at the data ingested by running the following query:

MDATPAdminAuditLog_CL

| project computerDnsName_s,type_s,TimeGenerated,creationDateTimeUtc_t

**Note**: If you don't get any data, wait for a couple minutes, as per my experience it can take up to 15 minutes until the data becomes available within Log Analytics

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate44.png)
# Creating the MDATP Admin Audit Log Dashboard

Great now that we have the Defender ATP machine actions data stored in an Azure Log Analytics workspace, we can continue creating our dashboard. But wait, let's first prepare the queries for the data we want to include into the dashboard.

## The Log Analytics Queries

For our very first dashboard I want to get the following data from our Defender ATP admin audit log:

- **List of all Machine Actions** – displays all the information for each machine action
- **A summary count of machine actions** – displays the total number of triggered actions by Action type
- **A summary of action requestors** – displays the total number of actions triggered by an MDATP admin or registered App that has permissions to trigger an action.
- **A summary count by Date** – displays the total number of actions by date

**List all Machine Actions****MDATPAdminAuditLog_CL **

**| where TimeGenerated > ago(360d)
**

**| extend Action = type_s
**

**| extend  DeviceName = computerDnsName_s
**

**| extend ScanType = scope_s
**

**| extend Requestor = strcat(requestor_s, requestor_g)
**

**| extend Status = status_s
**

**| extend ActionComment = requestorComment_s
**

**| extend ActionCreationDateTimeUtc = creationDateTimeUtc_t
**

**| extend ActionID = id_g
**

**| summarize  arg_max(ActionCreationDateTimeUtc, ActionID) by ActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID
**

**| sortby ActionCreationDateTimeUtc desc
**

****

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate45.png)******Machine Actions Summary****MDATPAdminAuditLog_CL **

**| where TimeGenerated > ago(360d)
**

**| extend Action = type_s
**

**| extend  DeviceName = computerDnsName_s
**

**| extend ScanType = scope_s
**

**| extend Requestor = strcat(requestor_s, requestor_g)
**

**| extend Status = status_s
**

**| extend ActionComment = requestorComment_s
**

**| extend ActionCreationDateTimeUtc = creationDateTimeUtc_t
**

**| extend ActionID = id_g
**

**| summarize  arg_max(ActionCreationDateTimeUtc, ActionID) by ActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID
**

**| summarizecount() by Action
**

****

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate46.png)******Machine Actions Requestor Summary****MDATPAdminAuditLog_CL **

**| where TimeGenerated > ago(360d)
**

**| extend Action = type_s
**

**| extend  DeviceName = computerDnsName_s
**

**| extend ScanType = scope_s
**

**| extend Requestor = strcat(requestor_s, requestor_g)
**

**| extend Status = status_s
**

**| extend ActionComment = requestorComment_s
**

**| extend ActionCreationDateTimeUtc = creationDateTimeUtc_t
**

**| extend ActionID = id_g
**

**| summarize  arg_max(ActionCreationDateTimeUtc, ActionID) by ActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID
**

**| summarizecount() by Requestor
**

****

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate47.png)******Machine Actions By Date****MDATPAdminAuditLog_CL**

**| where TimeGenerated > ago(360d)
**

**| extendAction = type_s**

**| extendDeviceName = computerDnsName_s**

**| extendScanType = scope_s**

**| extendRequestor = strcat(requestor_s, requestor_g)
**

**| extendStatus = status_s**

**| extendActionComment = requestorComment_s**

**| extendActionCreationDateTimeUtc = creationDateTimeUtc_t**

**| extendActionCreationDate = format_datetime(ActionCreationDateTimeUtc, 'MM-dd-yyyy')
**

**| extendActionID = id_g**

**| summarizearg_max(ActionCreationDateTimeUtc, ActionID) byActionCreationDate ,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID**

**| summarizecount() bybin( ActionCreationDateTimeUtc,1d)
**

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate48.png)****
## Creating the workbook

Now that we have our queries prepared, let's move on to the final task and create our MDATP Admin Audit log dashboard.
**#****Description****1**Within the MDATPAdminAuditLog Log Analytics workspace, select **Workbook**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate49.png)**2**Select **Default Template**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate50.png)**3**Click on the Save Icon and enter the **Title** for the Workbook, then select Save to **Shared Reports, **then click Save.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate51.png)

Now that we have saved our workbook, we can continue editing it. First, we are going to adjust the Workbook Title and description, select **Edit**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate52.png)

Change the **title** and a **description**, then click on **Done Editing**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate53.png)![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate54.png)**4**Next, we are going to display the total number of actions triggered within the last 360 days.  Copy the following query into the query field and then select **Run Query
**MDATPAdminAuditLog_CL

| where TimeGenerated > ago(360d)

| extendAction = type_s

| extendDeviceName = computerDnsName_s

| extendScanType = scope_s

| extendRequestor = strcat(requestor_s, requestor_g)

| extendStatus = status_s

| extendActionComment = requestorComment_s

| extendActionCreationDateTimeUtc = creationDateTimeUtc_t

| extendActionID = id_g

| summarizearg_max(ActionCreationDateTimeUtc, ActionID) byActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID

| summarizecount() byAction

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate55.png)**5**From the **Visualization** drop down menu select **Tiles**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate56.png)

Our dashboard is slowly taking shape.

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate57.png)

Select **Done Editing****6**Select **Add Query**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate58.png)**7**Cop the following query into the query field and set the **visualization** to **Grid, **then select **Run Query**MDATPAdminAuditLog_CL

| where TimeGenerated > ago(360d)

| extendAction = type_s

| extendDeviceName = computerDnsName_s

| extendScanType = scope_s

| extendRequestor = strcat(requestor_s, requestor_g)

| extendStatus = status_s

| extendActionComment = requestorComment_s

| extendActionCreationDateTimeUtc = creationDateTimeUtc_t

| extendActionID = id_g

| summarizearg_max(ActionCreationDateTimeUtc, ActionID) byActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID

| sortbyActionCreationDateTimeUtcdesc

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate59.png)

Select **Done Editing****8**Let's add a line between this and the next data section, select **Add Text**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate60.png)

Type --- and then click **Done Editing**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate61.png)

--- ? Yes this is the [markup language format](#) that draws a line.**9**Select **Add Query
**

Cop the following query into the query field and set the **visualization** to **Grid, **then select **Run Query**MDATPAdminAuditLog_CL

| where TimeGenerated > ago(360d)

| extendAction = type_s

| extendDeviceName = computerDnsName_s

| extendScanType = scope_s

| extendRequestor = strcat(requestor_s, requestor_g)

| extendStatus = status_s

| extendActionComment = requestorComment_s

| extendActionCreationDateTimeUtc = creationDateTimeUtc_t

| extendActionID = id_g

| summarizearg_max(ActionCreationDateTimeUtc, ActionID) byActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID

| summarizecount() byRequestor

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate62.png)

Select **Done Editing****10**Add a line, as shown in step 8**11**Select **Add Query
**

Cop the following query into the query field and set the **visualization** to **Grid, **then select **Run Query**MDATPAdminAuditLog_CL

| where TimeGenerated > ago(360d)

| extendAction = type_s

| extendDeviceName = computerDnsName_s

| extendScanType = scope_s

| extendRequestor = strcat(requestor_s, requestor_g)

| extendStatus = status_s

| extendActionComment = requestorComment_s

| extendActionCreationDateTimeUtc = creationDateTimeUtc_t

| extendActionID = id_g

| summarizearg_max(ActionCreationDateTimeUtc, ActionID) byActionCreationDateTimeUtc,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID

| summarizecount() byDeviceName

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate63.png)

Select **Done Editing****12**Select **Add Query
**

Cop the following query into the query field and set the **visualization** to **Grid, **then select **Run Query**MDATPAdminAuditLog_CL

| where TimeGenerated > ago(360d)

| extendAction = type_s

| extendDeviceName = computerDnsName_s

| extendScanType = scope_s

| extendRequestor = strcat(requestor_s, requestor_g)

| extendStatus = status_s

| extendActionComment = requestorComment_s

| extendActionCreationDateTimeUtc = creationDateTimeUtc_t

| extendActionCreationDate = format_datetime(ActionCreationDateTimeUtc, 'MM-dd-yyyy')

| extendActionID = id_g

| summarizearg_max(ActionCreationDateTimeUtc, ActionID) byActionCreationDate ,DeviceName, Action, ScanType, Status, Requestor, ActionComment , ActionID

| summarizecount() bybin( ActionCreationDateTimeUtc,1d)

Set the Visualization to **Time Chart**![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate64.png)

Select **Done Editing****13**Select **Done Editing** and Save the workbook by selecting the **Save** icon

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate65.png)
And there we go, we know have our Microsoft Defender ATP Admin Audit log

![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate66.png)![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate67.png)![](https://www.verboon.info/wp-content/uploads/2020/04/041120_2005_Howtocreate68.png)

There is still room for improvements here. For example, right now we retrieve the complete machine actions history and store the results into log analytics, this means that we have many duplicate records, this isn't an issue per se, because with the queries we use, we are removing these duplicates, nevertheless I am thinking of adding an OData filter to the query that limits the # of record to only the past n days. I am also thinking of adding parameters to the workbook that allows you to select a specific device and then get a list of all actions triggered for that device.

But this is it for today, I hope you enjoyed this blog post. As always, comments, feedback or suggestions are welcome.

Alex

