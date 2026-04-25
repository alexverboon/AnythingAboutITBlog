---
title: "ToolTip: DirCreator"
layout: "post"
date: 2012-11-12T21:29:04Z
slug: "tooltip-dircreator"
aliases:
  - "/2012/11/tooltip-dircreator/"
description: "Are you an Administrator tired of manually creating folder structures for new projects? Then DirCreator is just what you need. DirCreator is an enterp..."
author: "Alex Verboon"
image: "img/post-heroes/tooltip-dircreator.png"
tags:
  - acl
  - active-directory
  - automate
  - dircreator
  - directory
  - folders
  - group-membership
  - project-folders
  - Windows
categories:
  - automation
  - tools
---
Are you an Administrator tired of manually creating folder structures for new projects? Then DirCreator is just what you need. DirCreator is an enterprise-proven tool to automatically generate structured, template-based directory structures, along with groups, members and ACLs.

  You can either create a template from scratch or create a template based on an existing folder structure. For this demonstration I first create a template folder structure on my home lab data share. 

  \\server01\data\Projects

  [
![clip_image002](images/clip_image002_thumb1.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image0021.jpg)

  I also modify the folders permissions

  [
![clip_image004](images/clip_image004_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image004.jpg)

  Next I run DirCreator with the following command line:

  C:\data\dircreator>DirCreator.exe ReadAcls -d \\server01\data\Projects -r true - x c:\data\template.xml

  This generates the template file template.xml

  As a next step, I’ll replace the folder name “Template” 

  [
![clip_image006](images/clip_image006_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image006.jpg)

  With $!{DirectoryName}

  [
![clip_image008](images/clip_image008_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image008.jpg)

  And then save the template.xml. To create a new Project folder called FooProject1 that contains all predefined sub folders, group members and ACL’s, I run the following command:

  C:\data\dircreator>DirCreator.exe -t c:\data\template.xml -n "**DirectoryName**=**FooProject1**"

  And see, a new Project folder is created, containing all predefined subfolders and folder permissions. 

  [
![clip_image010](images/clip_image010_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image010.jpg)

  [
![clip_image012](images/clip_image012_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image012.jpg)

  [
![clip_image014](images/clip_image014_thumb.jpg)
](https://www.verboon.info/wp-content/uploads/2012/11/clip_image014.jpg)

  In this example I only used static AD group names, but if you have a little bit of time, you can customize DirCreator to automatically create project specific groups for you. 

  DirCreator can be used as a standalone command line tool or as a Windows Service where it will automatically process *.job.xml files once stored in the defined directory. 

  More information about DirCreator and download links can be found [here](http://dircreator.codeplex.com/)

