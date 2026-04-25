As [announced](http://blogs.technet.com/b/office_resource_kit/archive/2013/09/27/setting-the-office-theme-using-group-policy.aspx) on the Office IT Pro blog a few days ago, there are updated [Office 2013 administrative templates](http://www.microsoft.com/en-us/download/details.aspx?id=35554) and Office updates that allow an administrator to pre-configure the Office 2013 Theme. 

 The term pre-configure is important, because the setting only applies as long as the user has not changed the theme before themselves via the GUI. When configuring the Theme via Group Policy, User Configuration \ Administrative Templates \ Microsoft Office 2013 \ Global Options Customize \ Default UI Theme, the setting is stored under HKEY_CURRENT_USER\Software\Policies\Microsoft\office\15.0\common\default ui theme

 0 = White, 1 = Light grey, 2 = Dark Grey. 

 [
![2013-09-30_20h44_13](images/2013-09-30_20h44_13_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/09/2013-09-30_20h44_13.png)

 Users can change the Theme settings via File, Options, General or just File, Account. 

 [
![2013-09-30 21h30_14](images/2013-09-30-21h30_14_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/09/2013-09-30-21h30_14.png)

  [
![2013-09-30 22h53_15](images/2013-09-30-22h53_15_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/09/2013-09-30-22h53_15.png)

 As soon as the user manually configures the Theme, the setting is stored under:

 HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Common\UI Theme

 0 = White, 1 = Light grey, 2 = Dark Grey. 

 You would hope that when deleting the above key, the Group Policy setting would kick in, but unfortunately that is not the case, to achieve that you have to delete the identities key located under [HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Common\Roaming\Identities

 Once i had deleted that key, the GPO setting would kick in, but to be honest, i have no clue what else might have been stored underneath that identifies key. More details on that [here](http://www.edugeek.net/forums/office-software/120952-force-colour-scheme.html). 

 Now as we speak about Theme settings, there is another Setting and Group Policy that could be of interest. If have signed in with a Microsoft Live Account and use multiple devices, you will notice that the Theme setting roams across these devices. To prevent this from happening, users can enable the “Always use these values regardless of sign-in to Office” setting. 

 [
![2013-09-30 23h11_30](images/2013-09-30-23h11_30_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/09/2013-09-30-23h11_30.png)

 Administrators can prevent the Theme settings (and more)  from roaming via User Configuration \ Administrative Templates \ Microsoft Office 2013 \ Global Options Customize \ Allow Roaming of all user customizations. Note that this setting also prevents other settings such as the Access Toolbar and Ribbon settings from roaming. 

 [
![2013-09-30 23h16_31](images/2013-09-30-23h16_31_thumb.png)
](https://www.verboon.info/wp-content/uploads/2013/09/2013-09-30-23h16_31.png)