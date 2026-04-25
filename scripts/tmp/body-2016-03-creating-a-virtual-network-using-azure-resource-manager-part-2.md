In the previous article ([Part1](https://www.verboon.info/2016/02/creating-a-virtual-network-using-azure-resource-manager-part-1/)) I walked through the steps of creating a Virtual Network using Azure Resource Manager and Visual Studio. In this article, we’ll look at using the Azure PowerShell cmdlets the some options for using parameters. 

  For this walkthrough you need the following:

     
- An Azure Subscription that allows you to deploy resources    
- Azure PowerShell 1.0 or great, download and installation details can be found [here](https://azure.microsoft.com/en-us/documentation/articles/powershell-install-configure/) 

   

  First login to Azure using the **Login-AzureRmAccount** command. 

  Next we define two variables that point to the template and the template parameter files I created previously. 

  # Variables for Template and Template parameter file   
$Templatefile = "[https://raw.githubusercontent.com/alexverboon/posh/master/Azure/ResourceManager/VirtualNetwork/azuredeploy_virtualnetwork.json"](https://raw.githubusercontent.com/alexverboon/posh/master/Azure/ResourceManager/VirtualNetwork/azuredeploy_virtualnetwork.json")    
$ParameterFile = [https://raw.githubusercontent.com/alexverboon/posh/master/Azure/ResourceManager/VirtualNetwork/azuredeploy_virtualnetwork.parameters.json](https://raw.githubusercontent.com/alexverboon/posh/master/Azure/ResourceManager/VirtualNetwork/azuredeploy_virtualnetwork.parameters.json)

  and we will also use a powershell object that holds the parameter value for the Virtual network name. 

  # Input Object   
$paramobj = @{ vnetname = "Vnet3"}

  We will also need a Resource Group, so let’s create a new one. 

  # Create Resource Group   
$ResourceGroupName = "TestResourceGroup"     
$Location = "westeurope"     
New-AzureRmResourceGroup -Name $ResourceGroupName -Location $location –Verbose

  Now that we have all the things in place, let’s test things first, before starting the deployments. The Test-AzureRmResourceGroupDeployment command allows us to test the various scenarios. The scenarios are as following:

     
- Deploy a new resource from template only. The *vnetname* is as defined in the template    
- Deploy a new resource from template and template parameter file to override the default value for the *vnetname* defined in the template    
- Deploy the new resource from the template and using a parameter object to override the default value for the *vnetname* defined in the template.     
-  

  #Test with Template only   
Test-AzureRmResourceGroupDeployment -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -Verbose    
#Test with Template and parameter file    
Test-AzureRmResourceGroupDeployment -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -TemplateParameterUri $ParameterFile -Verbose    
#Test with template and parameter object    
Test-AzureRmResourceGroupDeployment -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -TemplateParameterObject $paramobj -Verbose

  [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2016/03/image.png)

  So now we know that the template, the template parameter file and the parameter object are valid. Let’s move on and create things.

  New-AzureRmResourceGroupDeployment -Name "Example1"  -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -Verbose    
New-AzureRmResourceGroupDeployment -Name "Example2"  -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -TemplateParameterUri $ParameterFile -Verbose    
New-AzureRmResourceGroupDeployment -Name "Example3"  -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -TemplateParameterObject $paramobj –Verbose 

  Now let’s look at the ResourceGroupDeployment via PowerShell. 

  Get-AzureRmResourceGroupDeployment -ResourceGroupName $ResourceGroupName 

  [
![image](images/image_thumb-1.png)
](https://www.verboon.info/wp-content/uploads/2016/03/image-1.png)

  and within the Azure Console. 

  [
![image](images/image_thumb-2.png)
](https://www.verboon.info/wp-content/uploads/2016/03/image-2.png)

  The New-AzureRmResourceDeployment has an important parameter we didn’t specify before, but that’s worth mentioning. –Mode. The online Azure documentation currently doesn’t say a lot about this option, but I found a good description [here](https://github.com/Azure/azure-content/blob/master/articles/resource-group-template-deploy.md). 

  By default, Resource Manager handles deployments as incremental updates to the resource group. With incremental deployment, Resource Manager:

     
- **leaves unchanged** resources that exist in the resource group but are not specified in the template     
- **adds** resources that are specified in the template but do not exist in the resource group     
- **does not re-provision** resources that exist in the resource group in the same condition defined in the template 

  Through Azure PowerShell or the REST API, you can specify a complete update to the resource group. Azure CLI currently does not support complete deployments. With complete deployment, Resource Manager:

     
- **deletes** resources that exist in the resource group but are not specified in the template     
- **adds** resources that are specified in the template but do not exist in the resource group     
- **does not re-provision** resources that exist in the resource group in the same condition defined in the template 

  You specify the type of deployment through the **Mode** property, as shown in the examples below for PowerShell and REST API.

  So let’s run the command again with the –Mode complete option and see what happens. 

  New-AzureRmResourceGroupDeployment -Name "Example1"  -ResourceGroupName $ResourceGroupName -TemplateUri $TemplateFile -Verbose **-Mode Complete**

  [
![image](images/image_thumb-3.png)
](https://www.verboon.info/wp-content/uploads/2016/03/image-3.png)

  [
![image](images/image_thumb-4.png)
](https://www.verboon.info/wp-content/uploads/2016/03/image-4.png)

  Only VNet1 is leftover, all other deployments are gone. 

  [
![image](images/image_thumb-5.png)
](https://www.verboon.info/wp-content/uploads/2016/03/image-5.png)

  The template, template parameter json files and the powershell code snipppets used in this article can be found here:

  [https://github.com/alexverboon/posh/tree/master/Azure/ResourceManager/VirtualNetwork](https://github.com/alexverboon/posh/tree/master/Azure/ResourceManager/VirtualNetwork)

  I hope this provided you with some ideas on how to work with the Azure Resource Manager templates. In a next blog post, I’ll walk through the deployment of a virtual machine.