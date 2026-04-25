---
title: "How to deploy your jump host in Azure"
layout: "post"
date: 2020-03-29T14:49:33Z
slug: "how-to-deploy-your-jump-host-in-azure"
aliases:
  - "/2020/03/how-to-deploy-your-jump-host-in-azure/"
description: "Due to the current COVID 19 pandemic, governments are urging their citizens to stay at home."
author: "Alex Verboon"
image: "img/post-heroes/how-to-deploy-your-jump-host-in-azure.png"
tags:
  - azure
  - jump-host
  - rdp
  - remote-access
  - securitiy
  - virtual-machine
  - Windows
  - PowerShell
  - Office
categories:
  - azure
  - remote-management
  - security
  - Windows
  - PowerShell
---
Due to the current CODV 19 pandemic, governments are urging their citizens to stay at home. For many people this means finding alternative ways to continue their work from home. This article is primarily aimed at IT administrators or IT consultants who do not have an existing solution in place and who are looking for a simple but secure solution to access their IT infrastructure remotely.

When saying existing solutions, I'm referring to remote access solutions like Citrix, Windows Virtual Desktop or corporate owned and security hardened Windows 10 notebooks with a VPN client, However not all companies have such solutions in place because maybe until recently there was no need for people to work remotely. With COVD 19 this all changed overnight.

If now companies must provide remote access to their employees at large scale, I still recommend pursuing solutions I mentioned above. But deploying such solutions doesn't happen overnight, so until these are in place, here's some guidance as to how to setup your jump host in Azure. I do especially recommend this setup to IT consultants who work for various customers. Instead of connecting to your customers IT infrastructure directly from your own device, consider setting up a dedicated jump host for each of your customers.

# Jump Host

So just in case you're asking yourself what's a jump host anyway? Here's the definition from Wikipedia:
*A jump server, jump host or jump box is a system on a network used to access and manage devices in a separate security zone. A jump server is a hardened and monitored device that spans two dissimilar security zones and provides a controlled means of access between them. The most common example is managing a host in a DMZ from trusted networks or computers.*
So in simple words, the idea is that you do not use the same device to read e-mail, browse the web, install software and perform administrative tasks for one or multiple IT infrastructures

# Real Life Scenario

I work as a Cyber Security Consultant mostly supporting my customers with the adoption of solutions included in the Microsoft Security suite and Windows 10. Many things can be done through the browser, i.e. managing security configurations within Azure AD, other tasks require that I access resources within the customers perimeter network, i.e. managing Active Directory Group Policy settings.

When I just can access resources through the browser for tasks that require read only access, I use Windows Defender Application guard that provides me with a browser that is isolated from my operating system. But when I need to access information with administrative privileges, use PowerShell or establish a VPN connection into the customers network I use my jump host in Azure.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy1.png)
# Prerequisites

To setup a jump host in Azure you need the following:

- An Azure Subscription either owned by your company or your own Pay as you go or MSDN subscription
- Credentials to access the customers Cloud infrastructure
- When your customer uses VPN software, the appropriate software installation binaries

# Setting up your Jump Host

Follow the hereafter described instructions to setup your jump host in Azure.
**#****Description****1**Logon to the **Azure Portal**[https://portal.azure.com](#) and select **Virtual Machines**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy2.png)**2**Select **Add
**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy3.png)**3**If you have multiple Azure subscriptions select the subscription. Next select **Create New** to create a new Resource Group

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy4.png)**4**Enter a **Name** for the resource group

*Example* rg_jumpstations

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy5.png)**5**Provide a **Name** for the virtual machine, here I recommend to use some sort of naming convention that can be used later to easily identify these jump hosts, for example to group them in the Defender ATP console or target configurations through Intune.

Example: RemoteJS01

Select the Azure **Region** where the virtual machine is deployed and the **availability option**.

