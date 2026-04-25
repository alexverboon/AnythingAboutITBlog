To keep a long story short, today i started looking into Azure PowerShell and Azure Resource Manager and quickly found out that if I wanted to make use of ARM, i have to change some scripts I have used so far to deploy my Azure VMs. More on that in a later post.

One cmdlet that I find paticularely annoying to use is **Set-AzureRmVMSourceImage** as it has a couple of mandatory parameters and to find the right values for these, you have to run the follwoing three cmdlets first.

	
- Get-AzureRmVMImagePublisher
	
- Get-AzureRmVMImageOffer
	
- Get-AzureRmVMImageSku

The order of the above list is on purpose. You have to start using the Get-AzureRmVMImagePublisher as this cmdlet only requires you to provide the location parameter. If you have worked with Azure cmdlets before you’re probably familiar with how locations are defined i.e “West US” or “West Europe”.

Run the following command to find all possible location values:

Get-AzureRmResourceProvider -ListAvailable | Select-Object -ExpandProperty ResourceTypes | Select-Object -ExpandProperty Locations -Unique

The Get-AzureRmVMImagePublisher will output all available Publishernames,  so now  you can move on using the Get-AzureRmVMImageOffer cmdlet, with that one you get the -offer parameter values that you need in order to use the Get-AzureRmVMImageSku cmdlet.

The trick of using a command like the one below doesn’t help anymore because Get-AzureRmVMImagedoesn’t expose the required information required by the Set-AzureRmVMSourceImage cmdlet.

*Get-AzureVMImage | where { $_.ImageFamily -eq "Windows 10 Enterprise (x64)" } | sort PublishedDate -Descending | select -ExpandProperty ImageName -First 1*

In order to identify the values required, i wrote the below helper script called Get-AzureImageSkuInfo