Good day everyone. Today I would like to share with you the Group Policy Xtended PowerShell module that i’ve written recently. Histrocially I used to have various cmdlets stored in individual files and ran them when needed, I also shared them among my peers and with the public via my blog and the [Microsoft Script repository](https://gallery.technet.microsoft.com/scriptcenter). The challenge with this approach is that it’s hard to ensure eveyone has the latest versions of the cmdlets  available and that when someone needs a cmdlet that he’s actually able to find it or actually knows that there’s one available. 

 So I’ve decided to put the Group Policy management cmdlets that I created in the course of time into a PowerShell module. Not only does this solve the challenge of sharing cmdlets in an effective way, but I also noticed that I raised the bar for my  code writing and code documentation. 

 The GroupPolicyXtended Module currently provides the following cmdlets.

  
-  Get-GPEventByCorrelationID
This function retrieves Group Policy event log entries filtered by Correlation ID from the specified computer

Read [this](https://blogs.technet.microsoft.com/heyscriptingguy/2015/02/01/weekend-scripter-use-powershell-to-troubleshoot-group-policy-part-2/) article to learn more about this cmdlet 
-  Get-GPProcessingtime
The Get-GPProcessingtime cmdlet gets Group Policy processing time for the user and computer related Group Policies that are processed on the specified computer(s). 

Read [this](https://blogs.technet.microsoft.com/heyscriptingguy/2014/08/24/weekend-scripter-use-powershell-to-troubleshoot-group-policy/) article to learn more about this cmdlet 
-  Set-GPLogging
The Set-GPLogging cmdlet enables or disables Group Policy Service or Group Policy Preferences logging.  
-  Get-GPLogging
The Get-GPLogging cmdlet retrieves information about the Group Policy Service Debug or Group Policy Preference logging configuration set on a computer.  
-  Update-GroupPolicyXtended
Run this cmdlet to update the module to the latest version. 

   To install the module, open a PowerShell session and paste the below code, then run it.  (all on one line) $wc=New-Object System.Net.WebClient;$wc.UseDefaultCredentials=$true;iex $wc.DownloadString([https://raw.githubusercontent.com/alexverboon/posh/master/GroupPolicy/install-GroupPolicyXtended.ps1](https://raw.githubusercontent.com/alexverboon/posh/master/GroupPolicy/install-GroupPolicyXtended.ps1)) The code is stored on GitHub here: [https://github.com/alexverboon/posh/tree/master/GroupPolicy](https://github.com/alexverboon/posh/tree/master/GroupPolicy) The cmdlets included in this module  assume that PowerShell remoting is enabled, furthermore when running the cmdlets against the local client, the PowerShell session should be launched with administrative rights.  As always, i welcome feedback, thoughts, improvement ideas.  Have a great day! Alex