Then select the [**image**](#) to use, in this example I use the Windows 10 Enterprise version 1909 from the Azure image gallery. See the next step for details on image selection.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy6.png)**5a**Below are the details of the VM Size that I am using. It's a VM with 8GB of RAM and two virtual CPUs, this provides me with enough performance to perform remote administrative tasks and connect to the customers network. Also this VM is supported on Generation 2 VMs, more on that later.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy7.png)**6**When you have selected the VM Size, the estimated cost per month is displayed. Note that the cost shown is based on running the VM permanently 24/7. You are most likely only going to start the VM when you need remote access, so the depending on the amount of time you spend here, the cost will be significantly lower.

*Real world:* For some customers, using this solution costs me less than 10 CHF per month.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy8.png)**7**Provide a **Username** and a **Password** for the local user account that is created on the Jump Host.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy9.png)**8**Next, we are going to define the inbound port rules. Here select **Allow selected ports** then select **RDP (3389). **You will see a warning but don't worry, we only enable this temporarily for our setup, we will disable this later again when we apply the Just in time VM access.

If you already have a Windows 10 E3/E5 license, select **Yes** for the Save Money option.

Select **Next Disks** at the bottom of the screen to move to the next configuration page.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy10.png)**9**Select the [**OS Disk type**](#). Here you can choose between Standard SSD, Premium SSD or HDD. For this purpose, Standard SSD will do.

Select **Next Networking** at the bottom of the screen to move to the next configuration page.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy11.png)**10**Here I recommend to setup a dedicated network and network security group for your Jump hosts. Adopt the settings as shown below, most important, select the **Advanced** option for the setup of the**[Network Security Group](#)**.

Select **Next Management** at the bottom of the screen to move to the next configuration page.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy12.png)**11**Configure the Management options for Monitoring as shown below.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy13.png)**12**Configure the [**Identity**](#) and [**Auto Shutdown**](#) options as shown below.

Select **Next Advanced** at the bottom of the screen to move to the next configuration page.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy14.png)**13**When we setup our jump host, we want to make sure Windows Defender is enabled and configured, therefore click on **Select an extension to install**. If you plan to manage your Jump Hosts with Intune later, you can consider skipping this step.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy15.png)**13a**Select **Microsoft Antimalware** and then clock on **Create**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy16.png)**13b**Configure the Windows Defender Settings

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy17.png)**14**If you decided to add the Antimalware extension, it's now displayed in the list of extensions.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy18.png)**15**Configure the **VM Generation** option to **Gen 2**

I selected a Generation 2 VM so that I can make use of as many features as possible, however please note that although Generation 2 VM are configured to use UEFI instead of BIOS, not all features are available. One important feature that is still missing is secure boot. For more details I recommend reading the Microsoft docs page [https://docs.microsoft.com/en-us/azure/virtual-machines/windows/generation-2?WT.mc_id=thomasmaurer-blog-thmaure](#) and Thomas Maurer's blog post [GENERATION 2 VM SUPPORT ON AZURE – AND WHY SHOULD I CARE?](#)

Select **Next Tags** at the bottom of the screen to move to the next configuration page.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy19.png)**16**If you want to make use of [**Tags**](#) for your Azure resources, specify tags and values.

Select **Next Review + Create ** at the bottom of the screen to move to the next configuration page.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy20.png)**17**When all configuration settings are validated, click on **Create** at the bottom of the screen to start the deployment of your jump host virtual machine.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy21.png)**18**Now sit back and wait until the deployment completes.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy22.png)**19**If all goes well, you get a notification as sown below.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy23.png)
# Secure Access to your Jump Host

Remember that in step 8 we allowed inbound connections through RDP (3389). Now it's a bad idea to leave this port permanently open, because this would make our Jump host vulnerable to RDP attacks. Read more about RDP brute force attacks here: [Data science for cybersecurity: A probabilistic time series model for detecting RDP inbound brute force attacks](#)

To prevent port 3389 from being permanently open, you can use two methods:

