---
title: "Creating GPO reports"
layout: "post"
date: 2008-11-13T22:00:05Z
slug: "creating-gpo-reports"
aliases:
  - "/2008/11/creating-gpo-reports/"
description: "Creating GPO Reports"
author: "Alex Verboon"
tags:
  - gpo
  - group-policy
  - scripting
categories:
  - GroupPolicy
---
Usually when you need a report for a given Group Policy object, you would launch the Group Policy Management Console, select the GPO and then select the settings tab that produces the report.

But what if you need a report for multiple or even all your GPOs you have within your Active Directory ? Going through each GPO and produce the report manually is going to take ages and is boring.

My colleague Rudi recently found a script that automatically creates GPO reports it finds within your AD. You can select them individually or simply report on all.

The script is stored on the [Win32 Scripting site](http://cwashington.netreach.net/) which is a usefull resource for admin scripts since many years. The GPO reporting script can be found [here](http://cwashington.netreach.net/depo/view.asp?Index=1117)

