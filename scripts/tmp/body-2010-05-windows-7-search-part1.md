Federated Search is one of the new features introduced with Windows 7. A few weeks ago I wrote another post about the [Windows 7 Search Provider](https://www.verboon.info/index.php/2010/04/windows-7-search-provider/) and demonstrated how to use a search connector that allows searching web content from within the Windows Explorer. Today I want to demonstrate how to extend Windows Search to find content on a remote network location. 

  To allow users searching content that is stored on a remote File Server, Windows Search must be enabled. On Windows Server 2008 and 2008 R2 Windows Search can be configured through the File Services Role.    
[
![image](images/image_thumb6.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image6.png) 

  Now let’s make sure our Shared folder is included within the Search Index. The Search Index can be configured through the Control Panel Indexing Options. Select Modify to in/exclude content. 

  [
![image](images/image_thumb7.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image7.png) 

  On the server side we’re done now, so let’s move over to the Windows 7 client. Open the Windows Explorer and navigate to the Libraries. 

  [
![image](images/image_thumb8.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image8.png) 

  Create a new Library called “CorpData”. 

  [
![image](images/image_thumb9.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image9.png) 

  Select “Include a Folder”, then navigate to the Remote Server Share

  [
![image](images/image_thumb10.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image10.png) 

  [
![image](images/image_thumb11.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image11.png) 

  Now let’s start a search for anything about “VDI”. 

  [
![image](images/image_thumb12.png)
](https://www.verboon.info/wp-content/uploads/2010/05/image12.png) 

  You see, it’s that easy. In an upcoming post I will focus on the manageability of Windows Search in an Enterprise environment.