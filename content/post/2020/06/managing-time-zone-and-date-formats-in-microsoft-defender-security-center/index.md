---
title: "Managing Time Zone and Date formats in Microsoft Defender Security Center"
layout: "post"
date: 2020-06-09T15:49:25Z
slug: "managing-time-zone-and-date-formats-in-microsoft-defender-security-center"
aliases:
  - "/2020/06/managing-time-zone-and-date-formats-in-microsoft-defender-security-center/"
description: "When you receive security alerts or investigate security events, the aspect of time is an important element."
author: "Alex Verboon"
image: "img/post-heroes/managing-time-zone-and-date-formats-in-microsoft-defender-security-center.png"
tags:
  - TimeZone
categories:
- Microsoft Defender XDR
---
When you receive security alerts or are investigating security related events , the aspect of time is important element. By default, date and time is displayed in Coordinated Universal Time (UTC) within the Microsoft Defender security center portal.

In todays' blog post, I want to provide you with some insights and tips how to manage Timezone and the date time format within the Microsoft Defender security center.

# Time zones

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim1.png)

You can use the **Time zone** menu to change the time to your local time.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim2.png)

Because my client is located in the Central European zone, Timezone local is displayed as UTC +2:00.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim3.png)

Once I change the Timezone to local, the time is displayed as my local time.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim4.png)

Suppose my client is located in Melbourne Australia, the Time zone menu displays the following option

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim5.png)

Now the time is displayed in Melbourne local time.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim6.png)
# Date and Time formats

Okay now let us take a look at how date and time is formatted within the portal. By default, date and time is displayed as following:

- Month, Day, Year , hour (in 12-hour format), minute (AM/PM)

In order to display date and time in your preferred format, we have to add additional languages to our browser configuration. For demonstration purposes I have added English United Kingdom and German (Switzerland) to my Microsoft Chromium Edge browser configuration.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim7.png)

After refreshing the page (F5), the Time zone menu now also shows us locale options. After changing the locale to de-CH (German Switzerland) the date and time is displayed differently,

- Day, Month, Year, hour (in 24-hour format), minutes.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim8.png)

The official documentation for time zone settings in defender security center is here: [https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/time-settings](#)
# Advanced Hunting

Now let us move on and let's look at how date and time is displayed in advanced hunting. As described in the Kusto query language [reference](#):

*A datetime value in Kusto is always in the UTC time zone. Displaying datetime values in other time zones is the responsibility of the user application that displays the data, not a property of the data itself. Should time zone values be required to be kept as a part of the data, a separate column should be used (providing offset information relative to UTC).
*

I also found the following [statement](#) with regards to a Kusto native function to convert UTC to local time.

Well luckily, the time zone settings also work within the advanced hunting portal, in the below example, the Timezone is set to UTC.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim9.png)

And when changing the Timezone to Timezone local the results are displayed in local time.

![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim10.png)

How about the date time format? Well the answer is the locale settings have no effect on how the results of an advanced hunting query are displayed, if you want to change the format, you have to use the Kusto scalar function [format_datetime()](#)```
DeviceAlertEvents
| where DeviceName contains "TestClient6"
| extend TimestampFormatted = format_datetime(Timestamp,"dd.MM.yyyy HH:mm:ss")
| project-reorder Timestamp, TimestampFormatted
| top 5 by Timestamp
```
![](https://www.verboon.info/wp-content/uploads/2020/06/060920_1544_ManagingTim11.png)

See the date is now displayed as we are used to here where I live, i.e. dd.MM.yyyy (Day before the month and using the . (dot) to separate the values instead of the / (forward slash).

Have a great day

Alex

