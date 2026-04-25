---
title: "OMS Log Analytics HTTP Data Collector API &ndash; Work notes"
layout: "post"
date: 02/08/2017 13:08:44
slug: "oms-log-analytics-http-data-collector-api-work-notes"
aliases:
  - "/2017/02/oms-log-analytics-http-data-collector-api-work-notes/"
description: "I believe that the Microsoft Operations Management Suite is yet another example of how cool Cloud based solutions can be. Instead of first having to s..."
author: "Alex Verboon"
tags:
  - api
  - azure
  - data-collector
  - json
  - log-analytics
  - oms
  - post
categories:
  - azure
  - log-analytics
  - oms
---
I believe that the Microsoft Operations Management Suite is yet another example of how cool Cloud based solutions can be. Instead of first having to spin up an entire backend infrastructure before you can actually start collecting data, with the Microsoft Operations Management Suite you can directly start focusing on the task of collecting and visualizing your data. This blog post is basically a summary of my notes and scripts that I created while exploring the OMS Log Analytics HTTP Data Collector API, that allows you to submit any type of data to an OMS Workspace.

 **Creating an OMS Workspace**

 First we create an OMS Workspace. Within the Azure Management portal. Select “New”  search for Log Analytics and then create a new OMS Workspace. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image.png)

 Once the provisioning process is completed, we have a new OMS Workspace. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_3.png)

 Clock on the “**OMS Portal**” button to access the portal. 

 ![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_4.png)

 **Managing OMS with PowerShell**

 The PowerShell Module “**AzureRM.OperationallInsights**” provides the cmdlets for managing OMS with PowerShell. More information on that can be found here:[https://blogs.technet.microsoft.com/privatecloud/2016/04/05/using-the-oms-search-api-with-native-powershell-cmdlets/](https://blogs.technet.microsoft.com/privatecloud/2016/04/05/using-the-oms-search-api-with-native-powershell-cmdlets/)

 When running the command:

```
Get-AzureRmOperationalInsightsWorkspace
```

We get the the following output:

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_5.png)

**Submitting Data to Log Analytics**

The Microsoft Operations Management suite provides a HTTP Data Collector API to send data to Log Analytics. A detailed overview including code examples is documented here: 
[https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api)

In the following example, we are going to submit custom data to the OMS workspace we just created. Let’s start with setting some variables:

```
#OMS workspace Name
$OMSWorkspacename = "APIDemo"

# identify ResourceGroup Name
$resourcegroupname = (Get-AzureRmOperationalInsightsWorkspace | Where-Object {$_.Name -eq "$OMSWorkspacename"}).ResourceGroupName

# Workspace ID
$customerId = (Get-AzureRmOperationalInsightsWorkspace | Where-Object {$_.Name -eq "$OMSWorkspaceName"}).CustomerId.guid

# Primary Shared Key
$sharedKey = (Get-AzureRmOperationalInsightsWorkspaceSharedKeys -ResourceGroupName $resourcegroupname -Name $OMSWorkspacename).PrimarySharedKey

```

As a next step we define the LogType and the TimeStampField reference. The LogType is the name of our custom log that will be created. The TimeStampField is a reference to the Field that contains the date-time stamp. (For more details look at the [Request Headers](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api) section). 

```
# Specify the name of the record type that you'll be creating
$LogType = "MyComputers"

# Specify a field with the created time for the records
$TimeStampField = "DateValue"

```

Next we define the data that we want to submit:

```
$json = @"
[{
    "MyComputerName": "Computer10",
    "MyModel": "T460",
    "MyManufacturer": "Lenovo",
    "MyLocation": "Zurich",
    "DateValue": "2017-02-08T12:13:35.576Z"
},
{
    "MyComputerName": "Computer11",
    "MyModel": "T450",
    "MyManufacturer": "Lenovo",
    "MyLocation": "Amsterdam",
    "DateValue": "2017-02-08T12:13:35.576Z"
},
{
    "MyComputerName": "Computer12",
    "MyModel": "T470",
    "MyManufacturer": "Lenovo",
    "MyLocation": "London",
    "DateValue": "2017-02-08T12:13:35.576Z"
}]
"@

```

And finally the code to submit the data to OMS, The Build-Signature and Post-OMSData functions originate from [example](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api) provided by Microsoft. 

