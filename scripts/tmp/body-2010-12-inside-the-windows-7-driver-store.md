The driver store is a trusted location of inbox and third-party driver packages. This means that before a driver can be installed it must first be injected into the driver store, this process is called staging. Today I want to take a closer look at what is inside the driver store specifically the drivers that are included within Windows 7. The driver store is located under C:\Windows\System32\Driverstore.

To get list of all drivers installed (staged) within the driver store, open an elevated command prompt and enter the following command:

[sourcecode language="plain"]
Dism /online /get-drivers /all /format:table >drivers2.txt
[/sourcecode]

[
![2010-12-28 14h59_42](images/2010-12-28-14h59_42_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-14h59_42.png)

Note that if you do not specify the /all option, only the 3rd party (non-inbox) drivers are listed. What the command actually does is collecting all the information from each INF file that is stored within each driver package folder within the driver store.

[
![2010-12-28 15h10_27](images/2010-12-28-15h10_27_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-15h10_27.png)

When organizing the data from drivers2.txt within Excel we get the following overview.

[
![2010-12-28 15h21_02](images/2010-12-28-15h21_02_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-15h21_02.png)

## **Is my device supported by the Windows 7 in-box drivers?**

The primary goal of the in-box drivers is to allow users install Windows 7 so that basic functionality can be provided. This means that critical boot drivers as well as network and display drivers for most mainstream hardware is provided. Once the user can get online, additional drivers can be installed via Windows Update or by downloading an OEM driver installation package. In an Enterprise environment the drivers for the known supported hardware should of course already be installed at deployment time.

From the above table we see that there are 107 in-box drivers for Printers. So does windows 7 only support 107 different printers out of the box? No, because each printer driver can support multiple devices.

[
![2010-12-28 15h50_40](images/2010-12-28-15h50_40_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-15h50_40.png)

From the above list we can see that for HP Printing devices there are 4 INF files included within the in-box drivers.

[
![2010-12-28 15h46_15](images/2010-12-28-15h46_15_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-15h46_15.png)

To get the full detail of a particular driver and the devices it supports, run the following command from an elevated command prompt.

[sourcecode language="plain"]
Dism /online /get-driverinfo /driver: <path to driver inf file>
[/sourcecode]

To get the full details for the above 4 listed HP printer drivers we run the following commands

[sourcecode language="plain"]

Dism /online /get-driverinfo /driver:C:\Windows\System32\DriverStore\FileRepository\prnhp002.inf_x86_neutral_e6daa9c39ac001a3\prnhp002.inf >hp1.txt

Dism /online /get-driverinfo /driver:C:\Windows\System32\DriverStore\FileRepository\prnhp003.inf_x86_neutral_8685826a5ca37e6b\prnhp003.inf >hp2.txt

Dism /online /get-driverinfo /driver:C:\Windows\System32\DriverStore\FileRepository\prnhp004.inf_x86_neutral_95288ae6f32f1fe7\prnhp004.inf >hp3.txt

Dism /online /get-driverinfo /driver:C:\Windows\System32\DriverStore\FileRepository\prnhp005.inf_x86_neutral_9307c57b91a7985e\prnhp005.inf >hp4.txt
[/sourcecode]

If now we open one of the output files we can see all the different HP printers the driver supports.

[
![2010-12-28 15h58_00](images/2010-12-28-15h58_00_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-15h58_00.png)

If we want to get this information into a nice Excel sheet, simply run the following command which extracts just the lines that start with “Description”.

[sourcecode language="plain"]

FINDSTR /C "Description" c:\temp\drvstore\hp*.txt >>c:\temp\drvstore\hpprinters.log
[/sourcecode]

Then open the hpprinters.log and within the Text Import wizard select that this is a delimited file. I won’t go into the detail here, assume that you have some experience with importing text data within Excel. 

[
![2010-12-28 16h10_14](images/2010-12-28-16h10_14_thumb.png)
](https://www.verboon.info/wp-content/uploads/2010/12/2010-12-28-16h10_14.png)

Conclusion the Windows 7 in-box drivers support 209 HP Print devices. Okay, now that we know how to get the data, let’s get it for everything” that is in the driver store. Instead of running the command manually for each INF file you can run the following command:

[sourcecode language="plain"]

FOR /R C:\WINDOWS\SYSTEM32\DRIVERSTORE\FILEREPOSITORY %%i IN (*.INF)  DO dism /online /get-driverinfo /driver:%%i >>c:\data\all.txt
[/sourcecode]

The all.txt file will have detailed driver information for any INF file found within the driver store. According to the information I dumped from a clean Windows 7 Enterprise 32 bit installation the Windows 7 in-box drivers support approx. 19’403 devices. I guess that should help most users to get their Windows 7 up and running.