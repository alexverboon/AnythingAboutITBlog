This year I have had the opportunity to speak with many customers about Windows 7. One topic that came up in almost every discussion was about how mobile users can install their local devices without having to grant them local administrator rights. With previous versions of Windows (NT 4, Windows 2000 and XP) many companies ended up in granting their mobile users local administrator or power user rights, just because they needed to have the flexibility of installing drivers for their local devices. While in the past the need for installing a local device was primarily for local printers, nowadays where people use multiple devices there is also a demand to support mobile phones, headsets and cameras. 

  With the release of Windows Vista and later Windows 7 Microsoft added a number of features and new technologies that provide a better end user experience and enhances local device installation manageability for enterprise administrators. In this blog post I will focus on what actually happens when connecting a new local device to a Windows 7 client and how the behavior can be influenced through Group Policy Settings. 

  With Windows XP a standard user can only install a new device if it is supported by a so-called in-box driver (drivers that are provided with the XP installation) or if a driver is found on Windows Update. In Windows XP the number of devices supported by the in-box drivers is limited compared to Windows 7 and often became outdated. Microsoft introduced the hardware related software content through Windows Update in the year 2005 and as we all know a year later they released Windows Vista, hence many hardware vendors didn’t probably invest a lot of effort in providing drivers through Windows Update for Windows XP. (just my personal observation). Due to these limitations mobile users often needed to be granted with local administrative rights to provide them with the required flexibility to install local devices. 

  With the introduction of Windows Vista the way how drivers are installed has quite changed. Instead of having multiple locations where previous Windows versions stored device driver sources, Windows Vista and later versions of Windows use the Driver Store which is a trusted location within Windows where all in-box and 3rd party drivers packages are stored. Only drivers that are stored within the Driver Store can be installed within Windows. The process of getting a driver into the Driver Store is called “staging”. The good news is that any device driver that is already staged within the driver store can be installed by a any user without administrative rights. 

  Let’s have a look at what happens when a user connects a new device to a Windows 7 client. By default Windows 7 will first search for a matching driver on Windows Update and if one is found automatically downloads and stages it into the driver store before installing it. If no matching driver could be found Windows continues searching for a matching driver within the driver store that holds both in-box drivers and 3rd party drivers that have already been pre-staged into the driver store. If a matching driver is found Windows installs it. If still no matching driver could be found Windows will continue to search within the locations specified within the DevicePath registry value, this can be a local folder on the system such as C:\Drivers or a network share. If in the end no matching driver could be found in any of the search locations, Windows will simply tell you that no driver was found. 

  The above described process will help most home and small business users to get their devices installed with or without local administrative rights but those of you who work in larger corporate environments will recognize some challenges. 

     
- Many companies want to know and approve the content that is being installed on their devices. So even if we can consider the content on Microsoft Windows Update as trustworthy, many companies won’t allow that their clients search for a matching driver on a remote Windows Update Server because it might cause a conflict with their internal IT security policy.      
    
- According to my findings, it’s not possible to separate the search locations for Windows Security updates and hardware related software (drivers), hence where companies use WSUS, clients will only search for drivers on the internal Windows Update Server also used for patch distribution. (*if I’m wrong here I’m happy to hear from you*)      
    
- Unless a company maintains a very strict policy for the use of specific devices, IT administrators will have a challenge to keep the Driver Store on their clients up to date with the required drivers.  

  But despite all these challenges, there are a number of solutions available. Like many other things, device driver installation behavior can be controlled through a number of Group Policies. 

  [
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/image.png)

  The settings can be found under Computer Configuration \ Administrative Templates \ System \ Device Installation, the settings under User Configuration \ Administrative Templates \ System \ Driver Installation can be ignored as they do not apply to Windows 7. 

  
