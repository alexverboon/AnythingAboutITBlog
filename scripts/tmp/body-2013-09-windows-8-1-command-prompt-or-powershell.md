If you have used the Windows 8.1 preview build, you will have noticed that the X-Menu by default had PowerShell enabled instead of the Command Prompt.. However within the RTM release of Windows 8.1 Microsoft changed this, so now the command prompt is the default again as it was in Windows 8.

 [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2013/09/image1.png)

 To change the default back to PowerShell open the Taskbar and Navigation Properties and enable “*Replace Command Prompt with Windows PowerShell in the menu when I right click the lower left corner or press Win +X*”

 [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2013/09/image2.png)

 Windows then sets the value of the registry key HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\
DontUsePowerShellOnWinX to 0

 [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2013/09/image3.png)

 And there is also a Group Policy setting to prevent users from changing this setting. It’s located under 
User Configuration \ Administrative Templates \Windows Components \ Edge UI

 Prevent users from replacing the Command Prompt with Windows PowerShell in the menu they see when they right-click the lower-left corner or press the Windows logo key+X

 [
![image](images/image_thumb4.png)
](https://www.verboon.info/wp-content/uploads/2013/09/image4.png)

 The result is that the option to change the setting is greyed out. 

 [
![image](images/image_thumb5.png)
](https://www.verboon.info/wp-content/uploads/2013/09/image5.png)