When creating objects in Active Directory you can set a flag that prevents accidental deletion of an object. 

 While this setting is visible in the UI by default when creating an Organizational Unit, for other objects like Users, Groups and Computers, this flag is not set by default and can only be set if the Advanced Features are enabled within the Active Directory Users and Computers Console. 

 [
![image](images/image-thumb2.png)
](https://www.verboon.info/wp-content/uploads/2009/06/image2.png) 

 So assume you would create some important user accounts that are used for critical back-end systems, you should consider enabling the "Protect object for accidental deletion" flag. 

 [
![image](images/image-thumb3.png)
](https://www.verboon.info/wp-content/uploads/2009/06/image3.png) 

 Once you have this flag set, anyone who would try to delete the user account would receive a message as shown below. 

 [
![image](images/image-thumb4.png)
](https://www.verboon.info/wp-content/uploads/2009/06/image4.png)