Since I am going install the ADK on several clients and servers, I decided to automate that process based on the information found in the MSDN article [Installing the Windows ADK](http://msdn.microsoft.com/en-us/library/hh825494.aspx)

  Because downloading all the ADK sources from the Microsoft web can take a while, the first task is to only download them and save the locally.

     
- Create a folder on your local drive, let’s say C:\DATA\ADKSETUP     
- Then download the ADKSETUP.EXE from the Microsoft download page [here](http://www.microsoft.com/en-us/download/details.aspx?id=29929) and store it into C:\DATA\ADKSETUP (Note that this link will change once the RTM version is released).     
- Create a batch file called ADK_Download.cmd that has the following content:      
      
@ ECHO OFF        
cd %~dp0  
adksetup.exe /quiet /installpath %~dp0  /layout %~dp0         
Pause       
    
- Then launch the script with elevated rights and wait for the download to complete.  

  [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2012/06/image1.png)

  When the ADK setup tool has downloaded all sources, you will find a new folder called Installers and a file called UserExperienceManifest. According to my findings, when the UserExperienceManifest file exists, the ADKSetup.exe assumes that the sources are downloaded and available in the Installers folder. To see the difference in behavior launch ADKSETUP.EXE with and without the file being present.

  Now that we have the installation sources stored locally we can install the ADK on any client or server offline. ADKSETUP.EXE provides several installation options that are explained in detail [here](http://msdn.microsoft.com/en-us/library/hh825494.aspx#InstallingNonNetworked) (go to section ADKSetup.exe Command-Line Syntax) or just launch ADKSEUP.EXE /?

  For installing all features included in the ADK do the following:

     
- Create a batch file called adk_install.cmd and add the following content:      
      
@ ECHO OFF        
cd %~dp0  
adksetup.exe /promptrestart /ceip on /quiet /installpath "c:\program files (x86)\Windows Kits\8.0" /features +  

  If you only want to install one or more specific features, then only specify those after the /features option.

     
- Create a batch file called adk_install_winpe.cmd and add the following content:      
      
@ ECHO OFF        
cd %~dp0  
adksetup.exe /promptrestart /ceip on /quiet /installpath "c:\program files (x86)\Windows Kits\8.0" /features OptionId.WindowsPreinstallationEnvironment  

  For a complete list of all available features run ADKSETUP.EXE /LIST

     OptionId.ApplicationCompatibilityToolkit

     OptionId.DeploymentTools

     OptionId.WindowsPreinstallationEnvironment

     OptionId.UserStateMigrationTool

     OptionId.VolumeActivationManagementTool

     OptionId.WindowsPerformanceToolkit

     OptionId.WindowsAssessmentToolkit

     OptionId.WindowsAssessmentServicesClient

     OptionId.SqlExpress2012

   

  Well and of course what gets installed sometimes must be removed, so to uninstall the ADK just run the following command:

  adksetup.exe /promptrestart /ceip on /quiet /uninstall

  Have a great day.