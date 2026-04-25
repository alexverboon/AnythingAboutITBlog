Here’s a ConfigMgr Compliance baseline that checks the BranchCache configuration on Windows 8 clients. With the release of Windows 8 and Server 2012 Microsoft also made available [PowerShell cmdlets for BranchCache](http://technet.microsoft.com/en-us/library/hh848392.aspx), so creating a script based configuration item in ConfigMgr becomes a pretty straight forward task. 

  The below Compliance Baseline checks the following 3 things. 

     
- Is BranchCache Enabled     
- Is the Service Running     
- Is BranchCache operating in Distributed Cache mode  

  [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image.png)

  The following PowerShell commands are included within the configuration items. 

  
```

$bcstat = get-bcstatus | Select-Object -Property BranchCacheIsEnabled
$($bcstat).BranchCacheIsEnabled
#True

$bcsrv = get-bcstatus | Select-Object -Property BranchCacheServiceStatus
$($bcsrv).BranchCacheServiceStatus
#Running

$bmode = get-bcstatus | Select-Object -ExpandProperty ClientConfiguration 
$($bmode).CurrentClientMode
# DistributedCache
```

The result is as following (when all is compliant. 

 

[
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image1.png)

Or as following when things are NOT Compliant.  

[
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image2.png)

You can download the exported Win8-BranchCache.cab fie from here: [http://sdrv.ms/GKMDyE](http://sdrv.ms/GKMDyE)