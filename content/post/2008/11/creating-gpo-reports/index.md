---
title: "Creating GPO reports"
layout: "post"
date: 11/13/2008 22:00:05
slug: "creating-gpo-reports"
aliases:
  - "/2008/11/creating-gpo-reports/"
description: "Usually when you need a report for a given Group Policy object, you would launch the Group Policy Management Console, select the GPO and then select t..."
author: "Alex Verboon"
tags:
  - gpo
  - group-policy
  - scripting
categories:
  - automation
  - group-policy
  - scripting
  - tip
  - tools
---
Usually when you need a report for a given Group Policy object, you would launch the Group Policy Management Console, select the GPO and then select the settings tab that produces the report.

But what if you need a report for multiple or even all your GPOs you have within your Active Directory ? Going through each GPO and produce the report manually is going to take ages and is boring.

My colleague Rudi recently found a script that automatically creates GPO reports it finds within your AD. You can select them individually or simply report on all.

The script is stored on the [Win32 Scripting site](http://cwashington.netreach.net/) which is a usefull resource for admin scripts since many years. The GPO reporting script can be found [here](http://cwashington.netreach.net/depo/view.asp?Index=1117)

