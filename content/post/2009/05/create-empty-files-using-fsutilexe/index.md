---
title: "Create empty files using fsutil.exe"
layout: "post"
date: 2009-05-25T18:46:55Z
slug: "create-empty-files-using-fsutilexe"
aliases:
  - "/2009/05/create-empty-files-using-fsutilexe/"
description: "I am currently busy with testing BranchCache in a real world environment. I will share more about these tests in another post. Testing BranchCache doe..."
author: "Alex Verboon"
categories:
  - 'Tips-Tools'
tags:
  - 'Empty-Files'
  - 'Large-Files'
---
I am currently busy with testing BranchCache in a real world environment. I will share more about these tests in another post. Testing BranchCache does mainly consist of copying files over the WAN and monitor how the client cache is being populated and how other clients, that copy the same content from the remote BranchCache enabled server, utilize the distributed cache located on peer clients that reside within the same LAN segment.

  Before testing the BranchCache feature with real content, I just wanted to create some large files with different file sizes  on the BranchCache enabled Server.

  I’ve seen some freeware utilities in the past that allow the creation of large files, but it can also be done with the out of the box provided toolset from Microsoft. FSUTIL.EXE allows you to create large files on the from the command prompt.

              **File size**        **Command**                  10 MB        fsutil file createnew largefile10mb.lf 10000000                  100 MB        fsutil file createnew largefile10mb.lf 100000000                  1 GB        fsutil file createnew largefile10mb.lf 1000000000                  10 GB        fsutil file createnew largefile10mb.lf 10000000000

  For more information about fsutil go to: [http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/fsutil.mspx?mfr=true](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/fsutil.mspx?mfr=true)


