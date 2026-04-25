---
title: "New Defrag options in Windows 8"
layout: "post"
date: 2011-11-13T16:53:46Z
slug: "new-defrag-options-in-windows-8"
aliases:
  - "/2011/11/new-defrag-options-in-windows-8/"
description: "Looks like Windows 8 introduces some additional DEFRAG options. **Option** **Description** **Option Available** **Windows 7** **Windows 8** /A Perform..."
author: "Alex Verboon"
tags:
  - defrag
  - optimization
  - windows-8
categories:
  - defrag
  - windows-8
---
Looks like Windows 8 introduces some additional DEFRAG options. 

              **Option**        **Description**        **Option Available**                  **Windows 7**        **Windows 8**                  /A        Perform analysis on the specified volumes        Yes        Yes                  /C        Perform the operation on all volumes        Yes        Yes                  **/D**        **Perform traditional defrag (this is the default)**        No        **Yes**                  /E        Perform the operation on all volumes except those specified        Yes        Yes                  /H        Run the operation at normal priority (default is low)        Yes        Yes                  **/K**        **Perform slab consolidation on the specified volumes**        No        **Yes**                  **/L**        **Perform retrim on the specified volumes**        No        **Yes**                  /M        Run the operation on each volume in parallel in the background        Yes        Yes                  **/O**        **Perform the proper optimization for each media type**        No        **Yes**                  /T        Track an operation already in progress on the specified volume        Yes        Yes                  /U        Print the progress of the operation on the screen        Yes        Yes                  /V        Print verbose output containing the fragmentation statistics        Yes        Yes                  /X        Perform free space consolidation on the specified volumes        Yes        Yes           

  There is little information yet about these options but I assume that they might have to do with the rumored new “protogon” file system and that there is more support for SSD included.

