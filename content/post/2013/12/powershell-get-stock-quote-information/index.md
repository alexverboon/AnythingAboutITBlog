---
title: PowerShell - Get Stock Quote Information
layout: post
date: '2013-12-15T13:29:17Z'
slug: powershell-get-stock-quote-information
aliases:
- /2013/12/powershell-get-stock-quote-information/
description: The below script makes use of a webservice hosted by webserviceX.net
  and provides stock quote information. ``` <# .Synopsis Retrieve stock information...
author: Alex Verboon
image: img/post-heroes/powershell-get-stock-quote-information.png
categories:
  - 'PowerShell'
tags:
  - 'Stockquote'
---
The below script makes use of a webservice hosted by webserviceX.net and provides stock quote information. 

`powershell

<#
.Synopsis
   Retrieve stock information
.DESCRIPTION
   Retrieve stock information 
.PARAMETER Symbol
  Stock symbol of one or more companies
.EXAMPLE
 Get-StockInfo -Symbol MSFT,INTC
.LINK
   
.NOTES
  Version 1.0, by Alex Verboon
#>
 
[CmdletBinding()]
Param(
[Parameter(Mandatory=$true,
            ValueFromPipelineByPropertyName=$true,
            HelpMessage= 'Stock Symbol for the company')]
            [String[]]$Symbol
)

begin{}
process{

if ([string]::IsNullOrEmpty($Symbol))
    {Write-Output "You must provide a Symbol"
    Exit}
  
ForEach ($stock in $Symbol)
    {
    [xml][/xml]$sq = Invoke-WebRequest -uri http://www.webservicex.net/stockquote.asmx/GetQuote?symbol=$stock
    $sqdetail = [xml][/xml]$sq.DocumentElement.'#text' 
    $sqdetail.StockQuotes.stocK
    }
}

End{}

```

![2013-12-15_14h28_47](images/2013-12-15_14h28_47_thumb.png)
