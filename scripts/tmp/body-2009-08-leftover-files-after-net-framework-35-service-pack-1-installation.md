Some of you might have noticed that after installing the .NET Framework 3.5 Service Pack 1, there can be a leftover folder in the root of the system as shown in the picture below.

[
![image](images/image-thumb.png)
](https://www.verboon.info/wp-content/uploads/2009/08/image.png)

We identified this issue right after .NET 3.5 SP1 was installed,  and found out soon that we were not the only ones having this issue. Microsoft describes this behavior in [KB951847](http://support.microsoft.com/default.aspx/kb/951847/en-us) and confirms the folder can be deleted.

*After you install the .NET Framework 3.5 SP1 in Windows XP or Windows Server 2003, there is an arbitrary folder that is generated in the root of drive C. This folder contains two subfolders that are named amd64 and i386. These two subfolders both include the following files: *

*Filterpipelineprintproc.dll
Msxpsdrv.cat
Msxpsdrv.inf
Msxpsinc.gpd
Msxpsinc.ppd
Mxdwdrv.dll
Xpssvcs.dll*

*These files were pending to be deleted from the XPSEPSC installation.*

But deleting that folder doesn’t appear to be so easy. When trying to delete the folder, you get the following error message:

[
![image](images/image-thumb1.png)
](https://www.verboon.info/wp-content/uploads/2009/08/image1.png)

When taking a closer look, you will notice that the folder as special permissions set, so the only way to get rid of this folder is to first take ownership of the content and then delete the folder. When working in an enterprise environment where we are used to automate things, manual steps are not an option, things must run in an automated way.

So we created a script. Since the folder names used by the windows update process are created randomly, we first need to identify the folder name. This is done by simply searching for the file mxdwdrv.dll that is not located in the Windows folder. Once we have identified the random folder name we need to take ownership of the folder before deleting it. We use the [SubInACL](http://www.microsoft.com/downloads/details.aspx?FamilyID=E8BA3E56-D8FE-4A91-93CF-ED6985E3927B&displaylang=en) resource kit utility from Microsoft to take ownership of the folder. Finally we can delete the folder.

Note that the below script will only work if the system was rebooted after the .NET Framework 3.5 SP1 installation.

**dotnet35leftoverfix.vbs**

[sourcecode language="vb"]
' dotnet35leftoverfix.vbs
' version 1.0
' 03.08.2009
The script expects SubInACL.exe to be present within the same folder as the script itself. </span>
Dim WshShell : SET WshShell = CreateObject("WScript.Shell")
Dim oFSO : SET oFSO = CreateObject("Scripting.FileSystemObject")
'Find where mxdwdrv.dll is located other than c:\windows
Dim colFSOSubFolders
'On Error Resume Next
Set oFolder = oFSO.GetFolder("C:\")
Set colFSOSubfolders = oFolder.Subfolders
For Each objSubfolder in colFSOSubfolders
'if its found it in WINDOWS then ignore it
if ucase(objSubfolder.Name) <> "WINDOWS" then
    if oFSO.FileExists("C:\" & objSubfolder.Name & "\i386\mxdwdrv.dll") then
        'ok this subfolder name is what I need to go after
        cmdline = fcurdir & "subinacl /subdirectories " & objSubfolder & "\*.* /setowner=Administrator /grant=Administrator=F"
        msgbox cmdline
        wshshell.run cmdline , ,true
        oFSO.DeleteFolder(objSubfolder)
    end if
end if
Next
function fCurDir()
set o=CreateObject("Scripting.FileSystemObject")
set of=o.GetFile(WScript.ScriptFullName)
fCurDir=of.ParentFolder&"\"
set of=Nothing
set o=Nothing
end function
[/sourcecode]

// <![CDATA[
	(function(){
		var corecss = document.createElement('link');
		var themecss = document.createElement('link');
		var corecssurl = "https://www.verboon.info/wp-content/plugins/syntaxhighlighter/syntaxhighlighter/styles/shCore.css?ver=2.1.364b";
		if ( corecss.setAttribute ) {
				corecss.setAttribute( "rel", "stylesheet" );
				corecss.setAttribute( "type", "text/css" );
				corecss.setAttribute( "href", corecssurl );
		} else {
				corecss.rel = "stylesheet";
				corecss.href = corecssurl;
		}
		document.getElementsByTagName("head")[0].appendChild(corecss);
		var themecssurl = "https://www.verboon.info/wp-content/plugins/syntaxhighlighter/syntaxhighlighter/styles/shThemeDefault.css?ver=2.1.364b";
		if ( themecss.setAttribute ) {
				themecss.setAttribute( "rel", "stylesheet" );
				themecss.setAttribute( "type", "text/css" );
				themecss.setAttribute( "href", themecssurl );
		} else {
				themecss.rel = "stylesheet";
				themecss.href = themecssurl;
		}
		document.getElementsByTagName("head")[0].appendChild(themecss);
	})();
	SyntaxHighlighter.config.clipboardSwf = 'https://www.verboon.info/wp-content/plugins/syntaxhighlighter/syntaxhighlighter/scripts/clipboard.swf';
	SyntaxHighlighter.config.strings.expandSource = 'show source';
	SyntaxHighlighter.config.strings.viewSource = 'view source';
	SyntaxHighlighter.config.strings.copyToClipboard = 'copy to clipboard';
	SyntaxHighlighter.config.strings.copyToClipboardConfirmation = 'The code is in your clipboard now';
	SyntaxHighlighter.config.strings.print = 'print';
	SyntaxHighlighter.config.strings.help = '?';
	SyntaxHighlighter.config.strings.alert = 'SyntaxHighlighter\n\n';
	SyntaxHighlighter.config.strings.noBrush = 'Can\'t find brush for: ';
	SyntaxHighlighter.config.strings.brushNotHtmlScript = 'Brush wasn\'t configured for html-script option: ';
	SyntaxHighlighter.all();
// ]]>

This script is provided "as is".  The author offers no warranty or guarantee of any kind. Use of this script is at your own risk. The author takes no responsibility for loss of data.

**UPDATE 27. October 2009**

If you are working in an enterprise environment and want to get rid of the folder in an automated way on many systems, the above script might be of use for you. If you are a HOME user and have no scripting skills, I recommend you use one of the manual based solutions below. Thanks to all those that have contributed to this article.