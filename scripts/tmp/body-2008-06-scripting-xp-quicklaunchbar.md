I posted this a couple of years ago into the MyITforum site and received plenty of replies on this, as at that stage it was an unknown trick. Below the trick how to enable the Windows XP quicklaunch bar by using a registry hack.

copy the reg key
"HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Streams\Desktop\Default Taskbar"
to:
"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Streams\Desktop\Taskbar"
(for XP RTM)
"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Streams\Desktop\TaskbarWinXP"
(for XP SP1) (to be safe copy it to both locations)