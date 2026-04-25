Today I worked on something where I needed a Windows 8 client that does not have a system reserved partition. To avoid a fresh installation of Windows I decided to re-use one of my Virtual Machine templates and apply the process described below. 

  I’m sure I’m not the first one that blogs about this but I’ve seen so many lengthy  and over-complicating descriptions (including instructions of loading the registry, use of 3rd party tools and rescue discs) that I decided to write this down anyway, even if it’s just for YOU who just stumbled over this blog post. 

  In case you plan to do this on a system with your or someone else’s data stored, I recommend making a backup BEFORE running the below described tasks. 

  **Step 1**  Open the Disk Management Console and get an overview of the current disk layout. 

  ..[
![image](images/image_thumb10.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image10.png)

  **Step 2**  Now boot the VM (or physical machine) from the Windows Installation media (USB/DVD). Once you see the Windows Setup menu, press SHIFT+F10 to open the command prompt. 

  [
![image](images/image_thumb11.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image11.png)

  **Step 3** At the command prompt type DISKPART, then type **LIS DIS**, you should then get something that looks like this

  [
![image](images/image_thumb12.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image12.png)

  **Step 4** Note down the Disk number and then type **SEL DIS <Disk#>** in this case **SEL DIS 0**

  **Step 5** Then type **LIS PAR** to get a listing of the partitions

  [
![image](images/image_thumb13.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image13.png)

  **Step 6** Note down the Partition Number and then enter **SEL PAR <Partition#>** in this case **SEL PAR 1**

  **Step 7** Now type **DEL PAR OVERRIDE** You should get the following result. 

  [
![image](images/image_thumb14.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image14.png)

  **Step 8** Type **SEL PAR 2** confirm with enter and then type **ACTIVE**, when you get a result as shown below, type **EXIT** to leave Diskpart. 

  [
![image](images/image_thumb15.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image15.png)

  So far so good, no rocked science, but at this point we must rebuild the BCD because it was stored on the partition we just deleted. So let’s do that now. And for that there is a simple command called [BOOTREC](http://support.microsoft.com/kb/927392), so no reason to go crazy by manually fixing the BCD store etc. . 

  **Step 9** At the command prompt type **BOOTREC /REBUILDBCD**

  [
![image](images/image_thumb16.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image16.png)

  When the above command has completed successfully, you can reboot the system and if all worked fine it boots into Windows. When opening the Disk Management Console you’ll see that the system reserved partition is gone, BUT there’s now unallocated space and unfortunately it’s not possible with Windows Build in tools to bring this space back to the system partition as that one does not allow to extend it’s partition. But we’re talking about 350 MB only here anyway.  

  [
![image](images/image_thumb17.png)
](https://www.verboon.info/wp-content/uploads/2012/04/image17.png)

  To avoid the creation of the system reserved partition during a fresh install you can follow the steps described [here](http://www.mydigitallife.info/hack-to-remove-100-mb-system-reserved-partition-when-installing-windows-7/) or if you’re using the Microsoft Deployment Toolkit add DoNotCreateExtraPartition=YES to the customsettings.ini.