```
# Create the function to create the authorization signature
Function Build-Signature ($customerId, $sharedKey, $date, $contentLength, $method, $contentType, $resource)
{
    $xHeaders = "x-ms-date:" + $date
    $stringToHash = $method + "`n" + $contentLength + "`n" + $contentType + "`n" + $xHeaders + "`n" + $resource

    $bytesToHash = [Text.Encoding]::UTF8.GetBytes($stringToHash)
    $keyBytes = [Convert]::FromBase64String($sharedKey)

    $sha256 = New-Object System.Security.Cryptography.HMACSHA256
    $sha256.Key = $keyBytes
    $calculatedHash = $sha256.ComputeHash($bytesToHash)
    $encodedHash = [Convert]::ToBase64String($calculatedHash)
    $authorization = 'SharedKey {0}:{1}' -f $customerId,$encodedHash
    return $authorization
}

# Create the function to create and post the request
Function Post-OMSData($customerId, $sharedKey, $body, $logType)
{
    $method = "POST"
    $contentType = "application/json"
    $resource = "/api/logs"
    $rfc1123date = [DateTime]::UtcNow.ToString("r")
    $contentLength = $body.Length
    $signature = Build-Signature `
        -customerId $customerId `
        -sharedKey $sharedKey `
        -date $rfc1123date `
        -contentLength $contentLength `
        -fileName $fileName `
        -method $method `
        -contentType $contentType `
        -resource $resource
    $uri = "https://" + $customerId + ".ods.opinsights.azure.com" + $resource + "?api-version=2016-04-01"

    $headers = @{
        "Authorization" = $signature;
        "Log-Type" = $logType;
        "x-ms-date" = $rfc1123date;
        "time-generated-field" = $TimeStampField;
    }

    $response = Invoke-WebRequest -Uri $uri -Method $method -ContentType $contentType -Headers $headers -Body $body -UseBasicParsing
    return $response.StatusCode

}

# Submit the data to the API endpoint
Post-OMSData -customerId $customerId -sharedKey $sharedKey -body ([System.Text.Encoding]::UTF8.GetBytes($json)) -logType $logType

```

If all went well we get a return code of “**200**” All possible return codes are documented [here](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api) in the Return Codes section. Let’s have a look if the data was successfully submitted, for this we can run the following command:

```
$dynamicQuery = "* Type=MyComputers_CL"
$result = Get-AzureRmOperationalInsightsSearchResults -ResourceGroupName $ResourceGroupName -WorkspaceName $OMSWorkspacename -Query $dynamicQuery -Top 100
$result.Value | ConvertFrom-Json

```

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_6.png)

**OMS Schema and custom fields**

When submitting data for the first time to OMS, the log analytics schema is extended with the custom fields defined within the json object. I wrote a little helper function that retrieves the Log Analytics schema information. The Get-OMSSchemaInfo cmdlet can be downloaded from [here](https://github.com/alexverboon/posh/blob/master/Azure/OMS/Get-OMSSchemaInfo.ps1). 

```
Get-OMSSchemaInfo -ResourceGroupName $ResourceGroupName -WorkSpaceName $OMSWorkspacename | Where-Object {$_.OwnerType -like "MyComputers*"}

```

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_7.png)

Okay, so far so good, we have submitted data, the schema has been extended and we can see the data we submitted to OMS. Now let’s head over to the OMS portal. 

**The OMS Portal**

Open the OMS Portal and select “Log Search”

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_8.png)

Next select “**Count of all data collected grouped by Type**”

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_9.png)

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_10.png)

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_11.png)

**Note**: Should you not see the full data but only the TimeGenerated information close all browser windows and open the OMS portal again. (Thanks to Cameron Fuller for the [tip](http://blogs.catapultsystems.com/cfuller/archive/2016/09/30/no-data-appearing-when-using-the-log-analytics-http-data-collector-api/)). 

You can also see the new created custom fields within the OMS Portal via Settings, Data, Custom Fields. 

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/e706d27f3053_964D/image_12.png)

In a next blog post, I’ll walk us through the creation of an OMS Dashboard. 

Hope you found this useful. 

Other useful resources that helped me throughout my OMS exploration process:

- [https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-data-collector-api)

- [https://blogs.technet.microsoft.com/stefan_stranger/2016/09/05/using-the-http-oms-data-collector-api-for-real-world-scenarios-part-1/](https://blogs.technet.microsoft.com/stefan_stranger/2016/09/05/using-the-http-oms-data-collector-api-for-real-world-scenarios-part-1/)

- [http://blogs.catapultsystems.com/cfuller/archive/2016/09/30/no-data-appearing-when-using-the-log-analytics-http-data-collector-api/](http://blogs.catapultsystems.com/cfuller/archive/2016/09/30/no-data-appearing-when-using-the-log-analytics-http-data-collector-api/)

- [https://gallery.technet.microsoft.com/Inside-the-Operations-2928e342](https://gallery.technet.microsoft.com/Inside-the-Operations-2928e342)

- Videos – Using OMS and Citrix
[https://www.youtube.com/watch?v=oysafpYZl38](https://www.youtube.com/watch?v=oysafpYZl38)
Great introduction from Marc Kean on Log Analytics
[https://www.youtube.com/watch?v=5qq4mBUJ6aQ](https://www.youtube.com/watch?v=5qq4mBUJ6aQ)

