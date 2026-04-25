---
title: "The Machine SID Duplication Myth"
layout: "post"
date: 2009-11-04T14:14:31Z
slug: "the-machine-sid-duplication-myth"
aliases:
  - "/2009/11/the-machine-sid-duplication-myth/"
description: "Mark Russinovich explains why he’s retiring “NewSID”. In short, he explains that he heard that people were having some issues with it on Vista, which ..."
author: "Alex Verboon"
tags:
  - sid
  - newsid
  - sysprep
categories:
  - deployment
  - tools
---
Mark Russinovich explains why he’s retiring “NewSID”. In short, he explains that he heard that people were having some issues with it on Vista, which made him do some research on whether SID changing is still necessary... Turns out he couldn’t find anyone in Microsoft who could tell him why duplicate SIDs could be a problem. Because it’s not a problem. And: It never was. Anyway for people that did OS deployment the correct way, this tool wasn’t needed, as the proper way is to use sysprep. 

  Read the entire article [here](http://blogs.technet.com/markrussinovich/archive/2009/11/03/3291024.aspx)

  Thanks to **Claude** for the pointer.

