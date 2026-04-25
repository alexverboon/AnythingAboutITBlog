---
title: "Accessing the BIOS in Windows Virtual PC"
layout: "post"
date: 2009-09-23T18:05:37Z
slug: "accessing-the-bios-in-windows-virtual-pc"
aliases:
  - "/2009/09/accessing-the-bios-in-windows-virtual-pc/"
description: "When setting up a Virtual Machine in Windows Virtual PC, You will see the following progress window when the VM is started. [ ![image](images/image_th..."
author: "Alex Verboon"
image: "img/post-heroes/accessing-the-bios-in-windows-virtual-pc.png"
tags:
  - bios
  - boot
  - virtual-pc
categories:
  - bios
  - tip
  - virtualization
  - windows7
  - xp-mode
---
When setting up a Virtual Machine in Windows Virtual PC, You will see the following progress window when the VM is started. [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image1.png)This indicates that the VM is running in **Enhanced** Mode which is the default. To better understand the different modes of Windows Virtual PC I recommend reading the “[Three Modes of Windows XP Mode](http://blogs.technet.com/windows_vpc/archive/2009/08/27/three-modes-of-windows-xp-mode.aspx)” article. 

  The progress windows is being displayed until the OS running in the VM has started up, so you have no chance to interrupt the boot process to access the BIOS. To get access to the VM BIOS, you  must run the VM in **Basic** Mode. Running a VM in Basic Mode means that you must disable the integration features. 

  The Integration Features can be disabled within the Virtual Machine settings. In a running VM, select the Tools Menu, then Settings, or if you haven’t started the VM yet, select the VM in the Virtual Machine Explorer and select Settings at the right mouse click context menu. 

  [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image2.png)

   Select the Integration Features option and unselect “Enable at Startup”.

   [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image3.png) 

  The next time you start the VM, you will see the boot window instead of the progress window. 

  [
![image](images/image_thumb4.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image4.png)

   Now press the “DELETE” key during the VM boot process to get access to the VM’s BIOS settings. 

  [
![image](images/image_thumb5.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image5.png) 

  Related Content:

  [Windows Virtual PC Team Blog](http://blogs.technet.com/windows_vpc/default.aspx)

  [Virtual PC Guy’s WebLog](http://blogs.msdn.com/virtual_pc_guy/default.aspx)

