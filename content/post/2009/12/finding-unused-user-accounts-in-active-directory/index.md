---
title: Finding unused User Accounts in Active Directory
layout: post
date: '2009-12-10T00:05:17Z'
slug: finding-unused-user-accounts-in-active-directory
aliases:
- /2009/12/finding-unused-user-accounts-in-active-directory/
description: As we move towards the end of the year I thought it’s a good time to
  do some housekeeping activities within the lab infrastructure in which we work on...
author: Alex Verboon
tags:
- active-directory
- lastlogontimestamp
- quest
- Windows
- PowerShell
categories:
- active-directory
- automation
- tip
- Windows
- PowerShell
---
As we move towards the end of the year I thought it’s a good time to do some housekeeping activities within the lab infrastructure in which we work on a daily basis. Throughout the year we often create test user and computer objects within Active Directory and of course sometimes we forget to delete them. 

  As I don’t want to reinvent a wheel again I searched the web and soon found a whole bunch of tools and scripts that would help me identifying unused user accounts. I decided that I wanted to use a script. I first found the [Last Logon Dates scripts](http://www.rlmueller.net/Last%20Logon.htm) from Richard L. Mueller which are written in WSH. But then I found the [Managing AD User Accounts with PowerShell](http://windowsitpro.com/article/articleid/99760/managing-ad-user-accounts-with-powershell.html) article on [WindowsITPro](http://windowsitpro.com/) and decided to use the opportunity of using PowerShell to accomplish my task. 

  Unfortunately the administration console I use hasn’t been migrated to Windows 7 yet, so I installed [PowerShell 2.0](http://support.microsoft.com/kb/968929) onto that Windows Vista client and then installed the [Quest AD cmdlets](http://www.quest.com/activeroles-server/arms.aspx). 

  On [PowerShell.com](http://powershell.com/cs/forums/p/2519/3393.aspx#3393) I found the following script that I modified a bit so that the output is written into an HTML file. 

  Get-QADUser -sizeLimit 0 | where {$_.lastlogontimestamp -lt (get-date).AddDays(-30)} | Select NAme,description,lastlogontimestamp | convertto-HTML | Out-File c:\temp\adlastloggedon.htm

  I wanted to do the same to find old computers, but it appears that the Get-QADComputer cmdlet has a bug, as it doesn’t return any LastLogonTimestamp values and I found various comments that this was identified as a bug which should have been fixed by now, but either the bug is still there or I might be doing something wrong. However I found a [“find old computer objects](http://gallery.technet.microsoft.com/ScriptCenter/en-us/7bc5bc1c-e934-4ce1-8a77-3b0105807402)” script on the Microsoft TechNet Script Center Gallery it just has a bid more lines of code :-)

  Note that your Windows domain must be at Windows 2003 Domain Functional Level for updates to the *llastLogontimeStamp* to occur.

  If you are looking for a command-line tool to find Old Computers in your domain, I recommend the [OldCmp](http://www.joeware.net/freetools/tools/oldcmp/index.htm) tool from Joe.

  Related content:   
[The LastLogonTimeStamp Attribute” – “What it was designed for and how it works](http://blogs.technet.com/askds/archive/2009/04/15/the-lastlogontimestamp-attribute-what-it-was-designed-for-and-how-it-works.aspx)

