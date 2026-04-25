To get a list of all users that belong to a given role, the Microsoft Azure Active Directory module has a cmdlet Get-MsolRoleMember, however to run the cmdlet you must use the RoleObjectId parameter and provide a value.  The possible values for RoleObjectId can be retrieved by running the Get-MsolRole cmdlet.

To simplify this, I wrote the Get-MsolRoleMemberDetails cmdlet.  As you can see from the below screenshot, the list of available roles is dynamically populated.

[
![image](images/image_thumb.png)
](https://www.verboon.info/wp-content/uploads/2016/11/image.png)

For this cmdlet I am using Dynamic Parameters as explained in great detail [here](https://blogs.technet.microsoft.com/heyscriptingguy/2014/03/21/use-dynamic-parameters-to-populate-list-of-printer-names/)  by Ed Wilson, the Microsoft Scripting Guy.

 

```

```