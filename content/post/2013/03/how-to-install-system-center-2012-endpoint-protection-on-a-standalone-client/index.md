---
title: "How to install System Center 2012 Endpoint Protection on a standalone client"
layout: "post"
date: 2013-03-24T14:48:33Z
slug: "how-to-install-system-center-2012-endpoint-protection-on-a-standalone-client"
aliases:
  - "/2013/03/how-to-install-system-center-2012-endpoint-protection-on-a-standalone-client/"
description: "Suppose you have a need to deploy System Center 2012 Endpoint Protection to a number of clients that later run in standalone mode, meaning that they a..."
author: "Alex Verboon"
image: "img/post-heroes/how-to-install-system-center-2012-endpoint-protection-on-a-standalone-client.png"
tags:
  - command-line
  - endpoint-protection
  - policy
  - scepinstall-exe
  - stand-alone
categories:
  - endpoint-protection
  - sccm-2012
---
Suppose you have a need to deploy System Center 2012 Endpoint Protection to a number of clients that later run in standalone mode, meaning that they are not joined to a domain, can’t be managed by SCCM and operate in a network that is not connected to your corporate network. 

  The installation source **scepinstall.exe** for the System Center Endpoint Protection agent is stored within the SCCM 2012 client installation folder on the SCCM 2012 SP1 server under C:\Program Files\Microsoft Configuration Manager\Client. Within that same directory we also find the endpoint protection default policy settings stored as **ep_defaultpolicy.xml**, but we won’t use this , as we are going to prepare our own policy that meets our requirements for a standalone unmanaged client. 

  To create a standalone policy open the Configuration Manager 2012 Console and under Assets and Compliance select Endpoint Protection / Antimalware Policies. Then select Create Antimalware policy. 

  Configure the various settings as per your requirements. 

  [
![2013-03-24_14h58_38](images/2013-03-24_14h58_38_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/03/2013-03-24_14h58_38.png)

  One very important setting is the Definition Updates Source configuration which by default points to the Configuration Manager. For our standalone scenario we will enable Microsoft Update and Microsoft Malware Protection Center only. If your clients do not have direct connectivity to the internet the use of a UNC share could also be an alternative, but then requires that you periodically update the share with latest definition updates packages.  

  [
![2013-03-24_14h59_12](images/2013-03-24_14h59_12_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/03/2013-03-24_14h59_12.png)

  Finally we export the settings and save them as standalone.xml

  [
![image](images/image_thumb6.png)
](https://www.verboon.info/wp-content/uploads/2013/03/image6.png)

  To install the System Center Endpoint Protection client run the following command (both the installer and policy file are stored in C:\Sources).

  **scepinstall.exe /s /q //policy C:\Sources\standalone.xml**

  Should you not wish to have the installer searching and installing definition updates, just add the **/NoSigsUpdateAtInitialExp** option. 

  If at some point you would need to change/update settings, simply create/update a new policy, export it within the Configuration Manager 2012 console and then run the following command on the client. 

  C:\Program Files\Microsoft Security Client\**ConfigSecurityPolicy.exe** c:\Sources\standalone2.xml

  [
![2013-03-24_15h44_12](images/2013-03-24_15h44_12_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/03/2013-03-24_15h44_12.png)

