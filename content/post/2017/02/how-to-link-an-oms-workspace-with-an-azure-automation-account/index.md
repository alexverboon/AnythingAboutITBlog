---
title: How to link an OMS Workspace with an Azure Automation Account
layout: post
date: '2017-02-09T21:14:19Z'
slug: how-to-link-an-oms-workspace-with-an-azure-automation-account
aliases:
- /2017/02/how-to-link-an-oms-workspace-with-an-azure-automation-account/
description: When adding solutions to your OMS workspace you might get prompted to
  specify an Azure Automation account which then results in a link being created b...
author: Alex Verboon
categories:
  - 'Azure'
tags:
  - 'Automation-Account'
  - 'Link'
---
When adding solutions to your OMS workspace you might get prompted to specify an Azure Automation account which then results in a link being created between the OMS workspace and the Azure Automation account. Now let’s assume you don’t need a specific OMS solution but you still want to create a link to an Automation account. While there is an “unlink workspace” option in the Azure portal, there is no “link workspace option” . 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image.png)

 Also within the OMS portal, there no option to directly link the workspace to an automation account. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_3.png)

 And as long as there is no connection, no runbooks can be selected in the Alert configuration screen. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_4.png)

 Now here’s the trick, just start the process of adding a solution that requires an automation account. For this example I use the “Change Tracking” solution. 

  ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_5.png)

 Next select “**Configure Workspace**” 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_6.png)

 Complete the workspace configuration, **this will create the link between the OMS Workspace and the Azure Automation account**. When completed, you will see a dialog where you can add the solution. There is no need to continue or add the solution, the link is already created. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_7.png)

 and within the Azure portal, we can now select the linked workspace from the Automation account blade. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_8.png)

 and last but not least, to unlink the workspace, select the “Unlink workspace” option. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/How-to-link_12F7C/image_9.png)

 I searched, but there does not seem to be any PowerShell cmdlets around yet that would allow automate these steps.

