This morning at the [GP Answers community forum](http://www.gpanswers.com/community/) someone asked how to configure the Start Menu option “Highlight newly installed programs” via GPO. As it turns out this setting is not included within the out of the box GPO templates. Since I have a few days off I thought let’s give a little help here. 

  But before jumping into the custom ADMX template, let’s quickly look at the configuration setting itself. When installing an application the new created shortcut within the Start Menu is highlighted. 

  [
![2011-04-21 14h03_10](images/2011-04-21-14h03_10_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-21-14h03_10.png)

  This setting can be customized manually by right clicking on the Start Menu logo, select properties, then select the Start Menu tab and then select customize. 

  [
![2011-04-21 14h05_58](images/2011-04-21-14h05_58_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-21-14h05_58.png)

  At the registry level the following registry settings are made:

  HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced

  Start_NotifyNewApps

  When the value is 0 this setting is disabled. When the value is 1 this setting is enabled. 

   

  Now let’s have a look at the custom ADMX file I’ve created. First copy the ADMX and ADMXL files into the Policydefinitions folder. The ADMX file goes straight into the folder C:\Windows\PolicyDefinitions and the ADML files must be copied into the en-US subfolder. Once you have tested this on a local machine consider copying these files into your GPO Central Store. 

  You will find the custom GPO Template under Administrative Templates “**Start Menu Customizations**” Note that this is not a real GPO setting, but rather a preference. 

  [
![2011-04-21 14h08_16](images/2011-04-21-14h08_16_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/04/2011-04-21-14h08_16.png)

  The Start Menu customization GPO template can be downloaded from [here](https://www.verboon.info/fun/StartmenuCustomization_admx.zip)