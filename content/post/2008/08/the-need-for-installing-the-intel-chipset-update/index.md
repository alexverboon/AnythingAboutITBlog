---
title: "The need for installing the Intel Chipset update"
layout: "post"
date: 08/21/2008 21:56:10
slug: "the-need-for-installing-the-intel-chipset-update"
aliases:
  - "/2008/08/the-need-for-installing-the-intel-chipset-update/"
description: "Within one of the projects I'm working on, there was a debate about installing the Intel Chipset software. It was requested not to install it. I could..."
author: "Alex Verboon"
tags:
  - chipset
  - drivers
categories:
  - deployment
  - drivers
---
Within one of the projects I'm working on, there was a debate about installing the Intel Chipset software. It was requested not to install it. I could not agree with that, as it is a common known best practice to install the Intel Chipset update software unless the operating system can configure the Intel chipset natively.

A detailed table about when the Intel chipset software installation is needed can be found here:

[http://www.intel.com/support/chipsets/inf/sb/CS-009270.htm](http://www.intel.com/support/chipsets/inf/sb/CS-009270.htm)

So what does it do ?

*The Intel Chipset Software Installation Utility files inform the operating system how to properly configure the chipset for specific functionality, such as AGP, USB, Core PCI and ISA PnP services. In order to be able to install any chipset-related drivers (e.g. graphics, IDE, etc.), your operating system must first be able to recognize your chipset.*

More on Intel's page: [http://www.intel.com/support/chipsets/inf/index.htm](http://www.intel.com/support/chipsets/inf/index.htm)

