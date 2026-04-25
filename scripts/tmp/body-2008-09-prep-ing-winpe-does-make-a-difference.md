When creating WinPE 2.0 boot images, make sure you run the [PEImg](http://technet.microsoft.com/en-us/library/cc749161.aspx) /prep command against your boot.wim as it does make a significant difference in sze as shown in the table below:

Bootable ISO file with WiinPE 2.0
Size in MB

boot.wim prepped
146 mb

boot.wim not prepped
203 MB

Considering this all is loaded into memory, you might want to make sure to reduce the size of the boot.wim to an absolute minimum.