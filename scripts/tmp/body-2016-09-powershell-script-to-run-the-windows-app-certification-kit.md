The Windows App Certification Kit is an easy to use tool to check whether an application has potential compatibility issues when running on Windows 10.  The tool can be executed in GUI mode and in command line mode. I wrote a PowerShell script that runs the Windows App Certification Kit in a more or less automated way.

 I say more or less, because the application installation process of the application itself might still prompt for input. Also the final report generation of the App Cert Tool itself requires manual interaction that i was unable to suppress. , Nevertheless I hope you find the script useful and saves you a bit of time when testing applications. 

```

```

Before you run the script, you must install the Windows App Certification Kit which you can download from here:[https://developer.microsoft.com/en-us/windows/develop/app-certification-kit](https://developer.microsoft.com/en-us/windows/develop/app-certification-kit)

The script creates a folder **AppCertReports** within the **MyDocuments** folder and stores the report results in there. If you want to look at the reports on a computer that does not have the Windows App Certification Kit installed, copy the following files to that computer.

"C:\ProgramData\Windows App Certification Kit\wslk_strings.xml"
"C:\ProgramData\Windows App Certification Kit\results.xsl"
"C:\ProgramData\Windows App Certification Kit\wp-results.xsl"

### Additional Information

- Certification requirements for Windows Desktop Apps: [https://msdn.microsoft.com/en-us/library/mt674655(v=vs.85).aspx](https://msdn.microsoft.com/en-us/library/mt674655(v=vs.85).aspx) 

- Windows 10 App Compat Strategy: [https://blogs.msdn.microsoft.com/cjacks/2016/09/12/windows-10-app-compat-strategy/](https://blogs.msdn.microsoft.com/cjacks/2016/09/12/windows-10-app-compat-strategy/)