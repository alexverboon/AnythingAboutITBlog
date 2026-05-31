---
title: "Shedding Light on Dormant Sensitive Accounts"
layout: "post"
date: 2025-07-08T15:34:54Z
slug: "shedding-light-on-dormant-sensitive-accounts"
aliases:
  - "/2025/07/shedding-light-on-dormant-sensitive-accounts/"
description: "Use Microsoft Defender XDR and KQL to enrich dormant sensitive account findings and add missing account context for remediation."
author: "Alex Verboon"
image: "img/post-heroes/shedding-light-on-dormant-sensitive-accounts.png"
categories:
  - 'Security'
tags:
  - 'Defender for Identity'
  - 'KQL'
  - 'Account Security'
---
Dormant sensitive accounts are a high-risk identity exposure. In Microsoft Defender XDR, the recommendation **Remove dormant accounts from sensitive groups** helps surface these accounts, including whether they are inactive, disabled, or have expired credentials.

![](images/shedding-light-on-dormant-sensitive-accounts-01.png)

You can export the detected entities, but the export often contains limited context. In many cases, you only get entity names or SID values, which makes remediation harder when you need ownership and organizational details.

![](images/shedding-light-on-dormant-sensitive-accounts-02.png)

A practical approach is to use the SID values to enrich the result set with identity attributes from `IdentityInfo`. You can quickly build a SID variable list using KustoVars, then query Defender XDR for additional context.

![](images/shedding-light-on-dormant-sensitive-accounts-03.png)

![](images/shedding-light-on-dormant-sensitive-accounts-04.png)

Use the following query under your SID variable block:

```kusto
IdentityInfo
| where TimeGenerated > ago(21d)
| where OnPremSid in~ (sid_list)
| summarize arg_max(TimeGenerated,*) by OnPremSid
| project AccountDisplayName, AccountName, AccountDomain, OnPremSid,
          OnPremObjectId, CompanyName, Department, Country,
          AccountUpn, DistinguishedName, IsAccountEnabled, Manager
```

![](images/shedding-light-on-dormant-sensitive-accounts-05.png)

With this enriched view, you can quickly assess account purpose, ownership, and placement before taking action. That makes it easier to decide whether dormant sensitive accounts should be disabled, cleaned up, or removed from sensitive groups.
