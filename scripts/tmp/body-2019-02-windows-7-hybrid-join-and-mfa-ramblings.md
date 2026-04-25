Today I ran into an issue where Windows 7 would not hybrid join as expected. Before going into the details, for those who might not be aware like Windows 10 and Server 2016, you can also hybrid join down-level devices. The functionality is of course not built into Windows so you need to install the "[Microsoft Workplace Join for non-Windows 10 computers](https://www.microsoft.com/en-us/download/details.aspx?id=53554)" software.

One reason why you want to hybrid join Windows 7 devices is Conditional access. Let's assume you plan to introduce Conditional access for your users where you want to enforce MFA when using a non-corporate device.

![](images/020519_1934_Windows7Hyb1.png)

The only way this is going to work in a mixed environment where your users use both Windows 10 and Windows 7 is to also hybrid-join Windows 7 devices, otherwise users logging on to Windows 7 devices would be required to authenticate through MFA.

Okay, now back to my ramblings, while I had this all nicely working in my lab, today while working with a client, we ran into an issue where the hybrid join failed. I asked myself what's different? Of course, in IT there are many things that work here but not there. Anyway, since at the same time we're also doing some work on enabling MFA and SSPR I had a suspicion where the problem could be. I went back to my lab, configured a few things and was able to get the same error.

![](images/020519_1934_Windows7Hyb2.png)

Within the Event log the error is as shown below.

![](images/020519_1934_Windows7Hyb3.png)

All prerequisites were validated, so none of the issues described here [Troubleshooting hybrid Azure Active Directory joined down-level devices](https://docs.microsoft.com/en-us/azure/active-directory/devices/troubleshoot-hybrid-join-windows-legacy) seemed to apply.

So what's the issue? Well it turned out that the user who logged in was in a **pending MFA registration state**,

![](images/020519_1934_Windows7Hyb4.png)

meaning that MFA registration was enforced through Azure Identity Protection, but the user did not complete the registration yet.

![](images/020519_1934_Windows7Hyb5.png)

Another location where MFA registration can be enforced / requested is within AzureAD Password reset.

![](images/020519_1934_Windows7Hyb6.png)

Once I completed the MFA registration and tried to hybrid join the Windows 7 device manually again.

C:\Program Files\Microsoft Workplace Join>AutoWorkplace.exe /i

The hybrid join completed successfully.

![](images/020519_1934_Windows7Hyb7.png)

Within the Event log the result is as shown below.

![](images/020519_1934_Windows7Hyb8.png)

And within AzureAD we get the status as well.

![](images/020519_1934_Windows7Hyb9.png)

Conclusion, if you're having issues with Windows 7 hybrid join and Event ID 404 check whether the user has completed MFA registration.

I hope you enjoyed the post and it's going to be of help for someone who runs into this particular issue.

Happy joining.

Alex