- Use Azure Security Center [**Just in time VM access**](#) – **Highly****Recommended! **A Just-in-time access enables you to lock down inbound traffic to your VM, by allowing access for only a limited time
- Manually enable / disable port 3389 access (there is a high risk you are going to forget doing this, so not really recommended)

## Configure Just in Time VM Access in Security Center

Follow the below steps to enable Just in Time VM access using Azure Security Center
**#****Description****1**Logon to the **Azure Portal**[https://portal.azure.com](#) and select **Security Center**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy24.png)**2**Within the Security Center portal, select **Just in time VM access**, then in the virtual machines list select **Recommended, **then select to VM to enable just in time VM access for then click on the **Enable JIT on VMs **button

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy25.png)**3**A list of ports is displayed that will only be enabled when using just in time VM access. By default, JIT activation lasts for 3 hours, if you feel that this is not enough click on a row and select the …. Menu at the end of the row to change the default settings. When completed save the settings.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy26.png)![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy27.png)**4**When JIT enabled, the virtual machine is listed in the list of **Configured** VMs for JIT

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy28.png)**5**Below is an example of a VM where Just in time VM access is configured and currently active, as you can see the Default-allow-RDP rule is set to Deny and the Security Center JIT Rules for RDP are set to Allow.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy29.png)
## Manually Enabling RDP access

Follow the below steps to manually configure access to RDP
**#****Description****1**Logon to the **Azure Portal**[https://portal.azure.com](#) and select the Jump Host virtual machine.**2**Select Networking, default-allow-RDP rule and then configure the Action Allow or Deny.

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy30.png)**3**You can of course use this as an alternative, just in case when you are not using Azure Security center, however the risk is high that you forget to toggle between deny and allow and so leave the machine vulnerable to RDP attacks while it's running unattended.
# Accessing the Jump Host

Now that you have completed the setup and configuration of your Jump Host, let's access it.
**#****Description****1**Logon to the **Azure Portal**[https://portal.azure.com](#) and select **Virtual Machines
**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy31.png)**2**Select your **Jump Host** virtual machine, and check the Status, if the VM is not running, select **Start**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy32.png)**3**Once the your Jump Host VM is running, select **Connect, RDP**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy33.png)**4**Next select **Request Access**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy34.png)

And wait for the access request to be **approved **and then select **Download RDP file**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy35.png)**5**Select **Open file** when the RDP file is downloaded

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy36.png)

Select **Connect**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy37.png)

Then enter the **credentials** you defined in **Step 7** when you provisioned the VM

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy38.png)

Confirm with **Yes**![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy39.png)**6****Congratulations**, you have successfully logged on to your Jump Host running in Azure

![](https://www.verboon.info/wp-content/uploads/2020/03/032920_1446_Howtodeploy40.png)
# Next Steps

Now that you have your Jump Host running in Azure, you can use this environment to remotely access your customers on premise IT infrastructure through VPN or Cloud infrastructure though the browser.

# Hardening your Jump Host

Here's what I recommend adding further security for your virtual jump host:

- Onboard the device in Microsoft Defender ATP if you are using this already
- Apply the Microsoft Security baseline
- Enable Windows Defender Network Protection and Exploit Guard
- Enable Virtualization based security, if you deployed a Gen 2 VM
- Do NOT install any productivity tools such as Office Outlook, 3rd party software, i.e. keep the VM as clean as possible, it's only a considered to be a jump Host, not a working device.
- Do NOT use this VM for general internet browsing purposes

# Conclusion

If you have nothing in place today to securely access a remote on premise or cloud hosted infrastructure, the here described solution can provide you with an intermediate solution that enables you to continue working in a more secure way, i.e. not using your own device to establish a direct connection to the target IT infrastructure. However, If you need a long term solution that provides more scalability, security and management options, I recommend looking into options such as Windows Virtual Desktop.

I hope you found this article useful, as always comments are welcome

Alex

