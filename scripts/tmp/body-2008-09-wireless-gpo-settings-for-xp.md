In the last 2 days i have spend some time in getting Wireless GPO settings applied to a Windows XP client.

I was actually about to describe what i have done to get it working, but just noticed that there is already a similar article published on [Technet Magazine](http://technet.microsoft.com/en-us/magazine/cc162468.aspx) related to Vista, so i am not going to rewrite things in detail again.

[*The Cable Guy Wireless Group Policy Settings for Windows Vista*](http://technet.microsoft.com/en-us/magazine/cc162468.aspx)

Maybe interesting to know is that for Windows XP you don't need to update the AD schema to get the Wireless GPO settings to work.

Unless you are running SP3 already, install [KB917021](http://support.microsoft.com/kb/917021) on top of Windows XP SP2.

To create the GPO settings itself, use a Windows Vista SP1 Admin console with RSAT installed so that you have the latest GPMC console available.

Enjoy !