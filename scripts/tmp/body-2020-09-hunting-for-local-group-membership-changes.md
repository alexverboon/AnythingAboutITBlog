Hello there,

A couple of days ago, someone in a forum asked whether it would be possible to detect changes to the local administrator's group using Microsoft Defender Advanced Threat protection. Before I continue why would you want to monitor such changes? Well here is what comes to my mind:

- An attacker tries to maintain persistence, creates an account, and adds it to the local administrator's group. [T1136.001 - Create Account: Local Account](#)
- A user obtained a LAPS password and misuses the temporary permission to add their own account to the local administrative group
- Local IT support works on fixing an issue, adds the user to the local administrator's group, but forgets to remove the account after the issue is being resolved
- In the days of COVID19, IT sometimes is in a rush and does anything to enable their users to work, a user is quickly added to the local administrators or remote desktop users group to enable them to use Remote Desktop Services (RDP)

Now the good news is, yes changes to local groups can be detected. As you can see from the screenshot below Microsoft Defender ATP exposes **UserAccountAddedToLocalGroup** ActionType in the [DeviceEvents](#) table.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL1.png)

Let us take a look at on particular event where the local Administrators group was changed. The **Timestamp** indicates the time of the event, the **DeviceName** describes the computer name of the device where the event happened. The **AccountName** field describes the name of the group that was changed, the **AccountSID** is the SID of the local group. The **initiatingProcessAccountName** indicates who made the change, in this case it was the device itself while processing group policy, that is why the initiatingProcessAccountName matches the device name, if the change was made by let's say another user or administrator, we would see the local or domain account name here, the **AdditionalFields** field contains the information about the SID of the user that was added.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL2.png)

Great, so we have a way to monitor changes to local groups, now let us continue to change the query a bit , so that we just return the data we actually need. First, we extract the SID of the user account from the **AdditionalFields** that was added to the group, the **AccountName** represents the local group name, so we call this field LocalGroup, the **AccountSID** represents the SID of the modified local group, so call this field LocalGroupSID.  The **InitiatingProcessAccountName** refers to who made the change, so we call this field Actor.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL3.png)DeviceEvents

| where ActionType == 'UserAccountAddedToLocalGroup'

| extend AddedAccountSID = tostring(parse_json(AdditionalFields).MemberSid)

| extend LocalGroup = AccountName

| extend LocalGroupSID = AccountSid

| extend Actor = trim(@"[^\w]+",InitiatingProcessAccountName)

| project Timestamp , DeviceName, AddedAccountSID , LocalGroup , LocalGroupSID , Actor
We now have a clear view of users that were added to a local group on the device, but we only have the SID of the user that was added, if we want to know the user account name we would have to lookup the SID of the user on the local device or within active directory.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL4.png)

On device lclient04 we see that the user with SID S-1-5-21-3227082263-3185695827-1030547828-1005 was added to the local administrators group, so if we lookup the SID we see that it was the local account *Jane* that was added.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL5.png)![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL6.png)

On device client01.corp.net we see that the user with SID S-1-5-21-2681622853-4232236494-3008232168-12101 was added to the local administrators group.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL7.png)

Doing manual SID lookups is not very efficient, so let us extend our hunting query a bit to enrich the output with the actual username of the user that was added. Let us first look at the local user accounts. I must add here that this will only work if Defender ATP has a log of the local created or modified user in its log history.  We first define the variable *NewUsers* and store the information of new or changed local user accounts and the join the information with the query that looks for group changes.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL8.png)

There we go, we now get the actual username back, it was Jane that was added. Now let us take a look at domain accounts that were added to a local group. I must mention here that this query will only work if you run the advanced hunting query from the Microsoft security portal i.e. MTP because that one exposes the schema [**IdentityInfo**](#) that provides us with Account information from various sources, including Azure Active Directory.

We define the variable *ADAZUsers* and store the identityinformation from AD/AzureAD.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL9.png)

You notice that the above query returns user additions to any local group, if you want to limit the query to the local administrators group only, uncomment the following line, we use the SID so that the query will also work in global environments with different languages.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL10.png)

See: for a [list of Well-known security identifiers in Windows operating systems](#) to find the SID of other local groups.

As mentioned earlier if the actor has the device name, the action was performed by the device itself, meaning it was an action such as a Group Policy Preference setting that added the user.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL11.png)

To exclude these types of actions simply add the following line to the query. This will exclude any events that have the device name in the Actor field.

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL12.png)

Now,  who are the most active Actors (administrators) making local group membership changes?

![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL13.png)

Want try it out yourself, here's the AH query to copy paste into your own environment: [https://gist.github.com/alexverboon/ad59c3b0f8bbace142bd3acaac5b6ad9](#)

And for all of you who do not have Microsoft Defender ATP, but use Microsoft Endpoint Configuration Manager, you can also query the security event log for local group membership changes with CMPivot by querying the security log for EventID [4732](#)![](https://www.verboon.info/wp-content/uploads/2020/09/090620_0816_HuntingforL14.png)

I hope you enjoyed this blog post, as always, feedback, comments are welcome

Alex