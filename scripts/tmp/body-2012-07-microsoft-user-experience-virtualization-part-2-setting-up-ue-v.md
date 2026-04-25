As a follow up on my earlier post [Microsoft User Experience Virtualization – Part 1: The Road to UE-V](https://www.verboon.info/index.php/2012/07/microsoft-user-experience-virtualization-part-1-the-road-to-ue-v/) in todays’ post I am going to describe how to get UE-V up and running in just a few steps. 

  To conduct this mini proof of concept, you need the following:

     
- Access to Active Directory (Group Policy Management and the Users and Computers Console)     
- Access to a File Server to create 2 shares     
- 2 Windows Clients both joined to the domain. Ideally one running Windows 7 and one running Windows 8, but it’s okay if both run Windows 7 or Windows 8.     
- On the Windows 8 client NET 3.5 or .NET 4.0 must be installed.     
- A test domain user account that has no roaming profile setup     
- If you’re doing this in a production environment I suggest you setup a dedicated test OU where you store both the test computer and user accounts.     
- Access to the UE-V Beta 2 installation sources. Click [here](http://go.microsoft.com/fwlink/?LinkID=245990&clcid=0x409) to download (Windows Live ID required)  

  **Active Directory Setup**

  For my proof of concept I have created an OU called Engineering that contains a Desktops OU that stores the computer objects and a Users OU that holds the test user accounts. 

  ![clip_image001](https://www.verboon.info/wp-content/uploads/2012/07/clip_image001.png)

  **Setting up the Shares**

  We need 2 shares. One where we store the UE-V Templates, and one where users will store their UE-V Settings. 

  For the UE-V Template store create a folder on the File Server called UEVTEMPLATES underneath the folder C:\DATA. The folder C:\DATA is shared as DATA. 

  Try opening the folder through \\<Servername>\<Share>\UEVTEMPLATES

  For the UE-V Settings storage create a folder on the File Server called UEVSETTINGS and then share that folder as UEVSETTINGS. Set the Share permissions as following:

                                **User Account**

                              **Permissions**

                                            Everyone

                              No Permissions

                                            Domain Users or Security Group for UE-V users

                              Full Control

                      

  Then apply the following NTFS permissions to the UEVSETTINGS folder.

                                **User Account**

                              **Permissions**

                              **Folder**

                                            Creator Owner

                              No permissions

                              No Permissions

                                            Domain Admins

                              Full Control

                              This Folder, Subfolders and files

                                            Domain Users (or Security group for UE-V Users)

                              List Folder / Read Data, Create Folders / Append Data

                              This Folder only

                                            Local System

                              Full Control

                              This Folder, Subfolders and Files

                                            Everyone

                              No permissions

                              No Permissions

                      

  Try opening the folder through \\<Servername>\UEVSETTINGS

  **Setting up the UE-V Group Policy Settings**

  The UE-V Agent can be easily configured through Group Policy settings. 

  First copy the UE-V ADMX template that is included in the UEV_ADMX_Templates.zip into your Group Policy central store. The file **UserExperienceVirtualization.admx** goes directly into the 

  \\<domain controller server>\SYSVOL\HOMELAB.LOCAL\Policies\PolicyDefinitions folder

  and the **UserExperienceVirtualization.adml** file must be copied into 

  \\<domain controller server>\SYSVOL\HOMELAB.LOCAL\Policies\PolicyDefinitions\en-US folder

  Now create a new Group Policy object called UE-V Configuration and apply the settings as listed below:

  ![clip_image003](https://www.verboon.info/wp-content/uploads/2012/07/clip_image003.jpg)

  ![clip_image005](https://www.verboon.info/wp-content/uploads/2012/07/clip_image005.jpg)

  Then link the GPO to the OU where you have stored the test user and computer accounts. In my case I have linked it to the Engineering OU. 

  ![clip_image006](https://www.verboon.info/wp-content/uploads/2012/07/clip_image006.png)

  **Installing the UE-V Agent on the Clients**

  And finally install the UE-V Agent on the Windows Clients by launching the **Agentsetup.exe** that is included in the UE-V Beta 2 installation sources. There is nothing special to choose from during the installation so just select Next, Next and Finish, once completed reboot the client. 

  **Show Time**

  Logon with the test user account on the first Client and open Notepad. From the Menu select View then enable the Status bar. Then select Format Fonts and set the Font Style to Bold and the size to 20. Then close Notepad. 

  ![clip_image008](https://www.verboon.info/wp-content/uploads/2012/07/clip_image008.jpg)

  Logon on the second client with the same user account and then open notepad. If UE-V kicked in correctly then the Font size should be set to bold and the size set to 20. Also the Status bar should be enabled. 

  ![clip_image010](https://www.verboon.info/wp-content/uploads/2012/07/clip_image010.jpg)

  Just out of the box this works for a number of Office 2010 applications, Internet Explorer, some Windows Settings, Notepad and WordPad. 

  If something wasn’t clear then you find all the details in the Admin guide **UE-Vv1_AdminGuide.pdf** that’s included in the UE-V Beta 2 sources. 

  In a following post I will explain how to create a template for your own application.