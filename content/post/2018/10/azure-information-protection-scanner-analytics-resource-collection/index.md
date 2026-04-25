---
title: "Azure Information Protection Scanner & Analytics – Resource Collection"
layout: "post"
date: 2018-10-31T18:42:25Z
slug: "azure-information-protection-scanner-analytics-resource-collection"
aliases:
  - "/2018/10/azure-information-protection-scanner-analytics-resource-collection/"
description: "Hey there, This might sound like a bad excuse for not writing up a whole blog post, but in fact I had planned to write a few words about the Azure Inf..."
author: "Alex Verboon"
tags:
  - aip
  - protection
  - scanner
  - PowerShell
categories:
  - azure-information-protection
  - PowerShell
---
Hey there,

This might sound like a bad excuse for not writing up a whole blog post, but in fact I had planned to write a few words about the Azure Information Protection Scanner and the recently announced Azure Information Protection Analytics that provides a central reporting capability for the AIP Scanner. Those that have used the AIP Scanner before, will agree that, gathering scanner results data was quite tedious as you had to grab plain text files from the local system and then process them manually or though some home-brew scripting to visualize the results.

However since I prefer to produce value–add blog content and not just reproduce stuff, I did a little bit of research this evening prior writing down my blog post and found out that what I had intended to describe is already mostly available, especially with regards to automating the AIP Scanner installation and the Azure information Protection Analytics workspace setup. Therefore, I just turn this blog post into a brief summary of references that I've been using myself over the past months while working with the AIP Scanner. I hope it's going to be useful for those that need a jump start into the topic.

If you haven't deployed the AIP Scanner before, I recommend reading the official Microsoft documentation.

 	
- Deploying the Azure Information Protection scanner to automatically classify and protect files
[https://docs.microsoft.com/en-us/azure/information-protection/deploy-aip-scanner](https://docs.microsoft.com/en-us/azure/information-protection/deploy-aip-scanner)
 	
- Central reporting for Azure Information Protection
[https://docs.microsoft.com/en-us/azure/information-protection/reports-aip](https://docs.microsoft.com/en-us/azure/information-protection/reports-aip)

Real hands-on experience is described in the following articles:

 	
- Installation, Configuration, and Usage of the AIP Scanner
[https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Installation-Configuration-and-Usage-of-the-AIP-Scanner/ba-p/221792](https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Installation-Configuration-and-Usage-of-the-AIP-Scanner/ba-p/221792)
 	
- Full AIP Scanner Configuration (AIP Premium P1 Edition)
[https://blogs.technet.microsoft.com/kemckinn/2018/07/18/full-aip-scanner-configuration-aip-premium-p1-edition/](https://blogs.technet.microsoft.com/kemckinn/2018/07/18/full-aip-scanner-configuration-aip-premium-p1-edition/)
 	
- Azure Information Protection Scanner
[https://alberthoitingh.com/2017/10/19/azure-information-protection-scanner/](https://alberthoitingh.com/2017/10/19/azure-information-protection-scanner/)
 	
- Configuring AIP Scanner
[https://samilamppu.com/2017/11/17/configuring-aip-scanner/](https://samilamppu.com/2017/11/17/configuring-aip-scanner/)

Then there is a Microsoft Case description from Microsoft how they use the AIP scanner.

 	
- Automating data protection with Azure Information Protection scanner
[https://www.microsoft.com/itshowcase/Article/Content/1070/Automating-data-protection-with-Azure-Information-Protection-scanner](https://www.microsoft.com/itshowcase/Article/Content/1070/Automating-data-protection-with-Azure-Information-Protection-scanner)

And finally, two articles that describe the recently announced Azure Information Protection Analytics. This is really a great enhancement as it now provides central logging for Azure Information Protection Scanner environments by storing the results into Azure Log Analytics.

 	
- Cataloging your Sensitive Data with AIP, Even Before Configuring Labels!
[https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Cataloging-your-Sensitive-Data-with-AIP-Even-Before-Configuring/ba-p/267241](https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Cataloging-your-Sensitive-Data-with-AIP-Even-Before-Configuring/ba-p/267241)

The above article also contains some very cool PowerShell code to fully automate the creation of the AIP Service Account, Azure App registrations and token script generation. The manual process is described [here](https://docs.microsoft.com/en-us/azure/information-protection/deploy-aip-scanner).

 	
- Data discovery, reporting and analytics for all your data with Microsoft Information Protection
[https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Data-discovery-reporting-and-analytics-for-all-your-data-with/ba-p/253854](https://techcommunity.microsoft.com/t5/Azure-Information-Protection/Data-discovery-reporting-and-analytics-for-all-your-data-with/ba-p/253854)

**Bonus tip:** If you're concerned about the costs for Azure Log Analytics, you can start with the FREE Tier plan, your data will only be retained for 30 days, but it will give you a god idea of how much log analytics usage you might be using, you can then later change the pricing tier to "per GB".

