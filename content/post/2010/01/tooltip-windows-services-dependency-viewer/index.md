---
title: "ToolTip: Windows Services Dependency Viewer"
layout: "post"
date: 2010-01-01T21:56:42Z
slug: "tooltip-windows-services-dependency-viewer"
aliases:
  - "/2010/01/tooltip-windows-services-dependency-viewer/"
description: "During my periodic visit on CodePlex I came across the Windows Services Dependency Viewer utility. The tool provides access to the following informati..."
author: "Alex Verboon"
image: "img/post-heroes/tooltip-windows-services-dependency-viewer.png"
tags:
  - dependency
  - process
  - services
  - viewer
  - windows
  - wmi
categories:
  - tip
  - tools
---
During my periodic visit on CodePlex I came across the Windows Services Dependency Viewer utility. The tool provides access to the following information:

     
- Windows service dependent and antecedent services    
- Services grouped by process    
- Service details (from Win32_Service WMI class)    
- Service process details (from Win32_Process WMI class 

  This tool might come in handy once you start changing a specific Service’s startup mode. 

  [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/01/image.png)

  The Windows Services Dependency Viewer can be downloaded from [here](http://svcdependencyviewer.codeplex.com/) Additional documentation can be found [here](http://svcdependencyviewer.codeplex.com/documentation)

  **Related Posts**    
[Windows Services, what changed from Vista to Windows7 Part1](https://www.verboon.info/index.php/2009/04/windows-services-what-changed-from-vista-to-windows7-part1/)    
[Windows Services, What changed from Vista to Windows7 – Part2](https://www.verboon.info/index.php/2009/04/windows-services-what-changed-from-vista-to-windows7-part2/)

