---
title: Collecting AzureAD User Authentication Method Information
layout: post
date: '2021-02-07T13:28:44Z'
slug: collecting-azuread-user-authentication-method-information
aliases:
- /2021/02/collecting-azuread-user-authentication-method-information/
description: Collect Azure AD user authentication methods using Microsoft Graph PowerShell
  for MFA and passwordless analysis.
author: Alex Verboon
image: img/post-heroes/collecting-azuread-user-authentication-method-information.png
tags:
- authenticationmethod
- Entra
- MFA
- PowerShell
categories:
- EntraID
- PowerShell
---
Hello everyone, last Friday I received an email from one of my customers, asking how to identify users in Azure AD that have enabled [passwordless sign-in with the Microsoft Authenticator app](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-passwordless-phone). Previously I usually made use of the [Script for Azure MFA authentication method analysis](https://docs.microsoft.com/en-us/samples/azure-samples/azure-mfa-authentication-method-analysis/azure-mfa-authentication-method-analysis/) but that script uses the MSOnline PowerShell module where the `Get-MsolUser` cmdlet does not expose the information about these newer authentication methods.

So heading over to Microsoft Graph and there we can grab all authentication methods for users as shown in the example below.

![](images/020721_1322_CollectingA1.png)

So, I created [Get-AzureADUserAuthMethodInventory.ps1](https://github.com/alexverboon/PowerShellCode/tree/main/AzureAD/MFA/MfaAuthMethodsAnalysisV2). The script first retrieves all users in Azure AD and then retrieves the registered authentication methods for each user.

If you have not done so yet, install the Microsoft Graph PowerShell modules.

```powershell
Find-Module -Name "Microsoft.Graph" | Install-Module -Scope CurrentUser
Find-Module -Name Microsoft.Graph.Identity.AuthenticationMethods | Install-Module -Scope CurrentUser
```

Then run the following command.

```powershell
Connect-Graph -Scopes @("UserAuthenticationMethod.Read.All", "User.Read.All")
```

Follow the instructions and grant consent.

![](images/020721_1322_CollectingA2.png)

And finally run the script.

```powershell
$AuthInfo = .\Get-AzureADUserAuthMethodInventory.ps1
```

![](images/020721_1322_CollectingA3.png)

For each user found in Azure AD the following information is collected.

![](images/020721_1322_CollectingA4.png)

Filter the results as needed.

![](images/020721_1322_CollectingA5.png)

The script and instructions can be found on GitHub here: [https://github.com/alexverboon/PowerShellCode/tree/main/AzureAD/MFA/MfaAuthMethodsAnalysisV2](https://github.com/alexverboon/PowerShellCode/tree/main/AzureAD/MFA/MfaAuthMethodsAnalysisV2)

Hope you liked this blog post, as always feedback is welcome.

Alex