## Prevent Clients from searching for drivers on Windows Update

  To prevent Windows 7 clients from searching for drivers on Windows Update, enable the Group Policy “Specify search order for device driver source locations” and configure it to “Do not search Windows Update”. 

  [
![image](images/image_thumb1.png)
](https://www.verboon.info/wp-content/uploads/2010/12/image1.png)

  
## Allow Standard Users to Install Drivers For Devices from Specified Setup Classes

  With the Group Policy Setting “Allow installation of devices using drivers that match these device setup classes” located under Configuration \ Administrative Templates \ System \ Device Installation \ Device Installation Restrictions IT Administrators can allow standard users to stage and install a driver of a specific Setup Class. This means that if the IT department can’t keep up with distributing printer driver packages to their clients, the installation for Printers can be completely enabled for standard users while maintaining the restriction for other types of devices. This means that a standard user can stage a driver into the driver store and install it. 

  [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2010/12/image2.png)

  Note when adding the setup class for printers you should also consider adding the class for imaging devices because a HP all in one inkjet printer has an imaging device class and not the printer class. A complete list of defined setup classes can be found [here](http://msdn.microsoft.com/en-us/library/ff553426(v=vs.85).aspx). A complete step by step guide on how to configure this can be found [here](http://technet.microsoft.com/en-us/library/cc770453(WS.10).aspx). 

  For more details on how to configure what devices users are allowed to install I recommend reading the following TechNet documentation [Controlling Which Devices Can Be Installed by Standard Users](http://technet.microsoft.com/en-us/library/cc732048(WS.10).aspx).

  
## Pre-Staging Drivers into the Windows Clients Driver Store

  For the widely knows devices the IT Administrator can pre-stage the appropriate drivers within the driver store of his mobile user devices. This could be done as following: 

     
- Pre-stage drivers within the corporate standard client image    
- Pre-stage drivers during the client post installation process (MDT, SCCM, WSUS)    
- Pre-stage drivers on demand like distributing a software package 

  I won’t go into the detail here how to accomplish this for each above listed scenario, but let’s take an easy example that many IT Administrators will face in the real world. 

  Almost any mobile user I know wants to synchronize their calendar on their mobile device and if that mobile device is running Windows Mobile, they will need the Windows Mobile Device Center which is required when you connect a Windows mobile device to a Windows 7 system. 

  Unless you do already exactly know what driver you need, a simple method is to just let the device automatically install on a client that has no restrictions and that can access Windows Update. Once the device installation is complete open the folder C:\Windows\System32\Drivers tore and look for the folder that was just added. 

  [
![2010-12-31 02h11_40](images/2010-12-31-02h11_40_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-31-02h11_40.png)

  Now you can just copy away that folder and use that as the source to pre-stage the driver store of your enterprise clients. Another possibility is to download the driver package [directly](http://support.microsoft.com/kb/323166) from the Windows Update Catalogue. 

  [
![2010-12-31 02h27_04](images/2010-12-31-02h27_04_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-31-02h27_04.png)

  Once downloaded you get the X86-ar_bg_zh-tw_cs_da_de_el_en_es_fi_fr_...v_th_tr_sl_et_lv_lt_zh-cn_pt_ja-nec-20060042_b5eca0da489018bbc1930e42252b1034f739af15.cab file. As a next step extract the content from the CAB file. 

  In this example I show you how to add a driver to the driver store on a running Windows 7 client for offline editing of a corporate image read [this article](http://www.msigeek.com/2661/add-or-remove-a-driver-from-a-wim-image-using-dism) from Vijay. 

  To add a driver to the driver store we can use the pnputil.exe command line utility as shown in the picture below. 

  [
![2010-12-31 02h34_16](images/2010-12-31-02h34_16_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-31-02h34_16.png)

  For those interested, the setupapi.dev.log located in c:\Windows\INF provides detailed information about what exactly is happening now. 

  [
![2010-12-31 02h51_23](images/2010-12-31-02h51_23_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-31-02h51_23.png)

  Now that the required Device Driver is pre-staged within the driver store, we can logon as a standard user and connect a mobile device. (in this case I used a Samsung Omnia GT8000 running Windows Mobile 6.5). 

  [
![gt_install](images/gt_install_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/gt_install.png)

  again the setupapi.dev.log provides more details on what is happening now. 

  [
![2010-12-31 02h57_10](images/2010-12-31-02h57_10_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-31-02h57_10.png)

  [
![gt_installed2](images/gt_installed2_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/gt_installed2.png)

  Since the driver was already pre-staged, the driver gets automatically installed and is ready for use shortly after having connected the device for the first time. 

  I hope you enjoyed this overview and as always, any comments, inputs are welcome. 

   

  **Additional Resources**

  [Windows 7 Device Installation Experience](http://download.microsoft.com/download/5/e/6/5e66b27b-988b-4f50-af3a-c2ff1e62180f/con-t532_wh08.pptx)

  [System-Defined Device Setup Classes available to vendors](http://msdn.microsoft.com/en-us/library/ff553426(v=vs.85).aspx)

  [Device Management and Installation Operations Guide](http://technet.microsoft.com/en-us/library/cc753759(WS.10).aspx)

  [GP Preferences: Add a new printer, set as default](http://blogs.technet.com/b/grouppolicy/archive/2009/06/24/gp-preferences-set-a-default-printer.aspx)