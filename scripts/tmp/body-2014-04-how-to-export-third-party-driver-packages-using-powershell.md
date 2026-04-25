Windows 8.1 Update introduces a new cmdlet that allows you to export third-party drivers that are located within the driver store of a Windows client. 

```
$ExpDrv = Export-WindowsDriver -Online -Destination c:\temp\3rdpartydrivers 

```

The result, all drivers exported into the provided destination directory

[
![2014-04-04_21h36_47](images/2014-04-04_21h36_47_thumb.png)
](https://www.verboon.info/wp-content/uploads/2014/04/2014-04-04_21h36_47.png)

Now we have a whole bunch of folders, but what drivers did we actually export?

```

$ExpDrv | Select-Object ClassName, ProviderName, Date, Version | Sort-Object ClassName

```

[
![2014-04-04_21h40_00](images/2014-04-04_21h40_00_thumb.png)
](https://www.verboon.info/wp-content/uploads/2014/04/2014-04-04_21h40_00.png)

For more information read the What’s new in DISM article [here](http://technet.microsoft.com/en-us/library/dn419776.aspx)