---
title: Exploring Microsoft Security Update information with PowerShell
layout: post
date: '2017-12-29T13:36:30Z'
slug: exploring-microsoft-security-update-information-with-powershell
aliases:
- /2017/12/exploring-microsoft-security-update-information-with-powershell/
description: Nowadays regular deployment of security updates is a must, whether at
  home or within the enterprise. If you are responsible to keep systems up to date...
author: Alex Verboon
tags:
- cve
- security
- updates
- vulnerability
- Windows
- PowerShell
categories:
- security
- Windows
- PowerShell
---
Nowadays regular deployment of security updates is a must, whether at home or within the enterprise. If you are responsible to keep systems up to date you deploy the latest updates as soon as possible.  But it is equally important to understand the vulnerabilities being addressed by these updates.

The Microsoft Security Update Guide allows you to find detailed information about security updates. Go to [https://portal.msrc.microsoft.com/en-us/](https://portal.msrc.microsoft.com/en-us/) and select “Go to the security update Guide”

![image](https://ftp.verboon.info/wp-content/uploads/7cdc1454a08e_9612/image.png)

Next select all options to show (1) and a text filter (2). In this example I have entered “1709” to see everything related to Windows 10 – 1709.

![image](https://ftp.verboon.info/wp-content/uploads/7cdc1454a08e_9612/image_3.png)

The “Details” column includes references to Microsoft Security Advisories or Common Vulnerabilities and Exposures (CVE) articles.

Now let’s take a look how to explore this information through PowerShell using the Microsoft Security Update API. Before we can use the cmdlets included in the MsrcSecurityUpdates PowerShell module we must obtain an API key.

Go to [https://portal.msrc.microsoft.com/en-us/developer](https://portal.msrc.microsoft.com/en-us/developer) (sign in with your Microsoft account) and then select “show” to expose your API key.

![image](https://ftp.verboon.info/wp-content/uploads/7cdc1454a08e_9612/image_4.png)

Next open PowerShell and install the MsrcSecurityUpdates Module.

```
### Install Module
Install-Module -Name MsrcSecurityUpdates
### Load the module
Import-Module -Name MsrcSecurityUpdates
```

 

Set the API key using the following command:

```
$apikey = "<PASTE KEY HERE>"
Set-MSRCApiKey -ApiKey $apikey
```

 

Okay, now we are ready to explore security update information through PowerShell.

To get a list of all Security updates that are available through the API simply enter the following command:

```
Get-MsrcSecurityUpdate
```

 

Now let’s take a look at the most recent update from December 2017.

```
$id = Get-MsrcCvrfDocument -ID '2017-Dec'
$affsw = Get-MsrcCvrfAffectedSoftware -Vulnerability $id.Vulnerability -ProductTree $id.ProductTree
$affsw
$cvesum = Get-MsrcCvrfCVESummary -Vulnerability $id.Vulnerability -ProductTree $id.ProductTree
$cvesum
$explind = Get-MsrcCvrfExploitabilityIndex -Vulnerability $id.Vulnerability
$explind
```

 

To generate a report with all CVE details included, we use the following command:

```
Get-MsrcVulnerabilityReportHtml -Vulnerability $id.Vulnerability -ProductTree $id.ProductTree | Out-File -FilePath "C:\temp\$($id.documenttitle).html"
Invoke-Item -Path "C:\temp\$($id.documenttitle).html"
```

 

 

![image](https://ftp.verboon.info/wp-content/uploads/7cdc1454a08e_9612/image_5.png)

I hope this article provided you with some inspiration as to how to explore security update information through PowerShell.

 	
- Additional Information:
PowerShell script that uses the Security Update API
[https://sqljana.wordpress.com/2017/08/31/powershell-get-security-updates-list-from-microsoft-by-monthproductkbcve-with-api/
](https://sqljana.wordpress.com/2017/08/31/powershell-get-security-updates-list-from-microsoft-by-monthproductkbcve-with-api/)
 	
- Security Update API
[https://portal.msrc.microsoft.com/en-us/developer](https://portal.msrc.microsoft.com/en-us/developer)

