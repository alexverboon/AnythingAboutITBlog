Instead of opening several windows, here’s an easy way to get a list of installed QFE’s. simply open a command prompt and type:

  **WMIC QFE **

  or

  **WMIC QFE get caption,hotfixid,installedon**

  [
![image](images/image_thumb10.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image10.png) 

  or if you are looking for a specific update, enter the following command:

  **WMIC QFE | find “958559”**

  where 958559 relates to the MS KB number. If the QFE is installed, it will be listed. 

  [
![image](images/image_thumb11.png)
](https://www.verboon.info/wp-content/uploads/2009/09/image11.png) 

  Related posts:

  [3 seconds to get system serial number](https://www.verboon.info/index.php/2008/09/3-seconds-to-get-system-serial-number/)