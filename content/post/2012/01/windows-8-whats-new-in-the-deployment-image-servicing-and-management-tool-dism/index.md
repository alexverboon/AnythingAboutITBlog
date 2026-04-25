---
title: "Windows 8 &ndash; What&rsquo;s new in the Deployment Image Servicing and Management tool (DISM)"
layout: "post"
date: 01/14/2012 12:43:03
slug: "windows-8-whats-new-in-the-deployment-image-servicing-and-management-tool-dism"
aliases:
  - "/2012/01/windows-8-whats-new-in-the-deployment-image-servicing-and-management-tool-dism/"
description: "On my journey discovering the new features within Windows 8 I’ve come across a bunch of new options within the Deployment Image Servicing and Manageme..."
author: "Alex Verboon"
tags:
  - dism
  - imagex
  - mount
  - servicing
  - vhd
  - wim
  - windows-8
categories:
  - dism-2
  - windows-8
---
On my journey discovering the new features within Windows 8 I’ve come across a bunch of new options within the Deployment Image Servicing and Management Tool aka DISM. When running launching the DISM command we get an overview of all the commands and options. The **blue** coloured commands and options below are the new ones added compared to Windows 7. At first we see a whole new command group being added called “Generic Imaging Commands. While the Windows 7 DISM command is used to service the current running operating system or WIM images, in Windows 8 the DISM tool has been extended with commands to service VHD type images. 

  GENERIC IMAGING COMMANDS:

    /Get-MountedImageInfo   - Displays information about mounted WIM and VHD images.       
  /Get-ImageInfo          - Displays information about images in a WIM or VHD file.        
  /Commit-Image           - Saves changes to a mounted WIM or VHD image.        
  /Unmount-Image          - Unmounts a mounted WIM or VHD image.        
  /Mount-Image            - Mounts an image from a WIM or VHD file.        
  /Remount-Image          - Recovers an orphaned image mount directory.        
  /Cleanup-Mountpoints    - Deletes resources associated with mounted        
                            images that are corrupt.      
WIM COMMANDS:

    /List-Image             - Displays a list of the files and folders within a        
                            specified image.        
  /Delete-Image           - Deletes the specified volume image from a .wim file         
                            with multiple volume images.        
  /Split-Image            - Splits an existing .wim file into multiple read-only         
                            split .wim (SWM) files.        
  /Export-Image           - Exports a copy of the specified image to another file.        
  /Append-Image           - Adds an additional image to a .wim file.        
  /Capture-Image          - Captures an image of a drive into a new .wim file.         
                            Captured directories include all subfolders and data.        
  /Apply-Image            - Applies an image.        
  /Get-MountedWimInfo     - Displays information about mounted WIM images.      
  /Get-WimInfo            - Displays information about images in a WIM file.      
  /Commit-Wim             - Saves changes to a mounted WIM image.      
  /Unmount-Wim            - Unmounts a mounted WIM image.      
  /Mount-Wim              - Mounts an image from a WIM file.      
  /Remount-Wim            - Recovers an orphaned WIM mount directory.      
  /Cleanup-Wim            - Deletes resources associated with mounted WIM      
                            images that are corrupt.

  IMAGE SPECIFICATIONS:

    /Online                 - Targets the running operating system.     
  /Image                  - Specifies the path to the root directory of an      
                            offline Windows image.

  DISM OPTIONS:

    /English                - Displays command line output in English.     
  /Format                 - Specifies the report output format.      
  /WinDir                 - Specifies the path to the Windows directory.      
  /SysDriveDir            - Specifies the path to the system-loader file named      
                            BootMgr.      
  /LogPath                - Specifies the logfile path.      
  /LogLevel               - Specifies the output level shown in the log (1-4).      
  /NoRestart              - Suppresses automatic reboots and reboot prompts.      
  /Quiet                  - Suppresses all output except for error messages.      
  /ScratchDir             - Specifies the path to a scratch directory.

   

  Note that all of the new commands listed under “Generic Imaging commands” apply to both WIM and VHD images. In fact for WIM files you can either use the Generic command or the one listed under the WIM commands. As an example the   
 /Get-MountedImageInfo does the same as the /Get-MountedWimInfo command. 

  Under WIM Commands we see a few new commands for managing WIM files, those who have used ImageX.exe which is part of the Windows Automated Installation Kit will be familiar with these commands. Beside new top level commands and options, DISM has also been extended by various image servicing commands like for listing, removing or adding Metro Style applications  (APPX Packages) from an image but I’ll cover that one in a separate post. 

  If you’re dealing with images frequently I strongly recommend you familiarize yourself with the new options provided in DISM.

