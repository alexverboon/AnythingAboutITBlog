On Windows 7 many users suffer from disappearing shortcuts on their desktop. I wrote about this in [Control Windows 7 Scheduled Maintenance Behavior Through Group Policy](https://www.verboon.info/index.php/2010/11/control-windows-7-scheduled-maintenance-behavior-through-group-policy/). On Windows 8 this shouldn’t happen anymore, since Microsoft has removed the related scripts and Tasks from the Diagnosis troubleshooting pack (DiagPackage.diagpkg)

  The following files have been removed from the C:\Windows\diagnostics\scheduled\Maintenance folder:

     
- RS_RemoveShortcuts.ps1    
- RS_RemoveUnusedDesktopIcons.ps1    
- TS_BrokenShortcuts.ps1    
- TS_UnusedDesktopIcons.ps1