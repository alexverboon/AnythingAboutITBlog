Today one of my colleagues ran into an issue after having slipstreamed Service Pack 3 into Windows XP. During the Windows XP unattended installation process the provided product key within the unattend.txt file was not accepted, which caused the system to prompt for the product key. 

  
![image](http://web.suffieldacademy.org/ils/netadmin/docs/howto/windows_xp_install/docs/images/setup_product_activation.png)

  This turned out to be a known issue as documented within the following Microsoft support article. [After you create Windows XP Service Pack 3 slipstreamed media, your product key is not accepted](http://support.microsoft.com/kb/950722/en-us). 

  Bottom line, don’t run the slipstream command on a Windows Vista or Windows Server 2008 system.