---
title: "Retrieve Azure Virtual Machine Size information with PowerShell"
layout: "post"
date: 2017-02-07T19:46:07Z
slug: "retrieve-azure-virtual-machine-size-information-with-powershell"
aliases:
  - "/2017/02/retrieve-azure-virtual-machine-size-information-with-powershell/"
description: "One important topic to consider when deploying virtual machines in Azure is the [size](https://azure.microsoft.com/en-us/pricing/details/cloud-service..."
author: "Alex Verboon"
tags:
  - azure
  - azure-storage
  - compute
  - pricing
  - size
  - PowerShell
categories:
  - azure
  - PowerShell
---
One important topic to consider when deploying virtual machines in Azure is the [size](https://azure.microsoft.com/en-us/pricing/details/cloud-services/) of the virtual machine as this affects the pricing, but beware that not only virtual machine sizing has a pricing impact other factors like [storage](https://azure.microsoft.com/en-us/pricing/details/storage/disks/) and optional features like [IP address options](https://azure.microsoft.com/en-in/pricing/details/ip-addresses/) add to the costs as well.

A good starting point to get an understanding of virtual machine costs is the Azure pricing calculator: [https://azure.microsoft.com/en-in/pricing/calculator/](https://azure.microsoft.com/en-in/pricing/calculator/)

![image](https://i1.wp.com/www.verboon.info/wp-content/uploads/Retrieve-Azure-Virtual-Machine-Size-info_11B7A/image.png)

Be aware that when selecting SSD disks, storage costs will be noticeable higher than when using HDD disks. To get a better understanding of the available Azure virtual machine sizes I strongly recommend to the read the following documentation:

Sizes for Cloud Services: [https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-sizes-specs](https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-sizes-specs)

Premium Storage: High Performance storage for Azure virtual machine workloads: [https://docs.microsoft.com/en-us/azure/storage/storage-premium-storage](https://docs.microsoft.com/en-us/azure/storage/storage-premium-storage)

To keep an overview of the virtual machine size of deployed virtual machines, i wrote a little helper script [Get-AzureRmVMSizeSpecs](https://github.com/alexverboon/posh/blob/master/Azure/Utilities/Get-AzureRmVMSizeSpecs.ps1)

For example, to get a list of all deployed virtual machines in any resource group in my subscription, I can run the following command:

```
ForEach ($rg in Get-AzureRmResourceGroup) {Get-AzureRmVMSizeSpecs -ResourceGroupName $rg.ResourceGroupName -Verbose}
```

The script has two usage modes. When using the **–Location** parameter, it shows all vmsizes available in the Azure regions the command is similar to the native cmdlet Get-AzureRmVmSize, but this version of the script allows you to select the location from all currently known Azure locations.

When using the -**ResourceGroup** parameter the script looks for virtual machine resources within the azure resource group and then retrieves the VM size information.

```

```

