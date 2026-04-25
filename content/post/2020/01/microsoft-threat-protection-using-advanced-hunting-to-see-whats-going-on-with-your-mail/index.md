---
title: Microsoft Threat Protection – Using advanced hunting to see what's going on
  with your mail
layout: post
date: '2020-01-15T22:09:35Z'
slug: microsoft-threat-protection-using-advanced-hunting-to-see-whats-going-on-with-your-mail
aliases:
- /2020/01/microsoft-threat-protection-using-advanced-hunting-to-see-whats-going-on-with-your-mail/
description: Last December Microsoft introduced Microsoft Threat Protection (MTP)
  including advanced hunting that allows us to run queries across multiple data sources.
author: Alex Verboon
image: img/post-heroes/microsoft-threat-protection-using-advanced-hunting-to-see-whats-going-on-with-your-mail.png
tags:
- atp
- hunting
- kusto
- mtp
- safeattachments
- safelinks
- Office
categories:
- mtp
- Office
---
Last December Microsoft introduced Microsoft Threat Protection (MTP) including advanced hunting that allows us to run queries across multiple data sources i.e. Microsoft Defender ATP and Office 365 ATP. If you haven't heard yet about MTP I recommend reading Christian Müller's blog post [Microsoft Threat Protection – unified hunting](#)Now while the primary purpose of the unified hunting capability is to find information about indicators and entities, we can also use it to get an overview of what's going on inside the systems that feed information into MTP i.e. Office 365.  So, I created a few simple queries that summarizes various attributes from the EmailEvents table.
![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh1.png)QuerySample OutputEmailEvents
| summarize count() by FinalEmailActionPolicy

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh2.png)EmailEvents
| summarize count() by DeliveryAction

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh3.png)EmailEvents
| summarize count() by DeliveryLocation

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh4.png)EmailEvents
| summarize count() by EmailDirection

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh5.png)EmailEvents
| summarize count() by FinalEmailAction

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh6.png)EmailEvents
| summarize count() by FinalEmailActionPolicy

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh7.png)EmailEvents
| summarize count() by tostring(MalwareDetectionMethod)

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh8.png)EmailEvents
| summarize count()  by tostring(PhishDetectionMethod)

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh9.png)EmailEvents
| summarize count() by MalwareFilterVerdict

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh10.png)EmailEvents
| summarize count() by PhishFilterVerdict

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh11.png)Now that we know about the possible values the system returns (note that there might be more values), we can start drilling into the details.  Let's assume I want to know more about the e-mails where ATP Safe Links URL Detonation kicked in.
EmailEvents

| where PhishDetectionMethod == @"[""ATP Safe Links URL Detonation""]"

| project NetworkMessageId, DeliveryAction , DeliveryLocation

| join ( EmailUrlInfo

| project Url, NetworkMessageId  )

on NetworkMessageId

| project Url, DeliveryAction , DeliveryLocation

![](https://www.verboon.info/wp-content/uploads/2020/01/011520_2205_MicrosoftTh12.png)Hope you enjoyed reading this blog post, as always, any comments are welcome
Alex

