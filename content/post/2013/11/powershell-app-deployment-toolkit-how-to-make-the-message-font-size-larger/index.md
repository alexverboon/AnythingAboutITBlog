---
title: "PowerShell App Deployment Toolkit&ndash; How to make the message  Font size larger"
layout: "post"
date: 2013-11-22T14:32:33Z
slug: "powershell-app-deployment-toolkit-how-to-make-the-message-font-size-larger"
aliases:
  - "/2013/11/powershell-app-deployment-toolkit-how-to-make-the-message-font-size-larger/"
description: "I have had a request this week to make the font size of the Message text displayed by the PowerShell App Deployment Tookit function **Show-Installatio..."
author: "Alex Verboon"
image: "img/post-heroes/powershell-app-deployment-toolkit-how-to-make-the-message-font-size-larger.png"
tags:
  - app-deployment-toolkit
  - fontsize
  - message
  - powershell
categories:
  - PowerShell
---
I have had a request this week to make the font size of the Message text displayed by the PowerShell App Deployment Tookit function **Show-InstallationPrompt **a bit larger. 

 [
![SNAGHTML173a21f](images/SNAGHTML173a21f_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/11/SNAGHTML173a21f.png)

 To make the font of the message larger, all you need to do is adding 2 lines of code to the **Function** 
**Show-InstallationPrompt** that is embedded within the **AppDeployToolkitMain.ps1** file. 

 Add the following code just above the “#button left” section. 

 #custom - Bigger text size
$Font = New-Object System.Drawing.Font("Arial",14,[System.Drawing.FontStyle]::Regular)
$labelText.Font = $Font
#custom - Bigger Text Size

 [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2013/11/image2.png)

 As you can see, now the text size of the message has increased. 

 [
![SNAGHTML17b9fcf](images/SNAGHTML17b9fcf_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/11/SNAGHTML17b9fcf.png)

