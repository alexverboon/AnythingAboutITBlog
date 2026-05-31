---
title: User Spam & Phish Submissions configuration in Office 365 – Part 1
layout: post
date: '2020-01-19T13:54:51Z'
slug: user-spam-phish-submissions-configuration-in-office-365-part-1
aliases:
- /2020/01/user-spam-phish-submissions-configuration-in-office-365-part-1/
description: A new feature being rolled out in Office 365 to configure user submissions.
author: Alex Verboon
image: img/post-heroes/user-spam-phish-submissions-configuration-in-office-365-part-1.png
categories:
  - 'PowerShell'
tags:
  - 'Office'
  - 'Spam'
---
Yesterday I noticed a [tweet](#) from @Pawp81 about a new feature being rolled out in Office 365 to configure user submissions.  So, let's have a look at this. When enabling the 'Report Message' add-in in Office 365, users can report misclassified email, whether safe or malicious, to Microsoft and its affiliates for analysis. Until now IT admins had to deploy the 'Report Message' add-in to their end users by configuring the centralized add-in deployment within the Microsoft 365 admin center as described [here](#) Furthermore when IT admins wanted to receive a copy of a reported message, a transport rule had to be created as described [here](#).

This has now all been simplified by a new user submissions policy that can be configured within the Office 365 security portal.

# Policy Configuration

Under the Threat management node, select Policy.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi1.png)

The User Submissions Policy provides us with several configuration options:

- **Turn on Report Message add-in for Outlook **– with this setting you can easily enable the Report Message add-in for all users with a single click. If you prefer to do a staged rollout, then use the process described [here](#). Note that it can take up to 12 hours until the Report Message add-in appears within the Outlook client.
- **Set up a Reporting Mailbox – **Here you can configure to send a copy of reported messages to a centralized mailbox.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi2.png)
- **Customize Confirmation Message –** allows you to configure custom messages shown before and after the user reports messages.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi3.png)
# End User Experience

Once the add-in is enabled within Outlook, users will see the 'Report Message' add-in within the Office ribbon.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi4.png)

And when they select Junk or Phishing, the custom before submission message is displayed.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi5.png)

And once submitted the custom after submission text is displayed.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi6.png)

At the time of writing this blog post (Sunday 19 January 2020), the reported messages weren't yet forwarded to the specified reporting mailbox, I assume maybe because this new feature Is still in the process of being rolled out. I will follow up on that later.

When sending the reported messages to Microsoft they are send to the following e-mail addresses

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi7.png)

More details about submitting spam and phish messages can be found [here](#)
# PowerShell

The configuration settings for the User submission settings can be retrieved through PowerShell, by using the **Get-ReportSubmissionPolicy** cmdlet that's included in the Exchange Online PowerShell Module.

![](https://www.verboon.info/wp-content/uploads/2020/01/011920_1351_UserSpamPhi8.png)

