---
title: "New IE Group Policy Settings for blocking out-of-date ActiveX controls"
layout: "post"
date: 2014-08-10T20:26:04Z
slug: "new-ie-group-policy-settings-for-blocking-out-of-date-activex-controls"
aliases:
  - "/2014/08/new-ie-group-policy-settings-for-blocking-out-of-date-activex-controls/"
description: "As [anounced](http://blogs.msdn.com/b/ie/archive/2014/08/06/internet-explorer-begins-blocking-out-of-date-activex-controls.aspx) by Microsoft last wee..."
author: "Alex Verboon"
categories:
  - 'Windows'
tags:
  - 'Activex'
  - 'Group Policy'
---
As [anounced](http://blogs.msdn.com/b/ie/archive/2014/08/06/internet-explorer-begins-blocking-out-of-date-activex-controls.aspx) by Microsoft last week on their IEBlog Internet Explorer will start blocking out of date ActiveX controls For managed environments there are updated [administrative templates](http://www.microsoft.com/en-us/download/details.aspx?id=40905) for Internet Explorer to control the behaviour of the ActiveX blocking feature.

 Although the link brings you to a site called “Administrative Templates for Internet Explorer 11” the settings are set to work for Internet Explorer 8,9, 10 and 11. If you haven’t updated your administrative templates since a while, beware of the [missing IE maintenance settings](http://msdn.microsoft.com/en-us/library/dn338129.aspx).

 The new settings are located under Computer Configuration or User Configuration | Administrative Templates | Windows Components | Internet Explorer | Security Features | Add-In Management

     **Setting**

  **Description**

   **Turn on ActiveX control logging in Internet Explorer**

  This policy setting determines whether Internet Explorer saves log information for ActiveX controls.

 If you enable this policy setting, Internet Explorer logs ActiveX control information (including the source URI that loaded the control and whether it was blocked) to a local file.

 If you disable or don't configure this policy setting, Internet Explorer won't log ActiveX control information.

 Note that you can turn this policy setting on or off regardless of the "Turn off blocking of outdated ActiveX controls for Internet Explorer" or "Turn off blocking of outdated ActiveX controls for Internet Explorer on specific domains" policy settings.

 For more information, see "Outdated ActiveX Controls" in the Internet Explorer TechNet library.

   **Remove "Run this time" button for outdated ActiveX controls in Internet Explorer**

  This policy setting allows you to stop users from seeing the "Run this time" button and from running specific outdated ActiveX controls in Internet Explorer.

 If you enable this policy setting, users won't see the "Run this time" button on the warning message that appears when Internet Explorer blocks an outdated ActiveX control.

 If you disable or don't configure this policy setting, users will see the "Run this time" button on the warning message that appears when Internet Explorer blocks an outdated ActiveX control. Clicking this button lets the user run the outdated ActiveX control once.

 For more information, see "Outdated ActiveX Controls" in the Internet Explorer TechNet library.

   **Turn off blocking of outdated ActiveX controls for Internet Explorer**

  This policy setting determines whether Internet Explorer blocks specific outdated ActiveX controls. Outdated ActiveX controls are never blocked in the Intranet Zone.

 If you enable this policy setting, Internet Explorer stops blocking outdated ActiveX controls.

 If you disable or don't configure this policy setting, Internet Explorer continues to block specific outdated ActiveX controls.

 For more information, see "Outdated ActiveX Controls" in the Internet Explorer TechNet library.

   **Turn off blocking of outdated ActiveX controls for Internet Explorer on specific domains**

  This policy setting allows you to manage a list of domains on which Internet Explorer will stop blocking outdated ActiveX controls. Outdated ActiveX controls are never blocked in the Intranet Zone.

 If you enable this policy setting, you can enter a custom list of domains for which outdated ActiveX controls won't be blocked in Internet Explorer. Each domain entry must be formatted like one of the following:

 1. "domain.name.TLD". For example, if you want to include *.contoso.com/*, use "contoso.com"
2. "hostname". For example, if you want to include [http://example](http://example), use "example"
3. "file:///path/filename.htm". For example, use "file:///C:/Users/contoso/Desktop/index.htm"

 If you disable or don't configure this policy setting, the list is deleted and Internet Explorer continues to block specific outdated ActiveX controls on all domains in the Internet Zone.

 For more information, see "Outdated ActiveX Controls" in the Internet Explorer TechNet library.

 At the registry side the settings are as following (User or Computer)


- Software\Microsoft\Windows\CurrentVersion\Policies\Ext|AuditModeEnabled
- Software\Microsoft\Windows\CurrentVersion\Policies\Ext|RunThisTimeEnabled
- Software\Microsoft\Windows\CurrentVersion\Policies\Ext|VersionCheckEnabled
- Software\Microsoft\Windows\CurrentVersion\Policies\Ext|ListBox_DomainAllowlist


