---
title: Don't send outlook messages without subject
layout: post
date: '2009-01-13T19:13:36Z'
slug: dont-send-outlook-messages-without-subject
aliases:
- /2009/01/dont-send-outlook-messages-without-subject/
description: This probably has happened to each of us, writing an e-mail, then added
  the recipients and then clicked the send button, and as you clicked it, you no...
author: Alex Verboon
tags:
- outlook
- Office
categories:
- tip
- Office
---
This probably has happened to each of us, writing an e-mail, then added the recipients and then clicked the send button, and as you clicked it, you notice that you forgot to fill in the subject.

To prevent this from happening, I found the following script today that will bring up an alert when trying to send an e-mail without a subject. 

To create the macro in Outlook 2003, go to Tools -> Macro -> Visual Basic Editor (this feature has to be installed). In Microsoft Office Outlook Objects -> ThisOutlookSession, then paste the following code:

Private Sub Application_ItemSend(ByVal Item As Object, Cancel As Boolean)
Dim strSubject As String
strSubject = Item.Subject
If Len(Trim(strSubject)) = 0 Then
Prompt$ = "Subject is Empty. Are you sure you want to send the Mail?"
If MsgBox(Prompt$, vbYesNo + vbQuestion + vbMsgBoxSetForeground, "Check for Subject") = vbNo Then
Cancel = True
End If
End If
End Sub

[](http://searchexchange.techtarget.com/tip/0,,sid43_gci1208873,00.html#)

