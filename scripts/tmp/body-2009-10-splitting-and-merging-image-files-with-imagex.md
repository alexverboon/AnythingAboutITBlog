ImageX is a command-line tool for capturing, modifying and applying file based disk images. ImageX is included within the Windows Automated Installation Kit. 

  In this post I want to focus on the functionality provided by ImageX to split and merge image files. So why would you want to split and merge image files? Well think of the following scenarios:

     
- Your image is too big to fit on one DVD and using Dual Layer DVD media is not an option.     
- Network related limitations to transfer large files    
- Merge image files provided on multiple DVDs for network based deployment 

  For the purpose of writing this article, I prepared a simple folder structure to demonstrate the capture, split and merge process. 

              [
![image](images/image_thumb2.png)
](https://www.verboon.info/wp-content/uploads/2009/10/image2.png)                             
- The folder “Output1” is used to store the initial captured image file which contains the data stored within the “source” folder. The source folder was filled with some wallpapers located in C:\Windows\Web\Wallpaper             
            
- The folder “Output2” is used to store the splitted image files.              
            
- The folder “Output2” is used to store the merged image file created from the splitted image files that are stored in folder “Output2”.          

                  

  To run the following commands you must open the “Deployment Tools command prompt” which gets automatically added to your start menu when having installed the WAIK. Note that all commands must be run with Administrator privileges. 

   **Image Capture**

  Use the following command to capture the first image:

  imagex /capture c:\data\splitmerge\source c:\data\splitmerge\output1\splitmerge.wim "splitmerge" /COMPRESS maximum

  For validation purposes, I talk about that later, we also produce an image info file using the following command:

  imagex /info /xml c:\data\splitmerge\output1\splitmerge.wim > info1.xml

  **Image Split**

  Now we are going to split the previously created splitmerge.wim file. Since we are dealing with a rather small image file, the split is set at 20 MB. 

  imagex /split c:\data\splitmerge\output1\splitmerge.wim c:\data\splitmerge\output2\splitmerge.swm 20

  and again we create an image info file. 

  imagex /info /xml c:\data\splitmerge\output2\splitmerge.swm > info2.xml

  **Image Merge**

  Finally we are going to merge the previously splitted image file back into a single image file. 

  imagex /ref c:\data\splitmerge\output2\splitmerge*.swm /check /export c:\data\splitmerge\output2\splitmerge.swm 1 c:\data\splitmerge\output3\splitmerge.wim "splitmerge" /COMPRESS maximum

  and create the image info file

  imagex /info /xml c:\data\splitmerge\output3\splitmerge.wim > info3.xml

  **The Output**

  If all worked fine, the following files should be present:

     
- C:\DATA\splitmerge\output1\splitmerge.wim    
- C:\DATA\splitmerge\output2\splitmerge.swm, splitmerge2.swm and depending on the size of the source folder your might also get an additional splitmerge3.swm    
- C:\DATA\splitmerge\output3\splitmerge.wim    
- C:\DATA\splitmerge\info1.xml    
- C:\DATA\splitmerge\info2.xml    
- C:\DATA\splitmerge\info3.xml 

  **Checking data integrity**

  When comparing the file size of the splitmerge.wim stored in c:\data\splitmerge\output1 with splitmerge.wim stored in c:\data\splitmerge\output3 you will probably notice that the size in bytes differs. The same applies for the total size of the swm files stored in c:\data\splitmerge\output2. 

  [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2009/10/image3.png) 

  Well, forget about these file/folder sizes, to ensure that your final wim file contains the exact same data as the initial wim file, we’ll take a look at the previously created image info files. 

  [
![image](images/image_thumb4.png)
](https://www.verboon.info/wp-content/uploads/2009/10/image4.png) 

  All of the 3 image info files have the same value stored for:

  <FILECOUNT>43</FILECOUNT>   
<TOTALBYTES>41339064</TOTALBYTES>

  Happy imaging !

  Related articles:

  [Getting your OS Restore DVD to work with large image files](https://www.verboon.info/index.php/2009/09/getting-your-os-restore-dvd-to-work-with-large-image-files/)