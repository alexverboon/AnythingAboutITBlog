---
title: "The GatherNetworkinfo.vbs Script"
layout: "post"
date: 2011-06-20T20:17:37Z
slug: "the-gathernetworkinfo-vbs-script"
aliases:
  - "/2011/06/the-gathernetworkinfo-vbs-script/"
description: "I recently read the whitepaper“[Using Windows Script Host and COM to Hack Windows](http://www.sans.org/reading_room/whitepapers/hackers/windows-script..."
author: "Alex Verboon"
image: "img/post-heroes/the-gathernetworkinfo-vbs-script.png"
tags:
  - collect
  - data
  - gather
  - gathernetworkinfo-vbs
  - script
  - system-information
  - windows-7
  - wsh
categories:
  - network
  - tcpip
  - windows-7
---
I recently read the whitepaper“[Using Windows Script Host and COM to Hack Windows](http://www.sans.org/reading_room/whitepapers/hackers/windows-script-host-hack-windows_33583)” that is mentioning the GatherNetworkinfo.vbs script I hadn’t paid attention to yet. The gathernetworkinfo.vbs script comes by default with every Windows 7 installation and is located within the C:\Windows\System32\ folder. 

  The script does collect various networking information about the Windows 7 system and its configuration and dumps the information into the C:\Windows\System32\Config folder. 

  On a system where the script hasn’t been executed yet the Config folder looks as following:

  [
![2011-06-20 21h42_17](images/2011-06-20-21h42_17_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/06/2011-06-20-21h42_17.png)

  Now open a command prompt with elevated rights and run cscript c:\windows\system32\gathernetworkinfo.vbs When the script has completed you will see that additional files have been added to the Config folder. 

  [
![2011-06-20 21h47_28](images/2011-06-20-21h47_28_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/06/2011-06-20-21h47_28.png)

  The structure of the script is quite easy to understand. Within the first part of the script all functions are defined, the second part defines the output file names and the last part actually calls the individual data collection functions including the output file parameter. 

  The script is also defined within a scheduled task called Nettrace which is not scheduled to run automatically. 

  [
![2011-06-20 21h57_23](images/2011-06-20-21h57_23_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/06/2011-06-20-21h57_23.png)

