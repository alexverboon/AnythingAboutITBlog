---
title: "How to automate the creation of Windows Eventlog Custom Views"
layout: "post"
date: 2011-12-17T16:32:31Z
slug: "how-to-automate-the-creation-of-windows-eventlog-custom-views-2"
aliases:
  - "/2011/12/how-to-automate-the-creation-of-windows-eventlog-custom-views-2/"
description: "In the past couple of days I have been working on measuring system boot performance and you are probably going to see some posts from me on that subje..."
author: "Alex Verboon"
image: "img/post-heroes/how-to-automate-the-creation-of-windows-eventlog-custom-views-2.png"
tags:
  - boot
  - boot-performance
  - custom-view
  - eventlog
  - eventvwr-exe
categories:
  - eventlog
  - tip
  - windows-7
---
In the past couple of days I have been working on measuring system boot performance and you are probably going to see some posts from me on that subject soon. Today I want to share with you how you can automate the creation of a Windows Eventlog custom view.   

  While running these boot performance tests I reinstalled Windows several times on different systems and each time I wanted to collect the boot performance data from these clients I had to create a custom view within the Windows Event log to filter out the boot events. Well after doing that a few times manually I thought I would be better of to get that thing automated.

  First open the Windows Event log viewer by launching eventvwr.exe then select Custom Views, Create Custom View. Then select the custom view options as shown below. 

   [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/12/image.png)

  When done click on OK. 

  [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2011/12/image1.png)

  Prove a Name and Description and then click OK to save the custom view. 

  [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2011/12/image2.png)

  Then right click on the new created custom view and select Export Custom View and save the custom view XML file to CV_boot.xml. Once saved, you can delete the custom view within the Event log Viewer. 

  [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2011/12/image3.png)

  To recreate the Custom Eventlog View on the same or another system just run the following command:

  eventvwr.exe /v:CV_Boot.xml

  after a view seconds the Eventlog Viewer will open with the new custom view created. And now that we have template we can easily change this easily into a custom view for System Standby. 

  [
![image](images/image_thumb4.png)
](https://www.verboon.info/wp-content/uploads/2011/12/image4.png)

  Happy Event Viewing!

