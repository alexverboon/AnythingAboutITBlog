Ever had that issue that you wanted to enter the VMWARE BIOS, but you simply don't made it because the VMWARE session boots too fast ?

Add the following line to your *.vmx file. 

bios.bootDelay = "3000"

[http://communities.vmware.com/docs/DOC-1201](http://communities.vmware.com/docs/DOC-1201)¨