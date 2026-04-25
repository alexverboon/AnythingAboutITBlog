When using WLAN on a day to day basis we can see the WLAN signal strength via the Windows User Interface as shown in the screenshot below. 

  [
![2011-03-15 20h33_47](images/2011-03-15-20h33_47_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-20h33_47.png)

  But there are other ways, and yes the approach might appear a bit inconvenient, but basically I want to demonstrate the Power of the Windows Event log. First open the Windows Event viewer (eventvwr.msc) and then within the View Menu enable the Show **Analytic and Debug Logs** option. 

  [
![2011-03-15 21h05_40](images/2011-03-15-21h05_40_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-21h05_40.png)

  Then navigate to the WLAN-autoconfig event log. Since we enabled the Analytic and Debug logs option, beside the Operational log we also see the Diagnostic log. 

  [
![2011-03-15 21h15_42](images/2011-03-15-21h15_42_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-21h15_42.png)

  The Diagnostic event log by default is not enabled, so first we have to enable it. (Right mouse-click, Properties)

  [
![2011-03-15 21h19_22](images/2011-03-15-21h19_22_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-21h19_22.png)

  As soon as we have the Diagnostics mode enabled we should see events coming in. To enforce things a bit simply disable and enable your Wireless connection using your vendors Wireless Connection Software or hardware button on the notebook. 

  When the following Event was logged I was sitting near our Wireless Access Point and got a Link Quality result of **81**. 

  [
![2011-03-15 21h31_31](images/2011-03-15-21h31_31_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-21h31_31.png)

  I then moved to the basement and got a Link Quality result of **38**. 

  [
![2011-03-15 21h22_18](images/2011-03-15-21h22_18_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-21h22_18.png)

  And finally placing the laptop right next to the Wireless Access Point resulted in a Link Quality of **97**. 

  [
![2011-03-15 21h52_11](images/2011-03-15-21h52_11_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/03/2011-03-15-21h52_11.png)

  Note! when you’re done, don’t forget to disable the logging.