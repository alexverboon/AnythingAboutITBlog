---
title: Preparing my Application Guard for Office test lab
layout: post
date: '2020-11-21T17:24:13Z'
slug: preparing-my-application-guard-for-office-test-lab
aliases:
- /2020/11/preparing-my-application-guard-for-office-test-lab/
description: Application Guard for Office in action - secure isolated container for
  Office documents.
author: Alex Verboon
image: img/post-heroes/preparing-my-application-guard-for-office-test-lab.png
tags:
- application-guard
- Office
categories:
  - security
  - Office
---

Hello everyone, today I wanted to see application guard for office in action. If you are not familiar with application guard for office, I suggest you read the following articles / documentation.

- [Microsoft Defender Application Guard for Office](#)
- [Application Guard for Office](#)

And now let me walk you through the steps to get application guard for office working in your test lab.

- Deploy Windows 10 20H1 or 20H2
- When running your test client in Hyper-V you have to enable [nested virtualization](#) so that we can later enable Application Guard![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy1.png)
- Next, we turn on the Microsoft Defender Application Guard. Now if your system does not meet the minimum [requirements](#) the option is greyed out as shown in the screenshot below.
![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy2.png)
But luckily there is a workaround described [here](#). Once you have added these registry keys, you will be able to enable Application Guard
![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy3.png)
- Now we have to enable Microsoft Defender Application Guard in managed mode, so that it can be used for Microsoft Edge and Office. Open the Group Policy editor and navigate to: Computer Configuration \ Administrative templates \ Windows Components \ Microsoft Defender Application Guard and open the setting: Turn on Microsoft Defender Application Guard in Managed Mode and set the value to 3 If you want to enable Application Guard for Edge and Office or 2 for Office only.
![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy4.png)
- Now that we have Defender Application Guard ready, let us move on to Office. The [official documentation](#) mentions Office Beta Channel Build version 2008 16.0.13212 or later, however as per [this announcement](#) it should work with the Insider current channel as well. Configure the following group policy settings for Office 365 Apps for Enterprise to enable insider releases:User Configuration \ Administrative Templates \ Microsoft Office 2016 \ miscellaneous \ Show the option for Office Insider

![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy5.png)
- Start Office and enable the Office Insider release. Select File, Account, Office Insider, **Change Channel**![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy6.png)

Choose the Channel, Beta or Current Channel (Preview) and then select Update options, update Office and once installed you should see the version changed to Beta or Current Channel Preview.

![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy7.png)
- Great, now we have everything in place to see Defender Application Guard for Office in action. Let us open a document that comes from the internet.
![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy8.png)

While Word is starting, it is telling us that the document is opened in Application Guard

![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy9.png)![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy10.png)
- And finally, if you have onboarded the device in Microsoft Defender for Endpoints, you can run the following query to see when Application Guard for Office was launched.![](https://www.verboon.info/wp-content/uploads/2020/11/112120_1710_Preparingmy11.png)
Have a great day

Alex

