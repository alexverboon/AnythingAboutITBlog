---
title: "Windows 8 - File History Feature replaces &ldquo;Previous Versions&rdquo; and Backup and Restore"
layout: "post"
date: 2012-04-29T15:36:33Z
slug: "windows-8-file-history-feature-replaces-previous-versions-and-backup-and-restore"
aliases:
  - "/2012/04/windows-8-file-history-feature-replaces-previous-versions-and-backup-and-restore/"
description: "While reading the [Windows 8 Consumer Preview and Windows Server “8” Beta Compatibility Cookbook](http://msdn.microsoft.com/en-us/library/hh848074(v=v..."
author: "Alex Verboon"
tags:
  - backup-and-restore
  - feature
  - file-history
  - previous-versions
  - restore
  - Windows
  - WinPE
categories:
  - file-history
  - Windows
  - WinPE
---
While reading the [Windows 8 Consumer Preview and Windows Server “8” Beta Compatibility Cookbook](http://msdn.microsoft.com/en-us/library/hh848074(v=vs.85).aspx) I came across the topic [Volume Shadow Copy Service UI Removed](http://msdn.microsoft.com/en-us/library/hh848072(v=vs.85).aspx). Due to the fact that this feature was obviously rarely used by end users and it’s negative impact on Windows performance, Microsoft decided to removed this feature from Windows 8. In addition Microsoft also decided to [deprecate the Windows 7 Backup and Restore](http://msdn.microsoft.com/en-us/library/hh848073(v=vs.85).aspx) feature, again because this functionality appears to be rarely used. 

  On Windows 7 client the “Previous Versions” feature is configured through the System Protection Settings as shown in the screenshot below. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image19.png)

  Users can access the previous versions through the Folder or File properties tab. 

  
![Picture of the Previous Versions tab](http://res1.windows.microsoft.com/resbox/en/Windows Vista/main/1febb176-70a8-4ea2-b8f4-3cf1d98fa8e8_14.png)

  As shown in the screen shot below the option for configuring System Protection - Previous files has been removed and so has the “Previous Versions” tab within the Folder & Files properties.

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image20.png)

  Windows7 Backup and Restore is still available in Windows 8 but is well hidden within the system, in order to access the feature you must search for “file recovery” or “recovery”. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image21.png)

  In Windows 8 Microsoft is trying to simplify the creation of user data backups and restore through a new feature called “File History”. File History allows users to backup their data to removable storage such as a USB drive or a network share. 

  For a general overview of what File History is about I recommend reading Paul Thurrott’s article [Windows 8 Feature Focus: File History](http://www.winsupersite.com/article/windows8/windows-8-feature-focus-file-history-142602) and Dr. Z’s blog posts [Windows 8 How To: 27. Backup your Files Using File History](http://blogs.msdn.com/b/zxue/archive/2012/03/09/windows-8-how-to-27-backup-your-documents-and-files.aspx) and [Windows 8 How To: 28. Restore Files Using File History](http://blogs.msdn.com/b/zxue/archive/2012/03/09/windows-8-how-to-28-restore-files-using-file-history.aspx)

  As an IT Pro I am of course interested in how things work, so I’ve started looking at how this all runs and is configured. 

  **The File History Service** - By default the File History Service is configured to start manually, but once a first user enables File History, the Service startup changes to Automatic (Delayed). Windows 8 is intelligent enough to identify multiple users that have File History enabled, so even if a user disables the feature at a later time, the Service remains configured to Start until no user has file history enabled and then sets the service back to start manually. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image22.png)

  **File History Configuration** - File History Service configuration is stored within the Windows Registry under:

  HKLM\SYSTEM\CurrentControllSet\Services\fhsvc

  For each user that enables File History a key (pointer) to the user specific File History configuration settings is created under:

  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\fhsvc\Parameters\Configs

  For this example the key is:

  C:\Users\Admin\AppData\Local\Microsoft\Windows\FileHistory\Configuration\Config

  Then there are 2 files called config1.xml and config2.xml, both files appear to be identical and I haven’t figured out yet why there’s two. The config file holds the configuration settings for the File History Service. 

  <?xml version="1.0" encoding="UTF-8"?>     
