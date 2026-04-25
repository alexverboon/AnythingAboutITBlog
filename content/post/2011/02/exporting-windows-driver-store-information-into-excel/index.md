---
title: Exporting Windows Driver Store Information into Excel
layout: post
date: '2011-02-02T21:16:51Z'
slug: exporting-windows-driver-store-information-into-excel
aliases:
- /2011/02/exporting-windows-driver-store-information-into-excel/
description: To obtain detailed information about a particular driver that is prestaged
  within the Windows 7 driver store, you can run the following command. `Dism...
author: Alex Verboon
tags:
- dism
- driver
- driver-store
- excel
- export
- Windows
- PowerShell
categories:
- driver-store
- excel
- Windows
- PowerShell
---
To obtain detailed information about a particular driver that is prestaged within the Windows 7 driver store, you can run the following command.

`Dism /online /get-driverinfo /driver: <path to driver inf file>`

Now there is quite a lot of interesting information in here, imagine you are working on a Windows 7 project and you want to know if a particular device is supported by the Windows 7 build in drivers. Of course you can do a bulk export of all the drivers into text files (as explained in this [earlier post](https://www.verboon.info/index.php/2010/12/inside-the-windows-7-driver-store/)) but wouldn’t it be nice if we could just have all the information consolidated in one Excel file or database?

I have spend quite some time to extract the data from the individual files using plain vbscript and powershell, but didn’t succeed because of the structure of the output, so I got a bit of help from my friend Claude Henchoz who provided a python script that does the final magic. So here we go.

First [download](http://www.python.org/ftp/python/2.7.1/python-2.7.1.msi) and install the Python scripting engine (just use the default installation options)

Then create a Folder C:\DATA\DRVSTORE and C:\DATA\DRVSTORE\ALL (or modify the paths in the below script)

Then copy paste the below code into a batch file called drvstore_collect_data.cmd and store it in C:\DATA\DRVSTORE

[sourcecode language="plain"]
@echo off
FOR /R C:\WINDOWS\SYSTEM32\DRIVERSTORE\FILEREPOSITORY %%i IN (*.INF) DO CALL :Subroutine %%i

:Subroutine
set filename=%~n1
echo %filename%
echo %~1
dism /online /get-driverinfo /driver:%~1  | dism2csv.py  >c:\data\drvstore\all\%~n1.txt"
[/sourcecode]

Then copy paste the code below and store it in a file called dism2csv.py and store the file in C:\DATA\DRVSTORE

[sourcecode language="py"]

import re
import sys

# Read from stdin
matchstr = sys.stdin.read()

# Process regular expression for header data
file_regex = r"""Published.Name.:.(.*)\n.*\nClass.Name.:.(.*)\nClass.Description.:.(.*)\n"""
compile_obj = re.compile(file_regex,  re.IGNORECASE| re.MULTILINE| re.VERBOSE)
file_info = compile_obj.findall(matchstr)

# Process regular expression for records
records_regex = r"""\n\s\s\s\s\w*.:.(.*)\n\s*\w*.:.(.*)\n\s*\w*.:.(.*)\n\s*\w*.\w*.:.(.*)\n\s*\w*.\w*.:.(.*)\n\s*\w*.\w*.:.(.*)\n\s*\w*.\w*.:.(.*)"""
compile_obj = re.compile(records_regex,  re.IGNORECASE| re.MULTILINE| re.VERBOSE)
records = compile_obj.findall(matchstr)

# Rearrange header and record list into regular strings, separated with tabs
for record in records:
print "\t".join(file_info[0]) + "\t" + "\t".join(record)
[/sourcecode]

Now launch the batch file and wait until it completes, you should then have the \All subfolder filled with files, the script creates a tab delimited text file for each driver within the driver store.

Finally within the \All folder run the following command to consolidate all the text files into one file.

[sourcecode language="plain"]
TYPE *.TXT >alldrivers.tab
[/sourcecode]

You can now import the file in Excel.

