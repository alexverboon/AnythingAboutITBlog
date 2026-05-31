---
title: "Scheduled Tasks for Windows Games"
layout: "post"
date: 2011-04-22T14:05:55Z
slug: "scheduled-tasks-for-windows-games"
aliases:
  - "/2011/04/scheduled-tasks-for-windows-games/"
description: "When opening the Windows Task Scheduler you might see a Task called “UpdateCheck_” located within the Games folder of the Task Scheduler Library. [ ![..."
author: "Alex Verboon"
image: "img/post-heroes/scheduled-tasks-for-windows-games.png"
categories:
  - 'Windows'
tags:
  - 'Scheduled-Task'
  - 'Games'
---
When opening the Windows Task Scheduler you might see a Task called “UpdateCheck_” located within the Games folder of the Task Scheduler Library. 

  ![2011-04-22 15h42_08](images/2011-04-22-15h42_08_thumb.png)

  To enable or disable this Task open the “Game Explorer” within Windows and then select options. 

  ![2011-04-22 15h48_49](images/2011-04-22-15h48_49_thumb.png)

  ![2011-04-22 15h52_04](images/2011-04-22-15h52_04_thumb.png)

  When selecting “Automatically check online for updates and news, then notify me when the’re available” a scheduled Task is automatically being created. When selecting “Never check online for updates or news, I’ll do it manually” the task if existed before is removed. 

  Note that this is a per user setting, so if multiple users on one system enable this setting, a separate task is created for each user. The task names contain the users SID. 

  ![2011-04-22 15h59_56](images/2011-04-22-15h59_56_thumb.png)

