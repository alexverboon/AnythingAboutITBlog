---
title: "Running within an SCCM 2007 Tasksequence or not?"
layout: "post"
date: 2011-12-22T19:18:52Z
slug: "running-within-an-sccm-2007-tasksequence-or-not"
aliases:
  - "/2011/12/running-within-an-sccm-2007-tasksequence-or-not/"
description: "I’ve been working on a batch script that runs as part of an SCCM 2007 TaskSequence or simply as a regular program. Because there were different condit..."
author: "Alex Verboon"
categories:
  - 'PowerShell'
tags:
  - 'Sccm-2007'
  - 'Tasksequence'
---
I’ve been working on a batch script that runs as part of an SCCM 2007 TaskSequence or simply as a regular program. Because there were different conditions whether I run the script as part of a TaskSequence or just as a program and did not want to create two separate scripts I needed a way to detect within what environment the script is running.

  I was first thinking of looking for the existence of any [_SMSxyz Task Sequence variables](http://technet.microsoft.com/en-us/library/bb632442.aspx) as they don’t exist when running a script within an advertised program, but that would have required some extra code I wanted to avoid. So I ended up with the code below.

  SET IsSMSTask="%~dp0"
echo %IsSMSTask% | find "TaskSequence"
if errorlevel 1 (
    ECHO Running as an advertised Program
        ) ELSE (
    ECHO Running in a SCCM Task Sequence
)

  So what does the script actually do? Well when you run a TaskSequence from SCCM 2007 the sources are stored within a root folder called *_SMSTaskSequence* and underneath that folder it stores the packages and other files that are used to execute the TaskSequence whereas if you just run a script as an advertised program, SCCM will either use the sources stored on the SCCM Distribution point package folder or in case the content was first downloaded to the client from the SCCM Client Cache folder.

  To figure out from where the script is run, we’ll use the %~dp0 variable that returns the directory path of the executing script and then we’re searching for the string *TaskSequence* within that path string. If the string “TaskSequence was found we can be sure that the script was executed from a TaskSequence.

  If you have another way to determine whether a script is executed from an SCCM 2007 TaskSequence let me know.


