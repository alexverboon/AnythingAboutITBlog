I’ve been involved in Windows 7 deployments since the Beta came out in 2009 and before Windows 7 there was Vista, XP, Windows 2000, Windows NT and even Windows 3.11 and although over time the technology has changed the basic challenges of every migration remained the same. 

  If today someone asks me what I consider as being one of the top 10 challenges I’ve seen in Windows 7 deployment projects I must mention KMS. Yes despite the fact that in theory this is nothing more than just a service you install on one or two servers in your datacenter and publish an SRV resource record in DNS, this is something that keeps people busy in nearly any project I’ve been involved so far. 

  In today’s blog post I want to talk about some of the experiences I’ve made, provide some considerations you should take and provide some useful tips and references that will hopefully help making your KMS deployment as smooth as possible. 

  **Challenge #1 – What is KMS?**

  By now you would expect that anyone who’s dealing with Microsoft technology should be familiar with the term KMS right? Well if you’re a Windows engineer or consultant who’s busy with deployments this is probably an obvious thing, but hey let’s not forget our server admin who’s been busy keeping his Windows 2003 based infrastructure alive, so that the desktop guy could deploy his Windows XP boxes or the CTO who last poked within the Windows registry on a Windows NT 4.0 box. If they haven’t read about it yet and didn’t talk to their Microsoft TAM for a while, the term KMS doesn’t ring a bell for them. So the first thing that needs to happen is to create the awareness on the topic and ensure they understand what KMS is all about. 

  Now sending a whole bunch of technical references won’t help at this stage, what people need is a short presentation or video. The tech guy will get to the [technical documentation](http://technet.microsoft.com/de-ch/library/ff719787(en-us).aspx) later anyway. 

  *Volume Activation for Windows and Office 2010*

    

  **Challenge #2 – Where are the KMS keys?**

  The next challenge is often to obtain the volume license keys to activate KMS. Many companies have downloaded their enterprise media and license keys for Windows Server 2003 and XP long time ago, getting the Windows 7 installation sources and volume license keys can cause a challenge as often it’s unclear who has the access rights to the [Microsoft volume Licensing Center](https://www.microsoft.com/licensing/servicecenter/default.aspx). And even if they then make it to the portal, in the worst case they have to find out that their current license agreement doesn’t cover Windows 7 yet, and since often new license agreements aren’t negotiated over night this can cause further delays in deployment projects. So my advice here is to look at the licensing right at the beginning of any Windows 7 deployment project. 

  **Challenge #3 – Do we need new servers for this?**

  When saying “We need a KMS infrastructure for rolling out Windows 7” some people immediately get worried, as when they hear the word “infrastructure” they imagine big servers, storage….costs. Fact is, most customers are pleased to hear that they can host KMS on their existing infrastructure, given it meets the system requirements for KMS about which I talk later in more detail. So the recommendation here is to explain right at the beginning that this is not like an SQL Cluster or Exchange server, it’s basically just a “Service” or even if that is not 100% correct for non-tech people just call it an application that runs on a server. 

  **Challenge #4 – KMS Servers already exist, they just don’t know about it**

  This is where I have seen most of the issues so far. On any project I was involved I advised to check for existing KMS servers within the infrastructure before deploying the new what is supposed to be the global enterprise wide KMS infrastructure. The reason for doing so is that we’ve often seen that KMS has already been deployed for the activation of Windows 2008/2008-R2 servers or Windows Vista clients. In the worst case you will find several KMS servers that are all managed by different local IT departments. Now if you are planning companywide deployments you really want to put in place a corporate managed KMS infrastructure and get rid of the locally managed ones because they will cause problems when deploying Windows 7 and Office 2010 especially if they haven’t been configured with the correct activation keys. 

  To [identify any KMS servers](https://www.verboon.info/index.php/2010/01/identifying-kms-servers/) that have registered themselves in DNS simply run the following command:

  nslookup -type=srv _vlmcs._tcp

  If locally managed KMS servers were found the high level cleanup process could look as following: 

     
- Put in place the new companywide KMS infrastructure and ensure all needed KMS license keys are configured.     
- Remove the DNS records pointing to the local KMS servers, so that new clients and servers can’t find them anymore or at change the [priority and weight settings in DNS](http://technet.microsoft.com/de-ch/library/ff793405(en-us).aspx).     
- Make sure that the existing systems that used these local KMS servers are now properly talking to the new KMS servers. (Remove or update any hard coded registry settings if such were made).  

  **Challenge #5 Windows Server 2008 can be a showstopper**

  Companies that plan to deploy Windows 7 and Office 2010 must be aware that only Server 2003 and Server 2008-R2 are supported to host the KMS service. Running KMS on a Windows 2008 server is not supported and there is no patch to make it work. More details on the subject [here](https://www.verboon.info/index.php/2010/05/office-2010-kms-server-requirements/). 

  **Challenge #6 We got it all up and running but clients don’t activate.** 

  Patience is required because KMS requires a minimum number of computers (physical or VM) in a network environment. The organization must have at least 5 computers to activate Windows Server 2008 R2 and at least 25 computers to activate Windows 7 clients. 

  If you managed to get through or avoid the previously described challenges, KMS should really be a set and forget thing, nevertheless let me share some additional hints that might become useful when troubleshooting activation problems. 

  **Hint #1 – There is no GUI, all configurations is done using a script** 

  On both the server and client, almost all activation related configuration is done through the slmgr.vbs script that is included on every Windows 7 and Server 2008-R2 installation. For Office 2010 there is the ospp.vbs script. To become familiar with the options, just run slmgr.vbs or ospp.vbs. 

  **Hint #2 – it’s all in the event logs**

  When troubleshooting just filter on Events 12288 through 12294. More details [here](http://technet.microsoft.com/de-ch/library/ff793440(en-us).aspx). 

  **Hint #3 - Get license status with just one command**

  At the command prompt or start menu just type SLUI.EXE and the Windows Activation window will open and show the activation status. 

  [
![clip_image002](images/clip_image002_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/01/clip_image002.jpg)

  **Hint #4 – What does that error code mean?**

  Troubleshooting at a customer site and not time to look up the error code on the internet? Then try this: 

  At the command prompt type Slui.exe 0x2a <errorcode> like slui 0x2a 0xC004F00F

  More details [here](http://technet.microsoft.com/de-ch/library/ff793399(en-us).aspx)

  [
![clip_image004](images/clip_image004_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/01/clip_image004.jpg)

  **Hint #5 – for those who like WMI**

  Much license activation information can be accessed through WMI for both Windows and Office. For Windows look at the WMI classes SoftwareLicensingProduct and SoftwareLicensingService and for Office look for the WMI classes OfficeSoftwareProtectionProduct and OfficeSoftwareProtectionService. More details [here](http://technet.microsoft.com/en-us/library/ff793441.aspx)

  Finally I recommend you read the [FAQ](http://www.microsoft.com/licensing/existing-customers/product-activation-faq.aspx) about license keys and carefully read the documentation on TechNet [here](http://technet.microsoft.com/de-ch/library/ff719787(en-us).aspx). Last but not least, the good news is that in the long run we’ll get [Active Directory based volume activation](https://www.verboon.info/index.php/2011/11/windows-8-active-directory-based-volume-activation/), but only for Windows 8 systems.