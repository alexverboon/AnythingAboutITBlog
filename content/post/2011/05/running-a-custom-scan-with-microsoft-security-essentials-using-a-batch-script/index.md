---
title: "Running a Custom Scan with Microsoft Security Essentials using a Batch Script"
layout: "post"
date: 05/07/2011 11:51:47
slug: "running-a-custom-scan-with-microsoft-security-essentials-using-a-batch-script"
aliases:
  - "/2011/05/running-a-custom-scan-with-microsoft-security-essentials-using-a-batch-script/"
description: "Here’s a small script I just wrote to perform an antivirus scan against a specified file. @Echo off FOR /F \"Tokens=4\" %%a IN ('\"C:\Program Files\Micro..."
author: "Alex Verboon"
image: "img/post-heroes/running-a-custom-scan-with-microsoft-security-essentials-using-a-batch-script.png"
tags:
  - antivirus
  - batch
  - custom-scan
  - microsoft-security-essentials
  - mpcmdrun
  - scan
  - threat
categories:
  - antivirus
  - scripting
  - tip
---
Here’s a small script I just wrote to perform an antivirus scan against a specified file. 

  @Echo off

  FOR /F "Tokens=4" %%a IN ('"C:\Program Files\Microsoft Security Client\AntiMalWare\mpcmdrun.exe" -Scan -ScanType 3 -File C:\TEMP\test1.wim -DisableRemediation') DO SET THREAT=%%a   
Echo.    
if "%THREAT%"=="no" (    
    color 2F    
    Echo No Threats Found - All clean    
    ) ELSE (    
    color 4F    
    Echo WARNING! Virus Found    
)    
Echo.    
pause

  If all is OK you get the following result

  [
![2011-05-07 13h46_17](images/2011-05-07-13h46_17_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/05/2011-05-07-13h46_17.png)

  If a virus was found you get the following result. 

  [
![2011-05-07 13h46_47](images/2011-05-07-13h46_47_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/05/2011-05-07-13h46_47.png)

  I used a test virus file which can be found [here](http://eicar.org/anti_virus_test_file.htm)

