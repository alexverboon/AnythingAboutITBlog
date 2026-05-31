---
title: "How to use Group Policy to configure default Library definition files in Windows 8"
layout: "post"
date: 2012-06-10T14:52:23Z
slug: "how-to-use-group-policy-to-configure-default-library-definition-files-in-windows-8"
aliases:
  - "/2012/06/how-to-use-group-policy-to-configure-default-library-definition-files-in-windows-8/"
description: "There is a new Group Policy setting for Windows 8 and Server 2012 called “**Location where all default Library definition files for users/machines res..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Group Policy'
  - 'Library'
---
There is a new Group Policy setting for Windows 8 and Server 2012 called “**Location where all default Library definition files for users/machines reside**”. The policy can be found under Computer or User Configuration / Administrative Templates / Windows Components / Windows Explorer.

  *If you enable this policy setting, administrators can specify a path where all default Library definition files for users reside. The user will not be allowed to make changes to these Libraries from the UI. On every logon, the policy settings are verified and Libraries for the user are updated or changed according to the path defined.*

  So assume your Marketing department has created a new set of document templates and wants you to make these easily accessible to all users by adding a Library in Windows Explorer that points directly to the central company template location.

     
- Open Windows Explorer and create a new Library      
![1image_thumb2](https://www.verboon.info/wp-content/uploads/2012/10/1image_thumb2.png)       
    
- Now Navigate to C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Libraries and there copy the new created Library file to a central location accessible by all users. Since I write this blog post on a disconnected client, I store the file locally under C:\LibTemplates.      
    
- Open the Group Policy Management Console or local Group Policy console and enable the Policy setting **Location where all default Library definition files for users/machines reside        
        
![2image_thumb3](https://www.verboon.info/wp-content/uploads/2012/10/2image_thumb3.png)         
**    
- Logon with with another domain or local user and then open Windows Explorer and notice the new added Library.      
![3image_thumb4](https://www.verboon.info/wp-content/uploads/2012/10/3image_thumb4.png)

