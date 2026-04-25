Yesterday evening I looked at some of the new features within Windows 7. So at some stage I wanted to see Applocker running. I spend about an hour reviewing my settings, checking GPO processing until I went back to the documentation, just to find out that little sentence at the very bottom of that page..... "***At least one Windows Server 2008 R2 domain controller is required to host the Applocker rules***".

Once more... [RTFM ](http://en.wikipedia.org/wiki/RTFM):-) Windows 2008 R2 download in progress......

**UPDATE 20.11.2009**

Source:

*[http://www.infoworld.com/d/windows/dont-upgrade-windows-server-2008-r2-until-you-read-785?page=0,1](http://www.infoworld.com/d/windows/dont-upgrade-windows-server-2008-r2-until-you-read-785?page=0,1)*

AppLocker: This is a new feature in Windows 7 and Windows Server 2008 R2 that replaces Software Restriction Policies. This features provides the ability to control how (or if) users can access .exe files, scripts, .msi files, and DLLs. You essentially define rules that can be assigned to users or security groups that are based on an applications digital signature, including the publisher, product name, file name, and/or file version. **And the good news is that AppLocker's Group Policy foundation requires no upgrade of domain controllers. Existing Windows Server 2003 and 2008 servers can host AppLocker policies.**