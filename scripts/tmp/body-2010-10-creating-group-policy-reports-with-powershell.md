I’ve had this on my “must do some hands on” list for months, finally found some time to play a bit with the new [PowerShell Group Policy CmdLets](http://technet.microsoft.com/en-us/library/ee461027.aspx) that where introduced with Windows 7. For today i decided to work with the [Get-GPO](http://technet.microsoft.com/en-us/library/ee461059.aspx) and the [Get-GPOReport](http://technet.microsoft.com/en-us/library/ee461057.aspx) CmdLets.

The Get-GPO CmdLet allows you to list one or all GPOs that exist in a domain. If you know the name and want to know when it was last modified, simply type Get-GPO <Group Policy Name>

[
![image](images/image_thumb15.png)
](https://www.verboon.info/wp-content/uploads/2010/10/image15.png)

The Get-GPOReport CmdLet allows you to create a detailed Group Policy report and save it in HTML or XML format. To generate a report that contains all GPOs with all its settings, simply run the following command:

[sourcecode language="powershell"]   get-gporeport -all -path c:\gporeports\allgpo.html -reporttype HTML [/sourcecode]

Below are two scripts I modified / created during my first hands-on with the Group Policy CmdLets.

The first script **GenerateGroupPolicyReports.ps1** is basically a copy from [Get-XMLForEachGPO.ps1](http://gallery.technet.microsoft.com/ScriptCenter/en-us/98f56f49-c78e-4563-baa1-d39a53a41529) that i found on TechNet Script Center. I’ve just changed the output type from XML to HTML. The script produces a Group Policy report for each GPO found in the domain.

**GenerateGroupPolicyReports.ps1**

[sourcecode language="powershell"] # import Group Policy Module
Import-Module -Name grouppolicy

# First Create the GPOReports Folder
if (Test-Path C:\GPOReports)
{
    "C:\GPOReports Folder already exists exists"
}
else
{
    "C:\GPOReports  does not exist, create it"
     New-Item C:\GPOReports -type directory -Force
}

# now generate the reports
$path = "C:\GPOReports"
get-gpo -All | ForEach-Object {
write-host "Generating GPO Report for:"  $($_.displayname)

Get-GPOReport -Name $_.displayname -ReportType HTML -Path (join-path -Path $path -ChildPath "$($_.displayname).HTML")
}

displayname -ReportType HTML -Path (join-path -Path $path -ChildPath "$($_.displayname).HTML")
  } 

 [/sourcecode]

The second script I put together simply lists all GPOs that exist in the domain and generates an HTML report.

# **GenerateGroupPolicySummaryReport.ps1**

[sourcecode language="powershell"] # import Group Policy Module
Import-Module -Name grouppolicy

# First Create the GPOReports Folder
if (Test-Path C:\GPOReports)
{
    "C:\GPOReports Folder already exists exists"
}
else
{
    "C:\GPOReports  does not exist, create it"
     New-Item C:\GPOReports -type directory -Force
}

# now generate the summary report

$a = "<style>"

$a = $a + "body    { background-color:#FFFFFF; border:0px solid #666666; color:#000000; font-size:68%; font-family:MS Shell Dlg; margin:0,0,10px,0; word-break:normal; word-wrap:break-word; }"

$a = $a + "table   { background-color:#E8E8E8; font-size:100%; table-layout:fixed; width:100%; }"

$a = $a + "H1  { background-color:#FEF7D6; border:1px solid #BBBBBB; color:#3333CC; cursor:hand; display:block; font-family:MS Shell Dlg; font-size:100%; font-weight:bold; height:2.25em; margin-bottom:-1px; margin-left:0px; margin-right:0px; padding-left:8px; padding-right:5em; padding-top:4px; position:relative; width:100%; }"

$a = $a + "td,th  { overflow:visible; text-align:left; vertical-align:top; white-space:normal; }"

$a = $a +".title  { background:#FFFFFF; border:none; color:#333333; display:block; height:24px; margin:0px,0px,-1px,0px; padding-top:4px; position:relative; table-layout:fixed; width:100%; z-index:5; }"
$a = $a + "</style>"

get-gpo -all | Select-object Displayname,GpoStatus, Description,CreationTime, ModificationTime | ConvertTo-HTML  -head $a -body "<H1> All Group Policies.</H1>  " | Out-file C:\GPOReports\GPOSummary.html

[/sourcecode]

The output of the above script looks as following.

[
![gporeport](images/gporeport_thumb15.png)
](https://www.verboon.info/wp-content/uploads/2010/10/gporeport15.png)