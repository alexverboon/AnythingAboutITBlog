---
title: "ConfigMgr 2012 local GPO settings"
layout: "post"
date: 2013-08-13T22:26:06Z
slug: "configmgr-2012-local-gpo-settings"
aliases:
  - "/2013/08/configmgr-2012-local-gpo-settings/"
description: "When configuring ConfigMgr 2012 client settings, notice that some of these settings result in Local Group Policy Settings being applied to the client...."
author: "Alex Verboon"
image: "img/post-heroes/configmgr-2012-local-gpo-settings.png"
tags:
  - bits
  - configmgr
  - configuration-manager
  - group-policy
  - local-group-policy
  - remote-desktop
  - wua
categories:
  - configmgr
  - group-policy
---
When configuring ConfigMgr 2012 client settings, notice that some of these settings result in Local Group Policy Settings being applied to the client. If you’re sure that you have not configured any other local GPOs, then a simple way to find out what settings are applied by ConfigMgr is to open the Local Group Policy Editor (gpedit.msc( and filter for configured settings. 

 [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image.png)

 When configuring the Background Intelligent Transfer Settings within ConfigMgr, the settings are applied into a local GPO. 

 [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image1.png)

 [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image2.png)

 Also configuring some of the Remote Tools settings result in a local GPO setting. 

 [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image3.png)

 [
![image](images/image_thumb4.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image4.png)

 [
![image](images/image_thumb5.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image5.png)

 [
![image](images/image_thumb6.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image6.png)

 Although not a client agent setting, also the Intranet Microsoft Update service location is set through a local GPO.

 [
![image](images/image_thumb7.png)
](https://www.verboon.info/wp-content/uploads/2013/08/image7.png)

 Conclusion: make sure that there are not conflicts with settings applied via GPO and Configuration Manager. 

 **Additional information worth reading**

 Observation on SCCM Clients BITS Settings
[http://blog.tyang.org/2012/05/05/my-observation-on-sccm-clients-bits-settings/](http://blog.tyang.org/2012/05/05/my-observation-on-sccm-clients-bits-settings/)
Configuration Manager Software Update Management and Group Policy
[http://blog.configmgrftw.com/?p=88](http://blog.configmgrftw.com/?p=88)
[http://blog.configmgrftw.com/?p=89](http://blog.configmgrftw.com/?p=89)

