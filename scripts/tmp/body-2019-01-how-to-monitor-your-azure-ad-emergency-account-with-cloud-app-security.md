As a best practice you should have at least one or two emergency accounts in your Azure Active Directory. You would use these accounts in the event where due to a configuration mistake you inadvertently locked yourself out of the Azure Active Directory or when for some reason you can't use MFA that should be enabled on all administrative accounts.

For more guidance about creating emergency accounts I suggest you read [Manage emergency access accounts in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-emergency-access).

The article recommends that at least for one of these emergency accounts you do not enable Multi-Factor Authentication, this for when there is a cell-network outage that prevents sending you phone calls or text messages. Furthermore, the article recommends [conducting regular reviews](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-emergency-access) of the Azure AD sign-in and audit logs.

The emergency account that has no Multi-Factor enabled is less secure and therefore I want to be immediately informed whenever there is activity with that account.  With Microsoft Cloud App Security, you can easily setup monitoring for these accounts.

Open the Microsoft Cloud App Security Portal and select Control, **Policies**.

![](images/010919_2111_Howtomonito1.png)

Then select **Create Policy, Activity Policy**

![](images/010919_2111_Howtomonito2.png)

Provide a Name, Description for the Policy, then define the Policy Severity and Category. Next define the Filter for the Policy and set that to "**Single Activity**"

![](images/010919_2111_Howtomonito3.png)

We then need to define the filter criteria, which is in simple words "Alert whenever the specified emergency account is involved in any of the following actions, Logon, Logon Failure, Enable MFA)"

The picture below illustrates the filter I have defined:

![](images/010919_2111_Howtomonito4.png)

The following Activity Types are enabled:

 	
- Failed logon
 	
- Logon on

And finally, we define what to do with the alert, in the example below I just send an e-mail and do not take any governance actions.

![](images/010919_2111_Howtomonito5.png)

For demonstration purposes I have logged on with the account, caused a failure by providing the wrong password etc. Almost instantly alerts were triggered.

![](images/010919_2111_Howtomonito6.png)

![](images/010919_2111_Howtomonito7.png)

![](images/010919_2111_Howtomonito8.png)

And finally, don't forget to also add that emergency account that should not have MFA enabled, to the Conditional Access Baseline Policy that will soon enforce MFA for all administrative roles.

![](images/010919_2111_Howtomonito9.png)

Hope you found this helpful. Comments, feedback is always welcome.

Alex