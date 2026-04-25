Aaron Margosis recently [released Policy Analyzer](http://blogs.technet.com/b/secguide/archive/2016/01/22/new-tool-policy-analyzer.aspx), a utility for analyzing and comparing sets of Group Policy Objects (GPOs). Here’s a brief description on how to use the tool to compare two Domain GPOs. 

 I created two GPOs in my test domain, both starting with the name “Foo” and then configured some settings. The Policy Analyzer can import GPO settings based on a GPO backup so as a next step we create a GPO backup. The quickest way is to do this via PowerShell. 

 **Get-GPO -All | Where-Object {$_.DisplayName -like "Foo Corp*"} | Backup-GPO -Path C:\data**

 [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image.png)

 Now that we have a backup we copy them into the Policy Analyzer working folder, in my case that’s:

 C:\Users\Admin\Documents\PolicyAnalyzer\**GPOs**

 [
![image](images/image_thumb-1.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-1.png)

 Next Open the Policy Analyzer Tool and select Add. 

 [
![image](images/image_thumb-2.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-2.png)

 A new window opens, select File, add files from GPOs

 [
![image](images/image_thumb-3.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-3.png)

 Select the first folder

 [
![image](images/image_thumb-4.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-4.png)

  

 [
![image](images/image_thumb-5.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-5.png)

 Select **Import**, and provide a name. 

  

 [
![image](images/image_thumb-6.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-6.png)

 Repeat these steps for every GPO you want to compare. 

  

 [
![image](images/image_thumb-7.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-7.png)

 Next select View / Compare. 

 [
![image](images/image_thumb-8.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-8.png)

 Select Export / Export all data to Excel

 [
![image](images/image_thumb-9.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-9.png)

 and there you, all information nicely prepared and ready for review. 

 [
![image](images/image_thumb-10.png)
](https://www.verboon.info/wp-content/uploads/2016/01/image-10.png)

 The Policy Analyzer tool and documentation is available for download [here](http://blogs.technet.com/b/secguide/archive/2016/01/22/new-tool-policy-analyzer.aspx)

  

 By the way, Microsoft also finally  released the Security Baseline for Windows 10  “[Security baseline for Windows 10 (v1511, "Threshold 2") -- FINAL](http://blogs.technet.com/b/secguide/archive/2016/01/22/security-baseline-for-windows-10-v1511-quot-threshold-2-quot-final.aspx)”   The [Windows 10 TH2 Security Baseline.zip](http://blogs.technet.com/cfs-filesystemfile.ashx/__key/telligent-evolution-components-attachments/01-4062-00-00-03-65-94-81/Windows-10-TH2-Security-Baseline.zip) also contains a backup of the Windows 10 baselnie GPOs, so you can import these into Policy Analzyer as well and start comparing your current GPOs with those of the Security Baseline. 

 Enjoy!