<DataProtectionUserConfig SchemaVersion="1">      
  <UserName>Admin</UserName>      
  <FriendlyName>Admin</FriendlyName>      
  <PCName>AV-WIN8-004</PCName>      
  <UserId>6f5671be-a258-45cc-9a08-377ef1c943fb</UserId>      
  <Library>      
    <LibraryName>*7b0db17d-9cd2-4a93-9733-46cc89022e7c</LibraryName>      
    <Folder>C:\Users\Admin\Documents</Folder>      
    <Folder>C:\Users\Public\Documents</Folder>      
  </Library>      
  <Library>      
    <LibraryName>*2112ab0a-c86a-4ffe-a368-0de96e47012e</LibraryName>      
    <Folder>C:\Users\Admin\Music</Folder>      
    <Folder>C:\Users\Public\Music</Folder>      
  </Library>      
  <Library>      
    <LibraryName>*a990ae9f-a03b-4e80-94bc-9912d7504104</LibraryName>      
    <Folder>C:\Users\Admin\Pictures</Folder>      
    <Folder>C:\Users\Public\Pictures</Folder>      
  </Library>      
  <Library>      
    <LibraryName>*491e922f-5643-4af4-a7eb-4e7a138d8174</LibraryName>      
    <Folder>C:\Users\Admin\Videos</Folder>      
    <Folder>C:\Users\Public\Videos</Folder>      
  </Library>      
  <UserFolder>C:\Users\Admin\Contacts</UserFolder>      
  <UserFolder>C:\Users\Admin\Desktop</UserFolder>      
  <UserFolder>C:\Users\Admin\Favorites</UserFolder>      
  <LocalCatalogPath1>C:\Users\Admin\AppData\Local\Microsoft\Windows\FileHistory\Configuration\Catalog1.edb</LocalCatalogPath1>      
  <LocalCatalogPath2>C:\Users\Admin\AppData\Local\Microsoft\Windows\FileHistory\Configuration\Catalog2.edb</LocalCatalogPath2>      
  <StagingArea>      
    <StagingAreaPath>C:\Users\Admin\AppData\Local\Microsoft\Windows\FileHistory\Data</StagingAreaPath>      
    <StagingAreaMaximumCapacity>24986936729</StagingAreaMaximumCapacity>      
    <StagingAreaWarningThreshold>18740202546</StagingAreaWarningThreshold>      
  </StagingArea>      
  <AvailabilityPolicies>      
    <TargetAbsenceTime>5</TargetAbsenceTime>      
    <TimeInUnprotectedState>3</TimeInUnprotectedState>      
  </AvailabilityPolicies>      
  <RetentionPolicies>      
    <RetentionPolicyType>DISABLED</RetentionPolicyType>      
    <MinimumRetentionAge>365</MinimumRetentionAge>      
  </RetentionPolicies>      
  <DPFrequency>3600</DPFrequency>      
  <DPStatus>ENABLED</DPStatus>      
  <Target>      
    <TargetName>\\labhome099\data\FileHistoryBackup</TargetName>      
    <TargetUrl>\\labhome099\data\FileHistoryBackup\</TargetUrl>      
    <TargetDriveType>REMOTE</TargetDriveType>      
    <TargetConfigPath1>Admin\AV-WIN8-004\Configuration\Config1.xml</TargetConfigPath1>      
    <TargetConfigPath2>Admin\AV-WIN8-004\Configuration\Config2.xml</TargetConfigPath2>      
    <TargetCatalogPath1>Admin\AV-WIN8-004\Configuration\Catalog1.edb</TargetCatalogPath1>      
    <TargetCatalogPath2>Admin\AV-WIN8-004\Configuration\Catalog2.edb</TargetCatalogPath2>      
    <TargetBackupStorePath>Admin\AV-WIN8-004\Data</TargetBackupStorePath>      
    <TargetWarningThreshold>98</TargetWarningThreshold>      
  </Target>      
</DataProtectionUserConfig>

  **File History Data** - The data that is being backed up is stored within the specified location e.g the Removable drive or network location. If a user has setup File History on multiple clients, then a subfolder is created per computer. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image23.png)

  Each time the File History Service starts a copy of each file version is stored within the defined backup location. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image24.png)

  **File History - Scheduled Task** - In addition to the File History Service that executes a backup based on the defined backup interval, there’s also a Scheduled Task for File History. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image25.png)

  When looking at the scheduled Task, you might notice that no “Next Run Time” is defined, this is because the File History Task is part of the Windows maintenance task e.g. the Task is executed when the Windows maintenance Task starts. 

  **File History Event logs** - For File History there are also a number of event logs. When enabling “Show Analytic and Debug logs” within the Event Viewer the following File History related event logs are displayed. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image26.png)

  **File History Group Policy Configuration** - Configuration of the File History through group policy is limited At present enterprise administrators can only prevent users from enabling File History. The setting can be found under: Computer Configuration \ Administrative Templates \ Windows Components \ File History. 

  ![image](https://www.verboon.info/wp-content/uploads/2012/04/image27.png)

